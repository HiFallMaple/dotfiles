import shutil
import subprocess
import os
from .config import register, sudo_command, run_command, ROOT


operate = 'install'
package = "bat"
link_src_name = "batcat"
link_dst_name = "bat"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    with open(".log", "a") as f:
        f.write("-"*40+f"\nInstalling {package}...\n")
        command = ["apt-get", "install", "-y", package]
        run_command(command, ROOT)