#!/bin/bash

# ANSI color codes
BLUE='\033[0;34m'
NC='\033[0m'  # No Color

# Make sure the script is running as root
if [ "$(id -u)" != "0" ]; then
    echo -e "${BLUE}This script must be run as root.${NC}"
    exit 1
fi

# Kill existing screens
screen -X -S web_session kill
screen -X -S update_session kill

# Update package list
apt update

# Install pip for Python 3
apt install -y python3-pip

# Verify installation
pip --version

# Display a message indicating successful installation
echo -e "${BLUE}pip for Python 3 has been successfully installed.${NC}"

# Check if xVpn directory exists and delete it
if [ -d "xVpn" ]; then
    echo -e "${BLUE}Deleting existing xVpn directory...${NC}"
    rm -rf xVpn
fi

# Clone the repository
git clone https://github.com/xshelll/xVpn.git

# Change to the project directory
cd xVpn

# Install dependencies from requirements.txt
pip install -r requirements.txt --break-system-packages
pip install -r requirements.txt

# Change permissions
chmod +x xray-knife

# Run the web.py script in a detached screen session
screen -dmS web_session python3 web.py

echo -e "${BLUE}web.py script is running in a 'web_session' screen session.${NC}"

# Run the update.py script in another detached screen session
screen -dmS update_session python3 update.py

echo -e "${BLUE}update.py script is running in an 'update_session' screen session.${NC}"

echo -e "${BLUE}Script execution complete.${NC}"
