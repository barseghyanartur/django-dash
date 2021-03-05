import os
from setuptools import find_packages, setup

version = '0.6.1'

# ***************************************************************************
# **************************** Package data *********************************
# ***************************************************************************

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
    screen_shots = open(
        os.path.join(os.path.dirname(__file__), 'SCREENSHOTS.rst')
    ).read()
    screen_shots = screen_shots.replace(
        '.. image:: _static',
        '.. figure:: https://github.com/barseghyanartur/django-dash/raw/'
        'master/docs/_static'
    )
except Exception:
    readme = ''
    screen_shots = ''

template_dirs = [
    "src/dash/templates/dash",  # Core templates
    # Android layout
    "src/dash/contrib/layouts/android/templates/android",
    # Bootstrap 2 layouts
    "src/dash/contrib/layouts/bootstrap2/templates/bootstrap2",
    # Bootstrap 3 layouts
    # "src/dash/contrib/layouts/bootstrap3/templates/bootstrap3",
    # Windows 8 layout
    "src/dash/contrib/layouts/windows8/templates/windows8",
    "src/dash/contrib/plugins/dummy/templates/dummy",  # Dummy plugin
    "src/dash/contrib/plugins/image/templates/image",  # Image plugin
    "src/dash/contrib/plugins/memo/templates/memo",  # Memo plugin
    # "src/dash/contrib/plugins/news/templates/news",  # News plugin
    "src/dash/contrib/plugins/rss_feed/templates/rss_feed",  # RSS feed plugin
    "src/dash/contrib/plugins/url/templates/url",  # URL plugin
    "src/dash/contrib/plugins/video/templates/video",  # Video plugin
    "src/dash/contrib/plugins/weather/templates/weather",  # Weather plugin
]
static_dirs = [
    "src/dash/static", # Core static
    "src/dash/contrib/layouts/android/static",  # Android layout
    "src/dash/contrib/layouts/bootstrap2/static",  # Bootstrap 2 layouts
    # "src/dash/contrib/layouts/bootstrap3/static",  # Bootstrap 3 layouts
    "src/dash/contrib/layouts/windows8/static",  # Windows 8 layout
    "src/dash/contrib/plugins/image/static",  # Image plugin
    # "src/dash/contrib/plugins/news/static",  # News plugin
    "src/dash/contrib/plugins/rss_feed/static",  # RSS feed plugin
    "src/dash/contrib/plugins/url/static",  # URL plugin
    "src/dash/contrib/plugins/video/static",  # Video plugin
    "src/dash/contrib/plugins/weather/static",  # Weather plugin
]

locale_dirs = [
    "src/dash/locale/nl",
    "src/dash/locale/ru",
]

templates = []
static_files = []
locale_files = []

for template_dir in template_dirs:
    templates += [os.path.join(template_dir, f)
                  for f in os.listdir(template_dir)]

for static_dir in static_dirs:
    static_files += [os.path.join(static_dir, f)
                     for f in os.listdir(static_dir)]

for locale_dir in locale_dirs:
    locale_files += [os.path.join(locale_dir, f)
                     for f in os.listdir(locale_dir)]

# ***************************************************************************
# ************************** Package versions *******************************
# ***************************************************************************

dependency_links = []

# If certain version of Django is already installed, choose version agnostic
# dependencies.

install_requires = [
    'Pillow>=6.0.0',
    'feedparser>=6.0.0',
    'pif>=0.5,<1.0',
    'transliterate>=1.5,<2.0',
    'vishap>=0.1.3,<2.0',
    'django-nine>=0.2.4',
    'Unidecode',
    'django-autoslug>=1.9.8',
    'django-tinymce>=3.2.0',
    'easy-thumbnails>=2.5.0'
]

tests_require = [
    'radar>=0.3,<1.0',
    'selenium',
]

# ***************************************************************************
# ******************************** Setup ************************************
# ***************************************************************************

setup(
    name='django-dash',
    version=version,
    description="Customisable, modular dashboard application framework "
                "for Django.",
    long_description="{0}{1}".format(readme, screen_shots),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 "
        "or later (LGPLv2+)",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/barseghyanartur/django-dash/issues",
        "Documentation": "https://django-dash.readthedocs.io/",
        "Source Code": "https://github.com/barseghyanartur/django-dash",
        "Changelog": "https://django-dash.readthedocs.io/"
                     "en/latest/changelog.html",
    },
    keywords='dashboard, django, django dashboard',
    author='Artur Barseghyan',
    author_email='artur.barseghyan@gmail.com',
    url='https://github.com/barseghyanartur/django-dash/',
    package_dir={'': 'src'},
    packages=find_packages(where='./src'),
    license='GPL-2.0-only OR LGPL-2.1-or-later',
    install_requires=install_requires,
    tests_require=tests_require,
    dependency_links=dependency_links,
    package_data={
        'dash': templates + static_files + locale_files
    },
    include_package_data=True,
)
