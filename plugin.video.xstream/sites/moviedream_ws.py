# -*- coding: utf-8 -*-
from resources.lib import logger
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser

SITE_IDENTIFIER = 'moviedream_ws'
SITE_NAME = 'MovieDream'
SITE_ICON = 'moviedream.png'
URL_MAIN = 'https://moviedream.ws/'

EPISODE_URL = URL_MAIN + 'episodeholen.php'
HOSTER_URL = URL_MAIN + 'episodeholen3.php'
URL_SEARCH = URL_MAIN + 'suchergebnisse.php?text=%s&sprache=Deutsch'
QUALITY_ENUM = {'SD': 1, 'HD': 4}


def load():
    logger.info("Load %s" % SITE_NAME)
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('value', 'film')
    oGui.addFolder(cGuiElement('Filme', SITE_IDENTIFIER, 'showMenu'), params)
    params.setParam('value', 'serien')
    oGui.addFolder(cGuiElement('Serien', SITE_IDENTIFIER, 'showMenu'), params)
    oGui.addFolder(cGuiElement('Suche', SITE_IDENTIFIER, 'showSearch'))
    oGui.setEndOfDirectory()


def showMenu():
    oGui = cGui()
    params = ParameterHandler()
    value = params.getValue('value')
    if value == 'film':
        params.setParam('sUrl', URL_MAIN + 'kino')
        oGui.addFolder(cGuiElement('Kino', SITE_IDENTIFIER, 'showEntries'), params)
    sHtmlContent = cRequestHandler(URL_MAIN).request()
    pattern = 'href="(?:\.\.\/)*([neu|beliebt]+%s[^"]*)"[^>]*>([^<]+)<\/a><\/li>' % value
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)

    for sID, sName in aResult:
        params.setParam('sUrl', URL_MAIN + sID)
        oGui.addFolder(cGuiElement(sName, SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MAIN)
    oGui.addFolder(cGuiElement('Genre', SITE_IDENTIFIER, 'showGenre'), params)
    oGui.setEndOfDirectory()


def showGenre():
    oGui = cGui()
    params = ParameterHandler()
    entryUrl = params.getValue('sUrl')
    value = params.getValue('value')
    sHtmlContent = cRequestHandler(entryUrl).request()
    pattern = 'href="(?:\.\.\/)*(%s[^"]+)">([^<]+)<\/a><\/li>' % value
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    for sUrl, sName in aResult:
        params.setParam('sUrl', entryUrl + sUrl)
        oGui.addFolder(cGuiElement(sName, SITE_IDENTIFIER, 'showEntries'), params)
    oGui.setEndOfDirectory()


def showEntries(entryUrl=False, sGui=False, sSearchText=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    if not entryUrl: entryUrl = params.getValue('sUrl')
    sBaseUrl = params.getValue('sBaseUrl')
    if not sBaseUrl:
        params.setParam('sBaseUrl', entryUrl)
        sBaseUrl = entryUrl
    oRequest = cRequestHandler(entryUrl, ignoreErrors=(sGui is not False))
    sHtmlContent = oRequest.request()
    pattern = 'class="linkto.*?href="([^"]+).*?src="([^"]+)">([^<]+)'
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)

    if not isMatch:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    cf = cRequestHandler.createUrl(entryUrl, oRequest)
    total = len(aResult)
    for sUrl, sThumbnail, sName in aResult:
        if sSearchText and not cParser().search(sSearchText, sName):
            continue
        sThumbnail = URL_MAIN + sThumbnail + cf
        isTvshow = True if 'serie' in sUrl else False
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showSeasons' if isTvshow else 'showHosters')
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        oGuiElement.setMediaType("tvshow" if isTvshow else "movie")
        params.setParam('entryUrl', URL_MAIN + sUrl)
        params.setParam('Name', sName)
        params.setParam('sThumbnail', sThumbnail)
        params.setParam('isTvshow', isTvshow)
        oGui.addFolder(oGuiElement, params, isTvshow, total)
    if not sGui:
        pattern = 'pagenumberselected.*?href=".*?href="([^"]+)'
        isMatchNextPage, sNextUrl = cParser.parseSingleResult(sHtmlContent, pattern)
        pattern = 'seiterr"[^>]href="([^"]+)'
        isMatchNextPage, Lastpage = cParser.parseSingleResult(sHtmlContent, pattern)
        if isMatchNextPage:
            if sNextUrl <= Lastpage:
                params.setParam('sUrl', sBaseUrl + sNextUrl)
                oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)
        oGui.setView('tvshows' if 'serie' in entryUrl else 'movies')
        oGui.setEndOfDirectory()


def showSeasons():
    oGui = cGui()
    params = ParameterHandler()
    entryUrl = params.getValue('entryUrl')
    sHtmlContent = cRequestHandler(entryUrl).request()
    pattern = '<div[^>]*season="(\d+)"[^>]*>.*?'
    pattern += 'imdbid\s*:\s*"(\d+)".*?'
    pattern += 'language\s*:\s*"([^"]+)"'
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)
    isDesc, sDesc = cParser.parse(sHtmlContent, '">([^<]+)</p>')

    total = len(aResult)
    for sSeason, imdbid, slanguage in aResult:
        oGuiElement = cGuiElement('Staffel ' + sSeason, SITE_IDENTIFIER, 'showEpisodes')
        oGuiElement.setMediaType('season')
        oGuiElement.setTVShowTitle(params.getValue('Name'))
        oGuiElement.setSeason(sSeason)
        if isDesc:
            oGuiElement.setDescription(sDesc[0])
        oGuiElement.setThumbnail(params.getValue('sThumbnail'))
        params.setParam('Season', sSeason)
        params.setParam('imdbid', imdbid)
        params.setParam('language', slanguage)
        oGui.addFolder(oGuiElement, params, True, total)
    oGui.setView('seasons')
    oGui.setEndOfDirectory()


def showEpisodes():
    oGui = cGui()
    params = ParameterHandler()
    entryUrl = params.getValue('entryUrl')
    sThumbnail = params.getValue('sThumbnail')
    sTVShowTitle = params.getValue('Name')
    oRequest = cRequestHandler(EPISODE_URL)
    oRequest.addHeaderEntry("X-Requested-With", "XMLHttpRequest")
    oRequest.setRequestType(1)
    oRequest.addParameters('imdbid', params.getValue('imdbid'))
    oRequest.addParameters('language', params.getValue('language'))
    oRequest.addParameters('season', params.getValue('Season'))
    sHtmlContent = oRequest.request()
    pattern = '>#([^<]+)</p>[^>]*[^>]*<script>.*?imdbid:[^>]"([^"]+).*?language:[^>]"([^"]+).*?season:[^>]"([^"]+)'
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    sHtmlContent = cRequestHandler(entryUrl).request()
    isDesc, sDesc = cParser.parse(sHtmlContent, '">([^<]+)</p>')

    total = len(aResult)
    for sEpisode, imdbid, slanguage, sSeason in aResult:
        oGuiElement = cGuiElement('Folge ' + sEpisode, SITE_IDENTIFIER, 'showHosters')
        oGuiElement.setMediaType('season')
        oGuiElement.setSeason(sSeason)
        oGuiElement.setEpisode(sEpisode)
        oGuiElement.setMediaType('episode')
        oGuiElement.setTVShowTitle(sTVShowTitle)
        if isDesc:
            oGuiElement.setDescription(sDesc[0])
        oGuiElement.setThumbnail(sThumbnail)
        params.setParam('Episode', sEpisode)
        params.setParam('Season', sSeason)
        params.setParam('imdbid', imdbid)
        params.setParam('language', slanguage)
        oGui.addFolder(oGuiElement, params, False, total)
    oGui.setView('episodes')
    oGui.setEndOfDirectory()


def showHosters():
    params = ParameterHandler()
    if params.getValue('isTvshow') == 'True':
        oRequest = cRequestHandler(HOSTER_URL)
        oRequest.addHeaderEntry("X-Requested-With", "XMLHttpRequest")
        oRequest.setRequestType(1)
        oRequest.addParameters('imdbid', params.getValue('imdbid'))
        oRequest.addParameters('language', params.getValue('language'))
        oRequest.addParameters('season', params.getValue('Season'))
        oRequest.addParameters('episode', params.getValue('Episode'))
        sHtmlContent = oRequest.request()
    else:
        sUrl = params.getValue('entryUrl')
        sHtmlContent = cRequestHandler(sUrl).request()

    if not sHtmlContent:
        return []

    pattern = '<a[^>]*href="([^"]+)"[^>]*><img[^>]*class="([s|h]d+)linkbutton"'
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)

    hosters = []
    if not isMatch:
        return hosters

    for sUrl, sQuali in aResult:
        hoster = {}
        if not 'nurhdfilm' in sUrl.lower():
            hoster['link'] = sUrl
            hoster['name'] = cParser.urlparse(sUrl)
            hoster['displayedName'] = '%s %s' % (hoster['name'], sQuali.upper())
            hoster['quality'] = QUALITY_ENUM[sQuali.upper()]
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
    showEntries(URL_SEARCH % sSearchText, oGui, sSearchText)
