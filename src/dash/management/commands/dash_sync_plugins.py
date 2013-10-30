from django.core.management.base import BaseCommand

from dash.utils import sync_plugins

class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Adds the missing plugins to database (``dash.models.DashboardPlugin``). This command shall be ran every
        time a developer adds a new plugin.
        """
        sync_plugins()
