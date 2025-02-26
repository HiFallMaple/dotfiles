from .config import appList, register
from pydotfiles import dpkg_check

operate = 'check'

def check_func_factory(app):
    @register.registe_method(['ubuntu22', 'ubuntu24'], operate, app)
    def ubuntu_check_package():
        return dpkg_check(app)

for app in appList:
    check_func_factory(app)