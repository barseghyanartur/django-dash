from django.core.management.base import BaseCommand

from ....utils import sync_plugins


class Command(BaseCommand):
    """Adds the missing plugins to database (``dash.models.DashboardPlugin``).

    This command shall be ran every
    time a developer adds a new plugin.
    """

    def handle(self, *args, **options):

        sync_plugins()
