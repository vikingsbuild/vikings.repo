#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

    service.py for Jen Template
    Copyright (C) 2018

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    -------------------------------------------------------------

    Version:
        2018-05-21:
            Updated to be self updating via settings.xml - NO Need To Change This File Anymore
            Takes into account if end-user API keys are stored in settings, and doesn't update it
                if they are.

        2018-05-19:
            Updated documentation in Header
            Added ability to disable service after updating API Keys (reduces load on Kodi startup)
            Removed old stuff

    Variables To Change:
        Nothing. Nada. Zilch. Woot!


    Usage:
        Set this in your Jen v1.6 or higher and it should keep your end user's API Keys and Root XML
            in order automatically. Takes into account when user's have entered their own API keys
            


"""

import os,re,traceback
import xbmc,xbmcaddon,xbmcgui


addon_id   = xbmcaddon.Addon().getAddonInfo('id')
addon_name = xbmcaddon.Addon().getAddonInfo('name')
addon_icon = xbmcaddon.Addon().getAddonInfo('icon')
ownAddon   = xbmcaddon.Addon(id=addon_id)

addon_path= xbmc.translatePath(('special://home/addons/%s' % (addon_id))).decode('utf-8')


#######################################################################
# Do Not Change Any Settings Or Code In This File.
#######################################################################


my_settings = {'root_xml':'file://jen_main.xml'}


def main():
    try:
        current_version = ownAddon.getSetting('current_version')
        if current_version == '':
            current_version = '0'
        enable_notification = ownAddon.getSetting('enable_notification')
        if enable_notification == '' or enable_notification == 'false':
            enable_notification = False
        else:
            enable_notification = True
        disable_after_update = ownAddon.getSetting('disable_after_update')
        if disable_after_update == '' or disable_after_update == 'false':
            disable_after_update = False
        else:
            disable_after_update = True

        update_version = ownAddon.getSetting('update_ver')
        if update_version == '':
            update_version = '0'

        debug = ownAddon.getSetting('debug')
        if debug == '' or debug == 'false':
            debug = False
        else:
            debug = True

        get_my_settings()

        if int(current_version) > int(update_version):
            if debug:
                pass
            else:
                ownAddon.setSetting('root_xml', my_settings['root_xml'])
            ownAddon.setSetting('tvdb_api_key', my_settings['tvdb_api_key'])
            ownAddon.setSetting('tmdb_api_key', my_settings['tmdb_api_key'])
            ownAddon.setSetting('trakt_api_client_id', my_settings['trakt_api_client_id'])
            ownAddon.setSetting('trakt_api_client_secret', my_settings['trakt_api_client_secret'])
            ownAddon.setSetting('TRAKT_ACCESS_TOKEN', my_settings['TRAKT_ACCESS_TOKEN'])
            ownAddon.setSetting('TRAKT_EXPIRES_AT', my_settings['TRAKT_EXPIRES_AT'])
            ownAddon.setSetting('TRAKT_REFRESH_TOKEN', my_settings['TRAKT_REFRESH_TOKEN'])
            ownAddon.setSetting('lastfm_api_key', my_settings['lastfm_api_key'])
            ownAddon.setSetting('lastfm_secret', my_settings['lastfm_secret'])
            ownAddon.setSetting('search_db_location', my_settings['search_db_location'])
 
            ownAddon.setSetting('update_ver', current_version)
            if enable_notification:
                xbmcgui.Dialog().notification(addon_name, 'Updated API keys', addon_icon)
    except:
        pass
    if disable_after_update:
        disable_this()


def get_my_settings():
    try:
        settings_xml_path = os.path.join(addon_path, 'resources/settings.xml')
        xml_content = openfile(settings_xml_path)

        xml_root = re.search('id="root_xml".+?/>', xml_content)
        if not xml_root == None:
            xml_root = re.findall('default="(.+?)"', xml_root.group())[0]
            my_settings['root_xml'] = (xml_root if not 'visible' in xml_root else 'file://main.xml')
        else:
            my_settings['root_xml'] = 'file://main.xml'

        tvdb_api_key = re.search('id="tvdb_api_key".+?/>', xml_content)
        if not tvdb_api_key == None:
            tvdb_api_key = re.findall('default="(.+?)"', tvdb_api_key.group())[0]
            my_settings['tvdb_api_key'] = (tvdb_api_key if not 'visible' in tvdb_api_key else '')
        else:
            my_settings['tvdb_api_key'] = ''

        tmdb_api_key = re.search('id="tmdb_api_key".+?/>', xml_content)
        if not tmdb_api_key == None:
            tmdb_api_key = re.findall('default="(.+?)"', tmdb_api_key.group())[0]
            my_settings['tmdb_api_key'] = (tmdb_api_key if not 'visible' in tmdb_api_key else '')
        else:
            my_settings['tmdb_api_key'] = ''

        trakt_api_client_id = re.search('id="trakt_api_client_id".+?/>', xml_content)
        if not trakt_api_client_id == None:
            trakt_api_client_id = re.findall('default="(.+?)"', trakt_api_client_id.group())[0]
            my_settings['trakt_api_client_id'] = (trakt_api_client_id if not 'visible' in trakt_api_client_id else '')
        else:
            my_settings['trakt_api_client_id'] = ''

        trakt_api_client_secret = re.search('id="trakt_api_client_secret".+?/>', xml_content)
        if not trakt_api_client_secret == None:
            trakt_api_client_secret = re.findall('default="(.+?)"', trakt_api_client_secret.group())[0]
            my_settings['trakt_api_client_secret'] = (trakt_api_client_secret if not 'visible' in trakt_api_client_secret else '')
        else:
            my_settings['trakt_api_client_secret'] = ''

        lastfm_api_key = re.search('id="lastfm_api_key".+?/>', xml_content)
        if not lastfm_api_key == None:
            lastfm_api_key = re.findall('default="(.+?)"', lastfm_api_key.group())[0]
            my_settings['lastfm_api_key'] = (lastfm_api_key if not 'visible' in lastfm_api_key else '')
        else:
            my_settings['lastfm_api_key'] = ''

        lastfm_secret = re.search('id="lastfm_secret".+?/>', xml_content)
        if not lastfm_secret == None:
            lastfm_secret = re.findall('default="(.+?)"', lastfm_secret.group())[0]
            my_settings['lastfm_secret'] = (lastfm_secret if not 'visible' in lastfm_secret else '')
        else:
            my_settings['lastfm_secret'] = ''

        search_db_location = re.search('id="search_db_location".+?/>', xml_content)
        if not search_db_location == None:
            search_db_location = re.findall('default="(.+?)"', search_db_location.group())[0]
            my_settings['search_db_location'] = (search_db_location if not 'visible' in search_db_location else '')
        else:
            my_settings['search_db_location'] = ''

        TRAKT_ACCESS_TOKEN = re.search('id="TRAKT_ACCESS_TOKEN".+?/>', xml_content)
        if not TRAKT_ACCESS_TOKEN == None:
            TRAKT_ACCESS_TOKEN = re.findall('default="(.+?)"', TRAKT_ACCESS_TOKEN.group())[0]
            my_settings['TRAKT_ACCESS_TOKEN'] = (TRAKT_ACCESS_TOKEN if not 'visible' in TRAKT_ACCESS_TOKEN else '')
        else:
            my_settings['TRAKT_ACCESS_TOKEN'] = ''

        TRAKT_EXPIRES_AT = re.search('id="TRAKT_EXPIRES_AT".+?/>', xml_content)
        if not TRAKT_EXPIRES_AT == None:
            TRAKT_EXPIRES_AT = re.findall('default="(.+?)"', TRAKT_EXPIRES_AT.group())[0]
            my_settings['TRAKT_EXPIRES_AT'] = (TRAKT_EXPIRES_AT if not 'visible' in TRAKT_EXPIRES_AT else '')
        else:
            my_settings['TRAKT_EXPIRES_AT'] = ''

        TRAKT_REFRESH_TOKEN = re.search('id="TRAKT_REFRESH_TOKEN".+?/>', xml_content)
        if not TRAKT_REFRESH_TOKEN == None:
            TRAKT_REFRESH_TOKEN = re.findall('default="(.+?)"', TRAKT_REFRESH_TOKEN.group())[0]
            my_settings['TRAKT_REFRESH_TOKEN'] = (TRAKT_REFRESH_TOKEN if not 'visible' in TRAKT_REFRESH_TOKEN else '')
        else:
            my_settings['TRAKT_REFRESH_TOKEN'] = ''
    except:
        pass


def disable_this():
    addonxml_path = os.path.join(addon_path, 'addon.xml')
    xml_content = openfile(addonxml_path)
    if re.search('point="xbmc.service"', xml_content):
        xml_content = xml_content.replace('point="xbmc.service"',
                'point="xbmc.jen"')
        savefile(addonxml_path, xml_content)
    else:
        pass


def openfile(path_to_the_file):
    try:
        fh = open(path_to_the_file, 'rb')
        contents = fh.read()
        fh.close()
        return contents
    except:
        print('Wont open: %s' % (path_to_the_file))
        return None


def savefile(path_to_the_file, content):
    try:
        fh = open(path_to_the_file, 'wb')
        fh.write(content)
        fh.close()
    except:
        print('Wont save: %s' % (path_to_the_file))


if __name__ == '__main__':
    main()