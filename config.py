import os

IGNORE_DIR = {"example", "__pycache__", "nodejs"}
sub_dir = {os.path.basename(f.path) for f in os.scandir(".") if f.is_dir() and os.path.isdir(os.path.join(f, "py"))} - IGNORE_DIR