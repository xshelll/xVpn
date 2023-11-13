#!/bin/bash

# Make sure the script is running as root
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root."
    exit 1
fi

# Update package list
sudo apt update

# Install pip for Python 3
sudo apt install -y python3-pip

# Verify installation
pip --version

# Display a message indicating successful installation
echo "pip for Python 3 has been successfully installed."

# Check if xVpn directory exists and delete it
if [ -d "xVpn" ]; then
    echo "Deleting existing xVpn directory..."
    rm -rf xVpn
fi

# Clone the repository
git clone https://github.com/xshelll/xVpn.git

# Change to the project directory
cd xVpn

# Install dependencies from requirements.txt
pip install -r requirements.txt --break-system-packages

# Change permissions
chmod +x knife-xray

# Run the web.py script in a detached screen session
screen -dmS web_session python3 web.py

echo "web.py script is running in a 'web_session' screen session."

# Run the update.py script in another detached screen session
screen -dmS update_session python3 update.py

echo "update.py script is running in an 'update_session' screen session."

echo "Script execution complete."
