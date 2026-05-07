from dagster import sensor, RunRequest

from pipeline.schedules import daily_job

@sensor(job=daily_job)
def file_sensor():

    new_file_found = True
    if new_file_found:
        yield RunRequest(
            run_key=None
        )
