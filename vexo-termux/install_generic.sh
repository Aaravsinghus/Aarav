#!/usr/bin/env bash
set -e

echo ""
echo "=============================="
echo "   Vexo Bot - Generic Linux Setup"
echo "=============================="
echo ""

echo "[1/4] Updating packages..."
sudo apt update && sudo apt upgrade -y

echo "[2/4] Installing dependencies..."
sudo apt install -y python3 python3-venv python3-pip git

echo "[3/4] Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel

echo "[4/4] Installing bot package..."
pip install -e .

echo ""
echo "Setup complete!"
echo "Copy config.env.example to config.env and add your bot token."
echo "Then run:" 
 echo "  source venv/bin/activate"
echo "  vexo-setup"
echo "  vexo main"
