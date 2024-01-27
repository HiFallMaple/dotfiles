from .config import register
from pydotfiles import command_check

operate = 'check'
package = "starship"


@register.registe_method('ubuntu', operate, package)
def ubuntu_check_package():
	return command_check(package)