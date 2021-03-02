from django.db import models
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

try:
    from tinymce.models import HTMLField
except ImportError:
    from django.db.models import TextField as HTMLField

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    '_news_images',
    'NEWS_IMAGES_STORAGE_PATH',
    'NewsItem',
)


NEWS_IMAGES_STORAGE_PATH = 'news-images'


def _news_images(instance, filename):
    """Store the images in their own folder.

    This allows us to keep thumbnailed versions of all images.
    """
    if instance.pk:
        return '{0}/{1}-{2}'.format(
            NEWS_IMAGES_STORAGE_PATH,
            str(instance.pk),
            filename.replace(' ', '-')
        )
    return '{0}/{1}'.format(
        NEWS_IMAGES_STORAGE_PATH,
        filename.replace(' ', '-')
    )


class NewsItem(models.Model):
    """News item.

    - `title`: Title of the news item.
    - `body`: Teaser of the news item. WYSIWYG.
    - `image`: Headline image of the news item.
    - `date_published`: Date item is published. On creating defaults to
        ``datetime.datetime.now``.
    - `language`: Language.
    """

    title = models.CharField(_("Title"), max_length=100)
    body = HTMLField(_("Body"))
    image = models.ImageField(_("Headline image"),
                              blank=True,
                              null=True,
                              upload_to=_news_images)
    date_published = models.DateTimeField(_("Date published"),
                                          blank=True,
                                          null=True,
                                          default=timezone.now)
    slug = models.SlugField(unique=True, verbose_name=_("Slug"))

    date_created = models.DateTimeField(_("Date created"), blank=True,
                                        null=True, auto_now_add=True,
                                        editable=False)
    date_updated = models.DateTimeField(_("Date updated"), blank=True,
                                        null=True, auto_now=True,
                                        editable=False)

    class Meta:
        """Meta."""

        verbose_name = _("News item")
        verbose_name_plural = _("News items")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Absolute URL, which goes to the foo item detail page.

        :return string:
        """
        kwargs = {'slug': self.slug}
        return reverse('news.detail', kwargs=kwargs)

    def admin_image_preview(self):
        """Preview of the ``image``.

        For admin use mainly.

        :return string:
        """
        if self.image:
            return render_to_string(
                'news/_image_preview.html',
                {'alt': self.title, 'image_file': self.image}
            )
        else:
            return u''
    admin_image_preview.allow_tags = True
    admin_image_preview.short_description = _('Image')
