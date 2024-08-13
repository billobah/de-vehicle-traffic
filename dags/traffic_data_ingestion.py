from airflow import DAG
from airflow.exceptions import AirflowException
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import os

# Define the DAG with default appropriate arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create new DAG named 'traffic_data_ingestion'
# # It specifies the start date and schedule interval for the DAG

def check_data_exists(**kwargs):
    data_file_path = '../data/data1.csv'
    if os.path.exists(data_file_path):
        return True
    else:
        raise AirflowException(f"Data file not found at: {data_file_path}. Please check the path and ensure the data is available.")

with DAG(
 dag_id='traffic_data_ingestion',
 default_args=default_args,
 description='Orchestrate dbt workflow',
 schedule_interval='@daily', # Schedule the DAG to run daily
) as dag:

    # Task to check if data file exists
    check_data_exists_task = PythonOperator(
        task_id='check_data_exists',
        python_callable=check_data_exists,
        provide_context=True,
    )

    # Task to load data into PostgreSQL
    load_data_task = BashOperator(
        task_id='load_data',
        bash_command='psql -h postgres -U postgres -d traffic_data_warehouse -c "COPY traffic_data FROM \'/data/data_1.csv\' WITH (HEADER TRUE, DELIMITER \',\');"',
        # Adding retry delays and retries in case of failure
        retries=3,
        retry_delay=timedelta(seconds=30),
    )

    # Set task dependencies
    check_data_exists_task >> load_data_task