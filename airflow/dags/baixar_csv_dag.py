from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import os
import requests

def baixar_arquivos_csv(ano_inicial, pasta):
    ano_atual = datetime.now().year
    os.makedirs(pasta, exist_ok=True)



    for ano in range(ano_inicial, ano_atual + 1):

        pasta_ano = os.path.join(pasta, str(ano))
        os.makedirs(pasta_ano, exist_ok=True)

        for mes in range(1, 13):
            meses = f"{mes:02d}"
            url = f"https://sistemas.anac.gov.br/dadosabertos/Aeronaves/RAB/Historico_RAB/{ano}-{meses}.csv"
            nome_arquivo = os.path.join(pasta_ano, f"{ano}-{meses}.csv")

            try:
                response = requests.get(url)
                response.raise_for_status()
                with open(nome_arquivo, 'wb') as f:
                    f.write(response.content)
                print(f"Arquivo {nome_arquivo} salvo com sucesso!")
            except requests.exceptions.RequestException as e:
                print(f"Erro ao baixar o arquivo {url}: {e}")

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': datetime(2017, 1, 1),
}

dag = DAG(
    'baixar_arquivos_csv',
    default_args=default_args,
    schedule_interval='@monthly',
)


download_task = PythonOperator(
    task_id='baixar_arquivos',
    python_callable=baixar_arquivos_csv,
    op_args=[2017, '/opt/airflow/data/raw'],
    dag=dag,
)