from __future__ import absolute_import, division, print_function

import logging

import pyro.poutine as poutine
from pyro.primitives import clear_param_store, enable_validation, get_param_store, iarange, irange, \
    module, param, sample, random_module, validation_enabled
from pyro.util import set_rng_seed

version_prefix = '0.2.0-a0'

# Get the __version__ string from the auto-generated _version.py file, if exists.
try:
    from pyro._version import __version__
except ImportError:
    __version__ = version_prefix

# Default logger to prevent 'No handler found' warning.
logging.getLogger(__name__).addHandler(logging.NullHandler())


__all__ = [
    "__version__",
    "clear_param_store",
    "enable_validation",
    "get_param_store",
    "iarange",
    "irange",
    "module",
    "param",
    "poutine",
    "random_module",
    "sample",
    "set_rng_seed",
    "validation_enabled",
]
