from .base import *

# Do not put any settings below this line
try:
    from .local_settings import *
except ImportError:
    pass
TEMPLATE_DEBUG = True
if DEBUG and DEBUG_TOOLBAR:
    try:
        # Make sure the django-debug-toolbar is installed
        import debug_toolbar

        # debug_toolbar
        MIDDLEWARE += (
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        )

        INSTALLED_APPS += (
            'debug_toolbar',
            'template_debug',
        )

        DEBUG_TOOLBAR_CONFIG = {
            'INTERCEPT_REDIRECTS': False,
        }

    except ImportError:
        pass
