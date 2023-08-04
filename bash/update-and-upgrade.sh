#!/bin/bash
# Update and upgrade the system if it is Ubuntu

release_file=/etc/os-release

if grep -q "Ubuntu" $release_file || grep -q "Debian" $release_file || grep -q "Pop" $release_file; then
    sudo apt-get update
    sudo apt-get dist-upgrade -y
fi
