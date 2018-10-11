::conda install -c defaults -c conda-forge "pandoc>=2.2.1"
set "script_dir=%~dp0"
cd /d "%script_dir%"

chcp 65001 > NUL
pandoc README.md -o README.rst
pause
