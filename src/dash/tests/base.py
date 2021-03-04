from django.contrib.auth import get_user_model
from django.core.management import call_command

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'DASH_TEST_USER_USERNAME',
    'DASH_TEST_USER_PASSWORD',
    'log_info',
    'create_dashboard_user',
    'setup_dash',
)

DASH_TEST_USER_USERNAME = 'test_admin'
DASH_TEST_USER_PASSWORD = 'test'
TRACK_TIME = False


def log_info(func):
    """Prints some useful info."""
    if not log_info:
        return func

    def inner(self, *args, **kwargs):
        result = func(self, *args, **kwargs)

        print('\n{0}'.format(func.__name__))
        print('============================')
        if func.__doc__:
            print('""" {0} """'.format(func.__doc__.strip()))
        print('----------------------------')
        if result is not None:
            print(result)
        print('\n')

        return result
    return inner


def create_dashboard_user():
    """
    Create a user for testing the dashboard.

    TODO: At the moment an admin account is being tested. Automated tests with
    diverse accounts are to be implemented.
    """
    User = get_user_model()
    u = User()
    u.username = DASH_TEST_USER_USERNAME
    u.email = 'admin@dev.django-dash.com'
    u.is_superuser = True
    u.is_staff = True
    u.set_password(DASH_TEST_USER_PASSWORD)

    try:
        u.save()
    except Exception as err:
        pass


DASH_SET_UP = False


def setup_dash():
    """Set up dash."""
    call_command('dash_sync_plugins', verbosity=3, interactive=False)
