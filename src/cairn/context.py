import logging
from contextlib import contextmanager
from typing import Generator
from .core import Cairn

@contextmanager
def cairn_test_context(level: str | None = None) -> Generator[None, None, None]:
    """
    Context manager for temporary logging overrides during tests.
    
    Args:
        level: Optional logging level to set for the duration of the context.
               If None, the current level is maintained.
               
    Yields:
        None
    """
    root_logger = logging.getLogger()
    old_level = root_logger.level
    
    if level:
        Cairn.set_level(level)
        
    try:
        yield
    finally:
        Cairn.set_level(logging.getLevelName(old_level))
