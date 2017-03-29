# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
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
i1iII1IiiIiI1 = "0.0.6"
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
def OoOOoOooooOOo ( ) :
 o0O ( '[COLORsteelblue]Delete Packages[/COLOR]' , '' , 6 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 o0O ( '[COLORsteelblue]Delete Cache[/COLOR]' , '' , 7 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 o0O ( '[COLORsteelblue]View Log File[/COLOR]' , '' , 50000 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 o0O ( '[COLORsteelblue]Force Refresh[/COLOR]' , '' , 50001 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 o0O ( '[COLORsteelblue]Force Close[/COLOR]' , '' , 8 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 if 87 - 87: II
 if 58 - 58: O0oooo0Oo00 % Iiii11I1i1Ii1
 if 50 - 50: IIIii1I1 . Iiii11I1i1Ii1
def ooO0OO ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def O000OOO ( url ) :
 if url == 'http://' : return False
 try :
  IIo0o0O0O00oOOo = urllib2 . Request ( url )
  IIo0o0O0O00oOOo . add_header ( 'User-Agent' , I1IiI )
  iIIIiIi = urllib2 . urlopen ( IIo0o0O0O00oOOo )
  iIIIiIi . close ( )
 except Exception , OO0O0 :
  return OO0O0
 return True
def I11I11 ( ) :
 i1I1ii11i1Iii = OOOO ( i11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i11i1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1I1ii11i1Iii )
 for i1I1iI , IIIii1II1II , IiI111111IIII , oOOo0O00o , o000O0O in i11i1 :
  o0O ( i1I1iI , IIIii1II1II , 60002 , IiI111111IIII , oOOoo00O0O + 'a.png' , o000O0O )
  if 18 - 18: IiiI11Iiiii - Ii1ii1 . IIIii1I1 . iIii1I11I1II1
def i1I ( name , url ) :
 if ooO0OO ( ) == 'android' :
  O0ooooOOoo0O = oOOoO0 . yesno ( Iii1ii1II11i , "Would you like to download and install:" , "%s" % name )
  if not O0ooooOOoo0O : iIIIIii1 ( Iii1ii1II11i , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  II1IiiIi1i = name
  if O0ooooOOoo0O :
   if not os . path . exists ( iiIIIII1i1iI ) : os . makedirs ( iiIIIII1i1iI )
   if not O000OOO ( url ) == True : iIIIIii1 ( Iii1ii1II11i , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   iIiiiI . create ( Iii1ii1II11i , 'Downloading %s' % II1IiiIi1i , '' , 'Please Wait' )
   iiI11ii1I1 = os . path . join ( iiIIIII1i1iI , "%s.apk" % name )
   try : os . remove ( iiI11ii1I1 )
   except : pass
   downloader . download ( url , iiI11ii1I1 , iIiiiI )
   xbmc . sleep ( 500 )
   iIiiiI . close ( )
   oOOoO0 . ok ( Iii1ii1II11i , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + iiI11ii1I1 + '")' )
  else : iIIIIii1 ( Iii1ii1II11i , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iIIIIii1 ( Iii1ii1II11i , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 82 - 82: oOOO0OOooOoO0Oo % ii1I11II1ii1i / iI11iiiI1II + O0oooo0Oo00 / Iiii11I1i1Ii1 / IIIii1I1
 if 70 - 70: Ii1III1i11i1i
 if 59 - 59: Iiii11I1i1Ii1 % Ii1III1i11i1i
def ii1iI1I11I ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 II1iI = xbmcgui . Dialog ( )
 II1iI . ok ( "Xhoans IPTV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Xhoans IPTV[/COLOR]" )
 return
 if 54 - 54: IIIii1I1 * I1I1i / IIIii1I1 / IIi * O0oooo0Oo00
def O0oOo0o0OO00O ( url ) :
 print '###' + Iii1ii1II11i + ' - DELETING Addons20.db ###'
 iIi = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , '' ) )
 II1i111Ii1i = os . path . join ( iIi , 'Addons20.db' )
 try :
  os . remove ( II1i111Ii1i )
  II1iI = xbmcgui . Dialog ( )
  print '=== ' + Iii1ii1II11i + ' - DELETING    ' + str ( II1i111Ii1i ) + '    ==='
  II1iI . ok ( Iii1ii1II11i , "       Remove Addons20.db Sucessfull Please Reboot To Take Affect" )
 except :
  II1iI = xbmcgui . Dialog ( )
  II1iI . ok ( Iii1ii1II11i , "       No File To Remove" )
 return
 if 15 - 15: oOOO0OOooOoO0Oo / i1IIi
 if 76 - 76: ii1I11II1ii1i / Ii1ii1 . O0 % II . Iiii11I1i1Ii1 + I1I1i
 if 71 - 71: IIIii1I1 . oOOO0OOooOoO0Oo
 if 62 - 62: OoooooooOO . ii1I11II1ii1i
def OoOo ( ) :
 if o00 == 'insert_password' :
  oOOoO0 . ok ( '[COLORsteelblue]Xhoans IPTV Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase ' , ' @ [COLORsteelblue]Xhoans IPTV Media[/COLOR]' )
  I1ii11iIi11i . openSettings ( sys . argv [ 0 ] )
 else :
  OoOoO ( )
  if 61 - 61: O0oooo0Oo00 - Ii1ii1 - i1IIi
def OOOO ( url ) :
 IIo0o0O0O00oOOo = urllib2 . Request ( url )
 IIo0o0O0O00oOOo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 iIIIiIi = urllib2 . urlopen ( IIo0o0O0O00oOOo )
 i1I1ii11i1Iii = iIIIiIi . read ( )
 iIIIiIi . close ( )
 return i1I1ii11i1Iii
def IiI1iIiIIIii ( ) :
 IIIii1II1II = oOo0oooo00o
 oOoO = oOOoO0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOoO00O0 = oOoO . lower ( )
 i1iIIIi1i = OOOO ( IIIii1II1II )
 OOIi1iI111II1I1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( i1iIIIi1i )
 for IIIii1II1II , O000oo , oOOoOooOo , I1iIIiiIIi1i , i1I1iI in OOIi1iI111II1I1 :
  if oOoO00O0 in i1I1iI . lower ( ) :
   o0O ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , IIIii1II1II , 15 , O000oo , I1iIIiiIIi1i , oOOoOooOo )
   iIiiiI . create ( '[COLORsteelblue]' + Iii1ii1II11i + '[/COLOR]' , "Checking Library" , '' , 'Please Wait' )
   iIiiiI . update ( 53 , "" , "Getting Movie Links" )
   if 91 - 91: Ii1ii1 % Ii1ii1 - II
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
 if 18 - 18: ii1I11II1ii1i - i11iIiiIii / oOOO0OOooOoO0Oo . Ii1ii1
def OoOo00o0O00 ( ) :
 i1I1ii11i1Iii = OOOO ( i1111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i11i1 = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1I1ii11i1Iii )
 for i1I1iI , IIIii1II1II , iiI , oOOo0O00o , ii11IIII11I in i11i1 :
  o0O ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , IIIii1II1II , 20 , iiI , oOOo0O00o , ii11IIII11I )
 i1Iii1i1I ( 'movies' , 'MAIN' )
def oOoo0oOo00 ( url ) :
 iIi = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 iIiiiI = xbmcgui . DialogProgress ( )
 iIiiiI . create ( "Xhoans IPTV" , "Downloading Files" , '' , 'Please Wait' )
 iiI11ii1I1 = os . path . join ( iIi , 'plugin.video.Xhoans' + '.zip' )
 try :
  os . remove ( iiI11ii1I1 )
 except :
  pass
 downloader . download ( url , iiI11ii1I1 , iIiiiI )
 IiiiIiii11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 iIiiiI . update ( 0 , "" , "Xhoans IPTV Is Now Installing Files Please Wait" )
 print '======================================='
 print IiiiIiii11
 print '======================================='
 extract . all ( iiI11ii1I1 , IiiiIiii11 , iIiiiI )
 OO0000o ( url )
 II1iI = xbmcgui . Dialog ( )
 II1iI . ok ( "Xhoans IPTV" , "Press ok to force close Xhoans IPTV, If unsuccessful Please press home button got to settings/apps and force close Xhoans IPTV and clear cache. " , "[COLOR yellow]Brought To You By Xhoans IPTV[/COLOR]" )
 i1I1i1 ( )
def OO0000o ( url ) :
 print '###' + Iii1ii1II11i + ' - DELETING PACKAGES###'
 O0OoooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooo0O0o00O , I1i11 , IiIi1I1 in os . walk ( O0OoooO0 ) :
   IiIIi1 = 0
   IiIIi1 += len ( IiIi1I1 )
   if 47 - 47: IIi * o0OOOOO00o0O0 + iIii1I11I1II1 / IIIii1I1 / iI11iiiI1II - OoooooooOO
   if 33 - 33: O0oooo0Oo00 * Ii1ii1 - oOOO0OOooOoO0Oo
   if IiIIi1 > 0 :
    if 83 - 83: O0oooo0Oo00 - I1i1iii / ii1I11II1ii1i / IIIii1I1 + Ii1III1i11i1i - O0
    II1iI = xbmcgui . Dialog ( )
    if II1iI . yesno ( "Delete Package Cache Files" , str ( IiIIi1 ) + " files found" , "Do you want to delete them?" ) :
     if 4 - 4: Ii1ii1 * iI11iiiI1II % i1IIi * i11iIiiIii % IIi - Ii1III1i11i1i
     for IIiII in IiIi1I1 :
      os . unlink ( os . path . join ( ooo0O0o00O , IIiII ) )
     for OOoOoOo in I1i11 :
      shutil . rmtree ( os . path . join ( ooo0O0o00O , OOoOoOo ) )
     II1iI = xbmcgui . Dialog ( )
     II1iI . ok ( Iii1ii1II11i , "       Deleting Packages all done" )
    else :
     pass
   else :
    II1iI = xbmcgui . Dialog ( )
    II1iI . ok ( Iii1ii1II11i , "       No Packages to DELETE" )
 except :
  II1iI = xbmcgui . Dialog ( )
  II1iI . ok ( Iii1ii1II11i , "Error Deleting Packages please visit The Support Group, Xhoans IPTV on facebook" )
 o000ooooO0o ( url )
 return
def o000ooooO0o ( url ) :
 iI1i11 = os . path . join ( iI1Ii11111iIi , 'addon_data' )
 OoOOoooOO0O = [
 ( iI1i11 ) ,
 ( I1i1iiI1 ) ,
 ( os . path . join ( IiII , 'cache' ) ) ,
 ( os . path . join ( IiII , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( I1i1iiI1 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I1i1iiI1 , 'plugin.video.Xhoans' , 'Images' ) ) ,
 ( os . path . join ( iI1i11 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( iI1i11 , 'plugin.video.Xhoans' , 'Images' ) ) ]
 if 86 - 86: Iiii11I1i1Ii1
 i1Iii11Ii1i1 = 0
 if 59 - 59: IIi % OoooooooOO . IiiI11Iiiii / I1I1i + II
 for o0O0oO0O00O0o in OoOOoooOO0O :
  if os . path . exists ( o0O0oO0O00O0o ) and not o0O0oO0O00O0o in [ I1i1iiI1 , iI1i11 ] :
   for ooo0O0o00O , I1i11 , IiIi1I1 in os . walk ( o0O0oO0O00O0o ) :
    IiIIi1 = 0
    IiIIi1 += len ( IiIi1I1 )
    if IiIIi1 > 0 :
     for IIiII in IiIi1I1 :
      if not IIiII in i1i1II :
       try :
        os . unlink ( os . path . join ( ooo0O0o00O , IIiII ) )
       except :
        pass
      else : O0OOO0OOoO0O ( 'Ignore Log File: %s' % IIiII )
     for OOoOoOo in I1i11 :
      try :
       shutil . rmtree ( os . path . join ( ooo0O0o00O , OOoOoOo ) )
       i1Iii11Ii1i1 += 1
       O0OOO0OOoO0O ( "[Success] cleared %s files from %s" % ( str ( IiIIi1 ) , os . path . join ( o0O0oO0O00O0o , OOoOoOo ) ) )
      except :
       O0OOO0OOoO0O ( "[Failed] to wipe cache in: %s" % os . path . join ( o0O0oO0O00O0o , OOoOoOo ) )
  else :
   for ooo0O0o00O , I1i11 , IiIi1I1 in os . walk ( o0O0oO0O00O0o ) :
    for OOoOoOo in I1i11 :
     if 'cache' in OOoOoOo . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( ooo0O0o00O , OOoOoOo ) )
       i1Iii11Ii1i1 += 1
       O0OOO0OOoO0O ( "[Success] wiped %s " % os . path . join ( o0O0oO0O00O0o , OOoOoOo ) )
      except :
       O0OOO0OOoO0O ( "[Failed] to wipe cache in: %s" % os . path . join ( o0O0oO0O00O0o , OOoOoOo ) )
       if 28 - 28: IIi + iI11iiiI1II * Ii1ii1 % Ii1III1i11i1i . ii1I11II1ii1i % O0
 iIIIIii1 ( Iii1ii1II11i , 'Clear Cache: Removed %s Files' % i1Iii11Ii1i1 )
def I1iiiiIii ( url ) :
 print '###' + Iii1ii1II11i + ' - DELETING PACKAGES###'
 O0OoooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooo0O0o00O , I1i11 , IiIi1I1 in os . walk ( O0OoooO0 ) :
   IiIIi1 = 0
   IiIIi1 += len ( IiIi1I1 )
   if 19 - 19: iI11iiiI1II - IIi . O0
   if 60 - 60: oOOO0OOooOoO0Oo + IIi
   if IiIIi1 > 0 :
    if 9 - 9: iiiIi1i1I * OoooooooOO - iIii1I11I1II1 + O0oooo0Oo00 / iI11iiiI1II . iI11iiiI1II
    II1iI = xbmcgui . Dialog ( )
    if II1iI . yesno ( "Delete Package Cache Files" , str ( IiIIi1 ) + " files found" , "Do you want to delete them?" ) :
     if 49 - 49: oOOO0OOooOoO0Oo
     for IIiII in IiIi1I1 :
      os . unlink ( os . path . join ( ooo0O0o00O , IIiII ) )
     for OOoOoOo in I1i11 :
      shutil . rmtree ( os . path . join ( ooo0O0o00O , OOoOoOo ) )
     II1iI = xbmcgui . Dialog ( )
     II1iI . ok ( Iii1ii1II11i , "       Deleting Packages all done" )
    else :
     pass
   else :
    II1iI = xbmcgui . Dialog ( )
    II1iI . ok ( Iii1ii1II11i , "       No Packages to DELETE" )
 except :
  II1iI = xbmcgui . Dialog ( )
  II1iI . ok ( Iii1ii1II11i , "Error Deleting Packages" )
 return
 if 25 - 25: OoooooooOO - II . II * Ii1III1i11i1i
def i1I1i1 ( ) :
 II1iI = xbmcgui . Dialog ( )
 o000oo = II1iI . yesno ( 'Force Close Xhoans IPTV' , 'You are about to close Xhoans IPTV' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if o000oo == 0 : return
 elif o000oo == 1 : pass
 o00o0 = ooO0OO ( )
 O0OOO0OOoO0O ( "Platform: " + str ( o00o0 ) )
 os . _exit ( 1 )
 O0OOO0OOoO0O ( "Force close failed!  Trying alternate methods." )
 if o00o0 == 'osx' :
  O0OOO0OOoO0O ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  II1iI . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif o00o0 == 'linux' :
  O0OOO0OOoO0O ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  II1iI . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif o00o0 == 'android' :
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
  II1iI . ok ( Iii1ii1II11i , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif o00o0 == 'windows' :
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
  II1iI . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  O0OOO0OOoO0O ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  O0OOO0OOoO0O ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  II1iI . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 50 - 50: IIi / IIi % o0OOOOO00o0O0 . o0OOOOO00o0O0
def oOO0O00Oo0O0o ( url ) :
 O0O0Oo00 = xbmc . Player ( oOoO00o ( ) )
 import urlresolver
 try : O0O0Oo00 . play ( url ) . strip ( )
 except : pass
def ooO0OO ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
 if 100 - 100: Iiii11I1i1Ii1 + Ii1ii1 * Iiii11I1i1Ii1
def O0OOO0OOoO0O ( log ) :
 xbmc . log ( "[%s]: %s" % ( Iii1ii1II11i , log ) )
 if not os . path . exists ( I1i1iiI1 ) : os . makedirs ( I1i1iiI1 )
 if not os . path . exists ( oo00 ) : IIiII = open ( oo00 , 'w' ) ; IIiII . close ( )
 with open ( oo00 , 'a' ) as IIiII :
  oOOo0OOOo00O = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  IIiII . write ( oOOo0OOOo00O . rstrip ( '\r\n' ) + '\n' )
  if 76 - 76: i11iIiiIii + Iiii11I1i1Ii1 / o0OOOOO00o0O0 - iI11iiiI1II - I1i1iii + o0OOOOO00o0O0
def oOoO00o ( ) :
 try :
  ooI1i = getSet ( "core-player" )
  if ( ooI1i == 'DVDPLAYER' ) : iIII = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( ooI1i == 'MPLAYER' ) : iIII = xbmc . PLAYER_CORE_MPLAYER
  elif ( ooI1i == 'PAPLAYER' ) : iIII = xbmc . PLAYER_CORE_PAPLAYER
  else : iIII = xbmc . PLAYER_CORE_AUTO
 except : iIII = xbmc . PLAYER_CORE_AUTO
 return iIII
 return True
 if 70 - 70: IiiI11Iiiii / iIii1I11I1II1
 if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / o0OOOOO00o0O0
def iI ( name , url , mode , iconimage , fanart , description ) :
 if 96 - 96: OoooooooOO + Ii1III1i11i1i
 iiII1i11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiIi = True
 OOOOO0O00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOOOO0O00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOOOO0O00 . setProperty ( "Fanart_Image" , fanart )
 IiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiII1i11i , listitem = OOOOO0O00 , isFolder = True )
 return IiIi
 if 30 - 30: iIii1I11I1II1 . II . Ii1ii1 / Iiii11I1i1Ii1
def o0O ( name , url , mode , iconimage , fanart , description ) :
 if 42 - 42: IIi
 iiII1i11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiIi = True
 OOOOO0O00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOOOO0O00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOOOO0O00 . setProperty ( "Fanart_Image" , fanart )
 IiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiII1i11i , listitem = OOOOO0O00 , isFolder = False )
 return IiIi
 if 19 - 19: Ii1III1i11i1i % o0OOOOO00o0O0 * iIii1I11I1II1 + II
def iii11I ( ) :
 I1Iii1 = [ ]
 iiI11Iii = sys . argv [ 2 ]
 if len ( iiI11Iii ) >= 2 :
  O0o0O0 = sys . argv [ 2 ]
  Ii1II1I11i1 = O0o0O0 . replace ( '?' , '' )
  if ( O0o0O0 [ len ( O0o0O0 ) - 1 ] == '/' ) :
   O0o0O0 = O0o0O0 [ 0 : len ( O0o0O0 ) - 2 ]
  oOoooooOoO = Ii1II1I11i1 . split ( '&' )
  I1Iii1 = { }
  for Ii111 in range ( len ( oOoooooOoO ) ) :
   I111i1i1111 = { }
   I111i1i1111 = oOoooooOoO [ Ii111 ] . split ( '=' )
   if ( len ( I111i1i1111 ) ) == 2 :
    I1Iii1 [ I111i1i1111 [ 0 ] ] = I111i1i1111 [ 1 ]
    if 49 - 49: iI11iiiI1II / Ii1III1i11i1i + O0 * Iiii11I1i1Ii1
 return I1Iii1
 if 28 - 28: iiiIi1i1I + i11iIiiIii / ii1I11II1ii1i % O0oooo0Oo00 % IIi - O0
 if 54 - 54: i1IIi + oOOO0OOooOoO0Oo
O0o0O0 = iii11I ( )
IIIii1II1II = None
i1I1iI = None
oOOO0oo0 = None
iiI = None
oOOo0O00o = None
ii11IIII11I = None
iIi1i1iIi1iI = None
if 26 - 26: OoooooooOO * II + Ii1ii1
if 24 - 24: i11iIiiIii % iIii1I11I1II1 + Ii1ii1 / i11iIiiIii
try :
 iIi1i1iIi1iI = int ( O0o0O0 [ "fav_mode" ] )
except :
 pass
 if 70 - 70: iI11iiiI1II * O0 . ii1I11II1ii1i + II . I1I1i
try :
 IIIii1II1II = urllib . unquote_plus ( O0o0O0 [ "url" ] )
except :
 pass
try :
 i1I1iI = urllib . unquote_plus ( O0o0O0 [ "name" ] )
except :
 pass
try :
 iiI = urllib . unquote_plus ( O0o0O0 [ "iconimage" ] )
except :
 pass
try :
 oOOO0oo0 = int ( O0o0O0 [ "mode" ] )
except :
 pass
try :
 oOOo0O00o = urllib . unquote_plus ( O0o0O0 [ "fanart" ] )
except :
 pass
try :
 ii11IIII11I = urllib . unquote_plus ( O0o0O0 [ "description" ] )
except :
 pass
 if 14 - 14: iIii1I11I1II1 % iIii1I11I1II1 * i11iIiiIii - iI11iiiI1II - ii1I11II1ii1i
 if 63 - 63: iI11iiiI1II
print str ( oO ) + ': ' + str ( i1iII1IiiIiI1 )
print "Mode: " + str ( oOOO0oo0 )
print "URL: " + str ( IIIii1II1II )
print "Name: " + str ( i1I1iI )
print "IconImage: " + str ( iiI )
if 69 - 69: iIii1I11I1II1 . o0OOOOO00o0O0 % iiiIi1i1I + iIii1I11I1II1 / O0 / o0OOOOO00o0O0
if 61 - 61: Ii1ii1 % Ii1ii1 * Iiii11I1i1Ii1 / Iiii11I1i1Ii1
def i1Iii1i1I ( content , viewType ) :
 if 75 - 75: I1I1i . iiiIi1i1I
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if I1ii11iIi11i . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % I1ii11iIi11i . getSetting ( viewType ) )
  if 50 - 50: O0oooo0Oo00
  if 60 - 60: iiiIi1i1I * iIii1I11I1II1 * o0OOOOO00o0O0 * IIi
if oOOO0oo0 == None : oOO00oOO ( )
elif oOOO0oo0 == 1 : Genres ( )
elif oOOO0oo0 == 2 : Lists ( IIIii1II1II , iiI )
elif oOOO0oo0 == 3 : all_mov ( )
elif oOOO0oo0 == 4 : IiI1iIiIIIii ( )
elif oOOO0oo0 == 5 : OoOOoOooooOOo ( )
elif oOOO0oo0 == 6 : I1iiiiIii ( IIIii1II1II )
elif oOOO0oo0 == 7 : o000ooooO0o ( IIIii1II1II )
elif oOOO0oo0 == 8 : i1I1i1 ( )
elif oOOO0oo0 == 9 : oo0 ( )
elif oOOO0oo0 == 10 : ooO0oOOooOo0 ( )
elif oOOO0oo0 == 11 : TvGuide ( )
elif oOOO0oo0 == 12 : OoOo ( )
elif oOOO0oo0 == 13 : ReCreate_Addon_ini ( )
elif oOOO0oo0 == 14 : iI1iIIiiii ( IIIii1II1II )
elif oOOO0oo0 == 144 : OOoO00 ( IIIii1II1II )
elif oOOO0oo0 == 15 : oOO0O00Oo0O0o ( IIIii1II1II )
elif oOOO0oo0 == 16 : iI11Ii ( )
elif oOOO0oo0 == 17 : Live_Events ( i1I1iI )
elif oOOO0oo0 == 18 : I1ii11iIi11i . openSettings ( sys . argv [ 0 ] )
elif oOOO0oo0 == 19 : OoOo00o0O00 ( )
elif oOOO0oo0 == 20 : oOoo0oOo00 ( IIIii1II1II )
elif oOOO0oo0 == 30 : o00oO0oo0OO ( )
elif oOOO0oo0 == 31 : o00O0 ( IIIii1II1II )
elif oOOO0oo0 == 40 : OOO ( )
elif oOOO0oo0 == 41 : oo0OOo0 ( IIIii1II1II )
elif oOOO0oo0 == 21 : ii1 ( IIIii1II1II )
elif oOOO0oo0 == 22 : O0O0ooOOO ( IIIii1II1II )
elif oOOO0oo0 == 50 : OooOooo ( )
elif oOOO0oo0 == 51 : oo0OooOOo0 ( IIIii1II1II )
elif oOOO0oo0 == 50000 : oo000OO00Oo ( )
elif oOOO0oo0 == 50001 : ii1iI1I11I ( )
elif oOOO0oo0 == 50002 : O0oOo0o0OO00O ( IIIii1II1II )
elif oOOO0oo0 == 60001 : I11I11 ( )
elif oOOO0oo0 == 60002 : i1I ( i1I1iI , IIIii1II1II )
if 69 - 69: I1i1iii * O0 . i11iIiiIii / I1i1iii . Iiii11I1i1Ii1
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
