# Django settings for resato_portal project.
import os
PROJECT_DIR = lambda base : os.path.abspath(os.path.join(os.path.dirname(__file__), base).replace('\\','/'))

DEBUG = True
DEBUG_TOOLBAR = not True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': PROJECT_DIR('../db/example.db'),                      # Or path to database file if using sqlite3.

        #'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        #'NAME': 'dash',
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'test',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

INTERNAL_IPS = ('127.0.0.1',)

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = PROJECT_DIR('../tmp')

DEFAULT_FROM_EMAIL = '<no-reply@example.com>'

DASH_DEBUG = True
#DASH_RESTRICT_PLUGIN_ACCESS = False

#DASH_ACTIVE_LAYOUT = 'windows8'

# Key for API weather
DASH_PLUGIN_WEATHER_API_KEY = 'verjs85fmvyq9wt77psezsdk'
