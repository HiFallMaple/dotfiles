#!/bin/bash
echo "Install: fd"
# Add installation commands here
sudo apt-get -y install fd-find
ln -s $(which fdfind) ~/.local/bin/fd
