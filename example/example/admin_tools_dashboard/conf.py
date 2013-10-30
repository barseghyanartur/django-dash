# Django-CMS apps
foo_apps = [
    'foo.models.*',
]

# News apps list
news_apps = [
    'dash.contrib.plugins.news.models.*',
]

# Dash apps
dash_apps = [
    'dash.models.*',
]

# Registration apps
registration_apps = [
    'registration.models.*',
]

apps_to_exclude = ['django.contrib.*',]
apps_to_exclude += foo_apps + news_apps + dash_apps + registration_apps
