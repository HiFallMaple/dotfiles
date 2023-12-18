import shutil
import subprocess
import os
from .config import register, sudo_command

operate = 'install'
package = "bat"
link_src_name = "batcat"
link_dst_name = "bat"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    with open(".log", "a") as f:
        f.write("-"*40+f"\nInstalling {package}...\n")
        command = sudo_command(["apt-get", "install", "-y", package])
        subprocess.run(command , stdout=f, stderr=subprocess.STDOUT, text=True, check=True)
        # link link_src_name to /usr/bin/$link_dst_name and /bin/$link_dst_name
        dst_path_list = [f"/bin/{link_dst_name}", f"/usr/bin/{link_dst_name}"]
        src_path = shutil.which(link_src_name)
        # check if dst_path exists
        for dst_path in dst_path_list:
            if not os.path.exists(dst_path):
                command = sudo_command(["ln", "-s", src_path, dst_path])
                subprocess.run(command , stdout=f, stderr=subprocess.STDOUT, text=True, check=True)
            elif os.path.isdir(dst_path):
                raise Exception(f"{dst_path} is a directory.")