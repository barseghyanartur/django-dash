__title__ = 'dash.compat'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('User',)

try:
    # Django 1.7 check
    from django.apps import AppConfig
    from django.conf import settings
    User = settings.AUTH_USER_MODEL
except ImportError:
    # Safe User import for Django < 1.5
    try:
        from django.contrib.auth import get_user_model
    except ImportError:
        from django.contrib.auth.models import User
    else:
        User = get_user_model()

    user = User()

    if not hasattr(user, 'username'):
        from dash.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured("Your custom user model ({0}.{1}) doesn't have ``username`` "
                                   "property, while ``django-dash`` relies on its' "
                                   "presence.".format(user._meta.app_label, user._meta.object_name))
