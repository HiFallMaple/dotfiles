import os
import subprocess
from .config import register, parent_dir, sudo_command

operate = 'install'
package = "fzf"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    with open(".log", "a") as f:
        f.write("-"*40+f"\nInstalling {package}...\n")
    with open(".log", "a") as f:
        script_path = os.path.join(parent_dir, "set_source.sh")
        command = sudo_command([script_path])
        subprocess.run(command , stdout=f, stderr=subprocess.STDOUT, text=True, check=True)
        command = sudo_command(["apt-get", "install", "-y", package])
        subprocess.run(command , stdout=f, stderr=subprocess.STDOUT, text=True, check=True)
        
        # download fzf-key-bindings.zsh
        dst_dir_path = os.path.expanduser("~/.config/.zsh/")
        dst_path = os.path.join(dst_dir_path, "fzf-key-bindings.zsh")
        os.makedirs(dst_dir_path, exist_ok=True)
        # check if dst_path exists
        if not os.path.exists(dst_path):
            command = ["wget", "https://raw.githubusercontent.com/junegunn/fzf/master/shell/key-bindings.zsh", "-O", dst_path]
            return subprocess.run(command , stdout=f, stderr=subprocess.STDOUT, text=True, check=True)
        elif os.path.isdir(dst_path):
            raise Exception(f"{dst_path} is a directory.")