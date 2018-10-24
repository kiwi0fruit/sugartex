::conda install -c defaults -c conda-forge twine
cd /d "%~dp0"

python setup.py sdist
twine upload dist/* --skip-existing
chcp 65001 && set "PYTHONIOENCODING=utf-8"
