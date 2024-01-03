from .config import register, sudo_command, run_command, ROOT, logger

operate = 'install'
package = "starship"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    logger.info(f"Installing {package}...")
    command = ['curl -sS https://starship.rs/install.sh | sh -s -- -f -y']
    return run_command(command, ROOT)