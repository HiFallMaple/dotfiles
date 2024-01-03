from .config import register, sudo_command, run_command, ROOT, logger
import requests

operate = 'install'
package = "starship"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    logger.info(f"Installing {package}...")
    script = requests.get("https://starship.rs/install.sh").text
    command = ["sh", "-c", script, "--", "-f", "-y"]
    return run_command(command, ROOT)
