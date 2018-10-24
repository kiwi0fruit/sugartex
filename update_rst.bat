::conda install -c defaults -c conda-forge "pandoc>=2.2.1"
cd /d "%~dp0"

pandoc README.md -o README.rst
