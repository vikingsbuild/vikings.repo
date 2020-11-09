import time
import xbmc
import os
import xbmcgui
import xbmcaddon
import urllib2
import webbrowser
import generator


AddonID = xbmcaddon.Addon().getAddonInfo('id')
addon = xbmcaddon.Addon(id=AddonID) 
AddonTitle = addon.getAddonInfo('name')

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        open1,
        open2,
        open3,
        open4,
        )
        
    call = dialog.select('[B][COLOR=blue]INFOTEC IPTV System[/COLOR][/B]', [
    '[B][COLOR=lime]      SITE  [/COLOR][/B][COLOR white] INFOTEC-KODI-ONLINE[/COLOR]', 
    '[B][COLOR=lime]      SITE  [/COLOR][/B][COLOR white] KODI OFFICIAL[/COLOR]',
    '[B][COLOR=lime]      BAIXAR[/COLOR][/B][COLOR orange][B] ADDON ELEMENTUM[/COLOR][/B]',
    '[B][COLOR=lime]      BAIXAR[/COLOR][/B][COLOR orange][B] SCRIPT ELEMENTUM BURST[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item	
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-4]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

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

myplatform = platform()

def open1():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin('StartAndroidActivity(,android.intent.action.VIEW,,%s)' % generator.open('H4sIAHerT18C/8soKSkottLXz8xLyy9JTdbNzk/J1M3Py8nMS9UrT03Ky09J1UvOz9UHAEKxSzYoAAAA'))
    else:
        opensite = webbrowser . open(generator.open('H4sIAHerT18C/8soKSkottLXz8xLyy9JTdbNzk/J1M3Py8nMS9UrT03Ky09J1UvOz9UHAEKxSzYoAAAA'))

def open2():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://kodi.tv/' ) )
    else:
        opensite = webbrowser . open('https://kodi.tv/')
 
def open3():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://github.com/elgatito/plugin.video.elementum/releases/download/v0.1.58/plugin.video.elementum-0.1.58.zip' ) )
    else:
        opensite = webbrowser . open('https://github.com/elgatito/plugin.video.elementum/releases/download/v0.1.58/plugin.video.elementum-0.1.58.zip')

def open4():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://github.com/elgatito/script.elementum.burst/releases/download/v0.0.49/script.elementum.burst-0.0.49.zip' ) )
    else:
        opensite = webbrowser . open('https://github.com/elgatito/script.elementum.burst/releases/download/v0.0.49/script.elementum.burst-0.0.49.zip')		
menuoptions()
