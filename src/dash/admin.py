from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from dash.models import DashboardWorkspace, DashboardEntry, DashboardPlugin, DashboardSettings

class DashboardWorkspaceAdmin(admin.ModelAdmin):
    """
    Dashboard workspace admin.
    """
    list_display = ('name', 'slug', 'layout_uid', 'position', 'user', 'is_public')
    list_editable = ('position',)
    list_filter = ('layout_uid', 'is_public')
    readonly_fields = ('slug',)
    fieldsets = (
        (None, {
            'fields': ('name', 'position', 'is_public')
        }),
        (_("User"), {
            'fields': ('user',)
        }),
        (_('Additional'), {
            'classes': ('collapse',),
            'fields': ('slug',)
        }),
    )

    class Meta:
        app_label = _('Dashboard workspace')


admin.site.register(DashboardWorkspace, DashboardWorkspaceAdmin)

class DashboardEntryAdmin(admin.ModelAdmin):
    """
    Dashboard entry admin.
    """
    list_display = ('plugin_uid', 'plugin_uid_code', 'plugin_data', 'layout_uid', 'placeholder_uid', 'position',
                    'workspace', 'user')
    list_filter = ('user', 'workspace', 'layout_uid', 'placeholder_uid', 'plugin_uid')
    list_editable = ('position',)
    readonly_fields = ('plugin_uid_code',)
    fieldsets = (
        (None, {
            'fields': ('plugin_uid', 'plugin_data', 'layout_uid', 'placeholder_uid', 'position', 'workspace')
        }),
        (_("User"), {
            'fields': ('user',)
        }),
    )

    class Meta:
        app_label = _('Dashboard entry')

    def queryset(self, request):
        queryset = super(DashboardEntryAdmin, self).queryset(request)
        queryset = queryset.select_related('workspace', 'user')
        return queryset


admin.site.register(DashboardEntry, DashboardEntryAdmin)

class DashboardPluginAdmin(admin.ModelAdmin):
    """
    Dashboard plugin admin.
    """
    list_display = ('plugin_uid_admin', 'users_list', 'groups_list')
    readonly_fields = ('plugin_uid', 'plugin_uid_admin')
    fieldsets = (
        (None, {
            'fields': ('plugin_uid', 'users', 'groups')
        }),
    )
    filter_horizontal = ('users', 'groups',)

    class Meta:
        app_label = _('Dashboard plugin')

    def queryset(self, request):
        queryset = super(DashboardPluginAdmin, self).queryset(request)
        queryset = queryset.prefetch_related('users', 'groups')
        return queryset


admin.site.register(DashboardPlugin, DashboardPluginAdmin)

class DashboardSettingsAdmin(admin.ModelAdmin):
    """
    Dashboard plugin admin.
    """
    list_display = ('title', 'user', 'layout_uid', 'is_public')
    #readonly_fields = ('plugin_uid',)
    fieldsets = (
        (None, {
            'fields': ('title', 'user', 'layout_uid', 'is_public')
        }),
    )

    class Meta:
        app_label = _('Dashboard settings')

    def queryset(self, request):
        queryset = super(DashboardSettingsAdmin, self).queryset(request)
        queryset = queryset.select_related('user')
        return queryset


admin.site.register(DashboardSettings, DashboardSettingsAdmin)
