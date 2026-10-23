@echo off
rem One-click market temperature: fetch -> compute -> render -> open the dashboard.
rem Extra args pass through, e.g.  run_market_temp.bat --no-fetch   or   run_market_temp.bat --pdf
chcp 65001 >nul
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8
echo [market_temp] fetching data and computing gauges ...
python scripts\market_temp\run.py %*
if errorlevel 1 (
  echo.
  echo [market_temp] run FAILED - see output\market_temp\^<date^>\run_log.txt
  pause
  exit /b 1
)
set /p LATEST=<output\market_temp\LATEST.txt
echo [market_temp] done -> output\market_temp\%LATEST%\
start "" "output\market_temp\%LATEST%\dashboard.png"
start "" "output\market_temp\%LATEST%\temp.md"
timeout /t 8 >nul
