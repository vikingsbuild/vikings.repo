import glob
import os
import re
import traceback

import xbmc
import xbmcgui
import xbmcaddon
import threading
from resources.lib.modules import log_utils
from resources.lib.modules import control
from xbmc import (LOGDEBUG, LOGERROR, LOGFATAL, LOGINFO,
                  LOGNONE, LOGNOTICE, LOGSEVERE, LOGWARNING)

control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))

addon_name = 'covenant'
addon_icon = xbmcaddon.Addon().getAddonInfo('icon')
addon_path = xbmc.translatePath(('special://home/addons/plugin.video.Covenant')).decode('utf-8')
module_path = xbmc.translatePath(('special://home/addons/script.module.openscrapers')).decode('utf-8')


def main():
    fum_ver = xbmcaddon.Addon(id='script.module.openscrapers').getAddonInfo('version')
    updated = xbmcaddon.Addon(id='plugin.video.Covenant').getSetting('module_base')
    if updated == '' or updated is None:
        updated = '0'

    if str(fum_ver) == str(updated):
        return

    xbmcgui.Dialog().notification(addon_name, 'Setting up Free Providers', addon_icon)
    settings_xml_path = os.path.join(addon_path, 'resources/settings.xml')
    scraper_path = os.path.join(module_path, 'lib/resources/lib/sources/en')
    log('Covenant Scraper Path: %s' % (str(scraper_path)), LOGINFO)
    try:
        xml = openfile(settings_xml_path)
    except Exception:
        failure = traceback.format_exc()
        log('Covenant Service - Exception: \n %s' % (str(failure)), LOGINFO)
        return

    new_settings = []
    new_settings = '<category label="32345">\n'
    for file in glob.glob("%s/*.py" % (scraper_path)):
        file = os.path.basename(file)
        if '__init__' not in file:
            file = file.replace('.py', '')
            new_settings += '        <setting id="provider.%s" type="bool" label="%s" default="true" />\n' % (
                file.lower(), file.upper())
    new_settings += '    </category>'

    xml = xml.replace('<category label="32345"></category>', str(new_settings))
    savefile(settings_xml_path, xml)

    xbmcaddon.Addon(id='plugin.video.Covenant').setSetting('module_base', fum_ver)
    xbmcgui.Dialog().notification(addon_name, 'Providers Updated', addon_icon)


    xbmcgui.Dialog().notification(addon_name, 'Setting up Debrid Providers', addon_icon)
    settings_xml_path = os.path.join(addon_path, 'resources/settings.xml')
    scraper_path = os.path.join(module_path, 'lib/resources/lib/sources/en_de')
    log('Covenant Path: %s' % (str(scraper_path)), LOGINFO)
    try:
        xml = openfile(settings_xml_path)
    except Exception:
        failure = traceback.format_exc()
        log('Covenant Service - Exception: \n %s' % (str(failure)), LOGINFO)
        return

    new_settings = []
    new_settings = '<category label="32615">\n'
    for file in glob.glob("%s/*.py" % (scraper_path)):
        file = os.path.basename(file)
        if '__init__' not in file:
            file = file.replace('.py', '')
            new_settings += '        <setting id="provider.%s" type="bool" label="%s" default="true" />\n' % (
                file.lower(), file.upper())
    new_settings += '    </category>'

    xml = xml.replace('<category label="32615"></category>', str(new_settings))
    savefile(settings_xml_path, xml)

    xbmcaddon.Addon(id='plugin.video.Covenant').setSetting('module_base', fum_ver)
    xbmcgui.Dialog().notification(addon_name, 'Providers Updated', addon_icon)


    xbmcgui.Dialog().notification(addon_name, 'Setting up Torrent Providers', addon_icon)
    settings_xml_path = os.path.join(addon_path, 'resources/settings.xml')
    scraper_path = os.path.join(module_path, 'lib/resources/lib/sources/en_tor')
    log('Covenant Scraper Path: %s' % (str(scraper_path)), LOGINFO)
    try:
        xml = openfile(settings_xml_path)
    except Exception:
        failure = traceback.format_exc()
        log('Covenant Service - Exception: \n %s' % (str(failure)), LOGINFO)
        return

    new_settings = []
    new_settings = '<category label="32616">\n'
    for file in glob.glob("%s/*.py" % (scraper_path)):
        file = os.path.basename(file)
        if '__init__' not in file:
            file = file.replace('.py', '')
            new_settings += '        <setting id="provider.%s" type="bool" label="%s" default="true" />\n' % (
                file.lower(), file.upper())
    new_settings += '    </category>'

    xml = xml.replace('<category label="32616"></category>', str(new_settings))
    savefile(settings_xml_path, xml)

    xbmcaddon.Addon(id='plugin.video.Covenant').setSetting('module_base', fum_ver)
    xbmcgui.Dialog().notification(addon_name, 'Providers Updated', addon_icon)
    
    
def openfile(path_to_the_file):
    try:
        fh = open(path_to_the_file, 'rb')
        contents = fh.read()
        fh.close()
        return contents
    except Exception:
        failure = traceback.format_exc()
        print('Service Open File Exception - %s \n %s' % (path_to_the_file, str(failure)))
        return None

def savefile(path_to_the_file, content):
    try:
        fh = open(path_to_the_file, 'wb')
        fh.write(content)
        fh.close()
    except Exception:
        failure = traceback.format_exc()
        print('Service Save File Exception - %s \n %s' % (path_to_the_file, str(failure)))


DEBUGPREFIX = '[COLOR red][ Covenant DEBUG ][/COLOR]'


def log(msg, level=LOGNOTICE):

    try:
        if isinstance(msg, unicode):
            msg = '%s (ENCODED)' % (msg.encode('utf-8'))
        print('%s: %s' % (DEBUGPREFIX, msg))
    except Exception as e:
        try:
            xbmc.log('Logging Failure: %s' % (e), level)
        except Exception:
            pass

if __name__ == '__covenant__':
    main()

