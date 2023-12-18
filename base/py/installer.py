import os
import subprocess
from .config import appList, register, sudo_command

operate = 'install'


for app in appList:
    @register.registe_method('ubuntu', operate, app)
    def ubuntu_install():
        with open(".log", "a") as f:
            f.write("-"*40+f"\nInstalling {app}...\n")
        with open(".log", "a") as f:
            command = sudo_command(["apt-get", "install", "-y", app])
            subprocess.run(command, stdout=f, stderr=subprocess.STDOUT, text=True, check=True)