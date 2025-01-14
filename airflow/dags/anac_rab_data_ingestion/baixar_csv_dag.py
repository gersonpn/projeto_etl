"""
Este módulo define uma DAG do Airflow para baixar arquivos CSV da ANAC.

A DAG é agendada para ser executada mensalmente e utiliza um operador Python para
executar a função `baixar_arquivos_csv` que baixa os arquivos CSV.

"""

from airflow import DAG
from datetime import datetime
from anac_rab_data_ingestion.tasks.ingest import baixar_arquivos_csv
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': datetime(2017, 1, 1),
}
"""
Argumentos padrão para a DAG.

- owner: Proprietário da DAG.
- retries: Número de tentativas de reexecução em caso de falha.
- start_date: Data de início da DAG.
"""

with DAG(
    'baixar_arquivos_csv',
    default_args=default_args,
    schedule_interval='@monthly',
    catchup=False,
) as dag:
    """
    Define a DAG para baixar arquivos CSV da ANAC.

    - default_args: Argumentos padrão para a DAG.
    - schedule_interval: Intervalo de agendamento da DAG.
    - catchup: Define se a DAG deve executar execuções passadas.
    """

    download_task = PythonOperator(
        task_id='download_task',
        python_callable=baixar_arquivos_csv,
        op_kwargs={'ano_inicial': 2017, 'pasta': '/opt/data/raw'},
        dag=dag,
    )
    """
    Tarefa para baixar arquivos CSV da ANAC.

    - task_id: Identificador da tarefa.
    - python_callable: Função Python a ser chamada.
    - op_kwargs: Argumentos para a função Python.
    - dag: DAG à qual a tarefa pertence.
    """
