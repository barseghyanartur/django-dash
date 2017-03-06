from autoslug.settings import slugify

from django.utils.encoding import force_text

from six import PY3

__title__ = 'dash.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'clean_plugin_data',
    'clone_plugin_data',
    'iterable_to_dict',
    'lists_overlap',
    'safe_text',
    'slugify_workspace',
    'uniquify_sequence',
    'update_plugin_data',
)


def slugify_workspace(val):
    """Slugify workspace."""
    return slugify(val.lower()).lower()


def safe_text(text):
    """Safe text (encode).

    :return str:
    """
    if PY3:
        return force_text(text, encoding='utf-8')
    else:
        return force_text(text, encoding='utf-8').encode('utf-8')


def lists_overlap(sub, main):
    for i in sub:
        if i in main:
            return True
    return False


def iterable_to_dict(items, key_attr_name):
    """Convert iterable of certain objects to dict.

    :param iterable items:
    :param string key_attr_name: Attribute to use as a dictionary key.
    :return dict:
    """
    items_dict = {}
    for item in items:
        items_dict.update({getattr(item, key_attr_name): item})
    return items_dict


def uniquify_sequence(sequence):
    """Makes the sequence unique.

    Makes sure items in the given sequence are unique, having the original
    order preserved.

    :param iterable sequence:
    :return list:
    """
    seen = set()
    seen_add = seen.add
    return [x for x in sequence if x not in seen and not seen_add(x)]


def clean_plugin_data(dashboard_entries, request=None):
    """Clean up the plugin data.

    Clean up the plugin data (database, files) for the dashboard_entries given.

    :param iterable dashboard_entries:
    :param django.http.HttpRequest request:
    :return bool: Boolean True if no errors occurred and False otherwise.
    """
    errors = False
    for dashboard_entry in dashboard_entries:
        plugin = dashboard_entry.get_plugin(request=request)

        if plugin:
            plugin._delete_plugin_data()

    return not errors


def clone_plugin_data(dashboard_entry, request=None):
    """Clone plugin data of a dashboard entry."""
    if dashboard_entry:
        plugin = dashboard_entry.get_plugin(request=request)

        if plugin:
            plugin_data = plugin._clone_plugin_data(dashboard_entry)

            if plugin_data is None:
                plugin_data = dashboard_entry.plugin_data

            return plugin_data


def update_plugin_data(dashboard_entry, request=None):
    """Update plugin data of a dashboard entry."""
    if dashboard_entry:
        plugin = dashboard_entry.get_plugin(request=request)

        if plugin:
            return plugin._update_plugin_data(dashboard_entry)
