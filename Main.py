import requests         # pip install requests
from pandas import DataFrame , read_excel   # pip install pandas
import numpy as np      # pip install numpy
from _verificar import verificar_bot , tags_tabela # arquivo separado necessario
from _partidas import dados_treino
from openpyxl import Workbook , load_workbook
import PySimpleGUI as sg
import json

# Precisa das extenções acima instaladas para funcionar corretamente
jogadores = {
    'Meliodas': 'CPPV2PQG',
    'Mohtep': 'R2LR2QLG',
    'Zeusbiel': 'R08QV29J',
    'Niceshot': 'GRLUYG0R',
    'Golden': '9QCJPL20',
    'Pitbull': '2LUP2PGR',
    'Rei do Fute': 'RVL0RPR9',
    'Zeta': '90JCYPQU',
    'Nico': 'PC9LPPYV',
    'Lenain': '20L88L2J'
}

# Layout do menu
layout = [
    [sg.Text('Escolha um jogador:', size=(20, 1), justification='left')],
    [sg.Button(nome, key=tag) for nome, tag in jogadores.items()]
]

# Criando a janela
window = sg.Window('Menu de Jogadores', layout)

# Loop para eventos
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        escolha = None  # Se a janela for fechada sem fazer uma escolha
        break

    if event in jogadores.values():
        escolha = event  # Atribui a tag do jogador selecionado a escolha
        break

# Fechar a janela ao finalizar
window.close()

print(f"Jogador selecionado: {escolha}")
print('Obtendo dados...')
# URL da API
# tagsPlanilha = read_excel('TimesAPI.xlsx')
# teste = tagsPlanilha['Tag 1']
# jogador = teste[0]
# jogador = jogador.replace("#", "")
# print(jogador)

with open('token.txt', 'r', encoding='utf-8') as arquivo:
    token = arquivo.read().strip()

url_api = f"https://api.brawlstars.com/v1/players/%23{escolha}/battlelog"
# Cabeçalho de autorização com o token JWT
headers = {"Authorization": f"Bearer {token}"}
# Solicitação HTTP GET para acessar a API
response = requests.get(url_api, headers=headers)

dados_treino(response)


