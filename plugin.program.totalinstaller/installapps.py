import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os, base64, sys, xbmcvfs
import shutil
import urllib2, urllib
import re
import extract
import downloader
import time



USER_AGENT 			= 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
ADDON_ID 			= 'plugin.program.totalinstaller'
ADDON 				= xbmcaddon.Addon(id=ADDON_ID)
ADDON_TITLE			= "Community Portal"
dialog				= xbmcgui.Dialog()
ADDON_TITLE3 		= "[COLOR=dodgerblue]C[/COLOR][COLOR ghostwhite]ommunity[/COLOR] [COLOR=dodgerblue]P[/COLOR][COLOR ghostwhite]ortal[/COLOR] [COLOR=dodgerblue]F[/COLOR][COLOR ghostwhite]ile[/COLOR] [COLOR=dodgerblue]C[/COLOR][COLOR ghostwhite]leaner[/COLOR]"
U 					= ADDON.getSetting('User')
FANART 				= xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'fanart.jpg'))
FANART1 			= xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'resources/art/fanart/fanart1.jpg'))
FANART2 			= xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'resources/art/fanart/fanart2.jpg'))
FANART3 			= xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'resources/art/fanart/fanart3.jpg'))
FANART_EMULATORS    = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'resources/art/emulators.png'))
ICON 				= xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID, 'icon1.png'))
ART 				= xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/art/android/'))
ART1 				= xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/art/windows/'))
ART2 				= xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/art/linux/'))
VERSION 			= "0.0.1"
DBPATH 				= xbmc.translatePath('special://database')
TNPATH 				= xbmc.translatePath('special://thumbnails');
PATH 				= "Kobra Wizard"            
BASEURL			    = "http://kodicustombuilds.com/builds"
BASEURL1 			= "http://kodicustombuilds.com/builds"
BASEURL2 			= "http://kodicustombuilds.com/test"
HOME 				= xbmc.translatePath('special://home/')
ADDONS 				= os.path.join(HOME,     'addons')
PACKAGES 			= os.path.join(ADDONS,   'packages')
H 					= 'http://' 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#################
#### INDEX 1 ####
#################

def INDEX1():
    if xbmc.getCondVisibility("System.Platform.Android"):
       BUILDMENU()
    #if xbmc.getCondVisibility("System.Platform.Windows"):   
       #BUILDMENU1()
    #if xbmc.getCondVisibility("System.Platform.Linux"):
       #COMINGSOONLINUX()
    #if xbmc.getCondVisibility("System.Platform.Darwin"):
       #COMINGSOONLINUX()
    addDir('[COLOR=dodgerblue]R[/COLOR][COLOR ghostwhite]equests[/COLOR]',BASEURL,13,ART+'requests.png',FANART3,'')
    setView('list', 'MAIN')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
######################
#### ANDROID MENU ####
######################

def BUILDMENU():
    addDir('[COLOR=dodgerblue]A[/COLOR][COLOR ghostwhite]pks[/COLOR]',BASEURL,6,ART+'apps3.png',FANART,'')
    addDir('[COLOR=dodgerblue]E[/COLOR][COLOR ghostwhite]mulators[/COLOR]',BASEURL,7,ART+'emulators3.png',FANART,'')
    addDir('[COLOR=dodgerblue]R[/COLOR][COLOR ghostwhite]oms[/COLOR]',BASEURL,99,ART+'roms3.png',FANART,'')
    #addDir('[COLOR=dodgerblue]A[/COLOR][COLOR ghostwhite]dult[/COLOR] [COLOR=dodgerblue]A[/COLOR][COLOR ghostwhite]pks[/COLOR]',BASEURL,9,ART+'adult.png',FANART,'')
    setView('list', 'MAIN')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
######################
#### WINDOWS MENU ####
######################
		
def BUILDMENU1():
    addDir('[COLOR=dodgerblue]P[/COLOR][COLOR ghostwhite]rograms[/COLOR]',BASEURL,98,ART1+'programs.png',FANART,'')
    addDir("[COLOR=dodgerblue]I[/COLOR][COLOR ghostwhite]so's[/COLOR]",BASEURL,98,ART1+'isos.png',FANART,'')
    setView('list', 'MAIN')
	
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------		
################
### APPS URL ###
################

def APPSWIZARD():
    link = OPEN_URL('http://kobracustombuilds.com/apks/wizard/wizard.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,5,iconimage,fanart,description)
    setView('list', 'MAIN')
	
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
######################
### ADULT APPS URL ###
######################

def APPSWIZARD1():
    link = OPEN_URL('http://kobracustombuilds.com/adult/wizard/wizard.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,10,iconimage,fanart,description)
    setView('list', 'MAIN')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
#####################
### EMULATORS URL ###
#####################

def EMULATORWIZARD():
    link = OPEN_URL('http://kobracustombuilds.com/emulators/wizard/wizard.txt').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,8,iconimage,fanart,description)
    setView('list', 'MAIN')
	
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#################################
####### POPUP TEXT BOXES ########
#################################

def TextBoxes(heading,announce):
  class TextBox():
    WINDOW=10147
    CONTROL_LABEL=1
    CONTROL_TEXTBOX=5
    def __init__(self,*args,**kwargs):
      xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
      self.win=xbmcgui.Window(self.WINDOW) # get window
      xbmc.sleep(500) # give window time to initialize
      self.setControls()
    def setControls(self):
      self.win.getControl(self.CONTROL_LABEL).setLabel(heading) # set heading
      try: f=open(announce); text=f.read()
      except: text=announce
      self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
      return
  TextBox()   
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
############################
#### APPS INSTALL ##########
############################
# THANKS TO ][NT3L][G3NC][ #
############################

def APPINSTALL(name,url,description):
   confirm=xbmcgui.Dialog()
   if confirm.yesno('[COLOR=dodgerblue]%s[/COLOR]' % name,description,"","","Go back","Download"):
    downloadpath = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR=dodgerblue]C[/COLOR][COLOR ghostwhite]ommunity[/COLOR] [COLOR=dodgerblue]P[/COLOR][COLOR ghostwhite]ortal[/COLOR] [COLOR=dodgerblue]A[/COLOR][COLOR ghostwhite]pk[/COLOR] [COLOR=dodgerblue]I[/COLOR][COLOR ghostwhite]nstaller[/COLOR]","Downloading",name,'Please wait...')
    lib=os.path.join(downloadpath, name+'.apk')
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=dodgerblue]C[/COLOR][COLOR ghostwhite]ommunity[/COLOR] [COLOR=dodgerblue]P[/COLOR][COLOR ghostwhite]ortal[/COLOR] [COLOR=dodgerblue]A[/COLOR][COLOR ghostwhite]pk[/COLOR] [COLOR=dodgerblue]I[/COLOR][COLOR ghostwhite]nstaller[/COLOR]","Download complete.","","Click [B]OK[/B] to install " + name + "")
	#][NT3L]I[G3NC][# 
    xbmc.executebuiltin('StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:'+lib+'")')
    time.sleep(4)
    CLEANUP()
    dialog.ok("[COLOR=dodgerblue]C[/COLOR][COLOR ghostwhite]ommunity[/COLOR] [COLOR=dodgerblue]P[/COLOR][COLOR ghostwhite]ortal[/COLOR] [COLOR=dodgerblue]A[/COLOR][COLOR ghostwhite]pk[/COLOR] [COLOR=dodgerblue]I[/COLOR][COLOR ghostwhite]nstaller[/COLOR]","Application installed [COLOR lime]successfully[/COLOR]"," ","Please click [B]OK[/B] to continue")
    try: os.remove(lib)
    except: pass

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
#########################
### EMULATOR INSTALL ####
#########################

def EMULATORINSTALL(name,url,description):
   confirm=xbmcgui.Dialog()
   if confirm.yesno('[COLOR=dodgerblue]%s[/COLOR]' % name,description,"","","Go back","Download"):
    downloadpath = xbmc.translatePath(os.path.join('special://home/addons','packages'))#
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR=dodgerblue]C[/COLOR][COLOR ghostwhite]ommunity[/COLOR] [COLOR=dodgerblue]P[/COLOR][COLOR ghostwhite]ortal[/COLOR] [COLOR=dodgerblue]E[/COLOR][COLOR ghostwhite]mulator[/COLOR] [COLOR=dodgerblue]I[/COLOR][COLOR ghostwhite]nstaller[/COLOR]","Downloading",name,'Please wait...')
    lib=os.path.join(downloadpath, name+'.apk')
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=dodgerblue]C[/COLOR][COLOR ghostwhite]ommunity[/COLOR] [COLOR=dodgerblue]P[/COLOR][COLOR ghostwhite]ortal[/COLOR] [COLOR=dodgerblue]E[/COLOR][COLOR ghostwhite]mulator[/COLOR] [COLOR=dodgerblue]I[/COLOR][COLOR ghostwhite]nstaller[/COLOR]","Download complete.","","Click [B]OK[/B] to install " + name + "")
	#][NT3L]I[G3NC][# 
    xbmc.executebuiltin('StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:'+lib+'")')
    time.sleep(4)
    CLEANUP()
    dialog.ok("[COLOR=dodgerblue]C[/COLOR][COLOR ghostwhite]ommunity[/COLOR] [COLOR=dodgerblue]P[/COLOR][COLOR ghostwhite]ortal[/COLOR] [COLOR=dodgerblue]E[/COLOR][COLOR ghostwhite]mulator[/COLOR] [COLOR=dodgerblue]I[/COLOR][COLOR ghostwhite]nstaller[/COLOR]","Emulator installed [COLOR lime]successfully[/COLOR]"," ","Please click [B]OK[/B] to continue")
    try: os.remove(lib)
    except: pass
	
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
##########################
### ADULT APP INSTALL ####
##########################

def ADULTINSTALL(name,url,description):
   confirm=xbmcgui.Dialog()
   if confirm.yesno('[COLOR=dodgerblue]%s[/COLOR]' % name,description,"","","Go back","Download"):
    downloadpath = xbmc.translatePath(os.path.join('special://home/addons','packages'))#
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR=dodgerblue]C[/COLOR][COLOR dodgerblue]ommunity[/COLOR] [COLOR=dodgerblue]P[/COLOR][COLOR dodgerblue]ortal[/COLOR] [COLOR=dodgerblue]A[/COLOR][COLOR dodgerblue]pk[/COLOR] [COLOR=dodgerblue]I[/COLOR][COLOR dodgerblue]nstaller[/COLOR]","Dowloading",name,'Please wait...')
    lib=os.path.join(downloadpath, name+'.apk')
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=dodgerblue]C[/COLOR][COLOR dodgerblue]ommunity[/COLOR] [COLOR=dodgerblue]P[/COLOR][COLOR dodgerblue]ortal[/COLOR] [COLOR=dodgerblue]A[/COLOR][COLOR dodgerblue]pk[/COLOR] [COLOR=dodgerblue]I[/COLOR][COLOR dodgerblue]nstaller[/COLOR]","Download complete.","","Click [B]OK[/B] to install " + name + "")
	#][NT3L]I[G3NC][# 
    xbmc.executebuiltin('StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:'+lib+'")')
    time.sleep(4)
    CLEANUP()
    dialog.ok("[COLOR=dodgerblue]C[/COLOR][COLOR dodgerblue]ommunity[/COLOR] [COLOR=dodgerblue]P[/COLOR][COLOR dodgerblue]ortal[/COLOR] [COLOR=dodgerblue]A[/COLOR][COLOR dodgerblue]pk[/COLOR] [COLOR=dodgerblue]I[/COLOR][COLOR dodgerblue]nstaller[/COLOR]","Application installed [COLOR lime]successfully[/COLOR]"," ","Please click [B]OK[/B] to continue")
    try: os.remove(lib)
    except: pass
	
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
################################
###### CLEAN UP PACKAGES #######
##### THANKS GUYS @ XUNITY ##### 
##### MODDED BY AFTERMATH ######
################################
		
def CLEANUP():
	if os.path.exists(PACKAGES):
		try:	
			for root, dirs, files in os.walk(PACKAGES):
				file_count = 0
				file_count += len(files)
				# Count files and give option to delete
				if file_count > 0:
					if dialog.yesno("[COLOR=dodgerblue]C[/COLOR][COLOR ghostwhite]ommunity[/COLOR] [COLOR=dodgerblue]P[/COLOR][COLOR ghostwhite]ortal[/COLOR] [COLOR=dodgerblue]F[/COLOR][COLOR ghostwhite]ile[/COLOR] [COLOR=dodgerblue]C[/COLOR][COLOR ghostwhite]leaner[/COLOR]", str(file_count) + " File(s) found","","Would you like to delete the package file(s)?", nolabel='No, cancel',yeslabel='Yes, delete'):
						for f in files:	os.unlink(os.path.join(root, f))
						for d in dirs: shutil.rmtree(os.path.join(root, d))
						dialog.ok(ADDON_TITLE3,'Clean up files: [COLOR lime] Success[/COLOR]!')
				else: dialog.ok(ADDON_TITLE3,'Clean up files: [COLOR red]None found[/COLOR]!')
		except: dialog.ok(ADDON_TITLE3,'Clean up files: [COLOR red] Error[/COLOR]!')
	else: dialog.ok(ADDON_TITLE3,'Clean up files: [COLOR red] None found[/COLOR]!')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
################
### REQUESTS ###
################

def REQUESTS():
    dialog.ok("[COLOR=dodgerblue]C[/COLOR][COLOR ghostwhite]ommunity[/COLOR] [COLOR=dodgerblue]P[/COLOR][COLOR ghostwhite]ortal[/COLOR]","Please send any package requests to:","[COLOR dodgerblue][COLOR=dodgerblue]F[/COLOR][COLOR dodgerblue]ace[/COLOR]book[/COLOR]: https://www.facebook.com/groups/KodiCustomBuilds/","[COLOR dodgerblue][COLOR=dodgerblue]F[/COLOR][COLOR dodgerblue]ace[/COLOR]book[/COLOR]: https://www.facebook.com/profile.php?id=100011845114961[/COLOR]")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###################
### COMING SOON ###
###################
	
def COMINGSOONWINDOWS():
    addDir('Coming soon...',BASEURL,0,ART1+'comingsoon4.png',FANART1,'')
    setView('movies', 'MAIN')
	
def COMINGSOONANDROID():
    addDir('Coming soon...',BASEURL,0,ART+'comingsoon3.png',FANART,'')
    setView('movies', 'MAIN')

def COMINGSOONLINUX():
    addDir('Coming soon...',BASEURL,0,ART2+'comingsoon5.png',FANART2,'')
    setView('movies', 'MAIN')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
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

N = base64.decodestring('')
T = base64.decodestring('L2FkZG9ucy50eHQ=')
B = base64.decodestring('')
F = base64.decodestring('')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==5 or mode==8  or mode==10 or mode==11 or mode==13:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
                      
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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
# THIS FUCKER HERE IS THE CULPRIT.
# BECAUSE THE MODE IS NONE IN DEFAULT.PY IT ALSO PICKS IT UP IN HERE AND ADDS THAT DIRECTORY

#if mode==None or url==None or len(url)<1:
#        INDEX1()

if mode==  2		 :BUILDMENU()
		
elif mode==5         :APPINSTALL(name,url,description)
		
elif mode==6         :APPSWIZARD()
		
elif mode==7         :EMULATORWIZARD()

elif mode==8      	 :EMULATORINSTALL(name,url,description)
		
elif mode==9    	 :APPSWIZARD1()

elif mode==10        :ADULTINSTALL(name,url,description)
		
elif mode==12        :BUILDMENU1()
		
elif mode==13        :REQUESTS()		
		
elif mode==97     	 :COMINGSOONLINUX()
		
elif mode==98        :COMINGSOONWINDOWS()
		
elif mode==99     	 :COMINGSOONANDROID()


