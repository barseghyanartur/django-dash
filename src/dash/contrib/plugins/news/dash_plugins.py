__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('News2x5Plugin', 'News4x5Plugin')

from django.utils.translation import ugettext_lazy as _

from slim.helpers import get_language_from_request

from dash.base import BaseDashboardPlugin, plugin_registry, plugin_widget_registry
from dash.contrib.plugins.news.models import NewsItem
from dash.contrib.plugins.news.forms import NewsForm
from dash.contrib.plugins.news.dash_widgets import News2x5AndroidMainWidget, News4x5AndroidMainWidget

# ***************************************************************************
# ******************************* News plugin *******************************
# ***************************************************************************

class News2x5Plugin(BaseDashboardPlugin):
    """
    News plugin.
    """
    uid = 'news_2x5'
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


plugin_registry.register(News2x5Plugin)

# ***************************************************************************
# ******************************* Huge news plugin **************************
# ***************************************************************************

class News4x5Plugin(BaseDashboardPlugin):
    """
    News plugin.
    """
    uid = 'news_4x5'
    name = _("News")
    form = NewsForm
    group = _("News")


plugin_registry.register(News4x5Plugin)

# *************************************************************************
# ****************** Registering the widgets ******************************
# *************************************************************************

# Registering the Android widgets for News plugin plugin.
plugin_widget_registry.register(News2x5AndroidMainWidget)

# Registering the Android widgets for Huge news plugin plugin.
plugin_widget_registry.register(News4x5AndroidMainWidget)
