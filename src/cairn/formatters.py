import logging
import time

class CairnFormatter(logging.Formatter):
    """
    Standard SurvivalStack Formatter with UTC support.
    """
    def __init__(self, fmt: str | None = None, datefmt: str | None = None, style: str = "%") -> None:
        # Pass style strictly if type checkers complain, though python 3.8+ handles it natively
        super().__init__(fmt, datefmt, style) # type: ignore
        self.converter = time.gmtime

