from __future__ import absolute_import

from django.core.management.base import BaseCommand

from ...utils import sync_plugins

__title__ = 'dash.management.commands.dash_sync_plugins'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('Command',)


class Command(BaseCommand):
    """Adds the missing plugins to database (``dash.models.DashboardPlugin``).

    This command shall be ran every
    time a developer adds a new plugin.
    """

    def add_arguments(self, parser):
        parser.add_argument(
            '--noinput',
            '--no-input',
            action='store_false',
            dest='interactive',
            help='Tells Django to NOT prompt the user for input of any '
                 'kind.',
        )

    def handle(self, *args, **options):
        sync_plugins()
