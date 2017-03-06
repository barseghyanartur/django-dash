from django.core.management.base import BaseCommand

from ...utils import update_plugin_data_for_entries


class Command(BaseCommand):
    """Update the plugin data for all dashboard entries of all users.

    Rules for update are specified in the plugin itself.

    This command shall be ran if significant changes have been made to the
    system for which the data shall be updated.
    """

    def handle(self, *args, **options):

        update_plugin_data_for_entries()
