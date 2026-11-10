@echo off
rem Copy the public-domain Minckley PDFs to C:\Obsidian\Fish_Science_Brain\MinckleyLibrary_PublicDomain as <MID>.pdf
rem (manifest ftp_manifest.csv in that folder). Resumable: run again to continue. The library folder is not changed.
rem Counts first: python -m utils.minckley_public plan
cd /d "%~dp0"
set PYTHONUTF8=1
set "PY=python"
where python >nul 2>nul || set "PY=py -3"
%PY% -m utils.minckley_public copy %*
pause
