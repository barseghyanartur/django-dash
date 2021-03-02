__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('max_num_template',)


def max_num_template(max_items, default):
    """Nax num of items in a template."""
    return ':{0}'.format(max_items if max_items else default)
