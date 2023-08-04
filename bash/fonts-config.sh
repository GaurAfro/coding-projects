#!/usr/bin/env bash

# fonts-config.sh
# This script is designed to manage font installations for the user.
# It checks for font files stored as .zip in either ~/dotfiles/fonts/ or the current directory.
# The script then ensures these fonts are properly extracted and installed in the user's font directory.
# Lastly, it updates the font cache to make the new fonts available system-wide.

# Check if the font directory does not exists
FONT_DIR="${HOME}/.local/share/fonts"
if [ ! -d "${FONT_DIR}" ]; then
	# Ensure the font directory exists
	echo "mkdir -p $FONT_DIR"
	mkdir -p "${FONT_DIR}"
else
	echo "Found fonts dir $FONT_DIR"
fi

# Check if there's a dedicated font repository under ~/dotfiles/fonts.
# If not, it will look for .zip font files in the current directory.
REPO="${HOME}/dotfiles/fonts/"
if [ ! -d "${REPO}" ]; then
	echo "Don't have $REPO, will get the fonts here"
	cp *zip "$FONT_DIR"
else
	# Inform the user about the copying process
	echo "Copying font files from ${HOME}/dotfiles/fonts/ to ${FONT_DIR}"
	# Copy the font zip files from dotfiles to the fonts directory
	cp "${HOME}/dotfiles/fonts/"*.zip "${FONT_DIR}"
fi

# Change to the font directory and unzip the files
cd "${FONT_DIR}"
for font_zip in *.zip; do
	# Get the base name without the .zip extension
	font_name="${font_zip%.zip}"

	# Create a directory for the font
	mkdir -p "${font_name}"

	# Unzip the font into its directory
	unzip "${font_zip}" -d "${font_name}"

	# Remove the zip file
	rm "${font_zip}"
done

# Update the system's font cache
echo "Updating font cache with fc-cache -f"
fc-cache -f
