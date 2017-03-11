find . -name "*.pyc" -exec rm -rf {} \;
find . -name "*.py,cover" -exec rm -rf {} \;
find . -name "__pycache__" -exec rm -rf {} \;
find . -name ".cache" -exec rm -rf {} \;
find . -name "*.orig" -exec rm -rf {} \;
rm MANIFEST.in~
rm .hgignore~
rm .gitignore~
rm -rf build/
rm -rf dist/
rm -rf examples/static/

mkdir examples/static/
