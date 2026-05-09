# CAIRN: ARCHITECTURAL SOURCE OF TRUTH

## 1.0 THE CAIRN MANDATE
Cairn is the singular logging authority for all SurvivalStack projects. Its purpose is to enforce formatting consistency, timezone standardization (UTC), and file rotation across the entire ecosystem.

## 2.0 ARCHITECTURAL DECISIONS

### 2.1 The Singleton Pattern Rationale
Cairn employs a strict Singleton design (`Cairn.initialize()`) to globally mutate the Python `root_logger`.
*   **Rationale**: By hijacking the root logger, Cairn ensures that all third-party libraries and unconfigured loggers automatically inherit the SurvivalStack standard formatting.
*   **Constraint**: This is a destructive operation. Cairn clears all existing handlers on the root logger upon initialization.

### 2.2 The `SSUnknown` Fallback Convention
All Cairn log records must include a `project` attribute. 
*   **Convention**: If a third-party library emits a log record that lacks the `project` attribute, Cairn's `ProjectFallbackFilter` intercepts it and injects `SSUnknown`.
*   **Benefit**: This guarantees that logs remain parsable by centralized ingestion systems without crashing the formatter.

### 2.3 Naming Standardization (1:1:1 Mapping)
During the Governance Bootstrapping phase, the canonical name was permanently established as **cairn**.
*   **Registry**: `cairn`
*   **Package Name**: `cairn` (in `pyproject.toml`)
*   **Import Name**: `cairn`
*   **Local Folder**: `/home/chadh/survivalstack/cairn` (Case-sensitive alignment applied post-bootstrapping).

## 3.0 FUTURE CONSIDERATIONS
*   **Passive Mode**: A non-destructive "passive mode" may be implemented in the future (Issue #7) to allow Cairn to co-exist in systems where the root logger is managed externally.
