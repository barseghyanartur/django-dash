"""
Compatibility module for safe and sane User model import.
"""

__title__ = 'dash.compat'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('User',)

from django.core.exceptions import ImproperlyConfigured

from nine.user import User

# Sanity checks. Possibly rely on the dynamic username field in future.
user = User()

if not hasattr(user, 'username'):
    from dash.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured(
        "Your custom user model ({0}.{1}) doesn't have ``username`` "
        "property, while ``django-dash`` relies on its' presence."
        "".format(user._meta.app_label, user._meta.object_name)
        )
