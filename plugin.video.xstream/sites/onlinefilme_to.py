# -*- coding: utf-8 -*-
from resources.lib import logger
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser

SITE_IDENTIFIER = 'onlinefilme_to'
SITE_NAME = 'OnlineFilme'
SITE_ICON = 'onlinefilme.png'
 
URL_MAIN = 'http://onlinefilme.to/'
URL_Filme = URL_MAIN + 'filme-online/'
URL_Serien = URL_MAIN + 'serie-online/'
URL_SEARCH = URL_MAIN + 'suche/%s'


def load():
    logger.info("Load %s" % SITE_NAME)
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('valueType', 'filme')
    params.setParam('sUrl', URL_Filme)
    oGui.addFolder(cGuiElement('Filme', SITE_IDENTIFIER, 'showMenu'), params)
    params.setParam('valueType', 'serie')
    params.setParam('sUrl', URL_Serien)
    oGui.addFolder(cGuiElement('Serien', SITE_IDENTIFIER, 'showMenu'), params)
    oGui.addFolder(cGuiElement('Suche', SITE_IDENTIFIER, 'showSearch'))
    oGui.setEndOfDirectory()


def showMenu():
    oGui = cGui()
    params = ParameterHandler()
    baseURL = params.getValue('sUrl')
    params.setParam('sUrl', baseURL + 'newest')
    oGui.addFolder(cGuiElement('Newest', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', baseURL + 'most-viewed')
    oGui.addFolder(cGuiElement('most viewed', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', baseURL + 'highest-rated')
    oGui.addFolder(cGuiElement('highest rated', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', baseURL + 'most-discussed')
    oGui.addFolder(cGuiElement('most discussed', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MAIN)
    oGui.addFolder(cGuiElement('Genre', SITE_IDENTIFIER, 'showGenres'), params)
    oGui.setEndOfDirectory()


def showGenres():
    oGui = cGui()
    params = ParameterHandler()
    entryUrl = params.getValue('sUrl')
    valueType = params.getValue('valueType')
    sHtmlContent = cRequestHandler(entryUrl).request()
    pattern = '<li>[^<]*<a[^>]*href="([^"]+%s-online[^"]+)"[^>]*><strong>([^<]+)</strong>' % valueType
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    for sUrl, sName in aResult:
        params.setParam('sUrl', sUrl)
        oGui.addFolder(cGuiElement(sName, SITE_IDENTIFIER, 'showEntries'), params)
    oGui.setEndOfDirectory()


def showEntries(entryUrl=False, sGui=False, sSearchText=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    if not entryUrl: entryUrl = params.getValue('sUrl')
    oRequest = cRequestHandler(entryUrl, ignoreErrors=(sGui is not False))
    sHtmlContent = oRequest.request()
    pattern = 'hover-link">.*?</div></div></div></div></a></li></ul>'
    isMatch, sContainer = cParser().parseSingleResult(sHtmlContent, pattern)
    if isMatch:
        pattern = 'href="([^"]+).*?original=".*?([^"]+).*?flagHolderDiv">.*?'
        pattern += "alt='([^']+).*?"
        pattern += 'title"><h2>([^<]+).*?left">([^<]+)'
        isMatch, aResult = cParser().parse(sContainer, pattern)

    if not isMatch:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    cf = cRequestHandler.createUrl(entryUrl, oRequest)
    total = len(aResult)
    for sUrl, sThumbnail, sLang, sName, sYear in aResult:
        if sSearchText and not cParser().search(sSearchText, sName):
            continue
        isTvshow = True if "serie" in sUrl else False
        sThumbnail = URL_MAIN + sThumbnail + cf
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showEpisodes' if isTvshow else 'showHosters')
        oGuiElement.setMediaType('tvshow' if isTvshow else 'movie')
        oGuiElement.setLanguage(sLang)
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        oGuiElement.setYear(sYear)
        oGuiElement.setMediaType('tvshow' if isTvshow else 'movie')
        params.setParam('TVShowTitle', sName)
        params.setParam('entryUrl', sUrl)
        params.setParam('sThumbnail', sThumbnail)
        oGui.addFolder(oGuiElement, params, isTvshow, total)
    if not sGui:
        isMatchNextPage, sNextUrl = cParser().parseSingleResult(sHtmlContent, "class='arrow'><a[^>]*href='([^']+)'>&raquo")
        if isMatchNextPage:
            params.setParam('sUrl', sNextUrl)
            oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)
        oGui.setView('tvshows' if 'serie' in entryUrl else 'movies')
        oGui.setEndOfDirectory()


def showEpisodes():
    oGui = cGui()
    params = ParameterHandler()
    sTVShowTitle = params.getValue('TVShowTitle')
    entryUrl = params.getValue('entryUrl')
    sThumbnail = params.getValue('sThumbnail')
    oRequest = cRequestHandler(entryUrl)
    sHtmlContent = oRequest.request()
    pattern = '<dd[^>]class="accordion-navigation"><a[^>]href=".*?"><strong>([^"]+)</strong>'
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    isDesc, sDesc = cParser.parseSingleResult(sHtmlContent, '<p>([^"]+)<u')
    total = len(aResult)
    for sName in aResult:
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showHosters')
        oGuiElement.setTVShowTitle(sTVShowTitle)
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        if isDesc:
            oGuiElement.setDescription(sDesc)
        oGuiElement.setMediaType('episode')
        params.setParam('sEpisode', sName)
        oGui.addFolder(oGuiElement, params, False, total)
    oGui.setView('episodes')
    oGui.setEndOfDirectory()


def getLinks():
    params = ParameterHandler()
    sUrl = params.getValue('entryUrl')
    sEpisode = params.getValue('sEpisode')
    sHtmlContent = cRequestHandler(sUrl).request()
    if sEpisode:
        pattern = "<strong>%s</strong>.*?</div>.*?<br>" % sEpisode
        isMatch, sContainer = cParser.parseSingleResult(sHtmlContent, pattern)
        pattern = '>([^<]+)</span></form>.*?true"[^>]title="([^"]+)"></div>.*?right"'
        pattern += "><a[^>]href='([^']+)"
        isMatch, aResult = cParser.parse(sContainer, pattern)
    else:
        pattern = '>([^"]+)</span></form>.*?true"[^>]title="([^"]+).*?</span></div>.*?'
        pattern += "<a[^>]href='([^']+)"
        isMatch, aResult = cParser().parse(sHtmlContent, pattern)
    return aResult


def showHosters():
    aResult = getLinks()
    hosters = []
    for sName, sLang, sUrl in aResult:
        oRequest = cRequestHandler(sUrl, caching=False)
        oRequest.request()
        hoster = {'link': oRequest.getRealUrl(), 'name': sName + ' ' + sLang}
        hosters.append(hoster)
    if hosters:
        hosters.append('getHosterUrl')
    return hosters


def getHosterUrl(sUrl=False):
    return [{'streamUrl': sUrl, 'resolved': False}]


def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if not sSearchText: return
    _search(False, sSearchText)
    oGui.setEndOfDirectory()


def _search(oGui, sSearchText):
    import base64
    sSearch = sSearchText
    sSearchText = base64.b64encode('search_term=%s&search_type=0&search_where=0&search_rating_start=1&search_rating_end=10&search_year_from=1900' % sSearchText)
    showEntries(URL_SEARCH % sSearchText, oGui, sSearch)
