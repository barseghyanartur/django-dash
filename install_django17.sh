pip install -r example/requirements.txt
python setup.py install
mkdir example/logs
mkdir example/db
mkdir example/media
mkdir example/media/static
python example/example/manage.py collectstatic --noinput --settings=settings_django17
python example/example/manage.py syncdb --noinput --settings=settings_django17
#python example/example/manage.py migrate --noinput --delete-ghost-migrations