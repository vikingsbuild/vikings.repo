# -*- coding: utf-8 -*-
from resources.lib import logger
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser

SITE_IDENTIFIER = 'kino_cx'
SITE_NAME = 'Kino.cx'
SITE_ICON = 'kino_cx.png'
URL_MAIN = 'https://kino.cx/'
URL_FILME = URL_MAIN + 'filme'
URL_SEARCH = URL_MAIN + '?s=%s'


def load():
    logger.info("Load %s" % SITE_NAME)
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('sUrl', URL_FILME)
    oGui.addFolder(cGuiElement('Filme', SITE_IDENTIFIER, 'showEntries'), params)
    oGui.addFolder(cGuiElement('Genre', SITE_IDENTIFIER, 'showGenres'))
    oGui.addFolder(cGuiElement('Suche', SITE_IDENTIFIER, 'showSearch'))
    oGui.setEndOfDirectory()


def showGenres():
    oGui = cGui()
    params = ParameterHandler()
    sHtmlContent = cRequestHandler(URL_MAIN).request()
    pattern = '<nav[^>]class="genres">.*?</ul>'
    isMatch, sContainer = cParser.parseSingleResult(sHtmlContent, pattern)

    if  isMatch:
        pattern = '<a[^>]*href="([^"]+)".*?>([^"]+)</a>'
        isMatch, aResult = cParser.parse(sContainer, pattern)

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
    if sSearchText is not False:
        pattern = 'search-page.*?<div[^>]class="sidebar[^>]scrolling">'
    else:
        pattern = 'class="item movies">.*?<div[^>]class="sidebar[^>]scrolling">'
    isMatch, sContainer = cParser.parseSingleResult(sHtmlContent, pattern)

    if isMatch:
        if sSearchText is not False:
            pattern = '<img[^>]src="([^"]+).*?<a[^>]href="([^"]+)">([^<]+).*?year">([\d]+)'
        else:
            pattern = '<img[^>]src="([^"]+).*?<h3><a[^>]href="([^"]+)">([^<]+)</a></h3>[^>]<span>([\d]+)'
        isMatch, aResult = cParser.parse(sContainer, pattern)

    if not isMatch:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    cf = cRequestHandler.createUrl(entryUrl, oRequest)
    total = len(aResult)
    for sThumbnail, sUrl, sName, sYear in aResult:
        if sSearchText and not cParser().search(sSearchText, sName):
            continue
        sThumbnail = cParser.replace('-\d+x\d+\.', '.', sThumbnail) + cf
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showHosters')
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        oGuiElement.setYear(sYear)
        oGuiElement.setMediaType('movie')
        params.setParam('entryUrl', sUrl)
        oGui.addFolder(oGuiElement, params, False, total)
    if not sGui:
        isMatchNextPage, sNextUrl = cParser().parseSingleResult(sHtmlContent, "<span[^>]class=[^>]current.*?</span><a[^>]href='([^']+)")
        if isMatchNextPage:
            params.setParam('sUrl', sNextUrl)
            oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)
        oGui.setView('movies')
        oGui.setEndOfDirectory()


def showHosters():
    sUrl = ParameterHandler().getValue('entryUrl')
    sHtmlContent = cRequestHandler(sUrl).request()
    pattern = "data-type='([^']+).*?data-post='([\d]+)[^>]*data-nume='([\d]+)'>.*?server'>([^<]+).*?src=[^>]([^>]+)"
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)
    hosters = []
    if isMatch:
        for type, post, nume, sName, sLang in aResult:
            if '/de' in sLang:
                lang = ' (Deutsch)'
            elif '/en' in sLang:
                lang = ' (Englisch)'
            else:
                lang = ''
            oRequest = cRequestHandler(URL_MAIN + 'wp-admin/admin-ajax.php')
            oRequest.addParameters('action', 'doo_player_ajax')
            oRequest.addParameters('nume', nume)
            oRequest.addParameters('post', post)
            oRequest.addParameters('type', type)
            oRequest.setRequestType(1)
            sHtmlContent = oRequest.request()
            isMatch, aResult = cParser().parse(sHtmlContent, "src=[^>]([^']+)")
            if 'mystream' in aResult[0]:
                isMatch, aResult = cParser().parse(aResult[0], "v/([^/]+)")
                oRequest = cRequestHandler('https://www.mystream.cz/api/source/' + aResult[0])
                oRequest.addParameters('r', 'https://kino.cx/')
                oRequest.addParameters('d', 'www.mystream.cz')
                oRequest.setRequestType(1)
                sHtmlContent = oRequest.request()
                isMatch, aResult = cParser().parse(sHtmlContent, 'file":"([^"]+)","label":"([^"]+)')
                for sUrl, q in aResult:
                    hoster = {'link': sUrl, 'name': sName + ' ' + q + lang}
                    hosters.append(hoster)
            else:
                for sUrl in aResult:
                    hoster = {'link': sUrl, 'name': sName + lang}
                    hosters.append(hoster)
    if hosters:
        hosters.append('getHosterUrl')
    return hosters


def getHosterUrl(sUrl=False):
    if 'fvs.io' in sUrl:
        return [{'streamUrl': sUrl, 'resolved': True}]
    else:
        return [{'streamUrl': sUrl, 'resolved': False}]


def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if not sSearchText: return
    _search(False, sSearchText)
    oGui.setEndOfDirectory()


def _search(oGui, sSearchText):
    showEntries(URL_SEARCH % sSearchText, oGui, sSearchText)
