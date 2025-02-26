from .config import appList, register, logger
from pydotfiles import run_command, ROOT


operate = 'uninstall'


def uninstall_func_factory(app):
    @register.registe_method(['ubuntu22', 'ubuntu24'], operate, app)
    def ubuntu_uninstall_package():
        logger.info(f"Uninstalling {app}...")
        command = ["apt-get", "purge", "-y", app]
        run_command(command, ROOT)
        

for app in appList:
    uninstall_func_factory(app)