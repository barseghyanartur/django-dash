from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _

from ....base import BaseDashboardPlugin
from ....factory import plugin_factory

from .forms import URLForm, BookmarkForm
from .models import Bookmark

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('BaseURLPlugin',)

# ****************************************************************************
# ********************************* URL plugin *******************************
# ****************************************************************************


class BaseURLPlugin(BaseDashboardPlugin):
    """Base URL plugin."""

    name = _("URL")
    group = _("URLs")
    form = URLForm

    @property
    def html_class(self):
        """HTML class.

        If plugin has an image, we add a class ``iconic`` to it.
        """
        html_class = super(BaseURLPlugin, self).html_class
        if self.data.image:
            html_class += ' iconic-url'
        return html_class

# ****************************************************************************
# ********** Generating and registering the URL plugins using factory ********
# ****************************************************************************


sizes = (
    (1, 1),
    (2, 2)
)

plugin_factory(BaseURLPlugin, 'url', sizes)


# ****************************************************************************
# ********************************* Bookmark plugin **************************
# ****************************************************************************


class BaseBookmarkPlugin(BaseDashboardPlugin):
    """Base URL plugin."""

    name = _("Bookmark")
    group = _("URLs")
    form = BookmarkForm

    @property
    def html_class(self):
        """HTML class.

        If plugin has an image, we add a class `iconic` to it.
        """
        html_class = super(BaseBookmarkPlugin, self).html_class
        if self.data.image:
            html_class += ' iconic-url'
        return html_class

    def update_plugin_data(self, dashboard_entry):
        """Update plugin data.

        Should return a dictionary with the plugin data which is supposed to
        be updated.
        """
        try:
            bookmark = Bookmark._default_manager.get(pk=self.data.bookmark)
        except ObjectDoesNotExist:
            return

        if bookmark:
            data = {
                'bookmark': bookmark.pk,
                'title': bookmark.title,
                'url': bookmark.url,
                'external': bookmark.external,
                'image': bookmark.image
            }
            return data

# ****************************************************************************
# ******* Generating and registering the Bookmark plugins using factory ******
# ****************************************************************************


sizes = (
    (1, 1),
    # (2, 2)
)

plugin_factory(BaseBookmarkPlugin, 'bookmark', sizes)
