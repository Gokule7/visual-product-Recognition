#!/bin/bash

# Setup script for Visual Product Matcher
# Run this script to set up the entire project

echo "=========================================="
echo "Visual Product Matcher - Setup Script"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "ERROR: Python is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed. Please install Node.js 16 or higher."
    exit 1
fi

echo "✓ Python found: $(python --version)"
echo "✓ Node.js found: $(node --version)"
echo ""

# Setup Backend
echo "Setting up backend..."
cd backend

echo "Creating virtual environment..."
python -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate  # On Windows use: venv\Scripts\activate

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Building feature cache (this may take a few minutes)..."
python build_features.py

echo "✓ Backend setup complete!"
echo ""

# Setup Frontend
echo "Setting up frontend..."
cd ../frontend

echo "Installing npm dependencies..."
npm install

echo "✓ Frontend setup complete!"
echo ""

# Done
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "To start the application:"
echo ""
echo "1. Start the backend (in one terminal):"
echo "   cd backend"
echo "   source venv/bin/activate  # On Windows: venv\\Scripts\\activate"
echo "   python app.py"
echo ""
echo "2. Start the frontend (in another terminal):"
echo "   cd frontend"
echo "   npm run dev"
echo ""
echo "3. Open http://localhost:3000 in your browser"
echo ""
echo "Happy coding! 🚀"
