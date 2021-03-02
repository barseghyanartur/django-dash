from django.core.management.base import BaseCommand

from ...utils import update_plugin_data_for_entries

__title__ = 'dash.management.commands.dash_update_plugin_data'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('Command',)


class Command(BaseCommand):
    """Update the plugin data for all dashboard entries of all users.

    Rules for update are specified in the plugin itself.

    This command shall be ran if significant changes have been made to the
    system for which the data shall be updated.
    """

    def handle(self, *args, **options):
        update_plugin_data_for_entries()
