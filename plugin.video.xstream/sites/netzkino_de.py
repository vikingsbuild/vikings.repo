# -*- coding: utf-8 -*-
import json
from resources.lib import logger
from resources.lib.config import cConfig
from resources.lib.gui.gui import cGui
from resources.lib.parser import cParser
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler


SITE_IDENTIFIER = 'netzkino_de'
SITE_NAME = 'NetzKino'
SITE_ICON = 'netzkino.png'

URL_MAIN = 'http://api.netzkino.de.simplecache.net/capi-2.0a/categories/%s.json?d=www&l=de-DE&v=unknown'
URL_SEARCH = 'http://api.netzkino.de.simplecache.net/capi-2.0a/search?q=%s&d=www&l=de-DE&v=unknown'


def load():
    logger.info("Load %s" % SITE_NAME)
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('sUrl', URL_MAIN % 'neu')
    oGui.addFolder(cGuiElement('Neu', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MAIN % 'actionkino')
    oGui.addFolder(cGuiElement('Actionkino', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MAIN % 'animekino')
    oGui.addFolder(cGuiElement('Animekino', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MAIN % 'arthousekino')
    oGui.addFolder(cGuiElement('Arthousekino', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MAIN % 'asiakino')
    oGui.addFolder(cGuiElement('Asiakino', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MAIN % 'dramakino')
    oGui.addFolder(cGuiElement('Dramakino', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MAIN % 'thrillerkino')
    oGui.addFolder(cGuiElement('Thrillerkino', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MAIN % 'liebesfilmkino')
    oGui.addFolder(cGuiElement('Liebesfilmkino', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MAIN % 'scifikino')
    oGui.addFolder(cGuiElement('Scifikino', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MAIN % 'kinderkino')
    oGui.addFolder(cGuiElement('Kinderkino', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MAIN % 'spasskino')
    oGui.addFolder(cGuiElement('Spasskino', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_MAIN % 'queerkino')
    oGui.addFolder(cGuiElement('Queerkino', SITE_IDENTIFIER, 'showEntries'), params)
    if showAdult():
        params.setParam('sUrl', URL_MAIN % 'horrorkino')
        oGui.addFolder(cGuiElement('Horrorkino', SITE_IDENTIFIER, 'showEntries'), params)
        params.setParam('sUrl', URL_MAIN % 'prickelkino')
        oGui.addFolder(cGuiElement('Prickelkino', SITE_IDENTIFIER, 'showEntries'), params)
        params.setParam('sUrl', URL_MAIN % 'kinoab18')
        oGui.addFolder(cGuiElement('Kino ab 18', SITE_IDENTIFIER, 'showEntries'), params)
    oGui.addFolder(cGuiElement('Suche', SITE_IDENTIFIER, 'showSearch'))
    oGui.setEndOfDirectory()


def showEntries(entryUrl=False, sGui=False, sSearchText=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    if not entryUrl: entryUrl = params.getValue('sUrl')
    isShowAdult = showAdult()
    sJson = cRequestHandler(entryUrl, ignoreErrors=(sGui is not False)).request()

    if not sJson:
        if not sGui: oGui.showError('xStream', 'Fehler beim Laden der Daten.')
        return

    aJson = json.loads(sJson)

    if not 'posts' in aJson or len(aJson['posts']) == 0:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    total = len(aJson['posts'])
    for item in aJson["posts"]:
        try:
            FSK = ','.join(item['custom_fields']['FSK'])
            if not isShowAdult and '18' in FSK.lower():
                continue
            if sSearchText and not cParser().search(sSearchText, item['title'].encode('utf-8', 'ignore')):
                continue

            oGuiElement = cGuiElement(item['title'].encode('utf-8', 'ignore'), SITE_IDENTIFIER, 'getHosterUrl')
            oGuiElement.setThumbnail(item['thumbnail'].encode('utf-8', 'ignore'))
            sFanart = ','.join(item['custom_fields']['featured_img_all'])
            oGuiElement.setFanart(sFanart.encode('utf-8', 'ignore'))
            sYahr = ','.join(item['custom_fields']['Jahr'])
            oGuiElement.setYear(sYahr)
            oGuiElement.setDescription(item['content'])
            Youtube = ','.join(item['custom_fields']['Youtube_Delivery_Id'])
            Streaming = ','.join(item['custom_fields']['Streaming'])
            params.setParam('Youtube', Youtube)
            params.setParam('Streaming', Streaming)
            oGui.addFolder(oGuiElement, params, False, total)
        except:
            pass
    if not sGui:
        oGui.setEndOfDirectory()


def getHosterUrl(Streaming=False):
    if not Streaming: Streaming = ParameterHandler().getValue('Streaming')
    sUrl = 'http://netzkino_and-vh.akamaihd.net/i/%s.mp4/master.m3u8' % Streaming
    results = []
    result = {'streamUrl': sUrl, 'resolved': True}
    results.append(result)
    return results


def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if not sSearchText: return
    _search(False, sSearchText)
    oGui.setEndOfDirectory()


def _search(oGui, sSearchText):
    if not sSearchText: return
    showEntries(URL_SEARCH % sSearchText.strip(), oGui, sSearchText)

def showAdult():
    oConfig = cConfig()
    if oConfig.getSetting('showAdult') == 'true':
        return True
    return False
