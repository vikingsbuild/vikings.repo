#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from os.path import join
from sys import path
import platform
from resources.lib import common
from resources.lib import logger

__settings__ = common.addon
__cwd__ = common.addonPath

# Add different library path
path.append(join(__cwd__, "resources", "lib"))
path.append(join(__cwd__, "resources", "lib", "gui"))
path.append(join(__cwd__, "resources", "lib", "handler"))
path.append(join(__cwd__, "resources", "art", "sites"))
path.append(join(__cwd__, "sites"))

# Run xstream
from xstream import run

logger.info('*---- Running xStream, version %s ----*' % __settings__.getAddonInfo('version'))
logger.info('Python-Version: %s' % platform.python_version())

try:
    run()
except Exception, err:
    if str(err) == 'UserAborted':
        logger.error("User aborted list creation")
    else:
        import traceback
        import xbmcgui

        logger.debug(traceback.format_exc())
        dialog = xbmcgui.Dialog().ok('Error', str(err.__class__.__name__) + " : " + str(err),
                                     str(traceback.format_exc().splitlines()[-3].split('addons')[-1]))
