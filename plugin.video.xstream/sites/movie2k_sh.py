# -*- coding: utf-8 -*-
import base64
from resources.lib import logger
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser

SITE_IDENTIFIER = 'movie2k_sh'
SITE_NAME = 'Movie2k SH'
SITE_ICON = 'movie2k_sh.png'

URL_MAIN = 'http://movie2k.sh/'
URL_MOVIE = URL_MAIN + 'latest/'
URL_SEARCH = URL_MAIN + 'search/%s'


def load():
    logger.info("Load %s" % SITE_NAME)
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('Page', '30')
    params.setParam('sUrl', URL_MOVIE)
    params.setParam('nUrl', URL_MOVIE)
    oGui.addFolder(cGuiElement('Filme', SITE_IDENTIFIER, 'showEntries'), params)
    oGui.addFolder(cGuiElement('Genre', SITE_IDENTIFIER, 'showGenre'))
    oGui.addFolder(cGuiElement('Suche', SITE_IDENTIFIER, 'showSearch'))
    oGui.setEndOfDirectory()


def showGenre():
    oGui = cGui()
    params = ParameterHandler()
    sHtmlContent = cRequestHandler(URL_MOVIE).request()
    pattern = 'genre.*?<li[^<]class="nav'
    isMatch, sHtmlContainer = cParser.parseSingleResult(sHtmlContent, pattern)

    if isMatch:
        pattern = 'href="([^"]+)">([^<]+)'
        isMatch, aResult = cParser.parse(sHtmlContainer, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    for sUrl, sName in aResult:
        params.setParam('nUrl', URL_MAIN + sUrl)
        params.setParam('sUrl', URL_MAIN + sUrl)
        oGui.addFolder(cGuiElement(sName.strip(), SITE_IDENTIFIER, 'showEntries'), params)
    oGui.setEndOfDirectory()


def showEntries(entryUrl=False, sGui=False, sSearchText=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    if not entryUrl: entryUrl = params.getValue('sUrl')
    oRequest = cRequestHandler(entryUrl, ignoreErrors=(sGui is not False))
    oRequest.addHeaderEntry('Referer', entryUrl)
    sHtmlContent = oRequest.request()
    pattern = '<a[^>]class="coverImage"[^>]title="([^"]+)"[^>]href="([^"]+).*?"[^>]src="([^"]+).*?(.*?)</a>.*?</span>'
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)

    if not isMatch:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    cf = cRequestHandler.createUrl(entryUrl, oRequest)
    total = len(aResult)
    for sName, sUrl, sThumbnail, sLang in aResult:
        if sSearchText and not cParser().search(sSearchText, sName.replace(' ', '%20')):
            continue
        isMatch, sYear = cParser.parse(sName, "(.*?)\((\d*)\)")
        for name, year in sYear:
            sName = name
            sYear = year
            break
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showHosters')
        oGuiElement.setThumbnail(sThumbnail + cf)
        oGuiElement.setFanart(sThumbnail + cf)
        oGuiElement.setYear(sYear)
        if 'en.png' in sLang and 'de.png' in sLang:
            oGuiElement.setLanguage('Deutsch & Englisch')
        elif 'de.png' in sLang:
            oGuiElement.setLanguage('Deutsch')
        elif 'en.png' in sLang:
            oGuiElement.setLanguage('Englisch')
        else:
            oGuiElement.setLanguage('')
        params.setParam('entryUrl', sUrl)
        oGui.addFolder(oGuiElement, params, False, total)
    if not sGui:
        Page = params.getValue('Page')
        Page = int(Page) + int(30)
        params.setParam('Page', Page)
        if not params.getValue('nUrl') == False:
            params.setParam('sUrl', params.getValue('nUrl') + '/' + str(Page))
            oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)
        oGui.setView('movies')
        oGui.setEndOfDirectory()


def showHosters():
    sUrl = ParameterHandler().getValue('entryUrl')
    sHtmlContent = cRequestHandler(sUrl).request()
    pattern = 'domain=([^"]+)">.*?href="([^"]+)">.*?([^"]+).png'
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)
    hosters = []
    if isMatch:
        for sName, sUrl, sLang in aResult:
            if 'link=' in sUrl:
                refUrl = ParameterHandler().getValue('entryUrl')
                oRequest = cRequestHandler(refUrl + sUrl, caching=True)
                oRequest.addHeaderEntry("Referer", refUrl)
                sUrl = refUrl + sUrl
                sHtmlContent = oRequest.request()
                pattern = "dingdong[^>]'([^']+)"
                isMatch, sUrl = cParser().parse(sHtmlContent, pattern)
                sUrl = base64.b64decode(sUrl[0])
                pattern = 'id="emolink" src="([^"]+)'
                isMatch, sUrl = cParser().parse(sUrl, pattern)
                sUrl = sUrl[0]
            if '/de' in sLang:
                lang = ' (Deutsch)'
            elif '/en' in sLang:
                lang = ' (Englisch)'
            else:
                lang = ''
            hoster = {'link': sUrl, 'name': sName.strip() + lang}
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
    sSearchText = sSearchText.replace(' ', '%20')
    showEntries(URL_SEARCH % sSearchText, oGui, sSearchText)
