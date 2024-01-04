from .config import register, logger
from pydotfiles import run_command, ROOT

operate = 'install'
package = "fd"
apt_package = "fd-find"
link_src_name = "fdfind"
link_dst_name = "fd"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    logger.info(f"Installing {package}...")
    command = ["apt-get", "install", "-y", apt_package]
    run_command(command, ROOT)
