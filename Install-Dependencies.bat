@echo off
echo Installing required Python packages...
pip install requests beautifulsoup4 lxml
if %errorlevel% neq 0 (
    echo There was an error installing the required packages.
    pause
    exit /b %errorlevel%
)
echo Installation complete.
pause