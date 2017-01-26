./scripts/uninstall.sh
./scripts/install.sh
rm docs/*.rst
rm -rf builddocs/
sphinx-apidoc src/dash --full -o docs -H 'django-dash' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -f -d 20
cp docs/conf.py.distrib docs/conf.py
#sphinx-apidoc src/dash --full -o docs -H 'django-dash' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -V '0.4.3' -f -d 20