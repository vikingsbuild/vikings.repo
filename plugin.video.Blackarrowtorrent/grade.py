import requests
import sys
from bs4 import BeautifulSoup

def grade(canal):
    pagina_de_busca = requests.get('https://meuguia.tv/programacao/canal/'+canal+'')
    

    soup = BeautifulSoup(pagina_de_busca.text, "html.parser")

    titulo = soup.find_all('div', attrs={'class': 'prog_comp_tit'})
    hora   = soup.find_all('div', attrs={'class': 'prog_comp_data'})
    w=i = j = 0
    grade ={}
    prog  = {}

    for item in hora:
        i = i + 1
        conv =str(item)
        tam = len(conv)
        grade[i] = conv[28:tam-6]
        #print(strg)

    for item2 in titulo:
        j = j + 1
        conv2 =str(item2)
        tam2 = len(conv2)
        prog[j] = conv2[26:tam2-6]
       # print(grade[j],prog)


        
    while w < 1:
        w = w+ 1
        #print(grade[w], grade[w+1],prog[w])
        #addDir(prog[w],'100',100,icon,FANART,'','','','')
        return prog[w]


print(grade("GSP"))
