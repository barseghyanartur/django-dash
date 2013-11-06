__all__ = ('handle_uploaded_file',)

import os

from django.conf import settings
from django.core.files.base import File

from dash.contrib.plugins.image.settings import IMAGES_UPLOAD_DIR

IMAGES_UPLOAD_DIR_ABSOLUTE_PATH = os.path.join(settings.MEDIA_ROOT, IMAGES_UPLOAD_DIR)

def handle_uploaded_file(image_file):
    """
    :param django.core.files.uploadedfile.InMemoryUploadedFile image_file:
    :return str: Path to the image (relative).
    """
    if isinstance(image_file, File):
        with open(os.path.join(IMAGES_UPLOAD_DIR_ABSOLUTE_PATH, image_file.name), 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
        return os.path.join(IMAGES_UPLOAD_DIR, image_file.name)
    return image_file

