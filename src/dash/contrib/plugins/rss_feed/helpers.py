__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('max_num_template',)

# Nax num of items in a template
max_num_template = lambda max_items, default: ':{0}'.format(max_items if max_items else default)
