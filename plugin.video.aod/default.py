#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3
if PY2:
	from urllib import quote, unquote, quote_plus, unquote_plus, urlencode  # Python 2.X
	from urllib2 import build_opener, HTTPCookieProcessor, Request, urlopen  # Python 2.X
	from cookielib import LWPCookieJar  # Python 2.X
	from urlparse import urljoin, urlparse, urlunparse  # Python 2.X
elif PY3:
	from urllib.parse import quote, unquote, quote_plus, unquote_plus, urlencode, urljoin, urlparse, urlunparse  # Python 3+
	from urllib.request import build_opener, HTTPCookieProcessor, Request, urlopen  # Python 3+
	from http.cookiejar import LWPCookieJar  # Python 3+
import json
import xbmcvfs
import shutil
import socket
import time
import hashlib
import pyxbmct

global debuging
pluginhandle = int(sys.argv[1])
addon = xbmcaddon.Addon()
addonPath = xbmc.translatePath(addon.getAddonInfo('path')).encode('utf-8').decode('utf-8')
dataPath = xbmc.translatePath(addon.getAddonInfo('profile')).encode('utf-8').decode('utf-8')
AOD_favorites = xbmc.translatePath(os.path.join(dataPath, 'AOD_favorites', '')).encode('utf-8').decode('utf-8')
temp        = xbmc.translatePath(os.path.join(dataPath, 'temp', '')).encode('utf-8').decode('utf-8')
defaultFanart = os.path.join(addonPath, 'fanart.jpg')
icon = os.path.join(addonPath, 'icon.png')
masterOLD = "favorit.txt"
masterNEW = "favorit.txt"
source = os.path.join(temp, masterOLD)
favdatei = os.path.join(AOD_favorites, masterNEW)
global quality
global qualityhtml1
quality=addon.getSetting("quality")
qualityhtml1=addon.getSetting("qualityhtml1")
username=addon.getSetting("user")
password=addon.getSetting("pass")
global movies
movies=addon.getSetting("movies")
filtertype=addon.getSetting("filtertype")

xbmcplugin.setContent(pluginhandle, 'tvshows')

if not xbmcvfs.exists(AOD_favorites):
	xbmcvfs.mkdirs(AOD_favorites)

if xbmcvfs.exists(source):
	xbmcvfs.copy(source, favdatei)

if not xbmcvfs.exists(temp):  
	xbmcvfs.mkdirs(temp)

def py2_enc(s, encoding='utf-8'):
	if PY2 and isinstance(s, unicode):
		s = s.encode(encoding)
	return s

def py2_uni(s, encoding='utf-8'):
	if PY2 and isinstance(s, str):
		s = unicode(s, encoding)
	return s

def py3_dec(d, encoding='utf-8'):
	if PY3 and isinstance(d, bytes):
		d = d.decode(encoding)
	return d

def translation(id):
	LANGUAGE = addon.getLocalizedString(id)
	LANGUAGE = py2_enc(LANGUAGE)
	return LANGUAGE

def failing(content):
	log(content, xbmc.LOGERROR)

def debug(content):
	log(content, xbmc.LOGDEBUG)

def log(msg, level=xbmc.LOGNOTICE):
	msg = py2_enc(msg)
	xbmc.log("["+addon.getAddonInfo('id')+"-"+addon.getAddonInfo('version')+"]"+msg, level)

cookie = os.path.join(temp, 'cookie.jar')
cj = LWPCookieJar()

if xbmcvfs.exists(cookie):
	cj.load(cookie, ignore_discard=True, ignore_expires=True)

opener = build_opener(HTTPCookieProcessor(cj))
baseURL="https://www.anime-on-demand.de"


class Infowindow(pyxbmct.AddonDialogWindow):    
	text=""
	pos=0
	image=""
	trailer=""
	starttext=""
	def __init__(self, text=''):
		self.ueberschrift=re.compile('<h1 style="margin: 0;">(.+?)</h1>', re.DOTALL).findall(text)[0]
		try:
			self.image= re.compile('class="newspic" src="(.+?)"', re.DOTALL).findall(text)[0]
			if self.image[:4] != "http":
				self.image = baseURL+self.image
		except: pass
		kurz_inhalt = text[text.find('<div class="article-text">')+1:]
		kurz_inhalt = kurz_inhalt[:kurz_inhalt.find('</div>')]  
		if "<table " in kurz_inhalt: 
			self.starttext=text
			debug("starttext :"+self.starttext)
			kurz_inhalt = kurz_inhalt[:kurz_inhalt.find('<table ')]  
		kurz_inhalt=ersetze(kurz_inhalt)
		kurz_inhalt= kurz_inhalt.replace("</p>","\n")
		spl=kurz_inhalt.split('\n')
		self.text=""
		self.textlen=0
		for i in range(1,len(spl),1):
			entry=spl[i]
			debug("Entry :"+entry)
			if not "img alt=" in entry and not "iframe " in entry and not "<p>Vom " in entry:
				entry=entry.replace("<br />","\n")
				entry=entry.replace("</li>","\n")
				entry = re.sub(r'\<.*?\>', '', entry)
				self.text=self.text+entry+"\n"
				self.textlen=self.textlen+1
		self.ueberschrift=ersetze(self.ueberschrift)
		try:
			self.trailer=re.compile('src="https://www.youtube.com/embed/([^"]+?)"', re.DOTALL).findall(text)[0]        
			if "?" in self.trailer:
				self.trailer=self.trailer.split('?')[0]
			debug("TRailer: "+self.trailer)
		except: pass
		super(Infowindow, self).__init__("NEWS")
		self.setGeometry(925, 650, 23, 10)
		self.set_info_controls()
		# Connect a key action (Backspace) to close the window.
		self.connect(pyxbmct.ACTION_NAV_BACK, self.close)

	def set_info_controls(self):   
		debug("set_info_controls start")    
		self.ueberschrift=pyxbmct.Label(self.ueberschrift,alignment=pyxbmct.ALIGN_CENTER) 
		self.placeControl(self.ueberschrift, 0, 0,columnspan=10,rowspan=1) 
		if not "<tbody>" in self.starttext:  
			if self.image=="" and self.trailer !="" :
				self.image="https://img.youtube.com/vi/"+self.trailer+"/hqdefault.jpg"        
			self.image = pyxbmct.Image(self.image,aspectRatio=4)
			self.placeControl(self.image, 1, 3,columnspan=4,rowspan=6)
			self.beschreibung=pyxbmct.TextBox()
			self.placeControl(self.beschreibung, 7, 0,columnspan=10,rowspan=15) 
			self.beschreibung.setText(self.text)
			self.beschreibung.autoScroll(3000, 2000, 3000)
			if self.trailer !="":
				self.info_button = pyxbmct.Button('[B]Trailer[/B]', font='font14')
				self.placeControl(self.info_button, 22, 0,columnspan=3,rowspan=2) 
				self.connect(self.info_button, self.startv)
			self.close_button = pyxbmct.Button('[B]Close[/B]', font='font14')
			self.placeControl(self.close_button, 22, 7,columnspan=3,rowspan=2) 
			self.connect(self.close_button, self.close)
			self.setFocus(self.close_button)
		else:
			#self.image = pyxbmct.Image(self.image,aspectRatio=4)
			#self.placeControl(self.image, 1, 3,columnspan=4,rowspan=4)
			self.beschreibung = pyxbmct.FadeLabel()
			self.placeControl(self.beschreibung, 1, 0,columnspan=10,rowspan=1) 
			self.beschreibung.addLabel(self.text)
			kurz_inhalt = self.starttext[self.starttext.find('<tbody>')+1:]
			kurz_inhalt = kurz_inhalt[:kurz_inhalt.find('</tbody>')]    
			kurz_inhalt=kurz_inhalt.replace("\n","")
			starty=2
			startx=0
			counter=0
			counter2=0
			spl=kurz_inhalt.split('</tr>')
			for i in range(0,len(spl),1):
				entry=spl[i]
				entry=entry.replace("<br />","###")
				match=re.compile('>(.+?)</td>', re.DOTALL).findall(entry)
				for feld in match:
					feld=ersetze(feld)
					feld = re.sub(r'\<.*?\>', '', feld)
					if len(feld)>20:
						gr=5
					else:
						gr=0
					if "###" in feld:
						sp2=feld.split('###')
						for i2 in range(0,len(sp2),1):
							entry2=sp2[i2]
							self.sp1=pyxbmct.Label(entry2)
							self.placeControl(self.sp1, starty, startx,columnspan=2+gr,rowspan=2)
							starty=starty+1
							counter=counter+1
						starty=starty-counter
						if counter2<counter:
							counter2=counter-1
						counter=0
						startx=startx+2+gr
					else:
						self.sp1=pyxbmct.Label(feld)
						self.placeControl(self.sp1, starty, startx,columnspan=2+gr,rowspan=2)
						startx=startx+2+gr 
				starty=starty+1+counter2
				counter2=0
				startx=0
				self.close_button = pyxbmct.Button('[B]Close[/B]', font='font14')
				self.placeControl(self.close_button, 22, 7,columnspan=3,rowspan=2) 
				self.connect(self.close_button, self.close)
				self.setFocus(self.close_button)  
		self.connectEventList([pyxbmct.ACTION_MOVE_LEFT,
			pyxbmct.ACTION_MOVE_RIGHT,
			pyxbmct.ACTION_MOUSE_DRAG,
			pyxbmct.ACTION_MOUSE_LEFT_CLICK],
			self.leftright)

	def startv(self):
		self.close()
		finalURL='plugin://plugin.video.youtube/play/?video_id='+self.trailer
		xbmc.Player().play(finalURL)
		debug("Pressed Button")

	def leftright(self):
		if self.trailer !="":
			if self.getFocus() == self.close_button:
				self.setFocus(self.info_button)
			elif self.getFocus() == self.info_button:
				self.setFocus(self.close_button)
		else:
			self.setFocus(self.close_button)

def ersetze(inhalt):
	inhalt=inhalt.replace('&amp;#39;', '\'')
	inhalt=inhalt.replace('&#39;', '\'')
	inhalt=inhalt.replace('&quot;','"')
	inhalt=inhalt.replace('&gt;','>')
	inhalt=inhalt.replace('&amp;','&')
	inhalt=inhalt.replace('&uuml;','ü')
	inhalt=inhalt.replace('&ouml;','ö')
	inhalt=inhalt.replace('&auml;','ä')
	inhalt=inhalt.replace('&Uuml;','Ü')
	inhalt=inhalt.replace('&Ouml;','Ö')
	inhalt=inhalt.replace('&Auml;','Ä')
	inhalt=inhalt.replace('&szlig;','ß') 
	inhalt=inhalt.replace('&nbsp;',' ')
	inhalt=inhalt.replace('&rsquo;','\'')
	inhalt=inhalt.replace('&ndash;','-')
	inhalt=inhalt.replace('&hellip;','...')
	inhalt=inhalt.replace('&Eacute','E')
	inhalt=inhalt.replace('\n','')
	inhalt=inhalt.replace('\t','')
	inhalt=inhalt.replace('&copy;','(c)')
	inhalt=inhalt.replace('&ldquo;','"')
	inhalt=inhalt.replace('&rdquo;','"')
	inhalt=inhalt.replace('&bdquo;','"')
	inhalt = inhalt.strip()
	return inhalt

def addDir(name, url, mode, iconimage, desc="",title="",bild=""):
	u = sys.argv[0]+"?url="+quote_plus(url)+"&mode="+str(mode)+"&title="+str(title)+"&bild="+str(bild)
	liz = xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=iconimage)
	liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": desc})
	if iconimage != icon:
		liz.setArt({'fanart': iconimage})
	else:
		liz.setArt({'fanart': defaultFanart})
	return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)

def addLink(name, url, mode, iconimage, duration="", desc="", genre='',csrftoken="",type="",play='true'):
	debug("addlink :" + url)  
	u = sys.argv[0]+"?url="+quote_plus(url)+"&mode="+str(mode)+"&csrftoken="+csrftoken+"&type="+type
	liz = xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=iconimage)
	liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": desc, "Genre": genre})
 	if iconimage != icon:
		liz.setArt({'fanart': iconimage})
	else:
		liz.setArt({'fanart': defaultFanart})
	liz.addStreamInfo('Video', {'Duration': duration})
	liz.setProperty('IsPlayable', play)
	return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz)

def alles(url=""):
	debug ("###Start ALL" + url)   
	content=geturl(url)   
	kurz_inhalt = content[content.find('<div class="three-box-container">')+1:]
	kurz_inhalt = kurz_inhalt[:kurz_inhalt.find('<div class="l-contentcontainer l-navigationscontainer">')]
	spl=kurz_inhalt.split('<div class="three-box animebox">')
	for i in range(1,len(spl),1):
		entry=spl[i]
		if not "zum Film" in entry or movies=="true"    :  
			title=re.compile('<h3 class="animebox-title">([^<]+)</h3>', re.DOTALL).findall(entry)[0]
			img=re.compile('<img src="([^"]+)"', re.DOTALL).findall(entry)[0]
			if img[:4] != "http":
				img = baseURL+img
			link=re.compile('<a href="([^"]+)">', re.DOTALL).findall(entry)[0]
			if link[:4] != "http":
				link = baseURL+link
			desc=re.compile('<p class="animebox-shorttext">.+</p>', re.DOTALL).findall(entry)[0]
			desc=desc.replace('<p class="episodebox-shorttext">','').replace('<p class="animebox-shorttext">','').replace("</p>",'')
			debug("::::: filtertype "+str(filtertype))        
			if ( "(OmU)" in  title and filtertype=="0" ) or ( not "(OmU)" in  title and filtertype=="1" ) or filtertype=="2":     
				addDir(name=ersetze(title), url=link, mode="Serie", iconimage=img, desc=desc,title=title,bild=img)
	xbmcplugin.endOfDirectory(pluginhandle)

def login(url):
    global opener
    global cj
    global username
    global password
    userAgent = "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"
    opener.addheaders = [('User-Agent', userAgent)]
    content=opener.open(baseURL+"/users/sign_in").read()
    match = re.compile('ame="authenticity_token" value="([^"]+)"', re.DOTALL).findall(content)
    token1=match[0]
    debug ("USERNAME: "+ username)
    values = {'user[login]' : username,
        'user[password]' : password,
        'user[remember_me]' : '1',
        'commit' : 'Einloggen' ,
        'authenticity_token' : token1
    }
    data = urlencode(values)
    content=opener.open(baseURL+"/users/sign_in",data).read()
    content=opener.open(url).read()
    return content

def Serie(url,title="",bild=""):
	global opener
	global cj
	global username
	global password
	debug ("#############################################################################################")
	debug ("URL : " + url)
	userAgent = "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"
	opener.addheaders = [('User-Agent', userAgent)]
	content=opener.open(url).read()  
	debug("COntent :")
	debug("-------------------------------")
	debug(content)
	menulist=""
	if not '<a href="/users/edit">Benutzerkonto</a>' in content :    
		content=login(url)
	cj.save(cookie,ignore_discard=True, ignore_expires=True)
	csrftoken = re.compile('<meta name="csrf-token" content="([^"]+)"', re.DOTALL).findall(content)[0]
	kurz_inhalt = content[content.find('<div class="three-box-container">')+1:]                                      
	kurz_inhalt = kurz_inhalt[:kurz_inhalt.find('<div class="l-contentcontainer l-navigationscontainer">')]
	if '<div class="three-box episodebox flip-container">' in kurz_inhalt:
		spl=kurz_inhalt.split('<div class="three-box episodebox flip-container">')
	else:
		spl=kurz_inhalt.split('<div class="l-off-canvas-container">')
	debug("------------------------------")
	debug ("Kurzinhalt:")
	debug (kurz_inhalt)  
	for i in range(1,len(spl),1):
		entry=spl[i]
		try:
			debug("------------------------------")
			debug("Entry:")
			debug(entry)          
			debug ("-------------------------------")     
			img=re.compile('src="([^"]+)"', re.DOTALL).findall(entry)[0]
			if img[:4] != "http":
				img = baseURL+img
			ret,menulist=flashvideo(entry,img,csrftoken,menulist)
			if ret==1:
				ret,menulist=html5video(entry,img,csrftoken,menulist)
		except :
			error=1  
	debug ("#############################################################################")
	f = open( os.path.join(temp,"menu.txt"), 'w')  
	f.write(menulist)
	f.close()
	addDir(translation(30127), url, mode="simil", iconimage="", desc="")      
	found=0
	if xbmcvfs.exists(favdatei):
		f=open(favdatei,'r')     
		for line in f:
			if url in line:
				found=1
	if found==0:
		addDir(translation(30128), url, mode="favadd", iconimage="", desc="",title=title,bild=bild)      
	else :
		addDir(translation(30129), url, mode="favdel", iconimage="", desc="")     
	xbmcplugin.endOfDirectory(pluginhandle)  

def favadd(url,titel,bild):
	debug(" favadd url :"+url)
	textfile=url+"###"+titel+"###"+bild+"\n"
	try:
		f=open(favdatei,'r')
		for line in f:
			textfile=textfile+line
		f.close()
	except: pass
	f=open(favdatei,'w')
	f.write(textfile)
	f.close()
	xbmc.executebuiltin('Notification('+ translation(30131)+',"'+translation(30132)+'")')
	xbmc.executebuiltin("Container.Refresh")

def favdel(url):
	debug(" FAVDEL url :"+url)
	textfile=""
	f=open(favdatei,'r')
	for line in f:
		if not url in line and not line=="\n":
			textfile=textfile+line
	f.close()
	f=open(favdatei,'w')
	f.write(textfile)
	f.close()
	xbmc.executebuiltin('Notification('+ translation(30133)+',"'+translation(30134)+'")')
	xbmc.executebuiltin("Container.Refresh")  

def listfav():
	if xbmcvfs.exists(favdatei):
		f=open(favdatei,'r')
		for line in f:
			spl=line.split('###')
			addDir(name=spl[1], url=spl[0], mode="Serie", iconimage=spl[2].strip(), desc="",title=spl[1],bild=spl[2].strip())
		f.close()
	xbmcplugin.endOfDirectory(pluginhandle)

def simil(url):
	userAgent = "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"
	opener.addheaders = [('User-Agent', userAgent)]
	content=opener.open(url).read()  
	kurz_inhalt = content[content.find('<div class="jcarousel">')+1:]                                      
	kurz_inhalt = kurz_inhalt[:kurz_inhalt.find('</div>')]
	spl=kurz_inhalt.split('<li>')
	for i in range(1,len(spl),1):
		entry=spl[i]
		match=re.compile('<a href="(.+?)">(.+?)</a>', re.DOTALL).findall(entry)
		urlx=match[0][0]
		title=match[0][1]
		if urlx[:4] != "http":
			urlx = baseURL+urlx
		img=re.compile('src="(.+?)"', re.DOTALL).findall(entry)[0]
		if img[:4] != "http":
			img = baseURL+img
		addDir(name=ersetze(title), url=urlx, mode="Serie", iconimage=img, desc="",title=title,bild=img)
	xbmcplugin.endOfDirectory(pluginhandle)

def html5video(entry,img,csrftoken,menulist):     
	error=0
	debug("Start HTMLvideo")
	try:
		title=re.compile(' title="([^"]+)"', re.DOTALL).findall(entry)[0]
		debug("Title :"+title)  
		try:
			if '<p class="episodebox-shorttext">' in entry:
				desc=re.compile('<p class="episodebox-shorttext">(.+)</p>', re.DOTALL).findall(entry)[0]
			else:
				desc=re.compile('<div itemprop="description">(.+)</p>', re.DOTALL).findall(entry)[0]
			desc=desc.replace("<br />","").replace("<p>","").replace("&quot;","\"")
		except: desc=""
		debug("csrftoken : "+csrftoken)
		match=re.compile('title="([^"]+)" data-playlist="([^"]+)"', re.DOTALL).findall(entry)
		for type,link in match:
			title2=title + " ( "+ type.replace("starten","").replace("Japanischen Stream mit Untertiteln","OmU").replace("Deutschen Stream","Sync") +")"
			if link[:4] != "http":
				link = baseURL+link
			debug("Link: "+ link)
			debug("title 2 :"+title2)
			idd=hashlib.md5(title2).hexdigest()
			menulist=menulist+idd+"###"+link+"###"+csrftoken+"###html5###\n"
			if (not "Sync" in  title2 and filtertype=="0") or ("Sync" in  title2 and filtertype=="1") or filtertype=="2": 
				addLink(name=ersetze(title2), url="plugin://plugin.video.aod/", mode="hashplay", iconimage=img, desc=desc,csrftoken=idd,type="html5")      
	except:
		error=1
	return error,menulist

def hashplay(idd):
	debug("hashplay url :"+idd)
	f=xbmcvfs.File(os.path.join(temp,"menu.txt"),"r")   
	daten=f.read()
	zeilen=daten.split('\n')  
	for zeile in zeilen:    
		debug ("Read Zeile :"+zeile)
		felder=zeile.split("###")
		debug("Felder ")
		debug(str(felder))
		if felder[0]==idd:    
			debug("Gefunden")
			uurl=felder[1]
			csrftoken=felder[2]          
			type=felder[3]                      
			debug("Type :"+type)
			Folge(uurl,csrftoken,type)

def flashvideo(entry,img,csrftoken,menulist):
    error=0 
    debug("Start Flashvideo")
    try:
      match=re.compile('title="([^"]+)" data-stream="([^"]+)" data-dialog-header="([^"]+)"', re.DOTALL).findall(entry)
      title=match[0][2]        
      debug("Title :"+ str(match))
      found=0      
      linka=""
      linko=""
      for qua,linka,name in match:
        titl=quality+ "-Stream"         
        if titl.lower() in qua.lower():
            link=linka
            found=1
        else:
             linko=linka
      if found==0:         
         link=linko
      if link :
         link=baseURL+link
         debug("Link: "+ link)
         if '<p class="episodebox-shorttext">' in entry:
           desc=re.compile('<p class="episodebox-shorttext">(.+)</p>', re.DOTALL).findall(entry)[0]
         else:
           desc=re.compile('<div itemprop="description">(.+)</p>', re.DOTALL).findall(entry)[0]
         desc = re.sub(r'\<.*?\>', '', desc)    
         debug("csrftoken : "+csrftoken)
         debug("URL :" + link)
         debug("title :"+title)
         idd=hashlib.md5(title).hexdigest()        
         menulist=menulist+idd+"###"+link+"###"+csrftoken+"###flash###\n"     
         addLink(name=ersetze(title), url="plugin://plugin.video.aod/", mode="hashplay", iconimage=img, desc=desc,csrftoken=idd,type="flash")      
    except :
       error=1
    return error,menulist

def Folge(url,csrftoken,type):
  global opener
  global cj
  global username
  global password
  debug("Folge URL :"+url+"#")
  debug("Folge csrftoken :"+csrftoken+"#")
  debug("Folge type :"+type+"#")
  try :        
    opener.addheaders = [('X-CSRF-Token', csrftoken),
                     ('X-Requested-With', "XMLHttpRequest"),
                     ('Accept', "application/json, text/javascript, */*; q=0.01")]      
    content=opener.open(url).read()    
    debug("Content:")
    debug("--------------------:")
    debug(content)
    debug("----------------:")
    if type=="html5":
      debug("Folge  html5")
      stream = re.compile('"file":"([^"]+)"', re.DOTALL).findall(content)[0].replace("\\u0026","&")
      debug("1")
      debug("stream :" + stream)
      content2=opener.open(stream).read()   
      debug("-------Content2---------")      
      debug(content2)      
      debug("----------------")      
      spl=content2.split('#EXT-X-STREAM-INF')
      debug("qualityhtml1 :"+qualityhtml1)
      if not qualityhtml1=="6":
        element=spl[int(qualityhtml1)+1]
        debug("Element: "+element)
        match = re.compile('chunklist(.+)', re.DOTALL).findall(element)
        qual="chunklist"+match[0]
        debug("Qal : "+qual)
        liste=stream.split('/')
        laenge=len(liste)
        pfadt=liste[0:-1]
        s="/"
        pfad=s.join(pfadt)
        debug("Pfad : "+ pfad)
        stream=pfad+"/"+qual[0:-1]    
      if qualityhtml1=="6":
        file=[]
        namen=[]
        liste=stream.split('/')
        laenge=len(liste)
        pfadt=liste[0:-1]
        s="/"
        pfad=s.join(pfadt)
        for i in range(1,len(spl),1):
          element=spl[i]
          match = re.compile('BANDWIDTH=(.+?),RESOLUTION=(.+?)chunklist', re.DOTALL).findall(element)
          band=match[0][0]
          res=match[0][1]
          match = re.compile('chunklist(.+)', re.DOTALL).findall(element)
          qual="chunklist"+match[0]
          file.append(qual)
          namen.append(res + "( "+ str(int(band)/1024) +" kb/s )")
        dialog = xbmcgui.Dialog()
        nr=dialog.select("Qualität", namen) 
        files=file[nr]
        debug("Files :"+files)
        stream=pfad+"/"+files[0:-1]
        debug("##AV ##"+ stream)        
      debug("----------------")
      listitem = xbmcgui.ListItem (path=stream)
    if type=="flash":
      stream = re.compile('"streamurl":"([^"]+)"', re.DOTALL).findall(content)[0]
      match = re.compile('(.+)mp4:(.+)', re.DOTALL).findall(stream)  
      path="mp4:"+match[0][1]
      server=match[0][0] 
      listitem = xbmcgui.ListItem (path=server +"swfUrl=https://ssl.p.jwpcdn.com/6/12/jwplayer.flash.swf playpath="+path+" token=83nqamH3#i3j app=aodrelaunch/ swfVfy=true")
    
    xbmcplugin.setResolvedUrl(pluginhandle,True, listitem)    
    debug(content)
  except IOError, e:          
        if e.code == 401:
            dialog = xbmcgui.Dialog()
            dialog.ok("Login",translation(30110))

def geturl(url):
	userAgent = "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"
	opener.addheaders = [('User-Agent', userAgent)]
	req = Request(url)
	inhalt = urlopen(req).read()   
	cj.save(cookie, ignore_discard=True, ignore_expires=True)
	return inhalt

def parameters_string_to_dict(parameters):
	paramDict = {}
	if parameters:
		paramPairs = parameters[1:].split("&")
		for paramsPair in paramPairs:
			paramSplits = paramsPair.split('=')
			if (len(paramSplits)) == 2:
				paramDict[paramSplits[0]] = paramSplits[1]
	return paramDict

def category():
	global opener
	global cj
	global username
	global password
	url=baseURL+"/animes"
	userAgent = "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"
	opener.addheaders = [('User-Agent', userAgent)]
	content=opener.open(url).read()  
	if not '<a href="/users/edit">Benutzerkonto</a>' in content :    
		content=login(url)
	cj.save(cookie,ignore_discard=True, ignore_expires=True)
	kurz_inhalt = content[content.find('<ul class="inline-block-list" style="display: block; text-align: center;">')+1:]                                      
	kurz_inhalt = kurz_inhalt[:kurz_inhalt.find('</ul>')]  
	match=re.compile('<a href="([^"]+)">([^<]+)</a>', re.DOTALL).findall(kurz_inhalt)
	for link,name in match:
		addDir(name=ersetze(name), url=baseURL+link, mode="catall",iconimage=icon, desc="")
	xbmcplugin.endOfDirectory(pluginhandle)
 
def language():
	global opener
	global cj
	global username
	global password
	url=baseURL+"/animes"
	userAgent = "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"
	opener.addheaders = [('User-Agent', userAgent)]
	content=opener.open(url).read()  
	if not '<a href="/users/edit">Benutzerkonto</a>' in content :    
		content=login(url)
	cj.save(cookie,ignore_discard=True, ignore_expires=True)
	kurz_inhalt = content[content.find('<ul class="inline-block-list" style="display: block; text-align: center;">')+1:]     
	kurz_inhalt = kurz_inhalt[kurz_inhalt.find('<ul class="inline-block-list" style="display: block; text-align: center;">')+1:]                                      
	kurz_inhalt = kurz_inhalt[:kurz_inhalt.find('</ul>')]  
	match=re.compile('<a href="([^"]+)">([^<]+)</a>', re.DOTALL).findall(kurz_inhalt)
	for link,name in match:
		if not "HTML5" in name:
			addDir(name=ersetze(name), url=baseURL+link, mode="catall",iconimage=icon, desc="")
	xbmcplugin.endOfDirectory(pluginhandle)
 
params = parameters_string_to_dict(sys.argv[2])  
mode = unquote_plus(params.get('mode', ''))
url = unquote_plus(params.get('url', ''))
type = unquote_plus(params.get('type', ''))
csrftoken = unquote_plus(params.get('csrftoken', ''))
title = unquote_plus(params.get('title', ''))
bild = unquote_plus(params.get('bild', ''))

def abisz():
	addDir("0-9", baseURL+"/animes/begins_with/0-9", 'catall', icon)
	letters = [chr(i) for i in xrange(ord('a'), ord('z')+1)]
	for letter in letters:
		addDir(letter.upper(), baseURL+"/animes/begins_with/"+letter.upper(), 'catall', icon)
	xbmcplugin.endOfDirectory(pluginhandle)

def newmenu():
	addDir(translation(30113), translation(30113), 'new_episodes', icon)
	addDir(translation(30114), translation(30114), 'new_simulcast', icon)
	addDir(translation(30115), translation(30115), 'new_animes', icon)
	xbmcplugin.endOfDirectory(pluginhandle)   

def newsmenu():
	addDir(translation(30119), "/articles/category/3/1", 'readnews', icon)
	addDir(translation(30120), "/articles/category/2/1", 'readnews', icon)
	addDir(translation(30121), "/articles/category/1/1", 'readnews', icon)
	addDir(translation(30122), "/articles/category/4/1", 'readnews', icon)
	xbmcplugin.endOfDirectory(pluginhandle)         

def readnews(kat):
	url=baseURL+kat
	content = geturl(url)    
	elemente = content.split('<div class="category-item">') 
	for i in range(1, len(elemente), 1):
		element=elemente[i]   
		match = re.compile('<a href="(.+?)">(.+?)</a>', re.DOTALL).findall(element)
		url=match[0][0]
		name=match[0][1]
		if url[:4] != "http":
			url = baseURL+url
		img = re.compile('src="(.+?)"', re.DOTALL).findall(element)[0]
		if img[:4] != "http":
			img = baseURL+img
		if not "aod auf der" in name.lower():
			addLink(name=ersetze(name), url=url, mode="artikel", iconimage=img, play="false") 
	xbmcplugin.endOfDirectory(pluginhandle)         

def artikel(url):
	debug("Start Artikel")
	debug("Artikel  ULR:"+ url)
	content = geturl(url) 
	debug(" ARtikeL ##")
	window=Infowindow(text=content)
	window.doModal()
	del window

def menu():
	addDir(translation(30118), "", 'newsmenu', icon)
	addDir(translation(30117), translation(30117), 'newmenu', icon)
	addDir(translation(30116), translation(30116), 'top10', icon)
	addDir(translation(30107), translation(30107), 'All', icon)
	addDir(translation(30104), translation(30104), 'AZ', icon)
	addDir(translation(30105), translation(30105), 'cat', icon)
	addDir(translation(30106), translation(30106), 'lang', icon)
	addDir(translation(30130), translation(30130), 'listfav', icon)
	addDir(translation(30111), translation(30111), 'cookies', icon)
	addDir(translation(30108), translation(30108), 'Settings', icon)
	xbmcplugin.endOfDirectory(pluginhandle)

def Start_listen(start_string):
	content=geturl("http://www.anime-on-demand.de/")
	kurz_inhalt = content[content.find(start_string)+1:]                                      
	kurz_inhalt = kurz_inhalt[:kurz_inhalt.find('<hr />')]
	spl=kurz_inhalt.split('<li>')
	for i in range(1,len(spl),1):
		entry=spl[i]
		debug("-------")
		debug(entry)
		img=re.compile('src="(.+?)"', re.DOTALL).findall(entry)[0]
		if img[:4] != "http":
			img = baseURL+img
		match=re.compile('<a href="(.+?)">(.+?)</a>', re.DOTALL).findall(entry)
		link=match[0][0]
		Serie=match[0][1]
		try :
			folgen=re.compile('<span class="neweps">(.+?)</span>', re.DOTALL).findall(entry)[0]
			name=ersetze(Serie + " ( "+ folgen + " ) ")
		except:
			name=ersetze(Serie)
		if link[:4] != "http":
			link = baseURL+link
		name = re.sub(r'\<.*?\>', '', name)
		if ( "(OmU)" in  name and filtertype=="0" ) or ( not "(OmU)" in  name and filtertype=="1" ) or filtertype=="2": 
			addDir(name=name, url=link, mode="Serie", iconimage=img, desc="",title=name,bild=img)
	xbmcplugin.endOfDirectory(pluginhandle)

def cookies():
	if xbmcvfs.exists(temp) and os.path.isdir(temp):
		shutil.rmtree(temp, ignore_errors=True)
	xbmcvfs.mkdirs(temp)
	menu()

# Wenn Settings ausgewählt wurde
if mode == 'Settings':
	addon.openSettings()
# Wenn Kategory ausgewählt wurde
elif mode == 'All':
	alles(baseURL+"/animes")
elif mode == 'Serie':
	Serie(url,title,bild) 
elif mode == 'Folge':
	Folge(url,csrftoken,type)            
elif mode == 'cat':
	category()  
elif mode == 'lang':
	language()  
elif mode == 'catall':
	alles(url)
elif mode == 'AZ':
	abisz()
elif mode == 'cookies':
	cookies()
elif mode == 'getcontent_search':
	getcontent_search(url)             
elif mode == 'new_episodes':
	Start_listen("Neue Episoden")  
elif mode == 'new_simulcast':
	Start_listen("Neue Simulcasts")  
elif mode == 'new_animes':
	Start_listen("Neue Anime-Titel")  
elif mode == 'top10':
	Start_listen("Anime Top 10")            
elif mode == 'hashplay':          
	hashplay(csrftoken)
elif mode == 'newsmenu':          
	newsmenu()
elif mode == 'newmenu':          
	newmenu()          
elif mode == 'readnews':          
	readnews(url)            
elif mode == 'artikel':          
	artikel(url)                      
elif mode == 'simil':          
	simil(url)          
elif mode == 'favadd':          
	favadd(url,title,bild)          
elif mode == 'favdel':          
	favdel(url)                             
elif mode == 'listfav':          
	listfav()     
else:
	menu()