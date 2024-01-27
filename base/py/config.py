import os
import sys
from .base_config import *


def __get_appList():
    appList_path = os.path.join(parent_dir, "appList")
    packages = []
    try:
        with open(appList_path, 'r') as f:
            packages = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: file {appList_path} not found.")
        sys.exit(1)
    return packages

appList: list = __get_appList()