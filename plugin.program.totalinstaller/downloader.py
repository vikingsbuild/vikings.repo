#
#      Copyright (C) 2014 Sean Poyser
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import xbmcgui
import urllib
import time

def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("Status...","Downloading Content",' ', ' ')
    dp.update(0)
    start_time=time.time()
    urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))
     
def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100) 
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total) 
            e = 'Speed: %.02f Kb/s ' % kbps_speed 
            e += 'ETA: %02d:%02d' % divmod(eta, 60) 
            dp.update(percent, mbs, e)
            if dp.iscanceled(): 
                dp.close()
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled(): 
            dp.close()
