# -*- coding: utf-8 -*-
from resources.lib import logger
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser

SITE_IDENTIFIER = 'hdkino_to'
SITE_NAME = 'HDKino.to'
SITE_ICON = 'hdkino_to.png'

URL_MAIN = 'https://hdkino.to'
URL_FILME = URL_MAIN + '/filme?page=%s'
URL_TOP_FILME = URL_MAIN + '/top?page=%s'


def load():
    logger.info("Load %s" % SITE_NAME)
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('page', 1)
    params.setParam('sUrl', URL_FILME)
    oGui.addFolder(cGuiElement('Filme', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_TOP_FILME)
    oGui.addFolder(cGuiElement('Top Filme', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('Value', 'Genre')
    oGui.addFolder(cGuiElement('Genres', SITE_IDENTIFIER, 'showValue'), params)
    params.setParam('Value', 'Jahr')
    oGui.addFolder(cGuiElement('Jahr', SITE_IDENTIFIER, 'showValue'), params)
    oGui.setEndOfDirectory()


def showValue():
    oGui = cGui()
    params = ParameterHandler()
    sHtmlContent = cRequestHandler(URL_MAIN).request()
    pattern = '>%s</div>.*?</div>' % params.getValue('Value')
    isMatch, sHtmlContainer = cParser.parseSingleResult(sHtmlContent, pattern)

    if isMatch:
        pattern = '<a[^>]*href="([^"]+)".*?>([^"]+)</a>'
        isMatch, aResult = cParser.parse(sHtmlContainer, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    for sUrl, sName in aResult:
        if sUrl.startswith('//'):
            sUrl = 'https:' + sUrl
        params.setParam('sUrl', sUrl + '?page=%s')
        oGui.addFolder(cGuiElement(sName.strip(), SITE_IDENTIFIER, 'showEntries'), params)
    oGui.setEndOfDirectory()


def showEntries(entryUrl=False, sGui=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    if not entryUrl: entryUrl = params.getValue('sUrl')
    page = params.getValue('page')
    oRequest = cRequestHandler(entryUrl % page)
    sHtmlContent = oRequest.request()
    pattern = 'search_frame".*?<a[^>]href="([^"]+)"><img[^>]src="([^"]+).*?<strong>([^<]+).*?year/([\d]+)'
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)

    if not isMatch:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    cf = cRequestHandler.createUrl(entryUrl, oRequest)
    total = len(aResult)
    for sUrl, sThumbnail, sName, sYear in aResult:
        sThumbnail = cParser().replace('\d+x\d+', '', sThumbnail + cf)
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showHosters')
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        oGuiElement.setYear(sYear)
        oGuiElement.setMediaType('movie')
        params.setParam('entryUrl', sUrl)
        oGui.addFolder(oGuiElement, params, False, total)
    if not sGui:
        isMatchNextPage, sNextUrl = cParser().parse(sHtmlContent, "page[^>]([\d]+)")
        if isMatchNextPage:
            if max(sNextUrl) > page:
                params.setParam('page', int(page) + 1)
                oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)
        oGui.setView('movies')
        oGui.setEndOfDirectory()


def showHosters():
    sUrl = ParameterHandler().getValue('entryUrl')
    sHtmlContent = cRequestHandler(sUrl).request()
    pattern = 'data-video-id="(.*?)"\sdata-provider="(.*?)"'
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)
    hosters = []
    if isMatch:
        for sID, sName in aResult:
            sHtmlContent = cRequestHandler(URL_MAIN + '/embed.php?video_id=' + sID + '&provider=' + sName).request()
            isMatch, aResult = cParser().parse(sHtmlContent, 'src="([^"]+)"')
            for sUrl in aResult:
                hoster = {'link': sUrl, 'name': sName}
                hosters.append(hoster)
    if hosters:
        hosters.append('getHosterUrl')
    return hosters


def getHosterUrl(sUrl=False):
    return [{'streamUrl': sUrl, 'resolved': False}]
