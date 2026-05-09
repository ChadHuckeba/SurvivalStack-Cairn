import logging
import threading
from pathlib import Path
from logging.handlers import RotatingFileHandler
from .formatters import CairnFormatter
from .filters import ProjectFallbackFilter

class Cairn:
    _lock = threading.Lock()
    _initialized = False
    _project_name = "SSUnknown"

    @classmethod
    def initialize(
        cls, 
        project_name: str, 
        log_file: str | None = None, 
        level: str = "INFO",
        rotation_mb: int = 10,
        backup_count: int = 5
    ) -> None:
        """
        Initializes the Cairn singleton, establishing global logging configurations.
        
        WARNING: This is a destructive operation. It will clear all existing
        handlers on the root logger and replace them with Cairn's standard
        console and (optional) file handlers.
        
        Args:
            project_name: The name of the project initializing the logger.
            log_file: Optional path to a file for log rotation output.
            level: The root logging level (e.g., 'INFO', 'DEBUG').
            rotation_mb: Max file size in MB before rotation occurs.
            backup_count: Number of backup log files to retain.
        """
        with cls._lock:
            if cls._initialized:
                return

            cls._project_name = project_name
            root_logger = logging.getLogger()
            root_logger.setLevel(level.upper())
            
            # Clear existing handlers
            for handler in root_logger.handlers[:]:
                root_logger.removeHandler(handler)

            # Standard Filter for all handlers
            fallback_filter = ProjectFallbackFilter(project_name)

            # Console Handler
            console_fmt = "%(asctime)s | %(levelname)-8s | %(project)s | %(name)s | %(message)s"
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(CairnFormatter(console_fmt))
            console_handler.addFilter(fallback_filter)
            root_logger.addHandler(console_handler)

            # File Handler
            if log_file:
                log_path = Path(log_file)
                log_path.parent.mkdir(parents=True, exist_ok=True)
                
                file_fmt = "[%(asctime)s] [%(levelname)s] [%(project)s] [%(name)s] - %(message)s"
                file_handler = RotatingFileHandler(
                    log_file, 
                    maxBytes=rotation_mb * 1024 * 1024, 
                    backupCount=backup_count
                )
                file_handler.setFormatter(CairnFormatter(file_fmt))
                file_handler.addFilter(fallback_filter)
                root_logger.addHandler(file_handler)

            cls._initialized = True

    @classmethod
    def reset(cls) -> None:
        """
        Resets the Cairn state, removing all handlers and filters from the root logger.
        
        This is primarily used for testing purposes to ensure a clean state
        between test cases.
        """
        with cls._lock:
            root_logger = logging.getLogger()
            for handler in root_logger.handlers[:]:
                root_logger.removeHandler(handler)
            # Remove global filters if any
            for f in root_logger.filters[:]:
                root_logger.removeFilter(f)
            cls._initialized = False
            cls._project_name = "SSUnknown"

    @classmethod
    def set_level(cls, level: str) -> None:
        """
        Thread-safe method to adjust the global logging level dynamically.
        
        Args:
            level: The new logging level string (e.g., 'DEBUG', 'WARNING').
        """
        with cls._lock:
            logging.getLogger().setLevel(level.upper())