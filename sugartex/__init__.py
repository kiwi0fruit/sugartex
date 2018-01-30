from .sugartex_filter import SugarTeX  # noqa
from .pre_sugartex import sugartex_preprocess, sugartex, stex  # noqa

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
