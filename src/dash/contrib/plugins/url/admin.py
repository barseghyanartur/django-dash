import logging

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ....models import DashboardEntry
from ....utils import update_plugin_data_for_entries

from .models import Bookmark

__title__ = 'dash.contrib.plugins.urls.admin'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('BookmarkAdmin',)

logger = logging.getLogger(__name__)


class BookmarkAdmin(admin.ModelAdmin):
    """Bookmark admin."""

    list_display = ('title', 'url', 'external', 'image')
    fieldsets = (
        (None, {
            'fields': ('title', 'url', 'external', 'image')
        }),
    )

    class Meta:
        """Meta."""

        app_label = _('Bookmark')

    def save_model(self, request, obj, form, change):
        """Updating the bookmark plugin entries on bookmarks update."""
        super(BookmarkAdmin, self).save_model(request, obj, form, change)

        dashboard_entries = DashboardEntry._default_manager.filter(
            plugin_uid__startswith='bookmark_'
        )
        try:
            update_plugin_data_for_entries(
                dashboard_entries=dashboard_entries,
                request=request
            )
        except Exception as err:
            logger.debug(str(err))


admin.site.register(Bookmark, BookmarkAdmin)
