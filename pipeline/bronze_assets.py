from dagster import asset
import pandas as pd
from connectors.oracle_connector import OracleConnector
from connectors.postgres_connector import PostgresConnector
from pipeline.utils import generate_hash



@asset
def bronze_query1():
    oracle = OracleConnector("data/query1.csv")        #Read the CSV file

    postgres = PostgresConnector(
        "postgresql://admin:admin@localhost:5432/data_platform"           #connect postgre
    )
    
    df = oracle.fetch_data()   #load data in dataframe
    df["ingestion_ts"] = pd.Timestamp.now()    #ingestion timestamp
    df["row_hash"] = df.apply(generate_hash, axis=1)    #Create row hash

    try:                 #handle incremental load with exception
        existing = postgres.read(
            "SELECT row_hash FROM bronze_query1"
        )

        df = df[
            ~df["row_hash"].isin(existing["row_hash"])
        ]
    except:
        pass
    postgres.write(df, "bronze_query1")    # Write to postgre

    return df
