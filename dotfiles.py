import sys
import subprocess

args = sys.argv

def init():
    subprocess.run("python3 init.py", shell=True, check=True)
    
def install():
    subprocess.run("sudo python3 install.py", shell=True, check=True)
    
def setup():
    subprocess.run("sudo python3 setup.py", shell=True, check=True)

def link():
    subprocess.run("sudo python3 link.py", shell=True, check=True)


if __name__ == "__main__":
    if len(args) == 1:
        init()
        install()
        setup()
        link()
    elif len(args) > 1:
        if args[1] == "init":
            init()
        elif args[1] == "install":
            install()
        elif args[1] == "setup":
            setup()
        elif args[1] == "link":
            link()
    