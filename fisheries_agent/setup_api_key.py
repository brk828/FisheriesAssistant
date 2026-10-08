"""Saves the OpenRouter key to .env from hidden input. The key is never echoed, printed or logged."""
import getpass
import os
import re
import subprocess
import sys
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent / ".env"
KEY_NAME = "OPENROUTER_API_KEY"
KEY_PATTERN = re.compile(r"^sk-or-[A-Za-z0-9_\-]{10,}$")
PLACEHOLDER_PREFIX = "your_"


def read_env_lines() -> list:
    return ENV_PATH.read_text(encoding="utf-8").splitlines() if ENV_PATH.exists() else []


def key_is_set() -> bool:
    for line in read_env_lines():
        name, _, value = line.partition("=")
        if name.strip() == KEY_NAME:
            value = value.strip().strip("\"'")
            return bool(value) and not value.startswith(PLACEHOLDER_PREFIX)
    return False


def write_key(key: str) -> None:
    """Replaces or appends the key line, keeping every other setting (e.g. OPENROUTER_MODEL)."""
    lines = [l for l in read_env_lines() if l.partition("=")[0].strip() != KEY_NAME]
    lines.append(f"{KEY_NAME}={key}")
    tmp = ENV_PATH.with_suffix(".tmp")
    tmp.write_text("\n".join(lines) + "\n", encoding="utf-8")
    os.replace(tmp, ENV_PATH)


def restrict_to_current_user() -> bool:
    """Windows only: drop inherited permissions so only this account can read .env."""
    user = os.environ.get("USERNAME")
    if os.name != "nt" or not user:
        return False
    result = subprocess.run(
        ["icacls", str(ENV_PATH), "/inheritance:r", "/grant:r", f"{user}:F"],
        capture_output=True, text=True,
    )
    return result.returncode == 0


def main() -> int:
    if not sys.stdin.isatty():
        print("Hidden input is not available in this session. Edit .env yourself:")
        print(f"  {ENV_PATH}\n  {KEY_NAME}=sk-or-v1-...")
        return 1

    if key_is_set():
        if input("An API key is already saved in .env. Replace it? (y/N): ").strip().lower() not in ("y", "yes"):
            return 0

    print("\n--- OPENROUTER API KEY ---")
    print("1. Create a key at https://openrouter.ai/keys and set a credit limit on it.")
    print("2. Paste it below and press Enter. Nothing appears on screen while you paste; that is expected.")
    print("   (Windows Terminal: Ctrl+V or right-click. Classic console: right-click.)")
    print("3. Leave it blank to skip and edit .env by hand instead.")

    for _ in range(3):
        key = getpass.getpass("OpenRouter API key (hidden): ").strip().strip("\"'")
        if not key:
            print("Skipped. Add the key to .env yourself before starting the orchestrator.")
            return 1
        if KEY_PATTERN.match(key):
            write_key(key)
            print("Saved to .env. The key was not displayed or logged.")
            if restrict_to_current_user():
                print("File access restricted to your Windows account.")
            return 0
        print("That does not look like an OpenRouter key (it should start with 'sk-or-'). Try again.")

    print("No valid key entered.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
