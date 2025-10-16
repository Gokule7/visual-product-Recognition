@echo off
REM Setup script for Visual Product Matcher (Windows)
REM Run this script to set up the entire project

echo ==========================================
echo Visual Product Matcher - Setup Script
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed. Please install Python 3.8 or higher.
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed. Please install Node.js 16 or higher.
    exit /b 1
)

python --version
node --version
echo.

REM Setup Backend
echo Setting up backend...
cd backend

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing Python dependencies...
pip install -r requirements.txt

echo Building feature cache (this may take a few minutes)...
python build_features.py

echo Backend setup complete!
echo.

REM Setup Frontend
echo Setting up frontend...
cd ..\frontend

echo Installing npm dependencies...
call npm install

echo Frontend setup complete!
echo.

REM Done
cd ..
echo ==========================================
echo Setup Complete!
echo ==========================================
echo.
echo To start the application:
echo.
echo 1. Start the backend (in one terminal):
echo    cd backend
echo    venv\Scripts\activate
echo    python app.py
echo.
echo 2. Start the frontend (in another terminal):
echo    cd frontend
echo    npm run dev
echo.
echo 3. Open http://localhost:3000 in your browser
echo.
echo Happy coding! 🚀
pause
