import requests         # pip install requests
from pandas import DataFrame , read_excel   # pip install pandas
import numpy as np      # pip install numpy
from openpyxl import Workbook , load_workbook
from _verificar import verificar_bot , tags_tabela, Salvar, formatarDocumento # arquivo separado necessario
import datetime

def dados_treino(response):
    coluna1 = ['Modo','Mapa','Tag 1','Tag 2','Tag 3','Player 1','Player 2','Player 3','Brawler 1','Brawler 2','Brawler 3','Resultado','Brawler 4','Brawler 5','Brawler 6','Player 4','Player 5','Player 6','Tag 4','Tag 5','Tag 6','Data']
    confirm = 1
    dia_feito = []
    listaEventos = []
    listaMapas = []
    resultTime = []
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
    contIndex = 0
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
                if gmode == 'friendly' or gmode == 'tournament':   
                    try:           

                        if p == 'event':
                            print('')
                            print('')
                            print('')
                            print(cont)
                            print('')
                            print(f'{p}:')
                            modo = [(jogos[cont][p]['mode'])]
                            mapa = [(jogos[cont][p]['map'])]
                            listaMapas.append(mapa)
                            listaEventos.append(modo)
                            
                        elif p == 'battle':
                            #print(jogos[cont][p]['teams'])
                            if len(jogos[cont][p]['teams'][0]) == 3 and len(jogos[cont][p]['teams'][1]) == 3:
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
                                                tags1.append(tag)
                                                players1.append(playername)
                                                brawlPlayers1.append(brawl)                                        
                                                    
                                                                                
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
                                                tags2.append(tag)
                                                players2.append(playername)
                                                brawlPlayers2.append(brawl)

                                                if n == 2:
                                                    for a in range(3):
                                                            result = jogos[cont][p]['result']                                  
                                                            if a == 2:
                                                                result = [result]
                                                                resultTime.append(result)
                                                    tagsTime2.append(tags2)
                                                    playersTime2.append(players2)
                                                    brawlTime2.append(brawlPlayers2)
                                                    tags2 = []
                                                    players2 = []
                                                    brawlPlayers2 = []
                                except IndexError:
                                    
                                    confirm = 0
                                    print()
                                    print('ERRO')
                                
                    except KeyError:
                        print('Partida rejeitada')
        if confirm == 1:
                for i in range(len(playersTime1)):
                    if not 'Bot' in playersTime1[i] and not 'Bot' in playersTime2[i]:
                        linha = listaEventos[i] + listaMapas[i] + tagsTime1[i] + playersTime1[i] + brawlTime1[i] + resultTime[i] + brawlTime2[i]  + playersTime2[i] + tagsTime2[i] + dia_feito[i]
                        verify = verificar_bot(linha)
                        if not verify:
                            tabela.append(linha)
                            contIndex+=1
                            index.append(contIndex)
                if len(index) > 0:
                    tabelaFinal = DataFrame(data=tabela,columns=coluna1,index=index)
                    print('')
                    print(tabelaFinal)
                    print('')
                    nomeArquivo = 'teste'
                    Salvar(tabelaFinal,nomeArquivo)
                    formatarDocumento(nomeArquivo)
                else:
                    print('')
                    print('Nenhuma partida amistosa encontrada')  
                    confirm = 0                      
    else:
        print(f"Erro na solicitação: {response.status_code}")
        print(response.text)
