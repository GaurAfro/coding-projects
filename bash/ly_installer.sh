#!/bin/bash

# Upgrading the system using Nala
echo "Upgrading the system using Nala..."
sudo nala upgrade -y

# Checking if timeout is available
echo "Checking if timeout is installed..."
if ! command -v timeout &> /dev/null; then
    echo "timeout could not be found. Installing..."
    sudo nala install timeout -y
else
    echo "timeout is already installed."
fi

# Installing other dependencies
echo "Installing dependencies: build-essential, libpam0g-dev, libxcb-xkb-dev, git..."
sudo nala install build-essential libpam0g-dev libxcb-xkb-dev git -y

# Cloning the repository
echo "Cloning the ly repository..."
git clone --recurse-submodules https://github.com/fairyglade/ly

# Changing the directory to `ly`
echo "Changing directory to 'ly'..."
cd ly

# Compiling the source
echo "Compiling the source..."
make

# Testing in the configured tty or terminal emulator
echo "Testing in the configured tty (tty2 by default) or terminal emulator..."
timeout --signal=SIGINT 3s make run

# Installing Ly and the systemd service file
echo "Installing Ly and the provided systemd service file..."
sudo make install installsystemd

# Checking if the display manager service link exists and delete it
if [ -f "/etc/systemd/system/display-manager.service" ]; then
    echo "Removing /etc/systemd/system/display-manager.service..."
    sudo rm /etc/systemd/system/display-manager.service
else
    echo "/etc/systemd/system/display-manager.service does not exist."
fi

# Enabling the service
echo "Enabling the ly service..."
sudo systemctl enable ly.service

# Disabling getty on Ly's tty
echo "Disabling getty on Ly's tty to prevent 'login' from spawning on top of it..."
sudo systemctl disable getty@tty2.service

echo "Script completed!"
    
