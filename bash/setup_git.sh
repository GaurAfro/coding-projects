#!/bin/bash

# Prompt user for name and email
read -p "Enter your name: " name
read -p "Enter your email: " email

# Set the provided name and email for git
git config --global user.name "$name"
git config --global user.email "$email"

# Generate SSH key
ssh-keygen -t ed25519 -C "$email"

# Start the ssh-agent and load the SSH key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy the SSH key to clipboard (requires xclip to be installed)
xclip -sel clip <~/.ssh/id_ed25519.pub

# Open the GitHub SSH keys settings page in the default browser
xdg-open "https://github.com/settings/keys"

# Test the SSH connection to GitHub
ssh -T git@github.com

echo "Git and SSH have been configured with the provided name and email."
