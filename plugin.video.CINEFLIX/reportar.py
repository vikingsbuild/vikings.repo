import subprocess
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmc

site = "http://www.vidatv.xyz"

def report():
    osWin = xbmc.getCondVisibility('system.platform.windows')
    osOsx = xbmc.getCondVisibility('system.platform.osx')
    osLinux = xbmc.getCondVisibility('system.platform.linux')
    osAndroid = xbmc.getCondVisibility('system.platform.linux')

    if osWin:
         subprocess.call(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",""+site+""])
    if  osAndroid:
        cmd = 'StartAndroidActivity(com.android.chrome,android.intent.action.VIEW,,'+site+')'
        xbmc.executebuiltin(cmd)
    if  osLinux:
       subprocess.call(["/usr/bin/google-chrome",""+site+""])
    if osOsx:
        r = subprocess.call(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",""+site+""])


       

