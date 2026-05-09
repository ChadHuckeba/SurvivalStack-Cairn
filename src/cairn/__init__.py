import logging
from .core import Cairn
from .context import cairn_test_context

__all__ = ["Cairn", "get_logger", "cairn_test_context"]

def get_logger(name: str):
    """
    Returns a logger instance with the project attribute pre-populated.
    """
    logger = logging.getLogger(name)
    # The Filter added to the root logger in Cairn.initialize() 
    # handles the 'project' attribute injection.
    return logger
