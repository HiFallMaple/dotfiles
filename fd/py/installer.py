import shutil
import subprocess
import os
from .config import register, sudo_command, run_command, ROOT

operate = 'install'
package = "fd"
apt_package = "fd-find"
link_src_name = "fdfind"
link_dst_name = "fd"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    with open(".log", "a") as f:
        f.write("-"*40+f"\nInstalling {package}...\n")
    with open(".log", "a") as f:
        command = ["apt-get", "install", "-y", apt_package]
        run_command(command, ROOT)
