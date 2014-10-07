reset
./uninstall.sh
./install_django17.sh
python example/example/manage.py test dash --traceback -v 3 --settings=settings_django17
#python example/example/manage.py test dummy --traceback -v 3
#python example/example/manage.py test memo --traceback -v 3