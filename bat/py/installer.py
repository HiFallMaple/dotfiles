from .config import register, logger
from pydotfiles import run_command, ROOT
import shutil

operate = 'install'
package = "bat"
link_src_name = "batcat"
link_dst_name = "bat"


@register.registe_method(['ubuntu22', 'ubuntu24'], operate, package)
def ubuntu_install_package():
    logger.info(f"Installing {package}...")
    command = ["apt-get", "install", "-y", package]
    run_command(command, ROOT)
    
    if shutil.which(link_dst_name) is None:
        command = ["ln", "-s", shutil.which(link_src_name), '/bin/bat']
        run_command(command, ROOT)