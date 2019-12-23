# -*- coding: utf-8 -*-
from resources.lib import logger
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser

SITE_IDENTIFIER = 'kinoger_com'
SITE_NAME = 'Kinoger'
SITE_ICON = 'kinoger.png'

URL_MAIN = 'http://kinoger.com/'
URL_SERIE = URL_MAIN + 'stream/serie/'


def load():
    logger.info("Load %s" % SITE_NAME)
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('sUrl', URL_MAIN)
    oGui.addFolder(cGuiElement('Filme & Serien', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_SERIE)
    oGui.addFolder(cGuiElement('Genre', SITE_IDENTIFIER, 'showGenre'))
    oGui.addFolder(cGuiElement('Serien', SITE_IDENTIFIER, 'showEntries'), params)
    oGui.addFolder(cGuiElement('Suche', SITE_IDENTIFIER, 'showSearch'))
    oGui.setEndOfDirectory()


def showGenre():
    oGui = cGui()
    params = ParameterHandler()
    sHtmlContent = cRequestHandler(URL_MAIN).request()
    pattern = '</li><li[^>]class="links"><a[^>]href="([^"]+).*?/>([^<]+)</a>'
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    for sUrl, sName in aResult:
        params.setParam('sUrl', URL_MAIN + sUrl)
        oGui.addFolder(cGuiElement(sName, SITE_IDENTIFIER, 'showEntries'), params)
    oGui.setEndOfDirectory()


def showEntries(entryUrl=False, sGui=False, sSearchText=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    if not entryUrl: entryUrl = params.getValue('sUrl')
    oRequest = cRequestHandler(entryUrl, ignoreErrors=(sGui is not False))
    if sSearchText:
        oRequest.addParameters('story', sSearchText)
        oRequest.addParameters('do', 'search')
        oRequest.addParameters('subaction', 'search')
        oRequest.addParameters('x', '0')
        oRequest.addParameters('y', '0')
        oRequest.addParameters('titleonly', '3')
        oRequest.addParameters('submit', 'submit')
    else:
        oRequest.addParameters('dlenewssortby', 'date')
        oRequest.addParameters('dledirection', 'desc')
        oRequest.addParameters('set_new_sort', 'dle_sort_main')
        oRequest.addParameters('set_direction_sort', 'dle_direction_main')
    oRequest.setRequestType(1)
    sHtmlContent = oRequest.request()
    pattern = 'class="img"[^>]/>[^>]<a[^>]href="([^"]+).*?<img[^>]src="([^"]+).*?title="([^"]+)'
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)

    if not isMatch:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    cf = cRequestHandler.createUrl(entryUrl, oRequest)
    total = len(aResult)
    for sUrl, sThumbnail, sName in aResult:
        if sSearchText and not cParser().search(sSearchText, sName):
            continue
        sThumbnail = sThumbnail + cf
        isTvshow = True if 'staffel' in sName.lower() else False
        isYear, sYear = cParser.parse(sName, "(.*?)\((\d*)\)")
        for name, year in sYear:
            sName = name
            sYear = year
            break
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showSeasons' if isTvshow else 'showHosters')
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        if isYear:
            oGuiElement.setYear(sYear)
        oGuiElement.setMediaType('tvshow' if isTvshow else 'movie')
        params.setParam('sThumbnail', sThumbnail)
        params.setParam('TVShowTitle', sName)
        params.setParam('entryUrl', sUrl)
        oGui.addFolder(oGuiElement, params, isTvshow, total)
    if not sGui:
        isMatchNextPage, sNextUrl = cParser().parseSingleResult(sHtmlContent, '<a[^>]href="([^"]+)">vorwärts')
        if isMatchNextPage:
            params.setParam('sUrl', sNextUrl)
            oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)
        oGui.setView('tvshows' if 'staffel' in sName.lower() else 'movies')
        oGui.setEndOfDirectory()


def showSeasons():
    oGui = cGui()
    params = ParameterHandler()
    entryUrl = params.getValue('entryUrl')
    sThumbnail = params.getValue('sThumbnail')
    sTVShowTitle = params.getValue('TVShowTitle')
    sHtmlContent = cRequestHandler(entryUrl).request()
    pattern = "hdgo.show.*?</script>"
    isMatch, sContainer = cParser.parseSingleResult(sHtmlContent, pattern)

    if isMatch:
        pattern = "'([^\]]+)"
        isMatch, aResult = cParser.parse(sContainer, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    i = 0
    total = len(aResult)
    for sSeasonNr in aResult:
        i = i + 1
        oGuiElement = cGuiElement('Staffel ' + str(i), SITE_IDENTIFIER, 'showEpisodes')
        oGuiElement.setTVShowTitle(sTVShowTitle)
        oGuiElement.setSeason(i)
        if sThumbnail:
            oGuiElement.setThumbnail(sThumbnail)
            oGuiElement.setFanart(sThumbnail)
        params.setParam('sNr', i)
        params.setParam('sSeasonNr', sSeasonNr)
        oGui.addFolder(oGuiElement, params, True, total)
    oGui.setView('seasons')
    oGui.setEndOfDirectory()


def showEpisodes():
    oGui = cGui()
    params = ParameterHandler()
    sEpisodeNr = params.getValue('sSeasonNr')
    sNr = params.getValue('sNr')
    sThumbnail = params.getValue('sThumbnail')
    sTVShowTitle = params.getValue('TVShowTitle')
    pattern = "(http[^']+)"
    isMatch, aResult = cParser.parse(sEpisodeNr, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    i = 0
    total = len(aResult)
    for sEpisodeNr in aResult:
        i = i + 1
        oGuiElement = cGuiElement('Episode ' + str(i), SITE_IDENTIFIER, 'showHostersSerie')
        oGuiElement.setTVShowTitle(sTVShowTitle)
        oGuiElement.setSeason(sNr)
        oGuiElement.setEpisode(i)
        if sThumbnail:
            oGuiElement.setThumbnail(sThumbnail)
            oGuiElement.setFanart(sThumbnail)
        params.setParam('entryUrl', sEpisodeNr)
        oGui.addFolder(oGuiElement, params, False, total)
    oGui.setView('episodes')
    oGui.setEndOfDirectory()


def showHostersSerie():
    sUrl = ParameterHandler().getValue('entryUrl')
    oRequest = cRequestHandler(sUrl)
    oRequest.addHeaderEntry('Referer', sUrl)
    sHtmlContent = oRequest.request()
    pattern = '<iframe[^>]src="//([^"]+)'
    isMatch, sHtmlContent = cParser().parse(sHtmlContent, pattern)
    oRequest = cRequestHandler('http://' + sHtmlContent[0])
    oRequest.addHeaderEntry('Referer', sUrl)
    sHtmlContent = oRequest.request()
    pattern = "url:[^>]'([^']+)"
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)
    hosters = []
    for sUrl in aResult:
        q = Qualy(sUrl)
        hoster = {'link': sUrl + '|Referer=' + sUrl, 'name': 'hdgo.cc' + q}
        hosters.append(hoster)
    if hosters:
        hosters.append('getHosterUrl')
    return hosters


def showHosters():
    sUrl = ParameterHandler().getValue('entryUrl')
    sHtmlContent = cRequestHandler(sUrl).request()
    sPattern = '''(hdgo.show[^>].*?|<iframe[^>]src=")(http[^"']+)'''
    isMatch, aResult = cParser().parse(sHtmlContent, sPattern)
    hosters = []
    if isMatch:
        for dummy, sUrl in aResult:
            if 'hdgo.cc' in sUrl:
                oRequest = cRequestHandler(sUrl)
                oRequest.addHeaderEntry('Referer', sUrl)
                sHtmlContent = oRequest.request()
                pattern = '<iframe[^>]src="//([^"]+)'
                isMatch, sHtmlContent = cParser().parse(sHtmlContent, pattern)
                oRequest = cRequestHandler('http://' + sHtmlContent[0])
                oRequest.addHeaderEntry('Referer', sUrl)
                sHtmlContent = oRequest.request()
                pattern = "url:[^>]'([^']+)"
                isMatch, aResult = cParser().parse(sHtmlContent, pattern)

                for sUrl in aResult:
                    q = Qualy(sUrl)
                    hoster = {'link': sUrl, 'name': 'hdgo.cc' + q}
                    hosters.append(hoster)

            elif 'getvi.tv' in sUrl:
                oRequest = cRequestHandler(sUrl)
                oRequest.addHeaderEntry('Referer', sUrl)
                sHtmlContent = oRequest.request()
                pattern = '''\[([0-9p]+)\](http(?:[^'",]+))'''
                isMatch, aResult = cParser().parse(sHtmlContent, pattern)

                for sQualy, sUrl in aResult:
                    hoster = {'link': sUrl, 'name': 'getvi.tv ' + sQualy}
                    hosters.append(hoster)
            else:
                sName = cParser.urlparse(sUrl)
                hoster = {'link': sUrl, 'name': sName}
                hosters.append(hoster)
    if hosters:
        hosters.append('getHosterUrl')
    return hosters


def getHosterUrl(sUrl=False):
    if sUrl.startswith('//'):
        sUrl = 'https:' + sUrl
    return [{'streamUrl': sUrl + '|Referer=' + sUrl + '&User-Agent=Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0', 'resolved': True}]


def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if not sSearchText: return
    _search(False, sSearchText)
    oGui.setEndOfDirectory()


def _search(oGui, sSearchText):
    showEntries(URL_MAIN, oGui, sSearchText)


def Qualy(sUrl):
    if '/1/' in sUrl:
        return ' 360p'
    elif '/2/' in sUrl:
        return ' 480p'
    elif '/3/' in sUrl:
        return ' 720p'
    elif '/4/' in sUrl:
        return ' 1080p'
    else:
        return ' SD'
