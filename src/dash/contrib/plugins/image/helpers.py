__all__ = ('handle_uploaded_file', 'get_crop_filter', 'delete_file')

import os
import glob
import logging

from django.conf import settings
from django.core.files.base import File

from dash.contrib.plugins.image.settings import (
    IMAGES_UPLOAD_DIR, FIT_METHOD_CROP_SMART, FIT_METHOD_CROP_CENTER, FIT_METHOD_CROP_SCALE
    )

logger = logging.getLogger(__file__)

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

def get_crop_filter(fit_method):
    if fit_method in (FIT_METHOD_CROP_SMART, FIT_METHOD_CROP_CENTER, FIT_METHOD_CROP_SCALE):
        return fit_method

def delete_file(image_file):
    """
    Delete file from disc.
    """
    try:
        # Delete the main file.
        file_path = os.path.join(settings.MEDIA_ROOT, image_file)
        os.remove(file_path)

        # Delete the sized version of it.
        files = glob.glob("{0}*".format(file_path))
        for f in files:
            try:
                os.remove(f)
            except Exception as e:
                logger.debug(str(e))

        # If all goes well...
        return True
    except Exception as e:
        logger.debug(str(e))
        return False
