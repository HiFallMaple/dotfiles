import os
import importlib
from pydotfiles import Loader
from config import SUB_DIR


def setup(module_name):
    module = importlib.import_module(module_name)
    setup_methods = module.register.get_setup_methods()
    for key in setup_methods:
        with Loader(desc=f"Setting up {key}...", end_success=f"SUCCESS: {key} setup successfully!", end_error=f""):
            setup_methods[key]()


if __name__ == "__main__":
    if os.getuid() != 0:
        print("Please run as root.")
        exit(1)
    for package in SUB_DIR:
        print(package)
        setup(f"{package}.py")
