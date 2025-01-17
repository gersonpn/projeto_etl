import os
import requests
import logging
def baixar_arquivos_csv(ano_inicial, mes, pasta):
    """
    Baixa arquivos CSV de acordo com o ano e mês especificados.
    """
    os.makedirs(pasta, exist_ok=True)
    url = f"https://sistemas.anac.gov.br/dadosabertos/Aeronaves/RAB/Historico_RAB/{ano_inicial}-{mes:02d}.csv"
    nome_arquivo = os.path.join(pasta, f"{ano_inicial}-{mes:02d}.csv")
    logging.info(f"Baixando arquivo {nome_arquivo}...")
    try:
        response = requests.head(url, timeout=10)
        if response.status_code == 200:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            with open(nome_arquivo, 'wb') as f:
                f.write(response.content)
            logging.info(f"Arquivo {nome_arquivo} salvo com sucesso!")
        else:
            raise ValueError(f"Arquivo não encontrado: {url}")
    except Exception as e:
        logging.error(f"Erro ao baixar {url}: {str(e)}")
        raise RuntimeError(f"Erro ao baixar {url}: {str(e)}")
