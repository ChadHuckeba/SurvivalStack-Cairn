# SurvivalStack Cairn

**Cairn** is the centralized, authoritative logging library for the SurvivalStack ecosystem. It ensures consistent log formatting, file rotation, and contextual attribution (e.g., project names) across all Product Line Architecture services.

## Installation

Install Cairn into your SurvivalStack project using `uv`:

```bash
uv add git+ssh://git@github.com/ChadHuckeba/SurvivalStack-Cairn.git
```

## Setup & Initialization

Initialize the `Cairn` singleton at the entry point of your application. This hijacks the root logger to guarantee consistent formatting.

```python
from cairn import Cairn, get_logger

# Initialize Cairn (Replace "YourProject" with your specific project tag)
Cairn.initialize(
    project_name="YourProject", 
    log_file="logs/your_project.log", 
    level="INFO"
)

logger = get_logger(__name__)
logger.info("Cairn initialized successfully.")
```

## Log Formats

Cairn produces highly structured, UTC-based logs.

**Console Format:**
```text
2026-05-09 12:00:00,000 | INFO     | YourProject | your_project.engine | Cairn initialized successfully.
```

**File Format:**
```text
[2026-05-09 12:00:00,000] [INFO] [YourProject] [your_project.engine] - Cairn initialized successfully.
```
