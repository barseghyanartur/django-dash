from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import NewsItem

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('NewsItemAdmin',)


class NewsItemAdmin(admin.ModelAdmin):
    """Foo item admin."""

    list_display = ('title', 'admin_image_preview', 'date_published')

    readonly_fields = ('date_created', 'date_updated', )

    ordering = ('-date_published',)

    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'body', 'image')
        }),
        (_("Publication date"), {
            'classes': ('',),
            'fields': ('date_published',)
        }),
        (_("Additional"), {
            'classes': ('collapse',),
            'fields': ('date_created', 'date_updated')
        })
    )

    class Meta:
        """Meta."""

        app_label = _('News item')


admin.site.register(NewsItem, NewsItemAdmin)
