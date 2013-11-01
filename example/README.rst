============================================
Example project for `django-dash`
============================================
Follow instructions below to install the example project. Commands below are written for Ubuntu/Debian,
but may work on other Linux distributions as well.

- Create a new- or switch to existing- virtual environement.

    $ virtualenv dash

    $ source dash/bin/activate

- Download the latest stable version of django-dash.

    $ wget https://github.com/barseghyanartur/django-dash/archive/stable.tar.gz

- Unpack it somewhere.

    $ tar -xvf stable.tar.gz

- Go to the unpacked directory.

    $ cd django-dash-stable

- Install Django, requirements and finally django-dash.

    $ pip install Django

    $ pip install -r example/requirements.txt

    $ pip install -e git+https://github.com/barseghyanartur/django-dash@stable#egg=django-dash

- Create some directories.

    $ mkdir example/media/
    
    $ mkdir example/media/static/

    $ mkdir example/static/

    $ mkdir example/db/

- Copy local_settings.example

    $ cp example/example/local_settings.example example/example/local_settings.py

- Run the commands to sync database, install test data and run the server.

    $ python example/example/manage.py syncdb --noinput --traceback -v 3

    $ python example/example/manage.py migrate --noinput

    $ python example/example/manage.py collectstatic --noinput --traceback -v 3

    $ python example/example/manage.py news_create_test_data --traceback -v 3

    $ python example/example/manage.py dash_create_test_data --traceback -v 3

    $ python example/example/manage.py runserver 0.0.0.0:8001 --traceback -v 3

- Open your browser and test the app.

Dashboard:

- URL: http://127.0.0.1:8001/dashboard/
- Admin username: test_admin
- Admin password: test

Django admin interface:

- URL: http://127.0.0.1:8001/administration/
- Admin username: test_admin
- Admin password: test