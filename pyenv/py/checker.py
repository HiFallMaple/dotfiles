from .config import register
from pydotfiles import dpkg_check

operate = 'check'
package = "pyenv"


@register.registe_method('ubuntu', operate, package)
def ubuntu_check_package():
    # to check package of python is installed is not easy, so always return False
	return False
