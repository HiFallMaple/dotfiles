import subprocess
from .config import register, sudo_command

operate = 'install'
package = "zsh"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    with open(".log", "a") as f:
        f.write("-"*40+f"\nInstalling {package}...\n")
    with open(".log", "a") as f:
        command = sudo_command(["apt-get", "install", "-y", package])
        subprocess.run(command , stdout=f, stderr=subprocess.STDOUT, text=True, check=True)
        command = ['chsh', '-s', '$(which zsh)']
        return subprocess.run(command , stdout=f, stderr=subprocess.STDOUT, text=True, check=True)