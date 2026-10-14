@echo off
rem Batch processing: window 1 = agent (main_orchestrator.py), window 2 = Minckley batch feeder.
rem Skips onboarding; run start.bat once first if project_manifest.yaml or the API key are missing.
cd /d "%~dp0"
set PYTHONUTF8=1

set "PY=python"
where python >nul 2>nul || set "PY=py -3"

if not exist project_manifest.yaml (
    echo project_manifest.yaml not found. Run start.bat once to complete onboarding first.
    pause
    exit /b 1
)

start "Agent" /D "%CD%" cmd /k %PY% main_orchestrator.py
start "Batch" /D "%CD%" cmd /k %PY% -m utils.minckley_batch
