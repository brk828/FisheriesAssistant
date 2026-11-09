@echo off
rem Re-OCR garbled full texts (local Tesseract only; no LLM, nothing is sent). Resumable: close the window or press
rem Ctrl+C to stop, run again to continue. Below-normal priority; keeps the PC awake while running.
rem   start_reocr.bat                  everything left in runs\reocr\targets.csv
rem   start_reocr.bat --hours 4        stop by itself after 4 hours
rem   start_reocr.bat --workers 6      more documents at once (default half the CPU cores)
rem Afterwards: python -m utils.reocr status, then python -m utils.reocr apply --dry-run
cd /d "%~dp0"
set PYTHONUTF8=1
set "PY=python"
where python >nul 2>nul || set "PY=py -3"
if not exist runs\reocr\targets.csv %PY% -m utils.reocr plan
%PY% -m utils.reocr run %*
pause
