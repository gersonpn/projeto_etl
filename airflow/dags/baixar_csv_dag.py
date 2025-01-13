from airflow import DAG
from datetime import datetime
from task.task import create_download_task

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': datetime(2017, 1, 1),
}

with DAG(
    'baixar_arquivos_csv',
    default_args=default_args,
    schedule_interval='@monthly',
    catchup=False,
) as dag:

    download_task = create_download_task(dag)
