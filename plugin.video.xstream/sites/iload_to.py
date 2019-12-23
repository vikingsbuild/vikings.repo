# -*- coding: utf-8 -*-
from resources.lib import logger
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser

SITE_IDENTIFIER = 'iload_to'
SITE_NAME = 'iLoad'
SITE_ICON = 'iload.png'

URL_MAIN = 'https://iload.to'
URL_FILME = URL_MAIN + '/category/3/filme/'
URL_SHOWS = URL_MAIN + '/category/7/serien/'
URL_SEARCH_MOVIE = URL_MAIN + '/suche/%s/Filme'
URL_SEARCH_TV = URL_MAIN + '/suche/%s/Serien'
ORDER_DESC = '/order/%s-0'
ORDER_ASC = '/order/%s-1'


def load():
    logger.info("Load %s" % SITE_NAME)
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('sUrl', URL_FILME)
    oGui.addFolder(cGuiElement('Filme', SITE_IDENTIFIER, 'showContentMenu'), params)
    params.setParam('sUrl', URL_SHOWS)
    oGui.addFolder(cGuiElement('Serien', SITE_IDENTIFIER, 'showContentMenu'), params)
    oGui.addFolder(cGuiElement('Suche', SITE_IDENTIFIER, 'showSearch'))
    oGui.setEndOfDirectory()


def showContentMenu():
    oGui = cGui()
    params = ParameterHandler()
    entryUrl = params.getValue('sUrl')
    params.setParam('sUrl', entryUrl + (ORDER_DESC % 0))
    oGui.addFolder(cGuiElement('Neuste', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', entryUrl + (ORDER_DESC % 1))
    oGui.addFolder(cGuiElement('A-Z', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', entryUrl + (ORDER_DESC % 2))
    oGui.addFolder(cGuiElement('Aufrufe', SITE_IDENTIFIER, 'showEntries'), params)
    if 'filme' in entryUrl:
        params.setParam('sUrl', entryUrl + (ORDER_DESC % 3))
        oGui.addFolder(cGuiElement('IMDB-Wertung', SITE_IDENTIFIER, 'showEntries'), params)
        params.setParam('sUrl', entryUrl)
        oGui.addFolder(cGuiElement('Genre', SITE_IDENTIFIER, 'showGenre'), params)
    oGui.setEndOfDirectory()


def showGenre():
    oGui = cGui()
    params = ParameterHandler()
    entryUrl = params.getValue('sUrl')
    sHtmlContent = cRequestHandler(entryUrl).request()
    pattern = '<a[^>]*href="([^"]+)"[^>]*class="next level3"[^>]*>.*?<div>([^<]+)</div>\s*</a>'
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    for sUrl, sName in aResult:
        params.setParam('sUrl', URL_MAIN + sUrl)
        oGui.addFolder(cGuiElement(sName, SITE_IDENTIFIER, 'showEntries'), params)
    oGui.setEndOfDirectory()


def showEntries(entryUrl=False, sGui=False, isInternalSearch=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    if not entryUrl: entryUrl = params.getValue('sUrl')
    oRequest = cRequestHandler(entryUrl, ignoreErrors=not isInternalSearch)
    sHtmlContent = oRequest.request()
    cf = createUrl(entryUrl, oRequest)
    sPattern = '<table[^>]*class="row".*?'  # container start
    sPattern += '<img[^>]*src="([^"]+).*?'  # thumbnail
    sPattern += '<a[^>]*href="([^"]*)"[^>]*>([^<]*).*?'  # url
    sPattern += '(?:<span[^>]*class="list-year"[^>]*>\s*(?:\((\d+)\))</span>.*?)?'  # year
    sPattern += '<td[^>]*class="description"[^>]*>(.*?)<'  # desc
    isMatch, aResult = cParser.parse(sHtmlContent, sPattern)

    if not isMatch:
        if isInternalSearch: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    isTvshow = True if "serien" in entryUrl.lower() else False
    total = len(aResult)
    for sThumbnail, sUrl, sName, sYear, sDesc in aResult:
        if sThumbnail.startswith('//'):
            sThumbnail = 'http:' + sThumbnail
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showSeasons' if isTvshow else 'showHosters')
        oGuiElement.setThumbnail(sThumbnail + cf)
        oGuiElement.setDescription(sDesc)
        if sYear:
            oGuiElement.setYear(sYear)
        oGuiElement.setMediaType('tvshow' if isTvshow else 'movie')
        params.setParam('entryUrl', URL_MAIN + sUrl)
        params.setParam('isTvshow', isTvshow)
        params.setParam('sThumbnail', sThumbnail)
        params.setParam('sDesc', sDesc)
        params.setParam('sName', sName)
        oGui.addFolder(oGuiElement, params, isTvshow, total)

    if not isInternalSearch:
        sPattern = '<span[^>]*class="selected">\d+</span>\s*<a[^>]*href="([^"]+)">\d+</a>'
        isMatchNextPage, aResult = cParser.parse(sHtmlContent, sPattern)
        if isMatchNextPage:
            params.setParam('sUrl', URL_MAIN + aResult[0])
            oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)

    if not sGui:
        oGui.setView('tvshows' if 'serien' in entryUrl else 'movies')
        oGui.setEndOfDirectory()


def showSeasons():
    oGui = cGui()
    params = ParameterHandler()
    sThumbnail = params.getValue('sThumbnail')
    sTVShowTitle = params.getValue('sName')
    sDesc = params.getValue('sDesc')
    entryUrl = params.getValue('entryUrl')
    sHtmlContent = cRequestHandler(entryUrl).request()
    pattern = '<td[^>]*data-title-name="[^"]*(\s+\d+)"[^>]*>\s*'  # name / nr
    pattern += '<a[^>]*href="([^"]*)"[^>]*>'  # url
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    total = len(aResult)
    for sSeasonNr, sUrl in aResult:
        sSeasonNr = str(int(sSeasonNr))
        oGuiElement = cGuiElement("Staffel " + sSeasonNr, SITE_IDENTIFIER, 'showEpisodes')
        oGuiElement.setMediaType('season')
        oGuiElement.setTVShowTitle(sTVShowTitle)
        oGuiElement.setSeason(sSeasonNr)
        oGuiElement.setDescription(sDesc)
        oGuiElement.setThumbnail(sThumbnail)
        params.setParam('sSeasonNr', sSeasonNr)
        params.setParam('sUrl', URL_MAIN + sUrl)
        oGui.addFolder(oGuiElement, params, True, total)
    oGui.setView('seasons')
    oGui.setEndOfDirectory()


def showEpisodes():
    oGui = cGui()
    params = ParameterHandler()
    sThumbnail = params.getValue('sThumbnail')
    sSeasonNr = params.getValue('sSeasonNr')
    sTVShowTitle = params.getValue('TVShowTitle')
    sDesc = params.getValue('sDesc')
    entryUrl = params.getValue('sUrl')
    sHtmlContent = cRequestHandler(entryUrl).request()
    pattern = '<td[^>]*data-title-name="[^"]*(\s+\d+)"[^>]*>\s*'  # name / nr
    pattern += '<a[^>]*href="([^"]*)"[^>]*>'  # url
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    total = len(aResult)
    for sEpisodeNr, sUrl in aResult:
        sEpisodeNr = str(int(sEpisodeNr))
        oGuiElement = cGuiElement("Folge " + sEpisodeNr, SITE_IDENTIFIER, 'showHosters')
        oGuiElement.setTVShowTitle(sTVShowTitle)
        oGuiElement.setSeason(sSeasonNr)
        oGuiElement.setEpisode(sEpisodeNr)
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setDescription(sDesc)
        oGuiElement.setMediaType('episode')
        params.setParam('entryUrl', URL_MAIN + sUrl)
        oGui.addFolder(oGuiElement, params, False, total)
    oGui.setView('episodes')
    oGui.setEndOfDirectory()


def showHosters():
    params = ParameterHandler()
    sUrl = params.getValue('entryUrl')
    hosters = []
    sHtmlContent = cRequestHandler(sUrl).request()
    sPattern = '<a[^>]*href="([^"]+\/TitleReleaseList[^"]*)"[^>]*>([^<]+)</a>'  # url
    isMatch, aResult = cParser.parse(sHtmlContent, sPattern)

    if isMatch:
        for sReleaseUrl, sName in aResult:
            sHtmlContent = cRequestHandler(URL_MAIN + sReleaseUrl).request()
            hosters.extend(getHostFromUrl(sHtmlContent, sName))
    else:
        hosters.extend(getHostFromUrl(sHtmlContent))
    if hosters:
        hosters.append('getHosterUrl')
    return hosters


def getHostFromUrl(sHtmlContent, sReleaseName=False):
    hosters = []
    sPattern = '<a[^>]*href="([^"]+)"[^>]*class="[^"]*ddl-mirror-box-stream-direct[^"]*"[^>]*>\s*'  # url
    sPattern += '<img[^>]*src="[^"]*host\/([^".]+)'  # name
    isMatch, aResult = cParser.parse(sHtmlContent, sPattern)

    if not isMatch:
        return []

    for sUrl, sName in aResult:
        hoster = {'link': URL_MAIN + sUrl, 'name': sName.title()}
        if sReleaseName:
            hoster['displayedName'] = '%s  [%s]' % (sName.title(), sReleaseName)
        hosters.append(hoster)
    return hosters


def getHosterUrl(sUrl=False):
    if not sUrl: sUrl = ParameterHandler().getValue('entryUrl')
    oRequest = cRequestHandler(sUrl, caching=False)
    oRequest.request()
    return [{'streamUrl': oRequest.getRealUrl(), 'resolved': False}]


def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if not sSearchText: return
    _search(False, sSearchText)
    oGui.setEndOfDirectory()


def _search(oGui, sSearchText):
    if not sSearchText: return
    isInternalSearch = (oGui == False)

    if isInternalSearch:
        oGui = cGui()

    showEntries(URL_SEARCH_MOVIE % sSearchText.strip(), oGui, isInternalSearch)
    showEntries(URL_SEARCH_TV % sSearchText.strip(), oGui, isInternalSearch)

    if isInternalSearch:
        oGui.setView('movies')
        oGui.setEndOfDirectory()


def createUrl(sUrl, oRequest):
    import urlparse
    parsed_url = urlparse.urlparse(sUrl)
    netloc = parsed_url.netloc[4:] if parsed_url.netloc.startswith('www.') else parsed_url.netloc
    cfId = oRequest.getCookie('__cfduid', '.' + netloc)
    cfClear = oRequest.getCookie('cf_clearance', '.' + netloc)
    if cfId and cfClear and 'Cookie=Cookie:' not in sUrl:
        delimiter = '&' if '|' in sUrl else '|'
        sUrl = delimiter + "Cookie=Cookie: __cfduid=" + cfId.value + "; cf_clearance=" + cfClear.value
    if 'User-Agent=' not in sUrl:
        delimiter = '&' if '|' in sUrl else '|'
        sUrl += delimiter + "User-Agent=" + oRequest.getHeaderEntry('User-Agent')
    return sUrl
