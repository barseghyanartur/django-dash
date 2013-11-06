__all__ = ('FIT_METHOD_CROP', 'FIT_METHOD_FIT_WIDTH', 'FIT_METHOD_FIT_HEIGHT', 'DEFAULT_FIT_METHOD', \
           'FIT_METHODS_CHOICES', 'FIT_METHODS_CHOICES_WITH_EMPTY_OPTION', 'IMAGES_UPLOAD_DIR')

from django.utils.translation import ugettext_lazy as _

FIT_METHOD_CROP = 'crop'
FIT_METHOD_FIT_WIDTH = 'fit_width'
FIT_METHOD_FIT_HEIGHT = 'fit_height'

DEFAULT_FIT_METHOD = FIT_METHOD_CROP

FIT_METHODS_CHOICES = (
    (FIT_METHOD_CROP, _("Crop")),
    (FIT_METHOD_FIT_WIDTH, _("Fit width")),
    (FIT_METHOD_FIT_HEIGHT, _("Fit height")),
)

FIT_METHODS_CHOICES_WITH_EMPTY_OPTION = [('', '---------')] + list(FIT_METHODS_CHOICES)

IMAGES_UPLOAD_DIR = 'dash-image-plugin-images'
