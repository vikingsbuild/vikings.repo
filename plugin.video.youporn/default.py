#
#  Skin by: Tron Wizard for Kodi
#  YouPorn Code by Echo Coder
#
#  Copyright (C) 2016 
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
import os
import sys
import urllib
import urlparse
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import time
import base64
import re
import xbmcvfs
import urllib2,urllib
from lib import dom_parser2

DIALOG          = xbmcgui.Dialog()
DP              = xbmcgui.DialogProgress()
HOME            = xbmc.translatePath('special://home/')
ADDONS          = os.path.join(HOME,     'addons')
USERDATA        = os.path.join(HOME,     'userdata')
ADDON           = xbmcaddon.Addon()
ADDONID         = ADDON.getAddonInfo('id')
ADDONVERSION    = ADDON.getAddonInfo('version')
CWD             = ADDON.getAddonInfo('path').decode('utf-8')
ACTION_PREVIOUS_MENU = 10
ACTION_SELECT_ITEM = 7

AddonTitle = 'You Porn'
#Default veriables

base_domain     = 'https://www.youporn.com'
NEW_VIDS        = 'https://www.youporn.com/'
TOP_VIDS        = 'https://www.youporn.com/top_rated/'
MOST_FAV        = 'https://www.youporn.com/most_favorited/'
MOST_VIEW       = 'https://www.youporn.com/most_viewed/'
MOST_DIS        = 'https://www.youporn.com/most_discussed/'

class WindowXML(xbmcgui.WindowXML):
    def onInit(self):
        #Put list populating code/GUI startup things here
        self.window = xbmcgui.Window(xbmcgui.getCurrentWindowId())
        self.list_control = self.window.getControl(401)
        self.pornvids = self.window.getControl(402)
        self.categories()
        self.GET_CONTENT(NEW_VIDS,self.pornvids)

    def categories(self):
        c = self.open_url('https://www.youporn.com/categories')
        r = dom_parser2.parse_dom(c, 'div', {'class': re.compile('row\smost_popular')})
        r = dom_parser2.parse_dom(r, 'a')
        r = [(i.attrs['href'], \
            dom_parser2.parse_dom(i, 'span'), \
            dom_parser2.parse_dom(i, 'img', req='data-original')) \
            for i in r if i]
        r = [(urlparse.urljoin(base_domain,i[0]), i[2][0].attrs['alt'], i[1][0].content.split(' ')[0], i[2][0].attrs['data-original']) for i in r]
        
        for i in r:
            name = "[COLOR rose][B]" + i[1] + " - " + i[2] + "[/B][/COLOR]"
            self.list_control.addItem(xbmcgui.ListItem(name, label2=i[0], iconImage=i[3], thumbnailImage=i[3]))

    def GET_CONTENT(self,url,currentlist):
        global souperback
        global souperbad
        checker = url
        c = self.open_url(url)
        
        r = dom_parser2.parse_dom(c, 'div', {'class': ['video-box','four-column']})
        r = [(dom_parser2.parse_dom(i, 'a', req='href'), \
              dom_parser2.parse_dom(i, 'div', {'class': 'video-box-title'}), \
              dom_parser2.parse_dom(i, 'div', {'class': 'video-duration'}), \
              dom_parser2.parse_dom(i, 'img', req='src')) for i in r]
        r = [(urlparse.urljoin(base_domain,i[0][0].attrs['href']), i[1][0].content, i[2][0].content, i[3][0].attrs['src']) for i in r if i]
        
        for i in r:
            name = "[COLOR rose]" + i[1] + " - [" + i[2] + "][/COLOR]"
            currentlist.addItem(xbmcgui.ListItem(name, label2=i[0], iconImage=i[3], thumbnailImage=i[3]))
        np=re.compile('<li class="current"(.+?)<div id="next">',re.DOTALL).findall(c)
        for item in np:
            current=re.compile('<div class="currentPage" data-page-number=".+?">(.+?)</div>').findall(item)[0]
            url2=re.compile('<a href="(.+?)=').findall(item)[0]
            next1 = int(float(current)) + 1
            url = "https://youporn.com" + str(url2) + "=" + str(next1)
            souperbad = url
            if next1 != 2:
                back1 = int(float(current)) - 1
                souperback = "https://youporn.com" + str(url2) + "=" + str(back1)
            else:
                souperback = "https://youporn.com" + str(url2) + "=" + str(1)
    def SEARCH(self):
        string =''
        keyboard = xbmc.Keyboard(string, 'Enter Search Term')
        keyboard.doModal()
        if keyboard.isConfirmed():
            string = keyboard.getText().replace(' ','').capitalize()
            if len(string)>1:
                url = "https://www.youporn.com/search/?query=" + string + "&page="
                xbmc.log(url)
                self.GET_CONTENT(url,self.pornvids)
            else: quit()
    def open_url(self, url): req = urllib2.Request(url); req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'); \
        response = urllib2.urlopen(req); link = response.read(); return link
    def PLAY_URL(self,name,url,iconimage):
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        import urlresolver, xbmcvfs
        xxx_plugins_path = 'special://home/addons/script.module.urlresolver.xxx/resources/plugins/'
        if xbmcvfs.exists(xxx_plugins_path): urlresolver.add_plugin_dirs(xbmc.translatePath(xxx_plugins_path))

        try: u = urlresolver.HostedMediaFile(url).resolve()
        except:
            xbmc.executebuiltin("Dialog.Close(busydialog)")
            quit()
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        xbmc.Player ().play(u, liz, False)

    def onAction(self, action):
        if action == ACTION_PREVIOUS_MENU:
            self.close()
    def onClick(self,controlID):
        if controlID == 402:
            name = xbmc.getInfoLabel('Container(402).Listitem.Label')
            url = xbmc.getInfoLabel('Container(402).Listitem.Label2')
            icon = xbmc.getInfoLabel('Container(402).Listitem.Icon')
            self.PLAY_URL(name,url,icon)
        if controlID == 401:
            name = xbmc.getInfoLabel('Container(402).Listitem.Label')
            url = xbmc.getInfoLabel('Container(401).Listitem.Label2')
            try:
                while name:
                    self.pornvids.removeItem(0)
            except:
                self.GET_CONTENT(url,self.pornvids)
                xbmc.log(self.soup)
        if controlID == 502:
            name = xbmc.getInfoLabel('Container(402).Listitem.Label')
            try:
                while name:
                    self.pornvids.removeItem(0)
            except:
                xbmc.log(souperbad)
                self.GET_CONTENT(souperbad,self.pornvids)
        if controlID == 501:
            name = xbmc.getInfoLabel('Container(402).Listitem.Label')
            try:
                while name:
                    self.pornvids.removeItem(0)
            except:
                self.GET_CONTENT(souperback,self.pornvids)
                xbmc.log(souperback)
        if controlID == 503:
            self.close()
        if controlID == 504:
            name = xbmc.getInfoLabel('Container(402).Listitem.Label')
            try:
                while name:
                    self.pornvids.removeItem(0)
            except:
                self.SEARCH()
    def onFocus(self,controlID):
        pass
import threading
class Thread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
    def run(self):
        self._target(*self._args)
if __name__ == "__main__":
    scriptDir = xbmcaddon.Addon('plugin.video.youporn').getAddonInfo('path')
    sys.path.insert(0, os.path.join(scriptDir, 'resources', 'src'))
    w = WindowXML("home.xml", scriptDir)
    w.doModal()
    del w