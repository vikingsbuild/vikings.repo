# -*- coding: utf-8 -*-
# Author: Lord Grey
# Created : 02.03.2019
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
import xbmcgui
import xbmcplugin
import resources.lib.xvideos as xvideos
import resources.lib.helper as helper

try:
    from urllib2 import urlparse
except ImportError:
    import urllib.parse as urlparse

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]

# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

if __name__ == '__main__':

    # We use string slicing to trim the leading '?'
    # from the plugin call paramstring
    paramstring = sys.argv[2][1:]

    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(urlparse.parse_qsl(paramstring))
    # xbmc.log(str(params),level=xbmc.LOGNOTICE)

    # Check the parameters passed to the plugin give new and restart
    # quit() is needed at the end of each if

    #################################
    #           1st Start           #
    #################################
    if params == {}:
        # Search
        list_item = xbmcgui.ListItem(label='Search')
        url = helper.get_url(_url, action='search')
        is_folder = True
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)

        # endOfDirectory
        xbmcplugin.endOfDirectory(_handle)
        quit()

    #################################
    #             play              #
    #################################
    if params['action'] == 'play':
        # Play a video from a provided URL.
        xvideos.play_video(_handle, params['video'])
        quit()

    #################################
    #            search             #
    #################################
    if params['action'] == 'search':
        s_therm = helper.get_search()

        if s_therm == None:
            quit()

        dialog = xbmcgui.Dialog()
        ret = dialog.select('Search by',
                            ['Relevance', 'Upload Date',
                             'Raiting', 'Length', 'Views'])

        if ret == 0:
            sort = '&sort=relevance'
        if ret == 1:
            sort = '&sort=uploaddate'
        if ret == 2:
            sort = '&sort=raiting'
        if ret == 3:
            sort = '&sort=length'
        if ret == 4:
            sort = '&sort=views'

        link = 'https://www.xvideos.com/?k=' + s_therm + sort
        videos = xvideos.get_vids(link, 'search')
        has_next = True

        helper.list_videos(_handle, _url, videos,
                           link, 'search', has_next)
        quit()

    #################################
    #              next             #
    #################################
    if params['action'] == 'next':
        # ads a &p= at first and raises the page number every call

        if params['page'] == '1':
            url = params['link'] + '&p=' + str(params['page'])
        else:
            url = params['link'] + str(params['page'])

        page = int(params['page']) + 1
        videos = xvideos.get_vids(url, params['category'])

        if int(videos[0]['page']) == page:
            has_next = False
        else:
            has_next = True

        helper.list_videos(_handle, _url, videos, url,
                           params['category'], has_next, page)
        quit()

    #################################
    #             error             #
    #################################
    # If the provided paramstring does not contain a supported action
    # we raise an exception. This helps to catch coding errors,
    # e.g. typos in action names.
    raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    quit()
