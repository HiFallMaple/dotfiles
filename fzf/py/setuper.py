import os
from .config import register, logger
from pydotfiles import expanduser, run_command, USER

operate = 'setup'
package = "fzf"


@register.registe_method(['ubuntu22', 'ubuntu24'], operate, package)
def ubuntu_setup_package():
    logger.info(f"Setting up fzf...")
    # download fzf-key-bindings.zsh
    dst_dir_path = expanduser("~/.config/.zsh/")
    dst_path = os.path.join(dst_dir_path, "fzf-key-bindings.zsh")
    command = ["mkdir", "-p", dst_dir_path]
    run_command(command, USER)
    # check if dst_path exists
    if not os.path.exists(dst_path):
        command = ["wget", "https://raw.githubusercontent.com/junegunn/fzf/master/shell/key-bindings.zsh", "-O", dst_path]
        return run_command(command, USER)
    elif os.path.isdir(dst_path):
        raise Exception(f"{dst_path} is a directory.")