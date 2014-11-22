pip install -r examples/requirements.txt
pip install -r examples/requirements3.txt
python setup.py install
mkdir examples/logs/
python examples/example/manage.py collectstatic --noinput
python examples/example/manage.py syncdb --noinput
python examples/example/manage.py migrate --noinput