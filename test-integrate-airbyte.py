from airflow import DAG
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from datetime import datetime

with DAG(
    dag_id='airbyte_sync_example',
#    start_date=datetime(2023, 1, 1),
#    schedule_interval=None,
    catchup=False,
    tags=['airbyte', 'sync'],
) as dag:
    trigger_airbyte_sync = AirbyteTriggerSyncOperator(
        task_id='test_trigger_airbyte_sync',
        airbyte_conn_id='test_airbyte',  # The Airflow connection ID for Airbyte
        connection_id='3e4c2d19-8bf3-462f-a108-493a7da4d582',  # The UUID of your Airbyte connection
        asynchronous=False,  # Set to True for asynchronous execution and monitoring
        timeout=3600,  # Max time to wait for sync completion (if asynchronous=False)
        wait_seconds=3,  # Time to wait between status checks (if asynchronous=False)
    )
