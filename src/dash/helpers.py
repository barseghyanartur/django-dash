__all__ = ('slugify_workspace', 'lists_overlap', 'iterable_to_dict')

from autoslug.settings import slugify

slugify_workspace = lambda s: slugify(s.lower()).lower()

def lists_overlap(sub, main):
    for i in sub:
        if i in main:
            return True
    return False

def iterable_to_dict(items, key_attr_name):
    """
    Converts iterable of certain objects to dict.

    :param iterable items:
    :param string key_attr_name: Attribute to use as a dictionary key.
    :return dict:
    """
    items_dict = {}
    for item in items:
        items_dict.update({getattr(item, key_attr_name): item})
    return items_dict
