# data-platform

I build a local data platform with Dagster,Docker , PostgreSQL and Python.

It ingests Oracle query results, processes them through bronze -> silver  -> gold layers, and serves downstream datasets for analytics.

CSV (Mock Oracle)
    ↓
Bronze Layer
    ↓
Silver Layer
    ↓
Gold Layer

Started dagster with 'dagster dev' command in CMD

Bronze Layer stores raw data  as received from source system.

Silver layer tranformend and cleans the data.

Gold layer create business ready datasets optimized for analytics.

To avoid full historical reloads, I implement hash-based row-level change detection to process only changed data.

Dagster assets were used to model explicit data dependencies and improve observability.
 
I also configured YAML files to support multiple clients deployment with minimum code change.

with more upgradations, i also implement later indexing, CI CD, partationing and more validations.

- Add schema validation

