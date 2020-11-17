################################################################################
#      Copyright (C) 2015 Surfacingx                                           #
#                                                                              #
#  This Program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 2, or (at your option)         #
#  any later version.                                                          #
#                                                                              #
#  This Program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with XBMC; see the file COPYING.  If not, write to                    #
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.       #
#  http://www.gnu.org/copyleft/gpl.html                                        #
################################################################################

version = 0.1
import wizard as wiz
import re


def apkScraper(name=""):
	if name == 'kodi':
		kodiurl1 = 'http://mirrors.kodi.tv/releases/android/arm/'
		kodiurl2 = 'http://mirrors.kodi.tv/releases/android/arm/old/'
		url1 = wiz.openURL(kodiurl1).replace('\n', '').replace('\r', '').replace('\t', '')
		url2 = wiz.openURL(kodiurl2).replace('\n', '').replace('\r', '').replace('\t', '')
		x = 0
		match1 = re.compile('<tr><td><a href="(.+?)">(.+?)</a></td><td>(.+?)</td><td>(.+?)</td></tr>').findall(url1)
		match2 = re.compile('<tr><td><a href="(.+?)">(.+?)</a></td><td>(.+?)</td><td>(.+?)</td></tr>').findall(url2)
		
		addFile("Official Kodi Apk\'s", themeit=THEME1)
		rc = False
		for url, name, size, date in match1:
			if url in ['../', 'old/']: continue
			if not url.endswith('.apk'): continue
			if not url.find('_') == -1 and rc == True: continue
			try:
				tempname = name.split('-')
				if not url.find('_') == -1:
					rc = True
					name2, v2 = tempname[2].split('_')
				else: 
					name2 = tempname[2]
					v2 = ''
				title = "[COLOR %s]%s v%s%s %s[/COLOR] [COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % (COLOR1, tempname[0].title(), tempname[1], v2.upper(), name2, COLOR2, size.replace(' ', ''), COLOR1, date)
				download = urljoin(kodiurl1, url)
				addFile(title, 'apkinstall', "%s v%s%s %s" % (tempname[0].title(), tempname[1], v2.upper(), name2), download)
				x += 1
			except:
				wiz.log("Error on: %s" % name)
			
		for url, name, size, date in match2:
			if url in ['../', 'old/']: continue
			if not url.endswith('.apk'): continue
			if not url.find('_') == -1: continue
			try:
				tempname = name.split('-')
				title = "[COLOR %s]%s v%s %s[/COLOR] [COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % (COLOR1, tempname[0].title(), tempname[1], tempname[2], COLOR2, size.replace(' ', ''), COLOR1, date)
				download = urljoin(kodiurl2, url)
				addFile(title, 'apkinstall', "%s v%s %s" % (tempname[0].title(), tempname[1], tempname[2]), download)
				x += 1
			except:
				wiz.log("Error on: %s" % name)
		if x == 0: addFile("Error Kodi Scraper Is Currently Down.")
	elif name == 'spmc':
		spmcurl1 = 'https://github.com/koying/SPMC/releases'
		url1 = wiz.openURL(spmcurl1).replace('\n', '').replace('\r', '').replace('\t', '')
		x = 0
		match1 = re.compile('<div.+?lass="release-body.+?div class="release-header".+?a href=.+?>(.+?)</a>.+?ul class="release-downloads">(.+?)</ul>.+?/div>').findall(url1)
		
		addFile("Official SPMC Apk\'s", themeit=THEME1)

		for name, urls in match1:
			tempurl = ''
			match2 = re.compile('<li>.+?<a href="(.+?)" rel="nofollow">.+?<small class="text-gray float-right">(.+?)</small>.+?strong>(.+?)</strong>.+?</a>.+?</li>').findall(urls)
			for apkurl, apksize, apkname in match2:
				if apkname.find('armeabi') == -1: continue
				if apkname.find('launcher') > -1: continue
				tempurl = urljoin('https://github.com', apkurl)
				break
			if tempurl == '': continue
			try:
				name = "SPMC %s" % name
				title = "[COLOR %s]%s[/COLOR] [COLOR %s]%s[/COLOR]" % (COLOR1, name, COLOR2, apksize.replace(' ', ''))
				download = tempurl
				addFile(title, 'apkinstall', name, download)
				x += 1
			except Exception, e:
				wiz.log("Error on: %s / %s" % (name, str(e)))
		if x == 0: addFile("Error SPMC Scraper Is Currently Down.")