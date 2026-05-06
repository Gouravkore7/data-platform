from dagster import Definitions

from pipeline.bronze_assets import bronze_query1
from pipeline.silver_assets import silver_query1

from pipeline.gold_assets import (
    gold_risk_dataset,
    gold_analytics_dataset
)

from pipeline.schedules import daily_schedule

from pipeline.sensors import file_sensor

from pipeline.checks import check_null_customer_ids


defs = Definitions(

    assets=[
        bronze_query1,
        silver_query1,
        gold_risk_dataset,
        gold_analytics_dataset
    ],

    schedules=[
        daily_schedule
    ],

    sensors=[
        file_sensor
    ],

    asset_checks=[
        check_null_customer_ids
    ]
)