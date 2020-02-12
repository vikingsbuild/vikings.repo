# -*- coding: utf-8 -*-
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib import logger
from resources.lib.config import cConfig
import re, time, xbmcgui


SITE_IDENTIFIER = 'animes-stream24_tv'
SITE_NAME = 'Animes-Stream24'
SITE_ICON = 'as24.png'
URL_MAIN = 'http://as.animes-stream24.tv/'
SITE_GLOBAL_SEARCH = False

def load():
    oGui = cGui()
    params = ParameterHandler()
    logger.info("Load %s" % SITE_NAME)
    if showAdult(True): #Adult object off
        params.setParam('entryMode', "a_z")
        oGui.addFolder(cGuiElement('A BIS Z', SITE_IDENTIFIER, 'showMovies'), params)
        params.setParam('entryMode', "top_animes")
        oGui.addFolder(cGuiElement('Top', SITE_IDENTIFIER, 'showMovies'), params)
        params.setParam('entryMode', "new")
        oGui.addFolder(cGuiElement('Neuste Animes', SITE_IDENTIFIER, 'showMovies'), params)
        params.setParam('entryMode', "a_z")
        oGui.addFolder(cGuiElement('Suche', SITE_IDENTIFIER, 'showSearch'), params)
    else: 
        oGui.addFolder(cGuiElement('Um Inhalte sehen zu können, muss der Adult Content aktiviert werden. \n(Klicke hier, um diese zu öffnen)', SITE_IDENTIFIER, 'getConf'), params)
    oGui.setEndOfDirectory()

    
def showMovies(sURL = False, sGui = False, sSearchText = ""):

    oGui = sGui if sGui else cGui()
    if not sURL: sURL = URL_MAIN
    params = ParameterHandler()
    eMode = ""
    if not eMode:
        eMode = params.getValue('entryMode')
    else:
        eMode = "ERROR"

    if "top_animes" in eMode:
        pattern = 'class="separator".*?<a href="([^"]+)".*?' #link
        pattern += '<img src="([^"]+)".*?' #img
        pattern += '([^><]+)</a>' #titel
    elif "a_z" in eMode:
        pattern = "<option value='([^']+)'>([^><]+)</option>" #link, titel
    elif "new" in eMode:
        sURL = sURL + "search?updated-max=" + time.strftime("%Y-%m-%d") + "T08:48:00%2B01:00&max-results="
        pattern = False
        aResult = False
    else:
        if not sGui: oGui.showInfo('xStream', eMode)
        return

    if pattern:
        oRequestHandler = cRequestHandler(sURL)
        sHtmlContent = oRequestHandler.request()
        oParser = cParser()
        aResult = oParser.parse(sHtmlContent, pattern)

        if not aResult[0]:
            if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
            return

        total = len(aResult[1])
        qual = "1080"

    if "top_animes" in eMode:
       for link, img, title in aResult[1]:
          guiElement = cGuiElement(title, SITE_IDENTIFIER, 'getEpisodes')
          guiElement.setThumbnail(img)
          #guiElement.setDescription(plot.decode('iso-8859-1'))
          guiElement.setMediaType('movie')
          params.setParam('eUrl',link)
          oGui.addFolder(guiElement, params, bIsFolder = True, iTotal = total)
    elif "new" in eMode:
       ymd_date = time.strftime("%Y-%m-%d")
       params.setParam('eUrl',sURL + "11")
       oGui.addFolder(cGuiElement("Zeige letzte 11 Einträge (" + ymd_date +")", SITE_IDENTIFIER, 'getEpisodes'),params)
       params.setParam('eUrl',sURL + "22")
       oGui.addFolder(cGuiElement("Zeige letzte 22 Einträge (" + ymd_date +")", SITE_IDENTIFIER, 'getEpisodes'),params)
       params.setParam('eUrl',sURL + "44")
       oGui.addFolder(cGuiElement("Zeige letzte 44 Einträge (" + ymd_date +")", SITE_IDENTIFIER, 'getEpisodes'),params)
    elif "a_z" in eMode:
       #sPattern = params.getValue('search_on')
       sPattern = sSearchText; a = []
       reg_ex = re.compile('.*' + sSearchText + '.*?', re.I)
       pattern = "class='post-title entry-title'><a href='([^']+)'>" #link
       pattern += "([^><]+).*?" #ep_Name
       pattern += '<img.*?src="([^"]+)".*?bung:.*?/>' #Img
       pattern += "(.*?)<br./>" #plot /Gen
       
       if sPattern:
           for link, title in aResult[1]:
              if re.search(reg_ex,title):
                guiElement = cGuiElement(title, SITE_IDENTIFIER, 'getEpisodes')
                sHtml = cRequestHandler(link).request()
                a = oParser.parse(sHtml, pattern)
                #xbmcgui.Dialog().ok("SHOW",str(a[1][1][3])) #.encode("utf-8"))
                guiElement.setThumbnail(a[1][1][2])
                guiElement.setDescription(a[1][1][3])
                params.setParam('eUrl',link)
                oGui.addFolder(guiElement, params, bIsFolder = True, iTotal = total)
       else:
           for link, title in aResult[1]:
              guiElement = cGuiElement(title, SITE_IDENTIFIER, 'getEpisodes')
              
              """
                TODO: ERROR HANDLING OUT OF RANGE - LAEDT SONST EWIG FUER DEN REQUEST
                    EVENTL AUFTEILEN ODER EINZELNE THREADS??
                ----------------------------------------------------------------------
                sHtml = cRequestHandler(link).request()
                a = oParser.parse(sHtml, pattern)
                guiElement.setThumbnail(a[1][1][2])
                guiElement.setDescription(a[1][1][3].decode('iso-8859-1').encode('utf-8'))
              """ 
            
              params.setParam('eUrl',link)
              oGui.addFolder(guiElement, params, bIsFolder = True, iTotal = total)

    oGui.setView('movies')
    oGui.setEndOfDirectory()

def getEpisodes():
    oGui = cGui()
    oParser = cParser()
    params = ParameterHandler()
    eUrl = ParameterHandler().getValue('eUrl')
    eUrl = eUrl.replace(" ", "%20"); eUrl = eUrl.replace("+", "%2B") #Decode(Leerzeichen, +)
    isMovie = True

    pattern = "class='post-title entry-title'><a href='([^']+)'>" #link
    pattern += "([^><]+).*?" #ep_Name
    pattern += '<img.*?src="([^"]+)".*?bung:.*?/>' #Img
    pattern += "(.*?)<br./>" #plot /Gen

    sHtmlContent = cRequestHandler(eUrl).request()
    aResult = oParser.parse(sHtmlContent, pattern)
    bResult = oParser.parse(sHtmlContent, "older-link'.*?href='([^']+)'")

    if not aResult[0]:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    total = len(aResult[1]) 
    for link, title, img, plot in aResult[1]:
        GuiElement = cGuiElement(title, SITE_IDENTIFIER, 'getHosters')
        GuiElement.setMediaType('movie' if isMovie else 'tvshow')
        GuiElement.setThumbnail(img)
        plot.replace('<b>', '')
        GuiElement.setDescription(plot)#.decode('iso-8859-1').encode('utf-8'))
        #GuiElement.setYear(year)
        params.setParam('siteUrl', link)
        params.setParam('sName', title)
        oGui.addFolder(GuiElement, params, False, total)

    if 'entry-title' in cRequestHandler(bResult[1][0]).request():
        params.setParam('eUrl', bResult[1][0])
        oGui.addFolder(cGuiElement("Weitere Episoden -->", SITE_IDENTIFIER, 'getEpisodes'),params)
    
    #logger.info('[[AZ24]] %s: ' % str(bResult[1][0]))    
    oGui.setView('movies')
    oGui.setEndOfDirectory()

def getHosters():
    oParams = ParameterHandler()
    oGui = cGui()
    sUrl = oParams.getValue('siteUrl')

    sHtmlContent = cRequestHandler(sUrl).request()

    sPattern = '(?:<iframe|<IFRAME).*?(?:src|SRC)="([^"]+).*?(?:\<\/if|\<\/IF)'
    sPattern_bkp = '-[0-9]".?>.*?(?:src|SRC)="([^"]+)".*?'
    aResult = cParser().parse(sHtmlContent, sPattern)

    if aResult[0]:
        hosters = []
        #test_link = '*.m3u8'
        #hosters.append({'link': test_link + '##testing', 'name': 'Test LAB', 'resolveable': True})
        reg_ex = re.compile('(?://|\.)?(?:[a-zA-Z0-9]+\.)?([a-zA-Z0-9-.]{0,})\..*?\/.*?\/?', re.I)
        for sUrl in aResult[1]:
            #CHECK IF PL.AS24 RESOLVE
            if 'pl.anime-stream24' in sUrl:
                sUrl = _plas24_resolver(sUrl)           
            sName = re.search(reg_ex, sUrl).group(1)
            
            if not sUrl.startswith('http'):
                if sUrl.startswith('//'):
                    sUrl = 'http:%s' % sUrl
                else:
                    sUrl = 'http://%s' % sUrl
            hosters.append({'link': sUrl, 'name': sName, 'resolveable': True})
        
        if hosters:
            hosters.append('getHosterUrl')
        
        logger.info('[[AZ24]] HOSTER ARRAY %s ' % str(hosters))
        return hosters
    else:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')

def getHosterUrl(sUrl=False):
    if not sUrl:
        sUrl = ParameterHandler().getValue('sUrl')

    if 'animes-stream24.net' in sUrl:
        sUrl = _as24_resolver(sUrl)
        res = True
    elif 'ani-stream.com' in sUrl: #DOT|net=off
        sUrl = _anistream_resolver(sUrl)
        res = True
    elif 'uploadkadeh.com' in sUrl:
        sUrl = 'http://uploadkadeh.com:182/d/' + _webtv_resolver(sUrl) + '/video.mp4'
        res = True
    elif sUrl in set(['web.tv','plublicvideohost.org']): #or bigfile.to
        sUrl = _webtv_resolver(sUrl)
        res = True
    elif 'cloudvideo.tv' in sUrl:
        sUrl = _webtv_resolver(sUrl)
        res = True
    elif 'testing' in sUrl:
        res = True
    else:
        res = False

    results = []
    result = {}
    #logger.info('[[AS24]] Url %s after:getHosterUrl(): ' % sUrl)
    result['streamUrl'] = sUrl
    result['resolved'] = res
    results.append(result)
    return results #play > [sUrl,[BOOL]]

def _plas24_resolver(url):
    sHtmlContent = cRequestHandler(url).request()
    match = re.findall('<iframe src="(.+?)"', sHtmlContent)
    if match:
        url = match[0]
        #content = requests.get(url, headers=headers).text.replace('\\','')
        if url:
            try:
                url = _redirectHoster(url, True, True)
            except Exception as e:
                pass #if ignore
                logger.info('Failed [AS24 LAB]: '+ str(e))
                url = "http://hoster.offline.off/off"
            return url
        else:
            xbmc.executebuiltin('Notification(Info: Error: URL,)')
            
def _as24_resolver(url):
    oParams = ParameterHandler()
    sHtmlContent = cRequestHandler(url).request()
    #sUrl = re.search("\{file:'([^']+)'", sHtmlContent, re.I).group(1)
    #redi = re.search("(http://.*?/)", sUrl, re.I).group(1) #getHosturl http://[HOST.DMN]/
    aResult = cParser().parse(sHtmlContent, '''\{file:.?(?:"|')([^'"]+)(?:"|').+''')
    redi = "http://as.animes-stream24.net/" # \.open\('(.+)'\)\;
 
    for sUrl in aResult[1]:
        if sUrl and redi:
            #sUrl = _redirectHoster(sUrl, sUrl, False)
            return sUrl
        else:
            return sUrl

def _webtv_resolver(url):
    oParams = ParameterHandler()
    sHtmlContent = cRequestHandler(url).request()
 
    if 'web.tv' in url:
        aResult = cParser().parse(sHtmlContent, '"sources.*?src.."(.*?)"}]')
    if 'publicvideohost.org' in url:
        pattern = '(?:file|source)+?:.?(?:"|'
        pattern += "')(.*?.flv+)(?:"
        pattern += '"|' + "')"
        aResult = cParser().parse(sHtmlContent, pattern)
        #(?:file|source)+?:.?(?:"|')(.*?.[a-zA-Z0-9]{2,3}+)(?:"|')
    if 'uploadkadeh.com' in url:
        aResult = cParser().parse(sHtmlContent, 'player_code.*?video\|([^\|]+)')
    if 'cloudvideo.tv' in url:
        aResult = cParser().parse(sHtmlContent, 'source..*?"(.+?)"')
        
    for sUrl in aResult[1]:
        if sUrl:
            return sUrl
        else:
            xbmcgui.Dialog().ok( "Fehler" , 'Error 666: ' + sUrl)
 
def _anistream_resolver(o_url):
    oParams = ParameterHandler()
    sHtmlContent = cRequestHandler(o_url).request()

    match = re.findall("file\s*:\s*(?:'|\")(.+?)(?:\'|\")", sHtmlContent)
    if match:
        url = match[0]
        #content = requests.get(url, headers=headers).text.replace('\\','')
        if url:
            try:
                #r = requests.head(url[0], headers=headers)
                #if r.headers.get('location'):
                    #url = [r.headers.get('location')]
                #logger.info('[[suhmser]] Url %s _anistream_Resolver(): ' % url)
                url = _redirectHoster(url)
            except:
                pass
            return url
        else:
            xbmc.executebuiltin('Notification(Info: Error: NO URL)')

def _redirectHoster(url, ref = False, cookie = False):

    if url:
       import urllib2
       ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"
       def req(url): 
           request = urllib2.Request(url)
           request.add_header('User-Agent', ua)
           if ref: request.add_header('Referer', ref)
           return request
           
       request = req(url)
       response = urllib2.urlopen(request, timeout=244) #Bypass Timeout Issues    
       
       if cookie or 'Set-Cookie' in response.info(): 
           request = req(URL_MAIN)
           res = urllib2.urlopen(request, timeout=12)
           cookie = res.info()['Set-Cookie'] #Get Cookieinfo
      
       if cookie:
           request.add_header('Cookie',cookie)
      
       if url != response.geturl():
           return response.geturl()
       else:
           return url

def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if not sSearchText: return

    # Filter Typ als Parameter (optional)
    sType = ParameterHandler().getValue('sType')
    if sType:
        sSearchText = sSearchText.strip() + "&type="+sType

    _search(False, sSearchText)
    oGui.setEndOfDirectory()

def _search(oGui, sSearchText):
    if not sSearchText: return
    ParameterHandler().setParam('search_on', sSearchText)
    showMovies(False, oGui, sSearchText)

def showAdult(switch = False):
    oConfig = cConfig()
    if oConfig.getSetting('showAdult')=='true':
        return True
    return switch

def getConf():
    oGui = cGui()
    oGui.openSettings()
    
