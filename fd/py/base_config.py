import logging
import logging.config
import os
from pydotfiles import Register, get_dependencies, LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
current_dir: str = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
dependency: list = get_dependencies(parent_dir)
register = Register()