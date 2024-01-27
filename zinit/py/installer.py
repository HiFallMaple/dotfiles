import os
from .config import register, logger
from pydotfiles import expanduser, run_command, USER

operate = 'install'
package = "zinit"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    logger.info(f"Installing {package}...")
    zinit_home = expanduser("~/.local/share/zinit/zinit.git")
    command = ["mkdir", "-p", zinit_home]
    run_command(command, USER)
    if not os.path.isdir(os.path.join(zinit_home, ".git")):
        command = ["git", "clone", "https://github.com/zdharma-continuum/zinit.git", zinit_home]
        return run_command(command, USER)