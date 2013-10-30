__all__ = ('IMAGE_CHOICES', 'IMAGE_CHOICES_WITH_EMPTY_OPTION')

from dash.contrib.plugins.url.conf import get_setting

IMAGE_CHOICES = get_setting('IMAGE_CHOICES')
IMAGE_CHOICES_WITH_EMPTY_OPTION = get_setting('IMAGE_CHOICES_WITH_EMPTY_OPTION')
