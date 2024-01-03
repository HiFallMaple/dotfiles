import subprocess
from .config import appList, register, run_command, ROOT


operate = 'uninstall'

for app in appList:
	@register.registe_method('ubuntu', operate, app)
	def ubuntu_uninstall():
		command = ["apt-get", "purge", "-y", app]
		run_command(command, ROOT)