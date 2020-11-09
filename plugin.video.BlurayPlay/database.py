import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmc,os,xbmcaddon, xbmcvfs
import sqlite3
try:    from sqlite3 import dbapi2 as database
except: from pysqlite2 import dbapi2 as database

def get_kversion():
	full_version_info = xbmc.getInfoLabel('System.BuildVersion')
	baseversion = full_version_info.split(".")
	intbase = int(baseversion[0])
	# if intbase > 16.5:
	# 	log('HIGHER THAN 16.5')
	# if intbase < 16.5:
	# 	log('LOWER THAN 16.5')
	return  intbase
    
def set_enabled(addon_id):
    if get_kversion() >16.5:
        try:
            dir_database = xbmc.translatePath("special://profile/Database")
            file_database = os.path.join(dir_database, 'Addons27.db')
            sqliteConnection = database.connect(file_database)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            print('****DATABASE: '+file_database+'****')
            state = 1
            print('***DATABASE ID ADDON: '+addon_id+' *****')
            cursor.execute("UPDATE installed SET enabled= ? WHERE addonID= ?", (state, addon_id,))            
            sqliteConnection.commit()
            print("Record Updated successfully")
            xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
            #xbmc.executebuiltin("XBMC.Container.Update()")
            #xbmc.executebuiltin("XBMC.Container.Refresh()")           
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
        finally:
            if (cursor):
                cursor.close()
                print("The sqlite connection is closed") 
 

def enable_addon(state, addon_id):
        try:            
            dir_database = xbmc.translatePath("special://profile/Database")
            file_database = os.path.join(dir_database, 'Addons27.db')
            sqliteConnection = database.connect(file_database)
            cursor = sqliteConnection.cursor()
            r = cursor.execute('SELECT * FROM installed WHERE enabled = ? AND addonID= ?', (state, addon_id,))
            if r.fetchone() == None:
                print('Addons Verificados!')
            else:
                print('Addon encontrado')
                set_enabled(addon_id)                
        except sqlite3.Error as error:
            print("Failed to check sqlite table", error)
        finally:
            if (cursor):
                cursor.close()
                print("The sqlite connection is closed")

def check_database(addon_id):
    enable_addon(0, addon_id)
#checkintegrity13122019