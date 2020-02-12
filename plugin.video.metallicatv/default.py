# -*- coding: utf-8 -*-
#------------------------------------------------------------
# metallicatv
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools
from addon.common.addon import Addon

addonID = 'plugin.video.metallicatv'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

fan01 = 'special://home/addons/plugin.video.metallicatv/resources/fan01.jpg'
icon = 'special://home/addons/plugin.video.metallicatv/resources/icon.png'
icon00 = 'special://home/addons/plugin.video.metallicatv/resources/icon00.png'
icon01 = 'special://home/addons/plugin.video.metallicatv/resources/icon01.png'
icon02 = 'special://home/addons/plugin.video.metallicatv/resources/icon02.png'
icon03 = 'special://home/addons/plugin.video.metallicatv/resources/icon03.png'



def run():
    plugintools.log("metallicatv.run")
    params = plugintools.get_params()
    if params.get("action") is None: main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()

def main_list(params):
	plugintools.log("metallicatv ===> " + repr(params))
	
	plugintools.add_item(title = "MetallicaTV", url = base + "playlist/UUbulh9WdLtEXiooRcYK7SWw/", thumbnail = icon01, fanart = fan01, folder = True)
	plugintools.add_item(title = "Metallica Concerts", url = base + "playlist/UUL-v32G1Q-Ibbfif0DxJ--w/", thumbnail = icon02, fanart = fan01, folder = True)
	plugintools.add_item(title = "Metallica Albums", url = base + "playlist/PL077BD914A7C9D11C/", thumbnail = icon03, fanart = fan01, folder = True)
		
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
	
run()
