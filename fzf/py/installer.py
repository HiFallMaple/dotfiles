import os
from .config import register, parent_dir, logger
from pydotfiles import expanduser, run_command, USER, ROOT
operate = 'install'
package = "fzf"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    logger.info(f"Installing {package}...")
    script_path = os.path.join(parent_dir, "set_source.sh")
    command = [script_path]
    run_command(command, ROOT)
    command = ["apt-get", "install", "-y", package]
    run_command(command, ROOT)
    
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