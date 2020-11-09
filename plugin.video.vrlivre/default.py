# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/OMundo2osBrasileiros
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools

from addon.common.addon import Addon

addonID = 'plugin.video.vrlivre'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

def run():
    plugintools.log("vrlivre.run")
    
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

def main_list(params):
		plugintools.log("vrlivre ===> " + repr(params))
                                                                                             
                plugintools.add_item(title = "[COLOR red]Curso de Arduino 2018[/COLOR]"              , url = base + "playlist/PLgezO2EG3LXu0KEA49Cv-nxYnYjna0mfy/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/Arduino.png", folder = True)
		plugintools.add_item(title = "[COLOR blue]Drops GIMP[/COLOR]"              , url = base + "playlist/PLgezO2EG3LXvrR6BVrmpani5-MxOGk2LP/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/gimp.png", folder = True)
		plugintools.add_item(title = "[COLOR lime]Batocera & Recalbox[/COLOR]"              , url = base + "playlist/PLgezO2EG3LXsLy024SPWs5oQOWCzu_5F8/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/recalbox.png", folder = True)
		plugintools.add_item(title = "[COLOR white]Portifólios da Informática (2007 à 2016)[/COLOR]"              , url = base + "playlist/PLgezO2EG3LXubMFEyYak9Y3j8tLH1GjgG/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/portifolio.png", folder = True)
		plugintools.add_item(title = "[COLOR yellow]Palestras e Eventos[/COLOR]"              , url = base + "playlist/PLgezO2EG3LXv_F7BalCn59t07fltG2_lq/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/palestras.png", folder = True)
                plugintools.add_item(title = "[COLOR blue]Curso de Artes Gráficas com Software Livre - Barbará Tostes[/COLOR]"              , url = base + "playlist/PL058pFiG1gecMSwTlDZdv-Oc57IuLsmuH/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/grafica.png", folder = True)
                plugintools.add_item(title = "[COLOR lime]Tutoriais do Canal Digola[/COLOR]"              , url = base + "playlist/PLHJQSVdtWwIUPl1agKHb_XYzZb2sEXIFM/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/digola.png", folder = True)
                plugintools.add_item(title = "[COLOR white]Tutoriais do Canal Vikings[/COLOR]"              , url = base + "playlist/PLgezO2EG3LXvdOf-ViGkdjVCVHb7SURa6/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/vikings.png", folder = True)
                plugintools.add_item(title = "[COLOR yellow]Desenhos Vetorizados do Canal Bruno Nerd Comics[/COLOR]"              , url = base + "playlist/PLvZLRSZ-A58sm-RBd_EDYox7n8ZKfye3c/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/nerdcomics.png", folder = True)

                plugintools.add_item(title = "[COLOR blue]Ultraman - Dublado (480p)[/COLOR]"              , url = base + "playlist/PLQKCUFcFQXDSTj4h8EM3ZXkQJLBFHD93u/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/ultraman.jpg", folder = True)
                plugintools.add_item(title = "[COLOR lime]O Regresso de Ultraman - Dublado (480p/720p)[/COLOR]"              , url = base + "playlist/PLxMLyiIzP7Ih-ih2Gcxw2kgS0xcruyEor/", thumbnail = "http://sergiogracas.com/emular/kodi/imagens/ultraman.jpg", folder = True)

		
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		xbmc.executebuiltin('Container.SetViewMode(500)')
		
run()
