import logging

class ProjectFallbackFilter(logging.Filter):
    """
    Ensures that every log record has a 'project' attribute.
    Defaults to 'SSUnknown' if missing.
    """
    def __init__(self, project_name: str = "SSUnknown") -> None:
        super().__init__()
        self.project_name = project_name

    def filter(self, record: logging.LogRecord) -> bool:
        if not hasattr(record, "project"):
            record.project = self.project_name  # type: ignore
        return True
