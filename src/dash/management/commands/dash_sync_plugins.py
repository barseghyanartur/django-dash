from __future__ import absolute_import

from django.core.management.base import BaseCommand

from ...utils import sync_plugins

__title__ = 'dash.management.commands.dash_sync_plugins'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Command',)


class Command(BaseCommand):
    """Adds the missing plugins to database (``dash.models.DashboardPlugin``).

    This command shall be ran every
    time a developer adds a new plugin.
    """

    def handle(self, *args, **options):

        sync_plugins()
