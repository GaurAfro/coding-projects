#!/bin/bash

# Header Comments
# Description: Script to set up Debian with Btrfs, Timeshift, ZRAM, nala, and a WM.
# Author: GaurAfro
# Date: 27/08/2023

# Variables
PACKAGES_ESSENTIAL=("xorg" "nala")
PACKAGES_WM=("i3" "rofi")

# Functions
install_packages() {
    sudo apt update
    sudo apt install -y "${PACKAGES_ESSENTIAL[@]}"
    # ... other package installations
}

configure_btrfs() {
    # Btrfs configurations
}

setup_timeshift() {
    # Timeshift configurations
}

# ... other functions ...

# Main Execution
if [[ $EUID -ne 0 ]]; then
    echo "Please run this script as root."
    exit 1
fi

echo "Starting the setup..."
install_packages
configure_btrfs
# ... call other functions ...

# Cleanup & Exit
echo "Setup completed successfully. Consider rebooting for all changes to take effect."
exit 0

