import os
import subprocess
from pydotfiles import OS_PLATFORM, is_allow_platform

if __name__ == "__main__":
    if not is_allow_platform(OS_PLATFORM):
        raise(f"Error: platform {OS_PLATFORM} not allowed.")
    elif 'ubuntu' in OS_PLATFORM:
        subprocess.run("sudo apt update", shell=True, check=True)
    uid = os.getuid()
    with open("UID", "w") as f:
        f.write(str(uid))