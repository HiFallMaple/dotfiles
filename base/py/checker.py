from .config import appList, register
from pydotfiles import dpkg_check

operate = 'check'

for app in appList:
	@register.registe_method('ubuntu', operate, app)
	def ubuntu_check():
		return dpkg_check(app)