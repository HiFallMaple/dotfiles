import subprocess
from .config import register, sudo_command

operate = 'uninstall'
package = "du-dust"


@register.registe_method('ubuntu', operate, package)
def ubuntu_uninstall_package():
	subprocess.run(sudo_command(["apt-get", "purge", "-y", package], check=True))