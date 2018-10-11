::conda install -c defaults -c conda-forge twine
set "script_dir=%~dp0"
cd /d "%script_dir%"

python setup.py sdist
chcp 1252 && set "PYTHONIOENCODING="
twine upload dist/* --skip-existing
chcp 65001 && set "PYTHONIOENCODING=utf-8"
