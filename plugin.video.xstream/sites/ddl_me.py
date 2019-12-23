# -*- coding: utf-8 -*-
import json
from resources.lib import logger
from resources.lib.config import cConfig
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser

SITE_IDENTIFIER = 'ddl_me'
SITE_NAME = 'DirectDownLoad'
SITE_ICON = 'ddl.png'
SITE_SETTINGS = '<setting default="de.ddl.me" enable="!eq(-2,false)" id="ddl_me-domain" label="30051" type="labelenum" values="de.ddl.me|en.ddl.me" />'

DOMAIN = cConfig().getSetting('ddl_me-domain')

URL_MAIN = 'https://' + DOMAIN
URL_SEARCH = URL_MAIN + '/search_99/?q='
URL_MOVIES = URL_MAIN + '/moviez'
URL_SHOWS = URL_MAIN + '/episodez'
URL_TOP100 = URL_MAIN + '/top100/cover/'

PARMS_GENRE_ALL = "_00"
PARMS_SORT_LAST_UPDATE = "_0"
PARMS_SORT_BLOCKBUSTER = "_1"
PARMS_SORT_IMDB_RATING = "_2"
PARMS_SORT_YEAR = "_3"


def load():
    logger.info("Load %s" % SITE_NAME)
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('sUrl', URL_MOVIES)
    params.setParam('sTop100Type', 'movies')
    oGui.addFolder(cGuiElement('Filme', SITE_IDENTIFIER, 'showMenu'), params)
    params.setParam('sUrl', URL_SHOWS)
    params.setParam('sTop100Type', 'tv')
    oGui.addFolder(cGuiElement('Serien', SITE_IDENTIFIER, 'showMenu'), params)
    params.setParam('sUrl', URL_TOP100 + 'total/all/')
    oGui.addFolder(cGuiElement('Hall of Fame', SITE_IDENTIFIER, 'showEntries'), params)
    oGui.addFolder(cGuiElement('Suche', SITE_IDENTIFIER, 'showSearch'))
    oGui.setEndOfDirectory()


def showMenu():
    oGui = cGui()
    params = ParameterHandler()
    baseURL = params.getValue('sUrl')
    oGui.addFolder(cGuiElement('Top 100', SITE_IDENTIFIER, 'showTop100'), params)
    params.setParam('sUrl', baseURL + PARMS_GENRE_ALL + PARMS_SORT_LAST_UPDATE)
    oGui.addFolder(cGuiElement('Letztes Update', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', baseURL + PARMS_GENRE_ALL + PARMS_SORT_BLOCKBUSTER)
    oGui.addFolder(cGuiElement('Blockbuster', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', baseURL + PARMS_GENRE_ALL + PARMS_SORT_IMDB_RATING)
    oGui.addFolder(cGuiElement('IMDB Rating', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', baseURL + PARMS_GENRE_ALL + PARMS_SORT_YEAR)
    oGui.addFolder(cGuiElement('Jahr', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', baseURL + PARMS_GENRE_ALL + PARMS_SORT_LAST_UPDATE)
    oGui.addFolder(cGuiElement('Genre', SITE_IDENTIFIER, 'showGenre'), params)
    oGui.setEndOfDirectory()


def showTop100():
    oGui = cGui()
    params = ParameterHandler()
    params.setParam('sUrl', URL_TOP100 + 'today/' + params.getValue('sTop100Type'))
    oGui.addFolder(cGuiElement('Heute', SITE_IDENTIFIER, 'showEntries'), params)
    params.setParam('sUrl', URL_TOP100 + 'month/' + params.getValue('sTop100Type'))
    oGui.addFolder(cGuiElement('Monat', SITE_IDENTIFIER, 'showEntries'), params)
    oGui.setEndOfDirectory()


def showGenre():
    oGui = cGui()
    params = ParameterHandler()
    sHtmlContent = cRequestHandler(params.getValue('sUrl')).request()
    pattern = '<i[^>]*class="genre.*?<span>Genre</span>'
    isMatch, sHtmlContainer = cParser.parseSingleResult(sHtmlContent, pattern)

    if isMatch:
        pattern = '<a[^>]*href="([^"]+)".*?i>([^<]+)'
        isMatch, aResult = cParser.parse(sHtmlContainer, pattern)

    if not isMatch:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    for sUrl, sName in aResult:
        params.setParam('sUrl', URL_MAIN + sUrl)
        oGui.addFolder(cGuiElement(sName.strip(), SITE_IDENTIFIER, 'showEntries'), params)
    oGui.setEndOfDirectory()


def showEntries(entryUrl=False, sGui=False, sSearchText=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    if not entryUrl: entryUrl = params.getValue('sUrl')
    sHtmlContent = cRequestHandler(entryUrl, ignoreErrors=(sGui is not False)).request()
    pattern = "type_(\d).*?title='([^']+)[^>]*href='([^']+).*?src='([^']+)"
    isMatch, aResult = cParser.parse(sHtmlContent, pattern)

    if not isMatch:
        if not sGui: oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    total = len(aResult)
    for smType, sName, sUrl, sThumbnail in aResult:
        if sSearchText and not cParser().search(sSearchText, sName):
            continue
        if smType == '3':
            continue
        if sThumbnail.startswith('//'):
            sThumbnail = 'https:' + sThumbnail
        isTvshow = True if "1" in smType else False
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showSeasons' if isTvshow else 'showHosters')
        oGuiElement.setMediaType('tvshow' if isTvshow else 'movie')
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        params.setParam('entryUrl', URL_MAIN + sUrl)
        params.setParam('sName', sName)
        params.setParam('sThumbnail', sThumbnail)
        oGui.addFolder(oGuiElement, params, isTvshow, total)
    if not sGui:
        pattern = "class='active'>\d</a><a[^>]href='([^']+)"
        isMatchNextPage, sNextUrl = cParser.parseSingleResult(sHtmlContent, pattern)
        if isMatchNextPage:
            params.setParam('sUrl', URL_MAIN + sNextUrl)
            oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)
        oGui.setView('tvshows' if 'download_1' in entryUrl else 'movies')
        oGui.setEndOfDirectory()


def showSeasons():
    oGui = cGui()
    params = ParameterHandler()
    sUrl = params.getValue('entryUrl')
    sHtmlContent = cRequestHandler(sUrl).request()
    aResult = cParser().parse(sHtmlContent, "var[ ]subcats[ ]=[ ](.*?);")

    if not aResult[0] or not aResult[1][0]:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    data = json.loads(aResult[1][0])
    seasons = []
    for key, value in data.items():
        SeasonsNr = int(value['info']['staffel'])
        if SeasonsNr not in seasons:
            seasons.append(SeasonsNr)
    sThumbnail = params.getValue('sThumbnail')
    sName = params.getValue('sName')
    seasons = sorted(seasons)
    isDesc, sDesc = cParser.parseSingleResult(sHtmlContent, '<img[^>]class.*?>(.*?)<br><br>')

    total = len(seasons)
    for iSeason in seasons:
        oGuiElement = cGuiElement("Staffel " + str(iSeason), SITE_IDENTIFIER, 'showEpisodes')
        oGuiElement.setTVShowTitle(sName)
        oGuiElement.setSeason(iSeason)
        oGuiElement.setMediaType('season')
        if isDesc:
            oGuiElement.setDescription(sDesc)
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        oGui.addFolder(oGuiElement, params, True, total)
    oGui.setView('seasons')
    oGui.setEndOfDirectory()


def showEpisodes():
    oGui = cGui()
    params = ParameterHandler()
    iSeason = int(params.getValue('season'))
    sThumbnail = params.getValue('sThumbnail')
    url = params.getValue('entryUrl')
    sHtmlContent = cRequestHandler(url).request()
    aResult = cParser().parse(sHtmlContent, "var[ ]subcats[ ]=[ ](.*?);")

    if not aResult[0] or not aResult[1][0]:
        oGui.showInfo('xStream', 'Es wurde kein Eintrag gefunden')
        return

    episodes = {}
    data = json.loads(aResult[1][0])
    for key, value in data.items():
        SeasonsNr = int(value['info']['staffel'])
        if SeasonsNr != iSeason:
            continue
        episodeNr = int(value['info']['nr'])
        if episodeNr not in episodes.keys():
            episodes.update({episodeNr: key})

    isMatchDesc, sDesc = cParser.parseSingleResult(sHtmlContent, '<img[^>]class.*?>(.*?)<br><br>')
    
    total = len(episodes)
    for sEpisodeNr, sEpisodesID in episodes.items():
        epiName = data[sEpisodesID]['info']['name'].encode('utf-8')
        epiName = epiName.split("»")[0].strip()
        oGuiElement = cGuiElement(str(sEpisodeNr) + " - " + epiName, SITE_IDENTIFIER, 'showHosters')
        oGuiElement.setEpisode(sEpisodeNr)
        oGuiElement.setMediaType('episode')
        if sDesc:
            oGuiElement.setDescription(sDesc)
        oGuiElement.setThumbnail(sThumbnail)
        oGuiElement.setFanart(sThumbnail)
        params.setParam('sJsonID', sEpisodesID)
        oGui.addFolder(oGuiElement, params, False, total)
    oGui.setView('episodes')
    oGui.setEndOfDirectory()


def showHosters():
    params = ParameterHandler()
    sHtmlContent = cRequestHandler(params.getValue('entryUrl')).request()
    aResult = cParser().parse(sHtmlContent, "var[ ]subcats[ ]=[ ](.*?);")
    if not aResult[0]: return []
    hosters = []
    data = json.loads(aResult[1][0])
    sJsonID = params.getValue('sJsonID')
    if not sJsonID:
        sJsonID = data.keys()[0]
    partCount = 1
    if '1' in data[sJsonID]:
        partCount = int(data[sJsonID]['1'])
    for jHoster in data[sJsonID]['links']:
        for jHosterEntry in data[sJsonID]['links'][jHoster]:
            if jHosterEntry[5] != 'stream': continue
            hoster = {}
            if partCount > 1:
                hoster['displayedName'] = jHoster + ' - Part ' + jHosterEntry[0]
            hoster['link'] = jHosterEntry[3]
            hoster['name'] = jHoster
            hosters.append(hoster)
    if len(hosters) > 0:
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
    showEntries(URL_SEARCH + sSearchText, oGui, sSearchText)
