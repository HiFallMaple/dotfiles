import os
import re
import shutil
from pydotfiles import file2set, run_command, expanduser, user_has_write_permission, ROOT, USER
from config import SUB_DIR, WHICH_REX


def ask_for_replace(dst):
    ans = input(f"{dst} exists. Replace it? (Y/n)")
        
    if ans.lower() == "" or ans.lower() == "y":
        command = ["rm","-rf", dst]
        if user_has_write_permission(dst):
            run_command(command, USER)
        else:
            run_command(command, ROOT)
        return True
    return False


def process_path(path, package_name):
    path = expanduser(path)
    if os.path.isabs(path):
        return path
    else:
        return os.path.abspath(os.path.join(package_name, "dotfile", path))
    

def replace_which(link_peer: str) -> (str, str):
    matches = re.finditer(WHICH_REX, link_peer)
    for match in matches:
        # match.group(0): $which/filename
        # match.group(1): filename
        link_peer = link_peer.replace(match.group(0), shutil.which(match.group(1)))
    return link_peer
    

def link_dotfiles_of_package(package_name, linkList):
    for link_peer in linkList:
        src, dst = replace_which(link_peer).split()
        src = process_path(src, package_name)
        dst = expanduser(dst)
        print(src, dst)
        if not os.path.exists(src):
            raise Exception(f"{src} does not exist.")
        if os.path.exists(dst):
            if not ask_for_replace(dst):
                continue
        command = ["ln", "-s", src, dst]
        src_dir = os.path.dirname(src)
        dst_dir = os.path.dirname(dst)
        if user_has_write_permission(src_dir) and user_has_write_permission(dst_dir):
            run_command(command, USER)
        else:
            run_command(command, ROOT)


def walk_dir(dir):
    for package_name in dir:
        linkList_path = os.path.join(package_name, "linkList")
        if os.path.isfile(linkList_path):
            linkList = file2set(linkList_path)
            if len(linkList) == 0:
                continue
            link_dotfiles_of_package(package_name, linkList)


if __name__ == "__main__":
    if os.getuid() != 0:
        print("Please run as root.")
        exit(1)
    walk_dir(SUB_DIR)
