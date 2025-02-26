from .config import register, logger
from pydotfiles import run_command, expanduser, ROOT, USER

operate = 'setup'


@register.registe_method(['ubuntu22', 'ubuntu24'], operate, "git")
def ubuntu_setup_package():
    logger.info(f"Setting up git...")
    command = ["git", "config", "--global", "init.defaultBranch", "main"]
    run_command(command, USER)
    command = ["git", "config", "--global", "core.editor", "\"vim\""]
    return run_command(command, USER)
    
@register.registe_method(['ubuntu22', 'ubuntu24'], operate, ".config")
def ubuntu_setup_package():
    logger.info(f"Create .config directory...")
    command = ["mkdir", "-p", expanduser("~/.config")]
    run_command(command, USER)