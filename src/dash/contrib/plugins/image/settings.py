"""
- ``FIT_METHOD_CROP_SMART`` (string)
- ``FIT_METHOD_CROP_CENTER`` (string)
- ``FIT_METHOD_CROP_SCALE`` (string)
- ``FIT_METHOD_FIT_WIDTH`` (string)
- ``FIT_METHOD_FIT_HEIGHT`` (string)
- ``DEFAULT_FIT_METHOD`` (string)
- ``FIT_METHODS_CHOICES`` (tuple)
- ``FIT_METHODS_CHOICES_WITH_EMPTY_OPTION`` (list)
- ``IMAGES_UPLOAD_DIR`` (string)
"""
from .conf import get_setting

__title__ = 'dash.contrib.plugins.image.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'DEFAULT_FIT_METHOD',
    'FIT_METHOD_CROP_CENTER',
    'FIT_METHOD_CROP_SCALE',
    'FIT_METHOD_CROP_SMART',
    'FIT_METHOD_FIT_HEIGHT',
    'FIT_METHOD_FIT_WIDTH',
    'FIT_METHODS_CHOICES',
    'FIT_METHODS_CHOICES_WITH_EMPTY_OPTION',
    'IMAGES_UPLOAD_DIR',
)

FIT_METHOD_CROP_SMART = get_setting('FIT_METHOD_CROP_SMART')
FIT_METHOD_CROP_CENTER = get_setting('FIT_METHOD_CROP_CENTER')
FIT_METHOD_CROP_SCALE = get_setting('FIT_METHOD_CROP_SCALE')
FIT_METHOD_FIT_WIDTH = get_setting('FIT_METHOD_FIT_WIDTH')
FIT_METHOD_FIT_HEIGHT = get_setting('FIT_METHOD_FIT_HEIGHT')
DEFAULT_FIT_METHOD = get_setting('DEFAULT_FIT_METHOD')
FIT_METHODS_CHOICES = get_setting('FIT_METHODS_CHOICES')
FIT_METHODS_CHOICES_WITH_EMPTY_OPTION = get_setting(
    'FIT_METHODS_CHOICES_WITH_EMPTY_OPTION'
)
IMAGES_UPLOAD_DIR = get_setting('IMAGES_UPLOAD_DIR')
