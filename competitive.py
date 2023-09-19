import requests         # pip install requests
import pandas as pd     # pip install pandas
import numpy as np      # pip install numpy
import xlwt
import datetime

# Precisa destas extenções instaladas para funcionar corretamente

confirm = 1
dia_feito = []
listaEventos = []
listaMapas = []
resultado1 = []
resultado2 = []
resultTime1 = []
resultTime2 = []
brawlTime1 = []
brawlTime2 = []
brawlPlayers1 = []
brawlPlayers2 = []
tagsTime1 = []
tagsTime2 = []
playersTime1 = []
playersTime2 = []
tabela = []
tags1 = []
tags2 = []
players1 = []
players2 = []
index = []
cont = -1


coluna1 = ['Modo','Mapa','Tag 1','Tag 2','Tag 3','Player 1','Player 2','Player 3','Brawler 1','Brawler 2','Brawler 3','Resultado','Brawler 4','Brawler 5','Brawler 6','Player 4','Player 5','Player 6','Tag 4','Tag 5','Tag 6','Data']
# Token JWT
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM4NzY4YjMwLTQ5YjUtNDAyOC1hMjRlLWI3YzQ1NWQwOTgyYyIsImlhdCI6MTY5NTA3Nzc5MCwic3ViIjoiZGV2ZWxvcGVyLzkwZmNhYjhlLTZiOGYtNzMzZS05NzllLTgwOWJjMTM3NTgzNyIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTc3Ljc2LjE5Mi4xNDkiLCIxODcuNzUuNjguMTY4Il0sInR5cGUiOiJjbGllbnQifV19.V8H_jlnFrSxC4hBLWORBSgugkQrBO3-EVQcqcenXFpuo5M50LZofXjhc905IDs5Ipp0bKOskap-f6oEjCsJUfA"


mohtep = 'R2LR2QLG'
zeusbiel = 'R08QV29J'
virus8 = 'UV8RV8JU'
niceshot = 'GRLUYG0R'
golden = '9QCJPL20'

escolha = input('Escolher jogador ( m / z / n / g / v ): ')
match escolha:
    case 'v':
        jogador = virus8
    case 'z':
        jogador = zeusbiel
    case '':
        jogador = mohtep
    case 'm':
        jogador = mohtep
    case 'n':
        jogador = niceshot
    case 'g':
        jogador = golden

# URL da API

url_api = f"https://api.brawlstars.com/v1/players/%23{jogador}/battlelog"

# Cabeçalho de autorização com o token JWT
headers = {
    "Authorization": f"Bearer {token}"
}

# Solicitação HTTP GET para acessar a API
response = requests.get(url_api, headers=headers)


if response.status_code == 200:
    dia = datetime.date.today()
    dia_formatada = [dia.strftime("%d/%m/%Y")]
    # Processar a resposta JSON da API
    data = response.json()
    print(data)
    jogos = data['items']
    #print(jogos)
    #print(data['items'][0])
    batalhas = len(jogos)
    print(f'Total de batalhas: {batalhas}')
    for i in jogos:
        cont+=1
        for p in jogos[cont]:
            gmode = jogos[cont]['battle']['type']
            if gmode == 'friendly':              
                if p == 'event':

                    print('')
                    print('')
                    print('')
                    print(cont)
                    print('')
                    print(f'{p}:')
                    modo = [(jogos[cont][p]['mode'])]
                    mapa = [(jogos[cont][p]['map'])]
                    
                elif p == 'battle':
                    result = jogos[cont][p]['result']
                    dia_feito.append(dia_formatada)
                    print(f'Resultados: {jogos[cont][p]}')
                    try:
                        for t in range(2):
                            tag = []
                            playername = []
                            brawl = []
                            if t == 0:
                                
                                for n in range(3):
                                    tag = jogos[cont][p]['teams'][t][n]['tag']
                                    playername = jogos[cont][p]['teams'][t][n]['name']
                                    brawl = jogos[cont][p]['teams'][t][n]['brawler']['name']                              
                                    
                                    if tag != [] and playername != [] and brawl != []:
                                        tags1.append(tag)
                                        players1.append(playername)
                                        brawlPlayers1.append(brawl)                                        
                                        listaMapas.append(mapa)
                                        listaEventos.append(modo)
                                                                      
                                    if n == 2:
                                        tagsTime1.append(tags1)
                                        playersTime1.append(players1)
                                        brawlTime1.append(brawlPlayers1)
                                        tags1 = []
                                        players1 = []
                                        brawlPlayers1 = []

                            elif t == 1:
                                
                                for n in range(3):

                                    tag = jogos[cont][p]['teams'][t][n]['tag']
                                    playername = jogos[cont][p]['teams'][t][n]['name']
                                    brawl = jogos[cont][p]['teams'][t][n]['brawler']['name']

                                    if tag != [] and playername != [] and brawl != []:
                                        tags2.append(tag)
                                        players2.append(playername)
                                        brawlPlayers2.append(brawl)

                                    if n == 2:
                                        for a in range(3):
                                                result = jogos[cont][p]['result']                                  
                                                if a == 2:
                                                    result = [result]
                                                    resultTime2.append(result)
                                        tagsTime2.append(tags2)
                                        playersTime2.append(players2)
                                        brawlTime2.append(brawlPlayers2)
                                        tags2 = []
                                        players2 = []
                                        brawlPlayers2 = []
                    except IndexError:
                        confirm = 0
                        print('ERRO')

    if confirm == 1:
            for i in range(len(playersTime1)):
                linha = listaEventos[i] + listaMapas[i] + tagsTime2[i] + playersTime2[i] + brawlTime2[i] + resultTime2[i] + brawlTime1[i]  + playersTime1[i] + tagsTime1[i] + dia_feito[i]
                tabela.append(linha)
                i+=1
                index.append(i)
            if len(index) > 0:
                tabelaFinal = pd.DataFrame(data=tabela,columns=coluna1,index=index)
                print('')
                print(tabelaFinal)
                print('')
                nomeArquivo = 'teste'
                tabelaFinal.to_excel(f'{nomeArquivo}.xlsx')
            else:
                print('')
                print('Nenhuma partida amistosa encontrada')                   
    

else:
    print(f"Erro na solicitação: {response.status_code}")
    print(response.text)

                    
                                                                    

