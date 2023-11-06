#!/bin/sh
echo "Install: zsh"
# Add installation commands here
# zsh
sudo apt-get -y install zsh

# zinit
bash -c "$(curl --fail --show-error --silent --location https://raw.githubusercontent.com/zdharma-continuum/zinit/HEAD/scripts/install.sh)"

# setup default shell
chsh -s $(which zsh)