#!/bin/bash
echo "Uninstall: bat"
# Add uninstallation commands here

sudo apt-get -y purge bat
rm ~/.local/bin/bat