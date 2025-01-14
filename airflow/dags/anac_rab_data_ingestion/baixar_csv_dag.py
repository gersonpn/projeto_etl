from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from anac_rab_data_ingestion.tasks.ingest import baixar_arquivos_csv

default_args = {
    'owner': 'airflow',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2017, 1, 1),
}

with DAG(
    'baixar_arquivos_csv',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    current_year = datetime.now().year
    current_month = datetime.now().month

    tasks = []

    for ano in range(2017, current_year + 1):
        for mes in range(1, 13):
            # Evita criar tasks para meses futuros no ano atual
            if ano == current_year and mes > current_month:
                break

            task = PythonOperator(
                task_id=f'baixar_{ano}_{mes:02d}',
                python_callable=baixar_arquivos_csv,
                op_kwargs={
                    'ano_inicial': ano,
                    'mes': mes,
                    'pasta': '/opt/data/raw',
                },
            )
            tasks.append(task)

    # Define dependências (opcional, caso precise rodar sequencialmente)
    for i in range(1, len(tasks)):
        tasks[i - 1] >> tasks[i]
