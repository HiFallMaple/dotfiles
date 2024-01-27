import os
import subprocess
from pydotfiles import OS_PLATFORM, ALLOW_PALTFORMS

if __name__ == "__main__":
    if OS_PLATFORM not in ALLOW_PALTFORMS:
        raise(f"Error: platform {OS_PLATFORM} not allowed.")
    elif OS_PLATFORM == 'ubuntu':
        subprocess.run("sudo apt update", shell=True, check=True)
    uid = os.getuid()
    with open("UID", "w") as f:
        f.write(str(uid))