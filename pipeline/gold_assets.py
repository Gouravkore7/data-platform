from dagster import asset
import pandas as pd

from connectors.postgres_connector import PostgresConnector


@asset(deps=["silver_query1"])
def gold_risk_dataset():

    postgres = PostgresConnector(
        "postgresql://admin:admin@localhost:5432/data_platform"
    )

    df = postgres.read(
        "SELECT * FROM silver_query1"
    )

    df["date"] = pd.to_datetime(df["date"])

    agg = df.groupby("customer_id").agg({
        "transaction_id": "count",
        "amount": "sum",
        "date": "max"
    }).reset_index()

    agg.columns = [
        "customer_id",
        "frequency",
        "monetary",
        "last_transaction_date"
    ]

    agg["recency_days"] = (
        pd.Timestamp.now() - agg["last_transaction_date"]
    ).dt.days

    postgres.write(
        agg,
        "gold_risk_dataset"
    )

    return agg


@asset(deps=["silver_query1"])
def gold_analytics_dataset():

    postgres = PostgresConnector(
        "postgresql://admin:admin@localhost:5432/data_platform"
    )

    df = postgres.read(
        "SELECT * FROM silver_query1"
    )

    df["date"] = pd.to_datetime(df["date"])

    df["month"] = df["date"].dt.to_period("M").astype(str)

    monthly_summary = df.groupby("month").agg({
        "amount": "sum",
        "transaction_id": "count"
    }).reset_index()

    monthly_summary.columns = [
        "month",
        "total_amount",
        "total_transactions"
    ]

    postgres.write(
        monthly_summary,
        "gold_analytics_dataset"
    )

    return monthly_summary