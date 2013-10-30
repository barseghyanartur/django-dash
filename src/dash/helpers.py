__all__ = ('slugify_workspace', 'lists_overlap')

from autoslug.settings import slugify

slugify_workspace = lambda s: slugify(s.lower()).lower()

def lists_overlap(sub, main):
    for i in sub:
        if i in main:
            return True
    return False
