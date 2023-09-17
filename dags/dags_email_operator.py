from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 * * *", # 0시 10분, 매월 첫 번째주 토요일에 작업을 수행함
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    send_email_task = EmailOperator(
        task_id='send_email_task'
        to='stickrpg@naver.com',
        subject='Airflow 성공 메일',
        html_content= 'Airflow 작업이 성공했습니다.'
    )
    
    

