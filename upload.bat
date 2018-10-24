::conda install -c defaults -c conda-forge twine
cd /d "%~dp0"

python setup.py sdist
twine upload dist/* --skip-existing
