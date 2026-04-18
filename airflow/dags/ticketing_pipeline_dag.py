from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "kaustav",
    "retries": 1,
    "retry_delay": timedelta(seconds=5)
}

with DAG(
    dag_id="ticketing_batch_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
    description="Ticket Processing Batch Pipeline"
) as dag:

    generate_data = BashOperator(
        task_id="generate_data",
        bash_command="python /opt/airflow/scripts/generate_data.py"
    )

    merge_data = BashOperator(
        task_id="merge_data",
        bash_command="python /opt/airflow/scripts/merge_data.py"
    )
    
    process_data = BashOperator(
        task_id="process_data",
        bash_command="python /opt/airflow/scripts/process.py"
    )

    load_to_db = BashOperator(
        task_id="load_to_db",
        bash_command="python /opt/airflow/scripts/load_to_db.py"
    )

    analysis = BashOperator(
        task_id="performance_analysis",
        bash_command="python /opt/airflow/scripts/performance_analysis.py"
    )

    # Flow
    generate_data >>  merge_data >> process_data >> load_to_db >> analysis