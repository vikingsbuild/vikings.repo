# This code is licensed under The GNU General Public License version 2 (GPLv2)
# If you decide to fork this code please obey by the licensing rules.
#
# Thanks go to the-one who initially created the initial speedtest code in early 2014
# That code broke but it didn't take too much to fix it, if you get problems it's most likely
# down to the fact that you need to use another download link that plays nicely with XBMC/Kodi
#
# This is brought to you by noobsandnerds.com, this code originates from the original Total Installer
# If you re-use this code please credit the original authors (the-one and whufclee)

import xbmc, xbmcplugin
import xbmcgui
import xbmcaddon
import urllib
import time
import os
import sys
import datetime
import downloader

ADDON_ID   =  'plugin.program.totalinstaller'
ADDON      =  xbmcaddon.Addon(id=ADDON_ID)
HOME       =  ADDON.getAddonInfo('path')
addon_name =  "Speed Test"
dialog     =  xbmcgui.Dialog()

max_Bps = 0.0
currently_downloaded_bytes = 0.0

#-----------------------------------------------------------------------------------------------------------------
def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        global max_Bps
        global currently_downloaded_bytes
        
        try:
            percent = min(numblocks * blocksize * 100 / filesize, 100) 
            currently_downloaded_bytes = float(numblocks) * blocksize
            currently_downloaded = currently_downloaded_bytes / (1024 * 1024) 
            Bps_speed = currently_downloaded_bytes / (time.time() - start_time) 
            if Bps_speed > 0:                                                 
                eta = (filesize - numblocks * blocksize) / Bps_speed 
                if Bps_speed > max_Bps: max_Bps = Bps_speed
            else: 
                eta = 0 
            kbps_speed = Bps_speed * 8 / 1024 
            mbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total) 
            dp.update(percent)
        except: 
            currently_downloaded_bytes = float(filesize)
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled(): 
            dp.close() 
            raise Exception("Cancelled")
#-----------------------------------------------------------------------------------------------------------------
def GetEpochStr():
    time_now  = datetime.datetime.now()
    epoch     = time.mktime(time_now.timetuple())+(time_now.microsecond/1000000.)
    epoch_str = str('%f' % epoch)
    epoch_str = epoch_str.replace('.','')
    epoch_str = epoch_str[:-3]
    return epoch_str
#-----------------------------------------------------------------------------------------------------------------
def runtest(url):
    addon_profile_path       = xbmc.translatePath(ADDON.getAddonInfo('profile'))
    speed_test_files_dir     = os.path.join(addon_profile_path, 'speedtestfiles')
    if not os.path.exists(speed_test_files_dir):
        os.makedirs(speed_test_files_dir)

    speed_test_download_file = os.path.join(speed_test_files_dir, GetEpochStr() + '.speedtest')
    timetaken = downloader.download(url, speed_test_download_file)
    xbmc.log('### time taken: %s' % timetaken)
    os.remove(speed_test_download_file)
    if timetaken:
        avgspeed = ((currently_downloaded_bytes / timetaken) * 8 / ( 1024 * 1024 ))
        maxspeed = (max_Bps * 8/(1024*1024))
        if avgspeed < 2:
            livestreams = 'Very low quality streams may work'
            onlinevids = 'Expect buffering, do not try HD'
        elif avgspeed < 2.5:
            livestreams = 'You should be ok for SD content only'
            onlinevids = 'SD/DVD quality should be ok, do not try HD'
        elif avgspeed < 5:
            livestreams = 'Some HD streams may struggle, SD will be fine'
            onlinevids = 'Most will be fine, some Blurays may struggle'
        elif avgspeed < 10:
            livestreams = 'All streams including HD should stream fine'
            onlinevids = 'Most will be fine, some Blurays may struggle'
        else:
            livestreams = 'All streams including HD should stream fine'
            onlinevids = 'You can play all files with no problems'
        xbmc.log("Average Speed: %s" % str(avgspeed))
        xbmc.log("Max. Speed: %s" % str(maxspeed))
        dialog.ok('SPEED TEST RESULTS','[COLOR blue]Live Streams:[/COLOR] ' + livestreams,'','[COLOR blue]Online Video:[/COLOR] ' + onlinevids)
    else:
        dialog.ok('DOWNLOAD FAILED','Sorry it was not possible to download the file, looks like we need to find a different file to test with.')
