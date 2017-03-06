__title__ = 'dash.exceptions'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BaseException',
    'ImproperlyConfigured',
    'InvalidRegistryItemType',
    'LayoutDoesNotExist',
    'NoActiveLayout',
    'PluginWidgetOutOfPlaceholderBoundaries',
)


class BaseException(Exception):
    """Base django-dash exception."""


class InvalidRegistryItemType(ValueError):
    """Raised when an attempt is made to register an item of improper type.

    Raised when an attempt is made to register an item of improper type in
    the registry .
    """


class LayoutDoesNotExist(BaseException):
    """Raised when layout does not exist."""


class NoActiveLayoutChosen(BaseException):
    """Raised when no active layout is chosen."""


class PluginWidgetOutOfPlaceholderBoundaries(BaseException):
    """Raised when plugin widget is out of placeholder boundaries."""


class ImproperlyConfigured(BaseException):
    """Raised when ``django-dash`` is somehow improperly configured."""
