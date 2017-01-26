pip install -r examples/requirements/django_1_8.txt
python setup.py install
mkdir examples/logs
mkdir examples/db
mkdir examples/media
mkdir examples/media/static
python examples/example/manage.py collectstatic --noinput --settings=settings/django_1_8
python examples/example/manage.py syncdb --noinput --settings=settings/django_1_8
#python examples/example/manage.py migrate --noinput --delete-ghost-migrations
