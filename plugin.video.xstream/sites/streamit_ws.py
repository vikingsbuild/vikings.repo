# -*- coding: utf-8 -*-
from resources.lib import logger
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser

SITE_IDENTIFIER = 'streamit_ws'
SITE_NAME = 'StreamIt'
SITE_ICON = 'streamit.png'

URL_MAIN = 'https://streamit.ws/'
URL_SERIELINKS = URL_MAIN + 'lade_episode.php'
URL_KINO = URL_MAIN + 'de/kino'
URL_FILME = URL_MAIN + 'de/film'
URL_SERIES = URL_MAIN + 'de/serie'
URL_GENRES_FILM = URL_MAIN + 'de/genre-filme'
URL_GENRES_SERIE = URL_MAIN + 'de/genre-serien'
URL_SEARCH = URL_MAIN + 'suche.php?s=%s'


def load():
    logger.info("Load %s" % SITE_NAME)
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('sUrl', URL_KINO)
    oGui.addFolder(cGuiElement('Kino Filme', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_FILME)
    oGui.addFolder(cGuiElement('Filme', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_SERIES)
    oGui.addFolder(cGuiElement('Serien', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_GENRES_FILM)
    oGui.addFolder(cGuiElement('Film Genre', SITE_IDENTIFIER, 'showGenre'), params)
    params.setParam('sUrl', URL_GENRES_SERIE)
    oGui.addFolder(cGuiElement('Serien Genre', SITE_IDENTIFIER, 'showGenre'), params)
    oGui.addFolder(cGuiElement('Suche', SITE_IDENTIFIER, 'showSearch'))
    oGui.setEndOfDirectory()


def showGenre():
    oGui = cGui()
    params = ParameterHandler()
    entryUrl = params.getValue('sUrl')
    sHtmlContent = cRequestHandler(entryUrl).request()
    isMatch, sContainer = cParser.parseSingleResult(sHtmlContent, 'id="categories.*?class="clear">')

    if isMatch:
        pattern = '<a[^>]href="([^"]+)"[^>]*>([^<]+)</a>([^<]+)'
        isMatch, aResult = cParser.parse(sContainer, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    for sUrl, sTitle, Nr in aResult:
        params.setParam('sUrl', URL_MAIN + sUrl)
        oGui.addFolder(cGuiElement(sTitle + Nr, SITE_IDENTIFIER, 'showEntries'), params)
    oGui.setEndOfDirectory()


def showEntries(entryUrl=False, sGui=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    entryUrl = params.getValue('sUrl')

    iPage = int(params.getValue('page'))
    if iPage > 0:
        entryUrl = entryUrl + ('&' if '?' in entryUrl else '?') + 'page=' + str(iPage)

    oRequestHandler = cRequestHandler(entryUrl, ignoreErrors=(sGui is not False))
    sHtmlContent = oRequestHandler.request()
    pattern = '<div[^>]class="post-thumb">.*?<a[^>]*href="([^"]+)"[^>]title="([^"]+)">.*?src="([^"]+)"'
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)

    if not isMatch:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    total = len(aResult)
    for sUrl, sName, sThumbnail in aResult:
        isTvshow = True if "serie" in sUrl else False
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showSeasons' if isTvshow else 'showHosters')
        if sThumbnail.startswith('//'):
            sThumbnail = 'https:' + sThumbnail
        if sThumbnail.startswith('/'):
            sThumbnail = URL_MAIN + sThumbnail
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        oGuiElement.setMediaType('tvshow' if isTvshow else 'movie')
        if sUrl.startswith('http'):
            params.setParam('entryUrl', sUrl)
        if not sUrl.startswith('http'):
            params.setParam('entryUrl', URL_MAIN + sUrl)
        params.setParam('sName', sName)
        params.setParam('Thumbnail', sThumbnail)
        oGui.addFolder(oGuiElement, params, isTvshow, total)
    if not sGui:
        isMatch, strPage = cParser().parseSingleResult(sHtmlContent, '<a[^>]*class="next page-numbers"[^>]*href="[^>]*page=([^"]+)">Next &raquo;')
        if isMatch:
            params.setParam('page', int(strPage))
            oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)
        oGui.setView('tvshows' if 'serie' in entryUrl else 'movies')
        oGui.setEndOfDirectory()


def showSeasons():
    oGui = cGui()
    params = ParameterHandler()
    sUrl = params.getValue('entryUrl')
    sThumbnail = params.getValue("Thumbnail")
    sName = params.getValue('sName')
    sHtmlContent = cRequestHandler(sUrl).request()
    pattern = '<select[^>]*class="staffelauswahl"[^>]*>(.*?)</select>'  # container
    isMatch, strContainer = cParser().parseSingleResult(sHtmlContent, pattern)

    if isMatch:
        pattern = 'value=([\d]+)'
        isMatch, aResult = cParser().parse(strContainer, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    total = len(aResult)
    for sSeason in aResult:
        oGuiElement = cGuiElement("Staffel " + sSeason, SITE_IDENTIFIER, 'showEpisodes')
        oGuiElement.setTVShowTitle(sName)
        oGuiElement.setSeason(sSeason)
        oGuiElement.setMediaType('season')
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        params.setParam('season', sSeason)
        oGui.addFolder(oGuiElement, params, True, total)
    oGui.setView('seasons')
    oGui.setEndOfDirectory()


def showEpisodes():
    oGui = cGui()
    params = ParameterHandler()
    sUrl = params.getValue('entryUrl')
    sThumbnail = params.getValue("Thumbnail")
    sSeason = params.getValue('season')
    sHtmlContent = cRequestHandler(sUrl).request()
    pattern = "href='#s%se([\d]+)" % sSeason
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    result, imdb = cParser().parseSingleResult(sHtmlContent, 'IMDB\s?=\s?\'(\d+)')

    total = len(aResult)
    for sEpisodeNr in aResult:
        oGuiElement = cGuiElement('Folge ' + sEpisodeNr, SITE_IDENTIFIER, "showHosters")
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        oGuiElement.setEpisode(sEpisodeNr)
        oGuiElement.setSeason(sSeason)
        oGuiElement.setMediaType('episode')
        params.setParam('val', 's' + sSeason + 'e' + sEpisodeNr)
        params.setParam('IMDB', imdb)
        oGui.addFolder(oGuiElement, params, False, total)
    oGui.setView('episodes')
    oGui.setEndOfDirectory()


def showHosters():
    params = ParameterHandler()
    sUrl = params.getValue('entryUrl')
    oRequestHandler = cRequestHandler(sUrl)

    if params.getValue('val'):
        oRequestHandler = cRequestHandler(URL_SERIELINKS)
        oRequestHandler.addParameters('val', params.getValue('val'))
        oRequestHandler.addParameters('IMDB', params.getValue('IMDB'))
        oRequestHandler.setRequestType(1)

    sHtmlContent = oRequestHandler.request()
    hosters = []
    isMatch, sContainer = cParser().parseSingleResult(sHtmlContent, '<select[^>]*class="sel_quali"[^>]*>(.*?)</select>')

    if not isMatch:
        return hosters

    isMatch, aResult = cParser().parse(sContainer, '<option[^>]*\((?:[^>]*quality/(\d+)\.png)?[^>]*id="(\w+)"[^>]*>(.*?)</option>')

    if not isMatch:
        return hosters

    for sQulityNr, sID, sQulityTitle in aResult:
        pattern = '<div[^>]*class="mirrors\w+"[^>]*id="%s">(.*?)</div></div>' % sID
        isMatchMirrors, sMirrorContainer = cParser().parse(sHtmlContent, pattern)

        if not isMatchMirrors:
            continue

        isMatchUrls, aResultMirrors = cParser().parse(sMirrorContainer[0], '<a[^>]*href="([^"]+)"[^>]*>.*?name="save"[^>]*value="(.*?)"[^>]*/>')

        if not isMatchUrls:
            continue

        for sUrl, sName in aResultMirrors:
            hoster = {'name': sName.strip(), 'displayedName': '[%s] %s' % (sQulityTitle, sName.strip()),
                      'quality': sQulityNr if sQulityNr else '0', 'link': URL_MAIN + sUrl}
            hosters.append(hoster)

    if hosters:
        hosters.append('getHosterUrl')
    return hosters


def getHosterUrl(sUrl=False):
    sHtmlContent = cRequestHandler(sUrl).request()
    isMatch, redirectUrl = cParser().parseSingleResult(sHtmlContent, 'none"><a[^>]*href="([^"]+)')
    return [{'streamUrl': redirectUrl, 'resolved': False}]


def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if not sSearchText: return
    _search(False, sSearchText)
    oGui.setEndOfDirectory()


def _search(oGui, sSearchText):
    showEntries(URL_SEARCH % sSearchText, oGui)
