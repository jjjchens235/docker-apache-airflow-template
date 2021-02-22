from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime


def hello_world():
    print('hello world!!')


default_args = {
    "owner": "airflow",
    "depends_on_past": True,
    'wait_for_downstream': True,
    "start_date": datetime(2021, 2, 20),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1
}


dag = DAG("hello_world", default_args=default_args,
          schedule_interval="* 9 * * *", max_active_runs=1)

start_of_data_pipeline = DummyOperator(task_id='start_of_data_pipeline', dag=dag)

hello_task = PythonOperator(
    task_id="hello_world_task",
    python_callable=hello_world,
    dag=dag
)

start_of_data_pipeline >> hello_task
