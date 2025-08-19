#!/bin/bash

# Woodstone Festival 2025 - Admin Portal Setup Script
# This script automates the extraction, setup, and running of the Flask admin portal

set -e  # Exit on any error

echo "🌌 Woodstone Festival 2025 - Admin Portal Setup"
echo "================================================"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 is not installed or not in PATH"
    echo "   Please install Python 3 before running this script"
    exit 1
fi

# Check if the tar.gz file exists
TAR_FILE="woodstone_festival_2025_euystacio_warp_full_ready_admin.tar.gz"
if [ ! -f "$TAR_FILE" ]; then
    echo "❌ Error: $TAR_FILE not found in current directory"
    echo "   Please ensure the admin archive is in the same directory as this script"
    exit 1
fi

echo "✅ Found $TAR_FILE"

# Step 1: Extract the archive
echo ""
echo "📦 Step 1: Extracting the admin portal..."
tar -xzf "$TAR_FILE"
echo "✅ Archive extracted successfully"

# Step 2: Change into the extracted directory
EXTRACTED_DIR="woodstone_festival_2025_euystacio_warp"
if [ ! -d "$EXTRACTED_DIR" ]; then
    echo "❌ Error: Expected directory $EXTRACTED_DIR not found after extraction"
    exit 1
fi

cd "$EXTRACTED_DIR"
echo "✅ Changed to directory: $EXTRACTED_DIR"

# Step 3: Create and activate Python virtual environment
echo ""
echo "🐍 Step 3: Setting up Python virtual environment..."
python3 -m venv venv

# Activation command varies by platform
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
    echo "✅ Virtual environment activated (Linux/macOS)"
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
    echo "✅ Virtual environment activated (Windows)"
else
    echo "❌ Error: Could not find virtual environment activation script"
    exit 1
fi

# Step 4: Install Flask and dependencies
echo ""
echo "📚 Step 4: Installing dependencies..."
pip install --upgrade pip
pip install flask markdown requests werkzeug
echo "✅ Dependencies installed successfully"

# Step 5: Change to app directory and run the application
echo ""
echo "🚀 Step 5: Starting the Flask application..."
cd app

echo ""
echo "🎉 Setup complete! Starting the Woodstone Festival 2025 Admin Portal..."
echo ""
echo "📋 ACCESS INFORMATION:"
echo "   URL: http://localhost:5000/connect"
echo "   Username: woodstone"
echo "   Password: threefold-zes"
echo "   Role: admin"
echo ""
echo "ℹ️  The server will start now. Press Ctrl+C to stop the server."
echo "ℹ️  You can access the portal at the URL above once the server starts."
echo ""

# Run the Flask app
python3 app.py