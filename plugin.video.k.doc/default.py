# -*- coding: utf-8 -*-
#------------------------------------------------------------
# PT DocS HD
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#-----------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools
from addon.common.addon import Addon

addonID = 'plugin.video.k.doc'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

fan01 = 'special://home/addons/plugin.video.k.doc/resources/fan01.jpg'
iconAA = 'special://home/addons/plugin.video.k.doc/resources/iconAA.png'
icon01 = 'special://home/addons/plugin.video.k.doc/resources/icon01.png'
icon02 = 'special://home/addons/plugin.video.k.doc/resources/icon02.png'
icon03 = 'special://home/addons/plugin.video.k.doc/resources/icon03.png'
icon04 = 'special://home/addons/plugin.video.k.doc/resources/icon04.png'
icon05 = 'special://home/addons/plugin.video.k.doc/resources/icon05.png'
icon06 = 'special://home/addons/plugin.video.k.doc/resources/icon06.png'
icon07 = 'special://home/addons/plugin.video.k.doc/resources/icon07.png'
icon08 = 'special://home/addons/plugin.video.k.doc/resources/icon08.png'
icon09 = 'special://home/addons/plugin.video.k.doc/resources/icon09.png'
icon10 = 'special://home/addons/plugin.video.k.doc/resources/icon10.png'
icon11 = 'special://home/addons/plugin.video.k.doc/resources/icon11.png'
icon12 = 'special://home/addons/plugin.video.k.doc/resources/icon12.png'
iconAB = 'special://home/addons/plugin.video.k.doc/resources/iconAB.png'
iconAC = 'special://home/addons/plugin.video.k.doc/resources/iconAC.png'
iconAD = 'special://home/addons/plugin.video.k.doc/resources/iconAD.png'
iconAE = 'special://home/addons/plugin.video.k.doc/resources/iconAE.png'








def run():
    plugintools.log("plugin.video.k.doc run")
    params = plugintools.get_params()
    if params.get("action") is None: main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()

def main_list(params):
	plugintools.log("pt.docs.hd ===> " + repr(params))
	plugintools.add_item(title = "[ Portugal Animal PT ]", url = base + "playlist/PLzfFJws0cxAwWwvCMS5pJrt_7YrHkdi3K/", thumbnail = iconAA, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Toda a verdade PT ]", url = base + "playlist/PLQ5Fc4sTMxGY3LW6-GhI6pvX8azu4MGMD/", thumbnail = icon01, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Biografia PT ]", url = base + "playlist/PLIK_Upxu-7NNQorPGzqjs0H_wG52xZlIi/", thumbnail = icon02, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Tragédias e mortes PT ]", url = base + "playlist/PLhqHwXAdTOLKeu4sWLS6WQ4WAWYlDQKKt/", thumbnail = icon03, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Ficheiros Forenses ]", url = base + "playlist/PLNh3Houu9XZsHUD6jAJRr0eubxOibwS5c/", thumbnail = icon04, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Extraterrestre PT ]", url = base + "playlist/PLUptSf5en2yFI0meK-4a95Dt474Uv-KhR/", thumbnail = icon05, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Conspiração PT ]", url = base + "playlist/PLQyKeyabQkaJ4bnbHrG3IFTA80O-W4OTD/", thumbnail = icon06, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Variados PT ]", url = base + "playlist/PLL6iDf7wfeR8iUAqoYH219waCPCCsMY50/", thumbnail = icon07, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Anedotas PT  ]", url = base + "playlist/UUBWj3v36qgNo34Y0wW6M35w/", thumbnail = icon09, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Culinaria PT ]", url = base + "playlist/UU4wsBtWPyyIGHX79-xe_YVg/", thumbnail = icon10, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Desporto PT ]", url = base + "playlist/UUMle2Qt_SNvzKJSxyedMCDw/", thumbnail = icon11, fanart = fan01, folder = True)	
	plugintools.add_item(title = "[ Ultramar PT ]", url = base + "playlist/PLNnM7uubGF22GfS7CMA1M9zzzzMh6yBzb/", thumbnail = icon12, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Historia PT ]", url = base + "playlist/PLer3Nin8AJE8rEgZ43YNkvSPwq37QMd7L/", thumbnail = iconAB, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Filmes PT ]", url = base + "playlist/PL8CA97E24D332C4E7/", thumbnail = iconAC, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Musica PT ]", url = base + "playlist/PLTfgKjfU6kHJO6JOhMbNgX77X4vraGejv/", thumbnail = iconAD, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Fado PT ]", url = base + "playlist/PLbUGGofvGuAsr8Jw75OgyRrol8WCzVC0q/", thumbnail = icon08, fanart = fan01, folder = True)
	plugintools.add_item(title = "[ Kodiazor Youtube ]", url = base + "playlist/UUqKqCBK7mCOhMvumPOwD6NQ/", thumbnail = iconAE, fanart = fan01, folder = True)
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
	
run()
