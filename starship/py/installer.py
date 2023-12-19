import subprocess
from .config import register, sudo_command, run_command, ROOT

operate = 'install'
package = "starship"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    with open(".log", "a") as f:
        f.write("-"*40+f"\nInstalling {package}...\n")
    with open(".log", "a") as f:
        command = ['curl -sS https://starship.rs/install.sh | sh -s -- -f -y']
        return run_command(command, ROOT)