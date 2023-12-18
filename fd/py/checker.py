from .config import register
from pydotfiles import dpkg_check

operate = 'check'
package = "fd"
apt_package = "fd-find"


@register.registe_method('ubuntu', operate, package)
def ubuntu_check_package():
	return dpkg_check(apt_package)