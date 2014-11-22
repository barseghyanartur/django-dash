reset
./uninstall.sh
./install.sh
pip uninstall django-localeurl -y
pip uninstall django-localeurl -y
pip install -e hg+https://bitbucket.org/barseghyanartur/django-localeurl@stable#egg=django-localeurl
python examples/example/manage.py test dash --traceback
#python examples/example/manage.py test dummy --traceback
#python examples/example/manage.py test note --traceback