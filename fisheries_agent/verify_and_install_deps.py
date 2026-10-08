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
        "python-dotenv": ("dotenv", "python-dotenv credential manager")
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
    
    # R environment evaluation safety fallback
    if missing_r is None:
        print(f"\n❌ {RED}CRITICAL:{RESET} Missing foundational R software binaries entirely.")
        sys.exit(1)
        
    print("\n=========================================================")
    
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
            
        print("\n=========================================================")
        print(f"🏁 {GREEN}INSTALLATION ROUTINE COMPLETED.{RESET}")
        print(" Re-run 'python verify_and_install_deps.py' to confirm full verification status.")
        print("=========================================================")
        sys.exit(2)  # installed; needs a fresh process to re-check
    else:
        print(f"\n❌ Installation aborted. Please resolve dependencies manually before continuing.")
        print("=========================================================")
        sys.exit(1)
