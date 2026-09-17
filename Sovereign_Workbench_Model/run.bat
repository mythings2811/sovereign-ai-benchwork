@echo off
setlocal
cd /d "%~dp0"
if "%WORKBENCH_HOST%"=="" set WORKBENCH_HOST=127.0.0.1
if "%WORKBENCH_PORT%"=="" set WORKBENCH_PORT=8010
if not exist .venv\Scripts\python.exe (
    echo Create the environment first: py -m venv .venv
    exit /b 1
)
.venv\Scripts\python.exe -m uvicorn workbench_model.api:app --host %WORKBENCH_HOST% --port %WORKBENCH_PORT%
