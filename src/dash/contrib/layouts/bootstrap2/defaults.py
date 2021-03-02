from django.utils.translation import gettext_lazy as _

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'IMAGE_CHOICES',
    'IMAGE_CHOICES_WITH_EMPTY_OPTION',
)

IMAGE_CHOICES = (
    # Icons that are also present in `URLPlugin`.
    ('icon-film', _("Film")),
    # ('icon-coffee', _("Coffee")),
    ('icon-calendar', _("Calendar")),
    ('icon-book', _("Book")),
    ('icon-music', _("Music")),
    ('icon-picture', _("Picture")),
    # ('icon-rss-sign', _("RSS")),
    ('icon-star', _("Star")),
    ('icon-thumbs-up', _("Thumbs-up")),
    # ('icon-smile', _("Smile")),
    # ('icon-gamepad', _("Gamepad")),
    ('icon-plane', _("Plane")),
    ('icon-road', _("Road")),
    ('icon-camera', _("Camera")),
    ('icon-download', _("Download")),
    # ('icon-food', _("Food")),
    ('icon-info-sign', _("Info")),
    ('icon-shopping-cart', _("Shopping cart")),
    # ('icon-truck', _("Truck")),
    ('icon-wrench', _("Wrench")),
    # ('icon-facebook', _("Facebook")),
    # ('icon-github', _("Github")),
    # ('icon-google-plus', _("Google plus")),
    # ('icon-linkedin', _("LinkedIn")),
    # ('icon-pinterest', _("Pinterest")),
    # ('icon-twitter', _("Twitter")),
    # ('icon-youtube', _("Youtube")),
    # ('icon-bitbucket', _("Bitbucket")),
    # ('icon-android', _("Android")),
    # ('icon-apple', _("Apple")),
    # ('icon-windows', _("Windows")),
    # ('icon-tumblr-sign', _("Tumblr")),
    # ('icon-instagram', _("Instagram")),
    # ('icon-dropbox', _("Dropbox")),
    # ('icon-trophy', _("Trophy")),
    # ('icon-legal', _("Legal")),
    ('icon-lock', _("Lock")),
    ('icon-heart', _("Heart")),
    ('icon-question-sign', _("Question")),
    ('icon-headphones', _("Headphones")),
    ('icon-gift', _("Gift")),
    # ('icon-key', _("Key")),
    # ('icon-female', _("Female")),
    # ('icon-male', _("Male")),
    ('icon-comment', _("Comment")),
    # ('icon-bug', _("Bug")),
    ('icon-bell', _("Bell")),
    ('icon-search', _("Search")),
    ('icon-map-marker', _("Map marker")),
    ('icon-globe', _("Globe")),
    ('icon-pencil', _("Pensil")),
    ('icon-tasks', _("Tasks")),
)

IMAGE_CHOICES_WITH_EMPTY_OPTION = [('', '---------')] + list(IMAGE_CHOICES)
