from connectors.postgres_connector import PostgresConnector
import pandas as pd

conn = PostgresConnector(
    "postgresql://admin:admin@localhost:5432/data_platform"
)

df = pd.DataFrame({
    "id": [1, 2],
    "name": ["A", "B"]
})

conn.write(df, "test_table")

print("SUCCESS")