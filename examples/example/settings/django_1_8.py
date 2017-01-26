from .base import *

INSTALLED_APPS = list(INSTALLED_APPS)

try:
    INSTALLED_APPS.remove('south')
except Exception:
    pass

# INSTALLED_APPS.remove('news')
