Aqui está um modelo de **README.md** para o seu projeto de Engenharia de Dados, que realiza a extração de dados da API da ANAC e os salva localmente para posterior processamento:

---

# Projeto de ETL - Dados da ANAC

Este projeto visa realizar a extração, transformação e carga (ETL) de dados históricos de aeronaves fornecidos pela ANAC (Agência Nacional de Aviação Civil). Os dados são extraídos a partir de uma API pública da ANAC e armazenados em arquivos CSV. Esse processo pode ser automatizado e integrado com ferramentas de orquestração como **Apache Airflow**.

## Descrição do Projeto

O script realiza o **download dos arquivos CSV** contendo dados históricos sobre aeronaves, organizados por ano e mês. O script é configurado para baixar dados desde um ano inicial (por exemplo, 2017) até o ano atual.

A extração dos dados é feita através de requisições HTTP para a URL da API da ANAC, e os arquivos são salvos localmente em uma pasta definida pelo usuário.

### Objetivos do Projeto
- **Extrair** dados históricos de aeronaves da API pública da ANAC.
- **Transformar** os dados, podendo ser feito no futuro para adequação a outros formatos ou limpeza.
- **Carregar** os dados em um banco de dados ou data lake (posteriormente).

## Estrutura do Projeto

A estrutura básica do projeto está organizada da seguinte forma:

```
projeto_etl/
├── dags/                  # Diretório para DAGs do Apache Airflow (caso utilizado)
├── logs/                  # Logs de execução dos scripts ETL
├── plugins/               # Plugins personalizados para o Airflow (se necessário)
├── raw/                   # Diretório para armazenar os arquivos CSV baixados
├── scripts/               # Scripts Python para o ETL (Extração, Transformação, Carga)
├── docker-compose.yml     # Arquivo de configuração para o Docker Compose (se necessário)
├── requirements.txt       # Dependências do projeto (ex: requests, pandas, etc.)
└── README.md              # Este arquivo
```

## Como Usar

### Requisitos

1. **Python 3.x** - Certifique-se de ter o Python instalado.
2. **Bibliotecas**: Instale as dependências do projeto usando o `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Docker (opcional)** - Se você deseja usar Docker para orquestrar o Apache Airflow, você pode configurar e executar os containers usando o arquivo `docker-compose.yml`.

4. **Diretórios**:
   - O diretório `raw/` será utilizado para armazenar os arquivos CSV baixados.
   - Os diretórios `logs/` e `plugins/` podem ser configurados para armazenar logs e plugins personalizados, caso esteja utilizando o Airflow para orquestração.

### Passos para Executar

1. **Executando o Script Python**:

   - O script `baixar_arquivos_csv.py` realiza a extração dos dados. Basta chamar a função `baixar_arquivos_csv(ano_inicial, pasta)` para começar o download dos arquivos CSV.

   Exemplo:
   ```python
   from baixar_arquivos_csv import baixar_arquivos_csv
   baixar_arquivos_csv(2017, "raw")
   ```

   - Isso baixará os arquivos desde 2017 até o ano atual e os salvará na pasta `raw/`.

2. **Usando Apache Airflow (opcional)**:
   - O Airflow pode ser usado para agendar e orquestrar o processo ETL.
   - A DAG (Directed Acyclic Graph) pode ser configurada para rodar o script periodicamente.
   - Verifique as instruções de como configurar o Airflow usando o `docker-compose.yml` ou configurando diretamente em seu ambiente.

3. **Armazenamento e Processamento**:
   - Após os arquivos serem baixados, você pode processá-los utilizando ferramentas como **pandas** para transformação ou carregamento para um banco de dados/data lake.

### Exemplo de Execução

1. **Baixar Arquivos**:
   Execute o script Python para baixar os arquivos de dados históricos da ANAC.

   ```bash
   python baixar_arquivos_csv.py
   ```

   Isso irá salvar os arquivos CSV em uma pasta chamada `raw/`.

2. **Carregar no Airflow (opcional)**:
   Caso deseje automatizar o processo, configure uma DAG no Airflow para executar o script de download periodicamente.

   Exemplo de DAG simples para execução no Airflow:
   ```python
   from airflow import DAG
   from airflow.operators.python_operator import PythonOperator
   from baixar_arquivos_csv import baixar_arquivos_csv
   from datetime import datetime

   default_args = {
       'owner': 'airflow',
       'retries': 1,
       'start_date': datetime(2023, 1, 1),
   }

   dag = DAG(
       'baixar_arquivos_csv',
       default_args=default_args,
       schedule_interval='@monthly',  # Executar mensalmente
   )

   download_task = PythonOperator(
       task_id='baixar_arquivos',
       python_callable=baixar_arquivos_csv,
       op_args=[2017, '/opt/airflow/dags/raw'],
       dag=dag,
   )
   ```

### Considerações Finais

- Este projeto pode ser expandido para incluir mais etapas de **Transformação** e **Carregamento** dos dados.
- A integração com bancos de dados (PostgreSQL, MySQL, etc.) ou soluções em nuvem (AWS S3, Google Cloud Storage) pode ser feita para armazenar dados processados.
- A automação e orquestração utilizando **Apache Airflow** ajuda a garantir a execução periódica e a monitoração do processo ETL.

## Tecnologias Usadas

- **Python 3.x**
- **requests** (para realizar requisições HTTP)
- **pandas** (para processamento e transformação de dados - caso seja necessário)
- **Docker** (para orquestração com o Airflow)
- **Apache Airflow** (para agendamento e orquestração do processo ETL)
- **PostgreSQL** ou outros bancos de dados (para armazenar dados processados)

---

Este **README** fornece uma explicação geral do projeto, como executá-lo localmente ou em ambientes de produção, e como expandir o pipeline ETL. Adapte conforme as necessidades do seu projeto e da sua equipe!