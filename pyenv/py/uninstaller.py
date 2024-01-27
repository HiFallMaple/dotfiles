from .config import register, logger
from pydotfiles import run_command, ROOT, USER

operate = 'install'


#======================================================================================================
# example
#======================================================================================================
#
# @register.registe_method('ubuntu', operate, package)
# def ubuntu_uninstall_package():
# 	logger.info(f"Uninstalling {package}...")
# 	command = ["apt-get", "purge", "-y", package]
# 	run_command(command, ROOT)
#
#======================================================================================================