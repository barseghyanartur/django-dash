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
