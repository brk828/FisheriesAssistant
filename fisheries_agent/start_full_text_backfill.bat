@echo off
rem Backfill the local full text of Minckley Library PDFs (text extraction and OCR only; no LLM, nothing is sent).
rem Runs at below-normal priority and keeps the PC awake. Close the window or press Ctrl+C to stop; run again to continue.
rem   start_full_text_backfill.bat                 everything left
rem   start_full_text_backfill.bat --hours 10      stop by itself after 10 hours
rem   start_full_text_backfill.bat --workers 6     more documents OCRd at once (default half the CPU cores)
rem Progress: python -m utils.full_text_backfill status
cd /d "%~dp0"
set PYTHONUTF8=1
set "PY=python"
where python >nul 2>nul || set "PY=py -3"
%PY% -m utils.full_text_backfill run %*
pause
