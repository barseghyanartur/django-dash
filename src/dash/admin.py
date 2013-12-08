__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

from django.contrib import admin
from django.contrib.admin import helpers
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.conf.urls import patterns, url
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages

from dash.models import DashboardWorkspace, DashboardEntry, DashboardPlugin, DashboardSettings
from dash.forms import BulkChangeDashboardPluginsForm
from dash.constants import ACTION_CHOICE_REPLACE

staff_member_required_m = method_decorator(staff_member_required)

# *********************************************************
# ************************ Admin helpers ******************
# *********************************************************

def bulk_change_dashboard_plugins(modeladmin, request, queryset):
    """
    Bulk change of dashboard plugins action additional view. Data is changed in
    ``DashboardPluginAdmin.bulk_change_dashboard_plugins`` method.
    """
    opts = modeladmin.model._meta
    app_label = opts.app_label

    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    post = dict(request.POST)
    if selected:
        post['selected_dashboard_plugins'] = ','.join(selected)
    if 'POST' == request.method:
        form = BulkChangeDashboardPluginsForm(
            data = post,
            files = request.FILES,
            initial={'selected_dashboard_plugins': ','.join(selected)}
            )
    else:
        form = BulkChangeDashboardPluginsForm(initial={'selected_dashboard_plugins': ','.join(selected)})

    context = {
        'form': form,
        'app_label': app_label,
        'opts': opts,
        'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
    }
    return render_to_response(
        'dash/admin/bulk_change_dashboard_plugins.html', context, context_instance=RequestContext(request)
        )

# *********************************************************
# *********************************************************

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

# *********************************************************

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

# *********************************************************

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
    actions = [bulk_change_dashboard_plugins]

    class Meta:
        app_label = _('Dashboard plugin')

    def queryset(self, request):
        queryset = super(DashboardPluginAdmin, self).queryset(request)
        queryset = queryset.prefetch_related('users', 'groups')
        return queryset

    @staff_member_required_m
    def bulk_change_dashboard_plugins(self, request):
        """
        This is where the data is actually processed.
        """
        if 'POST' == request.method:
            form_cls = BulkChangeDashboardPluginsForm
            form = form_cls(
                data = request.POST,
                files = request.FILES
                )
            if form.is_valid():
                ids = form.cleaned_data.pop('selected_dashboard_plugins').split(',')
                users = form.cleaned_data.pop('users')
                groups = form.cleaned_data.pop('groups')
                users_action = form.cleaned_data.pop('users_action')
                groups_action = form.cleaned_data.pop('groups_action')
                cleaned_data = dict((key, val) for (key, val) in form.cleaned_data.iteritems() if val is not None)

                # Queryset to work with
                queryset = DashboardPlugin._default_manager.filter(pk__in=ids)

                # Update simple fields
                updated = queryset.update(**cleaned_data)

                # Update groups
                for dashboard_plugin in queryset:
                    # If groups action chose is ``replace``, clearing the groups first.
                    if groups_action == ACTION_CHOICE_REPLACE:
                        dashboard_plugin.groups.clear()

                    # If users action chose is ``replace``, clearing the users first.
                    if users_action == ACTION_CHOICE_REPLACE:
                        dashboard_plugin.users.clear()

                    dashboard_plugin.groups.add(*groups) # Adding groups
                    dashboard_plugin.users.add(*users) # Adding users

                messages.info(request, _('{0} Dashboard plugins were changed successfully.').format(len(ids)))
                return redirect('admin:dash_dashboardplugin_changelist')
        else:
            messages.warning(request, _('POST required when changing in bulk!'))
            return redirect('admin:dash_dashboardplugin_changelist')

    def get_urls(self):
        my_urls = patterns('',
            # Bulk change dashboard plugins
            url(r'^bulk-change-dashboard-plugins/$', self.bulk_change_dashboard_plugins,
                name='bulk_change_dashboard_plugins'),
        )
        return my_urls + super(DashboardPluginAdmin, self).get_urls()


admin.site.register(DashboardPlugin, DashboardPluginAdmin)

# *********************************************************

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
