from .config import register
from pydotfiles import dpkg_check

operate = 'check'
package = "bat"

#============================================================
# example
#============================================================
#
# @register.registe_method(['ubuntu22'], operate, package)
# def ubuntu_check_package():
# 	return dpkg_check(package)
#
#============================================================


@register.registe_method(['ubuntu22', 'ubuntu24'], operate, package)
def ubuntu_check_package():
	return dpkg_check(package)