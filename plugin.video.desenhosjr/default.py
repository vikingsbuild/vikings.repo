# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/Brasileiros
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools

from addon.common.addon import Addon

addonID = 'plugin.video.desenhosjr'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

icon1 = 'special://home/addons/plugin.video.desenhosjr/capas/icon1.png'
icon2 = 'special://home/addons/plugin.video.desenhosjr/capas/icon2.png'
icon3 = 'special://home/addons/plugin.video.desenhosjr/capas/icon3.png'
icon4 = 'special://home/addons/plugin.video.desenhosjr/capas/icon4.png'
icon5 = 'special://home/addons/plugin.video.desenhosjr/capas/icon5.png'
icon6 = 'special://home/addons/plugin.video.desenhosjr/capas/icon6.png'
icon7 = 'special://home/addons/plugin.video.desenhosjr/capas/icon7.png'
icon8 = 'special://home/addons/plugin.video.desenhosjr/capas/icon8.png'
icon9 = 'special://home/addons/plugin.video.desenhosjr/capas/icon9.png'
icon10 = 'special://home/addons/plugin.video.desenhosjr/capas/icon10.png'
icon11 = 'special://home/addons/plugin.video.desenhosjr/capas/icon11.png'
icon12 = 'special://home/addons/plugin.video.desenhosjr/capas/icon12.png'
icon13 = 'special://home/addons/plugin.video.desenhosjr/capas/icon13.png'
icon14 = 'special://home/addons/plugin.video.desenhosjr/capas/icon14.png'
icon15 = 'special://home/addons/plugin.video.desenhosjr/capas/icon15.png'
icon16 = 'special://home/addons/plugin.video.desenhosjr/capas/icon16.png'
icon17 = 'special://home/addons/plugin.video.desenhosjr/capas/icon17.png'
icon18 = 'special://home/addons/plugin.video.desenhosjr/capas/icon18.png'
icon19 = 'special://home/addons/plugin.video.desenhosjr/capas/icon19.png'
icon20 = 'special://home/addons/plugin.video.desenhosjr/capas/icon20.png'
icon0 = 'special://home/addons/plugin.video.desenhosjr/capas/icon0.png'

def run():
    plugintools.log("Desenhos.jr.run")
    
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

def main_list(params):
		plugintools.log("Desenhos.jr ===> " + repr(params))

		plugintools.add_item(title = "[COLOR red]CAILLOU [/COLOR]" , url = base + "channel/UCxc9Eq3hOuhAbovmyTqBIig/", thumbnail = icon1, folder = True)
		plugintools.add_item(title = "[COLOR red]PJ MASK [/COLOR]" , url = base + "channel/UC6RA9q6uVGJpe4QcS3UmGmg/", thumbnail = icon2, folder = True)
		plugintools.add_item(title = "[COLOR red]MASHA e o URSO [/COLOR]" , url = base + "channel/UCJKBSfD5JSUxGhriFeoPCCg/", thumbnail = icon3, folder = True)
		plugintools.add_item(title = "[COLOR red]PEPPA PIG [/COLOR]" , url = base + "user/OficialPeppa/", thumbnail = icon4, folder = True)
		plugintools.add_item(title = "[COLOR red]Galinha-Pintadinha [/COLOR]" , url = base + "user/juptube/", thumbnail = icon5, folder = True)
		plugintools.add_item(title = "[COLOR red]O SHOW DA LUNA [/COLOR]" , url = base + "user/OShowDaLuna/", thumbnail = icon6, folder = True)
		plugintools.add_item(title = "[COLOR red]Bob.Zoom [/COLOR]" , url = base + "user/bobzoomclub/", thumbnail = icon7, folder = True)
		plugintools.add_item(title = "[COLOR red]Mr.Ben [/COLOR]" , url = base + "user/mrbeancartoonworld/", thumbnail = icon8, folder = True)
		plugintools.add_item(title = "[COLOR red]PINGU [/COLOR]" , url = base + "user/pingu/", thumbnail = icon9, folder = True)
		plugintools.add_item(title = "[COLOR red]PEIXONAUTA [/COLOR]" , url = base + "user/PeixonauTube/", thumbnail = icon10, folder = True)
		plugintools.add_item(title = "[COLOR red]POCOYO [/COLOR]" , url = base + "user/PocoyoBrazil/", thumbnail = icon11, folder = True)
		plugintools.add_item(title = "[COLOR red]PICA-PAU [/COLOR]" , url = base + "channel/UCiFg-2CjsG_xcSsHNjDeLpw/", thumbnail = icon12, folder = True)
		plugintools.add_item(title = "[COLOR red]BACKYARDIGANS [/COLOR]" , url = base + "channel/UCoEx2PlHPo4V6Dwr7-dnPCw/", thumbnail = icon13, folder = True)
		plugintools.add_item(title = "[COLOR red]TIGRE DANIEL [/COLOR]" , url = base + "channel/UC0uzSknyMFmFV6YrKyglYfQ/", thumbnail = icon14, folder = True)
		plugintools.add_item(title = "[COLOR red]HE-MAN [/COLOR]" , url = base + "channel/UCAdYfCTaSxKxUp3fNyIfA0w/", thumbnail = icon15, folder = True)
		plugintools.add_item(title = "[COLOR red]BEN e HOLLY [/COLOR]" , url = base + "channel/UCtfoEVSgFIPPoUIwwT9t0pA/", thumbnail = icon16, folder = True)
		plugintools.add_item(title = "[COLOR red]BUSCA DO VALE ENCANTADO [/COLOR]" , url = base + "channel/UCmp50hux7Zj56yRXJFW_aIw/", thumbnail = icon17, folder = True)
		plugintools.add_item(title = "[COLOR red]GEORGE o CURIOSO [/COLOR]" , url = base + "channel/UCg3VS8afaNzH4EWJmMcdqMg/", thumbnail = icon18, folder = True)
		plugintools.add_item(title = "[COLOR red]MORANGUINHO [/COLOR]" , url = base + "channel/UCjgMnjThnmvtWN6SgveQvlA/", thumbnail = icon19, folder = True)
		plugintools.add_item(title = "[COLOR red]PANTERA COR DE ROSA [/COLOR]" , url = base + "user/PinkPanthersShow/", thumbnail = icon20, folder = True)
		plugintools.add_item(title = "[COLOR red]LULUZINHA [/COLOR]" , url = base + "channel/UCv9NGc0M31y3L6CdF8ASvdA/", thumbnail = icon0, folder = True)

	
		
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		xbmc.executebuiltin('Container.SetViewMode(500)')
		
run()