from .config import register

operate = 'uninstall'


#==================================================================================
# example
#==================================================================================
#
# @register.registe_method('ubuntu', operate, package)
# def ubuntu_uninstall_package():
# 	subprocess.run(["sudo", "apt-get", "purge", "-y", package], check=True)
#
#==================================================================================