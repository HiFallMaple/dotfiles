import os
import shutil
import subprocess
from pydotfiles import check_sudo_nopasswd, add_sudo_nopasswd, remove_sudo_nopasswd, sudo_command, file2set
from config import sub_dir


def ask_for_replace(dst):
    ans = input(f"{dst} exists. Replace it? (Y/n)")
        
    if ans.lower() == "" or ans.lower() == "y":
        command = ["rm","-rf", dst]
        if not os.access(dst, os.W_OK):
            command = sudo_command(command)
        subprocess.run(command, text=True, check=True)
        return True
    return False


def process_path(path, package_name):
    path = os.path.expanduser(path)
    if os.path.isabs(path):
        return path
    else:
        return os.path.abspath(os.path.join(package_name, "dotfile", path))


def link_dotfiles_of_package(package_name, linkList):
    for link_peer in linkList:
        src, dst = link_peer.replace("$which", os.path.dirname(
            shutil.which(package_name))).split()
        src = process_path(src, package_name)
        dst = os.path.expanduser(dst)
        print(src, dst)
        if not os.path.exists(src):
            raise Exception(f"{src} does not exist.")
        if os.path.exists(dst):
            if not ask_for_replace(dst):
                continue
        command = ["ln", "-s", src, dst]
        if not (os.access(os.path.dirname(src), os.W_OK) and os.access(os.path.dirname(dst), os.W_OK)):
            command = sudo_command(command)
        subprocess.run(command, text=True, check=True)


def walk_dir(dir):
    for package_name in dir:
        linkList_path = os.path.join(package_name, "linkList")
        if os.path.isfile(linkList_path):
            linkList = file2set(linkList_path)
            if len(linkList) == 0:
                continue
            link_dotfiles_of_package(package_name, linkList)


if __name__ == "__main__":
    if not check_sudo_nopasswd():
        add_sudo_nopasswd()

    walk_dir(sub_dir)

    remove_sudo_nopasswd()
