pip install -r examples/requirements/latest.txt
pip install -e .
mkdir examples/logs
mkdir examples/db
mkdir examples/media
mkdir examples/media/static
python examples/example/manage.py collectstatic --noinput
python examples/example/manage.py migrate --noinput --delete-ghost-migrations
