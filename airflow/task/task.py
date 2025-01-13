from airflow.operators.python_operator import PythonOperator
from function.function import baixar_arquivos_csv

def create_download_task(dag):
    return PythonOperator(
        task_id='baixar_arquivos',
        python_callable=baixar_arquivos_csv,
        op_args=[2017, '/opt/airflow/data/raw'],
        dag=dag,
    )
