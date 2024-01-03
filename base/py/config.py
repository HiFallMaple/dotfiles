import logging
import logging.config
import os
import sys
from pydotfiles import Register, get_dependencies, sudo_command, run_command, ROOT, USER, LOGGING_CONFIG


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

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
current_dir: str = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
dependency: list = get_dependencies(parent_dir)
appList: list = __get_appList()
register = Register()
