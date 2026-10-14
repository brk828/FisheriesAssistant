@echo off
rem One-step batch processing: tab 1 = agent (answers the ingest prompt), tab 2 = Minckley batch feeder.
cd /d "%~dp0"

set "PY=python"
where python >nul 2>nul || set "PY=py -3"

set "AGENT=$env:PYTHONUTF8=1; %PY% start.py"
set "BATCH=$env:PYTHONUTF8=1; %PY% -m utils.minckley_batch"

where wt >nul 2>nul
if %errorlevel%==0 (
    wt -d "%CD%" --title "Agent" powershell -NoExit -Command "%AGENT%" ; new-tab -d "%CD%" --title "Batch" powershell -NoExit -Command "%BATCH%"
) else (
    start "Agent" powershell -NoExit -Command "Set-Location -LiteralPath '%CD%'; %AGENT%"
    start "Batch" powershell -NoExit -Command "Set-Location -LiteralPath '%CD%'; %BATCH%"
)
