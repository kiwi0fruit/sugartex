from .sugartex_filter import SugarTeX  # noqa
from .pre_sugartex import (
    sugartex,
    sugartex_replace_all, sugartex_replace_all as all,
    sugartex_preprocess, sugartex_preprocess as pre
)  # noqa

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
