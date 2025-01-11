from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Função para a tarefa de teste
def print_hello():
    print("Hello, Airflow!")

# Definindo a DAG
dag = DAG(
    'test_dag',  # Nome da DAG
    description='Uma DAG de teste simples',
    schedule_interval=None,  # Não é agendada, será executada manualmente
    start_date=datetime(2025, 1, 11),  # Data de início
    catchup=False,  # Não executar tarefas passadas
)

# Definindo a tarefa
task1 = PythonOperator(
    task_id='print_hello_task',
    python_callable=print_hello,
    dag=dag,
)

# Definindo a sequência de execução
task1
