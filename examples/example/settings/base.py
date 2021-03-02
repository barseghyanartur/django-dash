# Django settings for example project.
import os
import sys

from .helpers import PROJECT_DIR, gettext

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False
DEBUG_TOOLBAR = False
# TEMPLATE_DEBUG = DEBUG
DEV = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': PROJECT_DIR(os.path.join('..', '..', 'db', 'example.db')),
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        # Empty for localhost through domain sockets or '127.0.0.1' for
        # localhost through TCP.
        'HOST': '',
        # Set to empty string for default.
        'PORT': '',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', gettext("English")),  # Main language!
    ('hy', gettext("Armenian")),
    ('nl', gettext("Dutch")),
    ('ru', gettext("Russian")),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_DIR(os.path.join('..', '..', 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_DIR(os.path.join('..', '..', 'static'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR(os.path.join('..', '..', 'media', 'static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# ***************************************

try:
    from .local_settings import DEBUG_TEMPLATE
except ImportError:
    DEBUG_TEMPLATE = False


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'APP_DIRS': True,
        'DIRS': [PROJECT_DIR(os.path.join('..', 'templates'))],
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                'django.template.context_processors.request',
                "django.contrib.auth.context_processors.auth",
                # "django.core.context_processors.i18n",
                # "django.core.context_processors.media",
                # "django.core.context_processors.static",
                # "django.core.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                # 'django.template.loaders.eggs.Loader',
                'admin_tools.template_loaders.Loader',
            ],
            'debug': DEBUG_TEMPLATE,
        }
    },
]


# ***************************************

# Make this unique, and don't share it with anybody.
SECRET_KEY = '6sf18c*w971i8a-m^1coasrmur2k6+q5_kyn*)s@(*_dk5q3&r'

# # List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
# )


MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'
#
# TEMPLATE_CONTEXT_PROCESSORS = (
#     "django.contrib.auth.context_processors.auth",
#     "django.core.context_processors.debug",
#     "django.core.context_processors.i18n",
#     "django.core.context_processors.media",
#     "django.core.context_processors.static",
#     "django.core.context_processors.tz",
#     "django.contrib.messages.context_processors.messages",
#     "django.core.context_processors.request"
# )

# TEMPLATE_DIRS = (
#     # Put strings here, like "/home/html/django_templates"
#     # or "C:/www/django/templates".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
#     PROJECT_DIR('templates'),
# )

# FIXTURE_DIRS = (
#   PROJECT_DIR(os.path.join('..', 'fixtures'))
# )

INSTALLED_APPS = (
    # Admin dashboard
    'admin_tools',
    'admin_tools.menu',

    # Django core and contrib apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',

    # Third party apps used in the project
    # 'tinymce',  # TinyMCE
    'django_registration',  # Auth views and registration app
    'easy_thumbnails',  # Thumbnailer
    'widget_tweaks',  # For tweaking the forms
    # 'slim',  # Multi-lingual models app

    # Dash core, contrib layouts and apps
    'dash',  # Dash core

    # Dash contrib layouts
    'dash.contrib.layouts.android',  # Android layout for Dash
    'dash.contrib.layouts.bootstrap2',  # Bootstrap 2 layouts for Dash
    # 'dash.contrib.layouts.bootstrap3',  # Bootstrap 3 layouts for Dash
    'dash.contrib.layouts.windows8',  # Windows 8 layout for Dash

    # Dash contrib plugins
    'dash.contrib.plugins.dummy',  # Dummy (testing) plugin for Dash
    'dash.contrib.plugins.memo',  # Memo plugin for Dash
    'dash.contrib.plugins.image',  # Image plugin for Dash
    'dash.contrib.plugins.rss_feed',  # RSS feed plugin for Dash
    'dash.contrib.plugins.url',  # URL plugin for Dash
    'dash.contrib.plugins.video',  # Video plugin for Dash
    'dash.contrib.plugins.weather',  # Weather plugin for Dash
    'dash.contrib.apps.public_dashboard',  # Public dashboard app for Dash

    # Other project specific apps
    # 'admin_tools_dashboard',  # Admin dashboard
    'foo',  # Test app
    'bar',  # Another test app
    'd3_samples',  # Sample D3 plugins
    'news',  # Sample news plugin for Dash
    # 'customauth',  # Custom user model
)

# Using custom user model
# AUTH_USER_MODEL = 'customauth.MyUser'

LOGIN_REDIRECT_URL = '/en/dashboard/'
LOGIN_URL = '/en/accounts/login/'
LOGIN_ERROR_URL = '/en/accounts/login/'
LOGOUT_URL = '/en/accounts/logout/'

# Tell slim to use localised language names
# SLIM_USE_LOCAL_LANGUAGE_NAMES = True

# django-admin-tools custom dashboard
ADMIN_TOOLS_MENU = 'admin_tools_dashboard.menu.CustomMenu'

ACCOUNT_ACTIVATION_DAYS = 2
# REGISTRATION_TEMPLATE_DIR = PROJECT_DIR('templates/registration')

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s [%(pathname)s:%(lineno)s] '
                      '%(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'django_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR(os.path.join("..", "..", "logs", "django.log")),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
        'dash_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR(os.path.join("..", "..", "logs", "dash.log")),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['django_log'],
            'level': 'ERROR',
            'propagate': True,
        },
        'dash': {
            'handlers': ['console', 'dash_log'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# Make settings quite compatible among various Django versions used.

MIGRATION_MODULES = {
    'dash': 'dash.migrations',
    'easy_thumbnails': 'easy_thumbnails.migrations',
}

# For Selenium tests
FIREFOX_BIN_PATH = None
PHANTOM_JS_EXECUTABLE_PATH = None

# CHROME_DRIVER_EXECUTABLE_PATH = os.environ.get('CHROME_BIN', None)
CHROME_DRIVER_EXECUTABLE_PATH = None
IS_TRAVIS = 'TRAVIS' in os.environ

if IS_TRAVIS:
    CHROME_DRIVER_EXECUTABLE_PATH = '/home/travis/chromedriver'

from selenium import webdriver
CHROME_DRIVER_OPTIONS = webdriver.ChromeOptions()
CHROME_DRIVER_OPTIONS.add_argument('-headless')
CHROME_DRIVER_OPTIONS.add_argument('-no-sandbox')
CHROME_DRIVER_OPTIONS.set_capability('chrome.binary', "/usr/bin/google-chrome")
# CHROME_DRIVER_OPTIONS.add_argument('-single-process')

try:
    from .local_settings import DEV
except ImportError:
    pass

try:
    from .local_settings import (
        FIREFOX_BIN_PATH,
        PHANTOM_JS_EXECUTABLE_PATH,
        CHROME_DRIVER_EXECUTABLE_PATH,
        CHROME_DRIVER_OPTIONS,
    )
except ImportError:
    pass

# Make the `django-dash` package available without installation.
if DEV:
    dash_source_path = os.environ.get('DASH_SOURCE_PATH', 'src')
    sys.path.insert(0, dash_source_path)
