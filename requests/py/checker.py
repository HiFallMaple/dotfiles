from .config import register
from pydotfiles import dpkg_check

operate = 'check'
package = 'requests'


@register.registe_method('ubuntu', operate, package)
def ubuntu_check_package():
    try:
        import requests
        return True
    except ImportError:
        return False
