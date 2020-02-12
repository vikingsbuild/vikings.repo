# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/DocHistory
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import os
import sys
import time
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.DocHistory'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"

YOUTUBE_CHANNEL_ID = "PLAl-cwrHd5apRdbV0NjbBfleGmUw_iZ9A"

# Ponto de Entrada
def run():
	# Pega Parâmetros
	params = plugintools.get_params()
	
	if params.get("action") is None:
		xbmc.Player().play(entryurl)
		
		while xbmc.Player().isPlaying():
			time.sleep(1)

		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"

	plugintools.close_item_list()

# Menu Principal
def main_list(params):
	plugintools.log("DocHistory.main_list "+repr(params))
	
	plugintools.log("DocHistory.run")
	
	#plugintools.direct_play(str(entryurl))

	plugintools.add_item(
		title = "Documentarios Historicos",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID+"/",
		thumbnail = icon,
		folder = True )
		

run()
