from .config import register, logger
from pydotfiles import run_command, ROOT

operate = 'setup'


@register.registe_method('ubuntu', operate, "git")
def ubuntu_setup_package():
    logger.info(f"Setting up git...")
    command = ["git", "config", "--global", "init.defaultBranch", "main"]
    run_command(command, ROOT)
    command = ["git", "config", "--global", "core.editor", "\"vim\""]
    return run_command(command, ROOT)