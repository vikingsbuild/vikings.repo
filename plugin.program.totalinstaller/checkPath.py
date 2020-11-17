#      Copyright (C) 2015 whufclee
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

import os, re, xbmc, xbmcaddon, xbmcgui
AddonID      = 'plugin.program.totalinstaller'
ADDON        =  xbmcaddon.Addon(id=AddonID)
zip          =  ADDON.getSetting('zip')
dialog       =  xbmcgui.Dialog()
path         =  xbmc.translatePath(os.path.join(zip,'testCBFolder'))

def check(direct):
    try:
        os.makedirs(path)
        os.removedirs(path)
        xbmc.executebuiltin('Dialog.Show(busydialog)')
        dialog.ok('[COLOR=lime]SUCCESS[/COLOR]', 'Great news, the path you chose is writeable.', 'Some of these builds are rather big, we recommend', 'a minimum of 1GB storage space.')
        
        if direct!='maintenance':
            ADDON.openSettings()
    
    except:
        xbmc.executebuiltin('Dialog.Show(busydialog)')
        dialog.ok('INVALID PATH', 'Kodi cannot write to the path you\'ve chosen. Please click OK and choose another location. Please note: currently network shares are not supported so we suggest using something like a USB stick.')
        ADDON.openSettings()
    
    xbmc.executebuiltin('Dialog.Close(busydialog)')
    
if __name__ == '__main__':
    check('settings')
