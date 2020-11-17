# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# modified by: EL RINCON DEL TERROR
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.ElRinconDelTerror'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLLxxgrF1QnBgTY1SlXDZMKjaD9BZhxx-2" 	#PACK 1 — 700 PELICULAS DE TERROR
YOUTUBE_CHANNEL_ID_2 = "PLLxxgrF1QnBj-OJo_5IcD4jQzz89ecHhw" 	#PACK 2 - 380 PELICULAS DE TERROR
YOUTUBE_CHANNEL_ID_3 = "PLQo6Q5cN_Mz1kweAJlxuxFMvedRswWHK3" 	#PACK 3 - 1K PELICULAS DE TERROR
YOUTUBE_CHANNEL_ID_4 = "PLLxxgrF1QnBivCVKsFZN_zwQu6ZDh9Ipw" 	#PELÍCULAS - STEPHEN KING FILMOGRAFIA
YOUTUBE_CHANNEL_ID_5 = "PLKG7EX6NsijFD872T4mQif-ia1tiUuT0l" 	#Serie completa Alfred hitchcock presenta 1985-1988
YOUTUBE_CHANNEL_ID_6 = "PLtSe2bb4MBZ9DzeVolo0M2742Top-1K87" 	#SERIE HISTORIAS PARA NO DORMIR
YOUTUBE_CHANNEL_ID_7 = "PLvUynHoF6Z-octXaavM5Xkw7bt7sXfmBo" 	#SERIE EN LOS LIMITES DE LA REALIDAD
YOUTUBE_CHANNEL_ID_8 = "PLhvu3K0rAjwoTp5rOLA71hIp38IPs1sI7" 	#SERIE HISTORIAS DE LA CRIPTA
YOUTUBE_CHANNEL_ID_9 = "PLjwGxAF80__odKyMKoDFDDn-86WLO5Yk6" 	#SERIE LA DIMENSION DESCONOCIDA
YOUTUBE_CHANNEL_ID_10 = "PLMp93nQTlQMBe1_NcswFO2u-sxpf5nh-N" 	#HISTORIAS REALES DE  TERROR
YOUTUBE_CHANNEL_ID_11 = "PL2uyZ-Y8sN0F-Us-zCJpUdbbTFfbJuwA4" 	#DOCUMENTALES DE TERROR
YOUTUBE_CHANNEL_ID_12 = "PLYn6mzqkgzkkNEOFcFiX6YCkCShs76cE4" 	#DOCUMENTALES TERROR 2
YOUTUBE_CHANNEL_ID_13 = "PLLxxgrF1QnBinkXrSdqaC5FwAsjXQt7Xm" 	#PACK 4 — 600  PELICULAS DE TERROR
YOUTUBE_CHANNEL_ID_14 = "PLqivnvaruBVGILSU7zT1chU7PJ4Actf8S" 	#HECHOS PERTURBADORES
YOUTUBE_CHANNEL_ID_15 = "PLShKu0sRclF_TCLGKxzFFpX3EVKCA-4nd" 	#PETICIONES DE PELICULAS DE TERROR
YOUTUBE_CHANNEL_ID_16 = "PLd1t82HTOKhmIbMf18laB8hJ8n5VdQYSn" 	#MUSICA PARA HALLOWEEN
YOUTUBE_CHANNEL_ID_17 = "PLdjV7zWer4CBmFbYLVytP8d7PpmHfBJ62" 	#HISTORIAS DE ESPIRITIMOS 
YOUTUBE_CHANNEL_ID_18 = "PLDoKNfjmoxIfAOi5yDpW46w95jvw509e9" 	#AL CAER LA NOCHE RADIO LATINO
YOUTUBE_CHANNEL_ID_19 = "PLvUynHoF6Z-octXaavM5Xkw7bt7sXfmBo" 	#CUENTOS DE HALLOWEEN PARA NIÑOS
YOUTUBE_CHANNEL_ID_20 = "PLP_gz3lCvyIZu-fogu8esAMyRuC_ocxh4" 	#MANUALIDADES Y MAQUILLAJES PARA HALLOWEEN
YOUTUBE_CHANNEL_ID_21 = "PLd1t82HTOKhkVGwxwdcKx2w_hLOmrlFgP" 	#PETICIONES DE HISTORIAS TERROR
# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]PACK 1 - 700 PELICULAS DE TERROR[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]PACK 2 - 380 PELICULAS DE TERROR[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]PACK 3 - 1K DE PELICLAS DE TERROR[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]PACK 4 - PELICULAS DE TERROR[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]PELICULAS DE STEPHEN KING FILMOGRAFIA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]SERIE COMPLETA ALFRED HITCHOCK PRESENTA 1985-1988[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )
		

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]SERIES HISTORIAS PARA NO DORMIR[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]SERIE EN LOS LIMITES DE LA REALIDAD[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]SERIE HISTORIAS DE LA CRIPTA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]SERIE LA DIMENSION DESCONOCIDA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )


    plugintools.add_item( 
        #action="", 
        title="[COLOR red]HISTORIAS REALES DE TERROR[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]DOCUMENTALES DE TERROR[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]DOCUMENTALES TERROR 2[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )



    plugintools.add_item( 
        #action="", 
        title="[COLOR red]HECHOS PERTUBADORES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]PETICIONES PELICULAS DE TERROR[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]MUSICA PARA HALLOWEEN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]HISTORIAS DE ESPIRITIMOS [/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )
		

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]AL CAER LA NOCHE RADIO LATINO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]CUENTOS DE HALLOWEEN PARA NIÑOS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]MANUALIDADES Y MAQUILLAJES PARA HALLOWEEN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR red]PETICIONES DE HISTORIAS TERROR[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/icon.png?raw=true",
		fanart="https://github.com/djliptv/ElRinconDelTerror/blob/master/Pics/Fanart.jpg?raw=true",
        folder=True )
run()