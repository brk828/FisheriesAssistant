@echo off
rem Rebuild source notes from their saved full text (Anthropic Batches API, 50% price). Shows an estimate and asks first.
rem Default list: runs\reocr\improved.csv. Resumable: if the window closes, run it again to pick up the batch.
rem   start_rebuild_notes.bat                   estimate, ask, send, wait, write the notes
rem   start_rebuild_notes.bat --ids 14702 PML0503
rem Progress: python -m utils.rebuild_notes status
cd /d "%~dp0"
set PYTHONUTF8=1
set "PY=python"
where python >nul 2>nul || set "PY=py -3"
%PY% -m utils.rebuild_notes run %*
pause
