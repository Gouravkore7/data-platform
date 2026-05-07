from dagster import asset

from connectors.postgres_connector import PostgresConnector



@asset(deps=["bronze_query1"])
def silver_query1():
    postgres = PostgresConnector(
        "postgresql://admin:admin@localhost:5432/data_platform"
    )

    df = postgres.read(
        "SELECT * FROM bronze_query1"                       # read bronze_data
    )

    df.columns = [col.lower() for col in df.columns]    # lowercase the column names

    df = df.drop_duplicates()      # remove duplicate data

    df = df.fillna(0)        # handle null valus

    
    df["date"] = df["date"].astype(str)    # convert date type

    df["pipeline_layer"] = "silver"

    postgres.write(df, "silver_query1")          # write data to silver table

    return df
