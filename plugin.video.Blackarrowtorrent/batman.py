import xbmc
import os
from random import randint
addonID = "plugin.video.Blackarrowtorrent"
addon_data_dir = os.path.join(xbmc.translatePath("special://userdata/addon_data" ).decode("utf-8"), addonID)
m3u =  os.path.join(addon_data_dir, "files.m3u")

def batmanz():
        
        temp = randint(1,291)
        if not os.path.exists(addon_data_dir):
                os.makedirs(addon_data_dir)

        m3u =  os.path.join(addon_data_dir, "files.m3u")

        file = open(""+m3u+"","w")
        file.close

        temp = randint(1,40)
        eps = 30
        valor = eps
        svalor = int(valor)
        stemp = "%03d" %(temp)
        sstemp  = str(stemp)
        i = temp
                
        for j in range(i,(eps+temp)):
                
                file = open(""+m3u+"","a")
                igvar = "%02d" %(j+1)
                gvar = ""
                gvar = str(igvar)
                # http://vd.ec.cx/vd/dd/RC/RCServer01/videos/NRTOSHPEP"+gvar+".mp4 
                file.write("http://cdnv2.ec.cx/RedeCanais/RedeCanais/RCServer09/ondemand/BTMNASRANMDEP"+igvar+".mp4")
                file.write("\n")
                file.close

        xbmc.Player().play(""+m3u+"")

