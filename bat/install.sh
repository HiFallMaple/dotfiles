#!/bin/sh
echo "Install: bat"
# Add installation commands here
sudo apt-get -y install bat
ln -s $(which batcat) ~/.local/bin/bat