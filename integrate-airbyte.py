from airflow.decorators import dag
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator

@dag(
    dag_id="trigger_airbyte_postgres_to_sftp",
#    schedule="@daily",  # Or whatever schedule you want
    catchup=False,
    tags=["airbyte", "sftp", "postgres"],
)
def trigger_airbyte_postgres_to_sftp_sync():
    """
    ### Airbyte Sync DAG
    This DAG manually triggers an Airbyte sync job for the
    PostgreSQL to SFTP JSON connection.
    """

    AirbyteTriggerSyncOperator(
        task_id="trigger_airbyte_sync_pg_to_sftp",

        # 1. This is the Airflow Connection ID you created in Step 3
        airbyte_conn_id="my_airbyte",

        # 2. This is the Airbyte Connection ID you got from the URL in Step 2
        connection_id="3e4c2d19-8bf3-462f-a108-493a7da4d582",

        # 3. (Optional) Wait for the sync to finish before marking the task as 'success'
        #wait_for_completion=True,

        # 4. (Optional) How long to wait before timing out (in seconds)
        timeout=3600 
    )

# Instantiate the DAG
trigger_airbyte_postgres_to_sftp_sync()
