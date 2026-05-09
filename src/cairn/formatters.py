import logging
import time

class CairnFormatter(logging.Formatter):
    """
    Standard SurvivalStack Formatter with UTC support.
    """
    def __init__(self, fmt=None, datefmt=None, style="%"):
        super().__init__(fmt, datefmt, style)
        self.converter = time.gmtime

