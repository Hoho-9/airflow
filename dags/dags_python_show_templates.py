import datetime
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task

with DAG(
    dag_id="example_python_operator",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=True
) as dag:
    
    @task(task_id='python_task')
    def show_templates(**kwargs):
        from pprint import pprint
        print(kwargs)
        
        
    show_templates()