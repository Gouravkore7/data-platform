from dagster import asset

from connectors.postgres_connector import PostgresConnector


@asset(deps=["bronze_query1"])
def silver_query1():

    postgres = PostgresConnector(
        "postgresql://admin:admin@localhost:5432/data_platform"
    )

    # Read bronze data
    df = postgres.read(
        "SELECT * FROM bronze_query1"
    )

    # Standardize column names
    df.columns = [col.lower() for col in df.columns]

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle nulls
    df = df.fillna(0)

    # Convert date type
    df["date"] = df["date"].astype(str)

    # Add metadata
    df["pipeline_layer"] = "silver"

    # Write silver table
    postgres.write(df, "silver_query1")

    return df