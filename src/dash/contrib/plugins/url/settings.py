from .conf import get_setting

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'BOOKMARK_IMAGE_CHOICES',
    'BOOKMARK_IMAGE_CHOICES_WITH_EMPTY_OPTION',
    'IMAGE_CHOICES',
    'IMAGE_CHOICES_WITH_EMPTY_OPTION',
)

IMAGE_CHOICES = get_setting('IMAGE_CHOICES')
IMAGE_CHOICES_WITH_EMPTY_OPTION = get_setting(
    'IMAGE_CHOICES_WITH_EMPTY_OPTION'
)
BOOKMARK_IMAGE_CHOICES = get_setting('BOOKMARK_IMAGE_CHOICES')
BOOKMARK_IMAGE_CHOICES_WITH_EMPTY_OPTION = get_setting(
    'BOOKMARK_IMAGE_CHOICES_WITH_EMPTY_OPTION'
)
