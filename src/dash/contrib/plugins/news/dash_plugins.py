__all__ = ('NewsPlugin', 'HugeNewsPlugin')

from django.utils.translation import ugettext_lazy as _

from slim.helpers import get_language_from_request

from dash.base import BaseDashboardPlugin, plugin_registry, plugin_widget_registry
from dash.contrib.plugins.news.models import NewsItem
from dash.contrib.plugins.news.forms import NewsForm
from dash.contrib.plugins.news.dash_widgets import NewsAndroidMainWidget, HugeNewsAndroidMainWidget

# ***************************************************************************
# ******************************* News plugin *******************************
# ***************************************************************************

class NewsPlugin(BaseDashboardPlugin):
    """
    News plugin.
    """
    uid = 'news'
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


plugin_registry.register(NewsPlugin)

# ***************************************************************************
# ******************************* Huge news plugin **************************
# ***************************************************************************

class HugeNewsPlugin(BaseDashboardPlugin):
    """
    News plugin.
    """
    uid = 'huge_news'
    name = _("News")
    form = NewsForm
    group = _("News")


plugin_registry.register(HugeNewsPlugin)

# *************************************************************************
# ****************** Registering the widgets ******************************
# *************************************************************************

# Registering the Android widgets for News plugin plugin.
plugin_widget_registry.register(NewsAndroidMainWidget)

# Registering the Android widgets for Huge news plugin plugin.
plugin_widget_registry.register(HugeNewsAndroidMainWidget)
