
@echo off
setlocal
cd /d "%~dp0"

echo Starting Workbench API-backed prototype...

where python >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not on PATH.
    pause
    exit /b 1
)


echo Starting backend at http://127.0.0.1:8000
venv\Scripts\python.exe -m uvicorn backend_mvp:app --host 127.0.0.1 --port 8000
goto :eof

:error
echo.
echo ERROR: Setup or startup failed. Review the output above.
pause
exit /b 1