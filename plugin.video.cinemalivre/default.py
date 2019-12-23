# -*- coding: UTF-8 -*-

import xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,sys,urllib,urllib2,re,base64,urlparse
from BeautifulSoup import BeautifulSoup

addon_id = 'plugin.video.cinemalivre'
addon_base = '[COLOR white]Cinema[COLOR red] Livre[/COLOR]'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
icon = addonfolder + '/icon.png'
fanart = addonfolder + '/fanart.jpg'
imagens = addonfolder+'/logos/'
base = 'http://cinemalivre.net/'
Todos = 'http://cinemalivre.net/todos_os_filmes_cont.php'
Generos = 'http://cinemalivre.net/todos_os_filmes.php'
Ranking = 'http://cinemalivre.net/ranking.php'
ORDEM = 'http://cinemalivre.net/ordem_alfabetica.php'
ARTISTA = 'http://cinemalivre.net/aartistas.php'
dialog=xbmcgui.Dialog()
Todos_Img = imagens+'TODOS OS FILMES.png'
Ranking_Img = imagens+'RANKING.png'
ORDEM_Img = imagens+'ORDEM ALFABetica.png'
ARTISTA_Img = imagens+'ARTISTAS.png'
Generos_Img = imagens+'GeNERO.png'

###################################################MENUS############################################
def Home():
	addDir('TODOS OS FILMES',Todos,1,Todos_Img)
	addDir('RANKING',Ranking,2,Ranking_Img)
	addDir('ORDEM ALFABÉTICA',ORDEM,4,ORDEM_Img)
	addDir('ARTISTAS',ARTISTA,5,ARTISTA_Img)
	addDir('GÊNERO',Generos,7,Generos_Img)


def ARTISTAS(url):
	link = abrir_url(url)
	r = '''<td class=".*"><a class=".*" href="(.*)">(.*)<.*a><.*>'''
	match = re.compile(r).findall(link)
	s = 1
	for a in match:
		name = a[1]
		url = base+a[0]
		addDir(name,url,6,ARTISTA_Img)
	
def Genero(url):
	link = abrir_url(url)
	r = '''<td class="left">\s*<a.*href="(.*)">\s*(.*)\s*<.*>\s*<.*>'''
	match = re.compile(r).findall(link)
	s = 1
	for a in match:
		name = a[1]
		url = base+a[0]
		if 'genero_' in url:
			addDir(name,url,8,Generos_Img)
	
def List_romances(url):
	link = abrir_url(url)
	r = '''<img src="(.*)".*width.*\s*.*\s*<a href="(.*)">\s*<.*>\s*(.*)\s*<.*>'''
	match = re.compile(r).findall(link)
	s = 1
	for a in match:
		name = a[2]
		url = base+a[1]
		img = base+a[0]
		if not name=='':
			addDir(name,url,3,img,False)
	
def List_ARTISTAS(url):
	link = abrir_url(url)
	r = '''<img src="(.*)".*width.*\s*.*\s*<a href="(.*)">\s*<.*>\s*(.*)\s*<.*>'''
	match = re.compile(r).findall(link)
	s = 1
	for a in match:
		name = a[2]
		url = base+a[1]
		img = base+a[0]
		addDir(name,url,3,img,False)
	
	
def ORDEM_ALFAB(url):
	link = abrir_url(url)
	r = '''<td class=".*">\s*<a class=".*" href="(.*)">\s*(.*)\s*<.*>\s*.*\s*.*\s*(.*)\s*<.*>'''
	match = re.compile(r).findall(link)
	s = 1
	for a in match:
		name = str(s)+'° '+a[1]+'  '+a[2]
		url = base+a[0]
		addDir(name,url,3,ORDEM_Img,False)
		s = s+1
		
def Todos_Rankig(url):
	link = abrir_url(url)
	r = '''<td class=".*".*>\s*(.*)\s*<.*>\s*<td class=".*">\s*<a class=".*" href="(.*)">\s*(.*)\s*<.*>\s*(.*)\s*<.*>\s*.*\s*(.*)\s*<.*>'''
	match = re.compile(r).findall(link)
	for a in match:
		name = a[0]+'   '+a[2]+' '+a[3]+'  '+a[4]
		url = base+a[1]
		addDir(name,url,3,Ranking_Img,False)

def Todos_Filmes(url):
	link = abrir_url(url)
	a =  BeautifulSoup(link,convertEntities=BeautifulSoup.HTML_ENTITIES)
	b = a.findAll('div',{'class':'galeria_item_painel_notas'})
	for i in b:
		name = i.text.encode('utf-8')
		url = base+i.a['href']
		img = base+i.img['src']
		addDir(name,url,3,img,False)

_url_re = re.compile("""
    http(s)?://(\w+\.)?youtube.com
    (?:
        (?:
            /(watch.+v=|embed/|v/)
            (?P<video_id>[0-9A-z_-]{11})
        )
        |
        (?:
            /(user|channel)/(?P<user>[^/?]+)
        )
    )
""", re.VERBOSE)

def Player_Filmes(url,name,iconimage):
	named = name
	link = abrir_url(url)
	if 'https://fast.wistia.com/embed/medias/' in link:
		c = re.compile('<script src="(.*?)" async><.*script>').findall(link)[0]
		b = c.replace('https://fast.wistia.com/embed/medias/','http://fast.wistia.net/embed/iframe/').replace('.jsonp','')
		a = abrir_url(b)
		if 'Video not found' in a:
			dialog.ok(addon_base,'Vídeo não encontrado','','')
			exit()
		abri = re.compile('"url":"(.*?)","').findall(a)[3]
		reproduzir  = abri
	elif 'player.vimeo.com' in link:
		b = re.compile('(?://|\.)(vimeo\.com)/(?:video/)?([0-9a-zA-Z]+)').findall(link)[0]
		a = abrir_url('https://player.vimeo.com/video/%s/config' % b[1])#.content#.result
		urls = []
		names = []
		match = re.compile('''{"profile":.*?,"width":.*?,"mime":"video.*?","fps":.*?,"url":"(.*?)","cdn":"akamai_interconnect","quality":"(.*?)","id":.*?,"origin":".*?","height":.*?}''').findall(a)
		for url,name in match:
			names.append(name)
			urls.append(url)	
		opcao = xbmcgui.Dialog().select('Lojink_resolver_vimeo', names)
		if opcao>= 0:
			reproduzir = urls[opcao]
		else:
			sys.exit(0)
	elif '//view.vzaar.com/' in link: 
		b = re.compile('src=".*view.vzaar.com/(.*)/player">').findall(link)[0]
		a = abrir_url('http://view.vzaar.com/v2/%s/video'% b)
		reproduzir = re.compile('"sourceUrl":"(.*?)"}').findall(a)[0]
	elif 'www.youtube.com' in link:
		a = re.compile('<iframe.*width.*height.*src="(.*?)".*llowfullscreen>').findall(link)[0]
		xbmc.log(_url_re.match(a).group("video_id"))
		reproduzir = 'plugin://plugin.video.youtube/play/?video_id=%s' % _url_re.match(a).group("video_id")
	
	listItem = xbmcgui.ListItem(named, thumbnailImage=iconimage)
	xbmc.Player().play(item=reproduzir, listitem=listItem)			
	sys.exit()	

############################################FUNÇÕES####################################################

def addDir(name,url,mode,iconimage,pasta=True,total=1):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+ "&iconimage=" + urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok

def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link
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
        Home()
		
elif mode==1:
	Todos_Filmes(url)
	
elif mode==2:
	Todos_Rankig(url)
	
elif mode==3:
	Player_Filmes(url,name,iconimage)
	
		
elif mode==4:
	ORDEM_ALFAB(url)
		
elif mode==5:
	ARTISTAS(url)
	
			
elif mode==6:
	List_ARTISTAS(url)
				
elif mode==7:
	Genero(url)
				
elif mode==8:
	List_romances(url)
	
	
	
	
xbmcplugin.endOfDirectory(int(sys.argv[1]))