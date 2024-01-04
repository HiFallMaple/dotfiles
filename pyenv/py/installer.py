from .config import register, logger, requirements_path
from pydotfiles import run_command, ROOT, USER

operate = 'install'
package = 'pyenv'


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    logger.info(f"Installing {package}...")
    command = ["apt-get", "install", "-y", "python3-pip"]
    run_command(command, ROOT)
    command = ["python3", "-m", "pip", "install", "-r", requirements_path]
    run_command(command, ROOT)