from six import print_

from django.core.management.base import BaseCommand

from dash.models import DashboardEntry
from dash.base import get_registered_layout_uids, get_registered_plugin_uids

class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Adds the missing plugins to database (``dash.models.DashboardPlugin``). This command shall be ran every
        time a developer adds a new plugin.
        """
        dashboard_entries = DashboardEntry._default_manager.all().only('id', 'plugin_uid', 'layout_uid') \
                                         .values_list('id', 'plugin_uid', 'layout_uid')
        broken_plugin_entries = []
        broken_layout_entries = []

        registered_plugin_uids = get_registered_plugin_uids()
        registered_layout_uids = get_registered_layout_uids()

        for entry_id, plugin_uid, layout_uid in dashboard_entries:
            if not plugin_uid in registered_plugin_uids:
                broken_plugin_entries.append((entry_id, plugin_uid))

            if not layout_uid in registered_layout_uids:
                broken_layout_entries.append((entry_id, layout_uid))

        if broken_plugin_entries:
            print_("Broken plugin entries found!", broken_plugin_entries)

        if broken_layout_entries:
            print_("Broken layout entries found!", broken_layout_entries)
