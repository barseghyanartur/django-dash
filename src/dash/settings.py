"""
- `RESTRICT_PLUGIN_ACCESS` (bool): If set to True, (Django) permission system for dash plugins is enabled.
- `PLUGINS_MODULE_NAME` (str): Name of the module to placed in the (external) apps in which the dash plugin
  code should be implemented and registered.
- `ACTIVE_LAYOUT` (str): Active layout UID.
- `LAYOUTS_MODULE_NAME` (str): Name of the python module to be placed in (external) apps in which the dash
  layouts should be implemented and registered.
- `DEFAULT_WORKSPACE_NAME` (str): Name of the default workspace.
- `DEFAULT_PLACEHOLDER_VIEW_TEMPLATE_NAME` (str): Default template name for the placeholder view.
- `DEFAULT_PLACEHOLDER_EDIT_TEMPLATE_NAME` (str): Default template name for the placeholder edit.
- `LAYOUT_CELL_UNITS` (str): Layout cell units. Allowed values are `em`, `px`, `pt`, `%`.
- `DISPLAY_AUTH_LINK` (bool): If set to True, the log in or log out link is shown in the Dash drop-down
  menu.
- `DEBUG`
"""
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('RESTRICT_PLUGIN_ACCESS', 'PLUGINS_MODULE_NAME', 'ACTIVE_LAYOUT', 'LAYOUTS_MODULE_NAME', 
           'DEFAULT_WORKSPACE_NAME', 'DEFAULT_PLACEHOLDER_VIEW_TEMPLATE_NAME', \
           'DEFAULT_PLACEHOLDER_EDIT_TEMPLATE_NAME', 'LAYOUT_CELL_UNITS', 'DISPLAY_AUTH_LINK', \
           'DISPLAY_LOGOUT_LINK', 'WAIT_BETWEEN_TEST_STEPS', 'WAIT_AT_TEST_END', 'DEBUG')

from dash.conf import get_setting

RESTRICT_PLUGIN_ACCESS = get_setting('RESTRICT_PLUGIN_ACCESS')

PLUGINS_MODULE_NAME = get_setting('PLUGINS_MODULE_NAME')

ACTIVE_LAYOUT = get_setting('ACTIVE_LAYOUT')

LAYOUTS_MODULE_NAME = get_setting('LAYOUTS_MODULE_NAME')

DEFAULT_WORKSPACE_NAME = get_setting('DEFAULT_WORKSPACE_NAME')

DEFAULT_PLACEHOLDER_VIEW_TEMPLATE_NAME = get_setting('DEFAULT_PLACEHOLDER_VIEW_TEMPLATE_NAME')

DEFAULT_PLACEHOLDER_EDIT_TEMPLATE_NAME = get_setting('DEFAULT_PLACEHOLDER_EDIT_TEMPLATE_NAME')

LAYOUT_CELL_UNITS = get_setting('LAYOUT_CELL_UNITS')

DISPLAY_AUTH_LINK = get_setting('DISPLAY_AUTH_LINK')
DISPLAY_LOGOUT_LINK = DISPLAY_AUTH_LINK

WAIT_BETWEEN_TEST_STEPS = get_setting('WAIT_BETWEEN_TEST_STEPS')
WAIT_AT_TEST_END = get_setting('WAIT_AT_TEST_END')

DEBUG = get_setting('DEBUG')
