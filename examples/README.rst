============================================
Example project for `django-dash`
============================================
Follow instructions below to install the example project. Commands below are
written for Ubuntu/Debian, but may work on other Linux distributions as well.

- Clone the repo, and cd into examples folder
    $ git+https://github.com/GMcD/django-dash#egg=django-dash
    $ cd django-dash/examples

- Create a new virtual environment.

    $ virtualenv env

    $ source env/bin/activate

- Install Django, requirements and finally django-dash, from GMcD, for 1.8 support

    $ pip install -r requirements.txt

- Create some directories.

    $ mkdir -p media/static/ static/ db/ logs

- Create Postgresql Dashboard database for local_settings.py

    $ dropdb Dashboard; createdb Dashboard;

- Run the commands to sync database, install test data and run the server.

    $ ./manage.py syncdb --noinput --traceback -v 3

    .. $ ./manage.py migrate --noinput

    $ ./manage.py collectstatic --noinput --traceback -v 3

    $ ./manage.py news_create_test_data --traceback -v 3

    $ ./manage.py dash_create_test_data --traceback -v 3

    $ ./manage.py runserver 0.0.0.0:8001 --traceback -v 3

- Open your browser and test the app.

Dashboard:

- URL: http://127.0.0.1:8001/dashboard/
- Admin username: test_admin
- Admin password: test

Django admin interface:

- URL: http://127.0.0.1:8001/administration/
- Admin username: test_admin
- Admin password: test
