"""
Creates all necessary dirs, syncs the database, etc.
"""
import os
import shutil
import subprocess

PROJECT_DIR = lambda base : os.path.abspath(os.path.join(os.path.dirname(__file__), base).replace('\\','/'))

os.makedirs('example/media/static')
os.mkdir('example/media/dash-image-plugin-images')
os.mkdir('example/static')
os.mkdir('example/db')
os.mkdir('example/logs')
os.mkdir('example/tmp')

shutil.copyfile('example/example/local_settings.example', 'example/example/local_settings.py')

commands = [
    'python example/example/manage.py syncdb --noinput --traceback -v 3',
    'python example/example/manage.py migrate --noinput',
    'python example/example/manage.py collectstatic --noinput --traceback -v 3',
    'python example/example/manage.py news_create_test_data --traceback -v 3',
    'python example/example/manage.py dash_create_test_data --traceback -v 3',
]

for cmd in commands:
    subprocess.call(cmd.split(' '))
