from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.task_group import TaskGroup
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
    concurrency=2,
) as dag:

    current_year = datetime.now().year
    current_month = datetime.now().month

    # Faltou criar as Dummies

    begin_ingestion = DummyOperator(task_id='begin_ingestion')
    end_ingestion = DummyOperator(task_id='end_ingestion')
    begin_transform = DummyOperator(task_id='begin_transform')
    end_transform = DummyOperator(task_id='end_transform')
    begin_load = DummyOperator(task_id='begin_load')
    end_load = DummyOperator(task_id='end_load')
  
    # Você também poderia criar um grupo de tasks para baixar os arquivos

    with TaskGroup('rab_data_ingestion') as rab_data_ingestion:

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
                begin_ingestion >> task >> end_ingestion
        
    # TODO: Criar as tasks de transformação e carga

    end_ingestion >> begin_transform >> end_transform >> begin_load >> end_load