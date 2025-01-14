"""
Este módulo contém a função para baixar arquivos CSV da ANAC.

A função `baixar_arquivos_csv` baixa arquivos CSV de uma URL específica e os salva
em um diretório local organizado por ano e mês.

"""

import os
import requests
from datetime import datetime

def baixar_arquivos_csv(ano_inicial, pasta):
    """
    Baixa arquivos CSV da ANAC e os salva em um diretório local.

    Esta função baixa arquivos CSV de uma URL específica da ANAC, organizados por ano e mês,
    e os salva em um diretório local. Se o diretório não existir, ele será criado.

    Args:
        ano_inicial (int): O ano inicial para o download dos arquivos CSV.
        pasta (str): O caminho do diretório onde os arquivos CSV serão salvos.

    Raises:
        requests.exceptions.RequestException: Se ocorrer um erro ao fazer a requisição HTTP.

    """
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
