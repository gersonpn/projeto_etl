import os
import requests
from datetime import datetime


#Função responsável por baixar os arquivos da API
def csv_arquivos(ano_inicial, pasta):
  ano_atual = datetime.now().year

  #Verifica se a pasta existe
  os.makedirs(pasta, exist_ok=True)


  # Laço de repetição responsável alterar na URL o ano e o mes.
  for ano in range(ano_inicial, ano_atual + 1):
    for mes in range(1, 13):
      meses = f"{mes:02d}"
      url = f"https://sistemas.anac.gov.br/dadosabertos/Aeronaves/RAB/Historico_RAB/{ano}-{meses}.csv"
      nome_arquivo = os.path.join(pasta, f" {ano}-{meses}.csv")


      try:
        response = requests.get(url) # Baixa o arquivo
        response.raise_for_status() # reporta se falhar

        #Salva localmente
        with open(nome_arquivo, 'wb') as f:
          f.write(response.content)
        print(f"Arquivo {nome_arquivo} salvo com sucesso!")
      except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo {url}: {e}")



csv_arquivos(2017, "arquivos_csv")