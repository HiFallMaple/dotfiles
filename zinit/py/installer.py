import os
import subprocess
from .config import register, expanduser, run_command, ROOT, USER

operate = 'install'
package = "zinit"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    with open(".log", "a") as f:
        f.write("-"*40+f"\nInstalling {package}...\n")
    with open(".log", "a") as f:
        zinit_home = expanduser("~/.local/share/zinit/zinit.git")
        command = ["mkdir", "-p", zinit_home]
        run_command(command, USER)
        if not os.path.isdir(os.path.join(zinit_home, ".git")):
            command = ["git", "clone", "https://github.com/zdharma-continuum/zinit.git", zinit_home]
            return run_command(command, USER)