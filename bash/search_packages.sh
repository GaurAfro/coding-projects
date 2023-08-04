#!/bin/bash

package_name="$1"

# Check if an argument was provided
if [[ -z "$package_name" ]]; then
	echo "You didn't provide a package name."
	read -p "Please enter the package name to search for: " package_name
fi

# Exit if the package name is still empty after prompting
if [[ -z "$package_name" ]]; then
	echo "No package name provided. Exiting."
	exit 1
fi

# Search using apt
echo "Searching for '$package_name' using apt..."
apt-cache search "$package_name"

# Search using snap
echo -e "\nSearching for '$package_name' using snap..."
snap find "$package_name"

# Search using flatpak
echo -e "\nSearching for '$package_name' using flatpak..."
flatpak search "$package_name"
