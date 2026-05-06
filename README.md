# data-platform

I built a modular local data platform using Dagster, PostgreSQL, Docker, and Python.

To avoid full reloads, I implemented hash-based row-level change detection.

Dagster assets model dependencies explicitly, with schedules, sensors, and asset checks added for orchestration and observability.

Configuration was externalized into YAML files to support multiple client deployments with minimal code changes.

With more time, I would add indexing, partitioning, CI/CD, and more robust validation.
