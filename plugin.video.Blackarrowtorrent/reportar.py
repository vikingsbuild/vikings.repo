import subprocess
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmc

doacao = "http://..."
credito = "http://..."
def report():
    osWin = xbmc.getCondVisibility('system.platform.windows')
    osOsx = xbmc.getCondVisibility('system.platform.osx')
    osLinux = xbmc.getCondVisibility('system.platform.linux')
    osAndroid = xbmc.getCondVisibility('system.platform.linux')

    if osWin:
         subprocess.call(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",""+doacao+""])
    if  osAndroid:
        cmd = 'StartAndroidActivity(com.android.chrome,android.intent.action.VIEW,,'+doacao+')'
        xbmc.executebuiltin(cmd)
    if  osLinux:
       subprocess.call(["/usr/bin/google-chrome",""+doacao+""])
    if osOsx:
        r = subprocess.call(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",""+doacao+""])


def credit():
    osWin = xbmc.getCondVisibility('system.platform.windows')
    osOsx = xbmc.getCondVisibility('system.platform.osx')
    osLinux = xbmc.getCondVisibility('system.platform.linux')
    osAndroid = xbmc.getCondVisibility('system.platform.linux')

    if osWin:
         subprocess.call(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",""+credito+""])
    if  osAndroid:
        cmd = 'StartAndroidActivity(com.android.chrome,android.intent.action.VIEW,,'+credito+')'
        xbmc.executebuiltin(cmd)
    if  osLinux:
       subprocess.call(["/usr/bin/google-chrome",""+credit+""])
    if osOsx:
        r = subprocess.call(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",""+credito+""])
       

