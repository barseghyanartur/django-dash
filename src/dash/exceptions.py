__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('InvalidRegistryItemType', 'LayoutDoesNotExist', 'NoActiveLayout', \
           'PluginWidgetOutOfPlaceholderBoundaries')

class InvalidRegistryItemType(ValueError):
    """
    Raised when an attempt is made to register an item in the registry which does not have a proper type.
    """

class LayoutDoesNotExist(Exception):
    """
    Raised when layout does not exist.
    """

class NoActiveLayoutChosen(Exception):
    """
    Raised when no active layout is chosen.
    """

class PluginWidgetOutOfPlaceholderBoundaries(Exception):
    """
    Raised when plugin widget is out of placeholder boundaries.
    """
