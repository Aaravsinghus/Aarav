#!/data/data/com.termux/files/usr/bin/bash

echo ""
echo "=============================="
echo "   Vexo Bot - Termux Setup"
echo "   Creator: Aarav Singh"
echo "=============================="
echo ""

# Step 1 - Packages
echo "[1/4] Packages install ho rahe hain..."
pkg update -y > /dev/null 2>&1
pkg install -y python git > /dev/null 2>&1
echo "      Done!"

# Step 2 - Virtual env
echo "[2/4] Virtual environment bana raha hai..."
python -m venv venv > /dev/null 2>&1
source venv/bin/activate
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
echo "      Done!"

# Step 3 - Bot install
echo "[3/4] Vexo install ho raha hai (2-3 min lagega)..."
pip install -e . --ignore-requires-python --no-build-isolation
if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Install fail hua. Manually try karo:"
    echo "  pip install -r requirements/base.txt"
    echo "  pip install -e . --ignore-requires-python --no-build-isolation"
    exit 1
fi
echo "      Done!"

# Step 4 - Setup
echo "[4/4] Bot setup ho raha hai..."
TOKEN=$(grep "^BOT_TOKEN=" config.env | cut -d'=' -f2)
PREFIX=$(grep "^PREFIX=" config.env | cut -d'=' -f2)
PREFIX=${PREFIX:-!}

python -c "
import subprocess
proc = subprocess.Popen(['vexo-setup'], stdin=subprocess.PIPE, text=True)
try:
    proc.communicate(input='main\n${TOKEN}\n${PREFIX}\n\n\n\n', timeout=30)
except:
    proc.kill()
" 2>/dev/null

echo ""
echo "=============================="
echo "  Setup complete!"
echo "=============================="
echo ""
echo "Bot start karne ke liye:"
echo ""
echo "  source venv/bin/activate"
echo "  vexo main"
echo ""
