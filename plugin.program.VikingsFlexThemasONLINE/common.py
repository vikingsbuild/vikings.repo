##======================================
## Vikings Themas ONLINE Wizard - Common
##======================================
import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys,urllib,urllib2
from urllib2 import urlopen
import shutil

AddonID = 'plugin.program.VikingsFlexThemasONLINE'
ADDON=xbmcaddon.Addon(id='plugin.program.VikingsFlexThemasONLINE')
ADDONPATH = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID))
HOME =  xbmc.translatePath('special://home/')
dialog = xbmcgui.Dialog()    
VERSION = xbmcaddon.Addon().getAddonInfo('version')
PATH = xbmcaddon.Addon().getAddonInfo('name')
packages = xbmc.translatePath(os.path.join('special://home/addons','packages/'))

##=================
##  Add to menus
#==================
def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok


def addItem(name,url,mode,iconimage,fanart,description):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	liz.setProperty( "Fanart_Image", fanart )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def addDirWTW(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addLink(name, url, mode, iconimage):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode)\
        + "&name=" + urllib.quote_plus(name)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png",
                           thumbnailImage=iconimage)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u,
                                     listitem=liz, isFolder=False)
    return ok


##=====================
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

##=======================
##  DETERMINE PLATFORM
##=======================
def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

##===============================
## FORCE CLOSE KODI
## ANDROID ONLY WORKS IF ROOTED
##===============================
def killxbmc():
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx':
        print "############   try MacOS Force Close  #################"
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        dialog.ok("[COLOR=red][B]ATENCAO  !!![/COLOR][/B]","Se voce esta vendo esta mensagem, significa que o Kodi nao conseguiu encerrar automaticamente. [COLOR yellow][B]Por favor, voce devera forcar o encerramento do Kodi.[/B][/COLOR] [COLOR=lime]JAMAIS [/COLOR] saia pelo menu do KODI.")
    elif myplatform == 'linux':
        print "############   try Linux Force Close  #################"
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        dialog.ok("[COLOR=red][B]ATENCAO  !!![/COLOR][/B]","Se voce esta vendo esta mensagem, significa que o Kodi nao conseguiu encerrar automaticamente. [COLOR yellow][B]Por favor force o encerramento do Kodi.[/B][/COLOR] [COLOR=lime]JAMAIS[/COLOR] saia pelo menu do KODI.")
    elif myplatform == 'android':
        print "############   try Android Force Close  #################"
        try: os.system('adb shell am force-stop org.xbmc.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc.xbmc')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc')
        except: pass                
        dialog.ok("[COLOR=red][B]ATENCAO  !!![/COLOR][/B]", "Seu dispositivo e um Android/Amazon [COLOR=yellow][B]Este tipo de dispositivo, impede o fechamento do KODI automaticamente.[/B][/COLOR] [COLOR=lime]Se for uma Box[/COLOR] simplesmente [COLOR yellow][B]remova o cabo de energia de seu dispositivo[/B][/COLOR] da tomada, e aguarde 15 Sugundos, se for [COLOR green][B]SMARTPHONE[/B][/COLOR] encerre seu KODI pelo gerenciados de Tarefas de seu Dispositivo.")
    elif myplatform == 'windows':
        print "############   try Windows Force Close  #################"
        try:
            os.system('@ECHO off')
            os.system('tskill XBMC.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('tskill Kodi.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im Kodi.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im XBMC.exe /f')
        except: pass
        dialog.ok("[COLOR=red][B]ATENCAO  !!![/COLOR][/B]", "Se voce esta vendo esta mensagem, significa que o Kodi nao conseguiu encerrar automaticamente. [COLOR yellow][B]Por favor force o encerramento do Kodi.[/B][/COLOR] [COLOR=lime]JAMAIS[/COLOR] SAIA DO KODI pelo MENU DE SAIDA. Para isso use o Gerenciador de Tarefas, mas nao NOT ALT-F4")
    elif myplatform == 'ios':
        ## No Force Close for iOS Devices
        dialog.ok("[COLOR=red][B]ATENCAO  !!![/COLOR][/B]", "Se voce esta vendo esta mensagem, significa que o Kodi nao conseguiu encerrar automaticamente. [COLOR yellow][B]from the App Switcher[/B][/COLOR] do seu APP. [COLOR=lime]JAMAIS[/COLOR] SAIA DO KODI pelo MENU DE SAIDA exit menu.")
    else:
        print "############   try Apple TV Force Close  #################"
        try: os.system('killall AppleTV')
        except: pass
        print "############   try Raspbmc Force Close  #################"
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        dialog.ok("[COLOR=red][B]ATENCAO  !!![/COLOR][/B]", "Se voce esta vendo esta mensagem, significa que o Kodi nao conseguiur encerrar automaticamente. [COLOR yellow][B]Please Force Close KODI.[/B][/COLOR] [COLOR=lime]JAMAIS[/COLOR] SAIA DO KODI pelo MENU DE SAIDA. O seu dispositivo e desconhecido, basta desconectar e reconectar o cabo de energia.")      

