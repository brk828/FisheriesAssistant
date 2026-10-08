"""One-command start: dependency check, onboarding, API key, then the orchestrator."""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "project_manifest.yaml"


def run(script: str) -> int:
    return subprocess.run([sys.executable, str(HERE / script)], cwd=HERE).returncode


def step_dependencies() -> bool:
    code = run("verify_and_install_deps.py")
    if code == 2:  # packages were just installed; check again in a fresh process
        code = run("verify_and_install_deps.py")
    return code == 0


def step_onboarding() -> bool:
    if MANIFEST.exists():
        answer = input("\nProject setup already exists. Run onboarding again? (y/N): ").strip().lower()
        if answer not in ("y", "yes"):
            return True
    run("setup_onboarding.py")
    return MANIFEST.exists()


def step_api_key() -> bool:
    sys.path.insert(0, str(HERE))
    import setup_api_key
    if setup_api_key.key_is_set():
        return True
    setup_api_key.main()
    return setup_api_key.key_is_set()


def main() -> int:
    if sys.version_info < (3, 10):
        print("Python 3.10 or newer is required.")
        return 1

    if not step_dependencies():
        print("\nStopped: fix the dependency problems above, then run start.bat again.")
        return 1
    if not step_onboarding():
        print("\nStopped: onboarding did not finish, so no project_manifest.yaml was created.")
        return 1
    if not step_api_key():
        print("\nStopped: no API key saved. Add it to .env (or run setup_api_key.py) and run start.bat again.")
        return 1

    print("\nAll set. Starting the orchestrator...\n")
    return run("main_orchestrator.py")


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
