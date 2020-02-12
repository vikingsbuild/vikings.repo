# -*- coding: utf-8 -*-
from resources.lib import logger
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser

SITE_IDENTIFIER = 'cinemaxx_cc'
SITE_NAME = 'Cinemaxx'
SITE_ICON = 'cinemaxx_cc.png'

URL_MAIN = 'http://cinemaxx.cc'
URL_FILME = URL_MAIN + '/filme/'
URL_KINO = URL_MAIN + '/kinofilme/'
URL_SERIE = URL_MAIN + '/serien/'
URL_TVSHOWS = URL_MAIN + '/tv-shows/'
URL_DOKUS = URL_MAIN + '/dokumentationen/'


def load():
    logger.info("Load %s" % SITE_NAME)
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('sUrl', URL_KINO)
    oGui.addFolder(cGuiElement('Kino Filme', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_FILME)
    oGui.addFolder(cGuiElement('Filme', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_SERIE)
    oGui.addFolder(cGuiElement('Serien', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_TVSHOWS)
    oGui.addFolder(cGuiElement('TV-Shows', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_DOKUS)
    oGui.addFolder(cGuiElement('Dokus', SITE_IDENTIFIER, 'showEntries'), params)
    oGui.addFolder(cGuiElement('Genre', SITE_IDENTIFIER, 'showGenre'))
    oGui.addFolder(cGuiElement('Suche', SITE_IDENTIFIER, 'showSearch'))
    oGui.setEndOfDirectory()


def showGenre():
    oGui = cGui()
    params = ParameterHandler()
    sHtmlContent = cRequestHandler(URL_MAIN).request()
    isMatch, sContainer = cParser.parseSingleResult(sHtmlContent, ">Genres.*?</ul>")

    if isMatch:
        pattern = '<a[^>]*href="([^"]+)".*?>([^"]+)</a>'
        isMatch, aResult = cParser.parse(sContainer, pattern)

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
        oRequest.addParameters('do', 'search')
        oRequest.addParameters('full_search', '0')
        oRequest.addParameters('search_start', '0')
        oRequest.addParameters('story', sSearchText)
        oRequest.addParameters('subaction', 'search')
        oRequest.addParameters('result_from', '1')
        oRequest.addParameters('submit', 'submit')
        oRequest.setRequestType(1)
    sHtmlContent = oRequest.request()
    pattern = '<div[^>]id="mainbar.*?<div[^>]class="clearfix'
    isMatch, sContainer = cParser().parseSingleResult(sHtmlContent, pattern)

    if isMatch:
        pattern = '<div[^>]class="shortstory-in">.*?<a[^>]href="([^"]+)"[^>]title="([^"]+).*?<img[^>]src="([^"]+).*?<span class="film-rip">(.*?)</span>'
        isMatch, aResult = cParser().parse(sContainer, pattern)

    if not isMatch:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    cf = cRequestHandler.createUrl(entryUrl, oRequest)
    total = len(aResult)
    for sUrl, sName, sThumbnail, sDummy in aResult:
        if sSearchText and not cParser().search(sSearchText, sName):
            continue
        isTvshow = True if 'Staffel' in sDummy else False
        sThumbnail = sThumbnail + cf
        if isTvshow:
            if not 'Staffel' in sName:
                isMatch, st = cParser().parseSingleResult(sDummy, 'Staffel.*?([\d]+).*?</a>')
                if isMatch:
                    sName = sName + ' ' + st + ' Staffel'
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showEpisodes' if isTvshow else 'showHosters')
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        oGuiElement.setMediaType('tvshow' if isTvshow else 'movie')
        params.setParam('sThumbnail', sThumbnail)
        params.setParam('TVShowTitle', sName)
        params.setParam('entryUrl', sUrl)
        oGui.addFolder(oGuiElement, params, isTvshow, total)
    if not sGui:
        isMatchNextPage, sNextUrl = cParser().parseSingleResult(sHtmlContent, 'pages-next">[^>][^>][^>][^>][^>]<a href="([^"]+)"')
        if isMatchNextPage:
            params.setParam('sUrl', sNextUrl)
            oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)
        oGui.setView('tvshows' if 'staffel' in sName.lower() else 'movies')
        oGui.setEndOfDirectory()


def showEpisodes():
    oGui = cGui()
    params = ParameterHandler()
    entryUrl = params.getValue('entryUrl')
    sThumbnail = params.getValue('sThumbnail')
    sTVShowTitle = params.getValue('TVShowTitle')
    oRequest = cRequestHandler(entryUrl)
    oRequest.addHeaderEntry('Referer', entryUrl)
    sHtmlContent = oRequest.request()
    pattern = 'vk.show.*?</script>'
    isMatch, sContainer = cParser.parseSingleResult(sHtmlContent, pattern)
    if isMatch:
        pattern = "(http[^',]+)"
        isMatch, aResult = cParser.parse(sContainer, pattern)
    if not isMatch:
        pattern = '<iframe[^>]src="([^"]+)'
        isMatch, sUrl = cParser().parse(sHtmlContent, pattern)
        if isMatch:
            oRequest = cRequestHandler('' + sUrl[0])
            oRequest.addHeaderEntry('Referer', entryUrl)
            sUrl = oRequest.request()
            pattern = '<iframe[^>]src="([^"]+)'
            isMatch, sUrl = cParser().parse(sUrl, pattern)
        if isMatch:
            oRequest = cRequestHandler('http:' + sUrl[0])
            oRequest.addHeaderEntry('Referer', entryUrl)
            sUrl = oRequest.request()
            pattern = "var[^>]season_list.*?var"
            isMatch, sContainer = cParser.parseSingleResult(sUrl, pattern)
            pattern = '"([^",]+)'
            isMatch, aResult = cParser.parse(sContainer, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    i = 0
    isDesc, sDesc = cParser.parseSingleResult(sHtmlContent, 'description[^>]*content="([^"]+)')
    total = len(aResult)
    for sUrl in aResult:
        i = i + 1
        oGuiElement = cGuiElement('Episode ' + str(i), SITE_IDENTIFIER, 'showHosters')
        oGuiElement.setTVShowTitle(sTVShowTitle)
        oGuiElement.setEpisode(i)
        if sThumbnail:
            oGuiElement.setThumbnail(sThumbnail)
            oGuiElement.setFanart(sThumbnail)
        if isDesc:
            oGuiElement.setDescription(sDesc)
        if 'hdgo' in sUrl:
            params.setParam('entryUrl', sUrl)
        else:
            params.setParam('entryUrl', 'http://s1.f53mbcg4ak.ru' + sUrl)
        oGui.addFolder(oGuiElement, params, False, total)
    oGui.setView('episodes')
    oGui.setEndOfDirectory()


def showHosters():
    sUrl = ParameterHandler().getValue('entryUrl')
    sHtmlContent = cRequestHandler(sUrl).request()
    if not 's1.f53mbcg4ak.ru' in sUrl:
        pattern = '<iframe[^>]src="([^"]+)'
        isMatch, aResult = cParser().parse(sHtmlContent, pattern)
        if aResult[0].startswith('//'):
            oRequest = cRequestHandler('http:' + aResult[0])
        else:
            oRequest = cRequestHandler(aResult[0])
        oRequest.addHeaderEntry('Referer', sUrl)
        sHtmlContent = oRequest.request()
        pattern = "url:[^>]'([^']+)"
        isMatch, aResult = cParser().parse(sHtmlContent, pattern)
        if not isMatch:
            pattern = '<iframe[^>]src="([^"]+)'
            isMatch, aResult = cParser().parse(sHtmlContent, pattern)
            oRequest = cRequestHandler('http:' + aResult[0])
            oRequest.addHeaderEntry('Referer', sUrl)
            sHtmlContent = oRequest.request()
    pattern = "url:[^>]'([^']+)"
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)
    hosters = []
    if isMatch:
        for sUrl in aResult:
            q = Qualy(sUrl)
            hoster = {'link': sUrl, 'name': q}
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
