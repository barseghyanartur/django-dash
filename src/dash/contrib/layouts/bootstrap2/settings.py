__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('IMAGE_CHOICES', 'IMAGE_CHOICES_WITH_EMPTY_OPTION')

from dash.contrib.layouts.bootstrap2.conf import get_setting

IMAGE_CHOICES = get_setting('IMAGE_CHOICES')
IMAGE_CHOICES_WITH_EMPTY_OPTION = get_setting('IMAGE_CHOICES_WITH_EMPTY_OPTION')
