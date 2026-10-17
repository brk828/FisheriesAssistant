import os
import yaml
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENV_DIR = HERE

def print_api_key_instructions():
    env_file = ENV_DIR / ".env"
    print("\n--- 4. OPENROUTER API KEY ---")
    print(" Create a key at https://openrouter.ai/keys (set a credit limit on it), then either:")
    print("  A. Run 'python setup_api_key.py' and paste it (hidden input; it is saved to .env only), or")
    print(f"  B. Edit {env_file} yourself:  OPENROUTER_API_KEY=sk-or-v1-...")
    print(" Keep the key safe:")
    print("  - Only put it in the .env file. Never in the YAML, R scripts, or chat.")
    print("  - Never commit .env to git, email it, or share it.")
    print("  - If a key is ever exposed, revoke it on openrouter.ai and create a new one.")
    print(f" Status: .env {'found' if env_file.exists() else 'not found yet'}.")

WINDOWS_RESERVED_NAMES = {'CON', 'PRN', 'AUX', 'NUL', *(f'COM{i}' for i in range(1, 10)), *(f'LPT{i}' for i in range(1, 10))}


def offer_icm_workspaces(projects):
    """Optional: restructure each selected project into an ICM workspace (the original is never modified)."""
    from utils import icm_integration, icm_restructure
    print("\n--- ICM WORKSPACES (optional) ---")
    print(" An ICM workspace gives a project staged folders, an AGENTS.md and project skills. Originals are never changed.")
    for project in projects:
        if icm_integration.is_workspace(project):
            continue
        if input(f"Create an ICM workspace for '{project.name}' now? (y/N): ").strip().lower() not in ("y", "yes"):
            continue
        try:
            dest = icm_restructure.run(project)
        except (SystemExit, Exception) as e:
            print(f" Skipped '{project.name}': {e}")
            continue
        if dest:
            print(f" Registered {icm_integration.register_workspace(dest, original=project.name)}")


def run_onboarding():
    print("=========================================================")
    print("⚓ FISHERIES AI AGENT FRAMEWORK - MACHINE ONBOARDING ⚓")
    print("=========================================================\n")
    
    # --- STEP 1: INTERVIEW THE USER ---
    print("--- 1. PROJECT DISCOVERY ---")
    r_projects_root = input("Enter the absolute path to your RProjects folder (e.g., C:\\Users\\drsmith\\RProjects): ").strip()
    
    root_path = Path(r_projects_root)
    if not root_path.exists():
        print(f"❌ Error: Path '{r_projects_root}' does not exist. Please restart setup.")
        return

    # List subdirectories to find active projects
    print("\nScanning root directory for projects...")
    available_folders = [d for d in root_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    print("\nFound the following project directories:")
    for idx, folder in enumerate(available_folders, start=1):
        print(f" [{idx}] {folder.name}")
        
    selections = input("\nEnter the numbers of the projects you want the AI Agent to manage (comma-separated, e.g., 1,3): ")
    selected_indices = [int(x.strip()) - 1 for x in selections.split(",") if x.strip().isdigit()]
    
    target_projects = [available_folders[i] for i in selected_indices if 0 <= i < len(available_folders)]
    if not target_projects:
        print("❌ No valid projects selected. Please restart setup.")
        return
    
    # --- STEP 2: PROFILE THE FILE STRUCTURES & HABITS ---
    print("\n--- 2. ANALYZING FILE STRUCTURES & CODING HABITS ---")
    
    manifest_data = {"global_settings": {"r_projects_root": str(root_path)}, "projects": {}}
    
    for project_path in target_projects:
        print(f"\nAnalyzing '{project_path.name}'...")
        
        # Gather file map
        all_files = []
        has_rmd = False
        has_qmd = False
        
        for root, _, files in os.walk(project_path):
            for file in files:
                if file.startswith('.'): continue  # also skips .env files; keys are never read
                if file.split('.')[0].upper() in WINDOWS_RESERVED_NAMES: continue  # e.g. stray 'nul' files
                try:
                    rel_path = os.path.relpath(os.path.join(root, file), project_path)
                except ValueError:
                    continue
                all_files.append(rel_path)
                if file.endswith('.Rmd'): has_rmd = True
                if file.endswith('.qmd'): has_qmd = True

        # Read snippet of an existing R script to try and gauge documentation habits
        documentation_style = "Undetermined (No clean script found)"
        r_scripts = [f for f in all_files if f.endswith('.R')]
        
        if r_scripts:
            try:
                sample_script_path = project_path / r_scripts[0]
                with open(sample_script_path, 'r', errors='ignore') as f:
                    snippet = f.read(1500) # Read first 1500 characters
                
                # Ask a fast local heuristic or keep a placeholder to let OpenRouter process later
                if "roxygen2" in snippet or "#'" in snippet:
                    documentation_style = "Roxygen2 / Formal packages"
                elif "####" in snippet or "----" in snippet:
                    documentation_style = "Section-blocked comments"
                else:
                    documentation_style = "Sparse / Script-inline comments"
            except Exception:
                pass

        # Build context yaml data
        manifest_data["projects"][project_path.name] = {
            "project_path": str(project_path),
            "primary_format": "Quarto (qmd)" if has_qmd else ("RMarkdown (Rmd)" if has_rmd else "Standard R Scripts"),
            "documentation_habit": documentation_style,
            "detected_files": all_files[:30] # Cap the file list length inside the configuration to avoid bloating text
        }
        print(f" -> Style Detected: {documentation_style} using {manifest_data['projects'][project_path.name]['primary_format']}")

    # --- STEP 3: SCAFFOLD INFRASTRUCTURE CONFIGURATIONS ---
    print("\n--- 3. CREATING BACKBONE CONFIGURATION FILES ---")
    
    # Write out YAML infrastructure map
    manifest_file = HERE / "project_manifest.yaml"
    if manifest_file.exists():  # keep existing ICM links when onboarding is re-run
        old = (yaml.safe_load(manifest_file.read_text(encoding="utf-8")) or {}).get("projects", {})
        for name, info in old.items():
            if info.get("icm_workspace"):
                manifest_data["projects"].setdefault(name, {"project_path": info["project_path"]})["icm_workspace"] = info["icm_workspace"]
    with open(manifest_file, "w") as f:
        yaml.dump(manifest_data, f, default_flow_style=False)
    print(f"✅ Generated infrastructure backbone: {manifest_file.resolve()}")

    offer_icm_workspaces(target_projects)
    
    # Write out .env.template if missing
    env_template = ENV_DIR / ".env.template"
    if not env_template.exists():
        with open(env_template, "w") as f:
            f.write("OPENROUTER_API_KEY=your_openrouter_api_key_here\n")
        print("✅ Dropped .env.template")

    print_api_key_instructions()

    print("\n=========================================================")
    print("🎉 ONBOARDING INITIALIZATION SETUP SUCCESSFUL!")
    print(" Next steps for the scientist:")
    print(" 1. Make sure your OpenRouter API key is saved in '.env' (see above).")
    print(" 2. Log in securely from anywhere using Tailscale and SSH.")
    print(" 3. Fire up 'main_orchestrator.py' to direct your workflows.")
    print("=========================================================")

if __name__ == "__main__":
    run_onboarding()
