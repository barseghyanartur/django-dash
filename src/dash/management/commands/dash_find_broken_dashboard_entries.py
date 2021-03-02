from six import print_

from django.core.management.base import BaseCommand

from ...base import get_registered_layout_uids, get_registered_plugin_uids
from ...models import DashboardEntry

__title__ = 'dash.management.commands.dash_find_broken_dashboard_entries'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('Command',)


class Command(BaseCommand):
    """Add the missing plugins to database (``dash.models.DashboardPlugin``).

    This command shall be ran every time a developer adds a new plugin.
    """

    def handle(self, *args, **options):

        dashboard_entries = DashboardEntry._default_manager \
            .all() \
            .only('id', 'plugin_uid', 'layout_uid') \
            .values_list('id', 'plugin_uid', 'layout_uid')

        broken_plugin_entries = []
        broken_layout_entries = []

        registered_plugin_uids = get_registered_plugin_uids()
        registered_layout_uids = get_registered_layout_uids()

        for entry_id, plugin_uid, layout_uid in dashboard_entries:
            if plugin_uid not in registered_plugin_uids:
                broken_plugin_entries.append((entry_id, plugin_uid))

            if layout_uid not in registered_layout_uids:
                broken_layout_entries.append((entry_id, layout_uid))

        if broken_plugin_entries:
            print_("Broken plugin entries found!", broken_plugin_entries)

        if broken_layout_entries:
            print_("Broken layout entries found!", broken_layout_entries)
