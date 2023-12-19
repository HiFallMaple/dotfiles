import os
from pydotfiles import Register, get_dependencies, sudo_command, run_command, ROOT, USER, expanduser


current_dir: str = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
dependency: list = get_dependencies(parent_dir)
register = Register()
