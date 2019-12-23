# -*- coding: utf-8 -*-

'''
Copyright (C) 2017

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
'''



import re
import urllib, urllib2, os, sys
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

mysettings = xbmcaddon.Addon(id = 'plugin.video.monkeyspank')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
logos = xbmc.translatePath(os.path.join(home, 'logos\\'))
homemenu = xbmc.translatePath(os.path.join(home, 'resources', 'playlists'))


xhamster = 'https://xhamster.com'


def menulist():
	try:
		mainmenu = open(homemenu, 'r')
		content = mainmenu.read()
		mainmenu.close()
		match = re.compile('#.+,(.+?)\n(.+?)\n').findall(content)
		return match
	except:
		pass

def make_request(url):
	try:
		req = urllib2.Request(url)
		if xhamster in url:
			req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/23.0.1271.64 Safari/537.11')
		else:
			req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
		response = urllib2.urlopen(req, timeout = 60)
		link = response.read()
		response.close()
		return link
	except urllib2.URLError, e:
		print 'We failed to open "%s".' % url
		if hasattr(e, 'code'):
			print 'We failed with error code - %s.' % e.code
		elif hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason

def home():
	add_dir('...[COLOR cyan]  Home  [/COLOR]...', '', None, icon, fanart)

def main():
    add_dir('[B][COLOR cyan]Monkey[COLOR deeppink]Spank [COLOR cyan]Videos[/COLOR][/B]', xhamster + '/new/1.html', 2, logos + 'xhamster.png', fanart)


def search():
	try:
		keyb = xbmc.Keyboard('', '[COLOR deeppink]Enter search text[/COLOR]')
		keyb.doModal()
		if (keyb.isConfirmed()):
			searchText = urllib.quote_plus(keyb.getText())
		if 'Monkey[COLOR cyan]Spank' in name:
			url = 'https://xhamster.com/search.php?q=' + searchText 
			start(url)
	except:
		pass

def start(url): 
	home()
	if 'xhamster' in url:
		content = make_request(url)
		add_dir('[COLOR deeppink]Monkey[COLOR cyan]Spank [COLOR deeppink]Search[/COLOR]', xhamster, 1, logos + 'xhamster.png', fanart)	
		add_dir('[COLOR cyan]Categories[/COLOR]', xhamster, 17, logos + 'xhamster.png', fanart) 
		add_dir('[COLOR deeppink]Rankings[/COLOR]', xhamster + '/rankings/weekly-top-viewed.html' , 42, logos + 'xhamster.png', fanart) 
		add_dir('[COLOR cyan]Change Content[/COLOR]', xhamster, 24, logos + 'xhamster.png', fanart)
		add_dir('[COLOR deeppink]Pornstars[/COLOR]', xhamster + '/pornstars/', 25, logos + 'xhamster.png', fanart)
		match = re.compile('><a href="https://xhamster.com/videos/(.+?)".+?<img src=\'(.+?)\'.+?alt="([^"]*)".+?<b>(.+?)</b>.+?<div class="(.+?)"', re.DOTALL).findall(content)
		for url, thumb, name, duration, dummy in match:
			name = name.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', '\'')
			if '?from=video_promo' in url:
				pass
			if 'hSpriteHD' in dummy:
				add_link(name + '[COLOR cyan]' +' [HD]' +'[/COLOR]' +' [COLOR deeppink]('+ duration + ')[/COLOR]', 'http://xhamster.com/videos/' + url, 4, thumb, fanart)
			else:
				add_link(name + '[COLOR deeppink]('+ duration +')[/COLOR]', 'http://xhamster.com/videos/' + url, 4, thumb, fanart)
		match = re.compile('<div id="cType"><div class="([^"]*)"></div>').findall(content)
		if "iconL iconTrans" in match :
			match = re.compile('<link rel="next" href="([^"]*)"><link rel="dns-prefetch"').findall(content) 
			add_dir('[COLOR deeppink]Next  Page  >>>>[/COLOR]', match[0] + '?content=shemale', 2, logos + 'xhamster.png', fanart)	
		if "iconL iconGays" in match :
			match = re.compile('<link rel="next" href="([^"]*)"><link rel="dns-prefetch"').findall(content) 
			add_dir('[COLOR deeppink]Next  Page  >>>>[/COLOR]', match[0] + '?content=gay', 2, logos + 'xhamster.png', fanart)	
		if "iconL iconStraight" in match :
			match = re.compile('<link rel="next" href="([^"]*)"><link rel="dns-prefetch"').findall(content) 
			add_dir('[COLOR deeppink]Next  Page  >>>>[/COLOR]', match[0] + '?content=straight', 2, logos + 'xhamster.png', fanart)		
		try:
			match = re.compile('<a href=\'(.+?)\' class=\'last\' overicon=\'iconPagerNextHover\'><div class=\'icon iconPagerNext\'>').findall(content) 
			match = [item.replace('&amp;', '&') for item in match]
			for url in match:
				if "search" in url:
					add_dir('[COLOR deeppink]Next  Page  >>>>[/COLOR]', match[0] , 2, logos + 'xhamster.png', fanart)
				else:pass
		except:
			pass

def xhamster_categories(url):
	home()
	content = make_request(url)
	match = re.compile('<a href="https://xhamster.com/categories/([^"]*)"').findall(content)
	for url in match:
		name = url
		name = name.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', '´').replace('new-', '').replace('-1.html', '').replace('_', '')
		name = name.capitalize()
		add_dir(name, xhamster + '/categories/' + url, 2, logos + 'xhamster.png', fanart)

def xhamster_content(url) :	
	home()
	content = make_request(url)	
	match = re.compile("<a href=\"(.+?)\" hint='(.+?)'><div class='iconL").findall(content)
	for url, name in match:
		add_dir(name, url,  2, logos + 'xhamster.png', fanart)

def xhamster_rankings(url) :
	home()
	content = make_request(url)
	match = re.compile('<a href="([^"]+)" >(.+?)</a>', re.DOTALL).findall(content)
	for url, name in match:
		add_dir(name, url,  2, logos + 'xhamster.png', fanart)

def xhamster_pornstars(url):
	home()
	content = make_request(url)
	match = re.compile('<a href="https://xhamster.com/pornstars/([^"]*)"').findall(content)
	for url in match:
		name = url
		name = name.replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', '´').replace('new-', '').replace('-1.html', '').replace('_', '')
		name = name.capitalize()
		add_dir(name, xhamster + '/pornstars/' + url, 2, logos + 'xhamster.png', fanart)
	
def resolve_url(url):
	content = make_request(url)
	if 'xhamster' in url:
		media_url = re.compile("file: '(.+?)',").findall(content)[0]
	else:
		media_url = url
	item = xbmcgui.ListItem(name, path = media_url)
	item.setMimeType('video/mp4')
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)	  
	return

def get_params():
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
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name, "overlay":"6"})
	liz.setProperty('fanart_image', fanart)
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok
	
def add_link(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)	
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo(type="Video", infoLabels={"Title": name})
	try:
		liz.setContentLookup(False)
	except:
		pass
	liz.setProperty('IsPlayable', 'true')
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz) 
	return ok

params = get_params()
url = None
name = None
mode = None
iconimage = None

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

if mode == None or url == None or len(url) < 1:
	main()

elif mode == 1:
	search()

elif mode == 2:
	start(url)
  
elif mode == 3:
	media_list(url)

elif mode == 4:
	resolve_url(url)

elif mode == 5:	
	xhamster_categories(url)

elif mode == 6:	
	xhamster_content(url)		

elif mode == 7:	
	xhamster_rankings(url)

elif mode == 17:	
	xhamster_categories(url)

elif mode == 24:	
	xhamster_content(url)

elif mode == 25:	
	xhamster_pornstars(url)

elif mode == 42:	
	xhamster_rankings(url)

elif mode == 9:
	item = xbmcgui.ListItem(name, path = url)
	item.setMimeType('video/mp4')
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
