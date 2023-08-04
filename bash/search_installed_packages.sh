
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

# Search installed packages using apt
echo "Searching for installed '$package_name' using apt..."
dpkg -l | grep "$package_name"

# Search installed apps using snap
echo -e "\nSearching for installed '$package_name' using snap..."
snap list | grep "$package_name"

# Search installed apps using flatpak
echo -e "\nSearching for installed '$package_name' using flatpak..."
flatpak list | grep "$package_name"
