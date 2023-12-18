import subprocess
from .config import appList, register


operate = 'uninstall'

for app in appList:
	@register.registe_method('ubuntu', operate, app)
	def ubuntu_uninstall():
		subprocess.run(["sudo", "apt-get", "purge", "-y", app], check=True)