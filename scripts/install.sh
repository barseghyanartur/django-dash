pip install -r examples/requirements.txt
python setup.py install
mkdir examples/logs
mkdir examples/db
mkdir examples/media
mkdir examples/media/static
python examples/example/manage.py collectstatic --noinput
python examples/example/manage.py syncdb --noinput
python examples/example/manage.py migrate --noinput --delete-ghost-migrations