import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep

#Alguns anos não trarão dados completos por ter uma formatação diferente

lista_anos_copa = [1930,1934,1938,1950,1954,1962,1966,1970,1974,1978,1982,1986,1990,1994,1998,2002,2006,2010,2014,2018,2022]
todos_dfs = []

def jogos_copa(ano):
    """Devolve todos os resultados da copa do ano desejado."""
    url = f'https://en.wikipedia.org/wiki/{ano}_FIFA_World_Cup'

    request = requests.get(url)

    soup = BeautifulSoup(request.text,'html.parser')

    partidas = soup.find_all('div', class_='footballbox')

    time_casa = []
    placar = []
    time_fora = []
    Ano = []

    for partida in partidas:
        time_casa.append(partida.find('th','fhome').get_text())
        placar.append(partida.find('th','fscore').get_text())
        time_fora.append(partida.find('th','faway').get_text())
        Ano.append(ano)

    dict_partidas = {"Casa":time_casa, "Placar":placar, "Fora":time_fora, "Ano":Ano}

    df = pd.DataFrame(dict_partidas)
    return df

for ano in lista_anos_copa:

    df = jogos_copa(ano)
    todos_dfs.append(df)
    sleep(1)

df_todas_copas = pd.concat(todos_dfs, ignore_index=True)

df_todas_copas.to_excel("resultados_copa.xlsx", index=False)
