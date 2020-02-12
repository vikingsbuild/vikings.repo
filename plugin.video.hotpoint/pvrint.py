import xbmc
import os



def urlpvr(url,epg):
    dir = xbmc.translatePath("special://home/userdata/addon_data/pvr.iptvsimple")

    getsit = os.path.exists(dir)

    if getsit == "False":
        makedirs(dir)
        config = ""+dir+"/settings.xml"
        file = open(""+config+"","a")
        file.write('<settings>')
        file.write('\n')
        file.write('    <setting id="epgCache" value="true" />')
        file.write('\n')
        file.write('    <setting id="epgPath" value="" />')
        file.write('\n')
        file.write('    <setting id="epgPathType" value="1" />')
        file.write('\n')
        file.write('    <setting id="epgTSOverride" value="false" />')
        file.write('\n')
        file.write('    <setting id="epgTimeShift" value="0.000000" />')
        file.write('\n')
        file.write('    <setting id="epgUrl" value="'+epg+'" />')
        file.write('\n')
        file.write('    <setting id="logoBaseUrl" value="" />')
        file.write('\n')
        file.write('    <setting id="logoFromEpg" value="0" />')
        file.write('\n')
        file.write('    <setting id="logoPath" value="" />')
        file.write('\n')
        file.write('    <setting id="logoPathType" value="1" />')
        file.write('\n')
        file.write('    <setting id="m3uCache" value="false" />')
        file.write('\n')
        file.write('    <setting id="m3uPath" value="" />')
        file.write('\n')
        file.write('    <setting id="m3uPathType" value="1" />')
        file.write('\n')
        file.write('    <setting id="m3uUrl" value="'+url+'" />')
        file.write('\n')
        file.write('    <setting id="sep1" value="" />')
        file.write('\n')
        file.write('    <setting id="sep2" value="" />')
        file.write('\n')
        file.write('    <setting id="sep3" value="" />')
        file.write('\n')
        file.write('    <setting id="startNum" value="1" />')
        file.write('\n')
        file.write('</settings>')
        file.write('\n')

    else:
        config = ""+dir+"/settings.xml"
        file = open(""+config+"","a")
        file.write('<settings>')
        file.write('\n')
        file.write('    <setting id="epgCache" value="true" />')
        file.write('\n')
        file.write('    <setting id="epgPath" value="" />')
        file.write('\n')
        file.write('    <setting id="epgPathType" value="1" />')
        file.write('\n')
        file.write('    <setting id="epgTSOverride" value="false" />')
        file.write('\n')
        file.write('    <setting id="epgTimeShift" value="0.000000" />')
        file.write('\n')
        file.write('    <setting id="epgUrl" value="'+epg+'" />')
        file.write('\n')
        file.write('    <setting id="logoBaseUrl" value="" />')
        file.write('\n')
        file.write('    <setting id="logoFromEpg" value="0" />')
        file.write('\n')
        file.write('    <setting id="logoPath" value="" />')
        file.write('\n')
        file.write('    <setting id="logoPathType" value="1" />')
        file.write('\n')
        file.write('    <setting id="m3uCache" value="false" />')
        file.write('\n')
        file.write('    <setting id="m3uPath" value="" />')
        file.write('\n')
        file.write('    <setting id="m3uPathType" value="1" />')
        file.write('\n')
        file.write('    <setting id="m3uUrl" value="'+url+'" />')
        file.write('\n')
        file.write('    <setting id="sep1" value="" />')
        file.write('\n')
        file.write('    <setting id="sep2" value="" />')
        file.write('\n')
        file.write('    <setting id="sep3" value="" />')
        file.write('\n')
        file.write('    <setting id="startNum" value="1" />')
        file.write('\n')
        file.write('</settings>')
        file.write('\n')



                

                

#url ="123"
#epg = "ade"

