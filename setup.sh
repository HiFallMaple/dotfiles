sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install vim
sudo apt-get -y install git
sudo apt-get -y install curl
sudo apt-get -y install wget
sudo apt-get -y install zsh
sudo apt-get -y install bat
sudo apt-get -y install fd-find
sudo apt-get -y install exa
sudo apt-get -y install duf
sudo apt-get -y install btop
sudo apt-get -y install ripgrep
sudo apt-get -y install du-dust

# setup bat and fd
mkdir -p ~/.local/bin
ln -s $(which batcat) ~/.local/bin/bat
ln -s $(which fdfind) ~/.local/bin/fd

git config --global user.name "FallMaple"
git config --global core.editor "vim"

# startship
curl -sS https://starship.rs/install.sh | sh -s -- -f -y

# install zinit
bash -c "$(curl --fail --show-error --silent --location https://raw.githubusercontent.com/zdharma-continuum/zinit/HEAD/scripts/install.sh)"

# copy config
cp -r .config ~
cp .zshrc ~

# install fzf
# wget -O ~/.zsh/fzf-key-bindings.zsh https://raw.githubusercontent.com/junegunn/fzf/master/shell/key-bindings.zsh
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install --bin
cp ~/.fzf/bin/* ~/.local/bin
# set fzf key bindings
cp ~/.fzf/shell/key-bindings.zsh ~/.config/.zsh/fzf-key-bindings.zsh
rm -rf ~/.fzf

# setup default shell
chsh -s $(which zsh)