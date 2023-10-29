bindkey '^A' beginning-of-line        # [Ctrl-A] - Jump to the start of the line
bindkey '^[[1;5C' forward-word        # [Ctrl-RightArrow] - move forward one word
bindkey '^[[1;5D' backward-word       # [Ctrl-LeftArrow] - move backward one wordx

autoload -z edit-command-line # [Ctrl + X, Ctrl + E] - Edit command in vim
zle -N edit-command-line
bindkey "^X^E" edit-command-line

autoload -U select-word-style
select-word-style bash
export WORDCHARS='.-'