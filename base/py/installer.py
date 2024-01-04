from .config import appList, register, logger
from pydotfiles import run_command, ROOT
operate = 'install'


def install_func_factory(app):
    @register.registe_method('ubuntu', operate, app)
    def ubuntu_install_package():
        logger.info(f"Installing {app}...")
        command = ["apt-get", "install", "-y", app]
        run_command(command, ROOT)


for app in appList:
    install_func_factory(app)
