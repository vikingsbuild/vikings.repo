# -*- coding: utf-8 -*-
import urllib
import urllib2
import datetime
import re
import os
import base64
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import cookielib
import sys
import xbmc
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP

try:
    import json
except:
    import simplejson as json
	
try:
    import jsunpack
except:
    pass
	
import SimpleDownloader as downloader
from HTMLParser import HTMLParser
h = HTMLParser()

addon = xbmcaddon.Addon(id='plugin.video.Blackarrowtorrent')
addon_version = addon.getAddonInfo('version')
profile = xbmc.translatePath(addon.getAddonInfo('profile').decode('utf-8'))
home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
plugin = addon.getSetting('plugin')
icon = os.path.join(home, 'icon.png')
FANART = os.path.join(home, 'fanart.jpg')
Site = xbmc.translatePath(os.path.join(home, 'Site.txt'))
dialog=xbmcgui.Dialog()

def abrir_url(url, headers=None):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		if headers:
			for h,hv in headers:
				req.add_header(h,hv)
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		return link
	except IOError as e:#     except urllib2.HTTPError, e:
		dialog.notification('','Não foi possivel acessar o servidor.',icon)
		sys.exit(0)

def Soups(url):
	link = abrir_url(url)
	return BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)		
	
	
def assistindoanime(url):	
	uri = Soups(url)
	try:
		img = uri('meta',{'property':'og:image'})[0]['content']
	except:
		img = icon
	try:
		descriptio = uri('p',{'id':'sinopse2'})[0].text.encode('utf-8')
	except:
		descriptio = ''
	r = uri.find('div',{'id':'episAnime'}).findAll('a')
	total = len(r)
	for a in r:
		name = a.span.text.encode('utf-8')
		url = a.get('href')
		icone = img
		add_link(name, url, 200, icone, fanart,descriptio)

	
def netcine(url):
	temporada = name.replace(' Temporada ','')
	link = abrir_url(url)
	soup = BeautifulSoup(link)
	try:
		img = soup('div',{'class':'imgs tsll'})[0].img['src']
	except:
		img = icon
	if 'Temporada' in name:
			reg = re.compile('<li>\s*<a href="(.*?)" target="_blank">\s*<span class="datex">(.*?)</span>\s*<span class="datix"><b class="icon-chevron-right"></b>\s*(.*?)\s*</span>').findall(link)
			for url,epi,epi_name in reg:	
				lists = epi.split(' - ')[0]
				if temporada in lists:	
					add_link(epi_name, url, 200, img, fanart,temporada)
	else:
		rew1 = re.compile('<span><b class="icon-bars"></b>(.*?)</span>').findall(link)
		for temp in rew1:
			add_link(temp,url,999, img, fanart,temp)

def week_series(url):
	temporada = name
	link = abrir_url(url)
	soup = BeautifulSoup(link)
	try:
		img = soup('meta',{'property':'og:image'})[0]['content']
	except:
		img = icon
	if 'ª temporada' in temporada:
		for b in re.compile('<div class="col.*?">.*?&#8211;(.*?)<br .>(.*?<.*?><.div>)').findall(description):
			add_link(name+'  '+ b[0].title(),url,30003, img, fanart,'')
			for uri,nami in re.compile('<a.*?href="(.*?)".*?target="_blank">(.*?)</a>').findall(b[1]):
				nami = nami.replace('&#8211;','-')
				uri = uri.replace('#038;','')
				add_link(nami,uri,200, img, fanart,'')
	else:
		fas = link.replace('\t','')		
		fa = fas.replace('\n','')		
		match =re.compile('<div class=".*?" id="(.*?)">(.*?</div></div>)').findall(fa)
		for a in match:
			temp = a[0].replace('temp','')+'ª temporada'
			if 'target="_blank">' in a[1]:
				add_link(temp,url,999, img, fanart,a[1])

					
def mmfilmes(url):
	referer = [('Referer','http://www.mmfilmes.tv/')]
	link = abrir_url(url)#, headers=referer)
	soup = BeautifulSoup(link)
	try:
		img = soup('div',{'class':'c_capa'})[0].img['src']
	except:
		try:
			img = iconimage
		except:
			img = icon
	if not '/embed/' in url:
		rew = re.compile('=(http.*?)&..=(.*?)&').findall(link)
		for url,name in rew:
			add_link(name,url,999, img, fanart,name)
	else:
		if '° Temporada' in description:
			name = description.replace('° Temporada','')
			base_mmf = 'http://player.mmfilmes.tv'
			tempo = int(name)
			referer = [('Referer','http://www.mmfilmes.tv/')]
			linkTV  = abrir_url(url, headers=referer)		
			linkTV = linkTV.replace("$('#player').css('display','none');","").replace("$('#Svplayer').css('display','block');","").replace('\t','').replace('\n','')
			try:
				match = re.compile('if.s == '+str(tempo)+'.{(.*)}\s*if.s == '+str(tempo+1)+'.{').findall(linkTV)
				matchsd = match[0].replace("$('#player').css('display','none');","").replace("$('#Svplayer').css('display','block');","").replace('\t','').replace('\n','')
			except:
				match =linkTV.split('if(s == '+str(tempo)+'){')[1]
				matchsd = match
			arquivos =[]
			a = re.compile("if.t == '(.*?)'.{(.*?);}}").findall(matchsd)
			for idioma,conteudo in a:
					matchs = re.compile("if.e == (.*?).{.*?addiframe.'(.*?)'.").findall(conteudo)
					for name,url in matchs:
						nome = 'Episódio %s - %s'% (name,idioma.replace('leg','Legendado').replace('dub','Dublado'))
						uri = url if url.startswith('http') else 'http://player.mmfilmes.tv/'+url		
						arquivos.append([nome,uri])
						arquivos.sort(key=lambda arquivos: int(re.compile('dio (.*?) -').findall(arquivos[0])[0]))
			for a,b in arquivos:
				if 'drive.google' in b:
					b = 'Other://plugin://plugin.video.gdrive?mode=streamURL&amp;url='+b.replace('/preview','/view')
				add_link(a,b,200, img, fanart,'episodios')
		else:
			referer = [('Referer','http://www.mmfilmes.tv/')]
			linkTV  = abrir_url(url, headers=referer)		
			match  = re.compile('if.s == (.*?).{').findall(linkTV)
			for a in match:
				temp = a+'° Temporada'
				add_link(temp,url,999, img, fanart,temp)
def megatorrentshd(url):
	link = abrir_url(url)
	soup = BeautifulSoup(link)
	rew = soup('div',{'class':"peli"})
	for a in rew:
		name  =  a.img['alt'].encode('utf-8')
		url   =  a.a['href'].encode('utf-8')
		img   =  a.img['src'].encode('utf-8')
		add_link(name,url,200, img, fanart,'[]')
	nameList = soup.findAll('div',attrs={"class": 'wp-pagenavi'})
	pag = len(nameList)
	for items in nameList:#
		#pagina_name = items_Beaulti(items.find("span", { "class" : "pages" }))
		pagina_url = items.findAll(attrs={ "class" : "nextpostslink" })[0].get('href')
		add_link('[COLOR green]Proxima Página[/COLOR]',pagina_url,999, icon, fanart,'[]')
	if pag==0:
		page = re.compile('<link rel="next" href="(.*)" />').findall(link)
		for a in page:
			#addDir('[COLOR green]Proxima Página[/COLOR]',a,2,artfolder + 'Proxima.png',True)
			add_link('[COLOR green]Proxima Página[/COLOR]',a,999, icon, fanart,'[]')
		
def Check_update():
	versao='6.0'
	Source_Update = os.path.join(home, 'Site_Kratos.py')
	base_update = abrir_url('https://raw.githubusercontent.com/brunolojino/listas/master/Site_Kratos.py')
	check = re.compile("versao='(.*?)'").findall(base_update)[0]
	if versao==check:
		pass
	else:
		f = open(Source_Update, 'wb')
		f.write(base_update)
		f.close()
		dialog.ok('-=BlackArrow kodi PT =-','Versão do Web Scraper: '+versao,'Versão do Web Scraper disponível: '+check,'Atualizando o Web Scraper do add-on feche e abra novamente.')
		sys.exit(0) 

Sites_kratos = ['www.assistindoanime.com','netcine.us/','week-series.com','mmfilmes.tv','megatorrentshd']	
def Capturar_sites(url,name,iconimage,description):   	
	Check_update()
	rURL = url.replace(';','')
	if Sites_kratos[0] in rURL:
		link = rURL
		assistindoanime(link)			
	elif Sites_kratos[1] in rURL:
		link = rURL
		netcine(link)
	elif Sites_kratos[2] in rURL:
		link = rURL
		week_series(link)
	elif Sites_kratos[3] in url:
		link = rURL
		mmfilmes(link)
	elif Sites_kratos[4] in rURL:
		megatorrentshd(rURL)
def add_link(name, url, mode, iconimage, fanart,description):
	u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name, "Plot": description} )
	cmItems = []
#	if mode==3 or mode==6:
#		cmItems.append(('[COLOR red]Ver Sinopse[/COLOR]', 'XBMC.RunPlugin(%s?url=%s&mode=9&name=%s&iconimage=%s)'%(sys.argv[0], url,name,iconimage)))	
#		cmItems.append(('[COLOR red]Play Trailer[/COLOR]', 'XBMC.RunPlugin(%s?url=%s&mode=10&name=%s&iconimage=%s)'%(sys.argv[0], url,name,iconimage)))	
	if not '<a href=' in description and not 'addiframe' in description:
		cmItems.append(('Movie Information', 'XBMC.Action(Info)'))
	liz.addContextMenuItems(cmItems, replaceItems=False)
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true') 
	if mode==200:
		ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = False) 
	else:
		ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True) 
	return ok	
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
            params=sys.argv[2]
            cleanedparams=params.replace('?','')
            if (params[len(params)-1]=='/'):
                params=params[0:len(params)-2]
            pairsofparams=cleanedparams.split('&')
            param={}
            for i in range(len(pairsofparams)):
                splitparams={}
                splitparams=pairsofparams[i].split('=')
                if (len(splitparams))==2:
                    param[splitparams[0]]=splitparams[1]
        return param
		
params=get_params()
xbmc.log('%s' % params)
url=None
name=None
mode=None
playlist=None
iconimage=None
fanart=FANART
playlist=None
description=None
fav_mode=None
regexs=None

try:
    url=urllib.unquote_plus(params["url"]).decode('utf-8')
except:
    pass
try:
    name=urllib.unquote_plus(params["name"])
except:
    pass
try:
    iconimage=urllib.unquote_plus(params["iconimage"])
except:
    pass
try:
    fanart=urllib.unquote_plus(params["fanart"])
except:
    pass
try:
    mode=int(params["mode"])
except:
    pass
try:
    playlist=eval(urllib.unquote_plus(params["playlist"]).replace('||',','))
except:
    pass
try:
    fav_mode=int(params["fav_mode"])
except:
    pass
try:
    regexs=params["regexs"]
except:
    pass
try:
    description=urllib.unquote_plus(params["description"])
except:
    pass
