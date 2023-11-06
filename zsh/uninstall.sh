#!/bin/sh
echo "Uninstall: zsh"
# Add uninstallation commands here

sudo apt-get -y purge zsh

# setup default shell
chsh -s $(which bash)