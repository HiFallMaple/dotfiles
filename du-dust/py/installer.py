import shutil
import subprocess
import os

import requests
from .config import register, sudo_command

operate = 'install'
package = "du-dust"
repo = "bootandy/dust"
api_url = f"https://api.github.com/repos/{repo}/releases"
download_path = "/tmp/du-dust_amd64.deb"


def __get_latest_amd64_deb_url() -> str:
    data = requests.get(api_url).json()
    for li in data[0]["assets"]:
        if ("amd64.deb" in li["name"]):
            return li["browser_download_url"]


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    with open(".log", "a") as f:
        f.write("-"*40+f"\nInstalling {package}...\n")
    with open(".log", "a") as f:
        deb_url = __get_latest_amd64_deb_url()
        command = ["wget", deb_url, "-O", download_path]
        subprocess.run(command , stdout=f, stderr=subprocess.STDOUT, text=True, check=True)
        command = sudo_command(["apt-get", "install", "-y", download_path])
        subprocess.run(command , stdout=f, stderr=subprocess.STDOUT, text=True, check=True)
        os.remove(download_path)