import requests
import xbmc

from bs4 import BeautifulSoup
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

def pegarfontes(link):
     
    pagina_de_busca = requests.get(''+link+'')
    soup = BeautifulSoup(pagina_de_busca.text, "html.parser")
    player = os.path.join(xbmc.translatePath("special://home/addons/plugin.video.Blackarrowtorrent/player.xml").decode("utf-8"))

    for item in soup.find_all('div', attrs={'style': 'padding: 10px;text-align: center;font-size: 16px;'}): 
        item2 = str(item)
        files = item2.replace('<div style="padding: 10px;text-align: center;font-size: 16px;"><b><a href="','\n<item><link>').replace('" style="color: #fff;" target="_blank">','</link><title>').replace('</a></b></div>','</title>\n<thumbnail>https://archive.org/download/icon_FN/icon_FN.png</thumbnail></item>'))

        f = open(''+player+'', 'w')
        f.write(''+files+'')
