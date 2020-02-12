# -*- coding: utf-8 -*-
# EXPLORA ADDON POR NETAI. SEPTIEMBRE 2017
import urllib, urllib2, sys, re, os, unicodedata
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
import cookielib,base64

#Declaramos las variables a Kodi.

addon = xbmcaddon.Addon('plugin.video.Explora')
addon_version = addon.getAddonInfo('version')
plugin_handle = int(sys.argv[1])
mysettings = xbmcaddon.Addon(id = 'plugin.video.Explora')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
buscar = xbmc.translatePath(os.path.join(home, 'buscar.png'))
adultos18 = xbmc.translatePath(os.path.join(home, 'atencion.png'))
animales= xbmc.translatePath(os.path.join(home, 'animales.png'))
celebridades = xbmc.translatePath(os.path.join(home, 'celebridades.png'))
ciencia = xbmc.translatePath(os.path.join(home, 'ciencia.png'))
ciudades = xbmc.translatePath(os.path.join(home, 'ciudades.png'))
comosehace = xbmc.translatePath(os.path.join(home, 'comosehace.png'))
conspiraciones = xbmc.translatePath(os.path.join(home, 'conspiraciones.png'))
curiosidades = xbmc.translatePath(os.path.join(home, 'curiosidades.png'))
deportes = xbmc.translatePath(os.path.join(home, 'deportes.png'))
desclasificados = xbmc.translatePath(os.path.join(home, 'desclasificados.png'))
egipto = xbmc.translatePath(os.path.join(home, 'egipto.png'))
extraterrestres = xbmc.translatePath(os.path.join(home, 'extraterrestres.png'))
fenomenos = xbmc.translatePath(os.path.join(home, 'fenomenos.png'))
guerra = xbmc.translatePath(os.path.join(home, 'guerra.png'))
historia = xbmc.translatePath(os.path.join(home, 'historia.png'))
informatica = xbmc.translatePath(os.path.join(home, 'informatica.png'))
musica = xbmc.translatePath(os.path.join(home, 'musica.png'))
pesca = xbmc.translatePath(os.path.join(home, 'pesca.png'))
religion = xbmc.translatePath(os.path.join(home, 'religion.png'))
universo = xbmc.translatePath(os.path.join(home, 'universo.png'))
adultos = xbmc.translatePath(os.path.join(home, 'adultos.png'))
espacio = xbmc.translatePath(os.path.join(home, 'espacio.png'))
narcos = xbmc.translatePath(os.path.join(home, 'narcos.png'))
segunda_guerra_mundial = xbmc.translatePath(os.path.join(home, 'segunda_guerra_mundial.png'))
roma = xbmc.translatePath(os.path.join(home, 'roma.png'))
#db = base64.b64decode('aHR0cDovL3d3dy5ncnVwby1uZXRhaS5vcmcvZXhwbG9yYS9iZC5tM3U=')
db="https://raw.githubusercontent.com/Andorth/Explora/master/categorias/bd.m3u"

########################################################################################################################
#
#
# Listamos las categorias y la ruta donde se encuentras las listas M3U :
#
#
########################################################################################################################


#Nuestras listas M3U donde estan nuestros videos o peliculas.
categoria = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/animales.m3u" #Animales
categoria2 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/personajes.m3u" #personajes
categoria3 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/ciencia.m3u" #Ciencia
categoria4 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/ciudades.m3u" #Ciudades
categoria5 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/comosehacen.m3u" #Como se hace
categoria6 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/conspiraciones.m3u" #conspiraciones
categoria7 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/curiosidades.m3u" #curiosidades
categoria8 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/deportes.m3u" #deportes
categoria9 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/desclasificados.m3u" #desclasificados
categoria10 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/egipto.m3u" #egipto
categoria11 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/extraterrestres.m3u" #extraterrestres
categoria12 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/fenomenos.m3u" #fenomenos
categoria13 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/guerra.m3u" #guerra
categoria14 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/historia.m3u" #historia
categoria15 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/informatica.m3u" #informatica
categoria16 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/musica.m3u" #musica
categoria17 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/pesca.m3u" #pesca
categoria18 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/religion.m3u" #religion
categoria19 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/universo.m3u" #universo
categoria20 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/adultos.m3u" #adultos
categoria21 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/narcos.m3u" #Narcos
categoria22 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/segunda_guerra_mundial.m3u" #segnda guerra mundial
categoria23 = "https://raw.githubusercontent.com/Andorth/Explora/master/categorias/roma.m3u" #roma



##REGEX - Esto mejor no lo toques. Sino phyton se pone tonto.
regex = 'name=(.+?)url=(.+)logo=(.+?)'
m3u_thumb_regex = 'tvg-logo=[\'"](.*?)[\'"]'
m3u_regex = '#(.+?),(.+)\s*(.+)\s*'

## Esto es para crear los menu y que no den las lata.
u_tube = 'http://www.youtube.com'

def removeAccents(s):
## Nos cargamos los acentos, phyton no los usa ni los reconoce. 
	return ''.join((c for c in unicodedata.normalize('NFD', s.decode('utf-8')) if unicodedata.category(c) != 'Mn'))
					
def read_file(file):
## FUNCION QUE LEE LOS FICHEROS:
    try:
        f = open(file, 'r')
        content = f.read()
        f.close()
        return content
    except:
        pass

def make_request(url):
##ESTA FUNCION lee las url declaradas donde estan los videos. || Aun no he conseguido modificar el script para que genere |token| tipico en cualquier pagina de video.
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
		response = urllib2.urlopen(req)	  
		link = response.read()
		response.close()  
		return link
	except urllib2.URLError, e:
		print 'We failed to open "%s".' % url
		if hasattr(e, 'code'):
			print 'We failed with error code - %s.' % e.code	
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason
			
def main():

##	MENUS.

	add_link_info('[B][COLOR gold] |EXPLORA| - DOCUMENTALES EN CASTELLANO. [/COLOR][/B]',icon, fanart)
	add_link_info('[B][COLOR red] [B]|EXPLORA| Algunos contenidos pueden no ser recomendados para menores de edad. No deje que un menor utilice este addon sin vigilancia. [/COLOR][/B]',adultos18, fanart)
	add_dir('[COLOR yellow][B]+Buscar[/B][/COLOR]', 'searchlink', 98, buscar, fanart)
	add_dir('[COLOR yellow][B]+Animales[/B][/COLOR]', u_tube, 2, animales, fanart)
	add_dir('[COLOR yellow][B]+Personajes[/B][/COLOR]', u_tube, 3, celebridades, fanart)
	add_dir('[COLOR yellow][B]+Ciencia[/B][/COLOR]', u_tube, 4, ciencia, fanart)
	add_dir('[COLOR yellow][B]+Ciudades[/B][/COLOR]', u_tube, 5, ciudades, fanart)
	add_dir('[COLOR yellow][B]+Como se hace[/B][/COLOR]', u_tube, 6, comosehace, fanart)
	add_dir('[COLOR yellow][B]+Conspiraciones[/B][/COLOR]', u_tube, 7, conspiraciones, fanart)
	add_dir('[COLOR yellow][B]+Curiosidades[/B][/COLOR]', u_tube, 8, curiosidades, fanart)
	add_dir('[COLOR yellow][B]+Deportes[/B][/COLOR]', u_tube, 9, deportes, fanart)
	add_dir('[COLOR yellow][B]+Desclasificados[/B][/COLOR]', u_tube, 10, desclasificados, fanart)
	add_dir('[COLOR yellow][B]+Egipto[/B][/COLOR]', u_tube, 11, egipto, fanart)
	add_dir('[COLOR yellow][B]+Extraterrestres[/B][/COLOR]', u_tube, 12, extraterrestres, fanart)
	add_dir('[COLOR yellow][B]+Fenomenos[/B][/COLOR]', u_tube, 13, fenomenos, fanart)
	add_dir('[COLOR yellow][B]+Guerra[/B][/COLOR]', u_tube, 14, guerra, fanart)
	add_dir('[COLOR yellow][B]+Historia[/B][/COLOR]', u_tube, 15, historia, fanart)
	add_dir('[COLOR yellow][B]+Informatica[/B][/COLOR]', u_tube, 16, informatica, fanart)
	add_dir('[COLOR yellow][B]+Musica[/B][/COLOR]', u_tube, 17, musica, fanart)
	add_dir('[COLOR yellow][B]+Pesca[/B][/COLOR]', u_tube, 18, pesca, fanart)
	add_dir('[COLOR yellow][B]+Religion[/B][/COLOR]', u_tube, 19, religion, fanart)
	add_dir('[COLOR yellow][B]+Universo[/B][/COLOR]', u_tube, 20, universo, fanart)
	add_dir('[COLOR yellow][B]+Adultos[/B][/COLOR]', u_tube, 21, adultos, fanart)
	add_dir('[COLOR yellow][B]+Narcos[/B][/COLOR]', u_tube, 22, narcos, fanart)
	add_dir('[COLOR yellow][B]+Segunda Guerra Mundial[/B][/COLOR]', u_tube, 23, segunda_guerra_mundial, fanart)
	add_dir('[COLOR yellow][B]+Roma[/B][/COLOR]', u_tube, 24, roma, fanart)



def search(): 	
## ESTA FUNCION BUSCA EN LAS LISTAS m3u DENTRO DE LAS CATEGORIAS. | Cuantas mas categorias, mas lento ira el buscador a no ser que hagamos buscadores individuales.
	try:
		keyb = xbmc.Keyboard('', 'Introduzca un texto a buscar')
		keyb.doModal()
		if (keyb.isConfirmed()):
		
			searchText = urllib.quote_plus(keyb.getText()).replace('+', ' ')
			content_db= make_request(db)
			match = re.compile(m3u_regex).findall(content_db)
			
			for thumb, name, url in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass
					
		
def lista(): #Animales
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass

def lista2(): #Celebridades
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria2)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass			

def lista3(): 
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria3)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass			

def lista4():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria4)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass

def lista5():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria5)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass			
#corte 5			
def lista6():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria6)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
def lista7():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria7)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass

def lista8():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria8)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
def lista9():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria9)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
def lista10():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria10)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
def lista11():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria11)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
def lista12():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria12)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
			
def lista13():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria13)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
def lista14():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria14)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
#corte 6
def lista15():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria15)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
def lista16():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria16)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
def lista17():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria17)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
def lista18():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria18)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
def lista19():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria19)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
def lista20():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria20)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
			
def lista20():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria20)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
#corte 7
def lista21():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria21)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
			
def lista22():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria22)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
			
def lista23():
## Obtiene la lista m3u que hayamos creado para una categoria.
	content = make_request(categoria23)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass
def playlist(name, url, thumb):	
#Basicamente mira en las categorias y devuelve un enlace sobre un fichero plano. name= nombre url="enlace" icon="xx"
	name = re.sub('\s+', ' ', name).strip()			
	url = url.replace('"', ' ').replace('&amp;', '&').strip()
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')			
			add_dir(name, url, '', thumb, thumb)			
		else:	
			add_dir(name, url, '', icon, fanart)
	else:
		if 'youtube.com/watch?v=' in url:
			url = 'plugin://plugin.video.youtube/play/?video_id=%s' % (url.split('=')[-1])
		elif 'dailymotion.com/video/' in url:
			url = url.split('/')[-1].split('_')[0]
			url = 'plugin://plugin.video.dailymotion_com/?mode=playVideo&url=%s' % url	
		else:			
			url = url
		if 'tvg-logo' in thumb:				
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			add_link(name, url, 1, thumb, thumb)			
		else:				
			add_link(name, url, 1, icon, fanart)	

def m3u_playlist(name, url, thumb):	
## despues de obtener las url de la lista m3u las muestra.
	name = re.sub('\s+', ' ', name).strip()			
	url = url.replace('"', ' ').replace('&amp;', '&').strip()
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')			
			add_dir(name, url, '', thumb, thumb)			
		else:	
			add_dir(name, url, '', icon, fanart)
	else:
		if 'youtube.com/watch?v=' in url:
			url = 'plugin://plugin.video.youtube/play/?video_id=%s' % (url.split('=')[-1])
		elif 'dailymotion.com/video/' in url:
			url = url.split('/')[-1].split('_')[0]
			url = 'plugin://plugin.video.dailymotion_com/?mode=playVideo&url=%s' % url	
		else:			
			url = url
		if 'tvg-logo' in thumb:				
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			add_link(name, url, 1, thumb, thumb)			
		else:				
			add_link(name, url, 1, icon, fanart)	

def play_video(url):
## Cuando se clica en el enlace de la url obtenida, si la lista es .m3u hara 'if' y si es texto plano hara else.
	if '.m3u8' in url:
		url = url.replace("http://","plugin://plugin.video.f4mTester/?url=http://").replace(".m3u8",".ts")
		url = url + "&amp;streamtype=TSDOWNLOADER"
		media_url = url
		item = xbmcgui.ListItem(name, path = media_url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
		return
	else:
		media_url = url
		item = xbmcgui.ListItem(name, path = media_url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
		return

def get_params():
## Codigo de shani de Live Stream Pro COn este script se obtienen los parametros. Sino sabes ... dejalo como lo puso Shani que asi funciona.
	param = []
	paramstring = sys.argv[2]
	if len(paramstring)>= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]
	return param

def add_dir(name, url, mode, iconimage, fanart):
## Añadre los directorios del menu. Con sus respetivos iconos y fanart y los enlaces a las acciones a enprender por el addon.
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		u = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
		ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
		return ok		
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok

def add_link(name, url, mode, iconimage, fanart):
## Agrega los links o enlaces.
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)	
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true') 
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz) 

def add_link_info(name, iconimage, fanart):
## Solo añade texto, no hace ninguna accion.
	u = sys.argv[0] + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)	
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'false') 
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz) 
	
def add_link_dummy(iconimage, fanart):
## Agrega los espacios en blaco en el menu pero no realiza ninguna accion.
	u = sys.argv[0] + "&iconimage=" + urllib.quote_plus(iconimage)	
	liz = xbmcgui.ListItem(iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'false') 
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)  

params = get_params()
url = None
name = None
mode = None
iconimage = None
#corte 9
try:
	url = urllib.unquote_plus(params["url"])
except:
	pass
try:
	name = urllib.unquote_plus(params["name"])
except:
	pass
try:
	mode = int(params["mode"])
except:
	pass
try:
	iconimage = urllib.unquote_plus(params["iconimage"])
except:
	pass  

print "Mode: " + str(mode)
print "URL: " + str(url)
print "Name: " + str(name)
print "iconimage: " + str(iconimage)	
## Vale esta parte son los llamados switch, lo que hace es redirigir a la funcion determinada en funcion al click que solicitemos en el menu.

if mode == None or url == None or len(url) < 1:
	main()

elif mode == 1:
	play_video(url)
	

elif mode == 2:
	lista()

elif mode == 3:
	lista2()
	
elif mode == 4:
	lista3()

elif mode == 98:
	search()


elif mode == 5:
	lista4()

elif mode == 6:
	lista5()

elif mode == 7:
	lista6()
	
elif mode == 8:
	lista7()

elif mode == 9:
	lista8()

elif mode == 10:
	lista9()
#corte 10
elif mode == 11:
	lista10()
elif mode == 12:
	lista11()
elif mode == 13:
	lista12()
elif mode == 14:
	lista13()
elif mode == 15:
	lista14()
elif mode == 16:
	lista15()
elif mode == 17:
	lista16()
elif mode == 18:
	lista17()
	
elif mode == 19:
	lista18()
elif mode == 20:
	lista19()
elif mode == 21:
	lista20()
elif mode == 21:
	lista20()
elif mode == 22:
	lista21()
elif mode == 23:
	lista22()
elif mode == 24:
	lista23()

xbmcplugin.endOfDirectory(plugin_handle)			