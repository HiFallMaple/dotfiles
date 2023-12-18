import subprocess
from .config import register

operate = 'install'


#======================================================================================================
# example
#======================================================================================================
#
# @register.registe_method('ubuntu', operate, package)
# def ubuntu_install_package():
#     with open(".log", "a") as f:
#         f.write("-"*40+f"\nInstalling {package}...\n")
#         command = ["sudo", "apt-get", "install", "-y", package]
#         subprocess.run(command, stdout=f, stderr=subprocess.STDOUT, text=True, check=True)
#
#======================================================================================================