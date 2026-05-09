import logging
from contextlib import contextmanager
from .core import Cairn

@contextmanager
def cairn_test_context(level=None):
    """
    Context manager for temporary logging overrides during tests.
    """
    root_logger = logging.getLogger()
    old_level = root_logger.level
    
    if level:
        Cairn.set_level(level)
        
    try:
        yield
    finally:
        Cairn.set_level(logging.getLevelName(old_level))
