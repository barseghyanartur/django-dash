__title__ = 'dash.contrib.plugins.rss_feed.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('max_num_template',)


def max_num_template(max_items, default):
    """Nax num of items in a template."""
    return ':{0}'.format(max_items if max_items else default)
