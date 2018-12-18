from .sugartex_filter import SugarTeX
from .pre_sugartex import (
    sugartex,
    sugartex_replace_all, sugartex_replace_all as stex,
    sugartex_preprocess, sugartex_preprocess as pre
)
from .sugartex_pandoc_filter import main

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
