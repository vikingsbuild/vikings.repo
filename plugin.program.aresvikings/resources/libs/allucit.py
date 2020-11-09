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

import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os, sys, xbmcvfs, glob
import shutil
import urllib2,urllib
import re
import uservar
import time
try:    from sqlite3 import dbapi2 as database
except: from pysqlite2 import dbapi2 as database
from datetime import date, datetime, timedelta
from resources.libs import wizard as wiz

ADDON_ID       = uservar.ADDON_ID
ADDONTITLE     = uservar.ADDONTITLE
ADDON          = wiz.addonId(ADDON_ID)
DIALOG         = xbmcgui.Dialog()
HOME           = xbmc.translatePath('special://home/')
ADDONS         = os.path.join(HOME,      'addons')
USERDATA       = os.path.join(HOME,      'userdata')
PLUGIN         = os.path.join(ADDONS,    ADDON_ID)
PACKAGES       = os.path.join(ADDONS,    'packages')
ADDONDATA      = os.path.join(USERDATA,  'addon_data', ADDON_ID)
ADDOND         = os.path.join(USERDATA,  'addon_data')
ALLUCFOLD      = os.path.join(ADDONDATA, 'Alluc')
ICON           = os.path.join(PLUGIN,    'icon.png')
TODAY          = date.today()
TOMORROW       = TODAY + timedelta(days=1)
THREEDAYS      = TODAY + timedelta(days=3)
KEEPALLUC      = wiz.getS('keepalluc')
ALLUCSAVE      = wiz.getS('alluclastsave')
COLOR1         = uservar.COLOR1
COLOR2         = uservar.COLOR2
ORDER          = ['nan', 'notsure', 'specto', 'covenant', 'bennu', 'deathstreams']

ALLUCID = {
	'nan': {
		'name'     : 'Nan Scrapers',
		'plugin'   : 'script.module.nanscrapers',
		'saved'    : 'allucnan',
		'path'     : os.path.join(ADDONS, 'script.module.nanscrapers'),
		'icon'     : os.path.join(ADDONS, 'script.module.nanscrapers', 'icon.png'),
		'fanart'   : os.path.join(ADDONS, 'script.module.nanscrapers', 'fanart.jpg'),
		'file'     : os.path.join(ALLUCFOLD, 'nan_alluc'),
		'settings' : os.path.join(ADDOND, 'script.module.nanscrapers', 'settings.xml'),
		'default'  : 'Alluc_user',
		'data'     : ['Alluc_enabled', 'Alluc_max', 'Alluc_user', 'Alluc_pw'],
		'activate' : ''},
	'notsure': {
		'name'     : 'Not Sure',
		'plugin'   : 'plugin.video.sedundnes',
		'saved'    : 'allucnotsure',
		'path'     : os.path.join(ADDONS, 'plugin.video.sedundnes'),
		'icon'     : os.path.join(ADDONS, 'plugin.video.sedundnes', 'icon.png'),
		'fanart'   : os.path.join(ADDONS, 'plugin.video.sedundnes', 'fanart.jpg'),
		'file'     : os.path.join(ALLUCFOLD, 'notsure_alluc'),
		'settings' : os.path.join(ADDOND, 'plugin.video.sedundnes', 'settings.xml'),
		'default'  : '',
		'data'     : ['alluc.api'],
		'activate' : ''},
	'covenant': {
		'name'     : 'Covenant',
		'plugin'   : 'plugin.video.covenant',
		'saved'    : 'alluccovenant',
		'path'     : os.path.join(ADDONS, 'plugin.video.covenant'),
		'icon'     : os.path.join(ADDONS, 'plugin.video.covenant', 'icon.png'),
		'fanart'   : os.path.join(ADDONS, 'plugin.video.covenant', 'fanart.jpg'),
		'file'     : os.path.join(ALLUCFOLD, 'covenant_alluc'),
		'settings' : os.path.join(ADDOND, 'plugin.video.covenant', 'settings.xml'),
		'default'  : '',
		'data'     : ['alluc.api'],
		'activate' : ''},
	'bennu': {
		'name'     : 'BENNU ',
		'plugin'   : 'plugin.video.bennu',
		'saved'    : 'allucbennu',
		'path'     : os.path.join(ADDONS, 'plugin.video.bennu'),
		'icon'     : os.path.join(ADDONS, 'plugin.video.bennu', 'icon.png'),
		'fanart'   : os.path.join(ADDONS, 'plugin.video.bennu', 'fanart.jpg'),
		'file'     : os.path.join(ALLUCFOLD, 'bennu_alluc'),
		'settings' : os.path.join(ADDOND, 'plugin.video.bennu', 'settings.xml'),
		'default'  : '',
		'data'     : ['alluc.api'],
		'activate' : ''},
	'specto': {
		'name'     : 'Specto',
		'plugin'   : 'plugin.video.specto',
		'saved'    : 'allucspecto',
		'path'     : os.path.join(ADDONS, 'plugin.video.specto'),
		'icon'     : os.path.join(ADDONS, 'plugin.video.specto', 'icon.png'),
		'fanart'   : os.path.join(ADDONS, 'plugin.video.specto', 'fanart.jpg'),
		'file'     : os.path.join(ALLUCFOLD, 'specto_alluc'),
		'settings' : os.path.join(ADDOND, 'plugin.video.specto', 'settings.xml'),
		'default'  : 'alluc_user',
		'data'     : ['alluc_user', 'alluc_password'],
		'activate' : ''},
	'deathstreams': {
		'name'     : 'Death Streams',
		'plugin'   : 'plugin.video.blamo',
		'saved'    : 'allucdeathstreams',
		'path'     : os.path.join(ADDONS, 'plugin.video.blamo'),
		'icon'     : os.path.join(ADDONS, 'plugin.video.blamo', 'icon.png'),
		'fanart'   : os.path.join(ADDONS, 'plugin.video.blamo', 'fanart.jpg'),
		'file'     : os.path.join(ALLUCFOLD, 'deathstreams_alluc'),
		'settings' : os.path.join(ADDOND, 'plugin.video.blamo', 'settings.xml'),
		'default'  : 'alluc.com-username',
		'data'     : ['alluc.com-enable', 'alluc.com-username', 'alluc.com-password', 'alluc.com-base_url', 'alluc.com_last_results'],
		'activate' : ''}
}

def allucUser(who):
	user=None
	if ALLUCID[who]:
		if os.path.exists(ALLUCID[who]['path']):
			try:
				add = wiz.addonId(ALLUCID[who]['plugin'])
				user = add.getSetting(ALLUCID[who]['default'])
			except:
				pass
	return user

def allucIt(do, who):
	if not os.path.exists(ADDONDATA): os.makedirs(ADDONDATA)
	if not os.path.exists(ALLUCFOLD):  os.makedirs(ALLUCFOLD)
	if who == 'all':
		for log in ORDER:
			if os.path.exists(ALLUCID[log]['path']):
				try:
					addonid   = wiz.addonId(ALLUCID[log]['plugin'])
					default   = ALLUCID[log]['default']
					user      = addonid.getSetting(default)
					if user == '' and do == 'update': continue
					updateAlluc(do, log)
				except: pass
			else: wiz.log('[Alluc Data] %s(%s) is not installed' % (ALLUCID[log]['name'],ALLUCID[log]['plugin']), xbmc.LOGERROR)
		wiz.setS('alluclastsave', str(THREEDAYS))
	else:
		if ALLUCID[who]:
			if os.path.exists(ALLUCID[who]['path']):
				updateAlluc(do, who)
		else: wiz.log('[Alluc Data] Invalid Entry: %s' % who, xbmc.LOGERROR)

def clearSaved(who, over=False):
	if who == 'all':
		for alluc in ALLUCID:
			clearSaved(alluc,  True)
	elif ALLUCID[who]:
		file = ALLUCID[who]['file']
		if os.path.exists(file):
			os.remove(file)
			wiz.LogNotify('[COLOR %s]%s[/COLOR]' % (COLOR1, ALLUCID[who]['name']),'[COLOR %s]Alluc Data: Removed![/COLOR]' % COLOR2, 2000, ALLUCID[who]['icon'])
		wiz.setS(ALLUCID[who]['saved'], '')
	if over == False: wiz.refresh()

def updateAlluc(do, who):
	file      = ALLUCID[who]['file']
	settings  = ALLUCID[who]['settings']
	data      = ALLUCID[who]['data']
	addonid   = wiz.addonId(ALLUCID[who]['plugin'])
	saved     = ALLUCID[who]['saved']
	default   = ALLUCID[who]['default']
	user      = addonid.getSetting(default)
	suser     = wiz.getS(saved)
	name      = ALLUCID[who]['name']
	icon      = ALLUCID[who]['icon']

	if do == 'update':
		if not user == '':
			try:
				with open(file, 'w') as f:
					for alluc in data: 
						f.write('<alluc>\n\t<id>%s</id>\n\t<value>%s</value>\n</alluc>\n' % (alluc, addonid.getSetting(alluc)))
					f.close()
				user = addonid.getSetting(default)
				wiz.setS(saved, user)
				wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, name), '[COLOR %s]Alluc Data: Saved![/COLOR]' % COLOR2, 2000, icon)
			except Exception, e:
				wiz.log("[Alluc Data] Unable to Update %s (%s)" % (who, str(e)), xbmc.LOGERROR)
		else: wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, name), '[COLOR %s]Alluc Data: Not Registered![/COLOR]' % COLOR2, 2000, icon)
	elif do == 'restore':
		if os.path.exists(file):
			f = open(file,mode='r'); g = f.read().replace('\n','').replace('\r','').replace('\t',''); f.close();
			match = re.compile('<alluc><id>(.+?)</id><value>(.+?)</value></alluc>').findall(g)
			try:
				if len(match) > 0:
					for alluc, value in match:
						addonid.setSetting(alluc, value)
				user = addonid.getSetting(default)
				wiz.setS(saved, user)
				wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, name), '[COLOR %s]Alluc: Restored![/COLOR]' % COLOR2, 2000, icon)
			except Exception, e:
				wiz.log("[Alluc Data] Unable to Restore %s (%s)" % (who, str(e)), xbmc.LOGERROR)
		#else: wiz.LogNotify(name,'Alluc Data: [COLOR red]Not Found![/COLOR]', 2000, icon)
	elif do == 'clearaddon':
		wiz.log('%s SETTINGS: %s' % (name, settings), xbmc.LOGDEBUG)
		if os.path.exists(settings):
			try:
				f = open(settings, "r"); lines = f.readlines(); f.close()
				f = open(settings, "w")
				for line in lines:
					match = wiz.parseDOM(line, 'setting', ret='id')
					if len(match) == 0: f.write(line)
					else:
						if match[0] not in data: f.write(line)
						else: wiz.log('Removing Line: %s' % line, xbmc.LOGNOTICE)
				f.close()
				wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, name),'[COLOR %s]Addon Data: Cleared![/COLOR]' % COLOR2, 2000, icon)
			except Exception, e:
				wiz.log("[Trakt Data] Unable to Clear Addon %s (%s)" % (who, str(e)), xbmc.LOGERROR)
	wiz.refresh()

def autoUpdate(who):
	if who == 'all':
		for log in ALLUCID:
			if os.path.exists(ALLUCID[log]['path']):
				autoUpdate(log)
	elif ALLUCID[who]:
		if os.path.exists(ALLUCID[who]['path']):
			u  = allucUser(who)
			su = wiz.getS(ALLUCID[who]['saved'])
			n = ALLUCID[who]['name']
			if u == None or u == '': return
			elif su == '': allucIt('update', who)
			elif not u == su:
				if DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like to save the [COLOR %s]Alluc[/COLOR] data for [COLOR %s]%s[/COLOR]?" % (COLOR2, COLOR1, COLOR1, n), "Addon: [COLOR green][B]%s[/B][/COLOR]" % u, "Saved:[/COLOR] [COLOR red][B]%s[/B][/COLOR]" % su if not su == '' else 'Saved:[/COLOR] [COLOR red][B]None[/B][/COLOR]', yeslabel="[B][COLOR green]Save Data[/COLOR][/B]", nolabel="[B][COLOR red]No Cancel[/COLOR][/B]"):
					allucIt('update', who)
			else: allucIt('update', who)

def importlist(who):
	if who == 'all':
		for log in ALLUCID:
			if os.path.exists(ALLUCID[log]['file']):
				importlist(log)
	elif ALLUCID[who]:
		if os.path.exists(ALLUCID[who]['file']):
			d  = ALLUCID[who]['default']
			sa = ALLUCID[who]['saved']
			su = wiz.getS(sa)
			n  = ALLUCID[who]['name']
			f  = open(ALLUCID[who]['file'],mode='r'); g = f.read().replace('\n','').replace('\r','').replace('\t',''); f.close();
			m  = re.compile('<alluc><id>%s</id><value>(.+?)</value></alluc>' % d).findall(g)
			if len(m) > 0:
				if not m[0] == su:
					if DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like to import the [COLOR %s]Alluc[/COLOR] data for [COLOR %s]%s[/COLOR]?" % (COLOR2, COLOR1, COLOR1, n), "File: [COLOR green][B]%s[/B][/COLOR]" % m[0], "Saved:[/COLOR] [COLOR red][B]%s[/B][/COLOR]" % su if not su == '' else 'Saved:[/COLOR] [COLOR red][B]None[/B][/COLOR]', yeslabel="[B][COLOR green]Save Data[/COLOR][/B]", nolabel="[B][COLOR red]No Cancel[/COLOR][/B]"):
						wiz.setS(sa, m[0])
						wiz.log('[Import Data] %s: %s' % (who, str(m)), xbmc.LOGNOTICE)
					else: wiz.log('[Import Data] Declined Import(%s): %s' % (who, str(m)), xbmc.LOGNOTICE)
				else: wiz.log('[Import Data] Duplicate Entry(%s): %s' % (who, str(m))), xbmc.LOGNOTICE
			else: wiz.log('[Import Data] No Match(%s): %s' % (who, str(m)), xbmc.LOGNOTICE)

def activateAlluc(who):
	if ALLUCID[who]:
		if os.path.exists(ALLUCID[who]['path']): 
			act     = ALLUCID[who]['activate']
			addonid = wiz.addonId(ALLUCID[who]['plugin'])
			if act == '': addonid.openSettings()
			else: url = xbmc.executebuiltin(ALLUCID[who]['activate'])
		else: DIALOG.ok(ADDONTITLE, '%s is not currently installed.' % ALLUCID[who]['name'])
	else: 
		wiz.refresh()
		return
	check = 0
	while allucUser(who) == None:
		if check == 30: break
		check += 1
		time.sleep(10)
	wiz.refresh()