#!/usr/bin/env bash
wget -O django_dash_example_app_installer.tar.gz https://github.com/barseghyanartur/django-dash/archive/stable.tar.gz
virtualenv dash
source dash/bin/activate
mkdir django_dash_example_app_installer/
tar -xvf django_dash_example_app_installer.tar.gz -C django_dash_example_app_installer
cd django_dash_example_app_installer/django-dash-stable/examples/example/
pip install -r ../requirements.txt
pip install https://github.com/barseghyanartur/django-dash/archive/stable.tar.gz
mkdir ../media/
mkdir ../media/static/
mkdir ../media/dash-image-plugin-images/
mkdir ../static/
mkdir ../db/
mkdir ../logs/
mkdir ../tmp/
cp settings/local_settings.example settings/local_settings.py
./manage.py migrate --noinput
./manage.py collectstatic --noinput --traceback -v 3
./manage.py news_create_test_data
./manage.py dash_create_test_data
./manage.py runserver 0.0.0.0:8001 --traceback -v 3
