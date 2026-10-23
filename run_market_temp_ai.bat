@echo off
rem Same as run_market_temp.bat, then calls Claude Code headless (claude -p, model sonnet, budget 3 USD)
rem to write ai_notes.md: why the market moved in the last two weeks, fill the stale data items, read the numbers.
chcp 65001 >nul
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8
echo [market_temp] fetching data, computing gauges, then AI notes (this part costs a few dollars) ...
python scripts\market_temp\run.py --ai %*
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
start "" "output\market_temp\%LATEST%\ai_notes.md"
timeout /t 8 >nul
