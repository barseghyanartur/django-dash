"""
Compatibility module for safe and sane User model import.
"""

from django.core.exceptions import ImproperlyConfigured

from nine.user import User

__title__ = 'dash.compat'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('User',)


# Sanity checks. Possibly rely on the dynamic username field in future.
user = User()

if not hasattr(user, 'username'):
    from .exceptions import ImproperlyConfigured
    raise ImproperlyConfigured(
        "Your custom user model ({0}.{1}) doesn't have ``username`` "
        "property, while ``django-dash`` relies on its' presence."
        "".format(user._meta.app_label, user._meta.object_name)
    )
