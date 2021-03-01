"""
This file was generated with the custommenu management command, it contains
the classes for the admin menu, you can customize this class as you want.

To activate your custom menu add the following to your settings.py::

    ADMIN_TOOLS_MENU = 'admin_tools_dashboard.menu.CustomMenu'
"""
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from admin_tools.menu import items, Menu

from admin_tools_dashboard import conf


class CustomMenu(Menu):
    """Custom Menu."""

    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Dashboard'), reverse('admin:index')),
        ]

        # Foo
        self.children.append(
            items.ModelList(
                _('Foo'),
                models=conf.foo_apps
            )
        )

        # News
        self.children.append(
            items.ModelList(
                _('News'),
                models=conf.news_apps
            )
        )

        # Bookmark
        self.children.append(
            items.ModelList(
                _('Bookmark'),
                models=conf.bookmark_apps
            )
        )

        # Dash
        self.children.append(
            items.ModelList(
                _('Dash'),
                models=conf.dash_apps
            )
        )

        # Registration
        self.children.append(
            items.ModelList(
                _('Registration'),
                models=conf.registration_apps
            )
        )

        # Append an app list module for "Administration"
        self.children.append(
            items.AppList(
                _('Administration'),
                models=['django.contrib.*']
            )
        )

    def init_with_context(self, context):
        """Use this method if you need to access the request context."""
        return super(CustomMenu, self).init_with_context(context)
