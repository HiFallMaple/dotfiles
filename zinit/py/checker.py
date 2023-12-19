from .config import register, expanduser
from pydotfiles import command_check
import os

operate = 'check'
package = "zinit"


@register.registe_method('ubuntu', operate, package)
def ubuntu_check_package():
	return True if os.path.isfile(expanduser("~/.local/share/zinit/zinit.git/zinit.zsh")) else False