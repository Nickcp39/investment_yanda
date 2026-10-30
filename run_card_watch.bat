@echo off
rem One-click card price watch: every latest decision_card vs today's price -> which cards need a re-run.
rem Extra args pass through, e.g.  run_card_watch.bat --no-fetch
chcp 65001 >nul
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8
echo [card_watch] reading cards and fetching prices (about 1-2 minutes) ...
python scripts\card_watch\card_watch.py %*
if errorlevel 1 (
  echo.
  echo [card_watch] run FAILED
  pause
  exit /b 1
)
for /f %%f in ('dir /b /o-d scripts\card_watch\out\card_watch_*.md') do (
  start "" "scripts\card_watch\out\%%f"
  goto :done
)
:done
timeout /t 8 >nul
