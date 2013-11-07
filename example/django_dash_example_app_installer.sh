wget -O django_dash_example_app_installer.tar.gz https://github.com/barseghyanartur/django-dash/archive/stable.tar.gz
mkdir django_dash_example_app_installer/
tar -xvf django_dash_example_app_installer.tar.gz -C django_dash_example_app_installer
cd django_dash_example_app_installer/django-dash-stable/example/example/
pip install Django
pip install -r ../requirements.txt
pip install -e git+https://github.com/barseghyanartur/django-dash@stable#egg=django-dash
mkdir ../media/
mkdir ../media/static/
mkdir ../media/dash-image-plugin-images/
mkdir ../static/
mkdir ../db/
mkdir ../logs/
mkdir ../tmp/
cp local_settings.example local_settings.py
./manage.py syncdb --noinput --traceback -v 3
./manage.py migrate --noinput
./manage.py collectstatic --noinput --traceback -v 3
./manage.py news_create_test_data --traceback -v 3
./manage.py dash_create_test_data --traceback -v 3
./manage.py runserver 0.0.0.0:8001 --traceback -v 3