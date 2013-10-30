from django.core.management.base import BaseCommand

from dash.utils import update_plugin_data

class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Updates the plugin data for all dashboard entries of all users. Rules for update are specified in the
        plugin itself.

        This command shall be ran if significant changes have been made to the system for which the data
        shall be updated.
        """
        update_plugin_data()
