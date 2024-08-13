from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'traffic_data_pipeline',
    default_args=default_args,
    description='Orchestrate dbt workflow',
    schedule_interval='@daily',  # Schedule the DAG to run daily
)

# Function to execute dbt transformation
def run_dbt_transformation(**kwargs):
    command = 'dbt run --profiles-dir ./ --project-dir ./'
    os.system(command)

# Define PythonOperator to execute dbt transformation
run_dbt_task = PythonOperator(
    task_id='run_dbt_transformation',
    python_callable=run_dbt_transformation,
    provide_context=True,
    dag=dag,
)

# Set task dependencies
# Set task dependencies
run_dbt_task >> load_data_task