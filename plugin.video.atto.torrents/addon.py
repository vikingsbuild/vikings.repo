# -*- coding: UTF-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
import sys
from BeautifulSoup import BeautifulSoup


addon_base = '[COLOR lime]Atto Torrents[/COLOR]'
addon_id = 'plugin.video.atto.torrents'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.jpg'
icones = addonfolder + '/icon.png'
base = 'http://www.megatorrentshd.com'
dialog = xbmcgui.Dialog()    
def CATEGORIES():
	addDir('[COLOR lime]LANÇAMENTOS[/COLOR]','http://www.megatorrentshd.com/category/lancamentos',2,artfolder + 'lancamentos.png')
	addDir('[COLOR lime]DESTAQUES[/COLOR]','http://www.megatorrentshd.com/destaque/',2,artfolder + 'Destaques.png')
	addDir('[COLOR lime]CATEGORIAS[/COLOR]','http://www.megatorrentshd.com/',4,artfolder + 'Categorias.png')
	addDir('[COLOR lime]SÉRIES[/COLOR]','http://www.megatorrentshd.com/series/',2,artfolder + 'series.png')
	addDir('[COLOR lime]PESQUISA[/COLOR]','-',5,artfolder + 'PESQUISA.png')	
	
def listar_paginas():
	link = abrir_url('http://www.megatorrentshd.com/lancamentos/')
	items_url = []
	items_name = []
	pagi = re.compile('<a class="last" href="http://www.megatorrentshd.com/lancamentos/page/(.*)/">.*</a>').findall(link)[0]
	co = int(pagi)
	for a in range(1,co+1):
		items_name.append('PÁGINA: %s' % a)		
		items_url.append('http://www.megatorrentshd.com/lancamentos/page/'+str(a)+'/')			
	opcao = xbmcgui.Dialog().select('-= Atto Torrents =-', items_name)
	if opcao>= 0:
		pass		
def categorias(url):
	link = abrir_url(url)
	soup = BeautifulSoup(link,convertEntities=BeautifulSoup.HTML_ENTITIES)
	match = soup.find('ul',{'class':"sub-menu"}).findAll('li')
	for a in match:
		name = a.text.encode('utf-8')
		url = a.a['href']
		if url.startswith('http'):
			url = url
		else:
			url = base+url
		addDir(name,url,2,icones)
		
		
		
def items_Beaulti(item,arquivo=False):
	for items in item:
		if not arquivo:
			return items
		else:
			return items.text.encode('utf-8')	
def listar_filmes(url):#title
	link  = abrir_url(url)
	html = link
	bsObj = BeautifulSoup(html)
	nameList = bsObj.findAll('div',attrs={"class": 'ItemN'})
	for items in nameList:#
		idiomas = items.findAll('span',attrs={'class':'idi'})[0]
		idioma = idiomas.text.encode('utf-8')		
		qualitys = items_Beaulti(items.findAll('span',attrs={'class':'quality'}),True)
		quality = qualitys
		filmes = items.findAll("div", {"class":"peli"})[0]
		name = filmes.img['alt'].encode('utf-8')
		img = filmes.img['src']
		url = filmes.a['href']
		name = name.split('– HD')[0].split(') HD')[0].split(' – BluRay')[0].split(' – WEB-DL')[0]
		name = name.replace('   ',' ').replace(' Completa ',' ').replace('   ',' ').replace('   ',' ')
		addDir('%s - %s - %s' % (name,idioma,quality),url.encode('utf-8'),99,img.encode('utf-8'))
		
	nameList = bsObj.findAll('div',attrs={"class": 'wp-pagenavi'})
	pag = len(nameList)
	for items in nameList:#
		pagina_name = items_Beaulti(items.find("span", { "class" : "pages" }))
		pagina_url = items.findAll(attrs={ "class" : "nextpostslink" })[0].get('href')
		addDir('[COLOR lime]'+pagina_name.encode('utf-8')+'[/COLOR]',pagina_url.encode('utf-8'),2,artfolder + 'Proxima.png',True)
	if pag==0:
		page = re.compile('<link rel="next" href="(.*)" />').findall(link)
		for a in page:
			addDir('[COLOR lime]Proxima Página[/COLOR]',a,2,artfolder + 'Proxima.png',True)
			
			
			
def pesquisa():
	keyb = xbmc.Keyboard('', 'Encontre filmes, atores e diretores')
	keyb.doModal()
	if (keyb.isConfirmed()):
		search = keyb.getText()
		parametro_pesquisa=urllib.quote(search)
		url = 'http://www.megatorrentshd.com/?s='+parametro_pesquisa
		listar_filmes(url)
	else:
		sys.exit()
	
	
def Listar_epiEfil(url,name,iconimage):
	link  = abrir_url(url)
	addDir('[COLOR lime]Sinopse:%s[/COLOR]'%name.split('(')[0],url,20,iconimage,False)
	bsObj = BeautifulSoup(link)
	nameList = bsObj.findAll(attrs={"class":"trailer litebox"})
	for filmes in nameList:#
		Trailer =  filmes.get('href')	
		addDir('[COLOR lime]Play Trailer[/COLOR]',Trailer,999,iconimage)
	match = bsObj.find('div',{'id':'categoria','class':'box_item center-widget'})
	matchs = match.findAll('div')
	for a in matchs:#('a'):
		name = a.text.encode('utf-8')
		try:
			url = a.a['href'].encode('utf-8')
		except:
			url= 'True'
		if name=='':
			xbmc.log('%s' % a)
			nomi = url.split('&dn=')[-1].split('&tr=')[0]
			name = urllib.unquote_plus(urllib.unquote_plus(nomi.split('[')[-0]))
		addDir(name,url,98,iconimage,True)
	
def Play_Trailer(url,name,iconimage):
	link  = abrir_url(url)
	bsObj = BeautifulSoup(link)
	nameList = bsObj.findAll(attrs={"class":"trailer litebox"})
	for filmes in nameList:#
		Trailer =  filmes.get('href')	
		Trailers(Trailer,name,iconimage)
def Descricao(url):
	html  = abrir_url(url)
	bsObj = BeautifulSoup(html,convertEntities=BeautifulSoup.HTML_ENTITIES)
	#nameList = bsObj.findAll("a", {"class":"trailer litebox"})
	nameList = bsObj.findAll(attrs={"class": 'meta_datos'})
	for filmes in nameList:#
		print(filmes)#
		names = filmes.h1.text
		imdb = filmes.find('div',{'class':'views'})
		imdbs = imdb.text.encode('utf-8').replace('|','\nVotos: ').replace('/ 10','').replace('votos','')
		description = bsObj.find(attrs={"class": 'meta_datos'}).findAll('p')
		descriptions = description[1].text.split('|')[-1]
		showText(addon_base,'Sinopse: %s'% names+'\n\n'+imdbs+'\n\n'+descriptions)

		
def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return 
        except:
            pass	

				
def Player_torrent(url,name,iconimage):
	if 'magnet:?xt' in url or '.torrent' in url:	#'xt=urn:btih:([^&/]+) plugin://plugin.video.elementum/play?uri=%s
		Players_Torrent = ['Quasar','Pulsar','Yatp','Torrenter','XbmcTorrent','Torrentin','Elementum','Ace Stream(APK)','BitX Torrent Video Player(APK)']
		if selfAddon.getSetting('player_torrent') == Players_Torrent[0]:#"Quasar":
			url = 'plugin://plugin.video.quasar/play?uri={0}'.format(urllib.quote_plus(url))
		elif selfAddon.getSetting('player_torrent') == Players_Torrent[1]:# "Pulsar":
			url = 'plugin://plugin.video.pulsar/play?uri={0}'.format(urllib.quote_plus(url))
		elif selfAddon.getSetting('player_torrent') == Players_Torrent[2]:#"Yatp":
			url = 'plugin://plugin.video.yatp/?action=play&torrent={0}'.format(urllib.quote_plus(url))
		elif selfAddon.getSetting('player_torrent') ==  Players_Torrent[3]:##"Torrenter":
			url = 'plugin://plugin.video.torrenter/?action=playSTRM&url={0}'.format(urllib.quote_plus(url))
		elif selfAddon.getSetting('player_torrent') ==  Players_Torrent[4]:# "XbmcTorrent":
			url = 'plugin://plugin.video.xbmctorrent/play/{0}'.format(urllib.quote_plus(url))
		elif selfAddon.getSetting('player_torrent') ==  Players_Torrent[5]:#"Torrentin":
			url = 'plugin://plugin.video.torrentin/?uri={0}'.format(urllib.quote_plus(url))
		elif selfAddon.getSetting('player_torrent') ==   Players_Torrent[6]:#"Elementum":
			url = 'plugin://plugin.video.elementum/play?uri={0}'.format(urllib.quote_plus(url))
		elif selfAddon.getSetting('player_torrent') ==   Players_Torrent[7]:##"Ace Stream (apk)":
			if xbmc.getCondVisibility('system.platform.android'):
				xbmc.executebuiltin('XBMC.StartAndroidActivity("org.acestream.media","android.intent.action.VIEW","","'+url+'")')
			else:
				dialog.ok(addon_base,  "FUNCIONA APENAS EM SISTEMAS ANDROID !!".decode('unicode_escape'),'')
				sys.exit(0)	
		elif selfAddon.getSetting('player_torrent') ==   Players_Torrent[8]:##"BitX Torrent Video Player":
			if xbmc.getCondVisibility('system.platform.android'):
				xbmc.executebuiltin('XBMC.StartAndroidActivity("tv.bitx.media","android.intent.action.VIEW","","'+url+'")')
			else:
				dialog.ok(addon_base,  "FUNCIONA APENAS EM SISTEMAS ANDROID !!".decode('unicode_escape'),'')
				sys.exit(0)	
				
				
	listItem = xbmcgui.ListItem(name, thumbnailImage=iconimage)
	xbmc.Player().play(item=url, listitem=listItem)			
	sys.exit()	
	
def Trailers(url,name,iconimage):
	import yt
	try:
		link = yt.Scrape(url)
		listItem = xbmcgui.ListItem(name, thumbnailImage=iconimage)
		xbmc.Player().play(item=link, listitem=listItem)			
		sys.exit()	
	except TypeError:
		dialog.ok(addon_base,'Desculpe, não foi possivel reproduzir o video.','','')
############################################################################################################
#                                           FUNÇOES FEITAS                                                 #
############################################################################################################		
		
def abrir_url(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		return link
	except IOError:#     except urllib2.HTTPError, e:
		dialog.notification(addon_base,'Não foi possivel acessar o servidor.',icones)
		sys.exit(0)

		
def addDir(name,url,mode,iconimage,pasta=True,total=1,plot=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	cmItems = []
	if mode==99:
		cmItems.append(('[COLOR lime]Ver Sinopse[/COLOR]', 'XBMC.RunPlugin(%s?url=%s&mode=20&name=%s&iconimage=%s)'%(sys.argv[0], url,name,iconimage)))	
		cmItems.append(('[COLOR lime]Play Trailer[/COLOR]', 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s&iconimage=%s)'%(sys.argv[0], url,name,iconimage)))	
	liz.addContextMenuItems(cmItems, replaceItems=False)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="video", infoLabels={ "title": name, "plot": plot } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok
	
############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################           
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
url=None
name=None
mode=None
iconimage=None
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

try:        
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################
if mode==None or url==None or len(url)<1:
        CATEGORIES()

elif mode==2: listar_filmes(url)
elif mode==6: listar_pesquisa(url)
elif mode==3: listar_series(url)
elif mode==4: categorias(url)
elif mode==5: pesquisa()

elif mode==20: Descricao(url)
elif mode==21: Play_Trailer(url,name,iconimage)
elif mode==99: Listar_epiEfil(url,name,iconimage)
elif mode==98: Player_torrent(url,name,iconimage)
elif mode==999: Trailers(url,name,iconimage)

#########################################          FIM
xbmcplugin.endOfDirectory(int(sys.argv[1]))