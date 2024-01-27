import os

IGNORE_DIR = {"example", "__pycache__", "nodejs"}
SUB_DIR = {os.path.basename(f.path) for f in os.scandir(".") if f.is_dir() and os.path.isdir(os.path.join(f, "py"))} - IGNORE_DIR
WHICH_REX = r'\$which/([^/\s]+)'