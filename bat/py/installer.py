from .config import register, logger
from pydotfiles import run_command, ROOT


operate = 'install'
package = "bat"
link_src_name = "batcat"
link_dst_name = "bat"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    logger.info(f"Installing {package}...")
    command = ["apt-get", "install", "-y", package]
    run_command(command, ROOT)
