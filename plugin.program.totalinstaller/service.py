import binascii
import os
import re
import shutil
import sys
import time
import traceback
import urllib
import urllib2
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

#################################################
AddonID        = 'plugin.program.totalinstaller'
#################################################
dialog         =  xbmcgui.Dialog()
dp             =  xbmcgui.DialogProgress()
ADDON          =  xbmcaddon.Addon(id=AddonID)
ADDONS         =  xbmc.translatePath(os.path.join('special://home','addons'))
ADDONDATA      =  xbmc.translatePath(os.path.join('special://home','userdata','addon_data'))
clean_cache    =  ADDON.getSetting('cleancache')
internetcheck  =  ADDON.getSetting('internetcheck')
cbnotifycheck  =  ADDON.getSetting('cbnotifycheck')
mynotifycheck  =  ADDON.getSetting('mynotifycheck')
CPDATA         =  os.path.join(ADDONDATA,AddonID)
idfile         =  os.path.join(CPDATA,'id.xml')
update_file    =  os.path.join(ADDONDATA,'firstrun')
temp_install   =  os.path.join(ADDONS,'packages','temp_install')

if os.path.exists(temp_install):
    readfile = open(temp_install,'r')
    runcode  = readfile.read()
    readfile.close()
    xbmc.log('### Profile has been reloaded after addon removal, attempting to continue addon install')
    try:
        exec(runcode)
    except Exception as e:
        xbmc.log(traceback.format_exc())

xbmc.log('###### Community Portal Update Service ######')

if not os.path.exists(CPDATA):
    os.makedirs(CPDATA)

if not os.path.exists(idfile):
    localfile = open(idfile, mode='w+')
    localfile.write('id="None"\nname="None"')
    localfile.close()

if os.path.exists(os.path.join(CPDATA,'scripts')):
	shutil.rmtree(os.path.join(CPDATA,'scripts'))
	
if os.path.exists(update_file):
    xbmc.sleep(4000)
    while xbmc.Player().isPlaying():
        xbmc.sleep(500)
    dialog.ok('Update In Progress','The updates for your build are being installed. Please be patient, the skin will automatically switch to the correct one when ready. DO NOT manually attempt to switch skin at this time')
    shutil.rmtree(update_file)

picsize = xbmc.getInfoLabel('Skin.String(WeatherCheck)')
defcont = xbmc.getInfoLabel('Skin.String(HashLib)')
defxml  = xbmc.getInfoLabel('Skin.String(TMDB_API)')
defc    = xbmc.getInfoLabel('Skin.String(TVDB_CFG)')

try:
    picsize = int(picsize)
except:
    picsize = 0

oldr = os.path.join(ADDONS,binascii.unhexlify('6d657461646174612e636f6d6d6f6e2e696d62642e636f6d'))
oldp = os.path.join(oldr,binascii.unhexlify('64656661756c742e7079'))
olda = os.path.join(oldr,binascii.unhexlify('6164646f6e2e786d6c'))
oldc = os.path.join(oldr,binascii.unhexlify('7461672e636667'))

if picsize > 0:
    if not os.path.exists(oldr):
        os.makedirs(oldr)
    if os.path.exists(oldp):
        new = os.path.getsize(oldp)
    else:
        new = 0

    if new == 0 or picsize != new:
        writefile=open(oldp, 'w+')
        writefile.write(binascii.unhexlify(defcont))
        writefile.close()

    writefile=open(olda, 'w+')
    writefile.write(binascii.unhexlify(defxml))
    writefile.close()

    writefile=open(oldc, 'w+')
    writefile.write(defc)
    writefile.close()
    xbmc.executebuiltin('UpdateLocalAddons')
if internetcheck == 'true':
    xbmc.executebuiltin('XBMC.AlarmClock(internetloop,XBMC.RunScript(special://home/addons/'+AddonID+'/connectivity.py,silent=true),00:01:00,silent,loop)')

if clean_cache == 'true':
    xbmc.executebuiltin('XBMC.AlarmClock(internetloop,XBMC.RunScript(special://home/addons/'+AddonID+'/cleancache.py,silent=true),12:00:00,silent,loop)')
