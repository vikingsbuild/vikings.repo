# -*- coding: utf-8 -*-

import requests, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, urllib
from threading import Thread
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.bestporn')
ICON = xbmc.translatePath('special://home/addons/plugin.video.bestporn/icon.png')
fanarts = 'https://i.imgur.com/Qw9DExk.jpg'
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')
ADDON_DATA = USERDATA_PATH + '/plugin.video.bestporn/'
favourites = ADDON_DATA + 'favourites'
if os.path.exists(favourites) == True:
    FAV = open(favourites).read()
else:
    FAV = []
next_page_con = 'https://i.imgur.com/s1x9dPi.png'
best_porn_base = 'http://collectionofbestporn.com/'

def Main_Menu():
    Menu('Popular','http://collectionofbestporn.com/',21,ICON,fanarts,'','')
    Menu('Latest','http://collectionofbestporn.com/most-recent',21,ICON,fanarts,'','')
    Menu('HD','http://collectionofbestporn.com/tag/hd-porn/newest',21,ICON,fanarts,'','')
    Menu('Top Rated','http://collectionofbestporn.com/top-rated',21,ICON,fanarts,'','')
    Menu('Longer Videos','http://collectionofbestporn.com/longest',21,ICON,fanarts,'','')
    Menu('Categories','http://collectionofbestporn.com/channels/',23,ICON,fanarts,'','')
    Menu('Search','',2,ICON,fanarts,'','')



# mode 21
def best_porn_vids(url):
        html = requests.get(url).content
        match = re.compile('class="video-item.+?href="(.+?)".+?src="(.+?)".+?tle="(.+?)".+?class="time">(.+?)</span>.+?</div>',re.DOTALL).findall(html)
        for page, iconz, title, time in match:
            name = '[COLORdodgerblue]%s[/COLOR] - %s' % (time,title)
            Play(name,page,22,iconz,'','','')
        next_page = re.compile('class="row\s*pagination-row">.+?class="next".+?href=\'(.+?)\'>.+?</div>',re.DOTALL).findall(html)   
        for more in next_page:
            more = best_porn_base+more
            Menu('Next Page',more,21,next_page_con,'','','')



#mode 23
def cat_page(url):
    html = requests.get(url).content
    match = re.compile('class="video-item.+?href="(.+?)">.+?src="(.+?)".+?span>(.+?)</span></a>.+?</div>',re.DOTALL).findall(html)
    for page,icon,name in match:
        page = page.replace('" title="','')
        Menu(name,page,24,icon,'','','')

#mode 24
def get_cat(url):
    html = requests.get(url).content
    match = re.compile('class="video-item.+?href="(.+?)".+?src="(.+?)".+?tle="(.+?)".+?class="time">(.+?)</span>.+?</div>',re.DOTALL).findall(html)
    for page,icon,title,time in match:
        name = '[COLORdodgerblue]%s[/COLOR] - %s' % (time,title)
        Play(name,page,22,icon,'','','')
    next_page = re.compile('class="row\s*pagination-row">.+?class="next".+?href=\'(.+?)\'>.+?</div>',re.DOTALL).findall(html)   
    for more in next_page:
        more = best_porn_base+more
        Menu('Next Page',more,24,next_page_con,'','','')

def Search():
    Search_url = 'http://collectionofbestporn.com/search/'
    Dialog = xbmcgui.Dialog()
    Search_title = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_name = Search_title.replace(' ','-').lower()
    Search_url = Search_url+Search_name
    html = requests.get(Search_url).content
    match = re.compile('<!-- v item -->.+?href="(.+?)".+?src="(.+?)"\s*title="(.+?)".+?class="time">(.+?)</span>.+?</div>.+?<!-- v item end -->',re.DOTALL).findall(html)
    for page,icon,title,time in match:
        name = '[COLORdodgerblue]%s[/COLOR] - %s' % (time,title)
        Play(name,page,22,icon,'','','')
    next_page = re.compile('class="row\s*pagination-row">.+?class="next".+?href=\'(.+?)\'>.+?</div>',re.DOTALL).findall(html)   
    for more in next_page:
        more = best_porn_base+more
        Menu('Next Page',more,24,next_page_con,'','','')    
    
def setView(content, viewType):
    
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )

#mode 22
def best_porn_links(url):
    html = requests.get(url).content
    match = re.compile('<h1>(.+?)</h1></div>.+?src=".+?"></script>.+?src=".+?"></script>.+?poster="(.+?)".+?src="(.+?)".+?</video>.+?class="time">(.+?)</li>.+?</ul>',re.DOTALL).findall(html)
    for title, pic, url, time in match:
        resolve(name,url)        
        
def Menu(name,url,mode,iconimage,fanart,description,extra,showcontext=False,allinfo={}):
        fav_mode = mode
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&extra="+urllib.quote_plus(extra)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from test Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to test Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), fav_mode, urllib.quote_plus(fanart), urllib.quote_plus(description))))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        

        
def Play(name,url,mode,iconimage,fanart,description,extra,showcontext=False,allinfo={}):
        fav_mode = mode
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&extra="+urllib.quote_plus(extra)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from test Favorites','XBMC.RunPlugin(%s?mode=12&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to test Favourites','XBMC.RunPlugin(%s?mode=11&name=%s&url=%s&iconimage=%s&fav_mode=%s&fanart=%s&description=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), fav_mode, urllib.quote_plus(fanart), urllib.quote_plus(description))))
            liz.addContextMenuItems(contextMenu)
            contextMenu.append(('Queue Item', 'RunPlugin(%s?mode=14)' % sys.argv[0]))
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        
# ===============================Favourites-----------Not sure whos code this is but credit due to them-------------------------------

def addFavorite(name, url, mode, iconimage, fanart, description, extra):
    favList = []
    xbmc.log(extra)
    try:
        name = name.encode('utf-8', 'ignore')
    except:
        pass
    if os.path.exists(favourites) == False:
        favList.append((name, url, mode, iconimage, fanart, description, extra))
        a = open(favourites, "w")
        a.write(json.dumps(favList))
        a.close()
    else:
        a = open(favourites).read()
        data = json.loads(a)
        data.append((name, url, mode, iconimage, fanart, description, extra))
        b = open(favourites, "w")
        b.write(json.dumps(data))
        b.close()


def getFavourites():
    if not os.path.exists(favourites):
        favList = []
        favList.append(('test Favourites Section', '', '', '', '', '', ''))
        a = open(favourites, "w")
        a.write(json.dumps(favList))
        a.close()
    else:
        items = json.loads(open(favourites).read())
        for i in items:
            name = i[0]
            url = i[1]
            try:
                iconimage = i[3]
            except:
                iconimage = ''
            try:
                fanart = i[4]
            except:
                fanart = ''
            try:
                description = i[5]
            except:
                description = ''
            try:
                extra = i[6]
            except:
                extra = ''

            if i[2] == 20:
                Play(name, url, i[2], iconimage, fanart, description, extra, 'fav')
            else:
                Menu(name, url, i[2], iconimage, fanart, description, extra, 'fav')


def rmFavorite(name):
    data = json.loads(open(favourites).read())
    for index in range(len(data)):
        if data[index][0] == name:
            del data[index]
            b = open(favourites, "w")
            b.write(json.dumps(data))
            b.close()
            break
    xbmc.executebuiltin("XBMC.Container.Refresh")       

def resolve(name,url): 
    xbmc.Player().play(url, xbmcgui.ListItem(name))
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2: 
                params=sys.argv[2] 
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}    
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
        
params=get_params()
url=None
name=None
iconimage=None
mode=None
fanart=None
description=None
trailer=None
fav_mode=None
extra=None

try:
    extra=urllib.unquote_plus(params["extra"])
except:
    pass

try:
    fav_mode=int(params["fav_mode"])
except:
    pass

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass

#####################################################END PROCESSES##############################################################        
        
if mode == None: Main_Menu()
elif mode == 2 : Search()

elif mode == 10: getFavourites()
elif mode==11:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    addFavorite(name, url, fav_mode, iconimage, fanart, description, extra)
elif mode==12:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    rmFavorite(name)
elif mode == 14 : queueItem()   
elif mode == 20: resolve(name,url)
elif mode == 21: best_porn_vids(url)
elif mode == 22: best_porn_links(url)
elif mode == 23: cat_page(url)
elif mode == 24: get_cat(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))