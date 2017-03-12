import os
import sys

from distutils.version import LooseVersion
from setuptools import find_packages, setup

version = '0.5.1'

# ***************************************************************************
# ************************** Python version *********************************
# ***************************************************************************
PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3
LTE_PY26 = PY2 and (7 > sys.version_info[1])
PYPY = hasattr(sys, 'pypy_translation_info')

# ***************************************************************************
# ************************** Django version *********************************
# ***************************************************************************
DJANGO_INSTALLED = False
try:
    import django
    DJANGO_INSTALLED = True

    LOOSE_DJANGO_VERSION = LooseVersion(django.get_version())
    LOOSE_DJANGO_MINOR_VERSION = LooseVersion(
        '.'.join([str(i) for i in LOOSE_DJANGO_VERSION.version[0:2]])
    )

    # Loose versions
    LOOSE_VERSIONS = (
        '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '1.10', '1.11', '2.0', '2.1',
        '2.2', '3.0'
    )

    for v in LOOSE_VERSIONS:
        var_name = 'LOOSE_VERSION_{0}'.format(v.replace('.', '_'))
        globals()[var_name] = LooseVersion(v)

    # Exact versions
    EXACT_VERSIONS = LOOSE_VERSIONS[:-1]

    for i, v in enumerate(EXACT_VERSIONS):
        l_cur = globals()['LOOSE_VERSION_{0}' \
                          ''.format(LOOSE_VERSIONS[i].replace('.', '_'))]
        l_nxt = globals()['LOOSE_VERSION_{0}' \
                          ''.format(LOOSE_VERSIONS[i + 1].replace('.', '_'))]
        var_name = 'DJANGO_{0}'.format(v.replace('.', '_'))
        globals()[var_name] = (l_cur <= LOOSE_DJANGO_VERSION < l_nxt)

    # LTE list
    LTE_VERSIONS = LOOSE_VERSIONS[:-1]

    for i, v in enumerate(EXACT_VERSIONS):
        l_cur = globals()['LOOSE_VERSION_{0}' \
                          ''.format(LOOSE_VERSIONS[i].replace('.', '_'))]
        var_name = 'DJANGO_LTE_{0}'.format(v.replace('.', '_'))
        globals()[var_name] = (LOOSE_DJANGO_MINOR_VERSION <= l_cur)

    # GTE list
    GTE_VERSIONS = LOOSE_VERSIONS[:-1]

    for i, v in enumerate(EXACT_VERSIONS):
        l_cur = globals()['LOOSE_VERSION_{0}' \
                          ''.format(LOOSE_VERSIONS[i].replace('.', '_'))]
        var_name = 'DJANGO_GTE_{0}'.format(v.replace('.', '_'))
        globals()[var_name] = (
            LOOSE_DJANGO_MINOR_VERSION >= l_cur
        )

except Exception as err:
    pass

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
    "src/dash/contrib/layouts/bootstrap3/templates/bootstrap3",
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

install_requires = []
# If certain version of Django is already installed, choose version agnostic
# dependencies.

install_requires = [
    'Pillow>=2.1.0',
    'feedparser>=5.1.3',
    'ordereddict>=1.1',
    'pif>=0.5,<1.0',
    'six>=1.9',
    'transliterate>=1.5,<2.0',
    'vishap>=0.1.3,<2.0',
    'django-nine>=0.1.1',
    'Unidecode',
]

if DJANGO_INSTALLED:
    if DJANGO_LTE_1_6:
        install_requires.append('django-autoslug==1.7.1')
    else:
        install_requires.append('django-autoslug>=1.9.3')

    if DJANGO_GTE_1_8:
        install_requires.append('django-tinymce>=2.0.0')
    else:
        install_requires.append('django-tinymce>=1.5.3,<2.0.0')

    if DJANGO_GTE_1_11:
        install_requires.append('easy-thumbnails')
        dependency_links.append(
            'https://github.com/SmileyChris/easy-thumbnails/archive/'
            'master.tar.gz'
            '#egg=easy-thumbnails'
        )
    elif PY3:
        install_requires.append('easy-thumbnails>=2.3')
    else:
        install_requires.append('easy-thumbnails>=1.4')
else:
    # We consider Django 1.8 as a default.
    install_requires.append('django-autoslug>=1.9.3')
    install_requires.append('django-tinymce>=2.0.0')
    install_requires.append('easy-thumbnails>=1.4')

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
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 "
        "or later (LGPLv2+)",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    keywords='dashboard, django, django dashboard',
    author='Artur Barseghyan',
    author_email='artur.barseghyan@gmail.com',
    url='https://github.com/barseghyanartur/django-dash/',
    package_dir={'': 'src'},
    packages=find_packages(where='./src'),
    license='GPL 2.0/LGPL 2.1',
    install_requires=install_requires,
    tests_require=tests_require,
    package_data={
        'dash': templates + static_files + locale_files
    },
    include_package_data=True,
)
