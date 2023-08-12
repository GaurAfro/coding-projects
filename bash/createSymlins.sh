#!/bin/bash
# ------------------------------------------------------
# Create symbolic links
# ------------------------------------------------------
echo ""
echo "-> Install symbolic links"

_createSymLink() {
    symlink="$1";
    linksource="$2";
    linktarget="$3";
    if [ -L "${symlink}" ]; then
        _handleExistingLink "${symlink}"
    else
        if [ -d ${symlink} ]; then
            _handleExistingDirectory "${symlink}"
        else
            if [ -f ${symlink} ]; then
                _handleExistingFile "${symlink}"
            else
                _createLink "${linksource}" "${linktarget}"
            fi
        fi
    fi
}

_handleExistingLink() {
    echo "Link ${symlink} exists already."
    rm -f "${symlink}" && echo "Link ${symlink} removed."
}

_handleExistingDirectory() {
    echo "Directory ${symlink}/ exists."
    mv -v -r "${symlink}" "${symlink}".bak && echo "Directory ${symlink}/ renamed to ${symlink}.bak"
}

_handleExistingFile() {
    echo "File ${symlink} exists."
    mv -v "${symlink}" "${symlink}".bak && echo "File ${symlink} renamed to ${symlink}.bak"
}

_createLink() {
    ln -s -p "${linksource}" "${linktarget}" 
    echo "Link ${linksource} -> ${linktarget} created."
}
_createSymLink ~/.config/qtile ~/arch-qtile/dotfiles/qtile/ ~/.config
_createSymLink ~/.config/alacritty ~/arch-qtile/dotfiles/alacritty/ ~/.config
_createSymLink ~/.config/picom ~/arch-qtile/dotfiles/picom/ ~/.config
_createSymLink ~/.config/rofi ~/arch-qtile/dotfiles/rofi/ ~/.config
_createSymLink ~/.config/vim ~/arch-qtile/dotfiles/vim/ ~/.config
_createSymLink ~/.config/nvim ~/arch-qtile/dotfiles/nvim/ ~/.config
_createSymLink ~/.config/polybar ~/arch-qtile/dotfiles/polybar/ ~/.config
_createSymLink ~/.config/dunst ~/arch-qtile/dotfiles/dunst/ ~/.config
_createSymLink ~/.config/starship.toml ~/arch-qtile/dotfiles/starship/starship.toml ~/.config/starship.toml
