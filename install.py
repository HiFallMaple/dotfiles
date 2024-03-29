import os
import importlib
from pydotfiles import Loader, file2set
from config import SUB_DIR


def install(module_name):
    module = importlib.import_module(module_name)
    install_methods = module.register.get_install_methods()
    check_methods = module.register.get_check_methods()
    for key in install_methods:
        if check_methods[key]():
            print(f"Skip: {key} is already installed.")
            continue
        with Loader(desc=f"Installing {key}...", end_success=f"SUCCESS: {key} installation successful!", end_error=f""):
            install_methods[key]()


def gen_install_order(packages):
    if "base" in packages:
        packages = packages-{"base"}
    else:
        raise Exception("No base dir found.")

    if "pyenv" in packages:
        packages = packages-{"pyenv"}
    else:
        raise Exception("No pyenv dir found.")

    # 創建一個字典來存儲每個包的依賴關係
    dependencies = {}
    for package in packages:
        dependency_path = os.path.join(package, "dependency")
        if os.path.exists(dependency_path):
            with open(dependency_path, "r") as f:
                dependencies[package] = file2set(dependency_path)

    base_appList = file2set(os.path.join("base", "appList"))
    sorted_packages = list(base_appList)
    # Perform topological sort recursively

    def visit(package):
        nonlocal sorted_packages
        # If the package is already sorted, return
        if package in sorted_packages:
            return
        # Visit each dependency of the package
        for dependency in dependencies[package]:
            visit(dependency)
        sorted_packages.append(package)

    # Perform topological sort for each package
    for package in packages:
        visit(package)

    sorted_packages = [
        package for package in sorted_packages if package not in base_appList]
    
    sorted_packages = ["base", "pyenv"] + sorted_packages
    return sorted_packages


if __name__ == "__main__":
    if os.getuid() != 0:
        print("Please run as root.")
        exit(1)
    install_order = gen_install_order(SUB_DIR)
    for package in install_order:
        install(f"{package}.py")
