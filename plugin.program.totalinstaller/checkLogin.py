#      Copyright (C) 2015 whufclee
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import os, re, xbmc, urllib, urllib2, binascii, xbmcaddon, xbmcgui

AddonID      = 'plugin.program.totalinstaller'
ADDON        =  xbmcaddon.Addon(id=AddonID)
username     =  ADDON.getSetting('username').replace(' ','%20')
password     =  ADDON.getSetting('password')
dialog       =  xbmcgui.Dialog()
userinforaw  = '687474703a2f2f6e6f6f6273616e646e657264732e636f6d2f54492f6c6f67696e2f6c6f67696e5f64657461696c732e7068703f757365723d257326706173733d2573'
BaseURL = binascii.unhexlify(userinforaw) % (username, password)
xbmc.log(BaseURL)

def Open_URL(url):
    req      = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link     = response.read()
    response.close()
    return link.replace('\r','').replace('\n','').replace('\t','')

link         = Open_URL(BaseURL).replace('\n','').replace('\r','')
welcomematch = re.compile('login_msg="(.+?)"').findall(link)
welcometext  = welcomematch[0] if (len(welcomematch) > 0) else ''

xbmc.executebuiltin('Dialog.Show(busydialog)')

if username.replace('%20',' ') in welcometext:
    dialog.ok('LOGIN SUCCESS','Congratulations your login credentials are correct','and this add-on is now fully unlocked.')

else:
    dialog.ok('There is a problem with your login details', 'Please make sure you entered your [COLOR=dodgerblue]username[/COLOR].', 'An email address and a username is NOT the same thing.', '[CR]Remember both username and password ARE case sensitive.')

xbmc.executebuiltin('Dialog.Close(busydialog)')
ADDON.openSettings()
xbmc.executebuiltin('ActivateWindow(10001,"plugin://plugin.program.totalinstaller&mode=None)')
