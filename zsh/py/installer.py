from .config import register, sudo_command, run_command, ROOT, USER, USER_NAME

operate = 'install'
package = "zsh"


@register.registe_method('ubuntu', operate, package)
def ubuntu_install_package():
    with open(".log", "a") as f:
        f.write("-"*40+f"\nInstalling {package}...\n")
    with open(".log", "a") as f:
        command = ["apt-get", "install", "-y", package]
        run_command(command, ROOT)
        command = ['chsh', '-s', '$(which zsh)', USER_NAME]
        return run_command(command, ROOT)