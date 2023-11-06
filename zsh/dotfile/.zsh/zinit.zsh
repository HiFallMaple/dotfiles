# Load a few important annexes, without Turbo
# (this is currently required for annexes)
zinit light-mode for \
    zdharma-continuum/zinit-annex-as-monitor \
    zdharma-continuum/zinit-annex-bin-gem-node \
    zdharma-continuum/zinit-annex-patch-dl \
    zdharma-continuum/zinit-annex-rust

zinit snippet OMZL::history.zsh
zinit snippet OMZP::sudo
zinit snippet OMZP::git/git.plugin.zsh
zinit snippet OMZP::pip/pip.plugin.zsh
zinit snippet OMZP::python/python.plugin.zsh
zinit snippet OMZP::golang/golang.plugin.zsh
zinit snippet OMZP::docker-compose/docker-compose.plugin.zsh
zinit light zsh-users/zsh-autosuggestions
zinit light zdharma-continuum/fast-syntax-highlighting
zinit ice wait lucid
zinit light hlissner/zsh-autopair
zinit ice wait lucid
zinit light Aloxaf/fzf-tab
zinit ice wait lucid
zinit light wfxr/forgit

# zinit ice as"completion"
# zinit snippet https://github.com/docker/cli/blob/master/contrib/completion/zsh/_docker
