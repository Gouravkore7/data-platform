
from dagster import (
    asset_check,
    AssetCheckResult
)
from connectors.postgres_connector import PostgresConnector



@asset_check(asset="gold_risk_dataset")
def check_null_customer_ids():

    postgres = PostgresConnector(
        "postgresql://admin:admin@localhost:5432/data_platform"
    )
    df = postgres.read(
        "SELECT * FROM gold_risk_dataset"
    )
    passed = df["customer_id"].isnull().sum() == 0
    return AssetCheckResult(
        passed=passed
    )
