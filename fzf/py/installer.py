import os
from .config import register, parent_dir, logger
from pydotfiles import run_command, USER, ROOT
operate = 'install'
package = "fzf"


@register.registe_method(['ubuntu22'], operate, package)
def ubuntu_install_package():
    logger.info(f"Installing {package}...")
    script_path = os.path.join(parent_dir, "set_source.sh")
    command = [script_path]
    run_command(command, ROOT)
    command = ["apt-get", "install", "-y", package]
    run_command(command, ROOT)
    
@register.registe_method(['ubuntu24'], operate, package)
def ubuntu_install_package():
    logger.info(f"Installing {package}...")
    command = ["apt-get", "install", "-y", package]
    run_command(command, ROOT)