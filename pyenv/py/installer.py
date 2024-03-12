from .config import register, logger, requirements_path
from pydotfiles import run_command, ROOT, USER
import sysconfig
import os

operate = 'install'
package = 'pyenv'


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    logger.info(f"Installing {package}...")
    externally_managed_path = os.path.join(sysconfig.get_path("stdlib", sysconfig.get_default_scheme()), "EXTERNALLY-MANAGED")
    if os.path.exists(externally_managed_path):
        logger.info("Python is managed externally. Move EXTERNALLY-MANAGED to EXTERNALLY-MANAGED.bak.")
        os.rename(externally_managed_path, externally_managed_path + ".bak")
        
    command = ["python3", "-m", "pip", "install", "-r", requirements_path]
    run_command(command, ROOT)
    
    if os.path.exists(externally_managed_path):
        logger.info("Moving EXTERNALLY-MANAGED.bak back to EXTERNALLY-MANAGED.")
        os.rename(externally_managed_path + ".bak", externally_managed_path)