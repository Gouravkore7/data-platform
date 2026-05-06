from dagster import asset
import pandas as pd

from connectors.oracle_connector import OracleConnector
from connectors.postgres_connector import PostgresConnector

from pipeline.utils import generate_hash


@asset
def bronze_query1():

    # Read CSV (mock Oracle)
    oracle = OracleConnector("data/query1.csv")

    # Connect Postgres
    postgres = PostgresConnector(
        "postgresql://admin:admin@localhost:5432/data_platform"
    )

    # Load data
    df = oracle.fetch_data()

    # Add ingestion timestamp
    df["ingestion_ts"] = pd.Timestamp.now()

    # Generate row hash
    df["row_hash"] = df.apply(generate_hash, axis=1)

    # Incremental loading
    try:
        existing = postgres.read(
            "SELECT row_hash FROM bronze_query1"
        )

        df = df[
            ~df["row_hash"].isin(existing["row_hash"])
        ]

    except:
        pass

    # Write to postgres
    postgres.write(df, "bronze_query1")

    return df