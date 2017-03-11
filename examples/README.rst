===================================
Example project for ``django-dash``
===================================
Follow instructions below to install the example project. Commands below are
written for Ubuntu/Debian, but may work on other Linux distributions as well.

#) Create a new- or switch to existing- virtual environment.

    .. code-block:: sh

        virtualenv dash

        source dash/bin/activate

#) Download the latest stable version of django-dash.

    .. code-block:: sh

        wget https://github.com/barseghyanartur/django-dash/archive/stable.tar.gz

#) Unpack it somewhere.

    .. code-block:: sh

        tar -xvf stable.tar.gz

#) Go to the unpacked directory.

    .. code-block:: sh

        cd django-dash-stable

#) Install Django, requirements and finally django-dash.

    .. code-block:: sh

        pip install Django

        pip install -r examples/requirements.txt

        pip install https://github.com/barseghyanartur/django-dash/archive/stable.tar.gz

- Create some directories.

    .. code-block:: sh

        mkdir -p examples/media/static/ examples/static/ examples/db/ examples/logs

- Copy local_settings.example

    .. code-block:: sh

        cp examples/example/settings/local_settings.example examples/example/settings/local_settings.py

- Run the commands to sync database, install test data and run the server.

    .. code-block:: sh

        python examples/example/manage.py syncdb --noinput --traceback -v 3

        python examples/example/manage.py migrate --noinput

        python examples/example/manage.py collectstatic --noinput --traceback -v 3

        python examples/example/manage.py news_create_test_data --traceback -v 3

        python examples/example/manage.py dash_create_test_data --traceback -v 3

        python examples/example/manage.py runserver 0.0.0.0:8001 --traceback -v 3

#) Open your browser and test the app.

    .. code-block:: text

        Dashboard:

        - URL: http://127.0.0.1:8001/dashboard/
        - Admin username: test_admin
        - Admin password: test

        Django admin interface:

        - URL: http://127.0.0.1:8001/administration/
        - Admin username: test_admin
        - Admin password: test
