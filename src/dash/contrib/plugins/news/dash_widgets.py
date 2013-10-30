__all__ = ('NewsAndroidMainWidget', 'HugeNewsAndroidMainWidget')

from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget
from dash.contrib.plugins.news.constants import PAGE_URL_PARAM, NUM_POSTS_URL_PARAM

# ************************************************************************
# ****************** Android widgets for Read RSS feed plugin ************
# ************************************************************************
class NewsAndroidMainWidget(BaseDashboardPluginWidget):
    """
    News plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'
    plugin_uid = 'news'
    cols = 2
    rows = 5

    media_js = [
        'js/dash_plugin_news.js',
    ]
    media_css = [
        'css/dash_plugin_news.css',
    ]

    def render(self, request=None):
        context = {'plugin': self.plugin,}
        return render_to_string('news/render_main.html', context)


# ************************************************************************
# ****************** Android widgets for Read RSS feed plugin ************
# ************************************************************************
class HugeNewsAndroidMainWidget(NewsAndroidMainWidget):
    """
    Huge news plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'huge_news'
    cols = 4
    rows = 5

    media_js = [
        'js/dash_plugin_huge_news.js',
    ]
    media_css = [
        'css/dash_plugin_news.css',
    ]

    def render(self, request=None):
        context = {
            'plugin': self.plugin,
            'PAGE_URL_PARAM': PAGE_URL_PARAM,
            'NUM_POSTS_URL_PARAM': NUM_POSTS_URL_PARAM
            }
        return render_to_string('news/render_huge_main.html', context)
