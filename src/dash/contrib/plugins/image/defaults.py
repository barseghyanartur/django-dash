from django.utils.translation import gettext_lazy as _

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

FIT_METHOD_CROP_SMART = 'smart'
FIT_METHOD_CROP_CENTER = 'center'
FIT_METHOD_CROP_SCALE = 'scale'
FIT_METHOD_FIT_WIDTH = 'fit_width'
FIT_METHOD_FIT_HEIGHT = 'fit_height'

DEFAULT_FIT_METHOD = FIT_METHOD_CROP_CENTER

FIT_METHODS_CHOICES = (
    (FIT_METHOD_CROP_SMART, _("Smart crop")),
    (FIT_METHOD_CROP_CENTER, _("Crop center")),
    (FIT_METHOD_CROP_SCALE, _("Crop scale")),
    (FIT_METHOD_FIT_WIDTH, _("Fit width")),
    (FIT_METHOD_FIT_HEIGHT, _("Fit height")),
)

FIT_METHODS_CHOICES_WITH_EMPTY_OPTION = \
    [('', '---------')] + list(FIT_METHODS_CHOICES)

IMAGES_UPLOAD_DIR = 'dash-image-plugin-images'
