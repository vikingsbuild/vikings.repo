import xbmcaddon

__plugin__ = 'Malandro'
__author__ = 'Coca-Cola Man'
__credits__ = 'Luis'

addon = xbmcaddon.Addon(id='plugin.video.malandro')
rootDir = addon.getAddonInfo('path')
if rootDir.endswith(';'):
    rootDir = rootDir[:-1]

class Main:
    def __init__(self):
        self.pDialog = None
        self.run()

    def run(self):
        import videodevil
        videodevil.Main()

Main()
