#!/bin/bash
echo "Install: fzf"
# Add installation commands here

git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install --bin
cp ~/.fzf/bin/* ~/.local/bin
# set fzf key bindings
cp ~/.fzf/shell/key-bindings.zsh ~/.config/.zsh/fzf-key-bindings.zsh
rm -rf ~/.fzf