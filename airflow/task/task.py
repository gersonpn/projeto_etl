download_task = PythonOperator(
    task_id='baixar_arquivos',
    python_callable=baixar_arquivos_csv,
    op_args=[2017, '/opt/airflow/data/raw'],
    dag=dag,
)