mkdir -p starship/.config
cp -r ~/.config/starship.toml starship/.config
cp -r ~/.zsh zsh
rm zsh/.zsh/fzf-key-bindings.zsh
cp ~/.zshrc zsh