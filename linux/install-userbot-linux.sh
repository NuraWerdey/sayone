#!/bin/bash

chmod +x install-userbot-linux.sh

clear

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}=== SayOne UserBot Installer (Linux/macOS) ===${NC}"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR] Python3 is not installed!${NC}"
    echo -e "Install Python3:"
    echo -e "Debian/Ubuntu: ${GREEN}sudo apt install python3${NC}"
    echo -e "macOS: ${GREEN}brew install python${NC}"
    exit 1
fi

# Check Git
if ! command -v git &> /dev/null; then
    echo -e "${RED}[ERROR] Git is not installed!${NC}"
    echo -e "Install Git:"
    echo -e "Debian/Ubuntu: ${GREEN}sudo apt install git${NC}"
    echo -e "macOS: ${GREEN}brew install git${NC}"
    exit 1
fi

# Settings
REPO_URL="https://github.com/nurawerdey/.git"
FOLDER_NAME="SayOne"

echo -e "\n${GREEN}[1/4] Cloning repository...${NC}"
git clone "$REPO_URL" "$FOLDER_NAME"
cd "$FOLDER_NAME" || exit

echo -e "\n${GREEN}[2/4] Installing dependencies...${NC}"
pip3 install -r requirements.txt

echo -e "\n${GREEN}[3/4] Creating config.py...${NC}"
cat > config.py << EOF
API_ID = 12345
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"  # Optional
EOF

echo -e "\n${GREEN}[4/4] Starting UserBot...${NC}"
python3 main.py
