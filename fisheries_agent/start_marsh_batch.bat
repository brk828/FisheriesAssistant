@echo off
rem Marsh Library ingest through the Anthropic Batches API (half price). Close the Agent and Batch windows first.
rem   start_marsh_batch.bat        every pending Marsh Library PDF (assigns PML codes to new files first)
rem   start_marsh_batch.bat 10     a test run of 10 documents spread across the library
rem Rerun the same way to resume after a reboot or a closed window.
rem   python -m utils.marsh_ingest status    progress;   python -m utils.marsh_ingest report --run    permission decisions
cd /d "%~dp0"
set PYTHONUTF8=1
set "PY=python"
where python >nul 2>nul || set "PY=py -3"
if "%~1"=="" (
    %PY% -m utils.marsh_ingest
) else (
    %PY% -m utils.marsh_ingest --size %1 --order spread
)
pause
