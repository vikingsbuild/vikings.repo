# -*- coding: utf-8 -*-
import sys, xbmc, xbmcgui
from resources.lib import logger
from resources.lib.config import cConfig
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.jsnprotect import *
from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.pluginHandler import cPluginHandler


def run():
    parseUrl()


def changeWatched(params):
    if not cConfig().getSetting('metahandler') == 'true': return
    meta = get_metahandler()
    if meta:
        season = ''
        episode = ''
        mediaType = params.getValue('mediaType')
        imdbID = params.getValue('imdbID')
        name = params.getValue('title')
        if params.exist('season'):
            season = params.getValue('season')
        if params.exist('episode'):
            episode = params.getValue('episode')
        if imdbID:
            meta.change_watched(mediaType, name, imdbID, season=season, episode=episode)
            xbmc.executebuiltin("XBMC.Container.Refresh")
    else:
        META = False
        logger.info("Could not import package 'metahandler'")
    return


def updateMeta(params):
    if not cConfig().getSetting('metahandler') == 'true':
        return
    # videoType, name, imdbID, season=season, episode=episode, year=year, watched=watched
    try:
        from metahandler import metahandlers
    except Exception as e:
        logger.info("Could not import package 'metahandler'")
        logger.info(e)
        return
    meta = get_metahandler()
    if not meta:
        return
    season = ''
    episode = ''
    mediaType = params.getValue('mediaType')
    imdbID = params.getValue('imdbID')
    name = str(params.getValue('title'))
    year = params.getValue('year')
    logger.info("MediaType: " + mediaType)
    if mediaType == 'movie' or mediaType == 'tvshow':
        # show meta search input
        oGui = cGui()
        sSearchText = oGui.showKeyBoard(name)
        if not sSearchText: return
        if mediaType == 'movie':
            try:
                foundInfo = meta.search_movies(sSearchText)
            except:
                logger.info('error or nothing found')
                foundInfo = False
        elif mediaType == 'tvshow':
            foundInfo = metahandlers.TheTVDB().get_matching_shows(sSearchText, language="all", want_raw=True)
        else:
            return

        if not foundInfo:
            oGui.showInfo('xStream', 'Suchanfrage lieferte kein Ergebnis')
            return
        # select possible match
        dialog = xbmcgui.Dialog()
        items = []
        for item in foundInfo:
            if mediaType == 'movie':
                items.append(str(item['title'].encode('utf-8')) + ' (' + str(item['year']) + ')')
            elif mediaType == 'tvshow':
                if 'FirstAired' in item:
                    items.append(
                        item['SeriesName'] + ' (' + str(item['FirstAired'])[:4] + ') ' + item.get('language', ''))
                else:
                    items.append(item['SeriesName'] + ' ' + item.get('language', ''))
            else:
                return
        index = dialog.select('Film/Serie wählen', items)
        if index > -1:
            item = foundInfo[index]
        else:
            return False

    if not imdbID:
        imdbID = ''
    if not year:
        year = ''
    if mediaType == 'movie':
        meta.update_meta(mediaType, name, imdbID, new_imdb_id=str(item['imdb_id']), new_tmdb_id=str(item['tmdb_id']),
                         year=year)
    elif mediaType == 'tvshow':
        if params.exist('season'):
            season = params.getValue('season')
            meta.update_season(name, imdbID, season)
        if params.exist('episode'):
            episode = params.getValue('episode')
        if season and episode:
            meta.update_episode_meta(name, imdbID, season, episode)
        elif season:
            meta.update_season(name, imdbID, season)
        else:
            meta.update_meta(mediaType, name, imdbID, new_imdb_id=str(item.get('IMDB_ID', '')),
                             new_tmdb_id=str(item['id']), year=year)
    xbmc.executebuiltin("XBMC.Container.Refresh")
    return


def get_metahandler():
    try:
        from metahandler import metahandlers
        return metahandlers.MetaData(tmdb_api_key=I11I1I1II1I1I1I1I1I())
    except Exception as e:
        logger.info("Could not import package 'metahandler'")
        logger.info(e)
        return False


def parseUrl():
    import urlparse
    netloc = [urlparse.urlparse(sys.argv[0]).netloc, '']
    if xbmc.getInfoLabel('Container.PluginName') not in netloc:
        sys.exit()
        return

    params = ParameterHandler()
    logger.info(params.getAllParameters())
    # If no function is set, we set it to the default "load" function
    if params.exist('function'):
        sFunction = params.getValue('function')
        if sFunction == 'spacer':
            return True
        elif sFunction == 'clearCache':
            from resources.lib.handler.requestHandler import cRequestHandler
            cRequestHandler('dummy').clearCache()
            return
        elif sFunction == 'changeWatched':
            changeWatched(params)
            return
        elif sFunction == 'updateMeta':
            updateMeta(params)
            return
        elif sFunction == 'searchAlter':
            searchAlter(params)
            return
        elif sFunction == 'updateXstream':
            from resources.lib import updateManager
            updateManager.xStreamUpdate()
            return
        elif sFunction == 'updateUrlResolver':
            from resources.lib import updateManager
            updateManager.urlResolverUpdate()
            return
        elif sFunction == 'updateAll':
            from resources.lib import updateManager
            updateManager.xStreamUpdate()
            updateManager.urlResolverUpdate()
            return
    elif params.exist('remoteplayurl'):
        try:
            import urlresolver
            remotePlayUrl = params.getValue('remoteplayurl')
            sLink = urlresolver.resolve(remotePlayUrl)
            if sLink:
                xbmc.executebuiltin("PlayMedia(" + sLink + ")")
            else:
                logger.info("Could not play remote url '%s'" % sLink)
        except urlresolver.resolver.ResolverError as e:
            logger.info('ResolverError: %s' % e)
        return
    else:
        sFunction = 'load'

    # Test if we should run a function on a special site
    if not params.exist('site'):
        xbmc.executebuiltin('XBMC.RunPlugin(%s?function=clearCache)' % sys.argv[0])

        xStreamUpdate = True if cConfig().getSetting('githubUpdateXstream') == 'true' else False
        urlResolverUpdate = True if cConfig().getSetting('githubUpdateUrlResolver') == 'true' else False

        if xStreamUpdate and urlResolverUpdate:
            xbmc.executebuiltin('XBMC.RunPlugin(%s?function=updateAll)' % sys.argv[0])
        elif xStreamUpdate:
            xbmc.executebuiltin('XBMC.RunPlugin(%s?function=updateXstream)' % sys.argv[0])
        elif urlResolverUpdate:
            xbmc.executebuiltin('XBMC.RunPlugin(%s?function=updateUrlResolver)' % sys.argv[0])
        # As a default if no site was specified, we run the default starting gui with all plugins
        showMainMenu(sFunction)
        return
    sSiteName = params.getValue('site')
    if params.exist('playMode'):
        from resources.lib.gui.hoster import cHosterGui
        url = False
        playMode = params.getValue('playMode')
        isHoster = params.getValue('isHoster')
        url = params.getValue('url')
        manual = params.exist('manual')
        if cConfig().getSetting(
                'hosterSelect') == 'Auto' and playMode != 'jd' and playMode != 'jd2' and playMode != 'pyload' and not manual:
            cHosterGui().streamAuto(playMode, sSiteName, sFunction)
        else:
            cHosterGui().stream(playMode, sSiteName, sFunction, url)
        return
    logger.info("Call function '%s' from '%s'" % (sFunction, sSiteName))
    # If the hoster gui is called, run the function on it and return
    if sSiteName == 'cHosterGui':
        showHosterGui(sFunction)
    # If global search is called
    elif sSiteName == 'globalSearch':
        searchterm = False
        if params.exist('searchterm'):
            searchterm = params.getValue('searchterm')

        searchGlobal(searchterm)
    elif sSiteName == 'favGui':
        showFavGui(sFunction)
    # If addon settings are called
    elif sSiteName == 'xStream':
        oGui = cGui()
        oGui.openSettings()
        oGui.updateDirectory()
    # If the urlresolver settings are called
    elif sSiteName == 'urlresolver':
        import urlresolver
        urlresolver.display_settings()
    # If metahandler settings are called
    elif sSiteName == 'metahandler':
        import metahandler
        metahandler.display_settings()
    elif sSiteName == 'settings':
        oGui = cGui()
        for folder in settingsGuiElements():
            oGui.addFolder(folder)
        oGui.setEndOfDirectory()
    else:
        # Else load any other site as plugin and run the function
        plugin = __import__(sSiteName, globals(), locals())
        function = getattr(plugin, sFunction)
        function()


def showMainMenu(sFunction):
    oGui = cGui()

    if cConfig().getSetting('GlobalSearchPosition') == 'true':
        oGui.addFolder(globalSearchGuiElement())

    oPluginHandler = cPluginHandler()
    aPlugins = oPluginHandler.getAvailablePlugins()
    if not aPlugins:
        logger.info("No (activated) Plugins found")
        # Open the settings dialog to choose a plugin that could be enabled
        oGui.openSettings()
        oGui.updateDirectory()
    else:
        # Create a gui element for every plugin found
        for aPlugin in sorted(aPlugins, key=lambda k: k['id']):
            oGuiElement = cGuiElement()
            oGuiElement.setTitle(aPlugin['name'])
            oGuiElement.setSiteName(aPlugin['id'])
            oGuiElement.setFunction(sFunction)
            if 'icon' in aPlugin and aPlugin['icon']:
                oGuiElement.setThumbnail(aPlugin['icon'])
            oGui.addFolder(oGuiElement)

        if cConfig().getSetting('GlobalSearchPosition') == 'false':
            oGui.addFolder(globalSearchGuiElement())

    if cConfig().getSetting('SettingsFolder') == 'true':
        # Create a gui element for Settingsfolder
        oGuiElement = cGuiElement()
        oGuiElement.setTitle(cConfig().getLocalizedString(30041))
        oGuiElement.setSiteName("settings")
        oGuiElement.setFunction("showSettingsFolder")
        oGuiElement.setThumbnail("DefaultAddonService.png")
        oGui.addFolder(oGuiElement)
    else:
        for folder in settingsGuiElements():
            oGui.addFolder(folder)
    oGui.setEndOfDirectory()


def settingsGuiElements():
    # Create a gui element for addon settings
    oGuiElement = cGuiElement()
    oGuiElement.setTitle(cConfig().getLocalizedString(30042))
    oGuiElement.setSiteName("xStream")
    oGuiElement.setFunction("display_settings")
    oGuiElement.setThumbnail("DefaultAddonProgram.png")
    xStreamSettings = oGuiElement

    # Create a gui element for urlresolver settings
    oGuiElement = cGuiElement()
    oGuiElement.setTitle(cConfig().getLocalizedString(30043))
    oGuiElement.setSiteName("urlresolver")
    oGuiElement.setFunction("display_settings")
    oGuiElement.setThumbnail("DefaultAddonRepository.png")
    urlResolverSettings = oGuiElement

    # Create a gui element for metahandler settings
    oGuiElement = cGuiElement()
    oGuiElement.setTitle(cConfig().getLocalizedString(30044))
    oGuiElement.setSiteName("metahandler")
    oGuiElement.setFunction("display_settings")
    oGuiElement.setThumbnail("DefaultAddonTvInfo.png")
    metaSettings = oGuiElement

    if cConfig().getSetting('metahandler') == 'true':
        return xStreamSettings, urlResolverSettings, metaSettings

    return xStreamSettings, urlResolverSettings


def globalSearchGuiElement():
    # Create a gui element for global search
    oGuiElement = cGuiElement()
    oGuiElement.setTitle(cConfig().getLocalizedString(30040))
    oGuiElement.setSiteName("globalSearch")
    oGuiElement.setFunction("globalSearch")
    oGuiElement.setThumbnail("DefaultAddonWebSkin.png")
    return oGuiElement


def showHosterGui(sFunction):
    from resources.lib.gui.hoster import cHosterGui
    oHosterGui = cHosterGui()
    function = getattr(oHosterGui, sFunction)
    function()
    return True


def searchGlobal(sSearchText=False):
    import threading
    oGui = cGui()
    oGui.globalSearch = True
    oGui._collectMode = True
    if not sSearchText:
        sSearchText = oGui.showKeyBoard()
    if not sSearchText: return True
    aPlugins = []
    aPlugins = cPluginHandler().getAvailablePlugins()
    dialog = xbmcgui.DialogProgress()
    dialog.create('xStream', "Searching...")
    numPlugins = len(aPlugins)
    threads = []
    for count, pluginEntry in enumerate(aPlugins):
        if not pluginEntry['globalsearch']:
            continue
        dialog.update((count + 1) * 50 / numPlugins, 'Searching: ' + str(pluginEntry['name']) + '...')
        logger.info('Searching for %s at %s' % (sSearchText.decode('utf-8'), pluginEntry['id']))
        t = threading.Thread(target=_pluginSearch, args=(pluginEntry, sSearchText, oGui), name=pluginEntry['name'])
        threads += [t]
        t.start()
    for count, t in enumerate(threads):
        t.join()
        dialog.update((count + 1) * 50 / numPlugins + 50, t.getName() + ' returned')
    dialog.close()
    # deactivate collectMode attribute because now we want the elements really added
    oGui._collectMode = False
    total = len(oGui.searchResults)
    dialog = xbmcgui.DialogProgress()
    dialog.create('xStream', "Gathering info...")
    for count, result in enumerate(sorted(oGui.searchResults, key=lambda k: k['guiElement'].getSiteName()), 1):
        oGui.addFolder(result['guiElement'], result['params'], bIsFolder=result['isFolder'], iTotal=total)
        dialog.update(count * 100 / total, str(count) + ' of ' + str(total) + ': ' + result['guiElement'].getTitle())
    dialog.close()
    oGui.setView()
    oGui.setEndOfDirectory()
    return True


def searchAlter(params):
    searchTitle = params.getValue('searchTitle')
    searchImdbId = params.getValue('searchImdbID')
    searchYear = params.getValue('searchYear')
    import threading
    oGui = cGui()
    oGui.globalSearch = True
    oGui._collectMode = True
    aPlugins = []
    aPlugins = cPluginHandler().getAvailablePlugins()
    dialog = xbmcgui.DialogProgress()
    dialog.create('xStream', "Searching...")
    numPlugins = len(aPlugins)
    threads = []
    for count, pluginEntry in enumerate(aPlugins):
        dialog.update((count + 1) * 50 / numPlugins, 'Searching: ' + str(pluginEntry['name']) + '...')
        logger.info('Searching for ' + searchTitle + pluginEntry['id'].encode('utf-8'))
        t = threading.Thread(target=_pluginSearch, args=(pluginEntry, searchTitle, oGui), name=pluginEntry['name'])
        threads += [t]
        t.start()
    for count, t in enumerate(threads):
        t.join()
        dialog.update((count + 1) * 50 / numPlugins + 50, t.getName() + ' returned')
    dialog.close()
    # check results, put this to the threaded part, too
    filteredResults = []
    for result in oGui.searchResults:
        guiElement = result['guiElement']
        logger.info('Site: %s Titel: %s' % (guiElement.getSiteName(), guiElement.getTitle()))
        if not searchTitle in guiElement.getTitle(): continue
        if guiElement._sYear and searchYear and guiElement._sYear != searchYear: continue
        if searchImdbId and guiElement.getItemProperties().get('imdbID', False) and guiElement.getItemProperties().get(
            'imdbID', False) != searchImdbId: continue
        filteredResults.append(result)

    oGui._collectMode = False
    total = len(filteredResults)
    for result in sorted(filteredResults, key=lambda k: k['guiElement'].getSiteName()):
        oGui.addFolder(result['guiElement'], result['params'], bIsFolder=result['isFolder'], iTotal=total)

    oGui.setView()
    oGui.setEndOfDirectory()
    xbmc.executebuiltin('Container.Update')
    return True


def _pluginSearch(pluginEntry, sSearchText, oGui):
    try:
        plugin = __import__(pluginEntry['id'], globals(), locals())
        function = getattr(plugin, '_search')
        function(oGui, sSearchText)
    except:
        logger.info(pluginEntry['name'] + ': search failed')
        import traceback
        logger.debug(traceback.format_exc())
