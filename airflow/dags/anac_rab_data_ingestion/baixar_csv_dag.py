from airflow import DAG
from datetime import datetime
from anac_rab_data_ingestion.tasks.ingest import baixar_arquivos_csv
from airflow.operators.python_operator import PythonOperator

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

    download_task = PythonOperator(
        task_id='download_task',
        python_callable=baixar_arquivos_csv,
        op_kwargs={'ano_inicial': 2017, 'pasta': '/opt/data/raw'},
        dag=dag,
    )

