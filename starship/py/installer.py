from .config import register, logger
from pydotfiles import run_command, ROOT
import requests

operate = 'install'
package = "starship"


@register.registe_method(['ubuntu22', 'ubuntu24'], operate, package)
def ubuntu_install_package():
    logger.info(f"Installing {package}...")
    script = requests.get("https://starship.rs/install.sh").text
    command = ["sh", "-c", script, "--", "-f", "-y"]
    return run_command(command, ROOT)
