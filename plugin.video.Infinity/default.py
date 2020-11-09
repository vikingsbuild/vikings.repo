# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import cookielib , base64
import generator
from BeautifulSoup import BeautifulStoneSoup , BeautifulSoup , BeautifulSOAP
oo000 = None
try :
 from xml . sax . saxutils import escape
except : traceback . print_exc ( )
try :
 import json
except :
 import simplejson as json
import SimpleDownloader as downloader
import time
ii = False
oOOo = [ '180upload.com' , 'allmyvideos.net' , 'bestreams.net' , 'clicknupload.com' , 'cloudzilla.to' , 'movshare.net' , 'novamov.com' , 'nowvideo.sx' , 'videoweed.es' , 'daclips.in' , 'datemule.com' , 'fastvideo.in' , 'faststream.in' , 'filehoot.com' , 'filenuke.com' , 'sharesix.com' , 'plus.google.com' , 'picasaweb.google.com' , 'gorillavid.com' , 'gorillavid.in' , 'grifthost.com' , 'hugefiles.net' , 'ipithos.to' , 'ishared.eu' , 'kingfiles.net' , 'mail.ru' , 'my.mail.ru' , 'videoapi.my.mail.ru' , 'mightyupload.com' , 'mooshare.biz' , 'movdivx.com' , 'movpod.net' , 'movpod.in' , 'movreel.com' , 'mrfile.me' , 'nosvideo.com' , 'openload.io' , 'played.to' , 'bitshare.com' , 'filefactory.com' , 'k2s.cc' , 'oboom.com' , 'rapidgator.net' , 'primeshare.tv' , 'bitshare.com' , 'filefactory.com' , 'k2s.cc' , 'oboom.com' , 'rapidgator.net' , 'sharerepo.com' , 'stagevu.com' , 'streamcloud.eu' , 'streamin.to' , 'thefile.me' , 'thevideo.me' , 'tusfiles.net' , 'uploadc.com' , 'zalaa.com' , 'uploadrocket.net' , 'uptobox.com' , 'v-vids.com' , 'veehd.com' , 'vidbull.com' , 'videomega.tv' , 'vidplay.net' , 'vidspot.net' , 'vidto.me' , 'vidzi.tv' , 'vimeo.com' , 'vk.com' , 'vodlocker.com' , 'xfileload.com' , 'xvidstage.com' , 'zettahost.tv' ]
O0 = [ 'plugin.video.dramasonline' , 'plugin.video.f4mTester' , 'plugin.video.shahidmbcnet' , 'plugin.video.SportsDevil' , 'plugin.stream.vaughnlive.tv' , 'plugin.video.ZemTV-shani' ]
if 70 - 70: oo0 . O0OO0O0O - oooo
class iIIii1IIi ( urllib2 . HTTPErrorProcessor ) :
 def http_response ( self , request , response ) :
  return response
 https_response = http_response
 if 73 - 73: II111iiii
def IiII1IiiIiI1 ( url ) :
 xbmc . Player ( ) . play ( "" + url + "" )
 if 40 - 40: oo * OoO0O00
IIiIiII11i = False ;
if IIiIiII11i :
 if 51 - 51: oOo0O0Ooo * I1ii11iIi11i
 if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
 try :
  import pysrc . pydevd as pydevd
  if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
  pydevd . settrace ( 'localhost' , stdoutToServer = True , stderrToServer = True )
 except ImportError :
  sys . stderr . write ( "Error: " +
 "You must add org.python.pydev.debug.pysrc to your PYTHONPATH." )
  sys . exit ( 1 )
  if 97 - 97: oO0o0ooO0 - IIII / O0oO - IiII
iiI11iii111 = xbmcaddon . Addon ( ) . getAddonInfo ( 'id' )
i1I1Ii1iI1ii = xbmcaddon . Addon ( id = iiI11iii111 )
II1iI = i1I1Ii1iI1ii . getAddonInfo ( 'name' )
i1iIii1Ii1II = i1I1Ii1iI1ii . getAddonInfo ( 'version' )
i1I1Iiii1111 = xbmc . translatePath ( i1I1Ii1iI1ii . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
i11 = xbmc . translatePath ( i1I1Ii1iI1ii . getAddonInfo ( 'path' ) . decode ( 'utf-8' ) )
I11 = os . path . join ( i1I1Iiii1111 , 'history' )
Oo0o0000o0o0 = os . path . join ( i1I1Iiii1111 , 'list_revision' )
oOo0oooo00o = os . path . join ( i11 , 'icon.png' )
oO0o0o0ooO0oO = os . path . join ( i11 , 'fanart.jpg' )
oo0o0O00 = os . path . join ( i11 , 'source_file' )
oO = os . path . join ( i1I1Iiii1111 , 'source_file' )
i1iiIIiiI111 = i1I1Iiii1111
downloader = downloader . SimpleDownloader ( )
oooOOOOO = i1I1Ii1iI1ii . getSetting ( 'debug' )
if 22 - 22: ooOoO0o * O0OO0O0O / I11i
if os . path . exists ( oo0o0O00 ) == True :
 o00ooooO0oO = open ( oo0o0O00 ) . read ( )
else : o00ooooO0oO = [ ]
if os . path . exists ( oO ) == True :
 o00ooooO0oO = open ( oO ) . read ( )
else : o00ooooO0oO = [ ]
if 63 - 63: OOooOOo % oo
def o0oOo0Ooo0O ( string ) :
 if oooOOOOO == 'true' :
  xbmc . log ( "[addon Lists-%s]: %s" % ( i1iIii1Ii1II , string ) )
  if 81 - 81: Ii1I * oO0o0ooO0 * I1Ii111 - o00O0oo - I11i
def OooO0OO ( ) :
 iiiIi = json . loads ( open ( oO ) . read ( ) )
 if len ( iiiIi ) > 1 :
  for IiIIIiI1I1 in iiiIi :
   if isinstance ( IiIIIiI1I1 , list ) :
    OoO000 ( IiIIIiI1I1 [ 0 ] . encode ( 'utf-8' ) , IiIIIiI1I1 [ 1 ] . encode ( 'utf-8' ) , 1 , oOo0oooo00o , oO0o0o0ooO0oO , '' , '' , '' , '' , 'source' )
   else :
    IIiiIiI1 = oOo0oooo00o
    iiIiIIi = oO0o0o0ooO0oO
    ooOoo0O = ''
    OooO0 = ''
    credits = ''
    II11iiii1Ii = ''
    if IiIIIiI1I1 . has_key ( 'thumbnail' ) :
     IIiiIiI1 = IiIIIiI1I1 [ 'thumbnail' ]
    if IiIIIiI1I1 . has_key ( 'fanart' ) :
     iiIiIIi = IiIIIiI1I1 [ 'fanart' ]
    if IiIIIiI1I1 . has_key ( 'description' ) :
     ooOoo0O = IiIIIiI1I1 [ 'description' ]
    if IiIIIiI1I1 . has_key ( 'date' ) :
     OooO0 = IiIIIiI1I1 [ 'date' ]
    if IiIIIiI1I1 . has_key ( 'genre' ) :
     II11iiii1Ii = IiIIIiI1I1 [ 'genre' ]
    if IiIIIiI1I1 . has_key ( 'credits' ) :
     credits = IiIIIiI1I1 [ 'credits' ]
    OoO000 ( IiIIIiI1I1 [ 'title' ] . encode ( 'utf-8' ) , IiIIIiI1I1 [ 'url' ] . encode ( 'utf-8' ) , 1 , IIiiIiI1 , iiIiIIi , ooOoo0O , II11iiii1Ii , OooO0 , credits , 'source' )
    if 70 - 70: iII111i / oooo % O0oO % oo0 . oOo0O0Ooo
 else :
  if len ( iiiIi ) == 1 :
   if isinstance ( iiiIi [ 0 ] , list ) :
    O0o0Oo ( iiiIi [ 0 ] [ 1 ] . encode ( 'utf-8' ) , oO0o0o0ooO0oO )
   else :
    O0o0Oo ( iiiIi [ 0 ] [ 'url' ] , iiiIi [ 0 ] [ 'fanart' ] )
    if 78 - 78: oooo - ooOoO0o * oO0o + I11i + o00O0oo + o00O0oo
def I11I11i1I ( url = None ) :
 if url is None :
  if not i1I1Ii1iI1ii . getSetting ( "new_url_source" ) == "" :
   ii11i1iIII = i1I1Ii1iI1ii . getSetting ( 'new_url_source' ) . decode ( 'utf-8' )
 else :
  ii11i1iIII = url
 if ii11i1iIII == '' or ii11i1iIII is None :
  return
 o0oOo0Ooo0O ( 'Adding New Source: ' + ii11i1iIII . encode ( 'utf-8' ) )
 if 3 - 3: oo / oOo0O0Ooo % I1Ii111 * oo0 / O0OO0O0O * I1Ii111
 III1ii1iII = None
 if 54 - 54: oOo0O0Ooo % OoO0O00 % OoO0O00
 iI1 = i11Iiii ( ii11i1iIII )
 print 'source_url' , ii11i1iIII
 if isinstance ( iI1 , BeautifulSOAP ) :
  if iI1 . find ( 'channels_info' ) :
   III1ii1iII = iI1 . channels_info
  elif iI1 . find ( 'items_info' ) :
   III1ii1iII = iI1 . items_info
 if III1ii1iII :
  iI = { }
  iI [ 'url' ] = ii11i1iIII
  try : iI [ 'title' ] = III1ii1iII . title . string
  except : pass
  try : iI [ 'thumbnail' ] = III1ii1iII . thumbnail . string
  except : pass
  try : iI [ 'fanart' ] = III1ii1iII . fanart . string
  except : pass
  try : iI [ 'genre' ] = III1ii1iII . genre . string
  except : pass
  try : iI [ 'description' ] = III1ii1iII . description . string
  except : pass
  try : iI [ 'date' ] = III1ii1iII . date . string
  except : pass
  try : iI [ 'credits' ] = III1ii1iII . credits . string
  except : pass
 else :
  if '/' in ii11i1iIII :
   I1i1I1II = ii11i1iIII . split ( '/' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '\\' in ii11i1iIII :
   I1i1I1II = ii11i1iIII . split ( '\\' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '%' in I1i1I1II :
   I1i1I1II = urllib . unquote_plus ( I1i1I1II )
  i1 = xbmc . Keyboard ( I1i1I1II , 'Dar um nome á lista:' )
  i1 . doModal ( )
  if ( i1 . isConfirmed ( ) == False ) :
   return
  IiIiiI = i1 . getText ( )
  if len ( IiIiiI ) == 0 :
   return
  iI = { }
  iI [ 'title' ] = IiIiiI
  iI [ 'url' ] = ii11i1iIII
  iI [ 'fanart' ] = iiIiIIi
  if 31 - 31: ooOoO0o . ooOoO0o - I11i / oO0o + O0oO * oOo0O0Ooo
 if os . path . exists ( oO ) == False :
  O0ooOooooO = [ ]
  O0ooOooooO . append ( iI )
  o00O = open ( oO , "w" )
  o00O . write ( json . dumps ( O0ooOooooO ) )
  o00O . close ( )
 else :
  iiiIi = json . loads ( open ( oO , "r" ) . read ( ) )
  iiiIi . append ( iI )
  o00O = open ( oO , "w" )
  o00O . write ( json . dumps ( iiiIi ) )
  o00O . close ( )
 i1I1Ii1iI1ii . setSetting ( 'new_url_source' , "" )
 xbmc . executebuiltin ( "XBMC.Notification(" + II1iI + ",Adicionado.,5000," + oOo0oooo00o + ")" )
 if not url is None :
  if 'xbmcplus.xb.funpic.de' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=14,replace)" % sys . argv [ 0 ] )
  elif 'community-links' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=10,replace)" % sys . argv [ 0 ] )
 else : i1I1Ii1iI1ii . openSettings ( )
 if 69 - 69: iII111i % IIII - I11i + IIII - O0OO0O0O % II111iiii
def Iii111II ( name ) :
 iiiIi = json . loads ( open ( oO , "r" ) . read ( ) )
 for iiii11I in range ( len ( iiiIi ) ) :
  if isinstance ( iiiIi [ iiii11I ] , list ) :
   if iiiIi [ iiii11I ] [ 0 ] == name :
    del iiiIi [ iiii11I ]
    o00O = open ( oO , "w" )
    o00O . write ( json . dumps ( iiiIi ) )
    o00O . close ( )
    break
  else :
   if iiiIi [ iiii11I ] [ 'title' ] == name :
    del iiiIi [ iiii11I ]
    o00O = open ( oO , "w" )
    o00O . write ( json . dumps ( iiiIi ) )
    o00O . close ( )
    break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 96 - 96: OoO0O00 % ooOoO0o . IiII + II111iiii * iII111i - OOooOOo
def O0o0Oo ( url , fanart , data = None ) :
 i11i1 = i11Iiii ( url , data )
 if 29 - 29: Ii1I % oOo0O0Ooo + O0oO / I11i + IiII * I11i
 if isinstance ( i11i1 , BeautifulSOAP ) :
  if 42 - 42: ooOoO0o + iII111i
  if len ( i11i1 ( 'channels' ) ) > 0 and i1I1Ii1iI1ii . getSetting ( 'donotshowbychannels' ) == 'false' :
   o0O0o0Oo = i11i1 ( 'channel' )
   for Ii11Ii1I in o0O0o0Oo :
    if 72 - 72: o00O0oo / oo * I1ii11iIi11i - IIII
    if 51 - 51: OoO0O00 * oO0o % I11i * OoO0O00 % Ii1I / O0oO
    iIIIIii1 = ''
    oo000OO00Oo = 0
    try :
     iIIIIii1 = Ii11Ii1I ( 'externallink' ) [ 0 ] . string
     oo000OO00Oo = len ( Ii11Ii1I ( 'externallink' ) )
    except : pass
    if 51 - 51: oO0o0ooO0 * I11i + I1Ii111 + oO0o
    if oo000OO00Oo > 1 : iIIIIii1 = ''
    if 66 - 66: OOooOOo
    oO000Oo000 = Ii11Ii1I ( 'name' ) [ 0 ] . string
    i111IiI1I = Ii11Ii1I ( 'thumbnail' ) [ 0 ] . string
    if i111IiI1I == None :
     i111IiI1I = ''
     if 70 - 70: ooOoO0o . I1ii11iIi11i / I11i . ooOoO0o - O0OO0O0O / oO0o0ooO0
    try :
     if not Ii11Ii1I ( 'fanart' ) :
      if i1I1Ii1iI1ii . getSetting ( 'use_thumb' ) == "true" :
       ooOooo000oOO = i111IiI1I
      else :
       ooOooo000oOO = fanart
     else :
      ooOooo000oOO = Ii11Ii1I ( 'fanart' ) [ 0 ] . string
     if ooOooo000oOO == None :
      raise
    except :
     ooOooo000oOO = fanart
     if 59 - 59: OoO0O00 + II111iiii * OOooOOo + oo
    try :
     ooOoo0O = Ii11Ii1I ( 'info' ) [ 0 ] . string
     if ooOoo0O == None :
      raise
    except :
     ooOoo0O = ''
     if 58 - 58: OoO0O00 * IiII * Ii1I / IiII
    try :
     II11iiii1Ii = Ii11Ii1I ( 'genre' ) [ 0 ] . string
     if II11iiii1Ii == None :
      raise
    except :
     II11iiii1Ii = ''
     if 75 - 75: iII111i
    try :
     OooO0 = Ii11Ii1I ( 'date' ) [ 0 ] . string
     if OooO0 == None :
      raise
    except :
     OooO0 = ''
     if 50 - 50: ooOoO0o / I1ii11iIi11i - iII111i - I1Ii111 % o00O0oo - iII111i
    try :
     credits = Ii11Ii1I ( 'credits' ) [ 0 ] . string
     if credits == None :
      raise
    except :
     credits = ''
     if 91 - 91: oO0o / I1Ii111 - OoO0O00 . I1Ii111
    try :
     if iIIIIii1 == '' :
      OoO000 ( oO000Oo000 . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 2 , i111IiI1I , ooOooo000oOO , ooOoo0O , II11iiii1Ii , OooO0 , credits , True )
     else :
      if 18 - 18: I11i
      OoO000 ( oO000Oo000 . encode ( 'utf-8' ) , iIIIIii1 . encode ( 'utf-8' ) , 1 , i111IiI1I , ooOooo000oOO , ooOoo0O , II11iiii1Ii , OooO0 , None , 'source' )
    except :
     o0oOo0Ooo0O ( 'There was a problem adding directory from getData(): ' + oO000Oo000 . encode ( 'utf-8' , 'ignore' ) )
  else :
   o0oOo0Ooo0O ( 'No Channels: getItems' )
   O0o0O00Oo0o0 ( i11i1 ( 'item' ) , fanart )
 else :
  O00O0oOO00O00 ( i11i1 )
  if 11 - 11: oO0o0ooO0 . Ii1I
def o0 ( url , fanart , data = None ) :
 i11i1 = oo0oOo ( url , data )
 if 89 - 89: OOooOOo
 if isinstance ( i11i1 , BeautifulSOAP ) :
  if 68 - 68: oO0o * II111iiii % O0OO0O0O + oO0o + O0oO
  if len ( i11i1 ( 'channels' ) ) > 0 and i1I1Ii1iI1ii . getSetting ( 'donotshowbychannels' ) == 'false' :
   o0O0o0Oo = i11i1 ( 'channel' )
   for Ii11Ii1I in o0O0o0Oo :
    if 4 - 4: O0oO + O0OO0O0O * IiII
    if 55 - 55: I1ii11iIi11i + oooo / OOooOOo * iII111i - oo0 - ooOoO0o
    iIIIIii1 = ''
    oo000OO00Oo = 0
    try :
     iIIIIii1 = Ii11Ii1I ( 'externallink' ) [ 0 ] . string
     oo000OO00Oo = len ( Ii11Ii1I ( 'externallink' ) )
    except : pass
    if 25 - 25: Ii1I
    if oo000OO00Oo > 1 : iIIIIii1 = ''
    if 7 - 7: oo / oOo0O0Ooo * IIII . oO0o0ooO0 . oooo
    oO000Oo000 = Ii11Ii1I ( 'name' ) [ 0 ] . string
    i111IiI1I = Ii11Ii1I ( 'thumbnail' ) [ 0 ] . string
    if i111IiI1I == None :
     i111IiI1I = ''
     if 13 - 13: IiII / oo0
    try :
     if not Ii11Ii1I ( 'fanart' ) :
      if i1I1Ii1iI1ii . getSetting ( 'use_thumb' ) == "true" :
       ooOooo000oOO = i111IiI1I
      else :
       ooOooo000oOO = fanart
     else :
      ooOooo000oOO = Ii11Ii1I ( 'fanart' ) [ 0 ] . string
     if ooOooo000oOO == None :
      raise
    except :
     ooOooo000oOO = fanart
     if 2 - 2: oOo0O0Ooo / O0OO0O0O / I11i % OOooOOo % ooOoO0o
    try :
     ooOoo0O = Ii11Ii1I ( 'info' ) [ 0 ] . string
     if ooOoo0O == None :
      raise
    except :
     ooOoo0O = ''
     if 52 - 52: I11i
    try :
     II11iiii1Ii = Ii11Ii1I ( 'genre' ) [ 0 ] . string
     if II11iiii1Ii == None :
      raise
    except :
     II11iiii1Ii = ''
     if 95 - 95: ooOoO0o
    try :
     OooO0 = Ii11Ii1I ( 'date' ) [ 0 ] . string
     if OooO0 == None :
      raise
    except :
     OooO0 = ''
     if 87 - 87: O0oO + OOooOOo . IiII + OOooOOo
    try :
     credits = Ii11Ii1I ( 'credits' ) [ 0 ] . string
     if credits == None :
      raise
    except :
     credits = ''
     if 91 - 91: O0OO0O0O
    try :
     if iIIIIii1 == '' :
      OoO000 ( oO000Oo000 . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 2 , i111IiI1I , ooOooo000oOO , ooOoo0O , II11iiii1Ii , OooO0 , credits , True )
     else :
      if 61 - 61: OoO0O00
      OoO000 ( oO000Oo000 . encode ( 'utf-8' ) , iIIIIii1 . encode ( 'utf-8' ) , 11 , i111IiI1I , ooOooo000oOO , ooOoo0O , II11iiii1Ii , OooO0 , None , 'source' )
    except :
     o0oOo0Ooo0O ( 'There was a problem adding directory from getData(): ' + oO000Oo000 . encode ( 'utf-8' , 'ignore' ) )
  else :
   o0oOo0Ooo0O ( 'No Channels: getItems' )
   O0o0O00Oo0o0 ( i11i1 ( 'item' ) , fanart )
 else :
  O00O0oOO00O00 ( i11i1 )
  if 64 - 64: O0oO / OOooOOo - O0OO0O0O - I1Ii111
  if 86 - 86: I1Ii111 % OOooOOo / oOo0O0Ooo / OOooOOo
def O00O0oOO00O00 ( data ) :
 iIIi1i1 = data . rstrip ( )
 i1IIIiiII1 = re . compile ( r'#EXTINF:(.+?),(.*?)[\n\r]+([^\r\n]+)' ) . findall ( iIIi1i1 )
 OOOOoOoo0O0O0 = len ( i1IIIiiII1 )
 print 'tsdownloader' , ii
 if 85 - 85: iII111i % oo0 - o00O0oo * II111iiii / oOo0O0Ooo % oOo0O0Ooo
 for IIiIi1iI , i1IiiiI1iI , i1iIi in i1IIIiiII1 :
  if 68 - 68: oo0 % Ii1I + oo0
  if 'tvg-logo' in IIiIi1iI :
   i111IiI1I = iii ( IIiIi1iI , 'tvg-logo=[\'"](.*?)[\'"]' )
   if i111IiI1I :
    if i111IiI1I . startswith ( 'http' ) :
     i111IiI1I = i111IiI1I
     if 1 - 1: I1ii11iIi11i / I11i % o00O0oo * oO0o0ooO0 . oo0
    elif not i1I1Ii1iI1ii . getSetting ( 'logo-folderPath' ) == "" :
     III1Iiii1I11 = i1I1Ii1iI1ii . getSetting ( 'logo-folderPath' )
     i111IiI1I = III1Iiii1I11 + i111IiI1I
     if 9 - 9: Ii1I / I1ii11iIi11i - oOo0O0Ooo / II111iiii / oooo - I11i
    else :
     i111IiI1I = i111IiI1I
     if 91 - 91: o00O0oo % oo % oooo
     if 20 - 20: IiII % ooOoO0o / ooOoO0o + ooOoO0o
  else :
   i111IiI1I = ''
   if 45 - 45: iII111i - oO0o0ooO0 - II111iiii - oO0o . OoO0O00 / O0OO0O0O
  if 'type' in IIiIi1iI :
   oo0o00O = iii ( IIiIi1iI , 'type=[\'"](.*?)[\'"]' )
   if oo0o00O == 'yt-dl' :
    i1iIi = i1iIi + "&mode=18"
   elif oo0o00O == 'regex' :
    o00O0OoO = i1iIi . split ( '&regexs=' )
    if 16 - 16: oooo
    oOooOOOoOo = i1Iii1i1I ( oo0oOo ( '' , data = o00O0OoO [ 1 ] ) )
    if 91 - 91: Ii1I + oOo0O0Ooo . IiII * Ii1I + oOo0O0Ooo * I1ii11iIi11i
    O000OOOOOo ( o00O0OoO [ 0 ] , i1IiiiI1iI , i111IiI1I , '' , '' , '' , '' , '' , None , oOooOOOoOo , OOOOoOoo0O0O0 )
    continue
   elif oo0o00O == 'ftv' :
    i1iIi = 'plugin://plugin.video.F.T.V/?name=' + urllib . quote ( i1IiiiI1iI ) + '&url=' + i1iIi + '&mode=125&ch_fanart=na'
  elif ii and '.ts' in i1iIi :
   i1iIi = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( i1iIi ) + '&amp;streamtype=TSDOWNLOADER&name=' + urllib . quote ( i1IiiiI1iI )
  O000OOOOOo ( i1iIi , i1IiiiI1iI , i111IiI1I , '' , '' , '' , '' , '' , None , '' , OOOOoOoo0O0O0 )
def Iiii1i1 ( name , url , fanart ) :
 i11i1 = oo0oOo ( url )
 OO = i11i1 . find ( 'channel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 oo000o = OO ( 'item' )
 try :
  ooOooo000oOO = OO ( 'fanart' ) [ 0 ] . string
  if ooOooo000oOO == None :
   raise
 except :
  ooOooo000oOO = fanart
 for Ii11Ii1I in OO ( 'subchannel' ) :
  name = Ii11Ii1I ( 'name' ) [ 0 ] . string
  try :
   i111IiI1I = Ii11Ii1I ( 'thumbnail' ) [ 0 ] . string
   if i111IiI1I == None :
    raise
  except :
   i111IiI1I = ''
  try :
   if not Ii11Ii1I ( 'fanart' ) :
    if i1I1Ii1iI1ii . getSetting ( 'use_thumb' ) == "true" :
     ooOooo000oOO = i111IiI1I
   else :
    ooOooo000oOO = Ii11Ii1I ( 'fanart' ) [ 0 ] . string
   if ooOooo000oOO == None :
    raise
  except :
   pass
  try :
   ooOoo0O = Ii11Ii1I ( 'info' ) [ 0 ] . string
   if ooOoo0O == None :
    raise
  except :
   ooOoo0O = ''
   if 44 - 44: oo % OoO0O00 + I1Ii111
  try :
   II11iiii1Ii = Ii11Ii1I ( 'genre' ) [ 0 ] . string
   if II11iiii1Ii == None :
    raise
  except :
   II11iiii1Ii = ''
   if 45 - 45: o00O0oo / o00O0oo + IIII + O0oO
  try :
   OooO0 = Ii11Ii1I ( 'date' ) [ 0 ] . string
   if OooO0 == None :
    raise
  except :
   OooO0 = ''
   if 47 - 47: I11i + O0oO
  try :
   credits = Ii11Ii1I ( 'credits' ) [ 0 ] . string
   if credits == None :
    raise
  except :
   credits = ''
   if 82 - 82: OoO0O00 . oO0o0ooO0 - oooo - oO0o0ooO0 * OoO0O00
  try :
   OoO000 ( name . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 3 , i111IiI1I , ooOooo000oOO , ooOoo0O , II11iiii1Ii , credits , OooO0 )
  except :
   o0oOo0Ooo0O ( 'There was a problem adding directory - ' + name . encode ( 'utf-8' , 'ignore' ) )
 O0o0O00Oo0o0 ( oo000o , ooOooo000oOO )
 if 77 - 77: oooo * oO0o
def oOooOo0 ( text , start_with , end_with ) :
 i1I1ii11i1Iii = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return i1I1ii11i1Iii
 if 26 - 26: I1Ii111 - oooo - oOo0O0Ooo / oO0o . OOooOOo % oooo
def OOiIiIIi1 ( name , url , iconimage , fanart ) :
 I1IIII1i = [ ] ; I1I11i = [ ] ; Ii1I1I1i1Ii = 0
 i1Oo0oO00o = oOooOo0 ( url , 'sublink:' , '#' )
 for i11I1II1I11i in i1Oo0oO00o :
  OooOoOO0 = i11I1II1I11i . replace ( 'sublink:' , '' ) . replace ( '#' , '' )
  if 36 - 36: oO0o0ooO0
  if len ( OooOoOO0 ) > 10 :
   Ii1I1I1i1Ii = Ii1I1I1i1Ii + 1 ; I1IIII1i . append ( name + ' Source [' + str ( Ii1I1I1i1Ii ) + ']' ) ; I1I11i . append ( OooOoOO0 )
   if 36 - 36: O0oO / O0OO0O0O * I1ii11iIi11i - IiII % oooo * iII111i
 if Ii1I1I1i1Ii == 1 :
  try :
   if 79 - 79: O0OO0O0O
   oOO00O = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage ) ; oOO00O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
   OOOoo0OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1I11i [ 0 ] , listitem = oOO00O )
   xbmc . Player ( ) . play ( oO0o0 ( I1I11i [ 0 ] ) , oOO00O )
  except :
   pass
 else :
  iI1Ii11iIiI1 = xbmcgui . Dialog ( )
  OO0Oooo0oOO0O = iI1Ii11iIiI1 . select ( '[COLOR red]Flecha[/COLOR] [COLOR black]Negra[/COLOR] Escolha um link:' , I1IIII1i )
  if OO0Oooo0oOO0O >= 0 :
   o00O0 = name
   oOO0O00Oo0O0o = str ( I1I11i [ OO0Oooo0oOO0O ] )
   if 13 - 13: II111iiii
   try :
    oOO00O = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage ) ; oOO00O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
    OOOoo0OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOO0O00Oo0O0o , listitem = oOO00O )
    xbmc . Player ( ) . play ( oO0o0 ( oOO0O00Oo0O0o ) , oOO00O )
   except :
    pass
    if 33 - 33: IIII + o00O0oo * iII111i / oooo - oOo0O0Ooo
def O0oOOO0ooOOO0OOO ( name , url , fanart ) :
 i11i1 = oo0oOo ( url )
 OO = i11i1 . find ( 'subchannel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 oo000o = OO ( 'subitem' )
 O0o0O00Oo0o0 ( oo000o , fanart )
 if 63 - 63: OOooOOo * o00O0oo
def O0o0O00Oo0o0 ( items , fanart , dontLink = False ) :
 OOOOoOoo0O0O0 = len ( items )
 o0oOo0Ooo0O ( 'Total Items: %s' % OOOOoOoo0O0O0 )
 ooiIi1 = i1I1Ii1iI1ii . getSetting ( 'add_playlist' )
 OoOOoOooooOOo = i1I1Ii1iI1ii . getSetting ( 'ask_playlist_items' )
 oOo0O = i1I1Ii1iI1ii . getSetting ( 'use_thumb' )
 oo0O0 = i1I1Ii1iI1ii . getSetting ( 'parentalblocked' )
 oo0O0 = oo0O0 == "true"
 for iIOO0O000 in items :
  iiIiI1i1 = False
  oO0O00oOOoooO = False
  if 46 - 46: oOo0O0Ooo - II111iiii - I1Ii111 * OoO0O00
  I1i1I11I = 'false'
  try :
   I1i1I11I = iIOO0O000 ( 'parentalblock' ) [ 0 ] . string
  except :
   o0oOo0Ooo0O ( 'parentalblock Error' )
   I1i1I11I = ''
  if I1i1I11I == 'true' and oo0O0 : continue
  if 80 - 80: oo0 % O0oO + ooOoO0o % I1Ii111 - Ii1I
  try :
   oO000Oo000 = iIOO0O000 ( 'title' ) [ 0 ] . string
   if oO000Oo000 is None :
    oO000Oo000 = 'unknown?'
  except :
   o0oOo0Ooo0O ( 'Name Error' )
   oO000Oo000 = ''
   if 18 - 18: o00O0oo - IiII . IIII . oooo
   if 2 - 2: IiII . oO0o
  try :
   if iIOO0O000 ( 'epg' ) :
    if iIOO0O000 . epg_url :
     o0oOo0Ooo0O ( 'Get EPG Regex' )
     O0ooooOOoo0O = iIOO0O000 . epg_url . string
     II1IiiIi1i = iIOO0O000 . epg_regex . string
     iiI11ii1I1 = Ooo0OOoOoO0 ( O0ooooOOoo0O , II1IiiIi1i )
     if iiI11ii1I1 :
      oO000Oo000 += ' - ' + iiI11ii1I1
    elif iIOO0O000 ( 'epg' ) [ 0 ] . string > 1 :
     oO000Oo000 += oOo0OOoO0 ( iIOO0O000 ( 'epg' ) [ 0 ] . string )
   else :
    pass
  except :
   o0oOo0Ooo0O ( 'EPG Error' )
  try :
   o00O0OoO = [ ]
   if len ( iIOO0O000 ( 'link' ) ) > 0 :
    if 11 - 11: Ii1I . oO0o * oO0o0ooO0 * II111iiii + O0oO
    if 33 - 33: O0OO0O0O * I11i - IIII % IIII
    for IiIIIiI1I1 in iIOO0O000 ( 'link' ) :
     if not IiIIIiI1I1 . string == None :
      o00O0OoO . append ( IiIIIiI1I1 . string )
      if 18 - 18: IIII / I1ii11iIi11i * IIII + IIII * oo0 * Ii1I
   elif len ( iIOO0O000 ( 'sportsdevil' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'sportsdevil' ) :
     if not IiIIIiI1I1 . string == None :
      I1II1 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + IiIIIiI1I1 . string
      oooO = iIOO0O000 ( 'referer' ) [ 0 ] . string
      if oooO :
       if 26 - 26: ooOoO0o % Ii1I
       I1II1 = I1II1 + '%26referer=' + oooO
      o00O0OoO . append ( I1II1 )
   elif len ( iIOO0O000 ( 'p2p' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'p2p' ) :
     if not IiIIIiI1I1 . string == None :
      if 'sop://' in IiIIIiI1I1 . string :
       o00Oo0oooooo = 'plugin://plugin.video.p2p-streams/?mode=2url=' + IiIIIiI1I1 . string + '&' + 'name=' + oO000Oo000
       o00O0OoO . append ( o00Oo0oooooo )
      else :
       O0oO0 = 'plugin://plugin.video.p2p-streams/?mode=1&url=' + IiIIIiI1I1 . string + '&' + 'name=' + oO000Oo000
       o00O0OoO . append ( O0oO0 )
   elif len ( iIOO0O000 ( 'vaughn' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'vaughn' ) :
     if not IiIIIiI1I1 . string == None :
      iII11 = 'plugin://plugin.stream.vaughnlive.tv/?mode=PlayLiveStream&amp;channel=' + IiIIIiI1I1 . string
      o00O0OoO . append ( iII11 )
   elif len ( iIOO0O000 ( 'ilive' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'ilive' ) :
     if not IiIIIiI1I1 . string == None :
      if not 'http' in IiIIIiI1I1 . string :
       iiIiii1IIIII = 'plugin://plugin.video.tbh.ilive/?url=http://www.streamlive.to/view/' + IiIIIiI1I1 . string + '&amp;link=99&amp;mode=iLivePlay'
      else :
       iiIiii1IIIII = 'plugin://plugin.video.tbh.ilive/?url=' + IiIIIiI1I1 . string + '&amp;link=99&amp;mode=iLivePlay'
   elif len ( iIOO0O000 ( 'yt-dl' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'yt-dl' ) :
     if not IiIIIiI1I1 . string == None :
      o00o = IiIIIiI1I1 . string + '&mode=18'
      o00O0OoO . append ( o00o )
   elif len ( iIOO0O000 ( 'dm' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'dm' ) :
     if not IiIIIiI1I1 . string == None :
      II = "plugin://plugin.video.dailymotion_com/?mode=playVideo&url=" + IiIIIiI1I1 . string
      o00O0OoO . append ( II )
   elif len ( iIOO0O000 ( 'dmlive' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'dmlive' ) :
     if not IiIIIiI1I1 . string == None :
      II = "plugin://plugin.video.dailymotion_com/?mode=playLiveVideo&url=" + IiIIIiI1I1 . string
      o00O0OoO . append ( II )
      if 7 - 7: Ii1I - oOo0O0Ooo . oooo - oo
   elif len ( iIOO0O000 ( 'vidatvbn' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'vidatvbn' ) :
     if not IiIIIiI1I1 . string == None :
      o0OOOoO0 = 'http://www.thenightanimes.net/p//video-mp4.php?v=' + IiIIIiI1I1 . string
      o00O0OoO . append ( o0OOOoO0 )
      if 73 - 73: I1Ii111 % oo0 - oOo0O0Ooo
   elif len ( iIOO0O000 ( 'vidatvb' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'vidatvb' ) :
     if not IiIIIiI1I1 . string == None :
      Ii1iI111II1I1 = 'http://www.branimes.com/video/video-play.mp4/?contentId=' + IiIIIiI1I1 . string
      o00O0OoO . append ( Ii1iI111II1I1 )
      if 91 - 91: IiII % IiII - oOo0O0Ooo
   elif len ( iIOO0O000 ( 'Link' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'Link' ) :
     if not IiIIIiI1I1 . string == None :
      I1iiii1I = 'http://twixar.me/' + IiIIIiI1I1 . string
      o00O0OoO . append ( I1iiii1I )
      if 54 - 54: oOo0O0Ooo / IIII / oooo % oO0o % ooOoO0o
   elif len ( iIOO0O000 ( 'bit' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'bit' ) :
     if not IiIIIiI1I1 . string == None :
      oooOoOoo0oOo00 = 'https://goo.gl/' + IiIIIiI1I1 . string
      o00O0OoO . append ( oooOoOoo0oOo00 )
      if 32 - 32: oOo0O0Ooo % oooo / oo - oOo0O0Ooo
   elif len ( iIOO0O000 ( 'goo' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'goo' ) :
     if not IiIIIiI1I1 . string == None :
      I1III1111iIi = 'https://bit.ly/' + IiIIIiI1I1 . string
      o00O0OoO . append ( I1III1111iIi )
      if 38 - 38: o00O0oo + I1Ii111 / IIII % O0oO - Ii1I
   elif len ( iIOO0O000 ( 'vidatvg' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'vidatvg' ) :
     if not IiIIIiI1I1 . string == None :
      iI11 = 'plugin://plugin.video.gdrive?mode=streamURL&amp;url=https://docs.google.com/file/d/' + IiIIIiI1I1 . string
      o00O0OoO . append ( iI11 )
      if 10 - 10: OoO0O00 / iII111i % II111iiii * I1Ii111 % Ii1I
   elif len ( iIOO0O000 ( 'playthis' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'playthis' ) :
     if not IiIIIiI1I1 . string == None :
      I1i11 = 'plugin://plugin.video.playthis/?mode=play&player=false&path=' + IiIIIiI1I1 . string
      o00O0OoO . append ( I1i11 )
      if 12 - 12: oo + oo - Ii1I * I1ii11iIi11i % I1ii11iIi11i - OoO0O00
   elif len ( iIOO0O000 ( 'sony' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'sony' ) :
     if not IiIIIiI1I1 . string == None :
      o0O = "" + IiIIIiI1I1 . string + "" '|User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
      o00O0OoO . append ( o0O )
      if 84 - 84: oO0o + oo - OoO0O00 . Ii1I * II111iiii + oOo0O0Ooo
   elif len ( iIOO0O000 ( 'urlsolve' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'urlsolve' ) :
     if not IiIIIiI1I1 . string == None :
      II1i11I = '' + IiIIIiI1I1 . string + ''
      o00O0OoO . append ( II1i11I )
      if 50 - 50: II111iiii % I1Ii111
   elif len ( iIOO0O000 ( 'vidaonef' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'vidaonef' ) :
     if not IiIIIiI1I1 . string == None :
      IIii1111 = 'plugin://plugin.video.playthis/?mode=play&player=false&path=https://emcc-my.sharepoint.com/:v:/g/personal/vidafilmes_ondrive_pw/' + IiIIIiI1I1 . string + '?download=1&rebase=on'
      o00O0OoO . append ( IIii1111 )
      if 42 - 42: I1Ii111 / I11i . iII111i + iII111i % OOooOOo + oo0
   elif len ( iIOO0O000 ( 'vidaones' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'vidaones' ) :
     if not IiIIIiI1I1 . string == None :
      oo0o0000 = 'plugin://plugin.video.playthis/?mode=play&player=false&path=https://emcc-my.sharepoint.com/:v:/g/personal/vidaseries_ondrive_pw/' + IiIIIiI1I1 . string + '?download=1&rebase=on'
      o00O0OoO . append ( oo0o0000 )
      if 11 - 11: oooo
   elif len ( iIOO0O000 ( 'base64x' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'base64x' ) :
     if not IiIIIiI1I1 . string == None :
      IiIIII1i11I = base64 . b64decode ( '' + IiIIIiI1I1 . string + '' )
      o00O0OoO . append ( IiIIII1i11I )
      if 86 - 86: I1ii11iIi11i . O0OO0O0O - II111iiii . oO0o + ooOoO0o
   elif len ( iIOO0O000 ( 'm3u' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'm3u' ) :
     if not IiIIIiI1I1 . string == None :
      if 57 - 57: I11i . oo . oO0o0ooO0 * oo0 + IIII . oO0o0ooO0
      oo0O00Oooo0O0 = "plugin://plugin.video.m3u/?logos=&amp;move=0&amp;mode=3&amp;index=-1&amp;url=" + IiIIIiI1I1 . string
      o00O0OoO . append ( oo0O00Oooo0O0 )
      if 34 - 34: O0oO . I11i % O0OO0O0O * o00O0oo + oOo0O0Ooo
   elif len ( iIOO0O000 ( 'yutube' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'yutube' ) :
     if not IiIIIiI1I1 . string == None :
      if 77 - 77: ooOoO0o + OoO0O00 . OOooOOo * IIII + IiII + IiII
      I1ii1I1iiii = 'plugin://plugin.video.youtube/playlist/' + IiIIIiI1I1 . string + '/'
      o00O0OoO . append ( I1ii1I1iiii )
      if 36 - 36: II111iiii . oO0o
      if 56 - 56: I1ii11iIi11i . Ii1I . oOo0O0Ooo
      if 39 - 39: O0OO0O0O + IIII
   elif len ( iIOO0O000 ( 'utube' ) ) > 0 :
    OoOooOoO = len ( iIOO0O000 ( 'utube' ) )
    for IiIIIiI1I1 in iIOO0O000 ( 'utube' ) :
     if not IiIIIiI1I1 . string == None :
      if ' ' in IiIIIiI1I1 . string :
       iiIiii1iI1i = 'plugin://plugin.video.youtube/search/?q=' + urllib . quote_plus ( IiIIIiI1I1 . string )
       oO0O00oOOoooO = iiIiii1iI1i
      elif len ( IiIIIiI1I1 . string ) == 11 :
       iiIiii1iI1i = 'plugin://plugin.video.youtube/play/?video_id=' + IiIIIiI1I1 . string
      elif ( IiIIIiI1I1 . string . startswith ( 'PL' ) and not '&order=' in IiIIIiI1I1 . string ) or IiIIIiI1I1 . string . startswith ( 'UU' ) :
       iiIiii1iI1i = 'plugin://plugin.video.youtube/play/?&order=default&playlist_id=' + IiIIIiI1I1 . string
      elif IiIIIiI1I1 . string . startswith ( 'PL' ) or IiIIIiI1I1 . string . startswith ( 'UU' ) :
       iiIiii1iI1i = 'plugin://plugin.video.youtube/play/?playlist_id=' + IiIIIiI1I1 . string
      elif IiIIIiI1I1 . string . startswith ( 'UC' ) and len ( IiIIIiI1I1 . string ) > 12 :
       iiIiii1iI1i = 'plugin://plugin.video.youtube/channel/' + IiIIIiI1I1 . string + '/'
       oO0O00oOOoooO = iiIiii1iI1i
       if 34 - 34: O0oO * oOo0O0Ooo . oo * O0oO / O0oO
       if 30 - 30: Ii1I + I1ii11iIi11i / I1ii11iIi11i % Ii1I . Ii1I
      elif not IiIIIiI1I1 . string . startswith ( 'UC' ) and not ( IiIIIiI1I1 . string . startswith ( 'PL' ) ) :
       iiIiii1iI1i = 'plugin://plugin.video.youtube/user/' + IiIIIiI1I1 . string + '/'
       oO0O00oOOoooO = iiIiii1iI1i
     o00O0OoO . append ( iiIiii1iI1i )
   elif len ( iIOO0O000 ( 'imdb' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'imdb' ) :
     if not IiIIIiI1I1 . string == None :
      if i1I1Ii1iI1ii . getSetting ( 'genesisorpulsar' ) == '0' :
       O0O0Oo00 = 'plugin://plugin.video.genesis/?action=play&imdb=' + IiIIIiI1I1 . string
      else :
       O0O0Oo00 = 'plugin://plugin.video.pulsar/movie/tt' + IiIIIiI1I1 . string + '/play'
      o00O0OoO . append ( O0O0Oo00 )
   elif len ( iIOO0O000 ( 'f4m' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'f4m' ) :
     if not IiIIIiI1I1 . string == None :
      if '.f4m' in IiIIIiI1I1 . string :
       oOoO00o = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( IiIIIiI1I1 . string )
      elif '.m3u8' in IiIIIiI1I1 . string :
       oOoO00o = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( IiIIIiI1I1 . string ) + '&amp;streamtype=HLS'
       if 100 - 100: I11i + IiII * I11i
      else :
       oOoO00o = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( IiIIIiI1I1 . string ) + '&amp;streamtype=SIMPLE'
     o00O0OoO . append ( oOoO00o )
   elif len ( iIOO0O000 ( 'ftv' ) ) > 0 :
    for IiIIIiI1I1 in iIOO0O000 ( 'ftv' ) :
     if not IiIIIiI1I1 . string == None :
      oOOo0OOOo00O = 'plugin://plugin.video.F.T.V/?name=' + urllib . quote ( oO000Oo000 ) + '&url=' + IiIIIiI1I1 . string + '&mode=125&ch_fanart=na'
     o00O0OoO . append ( oOOo0OOOo00O )
   elif len ( iIOO0O000 ( 'urlsolve' ) ) > 0 :
    if 76 - 76: oo0 + I11i / Ii1I - oO0o - ooOoO0o + Ii1I
    for IiIIIiI1I1 in iIOO0O000 ( 'urlsolve' ) :
     if not IiIIIiI1I1 . string == None :
      ooI1i = IiIIIiI1I1 . string + '&mode=19'
      o00O0OoO . append ( ooI1i )
   if len ( o00O0OoO ) < 1 :
    raise
  except :
   o0oOo0Ooo0O ( 'Error <link> element, Passing:' + oO000Oo000 . encode ( 'utf-8' , 'ignore' ) )
   continue
  try :
   iiIiI1i1 = iIOO0O000 ( 'externallink' ) [ 0 ] . string
  except : pass
  if 32 - 32: OOooOOo / oO0o + IiII
  if iiIiI1i1 :
   ii1I1i1iiiI = [ iiIiI1i1 ]
   iiIiI1i1 = True
  else :
   iiIiI1i1 = False
  try :
   oO0O00oOOoooO = iIOO0O000 ( 'jsonrpc' ) [ 0 ] . string
  except : pass
  if oO0O00oOOoooO :
   if 96 - 96: II111iiii + iII111i
   ii1I1i1iiiI = [ oO0O00oOOoooO ]
   if 44 - 44: iII111i
   oO0O00oOOoooO = True
  else :
   oO0O00oOOoooO = False
  try :
   i111IiI1I = iIOO0O000 ( 'thumbnail' ) [ 0 ] . string
   if i111IiI1I == None :
    raise
  except :
   i111IiI1I = ''
  try :
   if not iIOO0O000 ( 'fanart' ) :
    if i1I1Ii1iI1ii . getSetting ( 'use_thumb' ) == "true" :
     ooOooo000oOO = i111IiI1I
    else :
     ooOooo000oOO = fanart
   else :
    ooOooo000oOO = iIOO0O000 ( 'fanart' ) [ 0 ] . string
   if ooOooo000oOO == None :
    raise
  except :
   ooOooo000oOO = fanart
  try :
   ooOoo0O = iIOO0O000 ( 'info' ) [ 0 ] . string
   if ooOoo0O == None :
    raise
  except :
   ooOoo0O = ''
   if 20 - 20: I1Ii111 + ooOoO0o / O0OO0O0O % oooo
  try :
   II11iiii1Ii = iIOO0O000 ( 'genre' ) [ 0 ] . string
   if II11iiii1Ii == None :
    raise
  except :
   II11iiii1Ii = ''
   if 88 - 88: OOooOOo / OoO0O00
  try :
   OooO0 = iIOO0O000 ( 'date' ) [ 0 ] . string
   if OooO0 == None :
    raise
  except :
   OooO0 = ''
   if 87 - 87: Ii1I - Ii1I - o00O0oo + iII111i
  oOooOOOoOo = None
  if iIOO0O000 ( 'regex' ) :
   try :
    OOooo = iIOO0O000 ( 'regex' )
    oOooOOOoOo = i1Iii1i1I ( OOooo )
   except :
    pass
  try :
   if 31 - 31: I11i % oO0o
   if len ( o00O0OoO ) > 1 :
    iI1I = 0
    OooOoOo = [ ]
    III1I1Iii1iiI = True if '$$LSPlayOnlyOne$$' in o00O0OoO [ 0 ] else False
    if 17 - 17: ooOoO0o % oooo - oooo
    for IiIIIiI1I1 in o00O0OoO :
     if ooiIi1 == "false" and not III1I1Iii1iiI :
      iI1I += 1
      O000OOOOOo ( IiIIIiI1I1 , '%s) %s' % ( iI1I , oO000Oo000 . encode ( 'utf-8' , 'ignore' ) ) , i111IiI1I , ooOooo000oOO , ooOoo0O , II11iiii1Ii , OooO0 , True , OooOoOo , oOooOOOoOo , OOOOoOoo0O0O0 )
     elif ( ooiIi1 == "true" and OoOOoOooooOOo == 'true' ) or III1I1Iii1iiI :
      if oOooOOOoOo :
       OooOoOo . append ( IiIIIiI1I1 + '&regexs=' + oOooOOOoOo )
      elif any ( x in IiIIIiI1I1 for x in oOOo ) and IiIIIiI1I1 . startswith ( 'http' ) :
       OooOoOo . append ( IiIIIiI1I1 + '&mode=19' )
      else :
       OooOoOo . append ( IiIIIiI1I1 )
     else :
      OooOoOo . append ( IiIIIiI1I1 )
      if 78 - 78: o00O0oo + I1Ii111 . O0oO - o00O0oo . ooOoO0o
    if len ( OooOoOo ) > 1 :
     if 30 - 30: oOo0O0Ooo + oO0o % ooOoO0o * o00O0oo / I1ii11iIi11i - I1Ii111
     O000OOOOOo ( '' , oO000Oo000 . encode ( 'utf-8' ) , i111IiI1I , ooOooo000oOO , ooOoo0O , II11iiii1Ii , OooO0 , True , OooOoOo , oOooOOOoOo , OOOOoOoo0O0O0 )
   else :
    if 64 - 64: oooo
    if dontLink :
     return oO000Oo000 , o00O0OoO [ 0 ] , oOooOOOoOo
    if iiIiI1i1 :
     if not oOooOOOoOo == None :
      OoO000 ( oO000Oo000 . encode ( 'utf-8' ) , ii1I1i1iiiI [ 0 ] . encode ( 'utf-8' ) , 11 , i111IiI1I , ooOooo000oOO , ooOoo0O , II11iiii1Ii , OooO0 , None , '!!update' , oOooOOOoOo , o00O0OoO [ 0 ] . encode ( 'utf-8' ) )
      if 21 - 21: I1ii11iIi11i . OoO0O00
     else :
      OoO000 ( oO000Oo000 . encode ( 'utf-8' ) , ii1I1i1iiiI [ 0 ] . encode ( 'utf-8' ) , 11 , i111IiI1I , ooOooo000oOO , ooOoo0O , II11iiii1Ii , OooO0 , None , 'source' , None , None )
      if 54 - 54: OoO0O00 % OoO0O00
    elif oO0O00oOOoooO :
     OoO000 ( oO000Oo000 . encode ( 'utf-8' ) , ii1I1i1iiiI [ 0 ] , 53 , i111IiI1I , fanart , ooOoo0O , II11iiii1Ii , OooO0 , None , 'source' )
    elif o00O0OoO [ 0 ] . find ( 'sublink' ) > 0 :
     OoO000 ( oO000Oo000 . encode ( 'utf-8' ) , o00O0OoO [ 0 ] , 25 , i111IiI1I , fanart , ooOoo0O , II11iiii1Ii , OooO0 , None , 'source' )
     if 86 - 86: O0OO0O0O % ooOoO0o * O0oO * oooo * oo * I1Ii111
    else :
     O000OOOOOo ( o00O0OoO [ 0 ] , oO000Oo000 . encode ( 'utf-8' , 'ignore' ) , i111IiI1I , ooOooo000oOO , ooOoo0O , II11iiii1Ii , OooO0 , True , None , oOooOOOoOo , OOOOoOoo0O0O0 )
     if 83 - 83: OOooOOo % OoO0O00 - OOooOOo + oO0o0ooO0 - O0OO0O0O
  except :
   o0oOo0Ooo0O ( 'There was a problem adding item - ' + oO000Oo000 . encode ( 'utf-8' , 'ignore' ) )
   if 52 - 52: I1ii11iIi11i * O0oO
def i11Iiii ( url , data = None ) :
 print 'getsoup' , url , data
 if url . startswith ( 'http://' ) or url . startswith ( 'https://' ) :
  data = i11IIIiIiIi ( url )
  if re . search ( "#EXTM3U" , data ) or 'm3u' in url :
   print 'found m3u data' , data
   return data
   if 27 - 27: Ii1I + OOooOOo - IiII + O0OO0O0O . ooOoO0o
 elif data == None :
  if xbmcvfs . exists ( url ) :
   if url . startswith ( "smb://" ) or url . startswith ( "nfs://" ) :
    iIi1i1iIi1iI = xbmcvfs . copy ( url , os . path . join ( i1I1Iiii1111 , 'temp' , 'sorce_temp.txt' ) )
    if iIi1i1iIi1iI :
     data = open ( os . path . join ( i1I1Iiii1111 , 'temp' , 'sorce_temp.txt' ) , "r" ) . read ( )
     xbmcvfs . delete ( os . path . join ( i1I1Iiii1111 , 'temp' , 'sorce_temp.txt' ) )
    else :
     o0oOo0Ooo0O ( "failed to copy from smb:" )
   else :
    data = open ( url , 'r' ) . read ( )
    if re . match ( "#EXTM3U" , data ) or 'm3u' in url :
     print 'found m3u data' , data
     return data
  else :
   o0oOo0Ooo0O ( "Soup Data not found!" )
   return
 return BeautifulSOAP ( data , convertEntities = BeautifulStoneSoup . XML_ENTITIES )
 if 26 - 26: II111iiii * oOo0O0Ooo + IiII
def i1Iii1i1I ( reg_item ) :
 try :
  oOooOOOoOo = { }
  for IiIIIiI1I1 in reg_item :
   oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] = { }
   oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'name' ] = IiIIIiI1I1 ( 'name' ) [ 0 ] . string
   if 24 - 24: oo0 % oooo + IiII / oo0
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'expres' ] = IiIIIiI1I1 ( 'expres' ) [ 0 ] . string
    if not oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'expres' ] :
     oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'expres' ] = ''
   except :
    o0oOo0Ooo0O ( "Regex: -- No Referer --" )
   oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'page' ] = IiIIIiI1I1 ( 'page' ) [ 0 ] . string
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'referer' ] = IiIIIiI1I1 ( 'referer' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- No Referer --" )
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'connection' ] = IiIIIiI1I1 ( 'connection' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- No connection --" )
    if 70 - 70: oO0o * O0OO0O0O . I1Ii111 + oOo0O0Ooo . oO0o0ooO0
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'notplayable' ] = IiIIIiI1I1 ( 'notplayable' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- No notplayable --" )
    if 14 - 14: oooo % oooo * oo0 - oO0o - I1Ii111
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'noredirect' ] = IiIIIiI1I1 ( 'noredirect' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- No noredirect --" )
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'origin' ] = IiIIIiI1I1 ( 'origin' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- No origin --" )
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'accept' ] = IiIIIiI1I1 ( 'accept' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- No accept --" )
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'includeheaders' ] = IiIIIiI1I1 ( 'includeheaders' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- No includeheaders --" )
    if 63 - 63: oO0o
    if 69 - 69: oooo . Ii1I % O0oO + oooo / O0OO0O0O / Ii1I
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'listrepeat' ] = IiIIIiI1I1 ( 'listrepeat' ) [ 0 ] . string
    if 61 - 61: IiII % IiII * I11i / I11i
   except :
    o0oOo0Ooo0O ( "Regex: -- No listrepeat --" )
    if 75 - 75: oO0o0ooO0 . O0oO
    if 50 - 50: OOooOOo
    if 60 - 60: O0oO * oooo * Ii1I * I1ii11iIi11i
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'proxy' ] = IiIIIiI1I1 ( 'proxy' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- No proxy --" )
    if 69 - 69: ooOoO0o * O0OO0O0O . oo0 / ooOoO0o . I11i
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'x-req' ] = IiIIIiI1I1 ( 'x-req' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- No x-req --" )
    if 63 - 63: I1Ii111 + I11i . OoO0O00 - oOo0O0Ooo
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'x-addr' ] = IiIIIiI1I1 ( 'x-addr' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- No x-addr --" )
    if 52 - 52: I11i % I1ii11iIi11i
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'x-forward' ] = IiIIIiI1I1 ( 'x-forward' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- No x-forward --" )
    if 64 - 64: O0OO0O0O % I1Ii111 % O0OO0O0O * oO0o . iII111i + oOo0O0Ooo
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'agent' ] = IiIIIiI1I1 ( 'agent' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- No User Agent --" )
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'post' ] = IiIIIiI1I1 ( 'post' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- Not a post" )
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'rawpost' ] = IiIIIiI1I1 ( 'rawpost' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- Not a rawpost" )
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'htmlunescape' ] = IiIIIiI1I1 ( 'htmlunescape' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- Not a htmlunescape" )
    if 75 - 75: I1Ii111 . II111iiii % I11i * I1Ii111 % II111iiii
    if 13 - 13: oO0o0ooO0 / oo0 % OoO0O00 % I1Ii111 . Ii1I
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'readcookieonly' ] = IiIIIiI1I1 ( 'readcookieonly' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- Not a readCookieOnly" )
    if 8 - 8: OOooOOo + I1ii11iIi11i - OoO0O00
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = IiIIIiI1I1 ( 'cookiejar' ) [ 0 ] . string
    if not oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] :
     oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = ''
   except :
    o0oOo0Ooo0O ( "Regex: -- Not a cookieJar" )
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'setcookie' ] = IiIIIiI1I1 ( 'setcookie' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- Not a setcookie" )
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'appendcookie' ] = IiIIIiI1I1 ( 'appendcookie' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- Not a appendcookie" )
    if 11 - 11: oo % oo0 - oo * OOooOOo
   try :
    oOooOOOoOo [ IiIIIiI1I1 ( 'name' ) [ 0 ] . string ] [ 'ignorecache' ] = IiIIIiI1I1 ( 'ignorecache' ) [ 0 ] . string
   except :
    o0oOo0Ooo0O ( "Regex: -- no ignorecache" )
    if 39 - 39: IIII
    if 86 - 86: I1Ii111 * oOo0O0Ooo + I1Ii111 + OoO0O00
    if 8 - 8: IIII - o00O0oo / O0oO
    if 96 - 96: OOooOOo
    if 29 - 29: Ii1I / oo . oOo0O0Ooo - OOooOOo - OOooOOo - ooOoO0o
  oOooOOOoOo = urllib . quote ( repr ( oOooOOOoOo ) )
  return oOooOOOoOo
  if 20 - 20: oo % oO0o . oOo0O0Ooo / oO0o0ooO0 * oo0 * IiII
 except :
  oOooOOOoOo = None
  o0oOo0Ooo0O ( 'regex Error: ' + oO000Oo000 . encode ( 'utf-8' , 'ignore' ) )
  if 85 - 85: I11i . OOooOOo / O0oO . O0OO0O0O % IIII
def OO0ooo0oOO ( url ) :
 try :
  for IiIIIiI1I1 in range ( 1 , 51 ) :
   oo000ii = OoO ( url )
   if "EXT-X-STREAM-INF" in oo000ii : return url
   if not "EXTM3U" in oo000ii : return
   xbmc . sleep ( 2000 )
  return
 except :
  return
  if 41 - 41: oo * OoO0O00 / II111iiii . IiII
def O0iII1 ( regexs , url , cookieJar = None , forCookieJarOnly = False , recursiveCall = False , cachedPages = { } , rawPost = False , cookie_jar_file = None ) :
 if not recursiveCall :
  regexs = eval ( urllib . unquote ( regexs ) )
  if 27 - 27: oO0o . I1Ii111 + OOooOOo / oooo % o00O0oo . O0oO
  if 14 - 14: iII111i + Ii1I - o00O0oo / O0OO0O0O . IIII
 i1iiIiI1Ii1i = re . compile ( '\$doregex\[([^\]]*)\]' ) . findall ( url )
 if 22 - 22: oO0o0ooO0 / oo0
 oOOoo = True
 for iII1111III1I in i1iiIiI1Ii1i :
  if iII1111III1I in regexs :
   if 39 - 39: oo / oO0o0ooO0
   oO000oOo00o0o = regexs [ iII1111III1I ]
   if 85 - 85: o00O0oo + II111iiii * o00O0oo - IIII % oo0
   OOo00OoO = False
   if 'cookiejar' in oO000oOo00o0o :
    if 10 - 10: I11i / oo0
    OOo00OoO = oO000oOo00o0o [ 'cookiejar' ]
    if '$doregex' in OOo00OoO :
     cookieJar = O0iII1 ( regexs , oO000oOo00o0o [ 'cookiejar' ] , cookieJar , True , True , cachedPages )
     if 92 - 92: I1Ii111 . IIII
     OOo00OoO = True
    else :
     OOo00OoO = True
     if 85 - 85: Ii1I . IIII
   if OOo00OoO :
    if cookieJar == None :
     if 78 - 78: O0oO * IIII + oooo + oooo / IIII . ooOoO0o
     cookie_jar_file = None
     if 'open[' in oO000oOo00o0o [ 'cookiejar' ] :
      cookie_jar_file = oO000oOo00o0o [ 'cookiejar' ] . split ( 'open[' ) [ 1 ] . split ( ']' ) [ 0 ]
      if 97 - 97: O0oO / IIII % oo % Ii1I
      if 18 - 18: oooo % I1Ii111
     cookieJar = O00oO0 ( cookie_jar_file )
     if 97 - 97: IIII - oooo
     if cookie_jar_file :
      oo0o0O0Oooooo ( cookieJar , cookie_jar_file )
      if 1 - 1: O0oO % OOooOOo * I1ii11iIi11i
      if 55 - 55: OOooOOo
      if 87 - 87: II111iiii % o00O0oo . oOo0O0Ooo / O0oO
    elif 'save[' in oO000oOo00o0o [ 'cookiejar' ] :
     cookie_jar_file = oO000oOo00o0o [ 'cookiejar' ] . split ( 'save[' ) [ 1 ] . split ( ']' ) [ 0 ]
     i1I1iI = os . path . join ( i1I1Iiii1111 , cookie_jar_file )
     if 62 - 62: IIII . oO0o0ooO0 . II111iiii
     oo0o0O0Oooooo ( cookieJar , cookie_jar_file )
   if oO000oOo00o0o [ 'page' ] and '$doregex' in oO000oOo00o0o [ 'page' ] :
    i111 = O0iII1 ( regexs , oO000oOo00o0o [ 'page' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if len ( i111 ) == 0 :
     i111 = 'http://regexfailed'
    oO000oOo00o0o [ 'page' ] = i111
    if 27 - 27: oo0 / Ii1I
   if 'setcookie' in oO000oOo00o0o and oO000oOo00o0o [ 'setcookie' ] and '$doregex' in oO000oOo00o0o [ 'setcookie' ] :
    oO000oOo00o0o [ 'setcookie' ] = O0iII1 ( regexs , oO000oOo00o0o [ 'setcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
   if 'appendcookie' in oO000oOo00o0o and oO000oOo00o0o [ 'appendcookie' ] and '$doregex' in oO000oOo00o0o [ 'appendcookie' ] :
    oO000oOo00o0o [ 'appendcookie' ] = O0iII1 ( regexs , oO000oOo00o0o [ 'appendcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 84 - 84: I1ii11iIi11i
    if 43 - 43: iII111i - II111iiii
   if 'post' in oO000oOo00o0o and '$doregex' in oO000oOo00o0o [ 'post' ] :
    oO000oOo00o0o [ 'post' ] = O0iII1 ( regexs , oO000oOo00o0o [ 'post' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 3 - 3: O0OO0O0O / o00O0oo
    if 31 - 31: IiII + I11i . II111iiii
   if 'rawpost' in oO000oOo00o0o and '$doregex' in oO000oOo00o0o [ 'rawpost' ] :
    oO000oOo00o0o [ 'rawpost' ] = O0iII1 ( regexs , oO000oOo00o0o [ 'rawpost' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages , rawPost = True )
    if 89 - 89: OoO0O00 + oo + OoO0O00
    if 7 - 7: O0OO0O0O % I11i + Ii1I * o00O0oo - o00O0oo
   if 'rawpost' in oO000oOo00o0o and '$epoctime$' in oO000oOo00o0o [ 'rawpost' ] :
    oO000oOo00o0o [ 'rawpost' ] = oO000oOo00o0o [ 'rawpost' ] . replace ( '$epoctime$' , II1Ii11I111I ( ) )
    if 13 - 13: O0oO / o00O0oo * oO0o . oO0o * O0oO
   if 'rawpost' in oO000oOo00o0o and '$epoctime2$' in oO000oOo00o0o [ 'rawpost' ] :
    oO000oOo00o0o [ 'rawpost' ] = oO000oOo00o0o [ 'rawpost' ] . replace ( '$epoctime2$' , O00oO ( ) )
    if 40 - 40: OOooOOo / oO0o0ooO0
    if 79 - 79: oO0o - oooo + ooOoO0o - IIII
   OoOiIIiii = ''
   if oO000oOo00o0o [ 'page' ] and oO000oOo00o0o [ 'page' ] in cachedPages and not 'ignorecache' in oO000oOo00o0o and forCookieJarOnly == False :
    if 61 - 61: oO0o0ooO0 . oo / IIII % oo0 * o00O0oo
    OoOiIIiii = cachedPages [ oO000oOo00o0o [ 'page' ] ]
   else :
    if oO000oOo00o0o [ 'page' ] and not oO000oOo00o0o [ 'page' ] == '' and oO000oOo00o0o [ 'page' ] . startswith ( 'http' ) :
     if '$epoctime$' in oO000oOo00o0o [ 'page' ] :
      oO000oOo00o0o [ 'page' ] = oO000oOo00o0o [ 'page' ] . replace ( '$epoctime$' , II1Ii11I111I ( ) )
     if '$epoctime2$' in oO000oOo00o0o [ 'page' ] :
      oO000oOo00o0o [ 'page' ] = oO000oOo00o0o [ 'page' ] . replace ( '$epoctime2$' , O00oO ( ) )
      if 31 - 31: IiII + O0OO0O0O
      if 87 - 87: O0oO
     IIIii = oO000oOo00o0o [ 'page' ] . split ( '|' )
     O00OooOo00o = IIIii [ 0 ]
     IiI11i1IIiiI = None
     if len ( IIIii ) > 1 :
      IiI11i1IIiiI = IIIii [ 1 ]
      if 60 - 60: Ii1I * oOo0O0Ooo
      if 17 - 17: IiII % I1ii11iIi11i / Ii1I . oO0o0ooO0 * IiII - OoO0O00
      if 41 - 41: ooOoO0o
      if 77 - 77: IIII
      if 65 - 65: OoO0O00 . oOo0O0Ooo % iII111i * oO0o
      if 38 - 38: OOooOOo / o00O0oo % I1ii11iIi11i
      if 11 - 11: o00O0oo - iII111i + OoO0O00 - oooo
      if 7 - 7: oO0o0ooO0 - I1Ii111 / OoO0O00 * ooOoO0o . o00O0oo * o00O0oo
      if 61 - 61: I1Ii111 % O0oO - oO0o / I1ii11iIi11i
      if 4 - 4: II111iiii - oo % ooOoO0o - IiII * I11i
     Ooooo00o0OoO = urllib2 . ProxyHandler ( urllib2 . getproxies ( ) )
     if 75 - 75: oOo0O0Ooo % OoO0O00
     if 30 - 30: oO0o0ooO0 + IIII - oO0o0ooO0 . oO0o0ooO0 - OoO0O00 + O0OO0O0O
     if 86 - 86: oo
     IIi11IIiIii1 = urllib2 . Request ( O00OooOo00o )
     if 'proxy' in oO000oOo00o0o :
      I1iIII1 = oO000oOo00o0o [ 'proxy' ]
      if 39 - 39: II111iiii
      if 38 - 38: oOo0O0Ooo
      if O00OooOo00o [ : 5 ] == "https" :
       oOo0OoOOo0 = urllib2 . ProxyHandler ( { 'https' : I1iIII1 } )
       if 30 - 30: Ii1I % oOo0O0Ooo
      else :
       oOo0OoOOo0 = urllib2 . ProxyHandler ( { 'http' : I1iIII1 } )
       if 89 - 89: IIII + II111iiii + IIII * oo + oooo % I1Ii111
      oOo0oO = urllib2 . build_opener ( oOo0OoOOo0 )
      urllib2 . install_opener ( oOo0oO )
      if 5 - 5: IiII - IiII . I1ii11iIi11i + OOooOOo - IiII . iII111i
      if 31 - 31: OoO0O00 - oooo - oooo % I1Ii111
     IIi11IIiIii1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
     I1iIII1 = None
     if 12 - 12: oooo
     if 'referer' in oO000oOo00o0o :
      IIi11IIiIii1 . add_header ( 'Referer' , oO000oOo00o0o [ 'referer' ] )
     if 'accept' in oO000oOo00o0o :
      IIi11IIiIii1 . add_header ( 'Accept' , oO000oOo00o0o [ 'accept' ] )
     if 'agent' in oO000oOo00o0o :
      IIi11IIiIii1 . add_header ( 'User-agent' , oO000oOo00o0o [ 'agent' ] )
     if 'x-req' in oO000oOo00o0o :
      IIi11IIiIii1 . add_header ( 'X-Requested-With' , oO000oOo00o0o [ 'x-req' ] )
     if 'x-addr' in oO000oOo00o0o :
      IIi11IIiIii1 . add_header ( 'x-addr' , oO000oOo00o0o [ 'x-addr' ] )
     if 'x-forward' in oO000oOo00o0o :
      IIi11IIiIii1 . add_header ( 'X-Forwarded-For' , oO000oOo00o0o [ 'x-forward' ] )
     if 'setcookie' in oO000oOo00o0o :
      if 20 - 20: I11i / oo
      IIi11IIiIii1 . add_header ( 'Cookie' , oO000oOo00o0o [ 'setcookie' ] )
     if 'appendcookie' in oO000oOo00o0o :
      if 71 - 71: OOooOOo . oo
      o0OooO0ooo0o = oO000oOo00o0o [ 'appendcookie' ]
      o0OooO0ooo0o = o0OooO0ooo0o . split ( ';' )
      for iii1 in o0OooO0ooo0o :
       I1i , OOOO = iii1 . split ( '=' )
       ooO0oO00O0o , I1i = I1i . split ( ':' )
       ooOO00oOOo000 = cookielib . Cookie ( version = 0 , name = I1i , value = OOOO , port = None , port_specified = False , domain = ooO0oO00O0o , domain_specified = False , domain_initial_dot = False , path = '/' , path_specified = True , secure = False , expires = None , discard = True , comment = None , comment_url = None , rest = { 'HttpOnly' : None } , rfc2109 = False )
       cookieJar . set_cookie ( ooOO00oOOo000 )
     if 'origin' in oO000oOo00o0o :
      IIi11IIiIii1 . add_header ( 'Origin' , oO000oOo00o0o [ 'origin' ] )
     if IiI11i1IIiiI :
      IiI11i1IIiiI = IiI11i1IIiiI . split ( '&' )
      for iii1 in IiI11i1IIiiI :
       if iii1 . split ( '=' ) == 2 :
        I1i , OOOO = iii1 . split ( '=' )
       else :
        IIi = iii1 . split ( '=' )
        I1i = IIi [ 0 ]
        OOOO = '=' . join ( IIi [ 1 : ] )
        if 27 - 27: IiII % ooOoO0o
       IIi11IIiIii1 . add_header ( I1i , OOOO )
       if 58 - 58: IiII * I11i + O0OO0O0O % IiII
     if not cookieJar == None :
      if 25 - 25: I1ii11iIi11i % Ii1I * O0oO
      I11oo0ooOO = urllib2 . HTTPCookieProcessor ( cookieJar )
      oOo0oO = urllib2 . build_opener ( I11oo0ooOO , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
      oOo0oO = urllib2 . install_opener ( oOo0oO )
      if 24 - 24: oO0o % oO0o * oooo
      if 50 - 50: oO0o . oo0 - iII111i . iII111i
      if 'noredirect' in oO000oOo00o0o :
       oOo0oO = urllib2 . build_opener ( I11oo0ooOO , iIIii1IIi , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
       oOo0oO = urllib2 . install_opener ( oOo0oO )
     elif 'noredirect' in oO000oOo00o0o :
      oOo0oO = urllib2 . build_opener ( iIIii1IIi , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
      oOo0oO = urllib2 . install_opener ( oOo0oO )
      if 31 - 31: IiII / I1ii11iIi11i * oo . OOooOOo
      if 57 - 57: IiII + oooo % oo % oOo0O0Ooo
     if 'connection' in oO000oOo00o0o :
      if 83 - 83: I11i / oo0 % oooo . I1Ii111 % iII111i . II111iiii
      from keepalive import HTTPHandler
      o00oO00 = HTTPHandler ( )
      oOo0oO = urllib2 . build_opener ( o00oO00 )
      urllib2 . install_opener ( oOo0oO )
      if 59 - 59: IiII + oooo * I11i + IIII . o00O0oo
      if 49 - 49: II111iiii * I1Ii111 - I1ii11iIi11i . iII111i
      if 89 - 89: O0oO + ooOoO0o * O0oO / O0oO
     i11i11 = None
     if 72 - 72: oo - OoO0O00 - IiII + IiII * I11i * IiII
     if 'post' in oO000oOo00o0o :
      iII1I1 = oO000oOo00o0o [ 'post' ]
      if 85 - 85: o00O0oo * I11i
      if 3 - 3: IiII
      if 20 - 20: OoO0O00 . o00O0oo / OoO0O00 % oo0 % o00O0oo
      if 11 - 11: oO0o0ooO0 % Ii1I % ooOoO0o / OoO0O00 % IIII - I1ii11iIi11i
      OOooO = iII1I1 . split ( ',' ) ;
      i11i11 = { }
      for O00O0OO00oo in OOooO :
       I1i = O00O0OO00oo . split ( ':' ) [ 0 ] ;
       OOOO = O00O0OO00oo . split ( ':' ) [ 1 ] ;
       i11i11 [ I1i ] = OOOO
      i11i11 = urllib . urlencode ( i11i11 )
      if 69 - 69: I11i / I1ii11iIi11i
     if 'rawpost' in oO000oOo00o0o :
      i11i11 = oO000oOo00o0o [ 'rawpost' ]
      if 43 - 43: Ii1I . oOo0O0Ooo / II111iiii % II111iiii
      if 33 - 33: IIII
      if 62 - 62: Ii1I + ooOoO0o + oo / II111iiii
      if 7 - 7: I11i + oo . oOo0O0Ooo / I1ii11iIi11i
     OoOiIIiii = ''
     try :
      if 22 - 22: O0oO - O0oO % IiII . IIII + iII111i
      if i11i11 :
       Oo00OOo00O = urllib2 . urlopen ( IIi11IIiIii1 , i11i11 )
      else :
       Oo00OOo00O = urllib2 . urlopen ( IIi11IIiIii1 )
      if Oo00OOo00O . info ( ) . get ( 'Content-Encoding' ) == 'gzip' :
       from StringIO import StringIO
       import gzip
       o0Ii1Iii111IiI1 = StringIO ( Oo00OOo00O . read ( ) )
       O00oOooo0 = gzip . GzipFile ( fileobj = o0Ii1Iii111IiI1 )
       OoOiIIiii = O00oOooo0 . read ( )
      else :
       OoOiIIiii = Oo00OOo00O . read ( )
       if 56 - 56: OoO0O00 / iII111i + oo0 + IiII
       if 54 - 54: ooOoO0o - I1Ii111 - IIII . oooo
       if 79 - 79: ooOoO0o . oO0o
      if 'proxy' in oO000oOo00o0o and not Ooooo00o0OoO is None :
       urllib2 . install_opener ( urllib2 . build_opener ( Ooooo00o0OoO ) )
       if 40 - 40: I11i + I1ii11iIi11i . I11i % O0oO
      OoOiIIiii = I11I1IIiiII1 ( OoOiIIiii )
      if 31 - 31: oOo0O0Ooo * iII111i + II111iiii - o00O0oo / II111iiii
      if 19 - 19: oO0o0ooO0 * O0oO * I11i + O0OO0O0O / O0OO0O0O
      if 'includeheaders' in oO000oOo00o0o :
       if 73 - 73: oooo / oooo - iII111i
       OoOiIIiii += '$$HEADERS_START$$:'
       for o00O in Oo00OOo00O . headers :
        OoOiIIiii += o00O + ':' + Oo00OOo00O . headers . get ( o00O ) + '\n'
       OoOiIIiii += '$$HEADERS_END$$:'
       if 91 - 91: iII111i + oOo0O0Ooo
      o0oOo0Ooo0O ( OoOiIIiii )
      o0oOo0Ooo0O ( cookieJar )
      if 59 - 59: oOo0O0Ooo + oo0 + oo / I1Ii111
      Oo00OOo00O . close ( )
     except :
      pass
     cachedPages [ oO000oOo00o0o [ 'page' ] ] = OoOiIIiii
     if 44 - 44: I1Ii111 . OOooOOo * oOo0O0Ooo + II111iiii - o00O0oo - oO0o0ooO0
     if 15 - 15: oO0o0ooO0 / O0OO0O0O . I11i . oo0
     if 59 - 59: IIII - I11i - O0oO
     if forCookieJarOnly :
      return cookieJar
    elif oO000oOo00o0o [ 'page' ] and not oO000oOo00o0o [ 'page' ] . startswith ( 'http' ) :
     if oO000oOo00o0o [ 'page' ] . startswith ( '$pyFunction:' ) :
      Ii11iI = oO00OoOO ( oO000oOo00o0o [ 'page' ] . split ( '$pyFunction:' ) [ 1 ] , '' , cookieJar , oO000oOo00o0o )
      if forCookieJarOnly :
       return cookieJar
      OoOiIIiii = Ii11iI
      OoOiIIiii = I11I1IIiiII1 ( OoOiIIiii )
     else :
      OoOiIIiii = oO000oOo00o0o [ 'page' ]
   if '$pyFunction:playmedia(' in oO000oOo00o0o [ 'expres' ] or 'ActivateWindow' in oO000oOo00o0o [ 'expres' ] or '$PLAYERPROXY$=' in url or any ( x in url for x in O0 ) :
    oOOoo = False
   if '$doregex' in oO000oOo00o0o [ 'expres' ] :
    oO000oOo00o0o [ 'expres' ] = O0iII1 ( regexs , oO000oOo00o0o [ 'expres' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 18 - 18: O0oO - OOooOOo % oo + O0OO0O0O + oo0 + oo
   if not oO000oOo00o0o [ 'expres' ] == '' :
    if 91 - 91: OOooOOo + O0oO . oOo0O0Ooo
    if '$LiveStreamCaptcha' in oO000oOo00o0o [ 'expres' ] :
     Ii11iI = O0oOoOOO0OO ( oO000oOo00o0o , OoOiIIiii , cookieJar )
     if 91 - 91: oO0o0ooO0 + OOooOOo + I11i - oooo
     url = url . replace ( "$doregex[" + iII1111III1I + "]" , Ii11iI )
     if 17 - 17: iII111i
    elif oO000oOo00o0o [ 'expres' ] . startswith ( '$pyFunction:' ) or '#$pyFunction' in oO000oOo00o0o [ 'expres' ] :
     if 22 - 22: I1Ii111 + oooo
     Ii11iI = ''
     if oO000oOo00o0o [ 'expres' ] . startswith ( '$pyFunction:' ) :
      Ii11iI = oO00OoOO ( oO000oOo00o0o [ 'expres' ] . split ( '$pyFunction:' ) [ 1 ] , OoOiIIiii , cookieJar , oO000oOo00o0o )
     else :
      Ii11iI = IIIii1iiIi ( oO000oOo00o0o [ 'expres' ] , OoOiIIiii , cookieJar , oO000oOo00o0o )
     if 'ActivateWindow' in oO000oOo00o0o [ 'expres' ] : return
     if forCookieJarOnly :
      return cookieJar
     if 'listrepeat' in oO000oOo00o0o :
      oooo0OOo = oO000oOo00o0o [ 'listrepeat' ]
      if 72 - 72: O0OO0O0O / O0oO + II111iiii * o00O0oo
      if 61 - 61: II111iiii % OoO0O00 - oOo0O0Ooo % Ii1I + oo
      return oooo0OOo , eval ( Ii11iI ) , oO000oOo00o0o , regexs , cookieJar
      if 39 - 39: oo
      if 86 - 86: oooo + OOooOOo . oo0 - ooOoO0o
      if 51 - 51: OOooOOo
     try :
      url = url . replace ( u"$doregex[" + iII1111III1I + "]" , Ii11iI )
     except : url = url . replace ( "$doregex[" + iII1111III1I + "]" , Ii11iI . decode ( "utf-8" ) )
    else :
     if 'listrepeat' in oO000oOo00o0o :
      oooo0OOo = oO000oOo00o0o [ 'listrepeat' ]
      if 14 - 14: oO0o0ooO0 % iII111i % I1ii11iIi11i - oo0
      if 53 - 53: ooOoO0o % I1ii11iIi11i
      if 59 - 59: IiII % oooo . oo + OoO0O00 * oO0o0ooO0
      if 41 - 41: ooOoO0o % Ii1I
      i1iIiIi1I = re . findall ( oO000oOo00o0o [ 'expres' ] , OoOiIIiii )
      if 37 - 37: ooOoO0o % oO0o
      return oooo0OOo , i1iIiIi1I , oO000oOo00o0o , regexs , cookieJar
      if 79 - 79: Ii1I + oOo0O0Ooo / oOo0O0Ooo
     Ii11iI = ''
     if not OoOiIIiii == '' :
      if 71 - 71: IiII * oO0o % II111iiii % oO0o / oOo0O0Ooo
      Oo0ooo0Ooo = re . compile ( oO000oOo00o0o [ 'expres' ] ) . search ( OoOiIIiii )
      try :
       Ii11iI = Oo0ooo0Ooo . group ( 1 ) . strip ( )
      except : traceback . print_exc ( )
     elif oO000oOo00o0o [ 'page' ] == '' or oO000oOo00o0o [ 'page' ] == None :
      Ii11iI = oO000oOo00o0o [ 'expres' ]
      if 9 - 9: I1ii11iIi11i
     if rawPost :
      if 99 - 99: I1Ii111 - IIII - iII111i % oO0o
      Ii11iI = urllib . quote_plus ( Ii11iI )
     if 'htmlunescape' in oO000oOo00o0o :
      if 21 - 21: OoO0O00 % Ii1I . oo - II111iiii
      import HTMLParser
      Ii11iI = HTMLParser . HTMLParser ( ) . unescape ( Ii11iI )
     try :
      url = url . replace ( "$doregex[" + iII1111III1I + "]" , Ii11iI )
     except : url = url . replace ( "$doregex[" + iII1111III1I + "]" , Ii11iI . decode ( "utf-8" ) )
     if 4 - 4: II111iiii . O0oO
     if 78 - 78: Ii1I + I1Ii111 - O0OO0O0O
   else :
    url = url . replace ( "$doregex[" + iII1111III1I + "]" , '' )
 if '$epoctime$' in url :
  url = url . replace ( '$epoctime$' , II1Ii11I111I ( ) )
 if '$epoctime2$' in url :
  url = url . replace ( '$epoctime2$' , O00oO ( ) )
  if 10 - 10: IIII % oOo0O0Ooo
 if '$GUID$' in url :
  import uuid
  url = url . replace ( '$GUID$' , str ( uuid . uuid1 ( ) ) . upper ( ) )
 if '$get_cookies$' in url :
  url = url . replace ( '$get_cookies$' , oo0OoOooo ( cookieJar ) )
  if 95 - 95: oO0o0ooO0 * Ii1I % O0oO % ooOoO0o - ooOoO0o
 if recursiveCall : return url
 if 97 - 97: Ii1I + oooo . O0OO0O0O
 if url == "" :
  return
 else :
  return url , oOOoo
  if 64 - 64: oo % O0oO / oo0 - oo % IiII . o00O0oo
def II1i111 ( t ) :
 import hashlib
 iii1 = hashlib . md5 ( )
 iii1 . update ( t )
 return iii1 . hexdigest ( )
 if 50 - 50: oO0o0ooO0 % oo
def iii11II1I ( encrypted ) :
 iI111I11i = ""
 if 23 - 23: ooOoO0o . I11i + I1ii11iIi11i - IiII
 if 18 - 18: OOooOOo % oo0 % Ii1I / iII111i / I11i / oo
 if 48 - 48: OOooOOo + I1Ii111 / oO0o0ooO0 + OoO0O00
 if 18 - 18: Ii1I
 if 23 - 23: OoO0O00
def ii1i1i ( media_url ) :
 try :
  import CustomPlayer
  II11iIII1i1I = CustomPlayer . MyXBMCPlayer ( )
  oOO0oo = xbmcgui . ListItem ( label = str ( oO000Oo000 ) , iconImage = "DefaultVideo.png" , thumbnailImage = xbmc . getInfoImage ( "ListItem.Thumb" ) , path = media_url )
  II11iIII1i1I . play ( media_url , oOO0oo )
  xbmc . sleep ( 1000 )
  while II11iIII1i1I . is_active :
   xbmc . sleep ( 200 )
 except :
  traceback . print_exc ( )
 return ''
 if 13 - 13: II111iiii * iII111i - ooOoO0o / IiII + I1Ii111 + oO0o0ooO0
def oo0oOo ( url , data = None ) :
 print 'myRequest' , url , data
 data = i11IIIiIiIi ( url )
 import gzip , binascii
 from StringIO import StringIO
 if 'afd+' [ : : - 1 ] in data :
  data = data . split ( 'afd+' [ : : - 1 ] )
  o0Ii1Iii111IiI1 = StringIO ( binascii . unhexlify ( data [ 0 ] ) )
  O00oOooo0 = gzip . GzipFile ( fileobj = o0Ii1Iii111IiI1 )
  data = O00oOooo0 . read ( )
 if re . search ( "#EXTM3U" , data ) or 'm3u' in url :
  if 39 - 39: oooo - II111iiii
  return data
 return BeautifulSOAP ( data , convertEntities = BeautifulStoneSoup . XML_ENTITIES )
 if 81 - 81: Ii1I - O0OO0O0O * II111iiii
def i11IIIiIiIi ( url , headers = None ) :
 try :
  if headers is None :
   headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' }
   if 23 - 23: OoO0O00 / iII111i
  if '|' in url :
   url , IiI11i1IIiiI = url . split ( '|' )
   IiI11i1IIiiI = IiI11i1IIiiI . split ( '&' )
   if 28 - 28: I1ii11iIi11i * O0oO - oO0o
   for iii1 in IiI11i1IIiiI :
    if len ( iii1 . split ( '=' ) ) == 2 :
     I1i , OOOO = iii1 . split ( '=' )
    else :
     IIi = iii1 . split ( '=' )
     I1i = IIi [ 0 ]
     OOOO = '=' . join ( IIi [ 1 : ] )
     if 19 - 19: I1Ii111
    print I1i , OOOO
    headers [ I1i ] = OOOO
    if 67 - 67: O0OO0O0O % oooo / oO0o0ooO0 . oo0 - ooOoO0o + O0OO0O0O
  IIi11IIiIii1 = urllib2 . Request ( url , None , headers )
  Oo00OOo00O = urllib2 . urlopen ( IIi11IIiIii1 )
  iI1 = Oo00OOo00O . read ( )
  Oo00OOo00O . close ( )
  return iI1
 except urllib2 . URLError , i1iiiIi1i :
  o0oOo0Ooo0O ( 'URL: ' + url )
  if hasattr ( i1iiiIi1i , 'code' ) :
   o0oOo0Ooo0O ( 'ERRO - CODIGO - %s.' % i1iiiIi1i . code )
   xbmc . executebuiltin ( "XBMC.Notification(" + II1iI + ",ERRO - CODIGO - " + str ( i1iiiIi1i . code ) + ",10000," + oOo0oooo00o + ")" )
  elif hasattr ( i1iiiIi1i , 'reason' ) :
   o0oOo0Ooo0O ( 'ERRO DE SERVIDOR.' )
   o0oOo0Ooo0O ( 'Reason: %s' % i1iiiIi1i . reason )
   xbmc . executebuiltin ( "XBMC.Notification(" + II1iI + ",ERRO DE SERVIDOR. - " + str ( i1iiiIi1i . reason ) + ",10000," + oOo0oooo00o + ")" )
   if 67 - 67: OOooOOo / I11i * oO0o / IiII * Ii1I / iII111i
def OoO000 ( name , url , mode , iconimage , fanart , description , genre , date , credits , showcontext = False , regexs = None , reg_url = None , allinfo = { } ) :
 if 64 - 64: iII111i - oOo0O0Ooo / o00O0oo - oO0o
 ii11I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 OOOoo0OO = True
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 oOO00O = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if len ( allinfo ) < 1 :
  oOO00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date , "credits" : credits } )
 else :
  oOO00O . setInfo ( type = "Video" , infoLabels = allinfo )
 oOO00O . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  i1IiIiiiIIIIi = [ ]
  oo0O0 = i1I1Ii1iI1ii . getSetting ( 'parentalblocked' )
  oo0O0 = oo0O0 == "true"
  ooOo00 = i1I1Ii1iI1ii . getSetting ( 'parentalblockedpin' )
  if 81 - 81: I1Ii111 / oO0o % II111iiii * iII111i / iII111i
  if len ( ooOo00 ) > 0 :
   if oo0O0 :
    i1IiIiiiIIIIi . append ( ( 'Disable Parental Block' , 'XBMC.RunPlugin(%s?mode=55&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
   else :
    i1IiIiiiIIIIi . append ( ( 'Enable Parental Block' , 'XBMC.RunPlugin(%s?mode=56&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
    if 28 - 28: oo0 / I11i . oooo / OoO0O00
  if showcontext == 'source' :
   if 72 - 72: II111iiii / oOo0O0Ooo + ooOoO0o / OOooOOo * ooOoO0o
   if name in str ( o00ooooO0oO ) :
    i1IiIiiiIIIIi . append ( ( 'Remover lista [COLOR red][B]Flecha[/B][/COLOR] [COLOR black][B]Negra[/B][/COLOR]' , 'XBMC.RunPlugin(%s?mode=8&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
    if 34 - 34: O0OO0O0O * O0OO0O0O % II111iiii + o00O0oo * oooo % ooOoO0o
    if 25 - 25: I1Ii111 + OOooOOo . I11i % OOooOOo * IiII
  elif showcontext == 'download' :
   i1IiIiiiIIIIi . append ( ( 'Download' , 'XBMC.RunPlugin(%s?url=%s&mode=9&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  oOO00O . addContextMenuItems ( i1IiIiiiIIIIi )
 OOOoo0OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii11I , listitem = oOO00O , isFolder = True )
 return OOOoo0OO
 if 32 - 32: oo0 - IIII
def oo00ooOoo ( params ) :
 iI1 = json . dumps ( params )
 iii1IIIiiiI = xbmc . executeJSONRPC ( iI1 )
 if 94 - 94: O0OO0O0O - I1Ii111 - oooo % O0oO / ooOoO0o % o00O0oo
 try :
  Oo00OOo00O = json . loads ( iii1IIIiiiI )
 except UnicodeDecodeError :
  Oo00OOo00O = json . loads ( iii1IIIiiiI . decode ( 'utf-8' , 'ignore' ) )
  if 44 - 44: I1ii11iIi11i % oooo
 try :
  if 'result' in Oo00OOo00O :
   return Oo00OOo00O [ 'result' ]
  return None
 except KeyError :
  logger . warn ( "[%s] %s" % ( params [ 'method' ] , Oo00OOo00O [ 'error' ] [ 'message' ] ) )
  return None
  if 90 - 90: OoO0O00 + II111iiii % II111iiii
def I11Ii ( proxysettings = None ) :
 if 16 - 16: I1ii11iIi11i / oo0
 if proxysettings == None :
  if 64 - 64: oo0 / ooOoO0o * oo
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.usehttpproxy", "value":false}, "id":1}' )
 else :
  if 73 - 73: I1ii11iIi11i - OOooOOo - iII111i - oOo0O0Ooo
  oo0o0oOo = proxysettings . split ( ':' )
  OO0oOOo0o = oo0o0oOo [ 0 ]
  I1 = oo0o0oOo [ 1 ]
  III11iiii11i1 = oo0o0oOo [ 2 ]
  ooOo0OoO = None
  i1iiIIi1I = None
  if 36 - 36: oOo0O0Ooo * I1ii11iIi11i
  if len ( oo0o0oOo ) > 3 and '@' in oo0o0oOo [ 3 ] :
   ooOo0OoO = oo0o0oOo [ 3 ] . split ( '@' ) [ 0 ]
   i1iiIIi1I = oo0o0oOo [ 3 ] . split ( '@' ) [ 1 ]
   if 77 - 77: iII111i % oo - ooOoO0o
   if 93 - 93: oO0o * I1ii11iIi11i
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.usehttpproxy", "value":true}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxytype", "value":' + str ( III11iiii11i1 ) + '}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyserver", "value":"' + str ( OO0oOOo0o ) + '"}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyport", "value":' + str ( I1 ) + '}, "id":1}' )
  if 73 - 73: I11i - oOo0O0Ooo * oo / oo0 * IiII % OoO0O00
  if 56 - 56: II111iiii * I1ii11iIi11i . I1ii11iIi11i . Ii1I
  if not ooOo0OoO == None :
   xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyusername", "value":"' + str ( ooOo0OoO ) + '"}, "id":1}' )
   xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxypassword", "value":"' + str ( i1iiIIi1I ) + '"}, "id":1}' )
   if 24 - 24: I1ii11iIi11i . I1Ii111 * ooOoO0o % o00O0oo / IiII
   if 58 - 58: oOo0O0Ooo - Ii1I % O0OO0O0O . oOo0O0Ooo % oO0o % oO0o0ooO0
def oOo0OooOo ( ) :
 o0iIiiIiiIi = oo00ooOoo ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.usehttpproxy" } , 'id' : 1 } ) [ 'value' ]
 if 40 - 40: I11i
 III11iiii11i1 = oo00ooOoo ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxytype" } , 'id' : 1 } ) [ 'value' ]
 if 78 - 78: oooo
 if o0iIiiIiiIi :
  OO0oOOo0o = oo00ooOoo ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyserver" } , 'id' : 1 } ) [ 'value' ]
  I1 = unicode ( oo00ooOoo ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyport" } , 'id' : 1 } ) [ 'value' ] )
  ooOo0OoO = oo00ooOoo ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyusername" } , 'id' : 1 } ) [ 'value' ]
  i1iiIIi1I = oo00ooOoo ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxypassword" } , 'id' : 1 } ) [ 'value' ]
  if 56 - 56: II111iiii - I1Ii111 - oo
  if ooOo0OoO and i1iiIIi1I and OO0oOOo0o and I1 :
   return OO0oOOo0o + ':' + str ( I1 ) + ':' + str ( III11iiii11i1 ) + ':' + ooOo0OoO + '@' + i1iiIIi1I
  elif OO0oOOo0o and I1 :
   return OO0oOOo0o + ':' + str ( I1 ) + ':' + str ( III11iiii11i1 )
 else :
  return None
  if 8 - 8: IIII / IiII . oOo0O0Ooo + Ii1I / oo0
def I1Iii1iI1 ( media_url , name , iconImage , proxyip , port , proxyuser = None , proxypass = None ) :
 if 86 - 86: O0OO0O0O
 O0o0oOooOoOo = xbmcgui . DialogProgress ( )
 O0o0oOooOoOo . create ( 'Progress' , 'Playing with custom proxy' )
 O0o0oOooOoOo . update ( 10 , "" , "setting proxy.." , "" )
 I1iOo = False
 IiIiIi1I1 = ''
 if 2 - 2: oo - O0oO + oOo0O0Ooo . I11i * I11i / OOooOOo
 try :
  if 93 - 93: oo
  IiIiIi1I1 = oOo0OooOo ( )
  print 'existing_proxy' , IiIiIi1I1
  if 53 - 53: II111iiii + I1ii11iIi11i + iII111i
  if 24 - 24: o00O0oo - oO0o0ooO0 - o00O0oo * Ii1I . II111iiii / oO0o0ooO0
  if not proxyuser == None :
   I11Ii ( proxyip + ':' + port + ':0:' + proxyuser + '@' + proxypass )
  else :
   I11Ii ( proxyip + ':' + port + ':0' )
   if 66 - 66: I1ii11iIi11i
   if 97 - 97: oo - II111iiii / IIII * oOo0O0Ooo
  I1iOo = True
  O0o0oOooOoOo . update ( 80 , "" , "setting proxy complete, now playing" , "" )
  if 55 - 55: I11i . o00O0oo
  O0o0oOooOoOo . close ( )
  O0o0oOooOoOo = None
  import CustomPlayer
  II11iIII1i1I = CustomPlayer . MyXBMCPlayer ( )
  oOO0oo = xbmcgui . ListItem ( label = str ( name ) , iconImage = iconImage , thumbnailImage = xbmc . getInfoImage ( "ListItem.Thumb" ) , path = media_url )
  II11iIII1i1I . play ( media_url , oOO0oo )
  xbmc . sleep ( 1000 )
  while II11iIII1i1I . is_active :
   xbmc . sleep ( 200 )
 except :
  traceback . print_exc ( )
 if O0o0oOooOoOo :
  O0o0oOooOoOo . close ( )
 if I1iOo :
  if 87 - 87: I11i % oooo
  I11Ii ( IiIiIi1I1 )
  if 100 - 100: IIII . oOo0O0Ooo * IIII - oOo0O0Ooo . I1Ii111 * ooOoO0o
 return ''
 if 89 - 89: oO0o + oO0o0ooO0 * IIII
 if 28 - 28: II111iiii . iII111i % Ii1I / oo / IiII
def III1I1I ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  i1i111i1 = page_value
  page_value = OoO ( page_value , headers = referer )
  if 99 - 99: oOo0O0Ooo + oo + oo0 + I1ii11iIi11i % iII111i / I1Ii111
 O0OO0o0OO0OO = "(eval\(function\(p,a,c,k,e,(?:r|d).*)"
 if 64 - 64: OoO0O00
 iIIIiIi1I1i = re . compile ( O0OO0o0OO0OO ) . findall ( page_value )
 i1I1ii11i1Iii = ""
 if iIIIiIi1I1i and len ( iIIIiIi1I1i ) > 0 :
  for OOOO in iIIIiIi1I1i :
   OoOOoO0oOo = O0ooOOOO0O0 ( OOOO )
   i1IIi1i1Ii1 = iii ( OoOOoO0oOo , '\'(.*?)\'' )
   if 'unescape' in OoOOoO0oOo :
    OoOOoO0oOo = urllib . unquote ( i1IIi1i1Ii1 )
   i1I1ii11i1Iii += OoOOoO0oOo + '\n'
   if 45 - 45: oooo . iII111i / OOooOOo / oO0o0ooO0
   if 55 - 55: oO0o0ooO0
  i1i111i1 = iii ( i1I1ii11i1Iii , 'src="(.*?)"' )
  if 24 - 24: oO0o + iII111i . I11i / iII111i
  page_value = OoO ( i1i111i1 , headers = referer )
  if 56 - 56: oooo . oo0 - IiII * OoO0O00 * IIII
  if 5 - 5: IiII / IiII - Ii1I
  if 79 - 79: Ii1I + IIII
 iIiIIi = iii ( page_value , 'streamer\'.*?\'(.*?)\'\)' )
 III1I = iii ( page_value , 'file\',\s\'(.*?)\'' )
 if 11 - 11: O0oO - IiII + O0oO * iII111i / oOo0O0Ooo
 if 53 - 53: oooo + I11i - OOooOOo - iII111i / O0oO % oo0
 return iIiIIi + ' playpath=' + III1I + ' pageUrl=' + i1i111i1
 if 3 - 3: o00O0oo . O0oO % oOo0O0Ooo + Ii1I
def oo0o ( ) :
 o0IiiiI111I = 'https://pastebin.com/raw/'
 III1I11i1iIi = i1I1Ii1iI1ii . getSetting ( 'raw' )
 if i1I1Ii1iI1ii . getSetting ( 'raw' ) :
  o0oOo0Ooo0O ( "PastebinLinks" )
  o0 ( o0IiiiI111I + base64 . b32decode ( III1I11i1iIi + 'KZGQ3XA===' ) , '' )
  return
 else :
  iI1Ii11iIiI1 = xbmcgui . Dialog ( )
  OOOoo0OO = iI1Ii11iIiI1 . ok ( 'Attention' , "Definir senha no primeiro uso deste Addon nas definições." )
  if 69 - 69: I1ii11iIi11i * OoO0O00 * O0oO . o00O0oo - Ii1I
def I11iiIIiI1ii ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  page_value = OoO ( page_value , headers = referer )
 O0OO0o0OO0OO = "var a = (.*?);\s*var b = (.*?);\s*var c = (.*?);\s*var d = (.*?);\s*var f = (.*?);\s*var v_part = '(.*?)';"
 iIIIiIi1I1i = re . compile ( O0OO0o0OO0OO ) . findall ( page_value ) [ 0 ]
 if 12 - 12: IIII % oo0 + I11i + IIII / I1Ii111
 i11I1II1I11i , o00O , Ii1I1I1i1Ii , O00 , O00oOooo0 , OOOO = ( iIIIiIi1I1i )
 O00oOooo0 = int ( O00oOooo0 )
 i11I1II1I11i = int ( i11I1II1I11i ) / O00oOooo0
 o00O = int ( o00O ) / O00oOooo0
 Ii1I1I1i1Ii = int ( Ii1I1I1i1Ii ) / O00oOooo0
 O00 = int ( O00 ) / O00oOooo0
 if 94 - 94: I1Ii111 . I1Ii111 + oo0 - IiII * Ii1I
 i1iIiIi1I = 'rtmp://' + str ( i11I1II1I11i ) + '.' + str ( o00O ) + '.' + str ( Ii1I1I1i1Ii ) + '.' + str ( O00 ) + OOOO ;
 return i1iIiIi1I
 if 9 - 9: I11i . oOo0O0Ooo - Ii1I
def IiiiI ( url , useragent = None ) :
 str = '#EXTM3U'
 str += '\n#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=361816'
 str += '\n' + url + '&bytes=0-200000'
 oo0o0O00 = os . path . join ( i1I1Iiii1111 , 'testfile.m3u' )
 str += '\n'
 iiIIi ( oo0o0O00 , str )
 if 36 - 36: I1Ii111 . OoO0O00
 return oo0o0O00
 if 25 - 25: iII111i
def iiIIi ( file_name , page_data , append = False ) :
 if append :
  O00oOooo0 = open ( file_name , 'a' )
  O00oOooo0 . write ( page_data )
  O00oOooo0 . close ( )
 else :
  O00oOooo0 = open ( file_name , 'wb' )
  O00oOooo0 . write ( page_data )
  O00oOooo0 . close ( )
  return ''
  if 34 - 34: OOooOOo . oooo % O0OO0O0O
def iI11Ii111 ( file_name ) :
 O00oOooo0 = open ( file_name , 'rb' )
 O00 = O00oOooo0 . read ( )
 O00oOooo0 . close ( )
 return O00
 if 54 - 54: OOooOOo % o00O0oo . OOooOOo * IiII + OOooOOo % oo
def I1I1I11Ii ( page_data ) :
 import re , base64 , urllib ;
 ii1Iii1 = page_data
 while 'geh(' in ii1Iii1 :
  if ii1Iii1 . startswith ( 'lol(' ) : ii1Iii1 = ii1Iii1 [ 5 : - 1 ]
  if 80 - 80: ooOoO0o - I11i
  ii1Iii1 = re . compile ( '"(.*?)"' ) . findall ( ii1Iii1 ) [ 0 ] ;
  ii1Iii1 = base64 . b64decode ( ii1Iii1 ) ;
  ii1Iii1 = urllib . unquote ( ii1Iii1 ) ;
 print ii1Iii1
 return ii1Iii1
 if 41 - 41: I11i - I1ii11iIi11i * oOo0O0Ooo
def OO0OoOo0OOO ( page_data ) :
 if 47 - 47: II111iiii % O0OO0O0O * o00O0oo . ooOoO0o
 ii111Iiii = OoO ( page_data ) ;
 oo0oO0o0 = '(http.*)'
 import uuid
 Iii1Ii = str ( uuid . uuid1 ( ) ) . upper ( )
 ii11I11i = re . compile ( oo0oO0o0 ) . findall ( ii111Iiii )
 oOOOO = [ ( 'X-Playback-Session-Id' , Iii1Ii ) ]
 for i11i11i1 in ii11I11i :
  try :
   iiIII1IIiIIII = OoO ( i11i11i1 , headers = oOOOO ) ;
   if 19 - 19: o00O0oo - I11i / I11i + I1ii11iIi11i
  except : pass
  if 98 - 98: oooo % IiII + I1Ii111 . O0oO
 return page_data + '|&X-Playback-Session-Id=' + Iii1Ii
 if 99 - 99: O0OO0O0O + O0OO0O0O * I1Ii111 + O0OO0O0O * iII111i
 if 80 - 80: oOo0O0Ooo . ooOoO0o
def I1I11ii ( page_data ) :
 if 93 - 93: Ii1I % OOooOOo . O0OO0O0O / o00O0oo * iII111i
 if page_data . startswith ( 'http://dag.total-stream.net' ) :
  oOOOO = [ ( 'User-Agent' , 'Verismo-BlackUI_(2.4.7.5.8.0.34)' ) ]
  page_data = OoO ( page_data , headers = oOOOO ) ;
  if 29 - 29: I11i
 if '127.0.0.1' in page_data :
  return oo0iIiI ( page_data )
 elif iii ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  oO00Ooo0oO = iii ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + iii ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + iii ( page_data , '\\?y=([^&]+)&' )
 else :
  oO00Ooo0oO = iii ( page_data , 'href="([^"]+)"[^"]+$' )
  if len ( oO00Ooo0oO ) == 0 :
   oO00Ooo0oO = page_data
 oO00Ooo0oO = oO00Ooo0oO . replace ( ' ' , '%20' )
 return oO00Ooo0oO
 if 100 - 100: oO0o / oo - oOo0O0Ooo % ooOoO0o - oooo
def iii ( data , re_patten ) :
 i1IIIiiII1 = ''
 oO000oOo00o0o = re . search ( re_patten , data )
 if oO000oOo00o0o != None :
  i1IIIiiII1 = oO000oOo00o0o . group ( 1 )
 else :
  i1IIIiiII1 = ''
 return i1IIIiiII1
 if 17 - 17: I1Ii111 / I11i % I1ii11iIi11i
def oo0iIiI ( page_data ) :
 oO00Ooo0oO = ''
 if '127.0.0.1' in page_data :
  oO00Ooo0oO = iii ( page_data , '&ver_t=([^&]+)&' ) + ' live=true timeout=15 playpath=' + iii ( page_data , '\\?y=([a-zA-Z0-9-_\\.@]+)' )
  if 71 - 71: oO0o0ooO0 . IIII . oO0o
 if iii ( page_data , 'token=([^&]+)&' ) != '' :
  oO00Ooo0oO = oO00Ooo0oO + '?token=' + iii ( page_data , 'token=([^&]+)&' )
 elif iii ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  oO00Ooo0oO = iii ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + iii ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + iii ( page_data , '\\?y=([^&]+)&' )
 else :
  oO00Ooo0oO = iii ( page_data , 'HREF="([^"]+)"' )
  if 68 - 68: oo0 % iII111i * oO0o * oO0o0ooO0 * OoO0O00 + O0OO0O0O
 if 'dag1.asx' in oO00Ooo0oO :
  return I1I11ii ( oO00Ooo0oO )
  if 66 - 66: I1Ii111 % Ii1I % II111iiii
 if 'devinlivefs.fplive.net' not in oO00Ooo0oO :
  oO00Ooo0oO = oO00Ooo0oO . replace ( 'devinlive' , 'flive' )
 if 'permlivefs.fplive.net' not in oO00Ooo0oO :
  oO00Ooo0oO = oO00Ooo0oO . replace ( 'permlive' , 'flive' )
 return oO00Ooo0oO
 if 34 - 34: I11i / o00O0oo % O0OO0O0O . oO0o . oo
 if 29 - 29: O0OO0O0O . IIII
def OO0o0oO0O000o ( str_eval ) :
 I1iI11iii = ""
 try :
  oo0oO = "w,i,s,e=(" + str_eval + ')'
  exec ( oo0oO )
  I1iI11iii = IiIi1iI11 ( w , i , ii1Iii1 , e )
 except : traceback . print_exc ( file = sys . stdout )
 if 11 - 11: Ii1I
 return I1iI11iii
 if 26 - 26: oooo * IIII - IiII
def IiIi1iI11 ( w , i , s , e ) :
 III1II111Ii1 = 0 ;
 o0O0OO0o = 0 ;
 OOOoOo = 0 ;
 OOoO0oo0O = [ ] ;
 iiI1I1ii = [ ] ;
 while True :
  if ( III1II111Ii1 < 5 ) :
   iiI1I1ii . append ( w [ III1II111Ii1 ] )
  elif ( III1II111Ii1 < len ( w ) ) :
   OOoO0oo0O . append ( w [ III1II111Ii1 ] ) ;
  III1II111Ii1 += 1 ;
  if ( o0O0OO0o < 5 ) :
   iiI1I1ii . append ( i [ o0O0OO0o ] )
  elif ( o0O0OO0o < len ( i ) ) :
   OOoO0oo0O . append ( i [ o0O0OO0o ] )
  o0O0OO0o += 1 ;
  if ( OOOoOo < 5 ) :
   iiI1I1ii . append ( s [ OOOoOo ] )
  elif ( OOOoOo < len ( s ) ) :
   OOoO0oo0O . append ( s [ OOOoOo ] ) ;
  OOOoOo += 1 ;
  if ( len ( w ) + len ( i ) + len ( s ) + len ( e ) == len ( OOoO0oo0O ) + len ( iiI1I1ii ) + len ( e ) ) :
   break ;
   if 79 - 79: oooo
 O00oO0o = '' . join ( OOoO0oo0O )
 I1i1iii = '' . join ( iiI1I1ii )
 o0O0OO0o = 0 ;
 IiI1iI1 = [ ] ;
 for III1II111Ii1 in range ( 0 , len ( OOoO0oo0O ) , 2 ) :
  if 23 - 23: o00O0oo + IiII * O0oO / oooo - o00O0oo
  OOooO0OO0 = - 1 ;
  if ( ord ( I1i1iii [ o0O0OO0o ] ) % 2 ) :
   OOooO0OO0 = 1 ;
   if 5 - 5: o00O0oo
  IiI1iI1 . append ( chr ( int ( O00oO0o [ III1II111Ii1 : III1II111Ii1 + 2 ] , 36 ) - OOooO0OO0 ) ) ;
  o0O0OO0o += 1 ;
  if ( o0O0OO0o >= len ( iiI1I1ii ) ) :
   o0O0OO0o = 0 ;
 i1iIiIi1I = '' . join ( IiI1iI1 )
 if 'eval(function(w,i,s,e)' in i1iIiIi1I :
  if 62 - 62: OOooOOo . II111iiii . IiII . oO0o * o00O0oo
  i1iIiIi1I = re . compile ( 'eval\(function\(w,i,s,e\).*}\((.*?)\)' ) . findall ( i1iIiIi1I ) [ 0 ]
  return OO0o0oO0O000o ( i1iIiIi1I )
 else :
  if 78 - 78: iII111i / oO0o - iII111i * II111iiii . OOooOOo
  return i1iIiIi1I
  if 96 - 96: oOo0O0Ooo % oo . I11i . O0OO0O0O
def O0ooOOOO0O0 ( page_value , regex_for_text = '' , iterations = 1 , total_iteration = 1 ) :
 try :
  Ii1Iii11 = None
  if page_value . startswith ( "http" ) :
   page_value = OoO ( page_value )
   if 97 - 97: IiII / iII111i . OoO0O00
  if regex_for_text and len ( regex_for_text ) > 0 :
   try :
    page_value = re . compile ( regex_for_text ) . findall ( page_value ) [ 0 ]
   except : return 'NOTPACKED'
   if 44 - 44: ooOoO0o % I1Ii111 . IIII
  page_value = Ii11Iii ( page_value , iterations , total_iteration )
 except :
  page_value = 'UNPACKEDFAILED'
  traceback . print_exc ( file = sys . stdout )
  if 68 - 68: oOo0O0Ooo % O0OO0O0O
 if 'sav1live.tv' in page_value :
  page_value = page_value . replace ( 'sav1live.tv' , 'sawlive.tv' )
  if 74 - 74: oo + OOooOOo + oooo * OOooOOo * oooo + I1Ii111
 return page_value
 if 64 - 64: oooo / O0OO0O0O % oO0o0ooO0 . II111iiii + oO0o0ooO0 + iII111i
def Ii11Iii ( sJavascript , iteration = 1 , totaliterations = 2 ) :
 if 79 - 79: II111iiii - oO0o0ooO0 * oO0o0ooO0 . OOooOOo
 if sJavascript . startswith ( 'var _0xcb8a=' ) :
  Oo00ooO0OoOo = sJavascript . split ( 'var _0xcb8a=' )
  oo0oO = "myarray=" + Oo00ooO0OoOo [ 1 ] . split ( "eval(" ) [ 0 ]
  exec ( oo0oO )
  o0oOO00 = 62
  ii11iiIi = int ( Oo00ooO0OoOo [ 1 ] . split ( ",62," ) [ 1 ] . split ( ',' ) [ 0 ] )
  i11iI11I1I = myarray [ 0 ]
  Ii1iiIi1I11i = myarray [ 3 ]
  with open ( 'temp file' + str ( iteration ) + '.js' , "wb" ) as O0OOO :
   O0OOO . write ( str ( Ii1iiIi1I11i ) )
   if 37 - 37: O0OO0O0O - I1Ii111
 else :
  if 21 - 21: oooo / IIII + O0oO - I1Ii111 / I1ii11iIi11i / OoO0O00
  if "rn p}('" in sJavascript :
   Oo00ooO0OoOo = sJavascript . split ( "rn p}('" )
  else :
   Oo00ooO0OoOo = sJavascript . split ( "rn A}('" )
   if 69 - 69: oOo0O0Ooo . OOooOOo
   if 53 - 53: I1Ii111
  i11iI11I1I , o0oOO00 , ii11iiIi , Ii1iiIi1I11i = ( '' , '0' , '0' , '' )
  if 68 - 68: iII111i / IIII % IIII % O0OO0O0O
  oo0oO = "p1,a1,c1,k1=('" + Oo00ooO0OoOo [ 1 ] . split ( ".spli" ) [ 0 ] + ')'
  exec ( oo0oO )
 Ii1iiIi1I11i = Ii1iiIi1I11i . split ( '|' )
 Oo00ooO0OoOo = Oo00ooO0OoOo [ 1 ] . split ( "))'" )
 if 90 - 90: oO0o0ooO0 . O0oO / oooo
 if 28 - 28: oO0o0ooO0 + iII111i - O0oO / oooo - oOo0O0Ooo
 if 45 - 45: O0OO0O0O / oo * iII111i * oO0o
 if 35 - 35: Ii1I / o00O0oo % oOo0O0Ooo + oooo
 if 79 - 79: OOooOOo / O0oO
 if 77 - 77: I1ii11iIi11i
 if 46 - 46: IIII
 if 72 - 72: o00O0oo * IiII
 if 67 - 67: oo
 if 5 - 5: OoO0O00 . II111iiii
 if 57 - 57: oOo0O0Ooo
 if 35 - 35: II111iiii - IIII / oO0o
 if 50 - 50: OOooOOo
 if 33 - 33: I1Ii111
 if 98 - 98: OOooOOo % OoO0O00
 if 95 - 95: oooo - IIII - IiII + IIII % Ii1I . oOo0O0Ooo
 if 41 - 41: O0OO0O0O + iII111i . oo - OoO0O00 * I11i . oO0o
 if 68 - 68: I11i
 if 20 - 20: IIII - IIII
 if 37 - 37: oO0o0ooO0
 if 37 - 37: I1ii11iIi11i / oO0o0ooO0 * O0OO0O0O
 if 73 - 73: o00O0oo * o00O0oo / O0oO
 i1iiiIi1i = ''
 O00 = ''
 if 43 - 43: Ii1I . oo . oO0o0ooO0 + O0OO0O0O * ooOoO0o * O0OO0O0O
 if 41 - 41: Ii1I + ooOoO0o % II111iiii . Ii1I + o00O0oo . o00O0oo
 Iiii11I = str ( OO0ooo0 ( i11iI11I1I , o0oOO00 , ii11iiIi , Ii1iiIi1I11i , i1iiiIi1i , O00 , iteration ) )
 if 7 - 7: Ii1I - iII111i * IiII + I11i . Ii1I
 if 85 - 85: O0OO0O0O
 if 32 - 32: II111iiii . oO0o / I1ii11iIi11i * I11i / I11i * ooOoO0o
 if 19 - 19: ooOoO0o
 if 55 - 55: IiII % IiII / O0OO0O0O % o00O0oo - I11i . I1ii11iIi11i
 if iteration >= totaliterations :
  if 49 - 49: oooo * oo . II111iiii
  return Iiii11I
 else :
  if 90 - 90: I11i % Ii1I - oooo % OOooOOo
  return Ii11Iii ( Iiii11I , iteration + 1 )
  if 8 - 8: OOooOOo * I1ii11iIi11i / oO0o0ooO0 % ooOoO0o - oOo0O0Ooo
def OO0ooo0 ( p , a , c , k , e , d , iteration , v = 1 ) :
 if 71 - 71: o00O0oo
 if 23 - 23: oo . oooo . IiII . O0OO0O0O % ooOoO0o % oo0
 if 11 - 11: O0OO0O0O - OoO0O00 . IiII . ooOoO0o % IIII
 while ( c >= 1 ) :
  c = c - 1
  if ( k [ c ] ) :
   IIi1 = str ( OoO0oO ( c , a ) )
   if v == 1 :
    p = re . sub ( '\\b' + IIi1 + '\\b' , k [ c ] , p )
   else :
    p = Ii ( p , IIi1 , k [ c ] )
    if 20 - 20: I11i * O0oO
    if 10 - 10: I1Ii111 - I1ii11iIi11i
    if 59 - 59: II111iiii * I1ii11iIi11i + oo
    if 23 - 23: O0oO
    if 13 - 13: oooo
    if 77 - 77: oo0 - oooo / iII111i / O0oO / oO0o
 return p
 if 56 - 56: II111iiii * O0OO0O0O
 if 85 - 85: II111iiii % OOooOOo * oooo
 if 44 - 44: oooo . Ii1I + IIII . O0oO
def Ii ( source_str , word_to_find , replace_with ) :
 II1i11 = None
 II1i11 = source_str . split ( word_to_find )
 if len ( II1i11 ) > 1 :
  Ii1IIIII = [ ]
  iiiIIiiii11 = 0
  for IIiI1iIIiI1I1i in II1i11 :
   if 44 - 44: oOo0O0Ooo + OOooOOo + Ii1I . oOo0O0Ooo * OOooOOo % oooo
   Ii1IIIII . append ( IIiI1iIIiI1I1i )
   Ii11iI = word_to_find
   if 72 - 72: IiII . IiII - Ii1I
   if 48 - 48: I1ii11iIi11i - O0oO + I1ii11iIi11i - oOo0O0Ooo * oo0 . o00O0oo
   if iiiIIiiii11 == len ( II1i11 ) - 1 :
    Ii11iI = ''
   else :
    if len ( IIiI1iIIiI1I1i ) == 0 :
     if ( len ( II1i11 [ iiiIIiiii11 + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( II1i11 [ iiiIIiiii11 + 1 ] ) > 0 and II1i11 [ iiiIIiiii11 + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) :
      Ii11iI = replace_with
      if 35 - 35: oO0o0ooO0 . O0OO0O0O + I1ii11iIi11i + IiII + oo
    else :
     if ( II1i11 [ iiiIIiiii11 ] [ - 1 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) and ( ( len ( II1i11 [ iiiIIiiii11 + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( II1i11 [ iiiIIiiii11 + 1 ] ) > 0 and II1i11 [ iiiIIiiii11 + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) ) :
      Ii11iI = replace_with
      if 65 - 65: O0OO0O0O * oOo0O0Ooo / oOo0O0Ooo . OOooOOo
   Ii1IIIII . append ( Ii11iI )
   iiiIIiiii11 += 1
   if 87 - 87: OoO0O00 * Ii1I % I1ii11iIi11i * I1ii11iIi11i
  source_str = '' . join ( Ii1IIIII )
 return source_str
 if 58 - 58: IiII . I11i + oOo0O0Ooo % I1ii11iIi11i - oO0o
def I1Iii1Ii1i1 ( num , radix ) :
 if 10 - 10: o00O0oo . oo + ooOoO0o
 oo000ii = ""
 if num == 0 : return '0'
 while num > 0 :
  oo000ii = "0123456789abcdefghijklmnopqrstuvwxyz" [ num % radix ] + oo000ii
  num /= radix
 return oo000ii
 if 66 - 66: oO0o % I11i
def OoO0oO ( cc , a ) :
 IIi1 = "" if cc < a else OoO0oO ( int ( cc / a ) , a )
 cc = ( cc % a )
 iI1ii11Ii = chr ( cc + 29 ) if cc > 35 else str ( I1Iii1Ii1i1 ( cc , 36 ) )
 return IIi1 + iI1ii11Ii
 if 97 - 97: IIII + iII111i - oO0o % iII111i - I11i
 if 37 - 37: II111iiii
def oo0OoOooo ( cookieJar ) :
 try :
  oo0ooO0 = ""
  for iiii11I , oOooo0OOO in enumerate ( cookieJar ) :
   oo0ooO0 += oOooo0OOO . name + "=" + oOooo0OOO . value + ";"
 except : pass
 if 65 - 65: II111iiii
 return oo0ooO0
 if 14 - 14: IiII % II111iiii
 if 86 - 86: oo0 + O0OO0O0O * oO0o0ooO0 - oO0o * IiII + O0OO0O0O
def oo0o0O0Oooooo ( cookieJar , COOKIEFILE ) :
 try :
  i1I1iI = os . path . join ( i1I1Iiii1111 , COOKIEFILE )
  cookieJar . save ( i1I1iI , ignore_discard = True )
 except : pass
 if 95 - 95: oooo . IIII % o00O0oo - IIII * OoO0O00
def O00oO0 ( COOKIEFILE ) :
 if 89 - 89: o00O0oo . oOo0O0Ooo
 ooOoo0OoOO = None
 if COOKIEFILE :
  try :
   i1I1iI = os . path . join ( i1I1Iiii1111 , COOKIEFILE )
   ooOoo0OoOO = cookielib . LWPCookieJar ( )
   ooOoo0OoOO . load ( i1I1iI , ignore_discard = True )
  except :
   ooOoo0OoOO = None
   if 38 - 38: oO0o / O0oO % IIII * I1Ii111 + oo0 % O0oO
 if not ooOoo0OoOO :
  ooOoo0OoOO = cookielib . LWPCookieJar ( )
  if 61 - 61: IIII - ooOoO0o % Ii1I / O0oO / o00O0oo + oooo
 return ooOoo0OoOO
 if 87 - 87: IIII + O0oO + O0OO0O0O / oo % oO0o0ooO0 / IIII
def oO00OoOO ( fun_call , page_data , Cookie_Jar , m ) :
 OOo000OO000 = ''
 if 83 - 83: I11i % iII111i + I1Ii111 % oo0 + O0OO0O0O
 if i1iiIIiiI111 not in sys . path :
  sys . path . append ( i1iiIIiiI111 )
  if 65 - 65: oooo % iII111i + O0OO0O0O / II111iiii
  if 52 - 52: ooOoO0o % IiII * oOo0O0Ooo % I1Ii111 + IiII / o00O0oo
 try :
  oo000oOO00o0oOO = 'import ' + fun_call . split ( '.' ) [ 0 ]
  if 27 - 27: I1ii11iIi11i
  exec ( oo000oOO00o0oOO )
  if 95 - 95: I1Ii111
 except :
  if 44 - 44: IiII + I1Ii111 . oO0o0ooO0 / OoO0O00 % oooo + oO0o0ooO0
  traceback . print_exc ( file = sys . stdout )
  if 61 - 61: IiII / oO0o + OoO0O00 . iII111i / I1ii11iIi11i * IiII
 exec ( 'ret_val=' + fun_call )
 if 46 - 46: oooo
 if 33 - 33: I1Ii111 % I1Ii111 % O0OO0O0O / oOo0O0Ooo . oo
 try :
  return str ( OOo000OO000 )
 except : return OOo000OO000
 if 91 - 91: O0oO * I1Ii111 - OoO0O00 . oOo0O0Ooo - I1ii11iIi11i + O0oO
def IIIii1iiIi ( fun_call , page_data , Cookie_Jar , m ) :
 if 56 - 56: I11i / oO0o0ooO0 * oOo0O0Ooo . I11i
 OOo000OO000 = ''
 if i1iiIIiiI111 not in sys . path :
  sys . path . append ( i1iiIIiiI111 )
  if 15 - 15: oo0
 O00oOooo0 = open ( os . path . join ( i1iiIIiiI111 , 'LSProdynamicCode.py' ) , "wb" )
 O00oOooo0 . write ( "# -*- coding: utf-8 -*-\n" )
 O00oOooo0 . write ( fun_call . encode ( "utf-8" ) ) ;
 if 13 - 13: I1Ii111 * OoO0O00 * iII111i * OoO0O00 % oO0o0ooO0 / oOo0O0Ooo
 O00oOooo0 . close ( )
 import LSProdynamicCode
 OOo000OO000 = LSProdynamicCode . GetLSProData ( page_data , Cookie_Jar , m )
 try :
  return str ( OOo000OO000 )
 except : return OOo000OO000
 if 100 - 100: oO0o0ooO0 . ooOoO0o - oooo . oo0 / OoO0O00
 if 71 - 71: IIII * I1ii11iIi11i . I1Ii111
def i1ii1iiIi1II ( captchakey , cj , type = 1 ) :
 if 98 - 98: oO0o - ooOoO0o . oO0o0ooO0 % oo0
 if 69 - 69: Ii1I + o00O0oo * O0OO0O0O . IiII % OOooOOo
 if 96 - 96: O0oO . O0oO - I1Ii111 / I1Ii111
 OoOo = ""
 iIIi11i1i1i1I = ""
 if 13 - 13: o00O0oo + IiII / oooo
 if 67 - 67: OOooOOo - OOooOOo * oO0o - o00O0oo % iII111i
 if 44 - 44: oOo0O0Ooo . oo + IiII
 if 16 - 16: I11i - oO0o / IIII
 if 48 - 48: oooo
 OoooooOo = False
 OooOo = None
 iIIi11i1i1i1I = None
 if len ( captchakey ) > 0 :
  oOo0 = captchakey
  if not oOo0 . startswith ( 'http' ) :
   oOo0 = 'http://www.google.com/recaptcha/api/challenge?k=' + oOo0 + '&ajax=1'
   if 30 - 30: IiII + OoO0O00 - oO0o0ooO0 * II111iiii
  OoooooOo = True
  if 19 - 19: oO0o0ooO0 - I11i . oooo . OOooOOo / IiII
  OOO0O00Oo = 'challenge.*?\'(.*?)\''
  ii1 = '\'(.*?)\''
  oOOO0ooOO = OoO ( oOo0 , cookieJar = cj )
  OoOo = re . findall ( OOO0O00Oo , oOOO0ooOO ) [ 0 ]
  i11IiI1iiI11 = 'http://www.google.com/recaptcha/api/reload?c=' ;
  OOoOOOO00 = oOo0 . split ( 'k=' ) [ 1 ]
  i11IiI1iiI11 += OoOo + '&k=' + OOoOOOO00 + '&reason=i&type=image&lang=en'
  IIii1III = OoO ( i11IiI1iiI11 , cookieJar = cj )
  OooOo = re . findall ( ii1 , IIii1III ) [ 0 ]
  ooooOoo0OO = 'http://www.google.com/recaptcha/api/image?c=' + OooOo
  if not ooooOoo0OO . startswith ( "http" ) :
   ooooOoo0OO = 'http://www.google.com/recaptcha/api/' + ooooOoo0OO
  import random
  I1i = random . randrange ( 100 , 1000 , 5 )
  Oo0 = os . path . join ( i1I1Iiii1111 , str ( I1i ) + "captcha.img" )
  O0000Oo00o = open ( Oo0 , "wb" )
  O0000Oo00o . write ( OoO ( ooooOoo0OO , cookieJar = cj ) )
  O0000Oo00o . close ( )
  II1 = iio00 ( captcha = Oo0 )
  iIIi11i1i1i1I = II1 . get ( )
  os . remove ( Oo0 )
  if 4 - 4: oO0o
 if OooOo :
  if type == 1 :
   return 'recaptcha_challenge_field=' + urllib . quote_plus ( OooOo ) + '&recaptcha_response_field=' + urllib . quote_plus ( iIIi11i1i1i1I )
  elif type == 2 :
   return 'recaptcha_challenge_field:' + OooOo + ',recaptcha_response_field:' + iIIi11i1i1i1I
  else :
   return 'recaptcha_challenge_field=' + urllib . quote_plus ( OooOo ) + '&recaptcha_response_field=' + urllib . quote_plus ( iIIi11i1i1i1I )
 else :
  return ''
  if 62 - 62: oo
  if 26 - 26: oo0 + OoO0O00 * II111iiii
def OoO ( url , cookieJar = None , post = None , timeout = 20 , headers = None , noredir = False ) :
 if 70 - 70: I1Ii111 % oO0o * o00O0oo + oooo
 if 11 - 11: IIII % oo0 % iII111i . oO0o0ooO0
 I11oo0ooOO = urllib2 . HTTPCookieProcessor ( cookieJar )
 if 92 - 92: OoO0O00
 if noredir :
  oOo0oO = urllib2 . build_opener ( iIIii1IIi , I11oo0ooOO , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
 else :
  oOo0oO = urllib2 . build_opener ( I11oo0ooOO , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
  if 45 - 45: O0OO0O0O % oOo0O0Ooo - o00O0oo . oO0o
 IIi11IIiIii1 = urllib2 . Request ( url )
 IIi11IIiIii1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36' )
 if headers :
  for iii1 , I1II in headers :
   IIi11IIiIii1 . add_header ( iii1 , I1II )
   if 9 - 9: I1ii11iIi11i % II111iiii - ooOoO0o
 Oo00OOo00O = oOo0oO . open ( IIi11IIiIii1 , post , timeout = timeout )
 OoOiIIiii = Oo00OOo00O . read ( )
 Oo00OOo00O . close ( )
 return OoOiIIiii ;
 if 43 - 43: oO0o % oO0o
def IIiii11ii1i ( str , reg = None ) :
 if reg :
  str = re . findall ( reg , str ) [ 0 ]
 II1iI1IIi = urllib . unquote ( str [ 0 : len ( str ) - 1 ] ) ;
 Ii11iiI1 = '' ;
 for IiIIIiI1I1 in range ( len ( II1iI1IIi ) ) :
  Ii11iiI1 += chr ( ord ( II1iI1IIi [ IiIIIiI1I1 ] ) - II1iI1IIi [ len ( II1iI1IIi ) - 1 ] ) ;
 Ii11iiI1 = urllib . unquote ( Ii11iiI1 )
 if 71 - 71: I11i / IiII % IiII
 return Ii11iiI1
 if 89 - 89: II111iiii + oo0 / I1Ii111 + oooo % O0oO
def I11I1IIiiII1 ( str ) :
 iI1ii1Ii = re . findall ( 'unescape\(\'(.*?)\'' , str )
 if 78 - 78: oooo * I1ii11iIi11i . I1ii11iIi11i - IiII . oooo
 if ( not iI1ii1Ii == None ) and len ( iI1ii1Ii ) > 0 :
  for I111I1I in iI1ii1Ii :
   if 54 - 54: OoO0O00 + I1Ii111 % I1Ii111 % I11i
   str = str . replace ( I111I1I , urllib . unquote ( I111I1I ) )
 return str
 if 25 - 25: o00O0oo - I1ii11iIi11i
Iii1IIIIIII = 0
def O0oOoOOO0OO ( m , html_page , cookieJar ) :
 global Iii1IIIIIII
 Iii1IIIIIII += 1
 iI1I11i = m [ 'expres' ]
 i1i111i1 = m [ 'page' ]
 I11i11I1II = re . compile ( '\$LiveStreamCaptcha\[([^\]]*)\]' ) . findall ( iI1I11i ) [ 0 ]
 if 13 - 13: II111iiii . O0oO + OOooOOo / ooOoO0o
 oOo0 = re . compile ( I11i11I1II ) . findall ( html_page ) [ 0 ]
 if 15 - 15: oO0o0ooO0 . oo * OOooOOo % oooo
 if not oOo0 . startswith ( "http" ) :
  III11I1 = 'http://' + "" . join ( i1i111i1 . split ( '/' ) [ 2 : 3 ] )
  if oOo0 . startswith ( "/" ) :
   oOo0 = III11I1 + oOo0
  else :
   oOo0 = III11I1 + '/' + oOo0
   if 61 - 61: OOooOOo - oO0o + oOo0O0Ooo * IiII % oO0o
 Oo0 = os . path . join ( i1I1Iiii1111 , str ( Iii1IIIIIII ) + "captcha.jpg" )
 O0000Oo00o = open ( Oo0 , "wb" )
 if 24 - 24: O0oO - I1Ii111 * iII111i
 IIi11IIiIii1 = urllib2 . Request ( oOo0 )
 IIi11IIiIii1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
 if 'referer' in m :
  IIi11IIiIii1 . add_header ( 'Referer' , m [ 'referer' ] )
 if 'agent' in m :
  IIi11IIiIii1 . add_header ( 'User-agent' , m [ 'agent' ] )
 if 'setcookie' in m :
  if 87 - 87: ooOoO0o - Ii1I % Ii1I . iII111i / Ii1I
  IIi11IIiIii1 . add_header ( 'Cookie' , m [ 'setcookie' ] )
  if 6 - 6: OOooOOo / oooo * II111iiii * oo0
  if 79 - 79: oO0o0ooO0 % oO0o
  if 81 - 81: oo0 + oo0 * oO0o + oO0o0ooO0
  if 32 - 32: O0OO0O0O . II111iiii
 urllib2 . urlopen ( IIi11IIiIii1 )
 Oo00OOo00O = urllib2 . urlopen ( IIi11IIiIii1 )
 if 15 - 15: oOo0O0Ooo . oO0o
 O0000Oo00o . write ( Oo00OOo00O . read ( ) )
 Oo00OOo00O . close ( )
 O0000Oo00o . close ( )
 II1 = iio00 ( captcha = Oo0 )
 iIIi11i1i1i1I = II1 . get ( )
 return iIIi11i1i1i1I
 if 17 - 17: oo0 / I1ii11iIi11i . oO0o / oOo0O0Ooo
def Ii1 ( imageregex , html_page , cookieJar , m ) :
 global Iii1IIIIIII
 Iii1IIIIIII += 1
 if 59 - 59: I1ii11iIi11i % O0OO0O0O . OOooOOo
 if 41 - 41: oo + OoO0O00 * O0oO
 if not imageregex == '' :
  if html_page . startswith ( "http" ) :
   III11I1 = OoO ( html_page , cookieJar = cookieJar )
  else :
   III11I1 = html_page
  oOo0 = re . compile ( imageregex ) . findall ( html_page ) [ 0 ]
 else :
  oOo0 = html_page
  if 'oneplay.tv/embed' in html_page :
   import oneplay
   III11I1 = OoO ( html_page , cookieJar = cookieJar )
   oOo0 = oneplay . getCaptchaUrl ( III11I1 )
   if 68 - 68: ooOoO0o - oOo0O0Ooo
 Oo0 = os . path . join ( i1I1Iiii1111 , str ( Iii1IIIIIII ) + "captcha.jpg" )
 O0000Oo00o = open ( Oo0 , "wb" )
 if 41 - 41: iII111i
 IIi11IIiIii1 = urllib2 . Request ( oOo0 )
 IIi11IIiIii1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
 if 'referer' in m :
  IIi11IIiIii1 . add_header ( 'Referer' , m [ 'referer' ] )
 if 'agent' in m :
  IIi11IIiIii1 . add_header ( 'User-agent' , m [ 'agent' ] )
 if 'accept' in m :
  IIi11IIiIii1 . add_header ( 'Accept' , m [ 'accept' ] )
 if 'setcookie' in m :
  if 21 - 21: O0oO + I11i % IIII + oo0 + o00O0oo + OoO0O00
  IIi11IIiIii1 . add_header ( 'Cookie' , m [ 'setcookie' ] )
  if 98 - 98: IIII
 Oo00OOo00O = urllib2 . urlopen ( IIi11IIiIii1 )
 if 49 - 49: I1ii11iIi11i * iII111i + I11i - oo0
 O0000Oo00o . write ( Oo00OOo00O . read ( ) )
 Oo00OOo00O . close ( )
 O0000Oo00o . close ( )
 II1 = iio00 ( captcha = Oo0 )
 iIIi11i1i1i1I = II1 . get ( )
 return iIIi11i1i1i1I
 if 74 - 74: I1ii11iIi11i / oooo . OoO0O00 - oO0o
 if 62 - 62: IiII / OoO0O00 + OOooOOo % O0oO / OOooOOo + Ii1I
def IiI11I111 ( name , headname ) :
 Ooo000O00 = xbmc . Keyboard ( 'default' , 'heading' , True )
 Ooo000O00 . setDefault ( name )
 Ooo000O00 . setHeading ( headname )
 Ooo000O00 . setHiddenInput ( False )
 return Ooo000O00 . getText ( )
 if 36 - 36: IiII % oo0
class iio00 ( xbmcgui . WindowDialog ) :
 def __init__ ( self , * args , ** kwargs ) :
  self . cptloc = kwargs . get ( 'captcha' )
  self . img = xbmcgui . ControlImage ( 335 , 30 , 624 , 60 , self . cptloc )
  self . addControl ( self . img )
  self . kbd = xbmc . Keyboard ( )
  if 47 - 47: oo + OoO0O00 . I1ii11iIi11i * iII111i . I1Ii111 / oo
 def get ( self ) :
  self . show ( )
  time . sleep ( 2 )
  self . kbd . doModal ( )
  if ( self . kbd . isConfirmed ( ) ) :
   i11ii = self . kbd . getText ( )
   self . close ( )
   return i11ii
  self . close ( )
  return False
  if 83 - 83: Ii1I * Ii1I + IiII
def II1Ii11I111I ( ) :
 import time
 return str ( int ( time . time ( ) * 1000 ) )
 if 57 - 57: O0OO0O0O - O0OO0O0O . Ii1I / I11i / ooOoO0o
def O00oO ( ) :
 import time
 return str ( int ( time . time ( ) ) )
 if 20 - 20: IiII * OoO0O00 - OOooOOo - iII111i * IIII
def I1i1II1 ( ) :
 oOOooI1 = [ ]
 ooiiI1IIIii = sys . argv [ 2 ]
 if len ( ooiiI1IIIii ) >= 2 :
  iIOO0OOoooo0o = sys . argv [ 2 ]
  IiIi1Ii = iIOO0OOoooo0o . replace ( '?' , '' )
  if ( iIOO0OOoooo0o [ len ( iIOO0OOoooo0o ) - 1 ] == '/' ) :
   iIOO0OOoooo0o = iIOO0OOoooo0o [ 0 : len ( iIOO0OOoooo0o ) - 2 ]
  iiIIiI11II1 = IiIi1Ii . split ( '&' )
  oOOooI1 = { }
  for IiIIIiI1I1 in range ( len ( iiIIiI11II1 ) ) :
   oooOo = { }
   oooOo = iiIIiI11II1 [ IiIIIiI1I1 ] . split ( '=' )
   if ( len ( oooOo ) ) == 2 :
    oOOooI1 [ oooOo [ 0 ] ] = oooOo [ 1 ]
 return oOOooI1
 if 79 - 79: iII111i - OoO0O00
def oO0o0 ( url ) :
 if i1I1Ii1iI1ii . getSetting ( 'Updatecommonresolvers' ) == 'true' :
  i11i11i1 = os . path . join ( i11 , 'generator.py' )
  if xbmcvfs . exists ( i11i11i1 ) :
   os . remove ( i11i11i1 )
   if 43 - 43: oo + O0OO0O0O % oO0o / ooOoO0o * oOo0O0Ooo
  OoOi1iI11Iii = 'https://raw.githubusercontent.com/lambda81/lambda-addons/master/plugin.video.genesis/commonresolvers.py'
  O000Oo = urllib . urlretrieve ( OoOi1iI11Iii , i11i11i1 )
  i1I1Ii1iI1ii . setSetting ( 'Updatecommonresolvers' , 'false' )
 try :
  import generator
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(Please enable Update Commonresolvers to Play in Settings. - ,10000)" )
  if 58 - 58: oO0o - OOooOOo . oo0 % oo0 / oo / iII111i
 Ii1ii1IiiiiiI = generator . get ( url ) . result
 if url == Ii1ii1IiiiiiI or Ii1ii1IiiiiiI is None :
  if 77 - 77: oo0
  xbmc . executebuiltin ( "XBMC.Notification(" + II1iI + ",Iniciar link!,5000," + oOo0oooo00o + ")" )
  import urlresolver
  i1IIii11i1I1 = urlresolver . HostedMediaFile ( url )
  if i1IIii11i1I1 :
   ooI1i = urlresolver . resolve ( url )
   Ii1ii1IiiiiiI = ooI1i
 if Ii1ii1IiiiiiI :
  if isinstance ( Ii1ii1IiiiiiI , list ) :
   for iII1111III1I in Ii1ii1IiiiiiI :
    Ii1I1 = i1I1Ii1iI1ii . getSetting ( 'quality' )
    if iII1111III1I [ 'quality' ] == 'HD' :
     ooI1i = iII1111III1I [ 'url' ]
     break
    elif iII1111III1I [ 'quality' ] == 'SD' :
     ooI1i = iII1111III1I [ 'url' ]
    elif iII1111III1I [ 'quality' ] == '1080p' and i1I1Ii1iI1ii . getSetting ( '1080pquality' ) == 'true' :
     ooI1i = iII1111III1I [ 'url' ]
     break
  else :
   ooI1i = Ii1ii1IiiiiiI
 return ooI1i
 if 98 - 98: oO0o0ooO0 * oooo . ooOoO0o * I1ii11iIi11i / Ii1I + O0oO
def iiI1ii111 ( url , listitem , pdialogue = None ) :
 if 97 - 97: O0OO0O0O / IiII + I11i . iII111i % OOooOOo - OOooOOo
 if url . lower ( ) . startswith ( 'plugin' ) :
  print 'playing via runplugin'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + url + ')' )
  for IiIIIiI1I1 in range ( 8 ) :
   xbmc . sleep ( 500 )
   try :
    if 33 - 33: I1Ii111 % OoO0O00 + oO0o
    if xbmc . getCondVisibility ( "Player.HasMedia" ) and xbmc . Player ( ) . isPlaying ( ) :
     return True
   except : pass
  return False
 import CustomPlayer , time
 if 93 - 93: oo . oO0o0ooO0 / oOo0O0Ooo + oO0o0ooO0
 II11iIII1i1I = CustomPlayer . MyXBMCPlayer ( )
 II11iIII1i1I . pdialogue = pdialogue
 OOooOO = time . time ( )
 if 59 - 59: oO0o - oO0o + o00O0oo
 print 'going to play'
 import time
 iiII = time . time ( )
 II11iIII1i1I . play ( url , listitem )
 xbmc . sleep ( 1000 )
 if 9 - 9: iII111i - IIII % O0OO0O0O . oo . oOo0O0Ooo / oOo0O0Ooo
 try :
  while II11iIII1i1I . is_active :
   xbmc . sleep ( 400 )
   if 82 - 82: I1Ii111 / O0oO * I1Ii111 % oo0 * OoO0O00
   if II11iIII1i1I . urlplayed :
    print 'yes played'
    return True
   if time . time ( ) - iiII > 4 : return False
   if 83 - 83: oO0o + IiII - I11i + oooo % I1ii11iIi11i
 except : pass
 print 'not played' , url
 return False
def II111I1 ( name , mu_playlist , queueVideo = None ) :
 OooOoOo = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 if 32 - 32: IiII % oo
 if '$$LSPlayOnlyOne$$' in mu_playlist [ 0 ] :
  mu_playlist [ 0 ] = mu_playlist [ 0 ] . replace ( '$$LSPlayOnlyOne$$' , '' )
  import urlparse
  IIi1i1 = [ ]
  o0O0Ooo = 0
  O0o0oOooOoOo = xbmcgui . DialogProgress ( )
  O0o0oOooOoOo . create ( 'Progress' , 'Trying Multiple Links' )
  for IiIIIiI1I1 in mu_playlist :
   if 79 - 79: O0oO . iII111i / iII111i - O0oO * I1ii11iIi11i / I11i
   if '$$lsname=' in IiIIIiI1I1 :
    iI1iiIi1 = IiIIIiI1I1 . split ( '$$lsname=' ) [ 1 ] . split ( '&regexs' ) [ 0 ]
    IIi1i1 . append ( iI1iiIi1 )
    mu_playlist [ o0O0Ooo ] = IiIIIiI1I1 . split ( '$$lsname=' ) [ 0 ] + ( '&regexs' + IiIIIiI1I1 . split ( '&regexs' ) [ 1 ] if '&regexs' in IiIIIiI1I1 else '' )
   if '$nortv=' in IiIIIiI1I1 :
    iI1iiIi1 = IiIIIiI1I1 . split ( '$nortv=' ) [ 1 ] . split ( '&regexs' ) [ 0 ]
    IIi1i1 . append ( iI1iiIi1 )
    mu_playlist [ o0O0Ooo ] = IiIIIiI1I1 . split ( '$nortv=' ) [ 0 ] + ( '&regexs' + IiIIIiI1I1 . split ( '&regexs' ) [ 1 ] if '&regexs' in IiIIIiI1I1 else '' )
   else :
    iI1iiIi1 = urlparse . urlparse ( IiIIIiI1I1 ) . netloc
    if iI1iiIi1 == '' :
     IIi1i1 . append ( name )
    else :
     IIi1i1 . append ( iI1iiIi1 )
   iiii11I = o0O0Ooo
   o0O0Ooo += 1
   if 49 - 49: O0oO . OoO0O00
   IioOooOOo00ooO = IIi1i1 [ iiii11I ]
   if O0o0oOooOoOo . iscanceled ( ) : return
   O0o0oOooOoOo . update ( o0O0Ooo / len ( mu_playlist ) * 100 , "" , "Link#%d" % ( o0O0Ooo ) , IioOooOOo00ooO )
   print 'auto playnamexx' , IioOooOOo00ooO
   if "&mode=19" in mu_playlist [ iiii11I ] :
    if 71 - 71: IIII - I11i - IiII
    oOO00O = xbmcgui . ListItem ( IioOooOOo00ooO , iconImage = iiI )
    oOO00O . setInfo ( type = 'Video' , infoLabels = { 'Title' : IioOooOOo00ooO } )
    oOO00O . setProperty ( "IsPlayable" , "true" )
    O0OO0o0O00oO = oO0o0 ( mu_playlist [ iiii11I ] . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) )
    oOO00O . setPath ( O0OO0o0O00oO )
    if 81 - 81: oO0o0ooO0 / I1Ii111
    III1 = iiI1ii111 ( O0OO0o0O00oO , oOO00O )
   elif "$doregex" in mu_playlist [ iiii11I ] :
    if 24 - 24: iII111i / IIII / I1Ii111 % OOooOOo / Ii1I * O0oO
    iiIiIIi11I1 = mu_playlist [ iiii11I ] . split ( '&regexs=' )
    if 86 - 86: oooo . oOo0O0Ooo * I1Ii111
    o00O0OoO , oOOoo = O0iII1 ( iiIiIIi11I1 [ 1 ] , iiIiIIi11I1 [ 0 ] )
    ii1i11ii = o00O0OoO . replace ( ';' , '' )
    oOO00O = xbmcgui . ListItem ( IioOooOOo00ooO , iconImage = iiI )
    oOO00O . setInfo ( type = 'Video' , infoLabels = { 'Title' : IioOooOOo00ooO } )
    oOO00O . setProperty ( "IsPlayable" , "true" )
    oOO00O . setPath ( ii1i11ii )
    if 11 - 11: I1ii11iIi11i - O0OO0O0O
    III1 = iiI1ii111 ( ii1i11ii , oOO00O )
    if 77 - 77: I1ii11iIi11i . oo0 / oo % o00O0oo % o00O0oo
   else :
    o00O0OoO = mu_playlist [ iiii11I ]
    o00O0OoO = o00O0OoO . split ( '&regexs=' ) [ 0 ]
    oOO00O = xbmcgui . ListItem ( IioOooOOo00ooO , iconImage = iiI )
    oOO00O . setInfo ( type = 'Video' , infoLabels = { 'Title' : IioOooOOo00ooO } )
    oOO00O . setProperty ( "IsPlayable" , "true" )
    oOO00O . setPath ( o00O0OoO )
    if 65 - 65: I1ii11iIi11i * O0OO0O0O / ooOoO0o . IIII % I1ii11iIi11i
    III1 = iiI1ii111 ( o00O0OoO , oOO00O )
    print 'played' , III1
   print 'played' , III1
   if III1 : return
  return
 if i1I1Ii1iI1ii . getSetting ( 'ask_playlist_items' ) == 'true' and not queueVideo :
  import urlparse
  IIi1i1 = [ ]
  o0O0Ooo = 0
  print mu_playlist
  for IiIIIiI1I1 in mu_playlist :
   print IiIIIiI1I1
   if '$$lsname=' in IiIIIiI1I1 :
    iI1iiIi1 = IiIIIiI1I1 . split ( '$$lsname=' ) [ 1 ] . split ( '&regexs' ) [ 0 ]
    IIi1i1 . append ( iI1iiIi1 )
    mu_playlist [ o0O0Ooo ] = IiIIIiI1I1 . split ( '$$lsname=' ) [ 0 ] + ( '&regexs' + IiIIIiI1I1 . split ( '&regexs' ) [ 1 ] if '&regexs' in IiIIIiI1I1 else '' )
   if '$nortv=' in IiIIIiI1I1 :
    iI1iiIi1 = IiIIIiI1I1 . split ( '$nortv=' ) [ 1 ] . split ( '&regexs' ) [ 0 ]
    IIi1i1 . append ( iI1iiIi1 )
    mu_playlist [ o0O0Ooo ] = IiIIIiI1I1 . split ( '$nortv=' ) [ 0 ] + ( '&regexs' + IiIIIiI1I1 . split ( '&regexs' ) [ 1 ] if '&regexs' in IiIIIiI1I1 else '' )
   else :
    iI1iiIi1 = urlparse . urlparse ( IiIIIiI1I1 ) . netloc
    if iI1iiIi1 == '' :
     IIi1i1 . append ( name )
    else :
     IIi1i1 . append ( iI1iiIi1 )
     if 24 - 24: oO0o
   o0O0Ooo += 1
  iI1Ii11iIiI1 = xbmcgui . Dialog ( )
  iiii11I = iI1Ii11iIiI1 . select ( '[COLOR red]Flecha[/COLOR] [COLOR black]Negra[/COLOR] Escolha um link:' , IIi1i1 )
  if iiii11I >= 0 :
   IioOooOOo00ooO = IIi1i1 [ iiii11I ]
   print 'playnamexx' , IioOooOOo00ooO
   if "&mode=19" in mu_playlist [ iiii11I ] :
    if 99 - 99: IiII / oO0o0ooO0 / ooOoO0o
    oOO00O = xbmcgui . ListItem ( IioOooOOo00ooO , iconImage = iiI )
    oOO00O . setInfo ( type = 'Video' , infoLabels = { 'Title' : IioOooOOo00ooO } )
    oOO00O . setProperty ( "IsPlayable" , "true" )
    O0OO0o0O00oO = oO0o0 ( mu_playlist [ iiii11I ] . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) )
    oOO00O . setPath ( O0OO0o0O00oO )
    xbmc . Player ( ) . play ( O0OO0o0O00oO , oOO00O )
   elif "$doregex" in mu_playlist [ iiii11I ] :
    if 84 - 84: oO0o / oooo
    iiIiIIi11I1 = mu_playlist [ iiii11I ] . split ( '&regexs=' )
    if 33 - 33: oo / IIII - oo . I1ii11iIi11i
    o00O0OoO , oOOoo = O0iII1 ( iiIiIIi11I1 [ 1 ] , iiIiIIi11I1 [ 0 ] )
    ii1i11ii = o00O0OoO . replace ( ';' , '' )
    oOO00O = xbmcgui . ListItem ( IioOooOOo00ooO , iconImage = iiI )
    oOO00O . setInfo ( type = 'Video' , infoLabels = { 'Title' : IioOooOOo00ooO } )
    oOO00O . setProperty ( "IsPlayable" , "true" )
    oOO00O . setPath ( ii1i11ii )
    xbmc . Player ( ) . play ( ii1i11ii , oOO00O )
    if 18 - 18: I1ii11iIi11i / O0OO0O0O + o00O0oo
   else :
    o00O0OoO = mu_playlist [ iiii11I ]
    o00O0OoO = o00O0OoO . split ( '&regexs=' ) [ 0 ]
    oOO00O = xbmcgui . ListItem ( IioOooOOo00ooO , iconImage = iiI )
    oOO00O . setInfo ( type = 'Video' , infoLabels = { 'Title' : IioOooOOo00ooO } )
    oOO00O . setProperty ( "IsPlayable" , "true" )
    oOO00O . setPath ( o00O0OoO )
    xbmc . Player ( ) . play ( o00O0OoO , oOO00O )
 elif not queueVideo :
  if 65 - 65: oo . Ii1I / O0oO
  OooOoOo . clear ( )
  iIOO0O000 = 0
  for IiIIIiI1I1 in mu_playlist :
   iIOO0O000 += 1
   I1i1I11111iI1 = xbmcgui . ListItem ( '%s) %s' % ( str ( iIOO0O000 ) , name ) )
   if 32 - 32: oOo0O0Ooo + Ii1I - iII111i + Ii1I / oo * iII111i
   try :
    if "$doregex" in IiIIIiI1I1 :
     iiIiIIi11I1 = IiIIIiI1I1 . split ( '&regexs=' )
     if 90 - 90: ooOoO0o % iII111i
     o00O0OoO , oOOoo = O0iII1 ( iiIiIIi11I1 [ 1 ] , iiIiIIi11I1 [ 0 ] )
    elif "&mode=19" in IiIIIiI1I1 :
     o00O0OoO = oO0o0 ( IiIIIiI1I1 . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) )
    if o00O0OoO :
     OooOoOo . add ( o00O0OoO , I1i1I11111iI1 )
    else :
     raise
   except Exception :
    OooOoOo . add ( IiIIIiI1I1 , I1i1I11111iI1 )
    pass
    if 6 - 6: II111iiii / oo0 / IIII
  xbmc . executebuiltin ( 'playlist.playoffset(video,0)' )
 else :
  if 60 - 60: oOo0O0Ooo % iII111i / I11i % iII111i * oo0 / o00O0oo
  oOO0oo = xbmcgui . ListItem ( name )
  OooOoOo . add ( mu_playlist , oOO0oo )
  if 34 - 34: IIII - IiII
def IIIiIi1iiI ( name , url ) :
 if 15 - 15: Ii1I . o00O0oo
 if i1I1Ii1iI1ii . getSetting ( 'save_location' ) == "" :
  xbmc . executebuiltin ( "XBMC.Notification('Choose a location to save files.',15000," + oOo0oooo00o + ")" )
  i1I1Ii1iI1ii . openSettings ( )
 iIOO0OOoooo0o = { 'url' : url , 'download_path' : i1I1Ii1iI1ii . getSetting ( 'save_location' ) }
 downloader . download ( name , iIOO0OOoooo0o )
 iI1Ii11iIiI1 = xbmcgui . Dialog ( )
 i1iIiIi1I = iI1Ii11iIiI1 . yesno ( 'Do you want to add this file as a source?' )
 if i1iIiIi1I :
  I11I11i1I ( os . path . join ( i1I1Ii1iI1ii . getSetting ( 'save_location' ) , name ) )
  if 94 - 94: I1Ii111 . oOo0O0Ooo
def oooOoo0OoOO0000 ( url , title , media_type = 'video' ) :
 if 2 - 2: ooOoO0o * Ii1I * II111iiii
 if 73 - 73: OOooOOo + I1ii11iIi11i
 import youtubedl
 if not url == '' :
  if media_type == 'audio' :
   youtubedl . single_YD ( url , download = True , audio = True )
  else :
   youtubedl . single_YD ( url , download = True )
 elif xbmc . Player ( ) . isPlaying ( ) == True :
  import YDStreamExtractor
  if YDStreamExtractor . isDownloading ( ) == True :
   if 61 - 61: oooo
   YDStreamExtractor . manageDownloads ( )
  else :
   iiI1 = xbmc . Player ( ) . getPlayingFile ( )
   if 50 - 50: O0oO * OOooOOo + Ii1I - oo0 + I1ii11iIi11i * Ii1I
   iiI1 = iiI1 . split ( '|User-Agent=' ) [ 0 ]
   I1i1I11111iI1 = { 'url' : iiI1 , 'title' : title , 'media_type' : media_type }
   youtubedl . single_YD ( '' , download = True , dl_info = I1i1I11111iI1 )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(DOWNLOAD,First Play [COLOR yellow]WHILE playing download[/COLOR] ,10000)" )
  if 20 - 20: IIII / I11i % OOooOOo
  if 69 - 69: IIII - oo % o00O0oo . IiII - IiII
def o0oO00o ( string ) :
 if isinstance ( string , basestring ) :
  if isinstance ( string , unicode ) :
   string = string . encode ( 'ascii' , 'ignore' )
 return string
def OOO0OoO0oo0OO ( string , encoding = 'utf-8' ) :
 if isinstance ( string , basestring ) :
  if not isinstance ( string , unicode ) :
   string = unicode ( string , encoding , 'ignore' )
 return string
def i1iI1Ii11Ii1 ( s ) : return "" . join ( filter ( lambda o0OoO0oo0O0o : ord ( o0OoO0oo0O0o ) < 128 , s ) )
if 6 - 6: OoO0O00 % IIII
def I1iiIiIII ( command ) :
 iI1 = ''
 try :
  iI1 = xbmc . executeJSONRPC ( OOO0OoO0oo0OO ( command ) )
 except UnicodeEncodeError :
  iI1 = xbmc . executeJSONRPC ( o0oO00o ( command ) )
  if 68 - 68: O0OO0O0O
 return OOO0OoO0oo0OO ( iI1 )
 if 76 - 76: Ii1I
def ooO000OO ( url , give_me_result = None , playlist = False ) :
 if 'audio' in url :
  i111IIiIiiI1 = OOO0OoO0oo0OO ( '{"jsonrpc":"2.0","method":"Files.GetDirectory","params": {"directory":"%s","media":"video", "properties": ["title", "album", "artist", "duration","thumbnail", "year"]}, "id": 1}' ) % url
 else :
  i111IIiIiiI1 = OOO0OoO0oo0OO ( '{"jsonrpc":"2.0","method":"Files.GetDirectory","params":{"directory":"%s","media":"video","properties":[ "plot","playcount","director", "genre","votes","duration","trailer","premiered","thumbnail","title","year","dateadded","fanart","rating","season","episode","studio","mpaa"]},"id":1}' ) % url
 OO0 = json . loads ( I1iiIiIII ( i111IIiIiiI1 ) )
 if 28 - 28: I1ii11iIi11i % IiII - oO0o + O0oO / O0oO
 if give_me_result :
  return OO0
 if OO0 . has_key ( 'error' ) :
  return
 else :
  if 82 - 82: I1ii11iIi11i
  for IiIIIiI1I1 in OO0 [ 'result' ] [ 'files' ] :
   IIIII = { }
   url = IiIIIiI1I1 [ 'file' ]
   oO000Oo000 = i1iI1Ii11Ii1 ( IiIIIiI1I1 [ 'label' ] )
   i111IiI1I = i1iI1Ii11Ii1 ( IiIIIiI1I1 [ 'thumbnail' ] )
   iiIiIIi = i1iI1Ii11Ii1 ( IiIIIiI1I1 [ 'fanart' ] )
   IIIII = dict ( ( k , v ) for k , v in IiIIIiI1I1 . iteritems ( ) if not v == '0' or not v == - 1 or v == '' )
   IIIII . pop ( "file" , None )
   if IiIIIiI1I1 [ 'filetype' ] == 'file' :
    if playlist :
     II111I1 ( oO000Oo000 , url , queueVideo = '1' )
     continue
    else :
     O000OOOOOo ( url , oO000Oo000 , i111IiI1I , iiIiIIi , '' , '' , '' , '' , None , '' , total = len ( OO0 [ 'result' ] [ 'files' ] ) , allinfo = IIIII )
     if 9 - 9: IIII * oO0o0ooO0 * IIII
     if IiIIIiI1I1 [ 'type' ] and IiIIIiI1I1 [ 'type' ] == 'tvshow' :
      xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'tvshows' )
     elif IiIIIiI1I1 [ 'episode' ] > 0 :
      xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'episodes' )
      if 74 - 74: oooo / I11i
   else :
    OoO000 ( oO000Oo000 , url , 53 , i111IiI1I , iiIiIIi , '' , '' , '' , '' , allinfo = IIIII )
  xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if 58 - 58: oooo - oOo0O0Ooo % I11i % II111iiii * oooo + IiII
def O000OOOOOo ( url , name , iconimage , fanart , description , genre , date , showcontext , playlist , regexs , total , setCookie = "" , allinfo = { } ) :
 if 25 - 25: IiII % O0OO0O0O
 i1IiIiiiIIIIi = [ ]
 oo0O0 = i1I1Ii1iI1ii . getSetting ( 'parentalblocked' )
 oo0O0 = oo0O0 == "true"
 ooOo00 = i1I1Ii1iI1ii . getSetting ( 'parentalblockedpin' )
 if 44 - 44: IIII . ooOoO0o * OoO0O00 / oO0o0ooO0 + oooo
 if len ( ooOo00 ) > 0 :
  if oo0O0 :
   i1IiIiiiIIIIi . append ( ( 'Disable Parental Block' , 'XBMC.RunPlugin(%s?mode=55&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  else :
   i1IiIiiiIIIIi . append ( ( 'Enable Parental Block' , 'XBMC.RunPlugin(%s?mode=56&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
   if 14 - 14: O0OO0O0O % oO0o0ooO0 % ooOoO0o * iII111i
 try :
  name = name . encode ( 'utf-8' )
 except : pass
 OOOoo0OO = True
 o0OOO00ooo = False
 if regexs :
  I1iI11IiiI11i = '17'
  if 'listrepeat' in regexs :
   o0OOO00ooo = True
   if 37 - 37: I11i % oo - I11i + oooo + IIII
   if 84 - 84: iII111i + IiII . o00O0oo
   if 71 - 71: O0oO / O0oO . OOooOOo % o00O0oo
 elif ( any ( x in url for x in oOOo ) and url . startswith ( 'http' ) ) or url . endswith ( '&mode=19' ) :
  url = url . replace ( '&mode=19' , '' )
  I1iI11IiiI11i = '19'
  i1IiIiiiIIIIi . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . endswith ( '&mode=18' ) :
  url = url . replace ( '&mode=18' , '' )
  I1iI11IiiI11i = '18'
  i1IiIiiiIIIIi . append ( ( '[COLOR white]!!Download!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=23&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  if i1I1Ii1iI1ii . getSetting ( 'dlaudioonly' ) == 'true' :
   i1IiIiiiIIIIi . append ( ( '!!Download [COLOR seablue]Audio!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . startswith ( 'magnet:?xt=' ) :
  if '&' in url and not '&amp;' in url :
   url = url . replace ( '&' , '&amp;' )
  url = 'plugin://plugin.video.pulsar/play?uri=' + url
  I1iI11IiiI11i = '12'
 else :
  I1iI11IiiI11i = '12'
  i1IiIiiiIIIIi . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 if 'plugin://plugin.video.youtube/play/?video_id=' in url :
  I1i1i1 = url . replace ( 'plugin://plugin.video.youtube/play/?video_id=' , 'https://www.youtube.com/watch?v=' )
  i1IiIiiiIIIIi . append ( ( '!!Download [COLOR blue]Audio!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( I1i1i1 ) , urllib . quote_plus ( name ) ) ) )
 ii11I = sys . argv [ 0 ] + "?"
 O0i1I11I = False
 if playlist :
  if i1I1Ii1iI1ii . getSetting ( 'add_playlist' ) == "false" and '$$LSPlayOnlyOne$$' not in playlist [ 0 ] :
   ii11I += "url=" + urllib . quote_plus ( url ) + "&mode=" + I1iI11IiiI11i
  else :
   ii11I += "mode=13&name=%s&playlist=%s" % ( urllib . quote_plus ( name ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) )
   name = name + '[COLOR blue][B] (' + str ( len ( playlist ) ) + ' OPÇÕES )[/B][/COLOR]'
   O0i1I11I = True
 else :
  ii11I += "url=" + urllib . quote_plus ( url ) + "&mode=" + I1iI11IiiI11i
 if regexs :
  ii11I += "&regexs=" + regexs
 if not setCookie == '' :
  ii11I += "&setCookie=" + urllib . quote_plus ( setCookie )
  if 34 - 34: ooOoO0o * I11i + IiII / oO0o0ooO0 / I1ii11iIi11i
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 oOO00O = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 if 14 - 14: o00O0oo - I1Ii111 * II111iiii + IiII . OoO0O00
 if allinfo == None or len ( allinfo ) < 1 :
  oOO00O . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date } )
 else :
  oOO00O . setInfo ( type = "Video" , infoLabels = allinfo )
 oOO00O . setProperty ( "Fanart_Image" , fanart )
 if 15 - 15: I1Ii111 % oo0
 if ( not O0i1I11I ) and not any ( x in url for x in O0 ) and not '$PLAYERPROXY$=' in url :
  if regexs :
   if 73 - 73: O0oO % O0oO . o00O0oo + IIII
   if '$pyFunction:playmedia(' not in urllib . unquote_plus ( regexs ) and 'notplayable' not in urllib . unquote_plus ( regexs ) and 'listrepeat' not in urllib . unquote_plus ( regexs ) :
    if 10 - 10: O0OO0O0O / IiII * O0oO - oO0o - oo . OOooOOo
    oOO00O . setProperty ( 'IsPlayable' , 'true' )
  else :
   oOO00O . setProperty ( 'IsPlayable' , 'true' )
 else :
  o0oOo0Ooo0O ( 'NOT setting isplayable' + url )
 if not playlist is None :
  if i1I1Ii1iI1ii . getSetting ( 'add_playlist' ) == "false" :
   OO00O00Oo = name . split ( ') ' ) [ 1 ]
   ooO = [
 ( 'Play ' + OO00O00Oo + ' PlayList' , 'XBMC.RunPlugin(%s?mode=13&name=%s&playlist=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( OO00O00Oo ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) ) )
 ]
   oOO00O . addContextMenuItems ( ooO )
   if 67 - 67: Ii1I . OoO0O00 - ooOoO0o % II111iiii
 OOOoo0OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii11I , listitem = oOO00O , totalItems = total , isFolder = o0OOO00ooo )
 if 49 - 49: Ii1I + O0OO0O0O . ooOoO0o * II111iiii
 return OOOoo0OO
 if 82 - 82: Ii1I
def OOO00o0 ( url , name , iconimage , setresolved = True ) :
 if setresolved :
  oOO00O = xbmcgui . ListItem ( name , iconImage = iconimage )
  oOO00O . setInfo ( type = 'Video' , infoLabels = { 'Title' : name } )
  oOO00O . setProperty ( "IsPlayable" , "true" )
  oOO00O . setPath ( str ( url ) )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOO00O )
 else :
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + url + ')' )
  if 97 - 97: Ii1I / Ii1I / oooo % oo . Ii1I . oO0o0ooO0
  if 4 - 4: I1ii11iIi11i - oO0o - oo0 * IIII / ooOoO0o - IiII
  if 45 - 45: I11i % I1ii11iIi11i * oo - O0OO0O0O
def oOo0OOoO0 ( link ) :
 o00O0OoO = urllib . urlopen ( link )
 oo00 = o00O0OoO . read ( )
 o00O0OoO . close ( )
 ooOooO = oo00 . split ( "Jetzt" )
 ooIi111iII = ooOooO [ 1 ] . split ( 'programm/detail.php?const_id=' )
 Oo0OoOo = ooIi111iII [ 1 ] . split ( '<br /><a href="/' )
 iiIIIi1i = Oo0OoOo [ 0 ] [ 40 : len ( Oo0OoOo [ 0 ] ) ]
 iIi1i1i1II11I = ooIi111iII [ 2 ] . split ( "</a></p></div>" )
 O0OO = iIi1i1i1II11I [ 0 ] [ 17 : len ( iIi1i1i1II11I [ 0 ] ) ]
 O0OO = O0OO . encode ( 'utf-8' )
 return "  - " + O0OO + " - " + iiIIIi1i
 if 75 - 75: Ii1I - OOooOOo * oo0 . II111iiii - I1ii11iIi11i . I1Ii111
 if 6 - 6: I1Ii111 * iII111i / II111iiii % ooOoO0o * I11i
def Ooo0OOoOoO0 ( url , regex ) :
 iI1 = i11IIIiIiIi ( url )
 try :
  iIOO0O000 = re . findall ( regex , iI1 ) [ 0 ]
  return iIOO0O000
 except :
  o0oOo0Ooo0O ( 'regex failed' )
  o0oOo0Ooo0O ( regex )
  return
  if 28 - 28: oO0o0ooO0 * oOo0O0Ooo % oO0o0ooO0
  if 95 - 95: O0OO0O0O / I1Ii111 . IIII
  if 17 - 17: I1Ii111
def o0OO0OO000OO ( d , root = "root" , nested = 0 ) :
 if 92 - 92: I1Ii111 % oo % O0oO % oO0o0ooO0 % I11i
 O00Ooo0O0OOOo = lambda o0oooo0O : '<' + o0oooo0O + '>'
 iI1iIIIIIiIi1 = lambda o0oooo0O : '</' + o0oooo0O + '>\n'
 if 19 - 19: OOooOOo . I11i . II111iiii
 iIi = lambda OOOO , ii1iI1i : ii1iI1i + O00Ooo0O0OOOo ( i1iiiI ) + str ( OOOO ) + iI1iIIIIIiIi1 ( i1iiiI )
 ii1iI1i = O00Ooo0O0OOOo ( root ) + '\n' if root else ""
 if 75 - 75: II111iiii . IiII + oO0o / ooOoO0o - oOo0O0Ooo % ooOoO0o
 for i1iiiI , O0OooooO0o0O0 in d . iteritems ( ) :
  oO0oo = type ( O0OooooO0o0O0 )
  if nested == 0 : i1iiiI = 'regex'
  if oO0oo is list :
   for OOOO in O0OooooO0o0O0 :
    OOOO = escape ( OOOO )
    ii1iI1i = iIi ( OOOO , ii1iI1i )
    if 52 - 52: oO0o0ooO0 % O0oO
  if oO0oo is dict :
   ii1iI1i = iIi ( '\n' + o0OO0OO000OO ( O0OooooO0o0O0 , None , nested + 1 ) , ii1iI1i )
  if oO0oo is not list and oO0oo is not dict :
   if not O0OooooO0o0O0 is None : O0OooooO0o0O0 = escape ( O0OooooO0o0O0 )
   if 25 - 25: I1Ii111 / I1Ii111 % II111iiii - Ii1I * iII111i
   if O0OooooO0o0O0 is None :
    ii1iI1i = iIi ( O0OooooO0o0O0 , ii1iI1i )
   else :
    if 23 - 23: oo0
    ii1iI1i = iIi ( O0OooooO0o0O0 . encode ( "utf-8" ) , ii1iI1i )
    if 100 - 100: iII111i + O0OO0O0O . oOo0O0Ooo + oo - OOooOOo + I11i
 ii1iI1i += iI1iIIIIIiIi1 ( root ) if root else ""
 if 65 - 65: OoO0O00 / I1ii11iIi11i
 return ii1iI1i
xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
if 42 - 42: oo0 . O0OO0O0O
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_UNSORTED )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_LABEL )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_DATE )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_GENRE )
except :
 pass
 if 75 - 75: IIII + oooo
iIOO0OOoooo0o = I1i1II1 ( )
if 19 - 19: oOo0O0Ooo + oo0 . oO0o0ooO0 - I1Ii111 / ooOoO0o + I11i
o00O0OoO = None
oO000Oo000 = None
I1iI11IiiI11i = None
OooOoOo = None
iiI = None
iiIiIIi = oO0o0o0ooO0oO
OooOoOo = None
II1i = None
oOooOOOoOo = None
if 75 - 75: Ii1I
try :
 o00O0OoO = urllib . unquote_plus ( iIOO0OOoooo0o [ "url" ] ) . decode ( 'utf-8' )
except :
 pass
try :
 oO000Oo000 = urllib . unquote_plus ( iIOO0OOoooo0o [ "name" ] )
except :
 pass
try :
 iiI = urllib . unquote_plus ( iIOO0OOoooo0o [ "iconimage" ] )
except :
 pass
try :
 iiIiIIi = urllib . unquote_plus ( iIOO0OOoooo0o [ "fanart" ] )
except :
 pass
try :
 I1iI11IiiI11i = int ( iIOO0OOoooo0o [ "mode" ] )
except :
 pass
try :
 OooOoOo = eval ( urllib . unquote_plus ( iIOO0OOoooo0o [ "playlist" ] ) . replace ( '||' , ',' ) )
except :
 pass
try :
 II1i = int ( iIOO0OOoooo0o [ "fav_mode" ] )
except :
 pass
try :
 oOooOOOoOo = iIOO0OOoooo0o [ "regexs" ]
except :
 pass
O00o = ''
try :
 O00o = urllib . unquote_plus ( iIOO0OOoooo0o [ "playitem" ] )
except :
 pass
 if 55 - 55: O0oO % I1Ii111 / oo0
o0oOo0Ooo0O ( "Mode: " + str ( I1iI11IiiI11i ) )
if 20 - 20: oO0o0ooO0 / IIII * oO0o0ooO0 * oO0o
if 72 - 72: oO0o . I11i * Ii1I . oooo % Ii1I . ooOoO0o
if not o00O0OoO is None :
 o0oOo0Ooo0O ( "URL: " + str ( o00O0OoO . encode ( 'utf-8' ) ) )
o0oOo0Ooo0O ( "Name: " + str ( oO000Oo000 ) )
if 70 - 70: IiII + O0oO * ooOoO0o . ooOoO0o + oO0o
if not O00o == '' :
 ii1Iii1 = i11Iiii ( '' , data = O00o )
 oO000Oo000 , o00O0OoO , oOooOOOoOo = O0o0O00Oo0o0 ( ii1Iii1 , None , dontLink = True )
 I1iI11IiiI11i = 117
 if 28 - 28: oo . IiII
if I1iI11IiiI11i == None :
 if i1I1Ii1iI1ii . getSetting ( "sourcefile" ) == "true" :
  o0oOo0Ooo0O ( "FileSources" )
  OooO0OO ( )
 else :
  o0oOo0Ooo0O ( "PastebinLinks" )
  oo0o ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 88 - 88: I1Ii111 + oOo0O0Ooo - I1Ii111 / II111iiii - oo0
elif I1iI11IiiI11i == 1 :
 o0oOo0Ooo0O ( "getData" )
 iI1 = None
 if 24 - 24: oooo
 if oOooOOOoOo and len ( oOooOOOoOo ) > 0 :
  iI1 , oOOoo = O0iII1 ( oOooOOOoOo , o00O0OoO )
  if 89 - 89: ooOoO0o / oo - I11i % oOo0O0Ooo . I1ii11iIi11i - O0OO0O0O
  if 71 - 71: oO0o % oOo0O0Ooo - o00O0oo . o00O0oo
  if iI1 . startswith ( 'http' ) or iI1 . startswith ( 'smb' ) or iI1 . startswith ( 'nfs' ) or iI1 . startswith ( '/' ) :
   o00O0OoO = iI1
   iI1 = None
   if 22 - 22: O0oO / O0oO - ooOoO0o % I1Ii111 . IiII + oO0o0ooO0
   if 64 - 64: oo % Ii1I / ooOoO0o % II111iiii
 O0o0Oo ( o00O0OoO , iiIiIIi , iI1 )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 24 - 24: IIII + II111iiii . oO0o0ooO0 / OOooOOo / I1Ii111
elif I1iI11IiiI11i == 2 :
 o0oOo0Ooo0O ( "getChannelItems" )
 Iiii1i1 ( oO000Oo000 , o00O0OoO , iiIiIIi )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 65 - 65: II111iiii
elif I1iI11IiiI11i == 3 :
 o0oOo0Ooo0O ( "getSubChannelItems" )
 O0oOOO0ooOOO0OOO ( oO000Oo000 , o00O0OoO , iiIiIIi )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 18 - 18: O0OO0O0O - oo . IIII
elif I1iI11IiiI11i == 7 :
 o0oOo0Ooo0O ( "addSource" )
 I11I11i1I ( o00O0OoO )
 if 98 - 98: I11i
elif I1iI11IiiI11i == 8 :
 o0oOo0Ooo0O ( "rmSource" )
 Iii111II ( oO000Oo000 )
 if 73 - 73: I1ii11iIi11i - o00O0oo . iII111i % oo . O0OO0O0O
elif I1iI11IiiI11i == 9 :
 o0oOo0Ooo0O ( "download_file" )
 IIIiIi1iiI ( oO000Oo000 , o00O0OoO )
 if 15 - 15: O0oO . oooo * oOo0O0Ooo % I1Ii111
elif I1iI11IiiI11i == 10 :
 o0oOo0Ooo0O ( "getCommunitySources" )
 getCommunitySources ( )
elif I1iI11IiiI11i == 11 :
 o0oOo0Ooo0O ( "getMyData" )
 iI1 = None
 if 21 - 21: oO0o - oOo0O0Ooo . II111iiii
 if oOooOOOoOo and len ( oOooOOOoOo ) > 0 :
  iI1 , oOOoo = O0iII1 ( oOooOOOoOo , o00O0OoO )
  if 6 - 6: oooo - oooo % I11i / oooo * IIII
  if 3 - 3: IiII . oO0o0ooO0 / I1ii11iIi11i
  if iI1 . startswith ( 'http' ) or iI1 . startswith ( 'smb' ) or iI1 . startswith ( 'nfs' ) or iI1 . startswith ( '/' ) :
   o00O0OoO = iI1
   iI1 = None
   if 89 - 89: II111iiii . oooo . I1ii11iIi11i * oooo - IIII
   if 92 - 92: II111iiii - Ii1I - II111iiii % oOo0O0Ooo % oOo0O0Ooo % oooo
 o0 ( o00O0OoO , iiIiIIi , iI1 )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I1iI11IiiI11i == 12 :
 o0oOo0Ooo0O ( "setResolvedUrl" )
 if not o00O0OoO . startswith ( "plugin://plugin" ) or not any ( x in o00O0OoO for x in O0 ) :
  iIOO0O000 = xbmcgui . ListItem ( path = o00O0OoO )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iIOO0O000 )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + o00O0OoO + ')' )
elif I1iI11IiiI11i == 13 :
 o0oOo0Ooo0O ( "play_playlist" )
 II111I1 ( oO000Oo000 , OooOoOo )
 if 92 - 92: o00O0oo * O0OO0O0O % IIII . oooo
elif I1iI11IiiI11i == 17 :
 o0oOo0Ooo0O ( "getRegexParsed" )
 o00O0OoO , oOOoo = O0iII1 ( oOooOOOoOo , o00O0OoO )
 if o00O0OoO :
  OOO00o0 ( o00O0OoO , oO000Oo000 , iiI , oOOoo )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(Failed to extract regex. - " + "this" + ",4000," + oOo0oooo00o + ")" )
elif I1iI11IiiI11i == 18 :
 o0oOo0Ooo0O ( "youtubedl" )
 try :
  import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000," ")" )
 i1iIi = youtubedl . single_YD ( o00O0OoO )
 OOO00o0 ( i1iIi , oO000Oo000 , iiI )
elif I1iI11IiiI11i == 19 :
 o0oOo0Ooo0O ( "Genesiscommonresolvers" )
 OOO00o0 ( oO0o0 ( o00O0OoO ) , oO000Oo000 , iiI , True )
elif I1iI11IiiI11i == 21 :
 o0oOo0Ooo0O ( "download current file using youtube-dl service" )
 oooOoo0OoOO0000 ( '' , oO000Oo000 , 'video' )
elif I1iI11IiiI11i == 23 :
 o0oOo0Ooo0O ( "get info then download" )
 oooOoo0OoOO0000 ( o00O0OoO , oO000Oo000 , 'video' )
elif I1iI11IiiI11i == 24 :
 o0oOo0Ooo0O ( "Audio only youtube download" )
 oooOoo0OoOO0000 ( o00O0OoO , oO000Oo000 , 'audio' )
elif I1iI11IiiI11i == 25 :
 OOiIiIIi1 ( oO000Oo000 , o00O0OoO , iiI , iiIiIIi )
elif I1iI11IiiI11i == 55 :
 o0oOo0Ooo0O ( "enabled lock" )
 ooOo00 = i1I1Ii1iI1ii . getSetting ( 'parentalblockedpin' )
 i1 = xbmc . Keyboard ( '' , 'Enter Pin' )
 i1 . doModal ( )
 if not ( i1 . isConfirmed ( ) == False ) :
  IiIiiI = i1 . getText ( )
  if IiIiiI == ooOo00 :
   i1I1Ii1iI1ii . setSetting ( 'parentalblocked' , "false" )
   xbmc . executebuiltin ( "XBMC.Notification(Controlo Parental desativado,5000," + oOo0oooo00o + ")" )
  else :
   xbmc . executebuiltin ( "XBMC.Notification(Pin errado??,5000," + oOo0oooo00o + ")" )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I1iI11IiiI11i == 56 :
 o0oOo0Ooo0O ( "disable lock" )
 i1I1Ii1iI1ii . setSetting ( 'parentalblocked' , "true" )
 xbmc . executebuiltin ( "XBMC.Notification(Controlo Parental ativado,5000," + oOo0oooo00o + ")" )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif I1iI11IiiI11i == 53 :
 o0oOo0Ooo0O ( "Requesting JSON-RPC Items" )
 ooO000OO ( o00O0OoO )
 if 66 - 66: I1Ii111 + ooOoO0o
elif I1iI11IiiI11i == 100 :
 xbmc . Player ( ) . play ( mp3 )
if not oo000 == None :
 print 'setting view mode'
 xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo000 ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
