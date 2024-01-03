import shutil
from .config import register, sudo_command, run_command, ROOT, USER, USER_NAME, logger

operate = 'install'
package = "zsh"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    logger.info(f"Installing {package}...")
    command = ["apt-get", "install", "-y", package]
    run_command(command, ROOT)
    command = ['chsh', '-s', shutil.which("zsh"), USER_NAME]
    return run_command(command, ROOT)