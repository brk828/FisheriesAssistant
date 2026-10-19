import os
import sys
import shutil
import subprocess
from pathlib import Path

# Color formatting for clean terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def check_python_dependencies():
    """Checks for required Python modules and aggregates missing ones."""
    print("🐍 Checking Python Environment...")
    missing_py = []
    
    # Python Version Check (Expect 3.10+)
    version = sys.version_info
    if version.major == 3 and version.minor >= 10:
        print(f"  [{GREEN}PASS{RESET}] Python version: {version.major}.{version.minor}.{version.micro}")
    else:
        print(f"  [{YELLOW}WARN{RESET}] Python version: {version.major}.{version.minor}.{version.micro} (Recommended: 3.10+)")

    # Dictionary mapping pip install handles to python import tokens
    required_modules = {
        "openai": ("openai", "OpenRouter API communication layer"),
        "pyyaml": ("yaml", "PyYAML framework manifest reader"),
        "pypdf": ("pypdf", "PyPDF background literature text extractor"),
        "pdf2image": ("pdf2image", "PDF page rasterizer for OCR (needs Poppler)"),
        "pytesseract": ("pytesseract", "OCR for scanned PDFs (needs Tesseract)"),
        "python-dotenv": ("dotenv", "python-dotenv credential manager"),
        "python-docx": ("docx", "Word (.docx) reader/writer for manuscripts")
    }
    
    for pip_handle, (import_name, purpose) in required_modules.items():
        try:
            if import_name == "yaml":
                import yaml
            elif import_name == "dotenv":
                import dotenv
            else:
                __import__(import_name)
            print(f"  [{GREEN}PASS{RESET}] Module '{import_name}' is installed. ({purpose})")
        except ImportError:
            print(f"  [{RED}FAIL{RESET}] Module '{import_name}' is MISSING! ({purpose})")
            missing_py.append(pip_handle)
            
    return missing_py

def check_r_dependencies():
    """Checks for R binary availability and aggregates missing fisheries packages."""
    print("\n📊 Checking R Statistical Environment...")
    missing_r = []
    
    rscript_path = shutil.which("Rscript")
    if not rscript_path:
        print(f"  [{RED}FAIL{RESET}] 'Rscript' executable not found in system PATH.")
        print("         Please install R manually before running this tool.")
        return None
        
    print(f"  [{GREEN}PASS{RESET}] 'Rscript' binary found at: {rscript_path}")
    
    required_r_packages = {
        "glmmTMB": "Zero-inflated count regression model engine",
        "nimble": "Bayesian mark-recapture / MCMC simulation array processor",
        "vegan": "Ecological ordination suite (PCA, MDS, cluster trees)",
        "ggplot2": "Data exploration and multivariate graphics library"
    }
    
    for package, purpose in required_r_packages.items():
        # Command checks if library loads cleanly
        cmd = ["Rscript", "--vanilla", "-e", f"suppressPackageStartupMessages(library({package}))"]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"  [{GREEN}PASS{RESET}] R Package '{package}' is installed. ({purpose})")
            else:
                print(f"  [{RED}FAIL{RESET}] R Package '{package}' is MISSING! ({purpose})")
                missing_r.append(package)
        except Exception as e:
            print(f"  [{RED}FAIL{RESET}] Failed to run R verification hook for '{package}': {str(e)}")
            missing_r.append(package)
            
    return missing_r

def check_system_dependencies():
    """Tesseract (OCR) and Poppler (PDF page images) are needed only for scanned PDFs, so a miss is a warning, not a stop."""
    print("\n📄 Checking PDF OCR tools (used by utils/pdf_ingest.py for scanned PDFs)...")
    from utils.pdf_ingest import find_poppler, find_tesseract
    missing = []
    exe = find_tesseract()
    if exe:
        print(f"  [{GREEN}PASS{RESET}] Tesseract OCR found at: {exe}")
    else:
        print(f"  [{YELLOW}WARN{RESET}] Tesseract OCR is MISSING! (reads scanned PDF pages)")
        missing.append("tesseract")
    if find_poppler()[0]:
        print(f"  [{GREEN}PASS{RESET}] Poppler (pdftoppm) found.")
    else:
        print(f"  [{YELLOW}WARN{RESET}] Poppler is MISSING! (turns PDF pages into images for OCR)")
        missing.append("poppler")
    return missing

# package names per installer: (winget id, brew formula, apt package)
SYSTEM_PACKAGES = {
    "tesseract": ("UB-Mannheim.TesseractOCR", "tesseract", "tesseract-ocr"),
    "poppler": ("oschwartz10612.Poppler", "poppler", "poppler-utils"),
}

def install_system_packages(missing):
    """Installs OCR tools with the platform's package manager (winget, Homebrew or apt)."""
    print(f"\n⚡ Installing OCR tools: {missing}...")
    if sys.platform == "win32" and shutil.which("winget"):
        cmds = [["winget", "install", "-e", "--id", SYSTEM_PACKAGES[m][0], "--accept-package-agreements", "--accept-source-agreements"] for m in missing]
    elif sys.platform == "darwin" and shutil.which("brew"):
        cmds = [["brew", "install", SYSTEM_PACKAGES[m][1]] for m in missing]
    elif shutil.which("apt-get"):
        prefix = [] if hasattr(os, "geteuid") and os.geteuid() == 0 else ["sudo"]
        cmds = [prefix + ["apt-get", "install", "-y"] + [SYSTEM_PACKAGES[m][2] for m in missing]]
    else:
        print(f"  [{RED}ERROR{RESET}] No supported package manager found (winget, brew, apt-get).")
        print("         Install manually: Tesseract (github.com/UB-Mannheim/tesseract/wiki) and Poppler (github.com/oschwartz10612/poppler-windows).")
        return
    for cmd in cmds:
        try:
            subprocess.run(cmd, check=True)
            print(f"  [{GREEN}SUCCESS{RESET}] {' '.join(cmd)}")
        except (subprocess.CalledProcessError, OSError) as e:
            print(f"  [{RED}ERROR{RESET}] Failed: {' '.join(cmd)} ({e})")
    print("         If a tool is still reported missing, open a new terminal so PATH refreshes, or set TESSERACT_CMD / POPPLER_PATH in .env.")

def install_python_packages(packages):
    """Programmatically installs missing pip packages."""
    print(f"\n⚡ Installing missing Python packages: {packages}...")
    for pkg in packages:
        try:
            # Use sys.executable to ensure installation targets the current environment
            subprocess.run([sys.executable, "-m", "pip", "install", pkg], check=True)
            print(f"  [{GREEN}SUCCESS{RESET}] Installed Python package: {pkg}")
        except subprocess.CalledProcessError:
            print(f"  [{RED}ERROR{RESET}] Failed to install Python package: {pkg}")

def install_r_packages(packages):
    """Programmatically installs R packages via a safe, non-interactive mirror link."""
    print(f"\n⚡ Installing missing R packages: {packages}...")
    # Formulate vector syntax for multi-package install
    packages_str = ", ".join([f"'{p}'" for p in packages])
    
    # repos='https://cloud.r-project.org' prevents interactive mirror selection popups
    r_command = f"install.packages(c({packages_str}), repos='https://cloud.r-project.org')"
    
    try:
        subprocess.run(["Rscript", "-e", r_command], check=True)
        print(f"  [{GREEN}SUCCESS{RESET}] Process completed for R packages: {packages}")
    except subprocess.CalledProcessError:
        print(f"  [{RED}ERROR{RESET}] Failed to execute R package installations.")

if __name__ == "__main__":
    print("=========================================================")
    print("⚓ FISHERIES AI AGENT FRAMEWORK - HEALTH & UTILITY CHECK ⚓")
    print("=========================================================\n")
    
    missing_py = check_python_dependencies()
    missing_r = check_r_dependencies()
    missing_sys = check_system_dependencies() if not missing_py else []
    
    # R environment evaluation safety fallback
    if missing_r is None:
        print(f"\n❌ {RED}CRITICAL:{RESET} Missing foundational R software binaries entirely.")
        sys.exit(1)
        
    print("\n=========================================================")
    
    if missing_sys and not missing_py and not missing_r:
        print(f"⚠️ {YELLOW}Optional:{RESET} {missing_sys} not found. Only scanned PDFs need them; text-based PDFs and everything else work without.")
        if input("Install them now? (y/n): ").strip().lower() in ["y", "yes"]:
            install_system_packages(missing_sys)
            print(" Re-run 'python verify_and_install_deps.py' to confirm.")
            sys.exit(2)
    if not missing_py and not missing_r:
        print(f"🎉 {GREEN}HEALTH CHECK PASSED!{RESET} Your environment is fully configured.")
        print(" Next: run 'start.bat' (or 'python start.py') to continue setup.")
        print("=========================================================")
        sys.exit(0)
        
    # Aggregate and notify regarding deficiencies
    print(f"⚠️ {YELLOW}ATTENTION:{RESET} Found missing environment dependencies.")
    if missing_py:
        print(f"  • Missing Python components: {missing_py}")
    if missing_r:
        print(f"  • Missing R analytical libraries: {missing_r}")
        
    user_choice = input("\nWould you like the framework utility to automatically install these dependencies now? (y/n): ").strip().lower()
    
    if user_choice in ['y', 'yes']:
        if missing_py:
            install_python_packages(missing_py)
        if missing_r:
            install_r_packages(missing_r)
        if missing_sys:
            install_system_packages(missing_sys)
            
        print("\n=========================================================")
        print(f"🏁 {GREEN}INSTALLATION ROUTINE COMPLETED.{RESET}")
        print(" Re-run 'python verify_and_install_deps.py' to confirm full verification status.")
        print("=========================================================")
        sys.exit(2)  # installed; needs a fresh process to re-check
    else:
        print(f"\n❌ Installation aborted. Please resolve dependencies manually before continuing.")
        print("=========================================================")
        sys.exit(1)
