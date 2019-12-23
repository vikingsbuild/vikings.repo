# -*- coding: utf-8 -*-
from resources.lib import logger
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.util import cUtil

SITE_IDENTIFIER = 'hd-streams_org'
SITE_NAME = 'HD-Streams'
SITE_ICON = 'hdstreams_org.png'

URL_MAIN = 'https://hd-streams.org/'
URL_FILME = URL_MAIN + 'movies?perPage=54'
URL_SERIE = URL_MAIN + 'seasons?perPage=54'
URL_SEARCH = URL_MAIN + 'search?q=%s&movies=true&seasons=true&actors=false&didyoumean=false'


def load():
    logger.info("Load %s" % SITE_NAME)
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('sUrl', URL_FILME)
    oGui.addFolder(cGuiElement('Filme', SITE_IDENTIFIER, 'showEntries'), params)
    oGui.addFolder(cGuiElement('Filme Genre', SITE_IDENTIFIER, 'showGenre'), params)
    params.setParam('sUrl', URL_SERIE)
    oGui.addFolder(cGuiElement('Serien', SITE_IDENTIFIER, 'showEntries'), params)
    oGui.addFolder(cGuiElement('Serien Genre', SITE_IDENTIFIER, 'showGenre'), params)
    oGui.addFolder(cGuiElement('Suche', SITE_IDENTIFIER, 'showSearch'))
    oGui.setEndOfDirectory()


def showGenre():
    oGui = cGui()
    params = ParameterHandler()
    entryUrl = params.getValue('sUrl')
    sHtmlContent = cRequestHandler(entryUrl).request()
    pattern = "text: '([^']+)', value: '([^']+)"
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)
    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return
    for sName, sID in aResult:
        params.setParam('sUrl', entryUrl + '&genre[]=' + sID)
        oGui.addFolder(cGuiElement(sName, SITE_IDENTIFIER, 'showEntries'), params)
    oGui.setEndOfDirectory()


def showEntries(entryUrl=False, sGui=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    if not entryUrl: entryUrl = params.getValue('sUrl')
    oRequest = cRequestHandler(entryUrl, ignoreErrors=(sGui is not False))
    sHtmlContent = oRequest.request()
    pattern = 'data-id=.*?">[^>]*<a[^>]href="([^"]+)".*?'
    pattern += "(?:url[^>]'([^']+)?).*?"
    pattern += 'filename">([^<]+)'
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)
    if not isMatch:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return
    cf = createUrl(entryUrl, oRequest)
    total = len(aResult)
    for sUrl, sThumbnail, sName in aResult:
        isMatch, sYear = cParser.parse(sName, "(.*?)\((\d*)\)")
        for name, year in sYear:
            sName = name
            sYear = year
            break
        isTvshow = True if "series" in sUrl else False
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showEpisodes' if isTvshow else 'showHosters')
        oGuiElement.setMediaType('tvshow' if isTvshow else 'movie')
        oGuiElement.setThumbnail(sThumbnail + cf)
        oGuiElement.setFanart(sThumbnail + cf)
        if sYear:
            oGuiElement.setYear(sYear)
        params.setParam('entryUrl', sUrl)
        oGui.addFolder(oGuiElement, params, isTvshow, total)
    isMatchNextPage, sNextUrl = cParser().parseSingleResult(sHtmlContent, '<a[^>]href="([^"]+)"[^>]*rel="next"')
    if isMatchNextPage:
        sNextUrl = cUtil.cleanse_text(sNextUrl)
        params.setParam('sUrl', sNextUrl)
        oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)
    if not sGui:
        oGui.setView('tvshows' if 'serie' in entryUrl else 'movies')
        oGui.setEndOfDirectory()


def showEpisodes():
    oGui = cGui()
    params = ParameterHandler()
    sUrl = params.getValue('entryUrl')
    oRequest = cRequestHandler(sUrl)
    sHtmlContent = oRequest.request()
    pattern = 'click="loadEpisode\S([\d]+).*?subheading">([^<]+)'
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)
    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return
    isMatchDesc, sDesc = cParser.parseSingleResult(sHtmlContent, '<div class="v-card__text">([^<]+)')
    isMatchFanart, sFanart = cParser.parseSingleResult(sHtmlContent, "background-image[^>]*url[^>]'([^']+)")
    cf = createUrl(sUrl, oRequest)
    total = len(aResult)
    for sName, sTitle in aResult:
        oGuiElement = cGuiElement(sName + ' - ' + sTitle, SITE_IDENTIFIER, 'showHosterserie')
        if sFanart:
            oGuiElement.setThumbnail(sFanart + cf)
            oGuiElement.setFanart(sFanart + cf)
        if sDesc:
            oGuiElement.setDescription(sDesc)
        params.setParam('Episodes', sName)
        oGui.addFolder(oGuiElement, params, False, total)
    oGui.setView('episodes')
    oGui.setEndOfDirectory()


def showHosterserie():
    sUrl = ParameterHandler().getValue('entryUrl')
    Episodes = ParameterHandler().getValue('Episodes')
    sHtmlContent = cRequestHandler(sUrl).request()
    pattern = "loadEpisodeStream[^>]'%s', '([^']+).*?title>([^<]+)" % Episodes
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)
    pattern = '<meta name="csrf-token" content="([^"]+)">'
    isMatch, token = cParser.parseSingleResult(sHtmlContent, pattern)
    hosters = []
    for h, sName in aResult:
        link = getLinks(sUrl, Episodes, h, token)
        hoster = {'link': link, 'name': sName}
        hosters.append(hoster)
    if hosters:
        hosters.append('getHosterUrl')
    return hosters


def showHosters():
    sUrl = ParameterHandler().getValue('entryUrl')
    sHtmlContent = cRequestHandler(sUrl).request()
    pattern = '<v-flex>[^>]*<v-btn.*?</v-flex>'
    isMatch, sHtmlContainer = cParser.parse(sHtmlContent, pattern)
    pattern = '<meta name="csrf-token" content="([^"]+)">'
    isMatch, token = cParser.parseSingleResult(sHtmlContent, pattern)
    hosters = []
    for a in sHtmlContainer:
        pattern = 'x">([^<]+)</v-btn>'
        isMatch, sQuality = cParser.parseSingleResult(a, pattern)
        pattern = "recaptcha[^>]'([^']+)', '([^']+)', '([^']+).*?"
        pattern += '">.*?>([^<]+)'
        isMatch, aResult = cParser().parse(a, pattern)
        for e, h, sLang, sName in aResult:
            link = getLinks(sUrl, e, h, token, sLang)
            hoster = {'link': link, 'name': sName.strip() + ' ' + sQuality.strip()}
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
    if not sSearchText: return
    showSearchEntries(URL_SEARCH % sSearchText.strip(), oGui, sSearchText)


def showSearchEntries(entryUrl=False, sGui=False, sSearchText=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    if not entryUrl: entryUrl = params.getValue('sUrl')
    sHtmlContent = cRequestHandler(URL_MAIN).request()
    pattern = '<meta name="csrf-token" content="([^"]+)">'
    isMatch, token = cParser.parseSingleResult(sHtmlContent, pattern)
    oRequest = cRequestHandler(entryUrl, ignoreErrors=(sGui is not False))
    oRequest.addHeaderEntry('X-Requested-With', 'XMLHttpRequest')
    oRequest.addHeaderEntry('X-CSRF-TOKEN', token)
    sHtmlContent = oRequest.request()
    pattern = '"title":"([^"]+).*?url":"([^"]+)'
    isMatch, aResult = cParser().parse(sHtmlContent, pattern)
    if not isMatch:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return
    total = len(aResult)
    for sName, sUrl in aResult:
        if sSearchText and not cParser().search(sSearchText, sName):
            continue
        isMatch, sYear = cParser.parse(sName, "(.*?)\((\d*)\)")
        for name, year in sYear:
            sName = name
            sYear = year
            break
        isTvshow = True if "series" in sUrl else False
        if 'season' in sUrl or 'movies' in sUrl:
            oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showEpisodes' if isTvshow else 'showHosters')
            if sYear:
                oGuiElement.setYear(sYear)
            params.setParam('entryUrl', sUrl.replace('\/', '/'))
            oGui.addFolder(oGuiElement, params, isTvshow, total)
    if not sGui:
        oGui.setEndOfDirectory()


def byteify(input, noneReplacement=None, baseTypesAsString=False):
    if isinstance(input, dict):
        return dict(
            [(byteify(key, noneReplacement, baseTypesAsString), byteify(value, noneReplacement, baseTypesAsString))
             for key, value in input.iteritems()])
    elif isinstance(input, list):
        return [byteify(element, noneReplacement, baseTypesAsString) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    elif input is None and noneReplacement != None:
        return noneReplacement
    elif baseTypesAsString:
        return str(input)
    else:
        return input


def getLinks(sUrl, e, h, token, sLang=False):
    import base64, json
    from binascii import unhexlify
    oRequest = cRequestHandler(sUrl + '/stream')
    oRequest.addHeaderEntry('X-CSRF-TOKEN', token)
    oRequest.addHeaderEntry('X-Requested-With', 'XMLHttpRequest')
    oRequest.addParameters('e', e)
    oRequest.addParameters('h', h)
    if sLang:
        oRequest.addParameters('lang', sLang)
    oRequest.setRequestType(1)
    sHtmlContent = oRequest.request()
    helper = json.loads(sHtmlContent)
    Data = byteify(helper)
    tmp = Data.get('d', '') + Data.get('c', '') + Data.get('iv', '') + Data.get('f', '') + Data.get(
        'h', '') + Data.get('b', '')
    tmp = byteify(json.loads(base64.b64decode(tmp)))
    salt = unhexlify(tmp['s'])
    ciphertext = base64.b64decode(tmp['ct'][::-1])
    b = base64.b64encode(token[::-1])
    tmp = cUtil.evp_decode(ciphertext, b, salt)
    tmp = byteify(json.loads(base64.b64decode(tmp)))
    ciphertext = base64.b64decode(tmp['ct'][::-1])
    salt = unhexlify(tmp['s'])
    b = ''
    a = token
    for idx in range(len(a) - 1, 0, -2):
        b += a[idx]
    if Data.get('e', None):
        b += '1'
    else:
        b += '0'
    tmp = cUtil.evp_decode(ciphertext, str(b), salt)
    return byteify(json.loads(tmp))


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
