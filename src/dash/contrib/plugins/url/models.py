from django.db import models
from django.utils.translation import gettext_lazy as _

from .settings import BOOKMARK_IMAGE_CHOICES_WITH_EMPTY_OPTION

__title__ = 'dash.contrib.plugins.urls.models'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('Bookmark',)


class Bookmark(models.Model):
    """Bookmark.

    - `title` (string): Bookmark title.
    - `url` (string): Bookmark URL.
    - `external` (bool): External/internal link.
    - `image` (string): Bookmark image icon.
    """

    title = models.CharField(_("Title"), max_length=100)
    url = models.URLField(_("URL"), max_length=255)
    external = models.BooleanField(_("External"), default=False)
    image = models.CharField(_("Image"),
                             max_length=255,
                             blank=True,
                             null=True,
                             choices=BOOKMARK_IMAGE_CHOICES_WITH_EMPTY_OPTION)

    class Meta:
        """Meta."""

        verbose_name = _("Bookmark")
        verbose_name_plural = _("Bookmarks")

    def __str__(self):
        return self.title
