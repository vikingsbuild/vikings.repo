# -*- coding: utf-8 -*-
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib import logger
from resources.lib.handler.ParameterHandler import ParameterHandler
import json

SITE_IDENTIFIER = 'mykino_to'
SITE_NAME = 'MyKino'
SITE_ICON = 'mykino.png'

URL_MAIN = 'http://mykino.to/'
URL_Kinofilme = URL_MAIN + 'aktuelle-kinofilme/'
URL_FILME = URL_MAIN + 'filme/'
URL_SERIE = URL_MAIN + 'serien/'
URL_SEARCH = URL_MAIN + 'index.php?do=search&subaction=search&story=%s'
URL_EPISODE = URL_MAIN + 'engine/ajax/a.sseries.php'


def load():
    logger.info("Load %s" % SITE_NAME)
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('sUrl', URL_Kinofilme)
    oGui.addFolder(cGuiElement('Aktuelle Kinofilme', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_FILME)
    oGui.addFolder(cGuiElement('Filme', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_SERIE)
    oGui.addFolder(cGuiElement('Serien', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MAIN)
    params.setParam('sGenreId', 1)
    oGui.addFolder(cGuiElement('Genre Filme', SITE_IDENTIFIER, 'showGenre'), params)
    params.setParam('sUrl', URL_MAIN)
    params.setParam('sGenreId', 2)
    oGui.addFolder(cGuiElement('Genre Serien', SITE_IDENTIFIER, 'showGenre'), params)
    oGui.addFolder(cGuiElement('A-Z', SITE_IDENTIFIER, 'showAlphaNumeric'))
    oGui.addFolder(cGuiElement('Suche', SITE_IDENTIFIER, 'showSearch'))
    oGui.setEndOfDirectory()


def showAlphaNumeric():
    sHtmlContent = cRequestHandler(URL_MAIN).request()
    pattern = '<div[^>]*class="catalog-nav"[^>]*>(.*?)</div>'
    isMatch, sContainer = cParser().parseSingleResult(sHtmlContent, pattern)

    if not isMatch:
        return

    pattern = '<a[^>]*href="([^"]+)"[^>]*>(\w)</a>'
    isMatch, aResult = cParser().parse(sContainer, pattern)

    if not isMatch:
        return

    oGui = cGui()
    params = ParameterHandler()
    for sUrl, sName in aResult:
        params.setParam('sUrl', URL_MAIN + sUrl)
        oGui.addFolder(cGuiElement(sName, SITE_IDENTIFIER, 'showEntries'), params)
    oGui.setEndOfDirectory()


def showGenre():
    oParams = ParameterHandler()
    sUrl = oParams.getValue('sUrl')
    sHtmlContent = cRequestHandler(sUrl).request()
    pattern = '<div[^>]*id="tabln%s"[^>]*>(.*?)</ul>' % oParams.getValue('sGenreId')
    isMatch, sContainer = cParser().parseSingleResult(sHtmlContent, pattern)

    if not isMatch:
        return

    pattern = '<a[^>]*href="([^"]+)"[^>]*>([^<]*)</a>'
    isMatch, aResult = cParser().parse(sContainer, pattern)

    if not isMatch:
        return

    oGui = cGui()
    for sUrl, sName in aResult:
        oParams.setParam('sUrl', URL_MAIN + sUrl)
        oGui.addFolder(cGuiElement(sName, SITE_IDENTIFIER, 'showEntries'), oParams)
    oGui.setEndOfDirectory()


def showEntries(entryUrl=False, sGui=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    if not entryUrl: entryUrl = params.getValue('sUrl')
    sHtmlContent = cRequestHandler(entryUrl, ignoreErrors=(sGui is not False)).request()

    pattern = '<a[^<]*href="(?:[^"]+)?(/(\d+)-[^"]+)"[^<]*>\s*'  # url / news-id
    pattern += '<img[^>]*src="([^"]*)"[^>]*>.*?'  # thumbnail
    pattern += '<div[^>]*class="boxgridtext"[^>]*>([^<]+)</div>\s*'  # name
    pattern += '(?:<br>)*\s*Jahr:\s*([^<]+)\s*'  # year
    pattern += '(?:<br>\s*Genre:([^<]+))?'  # genre (optional for search)
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)

    if not isMatch:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    containsTvShows = False

    total = len(aResult)
    for sUrl, news_id, sThumbnail, sName, sYear, sGenre in aResult:
        isTvshow = True if "Serie" in sGenre else False
        if not sGenre:
            sHtmlContent = cRequestHandler(URL_MAIN + sUrl, ignoreErrors=(sGui is not False)).request()
            isTvshow, aDummyResult = cParser.parse(sHtmlContent, '<select[^>]*id="sseriesSeason"[^>]*>')
        if isTvshow:
            containsTvShows = True
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showHosters')
        oGuiElement.setMediaType('tvshow' if isTvshow else 'movie')
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setYear(sYear)
        params.setParam('entryUrl', URL_MAIN + sUrl)
        params.setParam('isTvshow', isTvshow)
        params.setParam('sThumbnail', sThumbnail)
        params.setParam('sName', sName)
        params.setParam('news_id', news_id)
        oGui.addFolder(oGuiElement, params, isTvshow, total)

    if not sGui:
        isMatchNextPage, sNextUrl = cParser.parseSingleResult(sHtmlContent, '<a[^>]*href="([^"]+)"[^>]*>Weiter</a>')
        if isMatchNextPage:
            params.setParam('sUrl', sNextUrl)
            oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)

        oGui.setView('tvshows' if containsTvShows else 'movies')
        oGui.setEndOfDirectory()


def showHosters():
    params = ParameterHandler()
    isTvshowEntry = params.getValue('isTvshow')

    if isTvshowEntry == 'True':
        entryUrl = params.getValue('entryUrl')
        sHtmlContent = cRequestHandler(entryUrl).request()
        pattern = '<select[^>]*id="sseriesSeason">.*?</select>'
        isMatch, sContainer = cParser().parseSingleResult(sHtmlContent, pattern)
        if not isMatch:
            return
        pattern = '<option[^>]*value="([^"]+)"[^>]*>([^<]+)'
        isMatch, aResult = cParser().parse(sContainer, pattern)
        if isMatch:
            showSeason(aResult, params)
    else:
        return getHosters()


def showSeason(aResult, params):
    oGui = cGui()
    sThumbnail = params.getValue('sThumbnail')
    sTVShowTitle = params.getValue('sName')

    total = len(aResult)
    for sId, sSeason in aResult:
        oGuiElement = cGuiElement("Staffel " + str(sId), SITE_IDENTIFIER, 'showEpisodes')
        oGuiElement.setMediaType('season')
        oGuiElement.setTVShowTitle(sTVShowTitle)
        oGuiElement.setSeason(sId)
        oGuiElement.setThumbnail(sThumbnail)
        params.setParam('sSeason', sId)
        oGui.addFolder(oGuiElement, params, True, total)

    oGui.setView('seasons')
    oGui.setEndOfDirectory()


def showEpisodes():
    oGui = cGui()
    params = ParameterHandler()
    sThumbnail = params.getValue('sThumbnail')
    sSeason = params.getValue('sSeason')
    news_id = params.getValue('news_id')
    sTVShowTitle = params.getValue('sName')

    oRequest = cRequestHandler(URL_EPISODE)
    oRequest.addParameters('news_id', news_id)
    oRequest.addParameters('season', sSeason)
    oRequest.setRequestType(1)
    sHtmlContent = oRequest.request()

    if not sHtmlContent:
        return

    data = json.loads(sHtmlContent)
    if "options" in data:
        sHtmlContent = data["options"]

    pattern = '<option[^>]*value="(\d+)"[^>]*>([^<]+(\d+))\s*</option>'
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)

    if not isMatch:
        return

    total = len(aResult)
    for seriesId, sName, Episodenr in aResult:
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'getHosters')
        oGuiElement.setTVShowTitle(sTVShowTitle)
        oGuiElement.setSeason(sSeason)
        oGuiElement.setEpisode(Episodenr)
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setMediaType('episode')
        params.setParam('seriesId', seriesId)
        oGui.addFolder(oGuiElement, params, False, total)

    oGui.setView('episodes')
    oGui.setEndOfDirectory()


def getHosters():
    params = ParameterHandler()
    seriesId = params.getValue('seriesId')
    news_id = params.getValue('news_id')
    sHtmlContent = ''

    hosters = []
    if seriesId and news_id:
        oRequest = cRequestHandler(URL_EPISODE)
        oRequest.addParameters('news_id', news_id)
        oRequest.addParameters('series', seriesId)
        oRequest.setRequestType(1)
        sJson = oRequest.request()

        if not sJson:
            return

        data = json.loads(sJson)
        if "links" in data:
            sHtmlContent = data["links"]
    else:
        sUrl = ParameterHandler().getValue('entryUrl')
        sHtmlContent = cRequestHandler(sUrl).request()

    isMatch, aResult = cParser.parse(sHtmlContent, '<a[^>]*data-href="([^"]+)"[^>]*>.*?<span>([^<]*)<\/span>')
    if not isMatch:
        return hosters

    for sUrls, sName in aResult:
        for idx, sLink in enumerate(sUrls.split(',')):
            hoster = {'name': sName, 'link': sLink, 'displayedName': '%s - Mirror %s' % (sName, idx + 1)}
            hosters.append(hoster)

    if hosters:
        hosters.append('getHosterUrl')
    return hosters


def getHosterUrl(sUrl=False):
    if not sUrl: sUrl = ParameterHandler().getValue('url')
    return [{'streamUrl': sUrl, 'resolved': False}]


def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if not sSearchText: return
    _search(False, sSearchText)
    oGui.setEndOfDirectory()


def _search(oGui, sSearchText):
    if not sSearchText: return
    showEntries(URL_SEARCH % sSearchText.strip(), oGui)
