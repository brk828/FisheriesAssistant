@echo off
rem Re-run the public-domain review for Marsh documents re-OCRd on 2026-11-09/10 (Anthropic Batches API, 50% price).
rem Shows an estimate and asks first. Resumable: run again if the window closes. Results: python -m utils.marsh_rereview status
cd /d "%~dp0"
set PYTHONUTF8=1
set "PY=python"
where python >nul 2>nul || set "PY=py -3"
%PY% -m utils.marsh_rereview run %*
pause
