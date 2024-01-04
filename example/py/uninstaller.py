from .config import register

operate = 'uninstall'


#==================================================================================
# example
#==================================================================================
#
# @register.registe_method('ubuntu', operate, package)
# def ubuntu_uninstall_package():
# 	command = ["sudo", "apt-get", "purge", "-y", package]
#   subprocess.run(command, stdout=f, stderr=subprocess.STDOUT, text=True, check=True)
#
#==================================================================================