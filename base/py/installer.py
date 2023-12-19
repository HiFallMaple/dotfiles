import os
import subprocess
from .config import appList, register, sudo_command, run_command, ROOT

operate = 'install'


for app in appList:
    @register.registe_method('ubuntu', operate, app)
    def ubuntu_install():
        with open(".log", "a") as f:
            f.write("-"*40+f"\nInstalling {app}...\n")
        with open(".log", "a") as f:
            command = ["apt-get", "install", "-y", app]
            run_command(command, ROOT)