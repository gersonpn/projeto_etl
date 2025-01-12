
---

# Projeto de ETL - Dados da ANAC

Este projeto tem como objetivo realizar a **extração**, **transformação** e **carga** (ETL) de dados históricos sobre aeronaves fornecidos pela ANAC (Agência Nacional de Aviação Civil). A extração é feita a partir de uma API pública da ANAC, e os dados são armazenados em arquivos CSV para posterior processamento.

Além disso, o processo pode ser automatizado e orquestrado utilizando ferramentas como **Apache Airflow**.

## Descrição do Projeto

Este projeto realiza a **extração** dos dados históricos sobre aeronaves a partir da API pública da ANAC. Os dados são organizados por ano e mês e são armazenados localmente em arquivos CSV para posterior processamento e análise.

### Objetivos do Projeto
- **Extrair** dados históricos de aeronaves da API pública da ANAC.
- **Transformar** os dados conforme necessário para adequação a outros formatos ou para limpeza.
- **Carregar** os dados em um banco de dados ou data lake, para posterior análise.

## Estrutura do Projeto

A estrutura básica do projeto é organizada da seguinte forma:

```
projeto_etl/
├── dags/                  # Diretório para DAGs do Apache Airflow
├── logs/                  # Logs de execução dos scripts ETL
├── plugins/               # Plugins personalizados para o Airflow
├── raw/                   # Armazenamento dos dados brutos (arquivos CSV)
├── docker-compose.yml     # Arquivo de configuração do Docker Compose
├── baixar_arquivos_csv.py # Script para baixar arquivos CSV da ANAC
└── README.md              # Este arquivo
```

## Como Usar

### Requisitos

1. **Python 3.x** - Certifique-se de ter o Python instalado.
2. **Bibliotecas**: Instale as dependências do projeto utilizando o comando:
   ```bash
   pip install -r requirements.txt
   ```

3. **Docker (opcional)** - Caso deseje usar Docker para orquestrar o Apache Airflow, pode configurar e executar os containers utilizando o arquivo `docker-compose.yml`.

4. **Diretórios**:
   - O diretório `raw/` será utilizado para armazenar os arquivos CSV baixados.
   - Os diretórios `logs/` e `plugins/` podem ser configurados para armazenar logs e plugins personalizados, caso esteja utilizando o Airflow.

### Passos para Executar

1. **Executando o Script Python**:

   Para iniciar o processo de download dos arquivos CSV, basta executar o script Python que realizará a extração dos dados. O script pode ser configurado para baixar os arquivos desde um ano inicial (ex: 2017) até o ano atual e armazená-los na pasta `raw/`.

2. **Usando Apache Airflow (opcional)**:
   - O Apache Airflow pode ser utilizado para automatizar e orquestrar o processo de extração dos dados. Caso opte por utilizá-lo, configure uma **DAG** (Directed Acyclic Graph) para executar o processo de forma periódica, conforme desejado.
   - O arquivo `docker-compose.yml` pode ser utilizado para configurar e rodar o Apache Airflow em containers Docker.

3. **Armazenamento e Processamento**:
   - Após o download dos arquivos, você pode processá-los utilizando ferramentas como **pandas** para transformação de dados ou carregar os dados em um banco de dados ou data lake para análises posteriores.

### Considerações Finais

- O projeto pode ser expandido para incluir mais etapas de **transformação** e **carregamento** dos dados.
- A integração com bancos de dados (como PostgreSQL ou MySQL) ou soluções em nuvem (como AWS S3 ou Google Cloud Storage) pode ser realizada para armazenar os dados processados.
- A automação e orquestração utilizando **Apache Airflow** garantem a execução periódica e a monitoração do processo ETL.

## Tecnologias Usadas

- **Python 3.x**
- **requests** (para realizar requisições HTTP)
- **pandas** (para manipulação e transformação de dados)
- **Docker** (para orquestração com o Airflow)
- **Apache Airflow** (para agendamento e orquestração do processo ETL)
- **PostgreSQL** (para armazenar dados processados)

---
