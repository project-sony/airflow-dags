from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="hello_world_dag_2",
    start_date=datetime(2023, 1, 1),
    #schedule_interval=None,  # Run manually
    catchup=False,
    tags=["example"],
) as dag:
    # Task to print "Hello"
    hello_task = BashOperator(
        task_id="print_hello",
        bash_command="echo 'Hello'",
    )

    # Task to print "World"
    world_task = BashOperator(
        task_id="print_world",
        bash_command="echo 'World'",
    )

    # Define the dependency: print_hello must complete before print_world
    hello_task >> world_task