from dagster import schedule, define_asset_job

daily_job = define_asset_job(
    name="daily_pipeline_job"
)

@schedule(
    cron_schedule="0 2 * * *",
    job=daily_job
)
def daily_schedule():
    return {}