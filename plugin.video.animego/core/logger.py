# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Logger multiplataforma
#------------------------------------------------------------
# pelisalacarta
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
# Creado por: Jesús (tvalacarta@gmail.com)
# Licencia: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
#------------------------------------------------------------
# Historial de cambios:
#------------------------------------------------------------

try:
    from core import config
except:
    import config



loggeractive = (config.get_setting("debug")=="true")

def log_enable(active):
    global loggeractive
    loggeractive = active

def info(texto):
    loggeractive=False
    if loggeractive:
            print texto

def debug(texto):
    if loggeractive:
            print texto

def error(texto):
    if loggeractive:
            print texto
