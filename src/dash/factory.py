import logging

from six import with_metaclass

from .base import plugin_registry, plugin_widget_registry

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'plugin_factory',
    'plugin_widget_factory'
)

logger = logging.getLogger(__name__)


def plugin_factory(base_class, plugin_uid_prefix, sizes=[]):
    """
    Plugin factory.

    :param dash.base.BaseDashboardWidget base_class: Subclass of.
    :param class base_class:
    :param string plugin_uid_prefix:
    :param list sizes:
    :param iterable sizes: Iterable of tuples.

    :example:
    >>> from dash.contrib.plugins.image.dash_plugins import BaseImagePlugin
    >>> plugin_factory(
    >>>     BaseImagePlugin, 'image', zip(range(6, 10), range(6, 10))
    >>> )

    The example above will update the plugin registry with the following
    dictionary:
    >>> {
    >>>     'image_6x6': dash.factory.Plugin,
    >>>     'image_7x7': dash.factory.Plugin,
    >>>     'image_8x8': dash.factory.Plugin,
    >>>     'image_9x9': dash.factory.Plugin,
    >>> }

    The generated class (one of them), would look as follows:

    >>> class Plugin(BaseImagePlugin):
    >>>     uid = 'image_6x6'

    The ``uid`` property is generated automatically.
    """
    for cols, rows in sizes:

        plugin_uid = "{plugin_uid_prefix}_{cols}x{rows}".format(
            plugin_uid_prefix=plugin_uid_prefix,
            cols=cols,
            rows=rows
        )

        class PluginMeta(type):
            """Dynamically created plugin plugin meta class."""

            def __new__(cls, name, bases, props):
                props['uid'] = plugin_uid
                return type.__new__(cls, name, bases, props)

        class Plugin(with_metaclass(PluginMeta, base_class)):
            """Dynamically created plugin class."""

        plugin_registry.register(Plugin)


def plugin_widget_factory(base_class,
                          layout_uid,
                          placeholder_uid,
                          plugin_uid_prefix,
                          sizes=[]):
    """Plugin widget factory.

    :param dash.base.BaseDashboardWidget base_class: Subclass of.
    :param string layout_uid: Layout UID, for which widgets are generated.
    :param string placeholder_uid: Placeholder UID, for which widgets are
        generated.
    :param string plugin_uid_prefix: Prefix of the plugin UID.
    :param iterable sizes: Iterable of tuples.

    :example:
    >>> from dash.contrib.plugins.image.dash_widgets import BaseImageWidget
    >>> plugin_widget_factory(
    >>>     BaseImageWidget,
    >>>     'android',
    >>>     'main',
    >>>     'image',
    >>>     zip(range(6, 10), range(6, 10))
    >>> )

    The example above will update the plugin widget registry with the
    following dictionary:

    >>> {
    >>>     'android.main.image_6x6': dash.factory.Widget,
    >>>     'android.main.image_7x7': dash.factory.Widget,
    >>>     'android.main.image_8x8': dash.factory.Widget,
    >>>     'android.main.image_9x9': dash.factory.Widget,
    >>> }

    The generated class (one of them), would look as follows:

    >>> class Widget(BaseImageWidget):
    >>>     layout_uid = 'android'
    >>>     placeholder_uid = 'main'
    >>>     plugin_uid = 'image_6x6'
    >>>     cols = 6
    >>>     rows = 6

    The ``layout_uid``, ``placeholder_uid``, ``plugin_uid``, ``cols``
    and ``rows`` properties are generated automatically.
    """
    for cols, rows in sizes:
        plugin_uid = "{plugin_uid_prefix}_{cols}x{rows}".format(
            plugin_uid_prefix=plugin_uid_prefix,
            cols=cols,
            rows=rows
        )

        # class_name = "{plugin_uid_prefix}{cols}x{rows}{layout_uid}" \
        #              "{placeholder_uid}Widget".format(
        #                 plugin_uid_prefix=plugin_uid_prefix.title(),
        #                 cols=cols,
        #                 rows=rows,
        #                 layout_uid=layout_uid.title(),
        #                 placeholder_uid=placeholder_uid.title()
        #              )

        class WidgetMeta(type):
            """Dynamically created plugin widget meta class."""

            def __new__(cls, name, bases, props):
                props['layout_uid'] = layout_uid
                props['placeholder_uid'] = placeholder_uid
                props['plugin_uid'] = plugin_uid
                props['cols'] = cols
                props['rows'] = rows
                return type.__new__(cls, name, bases, props)

        class Widget(with_metaclass(WidgetMeta, base_class)):
            """Dynamically created widget class."""

        plugin_widget_registry.register(Widget)
