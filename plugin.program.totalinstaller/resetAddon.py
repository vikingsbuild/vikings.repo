#
#      Copyright (C) 2014 Richard Dean
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

import xbmc
import xbmcgui
import xbmcaddon
import shutil

AddonID      = 'plugin.program.totalinstaller'
ADDON        =  xbmcaddon.Addon(id=AddonID)

def resetAddon():
    path = xbmc.translatePath('special://profile/addon_data/'+AddonID)
    shutil.rmtree(path)
    
    d = xbmcgui.Dialog()
    d.ok('Add-on Successfully Reset', 'Your add-on has now been reset to defaults. If you previously had login information entered in the settings don\'t forget to add the details back again.')


if __name__ == '__main__':
    xbmc.executebuiltin('Dialog.Show(busydialog)')
    resetAddon()
    xbmc.executebuiltin('Dialog.Close(busydialog)')
    ADDON.openSettings()