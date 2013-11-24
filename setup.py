import sys
import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
except:
    readme = ''

template_dirs = [
    "src/dash/templates/dash", # Core templates
    "src/dash/contrib/layouts/android/templates/android", # Android layout
    "src/dash/contrib/layouts/bootstrap2/templates/bootstrap2", # Bootstrap 2 layouts
    "src/dash/contrib/layouts/windows8/templates/windows8", # Windows 8 layout
    "src/dash/contrib/plugins/dummy/templates/dummy", # Dummy plugin
    "src/dash/contrib/plugins/image/templates/image", # Image plugin
    "src/dash/contrib/plugins/memo/templates/memo", # Memo plugin
    "src/dash/contrib/plugins/news/templates/news", # News plugin
    "src/dash/contrib/plugins/rss_feed/templates/rss_feed", # RSS feed plugin
    "src/dash/contrib/plugins/url/templates/url", # URL plugin
    "src/dash/contrib/plugins/video/templates/video", # Video plugin
    "src/dash/contrib/plugins/weather/templates/weather", # Weather plugin
]
static_dirs = [
    "src/dash/static", # Core static
    "src/dash/contrib/layouts/android/static", # Android layout
    "src/dash/contrib/layouts/bootstrap2/static", # Bootstrap 2 layouts
    "src/dash/contrib/layouts/windows8/static", # Windows 8 layout
    "src/dash/contrib/plugins/image/static", # Image plugin
    "src/dash/contrib/plugins/news/static", # News plugin
    "src/dash/contrib/plugins/rss_feed/static", # RSS feed plugin
    "src/dash/contrib/plugins/url/static", # URL plugin
    "src/dash/contrib/plugins/video/static", # Video plugin
    "src/dash/contrib/plugins/weather/static", # Weather plugin
]

locale_dirs = [
    "src/dash/locale/nl",
    "src/dash/locale/ru",
]

templates = []
static_files = []
locale_files = []

for template_dir in template_dirs:
    templates += [os.path.join(template_dir, f) for f in os.listdir(template_dir)]

for static_dir in static_dirs:
    static_files += [os.path.join(static_dir, f) for f in os.listdir(static_dir)]

for locale_dir in locale_dirs:
    locale_files += [os.path.join(locale_dir, f) for f in os.listdir(locale_dir)]

#print(templates)
#print(static_files)
#raise Exception()

version = '0.3'

install_requires = [
    'Pillow==2.1.0',
    'django-autoslug==1.7.1',
    'django-slim==0.7.1',
    'django-tinymce==1.5.1',
    'feedparser==5.1.3',
    'ordereddict==1.1',
    'pif==0.5',
    'radar==0.3',
    'six==1.4.1',
    'easy-thumbnails==1.4',
    'transliterate==1.5',
    'vishap==0.1'
]

try:
    PY2 = sys.version_info[0] == 2
    PY3 = sys.version_info[0] == 3
    if PY2:
        install_requires.append('django-localeurl==2.0.1')
except:
    pass

setup(
    name = 'django-dash',
    version = version,
    description = ("Customisable, modular dashboard application framework for Django."),
    long_description = readme,
    classifiers = [
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    keywords = 'dashboard, django, django dashboard',
    author = 'Artur Barseghyan',
    author_email = 'artur.barseghyan@gmail.com',
    url = 'https://github.com/barseghyanartur/django-dash/',
    package_dir = {'':'src'},
    packages = find_packages(where='./src'),
    license = 'GPL 2.0/LGPL 2.1',
    install_requires = install_requires,
    package_data = {
        'dash': templates + static_files + locale_files
    },
    include_package_data = True,
)
