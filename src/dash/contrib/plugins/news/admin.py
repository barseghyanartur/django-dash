__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from slim.admin import SlimAdmin

from dash.contrib.plugins.news.models import NewsItem

class NewsItemAdmin(SlimAdmin):
    """
    Foo item admin.
    """
    # If you don't inherit the SlimAdmin, append 'language' and 'available_translations_admin' to ``list_display``.
    list_display = ('title', 'admin_image_preview', 'date_published')

    # If you don't inherit the SlimAdmin, append 'available_translations_exclude_current_admin' to ``readonly_fields``.
    readonly_fields = ('date_created', 'date_updated', )

    ordering = ('-date_published',)

    prepopulated_fields = {'slug': ('title',)}

    collapse_slim_fieldset = False

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
        app_label = _('News item')


admin.site.register(NewsItem, NewsItemAdmin)
