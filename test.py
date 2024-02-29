import requests         # pip install requests
from pandas import DataFrame , read_excel   # pip install pandas
import numpy as np      # pip install numpy
from _verificar import verificar_bot , tags_tabela # arquivo separado necessario
from openpyxl import Workbook , load_workbook
import xlwt
import datetime
#https://api.brawlstars.com/v1/#/definitions/BannedBrawlEntry


with open('token.txt', 'r', encoding='utf-8') as arquivo:
    token = arquivo.read().strip()

jogador = 'R2LR2QLG'

url_api = f"https://api.brawlstars.com/v1/players/%23{jogador}/battlelog"
headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url_api, headers=headers)

if response.status_code == 200:  # Verifica se a solicitação foi bem-sucedida
    data = response.json()  # Converte a resposta JSON em um dicionário Python
    print(data)

    # Verifica se a resposta contém uma lista de brawlers banidos
    if "BannedBrawlerList" in data:
        banned_brawlers = data["BannedBrawlerList"]

        # Itera sobre a lista de brawlers banidos e exibe os dados
        for brawler in banned_brawlers:
            brawler_id = brawler.get("id")
            brawler_side = brawler.get("side")
            print(f"Brawler ID: {brawler_id}, Side: {brawler_side}")
    else:
        print("Não foram encontrados brawlers banidos na resposta da API.")
else:
    print(f"Erro ao acessar a API. Código de status: {response.status_code}")
