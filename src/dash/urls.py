from django.conf.urls import patterns, url

urlpatterns = patterns('dash.views',
    # Add dashboard entry.
    url(r'^entry/add/(?P<placeholder_uid>[\w_]+)/(?P<plugin_uid>[\w_\-]+)/ws/(?P<workspace>[\w_\-]+)/pos/(?P<position>\d+)/$', \
        view='add_dashboard_entry', name='dash.add_dashboard_entry'),
    url(r'^entry/add/(?P<placeholder_uid>[\w_]+)/(?P<plugin_uid>[\w_\-]+)/ws/(?P<workspace>[\w_\-]+)/$', \
        view='add_dashboard_entry', name='dash.add_dashboard_entry'),
    url(r'^entry/add/(?P<placeholder_uid>[\w_]+)/(?P<plugin_uid>[\w_\-]+)/pos/(?P<position>\d+)/$', \
        view='add_dashboard_entry', name='dash.add_dashboard_entry'),
    url(r'^entry/add/(?P<placeholder_uid>[\w_]+)/(?P<plugin_uid>[\w_\-]+)/$', view='add_dashboard_entry', \
        name='dash.add_dashboard_entry'),

    # Edit dashboard entry.
    url(r'^entry/edit/(?P<entry_id>\d+)/$', view='edit_dashboard_entry', name='dash.edit_dashboard_entry'),

    # Delete dashboard entry.
    url(r'^entry/delete/(?P<entry_id>\d+)/$', view='delete_dashboard_entry', name='dash.delete_dashboard_entry'),

    # ********************** Edit dashboard
    # Edit dashboard.
    url(r'^edit/(?P<workspace>[\w_\-]+)/$', view='edit_dashboard', name='dash.edit_dashboard'),
    url(r'^edit/$', view='edit_dashboard', name='dash.edit_dashboard'),

    # ********************** Widgets for dashboard entries
    url(r'^plugin-widgets/(?P<placeholder_uid>[\w_]+)/(?P<workspace>[\w_\-]+)/pos/(?P<position>\d+)/$', \
        view='plugin_widgets', name='dash.plugin_widgets'),
    # Workspace should not be named `pos`. Add check. TODO.
    url(r'^plugin-widgets/(?P<placeholder_uid>[\w_]+)/pos/(?P<position>\d+)/$', view='plugin_widgets', \
        name='dash.plugin_widgets'),
    url(r'^plugin-widgets/(?P<placeholder_uid>[\w_]+)/(?P<workspace>[\w_\-]+)/$', view='plugin_widgets', \
        name='dash.plugin_widgets'),
    url(r'^plugin-widgets/(?P<placeholder_uid>[\w_]+)/$', view='plugin_widgets', name='dash.widgets'),

    # ********************** Dashboard workspace
    # List workspaces.
    url(r'^workspaces/(?P<workspace>[\w_\-]+)/$', view='dashboard_workspaces', name='dash.dashboard_workspaces'),
    url(r'^workspaces/$', view='dashboard_workspaces', name='dash.dashboard_workspaces'),

    # Create dashboard workspace.
    url(r'^workspace/create/$', view='create_dashboard_workspace', name='dash.create_dashboard_workspace'),

    # Edit dashboard workspace.
    url(r'^workspace/edit/(?P<workspace_id>\d+)/$', view='edit_dashboard_workspace',
        name='dash.edit_dashboard_workspace'),

    # Delete dashboard workspace.
    url(r'^workspace/delete/(?P<workspace_id>\d+)/$', view='delete_dashboard_workspace',
        name='dash.delete_dashboard_workspace'),

    # View dashboard workspace.
    url(r'^workspace/(?P<workspace>[\w_\-]+)/$', view='dashboard', name='dash.dashboard'),

    # Edit dashboard settings.
    url(r'^settings/edit/$', view='edit_dashboard_settings', name='dash.edit_dashboard_settings'),

    # View default dashboard (no workspace selected == default workspace used).
    url(r'^$', view='dashboard', name='dash.dashboard'),
)
