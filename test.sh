reset
./uninstall.sh
./install.sh
python examples/example/manage.py test dash --traceback -v 3
#python examples/example/manage.py test dummy --traceback -v 3
#python examples/example/manage.py test memo --traceback -v 3