import shutil
from .config import register, logger
from pydotfiles import run_command, ROOT, USER_NAME

operate = 'setup'
package = "zsh"


@register.registe_method(['ubuntu22', 'ubuntu24'], operate, package)
def ubuntu_setup_package():
    logger.info(f"Setting up {package}...")
    command = ['chsh', '-s', shutil.which("zsh"), USER_NAME]
    return run_command(command, ROOT)