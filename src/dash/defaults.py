__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('RESTRICT_PLUGIN_ACCESS', 'PLUGINS_MODULE_NAME', 'LAYOUTS_MODULE_NAME', 'ACTIVE_LAYOUT', \
           'LAYOUT_CELL_UNITS', 'DEFAULT_WORKSPACE_NAME', 'DEFAULT_PLACEHOLDER_VIEW_TEMPLATE_NAME', \
           'DEFAULT_PLACEHOLDER_EDIT_TEMPLATE_NAME', 'DISPLAY_AUTH_LINK', 'WAIT_BETWEEN_TEST_STEPS', \
           'WAIT_AT_TEST_END', 'DEBUG')

gettext = lambda s: s

# If set to True, plugins would be only accessible by the white-listed user(s) or group(s). If set to False, all
# users have the same access rights to all plugins.
RESTRICT_PLUGIN_ACCESS = True

# Name of the module in which the dash plugins are registered.
PLUGINS_MODULE_NAME = 'dash_plugins'

# Name of the module in which the dash layouts are registered.
LAYOUTS_MODULE_NAME = 'dash_layouts'

# UID of the active layout.
ACTIVE_LAYOUT = 'android'

# Allowed layout cell units.
LAYOUT_CELL_UNITS = ('em', 'px', 'pt', '%')

# Name of the default dashboard workspace (no workspace).
DEFAULT_WORKSPACE_NAME = 'Default'

DEFAULT_PLACEHOLDER_VIEW_TEMPLATE_NAME = 'dash/layouts/base_placeholder_view.html'
DEFAULT_PLACEHOLDER_EDIT_TEMPLATE_NAME = 'dash/layouts/base_placeholder_edit.html'

# If set to True, the logout link is shown in the menu.
DISPLAY_AUTH_LINK = True

WAIT_BETWEEN_TEST_STEPS = 2
WAIT_AT_TEST_END = 4

DEBUG = False
