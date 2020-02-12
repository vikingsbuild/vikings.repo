# -*- coding: utf-8 -*-
from resources.lib import logger
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser

SITE_IDENTIFIER = 'tmovie_to'
SITE_NAME = 'TMovie'
SITE_ICON = 'tmovie.to.png'

URL_MAIN = 'https://tmovie.to'
URL_FILME = URL_MAIN + '/filme'
URL_SERIE = URL_MAIN + '/serien'
URL_SEARCH = URL_MAIN + '/search?keyword=%s'
URL_HOSTER = URL_MAIN + '/embed/getembed/'


def load():
    logger.info("Load %s" % SITE_NAME)
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('sUrl', URL_FILME)
    oGui.addFolder(cGuiElement('Filme', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_SERIE)
    oGui.addFolder(cGuiElement('Serien', SITE_IDENTIFIER, 'showEntries'), params)
    oGui.addFolder(cGuiElement('Genre', SITE_IDENTIFIER, 'showGenre'))
    oGui.addFolder(cGuiElement('Suche', SITE_IDENTIFIER, 'showSearch'))
    oGui.setEndOfDirectory()


def showGenre():
    oGui = cGui()
    params = ParameterHandler()
    sHtmlContent = cRequestHandler(URL_MAIN).request()
    pattern = '<a[^>]href="(/genre[^"]+)"><div>([^<]+)</div>'
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
    sHtmlContent = oRequest.request()
    pattern = 'class="rig-cell"[^>]href="([^"]+).*?src="([^"]+).*?<span[^>]class="name">([^<]+)'
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)

    if not isMatch:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    cf = cRequestHandler.createUrl(entryUrl, oRequest)
    total = len(aResult)
    for sUrl, sThumbnail, sName in aResult:
        if sSearchText and not cParser().search(sSearchText, sName):
            continue
        isTvshow = True if 'staffel' in sUrl.lower() else False
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showEpisodes' if isTvshow else 'showHosters')
        sThumbnail = URL_MAIN + sThumbnail + cf
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        oGuiElement.setMediaType('tvshow' if isTvshow else 'movie')
        params.setParam('TVShowTitle', sName)
        params.setParam('entryUrl', URL_MAIN + sUrl)
        params.setParam('sThumbnail', sThumbnail)
        params.setParam('isTvshow', 'false')
        oGui.addFolder(oGuiElement, params, isTvshow, total)
    if not sGui:
        isMatchNextPage, sNextUrl = cParser().parseSingleResult(sHtmlContent, '<a[^>]href="([^"]+)">N')
        if isMatchNextPage:
            params.setParam('sUrl', URL_MAIN + sNextUrl)
            oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)
        oGui.setView('tvshows' if 'staffel' in sUrl.lower() else 'movies')
        oGui.setEndOfDirectory()


def showEpisodes():
    oGui = cGui()
    params = ParameterHandler()
    sTVShowTitle = params.getValue('TVShowTitle')
    entryUrl = params.getValue('entryUrl')
    sThumbnail = params.getValue('sThumbnail')
    sHtmlContent = cRequestHandler(entryUrl).request()
    pattern = 'class="list-group">.*?<div[^>]style="clear'
    isMatch, sContainer = cParser.parseSingleResult(sHtmlContent, pattern)

    if isMatch:
        pattern = '">([\d]+)'
        isMatch, aResult = cParser.parse(sContainer, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    total = len(aResult)
    for sEpisodeNr in aResult:
        oGuiElement = cGuiElement('Folge ' + sEpisodeNr, SITE_IDENTIFIER, 'showHosters')
        oGuiElement.setTVShowTitle(sTVShowTitle)
        oGuiElement.setEpisode(sEpisodeNr)
        oGuiElement.setMediaType('episode')
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        params.setParam('sEpisodeNr', sEpisodeNr)
        params.setParam('isTvshow', 'true')
        oGui.addFolder(oGuiElement, params, False, total)
    oGui.setView('episodes')
    oGui.setEndOfDirectory()


def showHosters():
    isTvshow = ParameterHandler().getValue('isTvshow')
    sUrl = ParameterHandler().getValue('entryUrl')
    hosters = []
    if 'true' in isTvshow:
        sEpisodeNr = ParameterHandler().getValue('sEpisodeNr')
        sHtmlContent = cRequestHandler(sUrl).request()
        pattern = 'value="([^"]+)"[^>]data-seq="[^"]+"[^>]class="btn[^"]+">%s</button>' % sEpisodeNr.strip()
        isMatch, aResult = cParser.parse(sHtmlContent, pattern)
    else:
        sHtmlContent = cRequestHandler(sUrl).request()
        pattern = 'type="button"[^>]value="([^"]+)'
        isMatch, aResult = cParser.parse(sHtmlContent, pattern)
    if isMatch:
        for sType in aResult:
            oRequest = cRequestHandler(URL_HOSTER)
            oRequest.addParameters('ec', sType)
            oRequest.setRequestType(1)
            sHtmlContent = oRequest.request()
            pattern = '"([^"]+)"'
            isMatch, sUrl = cParser().parseSingleResult(sHtmlContent, pattern)
            sName = cParser.urlparse(sUrl)
            hoster = {'link': sUrl, 'name': sName}
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
