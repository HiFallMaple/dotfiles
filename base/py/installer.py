import os
import subprocess
from .config import appList, register, run_command, ROOT, logger

operate = 'install'


for app in appList:
    @register.registe_method('ubuntu', operate, app)
    def ubuntu_install():
        logger.info(f"Installing {app}...")
        command = ["apt-get", "install", "-y", app]
        run_command(command, ROOT)