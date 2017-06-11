# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import xml . etree . ElementTree as ElementTree
import urlresolver
import httplib
import requests
import urlparse
import shutil
import binascii
import subprocess
import urllib2 , urllib , glob , traceback
import re
import plugintools
import zipfile
import time
import ntpath
import cookielib
import buggalo
import extract
import downloader
from urllib2 import urlopen
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup , BeautifulSOAP
from cookielib import CookieJar
from addon . common . addon import Addon
from addon . common . net import Net
from datetime import date , datetime , timedelta
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = 'plugin.video.Xhoans'
oo = 'plugin.video.Xhoans'
i1iII1IiiIiI1 = "0.0.8"
iIiiiI1IiI1I1 = xbmc . translatePath ( 'special://home/addons/' )
o0OoOoOO00 = base64 . decodestring
I11i = datetime . now ( )
O0O = xbmc . translatePath ( 'special://logpath/' )
Oo = xbmc . translatePath ( 'special://home/addonsbroke/' )
I1ii11iIi11i = xbmcaddon . Addon ( id = oo )
I1IiI = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
o0OOO = 'plugin.video.Xhoans'
iIiiiI = xbmcgui . DialogProgress ( )
Iii1ii1II11i = "Xhoans IPTV"
iI111iI = Net ( )
IiII = xbmc . translatePath ( 'special://home/' )
o0OoOoOO00 = base64 . decodestring
iI1Ii11111iIi = xbmc . translatePath ( 'special://profile/' )
i1i1II = [ 'xbmc.log' , 'xbmc.old.log' , 'kodi.log' , 'kodi.old.log' , 'spmc.log' , 'spmc.old.log' , 'tvmc.log' , 'tvmc.old.log' ]
O0oo0OO0 = os . path . join ( IiII , 'userdata' )
I1i1iiI1 = os . path . join ( O0oo0OO0 , 'addon_data' , o0OO00 )
iiIIIII1i1iI = os . path . join ( iIiiiI1IiI1I1 , 'packages' )
o0oO0 = I1ii11iIi11i . getSetting ( 'User' )
oo00 = os . path . join ( I1i1iiI1 , 'wizard.log' )
o00 = I1ii11iIi11i . getSetting ( 'Pass' )
Oo0oO0ooo = I1ii11iIi11i . getSetting ( 'AdultPass' )
o0oOoO00o = ( o0OoOoOO00 ( 'aHR0cDovL2dlbmlldHYuY28udWsveGhvYW4v' ) )
i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oo , 'icon.png' ) )
oOOoo00O0O = o0oOoO00o + ( o0OoOoOO00 ( 'YXJ0Lw==' ) )
i1111 = o0oOoO00o + ( o0OoOoOO00 ( 'cmVzZWwvd2l6LnhtbA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
i11 = o0oOoO00o + ( o0OoOoOO00 ( 'YXBrLnR4dA==' ) )
I11 = ( o0OoOoOO00 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwLw==' ) )
Oo0o0000o0o0 = 'WEBSITE'
oOo0oooo00o = ( o0OoOoOO00 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
oO0o0o0ooO0oO = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.Xhoans' )
oo0o0O00 = xbmc . translatePath ( 'special://thumbnails' ) ;
oO = "Xhoans IPTV"
i1iiIIiiI111 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oo , 'fanart.jpg' ) )
oooOOOOO = I1ii11iIi11i . getLocalizedString
i1iiIII111ii = CookieJar ( )
i1iIIi1 = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( i1iiIII111ii ) )
i1iIIi1 . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
ii11iIi1I = int ( sys . argv [ 1 ] )
iI111I11I1I1 = xbmc . translatePath ( I1ii11iIi11i . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
O0oo0OO0 = xbmc . translatePath ( 'special://home/userdata/' )
OOooO0OOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
iIii1 = oO0o0o0ooO0oO + '/addons.ini'
oOOoO0 = xbmcgui . Dialog ( )
if 59 - 59: oOOO0OOooOoO0Oo * II + IIi - iI11iiiI1II + O0oooo0Oo00
if 17 - 17: Iiii11I1i1Ii1 % o0OOOOO00o0O0 * Ii1III1i11i1i % Ii1ii1
if 35 - 35: ii1I11II1ii1i % I1i1iii - IiiI11Iiiii / I1I1i / IIIii1I1 * iiiIi1i1I
def oOO00oOO ( ) :
 OoOo ( )
 iI ( '[COLORsteelblue]Live Lists[/COLOR]' , '' , 9 , oOOoo00O0O + '1.png' , i1iiIIiiI111 , '' )
 iI ( '[COLORsteelblue]Movies (External Source)[/COLOR]' , o0OoOoOO00 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvTW92aWVzL01vdmllcy5waHA=' ) , 21 , oOOoo00O0O + '2.png' , i1iiIIiiI111 , '' )
 iI ( '[COLORsteelblue]World Radio (External Source)[/COLOR]' , '' , 50 , oOOoo00O0O + '3.png' , i1iiIIiiI111 , '' )
 if 60 - 60: ii1I11II1ii1i / ii1I11II1ii1i
 iI ( '[COLORsteelblue]Maintenance[/COLOR]' , '' , 5 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 iI ( '[COLORsteelblue]APK Installer[/COLOR]' , '' , 60001 , oOOoo00O0O + '5.png' , i1iiIIiiI111 , '' )
 iI ( '[COLORsteelblue]Open Addon Settings[/COLOR]' , '' , 18 , oOOoo00O0O + '6.png' , i1iiIIiiI111 , '' )
 if 46 - 46: I1i1iii * Ii1ii1 - iI11iiiI1II * Ii1III1i11i1i - IIIii1I1
def oo0 ( ) :
 iI ( '[COLORsteelblue]My Account[/COLOR]' , '' , 10 , oOOoo00O0O + '7.png' , i1iiIIiiI111 , '' )
 iI ( '[COLORsteelblue]Channel Lists[/COLOR]' , '' , 16 , oOOoo00O0O + '1.png' , i1iiIIiiI111 , '' )
 iI ( '[COLORsteelblue]CatchUp Tv[/COLOR]' , '' , 90026 , oOOoo00O0O + 'catchup.png' , i1iiIIiiI111 , '' )
 iI ( '[COLORsteelblue]Live Sport[/COLOR]' , ( o0OoOoOO00 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 22 , oOOoo00O0O + '9.png' , i1iiIIiiI111 , '' )
 iI ( '[COLORsteelblue]VOD Lists[/COLOR]' , '' , 40 , oOOoo00O0O + '10.png' , i1iiIIiiI111 , '' )
 if 57 - 57: Ii1ii1 . Ii1ii1
def OooOooo ( ) :
 O000oo0O = OOOO ( o0OoOoOO00 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 i11i1 = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( O000oo0O )
 for IIIii1II1II , i1I1iI in i11i1 :
  iI ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , 'http://www.listenlive.eu/' + IIIii1II1II , 51 , oOOoo00O0O + '3.png' , '' , '' )
def oo0OooOOo0 ( url ) :
 O000oo0O = OOOO ( url )
 i11i1 = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( O000oo0O )
 for i1I1iI , url in i11i1 :
  o0O ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , url , 15 , oOOoo00O0O + '3.png' , '' , '' )
  if 72 - 72: IiiI11Iiiii / i1IIi * IIi - IIIii1I1
  if 51 - 51: oOOO0OOooOoO0Oo * iI11iiiI1II % Iiii11I1i1Ii1 * oOOO0OOooOoO0Oo % o0OOOOO00o0O0 / iiiIi1i1I
def iIIIIii1 ( title , message , times = 2000 , icon = i1 ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
def oo000OO00Oo ( ) :
 O0OOO0OOoO0O = O00Oo000ooO0 ( )
 OoO0O00 = O0OOO0OOoO0O . replace ( O0O , "" )
 if os . path . exists ( O0OOO0OOoO0O ) or not O0OOO0OOoO0O == False :
  IIiII = open ( O0OOO0OOoO0O , mode = 'r' ) ; o0 = IIiII . read ( ) ; IIiII . close ( )
  ooOooo000oOO ( "%s - %s" % ( Iii1ii1II11i , OoO0O00 ) , o0 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def O00Oo000ooO0 ( ) :
 Oo0oOOo = False
 if os . path . exists ( os . path . join ( O0O , 'xbmc.log' ) ) :
  Oo0oOOo = os . path . join ( O0O , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( O0O , 'kodi.log' ) ) :
  Oo0oOOo = os . path . join ( O0O , 'kodi.log' )
 elif os . path . exists ( os . path . join ( O0O , 'spmc.log' ) ) :
  Oo0oOOo = os . path . join ( O0O , 'spmc.log' )
 elif os . path . exists ( os . path . join ( O0O , 'tvmc.log' ) ) :
  Oo0oOOo = os . path . join ( O0O , 'tvmc.log' )
 return Oo0oOOo
 if 58 - 58: oOOO0OOooOoO0Oo * Ii1ii1 * o0OOOOO00o0O0 / Ii1ii1
 if 75 - 75: Ii1III1i11i1i
 if 50 - 50: I1i1iii / IIi - Ii1III1i11i1i - ii1I11II1ii1i % IiiI11Iiiii - Ii1III1i11i1i
 if 91 - 91: iI11iiiI1II / ii1I11II1ii1i - oOOO0OOooOoO0Oo . ii1I11II1ii1i
 if 18 - 18: Iiii11I1i1Ii1
def ooOooo000oOO ( heading , announce ) :
 class O0o0O00Oo0o0 ( ) :
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
   try : IIiII = open ( announce ) ; O00O0oOO00O00 = IIiII . read ( )
   except : O00O0oOO00O00 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O00O0oOO00O00 ) )
   return
 O0o0O00Oo0o0 ( )
 O0o0O00Oo0o0 ( )
 if 11 - 11: I1I1i . o0OOOOO00o0O0
 if 92 - 92: IiiI11Iiiii . IIIii1I1
def i1i ( data ) :
 iiI111I1iIiI = len ( data ) % 4
 if 41 - 41: IIi . iiiIi1i1I + O0 * Iiii11I1i1Ii1 % IIi * IIi
 if 19 - 19: IiiI11Iiiii
 if 46 - 46: o0OOOOO00o0O0 - I1i1iii . iIii1I11I1II1 / o0OOOOO00o0O0
 if 7 - 7: i1IIi / II * IIIii1I1 . I1I1i . iIii1I11I1II1
 if 13 - 13: Ii1ii1 / i11iIiiIii
 if 2 - 2: II / O0 / Iiii11I1i1Ii1 % O0oooo0Oo00 % I1i1iii
 if iiI111I1iIiI != 0 :
  data += b'=' * ( 4 - iiI111I1iIiI )
 return base64 . decodestring ( data )
o0o00OO0 = I11 + 'player_api.php?username=%s&password=%s' % ( o0oO0 , o00 )
i1I1ii = I11 + 'movie/%s/%s/' % ( o0oO0 , o00 )
oOOo0 = I11 + 'live/%s/%s/' % ( o0oO0 , o00 )
oo00O00oO = '&action=get_live_categories'
iIiIIIi = I11 + 'player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( o0oO0 , o00 )
ooo00OOOooO = I11 + 'player_api.php?username=%s&password=%s&action=get_vod_categories' % ( o0oO0 , o00 )
O00OOOoOoo0O = I11 + 'enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( o0oO0 , o00 )
O000OOo00oo = I11 + 'player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( o0oO0 , o00 )
oo0OOo = I11 + 'enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=' % ( o0oO0 , o00 )
if 64 - 64: ii1I11II1ii1i
def iI11Ii ( ) :
 iI ( ( '[COLORsteelblue]Full List[/COLOR]' ) . replace ( '\/' , ' - ' ) , '0' , 14 , oOOoo00O0O + '1.png' , i1iiIIiiI111 , '' )
 iI ( ( '[COLORsteelblue]PPV Wrestling[/COLOR]' ) . replace ( '\/' , ' - ' ) , '23' , 14 , oOOoo00O0O + '1.png' , i1iiIIiiI111 , '' )
 iI ( ( '[COLORsteelblue]PPV Boxing[/COLOR]' ) . replace ( '\/' , ' - ' ) , '13' , 14 , oOOoo00O0O + '1.png' , i1iiIIiiI111 , '' )
 iI ( ( '[COLORsteelblue]IND/PAK[/COLOR]' ) . replace ( '\/' , ' - ' ) , '21' , 14 , oOOoo00O0O + '1.png' , i1iiIIiiI111 , '' )
 iI ( ( '[COLORsteelblue]International[/COLOR]' ) . replace ( '\/' , ' - ' ) , '12' , 14 , oOOoo00O0O + '1.png' , i1iiIIiiI111 , '' )
 i1iIIIi1i = OOOO ( o0o00OO0 + oo00O00oO )
 i11i1 = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( i1iIIIi1i )
 for IIIii1II1II , i1I1iI in i11i1 :
  iI ( ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , IIIii1II1II , 14 , oOOoo00O0O + '1.png' , i1iiIIiiI111 , '' )
def iI1iIIiiii ( url ) :
 url = url
 i1iIIIi1i = OOOO ( oo0OOo + url )
 i1iI11i1ii11 = re . compile ( '<channel>(.+?)</channel>' ) . findall ( i1iIIIi1i )
 i11i1 = re . compile ( '<title>(.+?)</title><description>(.+?)/description><desc_image><!.+?http(.+?)".+?<stream_url><!.+?http(.+?).ts.+?></stream_url>' , re . DOTALL ) . findall ( str ( i1iI11i1ii11 ) )
 OOooo0O00o = re . compile ( '<title>(.+?)</title>.+?<description/><desc_image><!.+?http(.+?)".+?<stream_url><!.+?http(.+?).ts.+?></stream_url>' , re . DOTALL ) . findall ( str ( i1iI11i1ii11 ) )
 for i1I1iI , oOOoOooOo , O000oo , IIi1I11I1II in i11i1 :
  if 'PPV' in i1I1iI :
   pass
  else :
   try :
    OooOoooOo = ( o0OoOoOO00 ( i1I1iI ) )
    ii11IIII11I = ( ( o0OoOoOO00 ( oOOoOooOo ) ) )
    OOooo = '('
    oOooOOOoOo = ')'
    o0O ( ( '[COLORsteelblue]' + OooOoooOo + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , 'http' + IIi1I11I1II + '.m3u8' , 15 , 'http' + O000oo , i1iiIIiiI111 , ( '[COLORsteelblue]' + ii11IIII11I + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( oOooOOOoOo , '[COLORsteelblue]' ) . replace ( OOooo , '[COLORorangered]' ) )
   except :
    pass
    OOooo = '('
    oOooOOOoOo = ')'
    o0O ( ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , 'http' + IIi1I11I1II + '.m3u8' , 15 , 'http' + O000oo , i1iiIIiiI111 , ( '[COLORsteelblue]' + oOOoOooOo + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( oOooOOOoOo , '[COLORsteelblue]' ) . replace ( OOooo , '[COLORorangered]' ) )
   i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 for i1I1iI , O000oo , IIi1I11I1II in OOooo0O00o :
  if 'PPV' in i1I1iI :
   pass
  OooOoooOo = ( i1i ( i1I1iI ) )
  o0O ( ( '[COLORsteelblue]' + OooOoooOo + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , 'http' + IIi1I11I1II + '.m3u8' , 15 , 'http' + O000oo , i1iiIIiiI111 , '' )
  i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
def OOoO00 ( url ) :
 url = url
 i1iIIIi1i = OOOO ( iIiIIIi + url )
 i11i1 = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( i1iIIIi1i )
 for i1I1iI , type , IIi1I11I1II , IiI111111IIII in i11i1 :
  i1Ii = ( oOOo0 + IIi1I11I1II + '.m3u8' ) . strip ( )
  o0O ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , i1Ii , 15 , ( IiI111111IIII ) . replace ( '\/' , '/' ) + 'jpg' , i1iiIIiiI111 , type )
  i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
  if 14 - 14: IiiI11Iiiii
  if 11 - 11: I1I1i * II . iIii1I11I1II1 % OoooooooOO + IiiI11Iiiii
def OOO ( ) :
 iI ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , o0o00OO0 + '&action=get_vod_streams' , 41 , oOOoo00O0O + '9.png' , i1iiIIiiI111 , '' )
 i1iIIIi1i = OOOO ( ooo00OOOooO )
 i11i1 = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( i1iIIIi1i )
 for IIIii1II1II , i1I1iI in i11i1 :
  iI ( ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , IIIii1II1II , 41 , oOOoo00O0O + '9.png' , i1iiIIiiI111 , '' )
def oo0OOo0 ( url ) :
 url = url
 i1iIIIi1i = OOOO ( O00OOOoOoo0O + url )
 i11i1 = re . compile ( '<title>(.+?)</title>.+?<desc_image>.+?http:(.+?).jpg.+?</desc_image>.+?<description>(.+?)</description>.+?<category_id>(.+?)</category_id>.+?<stream_url>.+?http:(.+?).mp4.+?</stream_url>' , re . DOTALL ) . findall ( i1iIIIi1i )
 for i1I1iI , IiI111111IIII , oOOoOooOo , I11IiI , url in i11i1 :
  OooOoooOo = ( o0OoOoOO00 ( i1I1iI ) )
  ii11IIII11I = ( ( o0OoOoOO00 ( oOOoOooOo ) ) )
  o0O ( '[COLORsteelblue]' + OooOoooOo + '[/COLOR]' , 'http:' + url + '.mp4' , 15 , 'http:' + ( IiI111111IIII ) . replace ( '\/' , '/' ) + '.jpg' , i1iiIIiiI111 , '[COLORsteelblue]' + ii11IIII11I + '[/COLOR]' )
  if 53 - 53: IiiI11Iiiii % oOOO0OOooOoO0Oo . I1I1i - iIii1I11I1II1 - I1I1i * oOOO0OOooOoO0Oo
def ooO0oOOooOo0 ( ) :
 i1I1ii11i1Iii = OOOO ( o0o00OO0 )
 i11i1 = re . compile ( '"username":"([^"]*)"' ) . findall ( i1I1ii11i1Iii )
 I1IiiiiI = re . compile ( '"password":"([^"]*)"' ) . findall ( i1I1ii11i1Iii )
 o0OIiII = re . compile ( '"status":"([^"]*)"' ) . findall ( i1I1ii11i1Iii )
 OOooo0O00o = re . compile ( '"exp_date":"([^"]*)"' ) . findall ( i1I1ii11i1Iii )
 ii1iII1II = re . compile ( '"active_cons":"([^"]*)"' ) . findall ( i1I1ii11i1Iii )
 Iii1I1I11iiI1 = re . compile ( '"created_at":"([^"]*)"' ) . findall ( i1I1ii11i1Iii )
 I1I1i1I = re . compile ( '"max_connections":"([^"]*)"' ) . findall ( i1I1ii11i1Iii )
 ii1I = re . compile ( '"is_trial":"1"' ) . findall ( i1I1ii11i1Iii )
 O0oO0 = re . compile ( '"is_trial":"0"' ) . findall ( i1I1ii11i1Iii )
 oO0 = re . compile ( '"timezone":"([^"]*)"' ) . findall ( i1I1ii11i1Iii )
 O0OO0O = re . compile ( '"time_now":"([^"]*)"' ) . findall ( i1I1ii11i1Iii )
 for IIIii1II1II in i11i1 :
  o0O ( '[COLORsteelblue]My Account Information[/COLOR]' , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
  o0O ( '[COLORsteelblue]Username:[/COLOR]  %s' % ( IIIii1II1II ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in I1IiiiiI :
  o0O ( '[COLORsteelblue]Password:[/COLOR]  %s' % ( IIIii1II1II ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in o0OIiII :
  o0O ( '[COLORsteelblue]Status:[/COLOR]  %s' % ( IIIii1II1II ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in Iii1I1I11iiI1 :
  OO = datetime . fromtimestamp ( float ( Iii1I1I11iiI1 [ 0 ] ) )
  OO . strftime ( '%Y-%m-%d %H:%M:%S' )
  o0O ( '[COLORsteelblue]Created:[/COLOR]  %s' % ( OO ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in OOooo0O00o :
  OO = datetime . fromtimestamp ( float ( OOooo0O00o [ 0 ] ) )
  OO . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I11i <= OO <= I11i + timedelta ( hours = 24 ) :
   o0O ( '[COLORred]Expires Today[/COLOR]' , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
  o0O ( '[COLORsteelblue]Expires:[/COLOR]  %s' % ( OO ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in ii1iII1II :
  o0O ( '[COLORsteelblue]Active Connection:[/COLOR]  %s' % ( IIIii1II1II ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in I1I1i1I :
  o0O ( '[COLORsteelblue]Max Connection:[/COLOR]  %s' % ( IIIii1II1II ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in ii1I :
  o0O ( '[COLORsteelblue]Trial:[/COLOR] Yes' , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in O0oO0 :
  o0O ( '[COLORsteelblue]Trial:[/COLOR] No' , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in oO0 :
  o0O ( '[COLORsteelblue]Timezone:[/COLOR] %s' % ( IIIii1II1II ) . replace ( '\/' , '/' ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in O0OO0O :
  o0O ( '[COLORsteelblue]Time Now:[/COLOR] %s' % ( IIIii1II1II ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 o0O ( '[COLORsteelblue]Sign up[/COLOR]' , '' , 50006 , '' , '' , '' )
def OoOoO ( ) :
 i1I1ii11i1Iii = OOOO ( I11 + 'panel_api.php?username=' + o0oO0 + '&password=' + o00 )
 i11i1 = re . compile ( '"exp_date":"(.+?)"' ) . findall ( i1I1ii11i1Iii )
 for IIIii1II1II in i11i1 :
  OO = datetime . fromtimestamp ( float ( i11i1 [ 0 ] ) )
  OO . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I11i <= OO <= I11i + timedelta ( hours = 24 ) :
   oOOoO0 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLORsteelblue]If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLORsteelblue]Please Visit [COLORred]' + Oo0o0000o0o0 + '[COLORsteelblue] To Purchase A licence[/COLOR]' )
   if 43 - 43: i11iIiiIii + IIi * oOOO0OOooOoO0Oo * IIIii1I1 * O0
def o00oO0oo0OO ( ) :
 i1iIIIi1i = OOOO ( o0o00OO0 + '&action=get_simple_data_table&stream_id=1309' )
 i11i1 = re . compile ( '"id":"([^"]*)","epg_id":"([^"]*)","title":"([^"]*)","lang":"([^"]*)","start":"([^"]*)","end":"([^"]*)","description":"([^"]*)","channel_id":"([^"]*)"' , re . DOTALL ) . findall ( i1iIIIi1i )
 for id , O0O0OOOOoo , OooOoooOo , oOooO0 , Ii1I1Ii , OOoO0 , oOOoOooOo , OO0Oooo0oOO0O in i11i1 :
  o0O ( '[COLORsteelblue]' + OO0Oooo0oOO0O + ' - ' + o0OoOoOO00 ( OooOoooOo ) + ' - ' + oOooO0 + '[/COLOR]' , id , 31 , oOOoo00O0O + '0.png' , i1iiIIiiI111 , Ii1I1Ii + '[CR]' + OOoO0 + '[CR]' + o0OoOoOO00 ( oOOoOooOo ) )
def o00O0 ( url ) :
 url = i1I1ii + id + '.mp4'
 oOO0O00Oo0O0o ( url )
def ii1 ( url ) :
 iI ( '*[COLORsteelblue]Search[/COLOR]*' , url , 4 , oOOoo00O0O + '2.png' , oOOoo00O0O + '2.png' , 'Search Movies' )
 i1iIIIi1i = OOOO ( url )
 i11i1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( i1iIIIi1i )
 for url , O000oo , oOOoOooOo , I1iIIiiIIi1i , i1I1iI in i11i1 :
  if 'php' in url :
   iI ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , url , 21 , oOOoo00O0O + '2.png' , oOOoo00O0O + '2.png' , oOOoOooOo )
  else :
   o0O ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , url , 15 , O000oo , I1iIIiiIIi1i , oOOoOooOo )
   xbmcplugin . addSortMethod ( ii11iIi1I , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0O0ooOOO ( url ) :
 i1iIIIi1i = OOOO ( url )
 i11i1 = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( i1iIIIi1i )
 for O000oo , i1I1iI , url in i11i1 :
  url = ( ( o0OoOoOO00 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + o0oO0 + '/' + o00 + url ) . strip ( )
  o0O ( ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(ULTIMATE ONLY)' , ' ' ) , url , 15 , O000oo , oOOo0O00o , '' )
  if 8 - 8: iI11iiiI1II
  if 49 - 49: II - ii1I11II1ii1i
  if 74 - 74: iIii1I11I1II1 * o0OOOOO00o0O0 + O0oooo0Oo00 / i1IIi / oOOO0OOooOoO0Oo . IIi
oooOo0OOOoo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.Xhoans/resources/catchup' , 'guide.xml' ) )
OOoO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.Xhoans/resources/catchup' , 'g' ) )
OO0O000 = 'http://piesustv.net:8000/panel_api.php?username=%s&password=%s' % ( o0oO0 , o00 )
def i1i ( data ) :
 iiI111I1iIiI = len ( data ) % 4
 if 37 - 37: OoooooooOO - O0 - Iiii11I1i1Ii1
 if 77 - 77: Ii1ii1 * iIii1I11I1II1
 if 98 - 98: II % I1i1iii * OoooooooOO
 if 51 - 51: iIii1I11I1II1 . O0oooo0Oo00 / Ii1III1i11i1i + Iiii11I1i1Ii1
 if 33 - 33: iiiIi1i1I . oOOO0OOooOoO0Oo % IiiI11Iiiii + Iiii11I1i1Ii1
 if 71 - 71: IIi % Ii1ii1
 if iiI111I1iIiI != 0 :
  data += b'=' * ( 4 - iiI111I1iIiI )
 return base64 . decodestring ( data )
def O00oO000O0O ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : I1i1i1iii = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : I1i1i1iii = ''
 else :
  try : I1i1i1iii = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : I1i1i1iii = ''
 return I1i1i1iii
 if 16 - 16: I1i1iii + I1I1i * O0 % i1IIi . II
 if 67 - 67: OoooooooOO / II * I1i1iii + ii1I11II1ii1i
def OooOo0ooo ( text , start_with , end_with ) :
 I1i1i1iii = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return I1i1i1iii
def o00oo0 ( ) :
 I11ii1IIiIi = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 I11ii1IIiIi . connect ( ( '8.8.8.8' , 0 ) )
 I11ii1IIiIi = I11ii1IIiIi . getsockname ( ) [ 0 ]
 return I11ii1IIiIi
 if 54 - 54: iIii1I11I1II1 % o0OOOOO00o0O0 - Ii1ii1 / Ii1III1i11i1i - iI11iiiI1II . ii1I11II1ii1i
def IIo0Oo0oO0oOO00 ( ) :
 open = OOOO ( 'http://canyouseeme.org/' )
 oo00OO0000oO = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( oo00OO0000oO . group ( ) )
def I1II1 ( ) :
 oooO = "http://piesustv.net:8000/get.php?username=" + o0oO0 + "&password=" + o00 + "&type=m3u_plus&output=ts"
 try :
  i1I1i111Ii = urllib2 . urlopen ( oooO )
  print i1I1i111Ii . getcode ( )
  i1I1i111Ii . close ( )
  if 67 - 67: II . i1IIi
  pass
  if 27 - 27: iiiIi1i1I % II
 except urllib2 . HTTPError , o0oooOO00 :
  print o0oooOO00 . getcode ( )
  oOOoO0 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 32 - 32: IIIii1I1
 IIIii1II1II = "http://piesustv.net:8000/xmltv.php?username=%s&password=%s" % ( o0oO0 , o00 )
 Iii1 ( IIIii1II1II , OOoO + "uide.xml" )
 if 61 - 61: O0oooo0Oo00 - Ii1ii1 - i1IIi
 IIiII = open ( oooOo0OOOoo0 , 'r+' )
 input = open ( oooOo0OOOoo0 ) . read ( ) . decode ( 'UTF-8' )
 IiI1iIiIIIii = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 IIiII . write ( IiI1iIiIIIii )
 IIiII . truncate ( )
 IIiII . close ( )
 oOoO ( )
 if 81 - 81: O0oooo0Oo00 - O0oooo0Oo00 . IiiI11Iiiii
def oOoO ( ) :
 open = OOOO ( OO0O000 )
 all = OooOo0ooo ( open , '{"num' , 'direct' )
 for o0OoOo00o0o in all :
  if '"tv_archive":1' in o0OoOo00o0o :
   i1I1iI = O00oO000O0O ( o0OoOo00o0o , '"epg_channel_id":"' , '"' )
   I1II1I11I1I = O00oO000O0O ( o0OoOo00o0o , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = O00oO000O0O ( o0OoOo00o0o , 'stream_id":"' , '"' )
   i1I1iI = i1I1iI . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   iI ( i1I1iI , id , 90027 , I1II1I11I1I , oOOo0O00o , i1I1iI )
   if 54 - 54: OoooooooOO + Iiii11I1i1Ii1 - i1IIi % i11iIiiIii
   if 3 - 3: Iiii11I1i1Ii1 % Iiii11I1i1Ii1
def oo00o0 ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 IiiiiI1i1Iii = open ( oooOo0OOOoo0 )
 oo00oO0o = ElementTree . parse ( IiiiiI1i1Iii )
 iiii111II = "apples"
 import datetime as dt
 from datetime import time
 I11iIiI1I1i11 = datetime . now ( ) - timedelta ( days = 5 )
 OOoooO00o0oo0 = str ( I11iIiI1I1i11 )
 I11i = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 O00O = oo00oO0o . findall ( "programme" )
 for I1i11 in O00O :
  if name in I1i11 . attrib . get ( 'channel' ) :
   IiIi1I1 = I1i11 . attrib . get ( 'start' )
   IiIIi1 , IIIIiii1IIii , II1i11I = IiIi1I1 . partition ( ' +' )
   OOoooO00o0oo0 = str ( OOoooO00o0oo0 ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   ii1I1IIii11 , O0o0oO , IIIIiIiIi1 = IiIi1I1 . partition ( '2017' )
   I11iiiiI1i = I1i11 . find ( 'title' ) . text + IiIi1I1
   IIIIiIiIi1 = IIIIiIiIi1 [ : - 6 ]
   if IiIIi1 > OOoooO00o0oo0 :
    if IiIIi1 < I11i :
     iI1i11 = IiIIi1
     iI1i11 = iI1i11 [ : 4 ] + '/' + iI1i11 [ 4 : ]
     IiIIi1 = IiIIi1 [ : 4 ] + '-' + IiIIi1 [ 4 : ]
     iI1i11 = iI1i11 [ : 7 ] + '/' + iI1i11 [ 7 : ]
     IiIIi1 = IiIIi1 [ : 7 ] + '-' + IiIIi1 [ 7 : ]
     iI1i11 = iI1i11 [ : 10 ] + ' - ' + iI1i11 [ 10 : ]
     IiIIi1 = IiIIi1 [ : 10 ] + ':' + IiIIi1 [ 10 : ]
     iI1i11 = iI1i11 [ : 15 ] + ':' + iI1i11 [ 15 : ]
     IiIIi1 = IiIIi1 [ : 13 ] + '-' + IiIIi1 [ 13 : ]
     iI1i11 = iI1i11 [ : - 2 ]
     IiIIi1 = IiIIi1 [ : - 2 ]
     OoOOoooOO0O = ( "http://piesustv.net:8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( IiIIi1 ) + "&duration=240" + "&stream=%s" ) % ( o0oO0 , o00 , id )
     iiii111II = OoOOoooOO0O + str ( IiIIi1 ) + "&duration=240"
     iI1i11 = '[COLOR blue]%s - [/COLOR]' % iI1i11
     I11iiiiI1i = str ( iI1i11 ) + I1i11 . find ( 'title' ) . text
     oOOoOooOo = I1i11 . find ( 'desc' ) . text
     o0O ( I11iiiiI1i , OoOOoooOO0O , 15 , oOOoo00O0O + 'catchup.png' , i1iiIIiiI111 , oOOoOooOo )
def ooo00Ooo ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , o0oO0 ) . replace ( 'PASSWORD' , o00 )
 Oo0o0O00 = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = i1 )
 Oo0o0O00 . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 Oo0o0O00 . setProperty ( 'IsPlayable' , 'true' )
 Oo0o0O00 . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo0o0O00 )
def Iii1 ( url , dest ) :
 iIiiiI = xbmcgui . DialogProgress ( )
 iIiiiI . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 iIiiiI . update ( 0 )
 ii1I1i11 = time . time ( )
 urllib . urlretrieve ( url , dest , lambda OOo0O0oo0OO0O , OO0 , o0Oooo : iiI ( OOo0O0oo0OO0O , OO0 , o0Oooo , iIiiiI , ii1I1i11 ) )
def iiI ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  oOIIiIi = min ( numblocks * blocksize * 100 / filesize , 100 )
  OOoOooOoOOOoo = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  Iiii1iI1i = numblocks * blocksize / ( time . time ( ) - start_time )
  if Iiii1iI1i > 0 :
   I1ii1ii11i1I = ( filesize - numblocks * blocksize ) / Iiii1iI1i
  else :
   I1ii1ii11i1I = 0
  Iiii1iI1i = Iiii1iI1i / 1024
  o0OoOO = Iiii1iI1i / 1024
  O0O0Oo00 = float ( filesize ) / ( 1024 * 1024 )
  oOoO00o = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( OOoOooOoOOOoo )
  o0oooOO00 = '[COLOR white]Speed:  %.02f Mb/s ' % o0OoOO + '[/COLOR]'
  dp . update ( oOIIiIi , oOoO00o , o0oooOO00 )
 except :
  oOIIiIi = 100
  dp . update ( oOIIiIi )
 if dp . iscanceled ( ) :
  oOOoO0 = xbmcgui . Dialog ( )
  oOOoO0 . ok ( "GenieTv" , 'The download was cancelled.' )
  if 100 - 100: Iiii11I1i1Ii1 + Ii1ii1 * Iiii11I1i1Ii1
  sys . exit ( )
  dp . close ( )
  if 80 - 80: Iiii11I1i1Ii1 * O0 - I1i1iii
def oo00O00Oo ( ) :
 o0O ( '[COLORsteelblue]Delete Packages[/COLOR]' , '' , 6 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 o0O ( '[COLORsteelblue]Delete Cache[/COLOR]' , '' , 7 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 o0O ( '[COLORsteelblue]View Log File[/COLOR]' , '' , 50000 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 o0O ( '[COLORsteelblue]Force Refresh[/COLOR]' , '' , 50001 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 o0O ( '[COLORsteelblue]Force Close[/COLOR]' , '' , 8 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 if 26 - 26: o0OOOOO00o0O0 - iI11iiiI1II - I1i1iii + o0OOOOO00o0O0
 if 51 - 51: iIii1I11I1II1 . iiiIi1i1I + iIii1I11I1II1
 if 95 - 95: II
def iII1ii1 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def I1i1iiiI1 ( url ) :
 if url == 'http://' : return False
 try :
  iIIi = urllib2 . Request ( url )
  iIIi . add_header ( 'User-Agent' , I1IiI )
  oO0o00oo0 = urllib2 . urlopen ( iIIi )
  oO0o00oo0 . close ( )
 except Exception , o0oooOO00 :
  return o0oooOO00
 return True
def ii1IIII ( ) :
 i1I1ii11i1Iii = OOOO ( i11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i11i1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1I1ii11i1Iii )
 for i1I1iI , IIIii1II1II , IiI111111IIII , oOOo0O00o , oO00oOooooo0 in i11i1 :
  o0O ( i1I1iI , IIIii1II1II , 60002 , IiI111111IIII , oOOoo00O0O + 'a.png' , oO00oOooooo0 )
  if 52 - 52: IIi . Ii1III1i11i1i / Ii1ii1
def OOooOoOo ( name , url ) :
 if iII1ii1 ( ) == 'android' :
  III1I1Iii1iiI = oOOoO0 . yesno ( Iii1ii1II11i , "Would you like to download and install:" , "%s" % name )
  if not III1I1Iii1iiI : iIIIIii1 ( Iii1ii1II11i , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  i1Iii11I1i = name
  if III1I1Iii1iiI :
   if not os . path . exists ( iiIIIII1i1iI ) : os . makedirs ( iiIIIII1i1iI )
   if not I1i1iiiI1 ( url ) == True : iIIIIii1 ( Iii1ii1II11i , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   iIiiiI . create ( Iii1ii1II11i , 'Downloading %s' % i1Iii11I1i , '' , 'Please Wait' )
   Oo00o0OO0O00o = os . path . join ( iiIIIII1i1iI , "%s.apk" % name )
   try : os . remove ( Oo00o0OO0O00o )
   except : pass
   downloader . download ( url , Oo00o0OO0O00o , iIiiiI )
   xbmc . sleep ( 500 )
   iIiiiI . close ( )
   oOOoO0 . ok ( Iii1ii1II11i , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Oo00o0OO0O00o + '")' )
  else : iIIIIii1 ( Iii1ii1II11i , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iIIIIii1 ( Iii1ii1II11i , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 82 - 82: ii1I11II1ii1i + OoooooooOO - i1IIi . i1IIi
 if 6 - 6: Iiii11I1i1Ii1 / ii1I11II1ii1i / oOOO0OOooOoO0Oo
 if 27 - 27: Ii1ii1 * iiiIi1i1I . IIIii1I1 % I1I1i * I1I1i . i1IIi
def O0OOoOOO0oO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 I1ii11 = xbmcgui . Dialog ( )
 I1ii11 . ok ( "Xhoans IPTV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Xhoans IPTV[/COLOR]" )
 return
 if 74 - 74: IIi - Iiii11I1i1Ii1 . i1IIi
def i1III ( url ) :
 print '###' + Iii1ii1II11i + ' - DELETING Addons20.db ###'
 iii1Ii1Ii1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , '' ) )
 IIiooO0oOo0o = os . path . join ( iii1Ii1Ii1 , 'Addons20.db' )
 try :
  os . remove ( IIiooO0oOo0o )
  I1ii11 = xbmcgui . Dialog ( )
  print '=== ' + Iii1ii1II11i + ' - DELETING    ' + str ( IIiooO0oOo0o ) + '    ==='
  I1ii11 . ok ( Iii1ii1II11i , "       Remove Addons20.db Sucessfull Please Reboot To Take Affect" )
 except :
  I1ii11 = xbmcgui . Dialog ( )
  I1ii11 . ok ( Iii1ii1II11i , "       No File To Remove" )
 return
 if 66 - 66: O0oooo0Oo00 . i1IIi . i11iIiiIii % IiiI11Iiiii % iiiIi1i1I
 if 43 - 43: O0
 if 39 - 39: II . iIii1I11I1II1 * I1i1iii % iiiIi1i1I . iIii1I11I1II1
 if 54 - 54: Ii1ii1
def OoOo ( ) :
 if o00 == 'insert_password' :
  oOOoO0 . ok ( '[COLORsteelblue]Xhoans IPTV Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase ' , ' @ [COLORsteelblue]Xhoans IPTV Media[/COLOR]' )
  I1ii11iIi11i . openSettings ( sys . argv [ 0 ] )
 else :
  OoOoO ( )
  if 45 - 45: OoooooooOO - Ii1ii1 + O0 * I1i1iii . o0OOOOO00o0O0
def OOOO ( url ) :
 iIIi = urllib2 . Request ( url )
 iIIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 oO0o00oo0 = urllib2 . urlopen ( iIIi )
 i1I1ii11i1Iii = oO0o00oo0 . read ( )
 oO0o00oo0 . close ( )
 return i1I1ii11i1Iii
def IiiiI ( ) :
 IIIii1II1II = oOo0oooo00o
 O00OoOO0oo0 = oOOoO0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOO = O00OoOO0oo0 . lower ( )
 i1iIIIi1i = OOOO ( IIIii1II1II )
 O0o0OO0000ooo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( i1iIIIi1i )
 for IIIii1II1II , O000oo , oOOoOooOo , I1iIIiiIIi1i , i1I1iI in O0o0OO0000ooo :
  if oOO in i1I1iI . lower ( ) :
   o0O ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , IIIii1II1II , 15 , O000oo , I1iIIiiIIi1i , oOOoOooOo )
   iIiiiI . create ( '[COLORsteelblue]' + Iii1ii1II11i + '[/COLOR]' , "Checking Library" , '' , 'Please Wait' )
   iIiiiI . update ( 53 , "" , "Getting Movie Links" )
   if 4 - 4: I1i1iii
  i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
def ooOooo000oOO ( heading , announce ) :
 class O0o0O00Oo0o0 ( ) :
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
   try : IIiII = open ( announce ) ; O00O0oOO00O00 = IIiII . read ( )
   except : O00O0oOO00O00 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O00O0oOO00O00 ) )
   return
 O0o0O00Oo0o0 ( )
 O0o0O00Oo0o0 ( )
 if 51 - 51: iI11iiiI1II - O0 % Ii1III1i11i1i - oOOO0OOooOoO0Oo
def I1II ( ) :
 i1I1ii11i1Iii = OOOO ( i1111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i11i1 = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1I1ii11i1Iii )
 for i1I1iI , IIIii1II1II , Oo000ooOOO , oOOo0O00o , ii11IIII11I in i11i1 :
  o0O ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , IIIii1II1II , 20 , Oo000ooOOO , oOOo0O00o , ii11IIII11I )
 i1Iii1i1I ( 'movies' , 'MAIN' )
def Ii11i1I11i ( url ) :
 iii1Ii1Ii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 iIiiiI = xbmcgui . DialogProgress ( )
 iIiiiI . create ( "Xhoans IPTV" , "Downloading Files" , '' , 'Please Wait' )
 Oo00o0OO0O00o = os . path . join ( iii1Ii1Ii1 , 'plugin.video.Xhoans' + '.zip' )
 try :
  os . remove ( Oo00o0OO0O00o )
 except :
  pass
 downloader . download ( url , Oo00o0OO0O00o , iIiiiI )
 I11i1 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 iIiiiI . update ( 0 , "" , "Xhoans IPTV Is Now Installing Files Please Wait" )
 print '======================================='
 print I11i1
 print '======================================='
 extract . all ( Oo00o0OO0O00o , I11i1 , iIiiiI )
 iIiIIIIIii ( url )
 I1ii11 = xbmcgui . Dialog ( )
 I1ii11 . ok ( "Xhoans IPTV" , "Press ok to force close Xhoans IPTV, If unsuccessful Please press home button got to settings/apps and force close Xhoans IPTV and clear cache. " , "[COLOR yellow]Brought To You By Xhoans IPTV[/COLOR]" )
 OOo0 ( )
def iIiIIIIIii ( url ) :
 print '###' + Iii1ii1II11i + ' - DELETING PACKAGES###'
 ii11I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oO0oo , Ii111iIi1iIi , IIIII in os . walk ( ii11I1 ) :
   o0ooOoO000oO = 0
   o0ooOoO000oO += len ( IIIII )
   if 85 - 85: Iiii11I1i1Ii1 . O0oooo0Oo00 / iiiIi1i1I . O0 % IIIii1I1
   if 90 - 90: IIi % O0 * iIii1I11I1II1 . IiiI11Iiiii
   if o0ooOoO000oO > 0 :
    if 8 - 8: iiiIi1i1I + oOOO0OOooOoO0Oo / IiiI11Iiiii / ii1I11II1ii1i
    I1ii11 = xbmcgui . Dialog ( )
    if I1ii11 . yesno ( "Delete Package Cache Files" , str ( o0ooOoO000oO ) + " files found" , "Do you want to delete them?" ) :
     if 74 - 74: O0 / i1IIi
     for IIiII in IIIII :
      os . unlink ( os . path . join ( oO0oo , IIiII ) )
     for OoO in Ii111iIi1iIi :
      shutil . rmtree ( os . path . join ( oO0oo , OoO ) )
     I1ii11 = xbmcgui . Dialog ( )
     I1ii11 . ok ( Iii1ii1II11i , "       Deleting Packages all done" )
    else :
     pass
   else :
    I1ii11 = xbmcgui . Dialog ( )
    I1ii11 . ok ( Iii1ii1II11i , "       No Packages to DELETE" )
 except :
  I1ii11 = xbmcgui . Dialog ( )
  I1ii11 . ok ( Iii1ii1II11i , "Error Deleting Packages please visit The Support Group, Xhoans IPTV on facebook" )
 Iiiiii111i1ii ( url )
 return
def Iiiiii111i1ii ( url ) :
 i1i1iII1 = os . path . join ( iI1Ii11111iIi , 'addon_data' )
 iii11i1IIII = [
 ( i1i1iII1 ) ,
 ( I1i1iiI1 ) ,
 ( os . path . join ( IiII , 'cache' ) ) ,
 ( os . path . join ( IiII , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( I1i1iiI1 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I1i1iiI1 , 'plugin.video.Xhoans' , 'Images' ) ) ,
 ( os . path . join ( i1i1iII1 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( i1i1iII1 , 'plugin.video.Xhoans' , 'Images' ) ) ]
 if 26 - 26: O0 . iI11iiiI1II * IIIii1I1 . II % i11iIiiIii
 i1Ii1iii = 0
 if 28 - 28: Ii1III1i11i1i . oOOO0OOooOoO0Oo / o0OOOOO00o0O0 + oOOO0OOooOoO0Oo . OoooooooOO . I1I1i
 for O000OOO0OOo in iii11i1IIII :
  if os . path . exists ( O000OOO0OOo ) and not O000OOO0OOo in [ I1i1iiI1 , i1i1iII1 ] :
   for oO0oo , Ii111iIi1iIi , IIIII in os . walk ( O000OOO0OOo ) :
    o0ooOoO000oO = 0
    o0ooOoO000oO += len ( IIIII )
    if o0ooOoO000oO > 0 :
     for IIiII in IIIII :
      if not IIiII in i1i1II :
       try :
        os . unlink ( os . path . join ( oO0oo , IIiII ) )
       except :
        pass
      else : O0OOO0OOoO0O ( 'Ignore Log File: %s' % IIiII )
     for OoO in Ii111iIi1iIi :
      try :
       shutil . rmtree ( os . path . join ( oO0oo , OoO ) )
       i1Ii1iii += 1
       O0OOO0OOoO0O ( "[Success] cleared %s files from %s" % ( str ( o0ooOoO000oO ) , os . path . join ( O000OOO0OOo , OoO ) ) )
      except :
       O0OOO0OOoO0O ( "[Failed] to wipe cache in: %s" % os . path . join ( O000OOO0OOo , OoO ) )
  else :
   for oO0oo , Ii111iIi1iIi , IIIII in os . walk ( O000OOO0OOo ) :
    for OoO in Ii111iIi1iIi :
     if 'cache' in OoO . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( oO0oo , OoO ) )
       i1Ii1iii += 1
       O0OOO0OOoO0O ( "[Success] wiped %s " % os . path . join ( O000OOO0OOo , OoO ) )
      except :
       O0OOO0OOoO0O ( "[Failed] to wipe cache in: %s" % os . path . join ( O000OOO0OOo , OoO ) )
       if 32 - 32: I1i1iii * O0
 iIIIIii1 ( Iii1ii1II11i , 'Clear Cache: Removed %s Files' % i1Ii1iii )
def O00oOo00o0o ( url ) :
 print '###' + Iii1ii1II11i + ' - DELETING PACKAGES###'
 ii11I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oO0oo , Ii111iIi1iIi , IIIII in os . walk ( ii11I1 ) :
   o0ooOoO000oO = 0
   o0ooOoO000oO += len ( IIIII )
   if 85 - 85: IiiI11Iiiii + OoooooooOO * IiiI11Iiiii - IIIii1I1 % i11iIiiIii
   if 71 - 71: o0OOOOO00o0O0 - iiiIi1i1I / O0oooo0Oo00 * O0oooo0Oo00 / i1IIi . i1IIi
   if o0ooOoO000oO > 0 :
    if 53 - 53: IIIii1I1
    I1ii11 = xbmcgui . Dialog ( )
    if I1ii11 . yesno ( "Delete Package Cache Files" , str ( o0ooOoO000oO ) + " files found" , "Do you want to delete them?" ) :
     if 21 - 21: ii1I11II1ii1i
     for IIiII in IIIII :
      os . unlink ( os . path . join ( oO0oo , IIiII ) )
     for OoO in Ii111iIi1iIi :
      shutil . rmtree ( os . path . join ( oO0oo , OoO ) )
     I1ii11 = xbmcgui . Dialog ( )
     I1ii11 . ok ( Iii1ii1II11i , "       Deleting Packages all done" )
    else :
     pass
   else :
    I1ii11 = xbmcgui . Dialog ( )
    I1ii11 . ok ( Iii1ii1II11i , "       No Packages to DELETE" )
 except :
  I1ii11 = xbmcgui . Dialog ( )
  I1ii11 . ok ( Iii1ii1II11i , "Error Deleting Packages" )
 return
 if 92 - 92: i11iIiiIii / IIIii1I1 - IiiI11Iiiii % iiiIi1i1I * IIIii1I1 + IIi
def OOo0 ( ) :
 I1ii11 = xbmcgui . Dialog ( )
 ii1Oo0000oOo = I1ii11 . yesno ( 'Force Close Xhoans IPTV' , 'You are about to close Xhoans IPTV' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if ii1Oo0000oOo == 0 : return
 elif ii1Oo0000oOo == 1 : pass
 I11o0oO00oO0o0o0 = iII1ii1 ( )
 O0OOO0OOoO0O ( "Platform: " + str ( I11o0oO00oO0o0o0 ) )
 os . _exit ( 1 )
 O0OOO0OOoO0O ( "Force close failed!  Trying alternate methods." )
 if I11o0oO00oO0o0o0 == 'osx' :
  O0OOO0OOoO0O ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  I1ii11 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif I11o0oO00oO0o0o0 == 'linux' :
  O0OOO0OOoO0O ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  I1ii11 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif I11o0oO00oO0o0o0 == 'android' :
  O0OOO0OOoO0O ( "############ try android force close #################" )
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop com.gadgetcity.Xhoans IPTV' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill com.gadgetcity.Xhoans IPTV' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc,kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.com.gadgetcity.Xhoans IPTV());' )
  except : pass
  I1ii11 . ok ( Iii1ii1II11i , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif I11o0oO00oO0o0o0 == 'windows' :
  O0OOO0OOoO0O ( "############ try windows force close #################" )
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill XBMC.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill Kodi.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im Kodi.exe /f' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im XBMC.exe /f' )
  except : pass
  I1ii11 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  O0OOO0OOoO0O ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  O0OOO0OOoO0O ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  I1ii11 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 17 - 17: ii1I11II1ii1i . I1I1i - oOOO0OOooOoO0Oo + O0 / iIii1I11I1II1 / i11iIiiIii
def oOO0O00Oo0O0o ( url ) :
 import urlresolver
 try :
  I1IIIiI1I1ii1 = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( I1IIIiI1I1ii1 , xbmcgui . ListItem ( i1I1iI ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( i1I1iI ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def iII1ii1 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
 if 30 - 30: O0 * OoooooooOO
def O0OOO0OOoO0O ( log ) :
 xbmc . log ( "[%s]: %s" % ( Iii1ii1II11i , log ) )
 if not os . path . exists ( I1i1iiI1 ) : os . makedirs ( I1i1iiI1 )
 if not os . path . exists ( oo00 ) : IIiII = open ( oo00 , 'w' ) ; IIiII . close ( )
 with open ( oo00 , 'a' ) as IIiII :
  I1iIIIi1 = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  IIiII . write ( I1iIIIi1 . rstrip ( '\r\n' ) + '\n' )
  if 17 - 17: iIii1I11I1II1 . OoooooooOO / ii1I11II1ii1i % oOOO0OOooOoO0Oo % i1IIi / i11iIiiIii
def OOOIiiiii1iI ( ) :
 try :
  IIiooOooo0 = getSet ( "core-player" )
  if ( IIiooOooo0 == 'DVDPLAYER' ) : oO0OO0 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( IIiooOooo0 == 'MPLAYER' ) : oO0OO0 = xbmc . PLAYER_CORE_MPLAYER
  elif ( IIiooOooo0 == 'PAPLAYER' ) : oO0OO0 = xbmc . PLAYER_CORE_PAPLAYER
  else : oO0OO0 = xbmc . PLAYER_CORE_AUTO
 except : oO0OO0 = xbmc . PLAYER_CORE_AUTO
 return oO0OO0
 return True
 if 82 - 82: I1I1i - I1I1i + O0oooo0Oo00
 if 8 - 8: Iiii11I1i1Ii1 % IiiI11Iiiii * Ii1III1i11i1i % I1i1iii . iiiIi1i1I / iiiIi1i1I
def iI ( name , url , mode , iconimage , fanart , description ) :
 if 81 - 81: iI11iiiI1II
 oO0o00oOOooO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOOoO000 = True
 Oo0o0O00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0o0O00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0o0O00 . setProperty ( "Fanart_Image" , fanart )
 OOOoO000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0o00oOOooO0 , listitem = Oo0o0O00 , isFolder = True )
 return OOOoO000
 if 57 - 57: oOOO0OOooOoO0Oo
def o0O ( name , url , mode , iconimage , fanart , description ) :
 if 54 - 54: IIi + Ii1III1i11i1i + i11iIiiIii
 oO0o00oOOooO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOOoO000 = True
 Oo0o0O00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0o0O00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0o0O00 . setProperty ( "Fanart_Image" , fanart )
 OOOoO000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oO0o00oOOooO0 , listitem = Oo0o0O00 , isFolder = False )
 return OOOoO000
 if 28 - 28: Ii1III1i11i1i
def ooo000o0ooO0 ( ) :
 I1I = [ ]
 oOoo000 = sys . argv [ 2 ]
 if len ( oOoo000 ) >= 2 :
  OooOo00o = sys . argv [ 2 ]
  IiI11i1IIiiI = OooOo00o . replace ( '?' , '' )
  if ( OooOo00o [ len ( OooOo00o ) - 1 ] == '/' ) :
   OooOo00o = OooOo00o [ 0 : len ( OooOo00o ) - 2 ]
  oOOo000oOoO0 = IiI11i1IIiiI . split ( '&' )
  I1I = { }
  for OoOo00o0OO in range ( len ( oOOo000oOoO0 ) ) :
   ii1IIIIiI11 = { }
   ii1IIIIiI11 = oOOo000oOoO0 [ OoOo00o0OO ] . split ( '=' )
   if ( len ( ii1IIIIiI11 ) ) == 2 :
    I1I [ ii1IIIIiI11 [ 0 ] ] = ii1IIIIiI11 [ 1 ]
    if 40 - 40: Iiii11I1i1Ii1
 return I1I
 if 67 - 67: Ii1III1i11i1i + oOOO0OOooOoO0Oo - O0 . Ii1III1i11i1i * oOOO0OOooOoO0Oo * ii1I11II1ii1i
 if 90 - 90: I1i1iii . I1I1i
OooOo00o = ooo000o0ooO0 ( )
IIIii1II1II = None
i1I1iI = None
OO00O0oOO = None
Oo000ooOOO = None
oOOo0O00o = None
ii11IIII11I = None
Ii1iI111 = None
if 51 - 51: I1I1i * O0 / oOOO0OOooOoO0Oo . I1i1iii % Ii1ii1 / II
if 9 - 9: II % II % oOOO0OOooOoO0Oo
try :
 Ii1iI111 = int ( OooOo00o [ "fav_mode" ] )
except :
 pass
 if 30 - 30: I1I1i + IIIii1I1 - I1I1i . I1I1i - oOOO0OOooOoO0Oo + O0
try :
 IIIii1II1II = urllib . unquote_plus ( OooOo00o [ "url" ] )
except :
 pass
try :
 i1I1iI = urllib . unquote_plus ( OooOo00o [ "name" ] )
except :
 pass
try :
 Oo000ooOOO = urllib . unquote_plus ( OooOo00o [ "iconimage" ] )
except :
 pass
try :
 OO00O0oOO = int ( OooOo00o [ "mode" ] )
except :
 pass
try :
 oOOo0O00o = urllib . unquote_plus ( OooOo00o [ "fanart" ] )
except :
 pass
try :
 ii11IIII11I = urllib . unquote_plus ( OooOo00o [ "description" ] )
except :
 pass
 if 86 - 86: i1IIi
 if 41 - 41: O0oooo0Oo00 * ii1I11II1ii1i / O0oooo0Oo00 % Ii1III1i11i1i
print str ( oO ) + ': ' + str ( i1iII1IiiIiI1 )
print "Mode: " + str ( OO00O0oOO )
print "URL: " + str ( IIIii1II1II )
print "Name: " + str ( i1I1iI )
print "IconImage: " + str ( Oo000ooOOO )
if 18 - 18: oOOO0OOooOoO0Oo . OoooooooOO % O0oooo0Oo00 % I1i1iii
if 9 - 9: iI11iiiI1II - IIi * OoooooooOO . IIi
def i1Iii1i1I ( content , viewType ) :
 if 2 - 2: OoooooooOO % Ii1ii1
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if I1ii11iIi11i . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % I1ii11iIi11i . getSetting ( viewType ) )
  if 63 - 63: II % iIii1I11I1II1
  if 39 - 39: IiiI11Iiiii / oOOO0OOooOoO0Oo / o0OOOOO00o0O0 % II
if OO00O0oOO == None : oOO00oOO ( )
elif OO00O0oOO == 1 : Genres ( )
elif OO00O0oOO == 2 : Lists ( IIIii1II1II , Oo000ooOOO )
elif OO00O0oOO == 3 : all_mov ( )
elif OO00O0oOO == 4 : IiiiI ( )
elif OO00O0oOO == 5 : oo00O00Oo ( )
elif OO00O0oOO == 6 : O00oOo00o0o ( IIIii1II1II )
elif OO00O0oOO == 7 : Iiiiii111i1ii ( IIIii1II1II )
elif OO00O0oOO == 8 : OOo0 ( )
elif OO00O0oOO == 9 : oo0 ( )
elif OO00O0oOO == 10 : ooO0oOOooOo0 ( )
elif OO00O0oOO == 11 : TvGuide ( )
elif OO00O0oOO == 12 : OoOo ( )
elif OO00O0oOO == 13 : ReCreate_Addon_ini ( )
elif OO00O0oOO == 14 : iI1iIIiiii ( IIIii1II1II )
elif OO00O0oOO == 144 : OOoO00 ( IIIii1II1II )
elif OO00O0oOO == 15 : oOO0O00Oo0O0o ( IIIii1II1II )
elif OO00O0oOO == 16 : iI11Ii ( )
elif OO00O0oOO == 17 : Live_Events ( i1I1iI )
elif OO00O0oOO == 18 : I1ii11iIi11i . openSettings ( sys . argv [ 0 ] )
elif OO00O0oOO == 19 : I1II ( )
elif OO00O0oOO == 20 : Ii11i1I11i ( IIIii1II1II )
elif OO00O0oOO == 30 : o00oO0oo0OO ( )
elif OO00O0oOO == 31 : o00O0 ( IIIii1II1II )
elif OO00O0oOO == 40 : OOO ( )
elif OO00O0oOO == 41 : oo0OOo0 ( IIIii1II1II )
elif OO00O0oOO == 21 : ii1 ( IIIii1II1II )
elif OO00O0oOO == 22 : O0O0ooOOO ( IIIii1II1II )
elif OO00O0oOO == 50 : OooOooo ( )
elif OO00O0oOO == 51 : oo0OooOOo0 ( IIIii1II1II )
elif OO00O0oOO == 50000 : oo000OO00Oo ( )
elif OO00O0oOO == 50001 : O0OOoOOO0oO ( )
elif OO00O0oOO == 50002 : i1III ( IIIii1II1II )
elif OO00O0oOO == 60001 : ii1IIII ( )
elif OO00O0oOO == 60002 : OOooOoOo ( i1I1iI , IIIii1II1II )
elif OO00O0oOO == 90026 : I1II1 ( )
elif OO00O0oOO == 90027 : oo00o0 ( i1I1iI , IIIii1II1II , ii11IIII11I )
elif OO00O0oOO == 90028 : ooo00Ooo ( IIIii1II1II )
if 89 - 89: IIIii1I1 + OoooooooOO + IIIii1I1 * i1IIi + iIii1I11I1II1 % ii1I11II1ii1i
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
