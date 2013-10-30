__all__ = ('max_num_template',)

# Nax num of items in a template
max_num_template = lambda max_items, default: ':{0}'.format(max_items if max_items else default)
