import os
import subprocess
from .config import register

operate = 'install'
package = "zinit"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    with open(".log", "a") as f:
        f.write("-"*40+f"\nInstalling {package}...\n")
    with open(".log", "a") as f:
        zinit_home = os.path.expanduser("~/.local/share/zinit/zinit.git")
        os.makedirs(zinit_home, exist_ok=True)
        if not os.path.isdir(os.path.join(zinit_home, ".git")):
            command = ["git", "clone", "https://github.com/zdharma-continuum/zinit.git", zinit_home]
            return subprocess.run(command , stdout=f, stderr=subprocess.STDOUT, text=True, check=True)