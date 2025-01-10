import os
import requests
from datetime import datetime


def baixar_arquivos_csv(ano_inicial, pasta):
  ano_atual = datetime.now().year


  os.makedirs(pasta, exist_ok=True)


  for ano in range(ano_inicial, ano_atual + 1):
    for mes in range(1, 13):
      meses = f"{mes:02d}"
      url = f"https://sistemas.anac.gov.br/dadosabertos/Aeronaves/RAB/Historico_RAB/{ano}-{meses}.csv"
      nome_arquivo = os.path.join(pasta, f" {ano}-{meses}.csv")


      try:
        response = requests.get(url)
        response.raise_for_status()

        with open(nome_arquivo, 'wb') as f:
          f.write(response.content)
        print(f"Arquivo {nome_arquivo} salvo com sucesso!")
      except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo {url}: {e}")



baixar_arquivos_csv(2017, "raw")


