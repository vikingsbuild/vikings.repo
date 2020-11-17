##=======================
## Vikings Wizard
##=======================
import xbmc,xbmcaddon,xbmcgui,xbmcplugin,os,sys,shutil,urllib,re

import installer
import common

AddonID = 'plugin.program.VikingsThemas'
ADDON=xbmcaddon.Addon(id='plugin.program.VikingsThemas')
AddonTitle = "[COLOR aqua]Vikings Kodi Wizard[/COLOR]"
ADDONPATH = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID))
HOME =  xbmc.translatePath('special://home/')  
VERSION = xbmcaddon.Addon().getAddonInfo('version')
PATH = xbmcaddon.Addon().getAddonInfo('name')
KODIVERSION  = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
dialog = xbmcgui.Dialog() 
	
def CATEGORIES():     
    if KODIVERSION <= 16.0:
        dialog.ok(AddonTitle,'Por favor, atualizar o seu sistema Kodi!','','')
        return
    else: 
    
	if KODIVERSION >= 17.0:	
	   WIZARDURL = "https://pastebin.com/raw/kjKBV5AG"
	
    if KODIVERSION >= 18.0:
        dialog.ok(AddonTitle,'Nada para atualizar!','','')
        return
    else: 
    
	link = common.OPEN_URL(WIZARDURL).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        common.addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')

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
fanart=None
description=None

try:
        url=urllib.unquote_plus(params["url"])
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
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass

print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )
        
        
if mode==None or url==None or len(url)<1:
        CATEGORIES()
       
elif mode==1:
        installer.WIZARD(name,url,description)

xbmcplugin.endOfDirectory(int(sys.argv[1]))