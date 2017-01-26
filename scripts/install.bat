C:\Python27\Scripts\pip.exe install -r example\requirements.txt
python.exe setup.py install
mkdir example\logs
mkdir example\db
mkdir example\media
mkdir example\media\static
python.exe example\example\manage.py collectstatic --noinput
python.exe example\example\manage.py syncdb --noinput
python.exe example\example\manage.py migrate --noinput