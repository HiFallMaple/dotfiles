import shutil
from .config import register, logger
from pydotfiles import run_command, ROOT, USER_NAME

operate = 'install'
package = "zsh"


@register.registe_method(['ubuntu22', 'ubuntu24'], operate, package)
def ubuntu_install_package():
    logger.info(f"Installing {package}...")
    command = ["apt-get", "install", "-y", package]
    run_command(command, ROOT)