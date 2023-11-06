#!/bin/sh
echo "Uninstall: fd"
# Add uninstallation commands here

sudo apt-get -y purge fd-find
rm ~/.local/bin/fd