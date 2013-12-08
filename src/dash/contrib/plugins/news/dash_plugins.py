__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseNewsPlugin',)

from django.utils.translation import ugettext_lazy as _

from slim.helpers import get_language_from_request

from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory
from dash.contrib.plugins.news.models import NewsItem
from dash.contrib.plugins.news.forms import NewsForm

# ********************************************************************************
# ****************************** Base News plugin ********************************
# ********************************************************************************

class BaseNewsPlugin(BaseDashboardPlugin):
    """
    Base news plugin.
    """
    name = _("News")
    form = NewsForm
    group = _("News")

    def post_processor(self):
        """
        Getting news items for the current active language.
        """
        results_kwargs = {}

        language = get_language_from_request(self.request)
        if language is not None:
            results_kwargs.update({'language': language})

        self.data.news_items = NewsItem._default_manager.filter(**results_kwargs) \
                                       .order_by('-date_published')[:self.data.max_items]

# ********************************************************************************
# ********** Generating and registering the plugins using factory ****************
# ********************************************************************************

sizes = (
    (2, 5),
    (4, 5)
)

plugin_factory(BaseNewsPlugin, 'news', sizes)
