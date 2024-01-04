# disable sort when completing `git checkout`
zstyle ':completion:*:git-checkout:*' sort false
# set descriptions format to enable group support
zstyle ':completion:*:descriptions' format '[%d]'
# set list-colors to enable filename colorizing
zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}
# preview directory's content with ls when completing cd
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'ls --color=always $realpath'
# preview directory's content with ls and file's content with bat when completing ls
zstyle ':fzf-tab:complete:ls:*' fzf-preview 'if [[ -f "$realpath" ]]; then if [[ $(file -bi "$realpath") == *text* ]]; then bat --color=always --style=plain $realpath; else ls --color=always $realpath; fi; elif [[ -d $realpath ]]; then ls --color=always $realpath; fi'
# switch group using `,` and `.`
zstyle ':fzf-tab:*' switch-group ',' '.'