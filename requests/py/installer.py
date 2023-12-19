import subprocess
from .config import register, run_command, ROOT, USER

operate = 'install'
package = 'requests'


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    with open(".log", "a") as f:
        f.write("-"*40+f"\nInstalling {package}...\n")
        command = ["python3", "-m", "pip", "install", package]
        return run_command(command, ROOT) # because use root to run python script