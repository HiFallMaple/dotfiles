import subprocess
from .config import register, run_command, ROOT

operate = 'uninstall'
package = "fzf"


@register.registe_method('ubuntu', operate, package)
def ubuntu_uninstall_package():
	command = ["apt-get", "purge", "-y", package]
	return run_command(command, ROOT)