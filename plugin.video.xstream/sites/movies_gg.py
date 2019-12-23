# -*- coding: utf-8 -*-
import json, re
from resources.lib import logger
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser

def Il1lIl(dGV4dA):
    cmU = ""
    for YnVjaHN0YWJl in range(len(dGV4dA)):
        cmU = cmU + chr(ord(dGV4dA[YnVjaHN0YWJl]) - ord('40'[YnVjaHN0YWJl%len('30')]))
    return cmU

SITE_IDENTIFIER = 'movies_gg'
SITE_NAME = 'Movies.GG'
SITE_ICON = 'movies_gg.png'

URL_MAIN = 'https://movies.gg'
URL_API = URL_MAIN + Il1lIl('c}£¶ùïuÄ}o')
S0VZ = Il1lIl('Zõô©q©ütz{ñ~~ä§yu©hñå£ãàå')
URL_NEW = URL_API + Il1lIl('¢ï´è°ü™ôô£qedV§ëõïqUß') + S0VZ
URL_TOP = URL_API + Il1lIl('®ü§è°ü™ôô£qedV§ëõïqUß') + S0VZ
URL_POPULAR = URL_API + Il1lIl('§ü§•†ë¶è°ü™ôô£qedV§ëõïqUß') + S0VZ
URL_HOSTER = URL_API + Il1lIl('õï®è†ô¢õßmY£')
URL_GENRE = URL_API + Il1lIl('õï¢¢ô£qUß')
URL_GENRE2 = Il1lIl('Z££¢®èñ©qôòVßü¶§qtyÉwV§ëõïqUßV§ëõô¢ë®ïqed') + S0VZ
URL_SEARCH = URL_MAIN + Il1lIl('cîô_ßïï¢óòs°qUß')


def load():
    logger.info("Load %s" % SITE_NAME)
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('page', 1)
    params.setParam('sUrl', URL_NEW)
    oGui.addFolder(cGuiElement('Neueste Filme', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_TOP)
    oGui.addFolder(cGuiElement('Top Filme', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_POPULAR)
    oGui.addFolder(cGuiElement('Beliebte Filme', SITE_IDENTIFIER, 'showEntries'), params)
    oGui.addFolder(cGuiElement('Genre', SITE_IDENTIFIER, 'showGenre'))
    oGui.addFolder(cGuiElement('Suche', SITE_IDENTIFIER, 'showSearch'))
    oGui.setEndOfDirectory()


def showGenre():
    oGui = cGui()
    params = ParameterHandler()
    sHtmlContent = cRequestHandler('https://movies.gg/de/genres#genresmenu').request()
    isMatch, aResult = cParser.parse(sHtmlContent, '<a[^>]href="/de/genres/([^"]+)"')

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    for sName in aResult:
        params.setParam('sUrl', URL_GENRE % sName + URL_GENRE2)
        oGui.addFolder(cGuiElement(sName, SITE_IDENTIFIER, 'showEntries'), params)
    oGui.setEndOfDirectory()


def showEntries(entryUrl=False, sGui=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    if not entryUrl: entryUrl = params.getValue('sUrl')
    Page = params.getValue('page')
    sJson = cRequestHandler(entryUrl % Page, ignoreErrors=(sGui is not False)).request()

    if not sJson:
        if not sGui: oGui.showError('xStream', 'Fehler beim Laden der Daten.')
        return

    aJson = json.loads(sJson)

    if not 'data' in aJson or len(aJson['data']) == 0:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return
    iPage = int(params.getValue('page'))
    if iPage <= 0:
        iPage = 1
    total = len(aJson['data'])
    for item in aJson['data']:
        try:
            oGuiElement = cGuiElement(item['title'].encode('utf-8', 'ignore'), SITE_IDENTIFIER, 'showHosters')
            if item['release_date']:
                oGuiElement.setYear(str(item['release_date'][0:4]))
            if item['plot']:
                oGuiElement.setDescription((item['plot']))
            if item['poster_path']:
                oGuiElement.setThumbnail('https://image.tmdb.org/t/p/w185/' + item['poster_path'])
            if item['background']:
                oGuiElement.setFanart('https://image.tmdb.org/t/p/w185/' + item['background'])
            if item['runtime']:
                oGuiElement.addItemValue('duration', int(item['runtime']) * 60)
            params.setParam('id', str(item['id']))
            oGui.addFolder(oGuiElement, params, False, total)
        except:
            pass
    if not sGui:
        if float(aJson["last_page"]) > iPage:
            iPage = int(params.getValue('page'))
            params.setParam('page', (iPage + 1))
            oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)
            oGui.setView('movies')
        oGui.setEndOfDirectory()


def showHosters():
    oParams = ParameterHandler()
    id = oParams.getValue('id')
    sHtmlContent = cRequestHandler(URL_HOSTER % id + S0VZ).request()
    sPattern = '(http[^"]+)'
    isMatch, aResult = cParser().parse(sHtmlContent, sPattern)
    hosters = []
    for sUrl in aResult:
        sUrl = sUrl.replace('\/', '/')
        hname = re.compile('^(?:https?:\/\/)?(?:[^@\n]+@)?([^:\/\n]+)', flags=re.I | re.M).findall(sUrl)[0]
        hoster = {'link': sUrl, 'name': hname}
        hosters.append(hoster)
    if hosters:
        hosters.append('getHosterUrl')
    return hosters


def getHosterUrl(sUrl=False):
    return [{'streamUrl': sUrl, 'resolved': False}]


def showSearchEntries(entryUrl=False, sGui=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    if not entryUrl: entryUrl = params.getValue('sUrl')
    sHtmlContent = cRequestHandler(entryUrl, ignoreErrors=(sGui is not False)).request()
    pattern = '</a>.*?</div>.*?</div>.*?<a[^>]href="/de/stream/([\d]+).*?src="([^"]+)" alt="([^"]+)"'
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)

    if not isMatch:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    total = len(aResult)
    for sId, sThumbnail, sName in aResult:
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showHosters')
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        params.setParam('id', sId)
        oGui.addFolder(oGuiElement, params, False, total)
    if not sGui:
        oGui.setEndOfDirectory()


def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if not sSearchText: return
    _search(False, sSearchText)
    oGui.setEndOfDirectory()


def _search(oGui, sSearchText):
    if not sSearchText: return
    showSearchEntries(URL_SEARCH % sSearchText.strip(), oGui)
