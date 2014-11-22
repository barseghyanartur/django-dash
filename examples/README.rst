============================================
Example project for `django-dash`
============================================
Follow instructions below to install the example project. Commands below are
written for Ubuntu/Debian, but may work on other Linux distributions as well.

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

    $ pip install -r examples/requirements.txt

    $ pip install -e git+https://github.com/barseghyanartur/django-dash@stable#egg=django-dash

- Create some directories.

    $ mkdir -p examples/media/static/ examples/static/ examples/db/ examples/logs

- Copy local_settings.example

    $ cp examples/example/local_settings.example examples/example/local_settings.py

- Run the commands to sync database, install test data and run the server.

    $ python examples/example/manage.py syncdb --noinput --traceback -v 3

    $ python examples/example/manage.py migrate --noinput

    $ python examples/example/manage.py collectstatic --noinput --traceback -v 3

    $ python examples/example/manage.py news_create_test_data --traceback -v 3

    $ python examples/example/manage.py dash_create_test_data --traceback -v 3

    $ python examples/example/manage.py runserver 0.0.0.0:8001 --traceback -v 3

- Open your browser and test the app.

Dashboard:

- URL: http://127.0.0.1:8001/dashboard/
- Admin username: test_admin
- Admin password: test

Django admin interface:

- URL: http://127.0.0.1:8001/administration/
- Admin username: test_admin
- Admin password: test
