@echo off
rem Unattended Minckley ingest through the Anthropic Batches API (half price). Close the Agent and Batch windows first.
rem   start_batch_api.bat        every remaining public-domain MID
rem   start_batch_api.bat 5      a small test run of the 5 smallest
rem Rerun the same way to resume after a reboot or a closed window; "python -m utils.batch_ingest status" shows progress.
cd /d "%~dp0"
set PYTHONUTF8=1
set "PY=python"
where python >nul 2>nul || set "PY=py -3"
if "%~1"=="" (
    %PY% -m utils.batch_ingest
) else (
    %PY% -m utils.batch_ingest --size %1
)
pause
