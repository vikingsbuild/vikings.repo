########################################
#Kodi Logfile Uploader
#  Original Code by Team Kodi
#    By Surfacingx and Whufclee
#
#  Modified to Support Kodi Forks
#  Added Email Logfile Url Support
########################################

import os
import re
import socket
from urllib import urlencode
from urllib import FancyURLopener
import urllib2
import urlparse
import urllib
import json
import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs

ADDON            = xbmcaddon.Addon(id='plugin.program.totalinstaller')
ADDONID          = ADDON.getAddonInfo('id')
ADDONNAME        = ADDON.getAddonInfo('name')
ADDONVERSION     = ADDON.getAddonInfo('version')
DIALOG           = xbmcgui.Dialog()
LOG              = xbmc.translatePath('special://logpath/')
URL              = 'https://paste.ubuntu.com/'
REPLACES         = (('//.+?:.+?@', '//USER:PASSWORD@'),('<user>.+?</user>', '<user>USER</user>'),('<pass>.+?</pass>', '<pass>PASSWORD</pass>'),)

socket.setdefaulttimeout(5)

def log(text):
	xbmc.log("[Upload Log] %s" % text)

def Grab_Log(old=False):
	finalfile   = 0
	logfilepath = os.listdir(LOG)
	logsfound   = []
	
	for item in logfilepath:
		if old == True and item.endswith('.old.log'): logsfound.append(os.path.join(LOG, item))
		elif old == False and item.endswith('.log') and not item.endswith('.old.log'): logsfound.append(os.path.join(LOG, item))
		
	if len(logsfound) > 0:
		logsfound.sort(key=lambda f: os.path.getmtime(f))
		return logsfound[-1]
	else: 
		return False

# Custom urlopener to set user-agent
class pasteURLopener(FancyURLopener):
	version = '%s: %s' % (ADDONID, ADDONVERSION)

class Main:
	def __init__(self):
		self.getSettings()
		files = self.getFiles()
		for item in files:
			filetype = item[0]
			if filetype == 'log':
				log = Grab_Log().replace(LOG, "")
				name = log if log != False else "kodi.log"
				error = "Error posting the %s file" % name
			elif filetype == 'oldlog':
				log = Grab_Log(True).replace(LOG, "")
				name = log if log != False else "kodi.old.log"
				error = "Error posting the %s file" % name
			elif filetype == 'crashlog':
				name = "crash log"
				error = "Error posting the crashlog file"
			succes, data = self.readLog(item[1])
			if succes:
				content = self.cleanLog(data)
				succes, result = self.postLog(content, name)
				if succes:
					msg = "Post this url for your [COLOR dodgerblue]%s[/COLOR]:[CR][COLOR dodgerblue]%s[/COLOR]" % (name, result)
					if len(self.email) > 5: 
						em_result, em_msg = self.email_Log(self.email, result, name)
						if em_result == 'message':
							msg += "[CR]%s" % em_msg
						else:
							msg += "[CR]Email ERROR: %s" % em_msg
					self.showResult(msg)
				else:
					self.showResult('%s[CR]%s' % (error, result))
			else:
				self.showResult('%s[CR]%s' % (error, result))

	def getSettings(self):
		self.oldlog   = ADDON.getSetting('oldlog') == 'true'
		self.crashlog = ADDON.getSetting('crashlog') == 'true'
		self.email    = ADDON.getSetting('email')

	def getFiles(self):
		logfiles = []
		log = Grab_Log()
		old = Grab_Log(True)
		if log != False:
			if os.path.exists(log): logfiles.append(['log', log])
			else: self.showResult("No log file found")
		else: self.showResult("No log file found")
		if self.oldlog:
			if old != False:
				if os.path.exists(old): logfiles.append(['oldlog', old])
				else: self.showResult("No old log file found")
			else: self.showResult("No old log file found")
		if self.crashlog:
			crashlog_path = ''
			items = []
			if xbmc.getCondVisibility('system.platform.osx'):
				crashlog_path = os.path.join(os.path.expanduser('~'), 'Library/Logs/DiagnosticReports/')
				filematch = 'Kodi'
			elif xbmc.getCondVisibility('system.platform.ios'):
				crashlog_path = '/var/mobile/Library/Logs/CrashReporter/'
				filematch = 'Kodi'
			elif xbmc.getCondVisibility('system.platform.linux'):
				crashlog_path = os.path.expanduser('~') # not 100% accurate (crashlogs can be created in the dir kodi was started from as well)
				filematch = 'kodi_crashlog'
			elif xbmc.getCondVisibility('system.platform.windows'):
				log("Windows crashlogs are not supported, please disable this option in the addon settings")
				#self.showResult("Windows crashlogs are not supported, please disable this option in the addon settings")
			elif xbmc.getCondVisibility('system.platform.android'):
				log("Android crashlogs are not supported, please disable this option in the addon settings")
				#self.showResult("Android crashlogs are not supported, please disable this option in the addon settings")
			if crashlog_path and os.path.isdir(crashlog_path):
				dirs, files = xbmcvfs.listdir(crashlog_path)
				for item in files:
					if filematch in item and os.path.isfile(os.path.join(crashlog_path, item)):
						items.append(os.path.join(crashlog_path, item))
						items.sort(key=lambda f: os.path.getmtime(f))
						lastcrash = items[-1]
						logfiles.append(['crashlog', lastcrash])
			if len(items) == 0:
				log("No crashlog file found")
		return logfiles

	def readLog(self, path):
		try:
			lf = xbmcvfs.File(path)
			content = lf.read()
			lf.close()
			if content:
				return True, content
			else:
				log('file is empty')
				return False, "File is Empty"
		except:
			log('unable to read file')
			return False, "Unable to Read File"

	def cleanLog(self, content):
		for pattern, repl in REPLACES:
			content = re.sub(pattern, repl, content)
			return content

	def postLog(self, data, name):
		params = {}
		params['poster'] = 'kodi'
		params['content'] = data
		params['syntax'] = 'text'
		params = urlencode(params)

		url_opener = pasteURLopener()

		try:
			page = url_opener.open(URL, params)
		except:
			e = 'failed to connect to the server'
			log(e)
			return False, e

		try:
			page_url = page.url.strip()
			log("URL for %s: %s" % (name, page_url))
			return True, page_url
		except:
			e = 'unable to retrieve the paste url'
			log(e)
			return False, e
			
	def email_Log(self, email, results, file):
		URL = 'http://aftermathwizard.net/mail_logs.php'
		data = {'email': email, 'results': results, 'file': file, 'wizard': "Community Portal"}
		params = urlencode(data)
		url_opener = pasteURLopener()
		try:
			result     = url_opener.open(URL, params)
			returninfo = result.read()
			log(str(returninfo))
		except:
			e = 'failed to connect to the server'
			log(e)
			return False, e
		try:
			js_data = json.loads(returninfo)
			if 'type' in js_data:
				return js_data['type'], str(js_data['text'])
			else: return str(js_data)
		except Exception as e:
			log("ERROR: "+ str(e))
		return "Error Sending Email."

	def showResult(self, message):
		log("%s: %s" % (ADDONNAME, message))
		confirm = DIALOG.ok(ADDONNAME, message)

if ( __name__ == '__main__' ):
	Main()
