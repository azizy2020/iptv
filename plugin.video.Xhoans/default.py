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
i1iII1IiiIiI1 = "0.0.9"
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
def i1i ( ) :
 iiI111I1iIiI = "http://piesustv.net:8000//get.php?username=" + o0oO0 + "&password=" + o00 + "&type=m3u_plus&output=ts"
 try :
  IIIi1I1IIii1II = urllib2 . urlopen ( iiI111I1iIiI )
  print IIIi1I1IIii1II . getcode ( )
  IIIi1I1IIii1II . close ( )
  if 65 - 65: I1i1iii . iIii1I11I1II1 / O0 - I1i1iii
  pass
  if 21 - 21: II * iIii1I11I1II1
 except urllib2 . HTTPError , oooooOoo0ooo :
  print oooooOoo0ooo . getcode ( )
  Dialog . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLORsteelblue]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLORsteelblue]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def I1I1IiI1 ( data ) :
 III1iII1I1ii = len ( data ) % 4
 if 61 - 61: oOOO0OOooOoO0Oo
 if 64 - 64: iiiIi1i1I / O0oooo0Oo00 - O0 - ii1I11II1ii1i
 if 86 - 86: ii1I11II1ii1i % O0oooo0Oo00 / II / O0oooo0Oo00
 if 42 - 42: iI11iiiI1II
 if 67 - 67: IIIii1I1 . IiiI11Iiiii . O0
 if 10 - 10: o0OOOOO00o0O0 % o0OOOOO00o0O0 - iIii1I11I1II1 / Ii1ii1 + I1i1iii
 if III1iII1I1ii != 0 :
  data += b'=' * ( 4 - III1iII1I1ii )
 return base64 . decodestring ( data )
 if 87 - 87: Ii1III1i11i1i * o0OOOOO00o0O0 + Ii1ii1 / iIii1I11I1II1 / IiiI11Iiiii
I1111IIi = I11 + 'player_api.php?username=%s&password=%s' % ( o0oO0 , o00 )
Oo0oO = I11 + 'movie/%s/%s/' % ( o0oO0 , o00 )
IIiIi1iI = I11 + 'live/%s/%s/' % ( o0oO0 , o00 )
i1IiiiI1iI = '&action=get_live_categories'
i1iIi = I11 + 'player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( o0oO0 , o00 )
ooOOoooooo = I11 + 'player_api.php?username=%s&password=%s&action=get_vod_categories' % ( o0oO0 , o00 )
II1I = I11 + 'enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( o0oO0 , o00 )
O0i1II1Iiii1I11 = I11 + 'player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( o0oO0 , o00 )
IIII = I11 + 'enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=' % ( o0oO0 , o00 )
if 32 - 32: OoooooooOO / iIii1I11I1II1 - Iiii11I1i1Ii1
def o00oooO0Oo ( ) :
 iI ( ( '[COLORsteelblue]Full List[/COLOR]' ) . replace ( '\/' , ' - ' ) , '0' , 14 , oOOoo00O0O + '1.png' , i1iiIIiiI111 , '' )
 iI ( ( '[COLORsteelblue]PPV Wrestling[/COLOR]' ) . replace ( '\/' , ' - ' ) , '23' , 14 , oOOoo00O0O + '1.png' , i1iiIIiiI111 , '' )
 iI ( ( '[COLORsteelblue]PPV Boxing[/COLOR]' ) . replace ( '\/' , ' - ' ) , '13' , 14 , oOOoo00O0O + '1.png' , i1iiIIiiI111 , '' )
 iI ( ( '[COLORsteelblue]IND/PAK[/COLOR]' ) . replace ( '\/' , ' - ' ) , '21' , 14 , oOOoo00O0O + '1.png' , i1iiIIiiI111 , '' )
 iI ( ( '[COLORsteelblue]International[/COLOR]' ) . replace ( '\/' , ' - ' ) , '12' , 14 , oOOoo00O0O + '1.png' , i1iiIIiiI111 , '' )
 o0O0OOO0Ooo = OOOO ( I1111IIi + i1IiiiI1iI )
 i11i1 = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( o0O0OOO0Ooo )
 for IIIii1II1II , i1I1iI in i11i1 :
  iI ( ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , IIIii1II1II , 14 , oOOoo00O0O + '1.png' , i1iiIIiiI111 , '' )
def iiIiI ( url ) :
 open = OOOO ( IIII + url )
 I1 = OOO00O0O ( open , '<channel>' , '</channel>' )
 for iii in I1 :
  i1I1iI = oOooOOOoOo ( iii , '<title>' , '</title>' )
  i1I1iI = base64 . b64decode ( i1I1iI )
  xbmc . log ( str ( i1I1iI ) )
  i1Iii1i1I = oOooOOOoOo ( iii , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  OOoO00 = oOooOOOoOo ( iii , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  IiI111111IIII = oOooOOOoOo ( iii , '<description>' , '</description>' )
  IiI111111IIII = base64 . b64decode ( IiI111111IIII )
  i1Ii = '('
  ii111iI1iIi1 = ')'
  addDir2 ( ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , OOoO00 , 15 , i1Iii1i1I , OOO , ( '[COLORsteelblue]' + IiI111111IIII + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( ii111iI1iIi1 , '[COLORsteelblue]' ) . replace ( i1Ii , '[COLORorangered]' ) )
  if 68 - 68: oOOO0OOooOoO0Oo + ii1I11II1ii1i
def I1I1I ( url ) :
 url = url
 o0O0OOO0Ooo = OOOO ( i1iIi + url )
 i11i1 = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( o0O0OOO0Ooo )
 for i1I1iI , type , OoOO000 , i1Ii11i1i in i11i1 :
  o0oOOoo = ( IIiIi1iI + OoOO000 + '.m3u8' ) . strip ( )
  o0O ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , o0oOOoo , 15 , ( i1Ii11i1i ) . replace ( '\/' , '/' ) + 'jpg' , i1iiIIiiI111 , type )
  oOo00O0oo00o0 ( 'tvshows' , 'Media Info 3' )
  if 45 - 45: O0
  if 26 - 26: ii1I11II1ii1i - iIii1I11I1II1 - II / iI11iiiI1II . O0oooo0Oo00 % iIii1I11I1II1
def OO ( ) :
 i1i ( )
 iI ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , I1111IIi + '&action=get_vod_streams' , 41 , oOOoo00O0O + 'Vod_Lists.png' , i1iiIIiiI111 , '' )
 o0O0OOO0Ooo = OOOO ( ooOOoooooo )
 i11i1 = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( o0O0OOO0Ooo )
 for IIIii1II1II , i1I1iI in i11i1 :
  o0O ( ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , IIIii1II1II , 41 , oOOoo00O0O + 'Vod_Lists.png' , i1iiIIiiI111 , '' )
def iIiIIi1 ( url ) :
 open = OOOO ( II1I + url )
 I1 = OOO00O0O ( open , '<channel>' , '</channel>' )
 for iii in I1 :
  if '<playlist_url>' in open :
   i1I1iI = oOooOOOoOo ( iii , '<title>' , '</title>' )
   OOoO00 = oOooOOOoOo ( iii , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   o0O ( str ( base64 . b64decode ( i1I1iI ) ) . replace ( '?' , '' ) , OOoO00 , 3 , icon , OOO , '' )
  else :
   i1I1iI = oOooOOOoOo ( iii , '<title>' , '</title>' )
   i1I1iI = base64 . b64decode ( i1I1iI )
   i1Iii1i1I = oOooOOOoOo ( iii , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   url = oOooOOOoOo ( iii , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   IiI111111IIII = oOooOOOoOo ( iii , '<description>' , '</description>' )
   IiI111111IIII = base64 . b64decode ( IiI111111IIII )
   I1IIII1i = oOooOOOoOo ( IiI111111IIII , 'PLOT:' , '\n' )
   I1I11i = oOooOOOoOo ( IiI111111IIII , 'CAST:' , '\n' )
   Ii1I1I1i1Ii = oOooOOOoOo ( IiI111111IIII , 'RATING:' , '\n' )
   i1Oo0oO00o = oOooOOOoOo ( IiI111111IIII , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
   i1Oo0oO00o = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( i1Oo0oO00o )
   i11I1II1I11i = oOooOOOoOo ( IiI111111IIII , 'DURATION_SECS:' , '\n' )
   OooOoOO0 = oOooOOOoOo ( IiI111111IIII , 'GENRE:' , '\n' )
   iI1i11iII111 ( str ( i1I1iI ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 15 , i1Iii1i1I , OOO , I1IIII1i , str ( i1Oo0oO00o ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( I1I11i ) . split ( ) , Ii1I1I1i1Ii , i11I1II1I11i , OooOoOO0 )
   xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   if 15 - 15: i11iIiiIii % I1i1iii . IIi + o0OOOOO00o0O0
def OO0OOOOoo0OOO ( ) :
 i1i1Ii1 = OOOO ( I1111IIi )
 i11i1 = re . compile ( '"username":"([^"]*)"' ) . findall ( i1i1Ii1 )
 Ii11iIi = re . compile ( '"password":"([^"]*)"' ) . findall ( i1i1Ii1 )
 O00O0Oooo0oO = re . compile ( '"status":"([^"]*)"' ) . findall ( i1i1Ii1 )
 IIii11I1 = re . compile ( '"exp_date":"([^"]*)"' ) . findall ( i1i1Ii1 )
 oOO0O00Oo0O0o = re . compile ( '"active_cons":"([^"]*)"' ) . findall ( i1i1Ii1 )
 ii1 = re . compile ( '"created_at":"([^"]*)"' ) . findall ( i1i1Ii1 )
 I1iIIiiIIi1i = re . compile ( '"max_connections":"([^"]*)"' ) . findall ( i1i1Ii1 )
 O0O0ooOOO = re . compile ( '"is_trial":"1"' ) . findall ( i1i1Ii1 )
 oOOo0O00o = re . compile ( '"is_trial":"0"' ) . findall ( i1i1Ii1 )
 iIiIi11 = re . compile ( '"timezone":"([^"]*)"' ) . findall ( i1i1Ii1 )
 OOOiiiiI = re . compile ( '"time_now":"([^"]*)"' ) . findall ( i1i1Ii1 )
 for IIIii1II1II in i11i1 :
  o0O ( '[COLORsteelblue]My Account Information[/COLOR]' , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
  o0O ( '[COLORsteelblue]Username:[/COLOR]  %s' % ( IIIii1II1II ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in Ii11iIi :
  o0O ( '[COLORsteelblue]Password:[/COLOR]  %s' % ( IIIii1II1II ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in O00O0Oooo0oO :
  o0O ( '[COLORsteelblue]Status:[/COLOR]  %s' % ( IIIii1II1II ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in ii1 :
  oooOo0OOOoo0 = datetime . fromtimestamp ( float ( ii1 [ 0 ] ) )
  oooOo0OOOoo0 . strftime ( '%Y-%m-%d %H:%M:%S' )
  o0O ( '[COLORsteelblue]Created:[/COLOR]  %s' % ( oooOo0OOOoo0 ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in IIii11I1 :
  oooOo0OOOoo0 = datetime . fromtimestamp ( float ( IIii11I1 [ 0 ] ) )
  oooOo0OOOoo0 . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I11i <= oooOo0OOOoo0 <= I11i + timedelta ( hours = 24 ) :
   o0O ( '[COLORred]Expires Today[/COLOR]' , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
  o0O ( '[COLORsteelblue]Expires:[/COLOR]  %s' % ( oooOo0OOOoo0 ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in oOO0O00Oo0O0o :
  o0O ( '[COLORsteelblue]Active Connection:[/COLOR]  %s' % ( IIIii1II1II ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in I1iIIiiIIi1i :
  o0O ( '[COLORsteelblue]Max Connection:[/COLOR]  %s' % ( IIIii1II1II ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in O0O0ooOOO :
  o0O ( '[COLORsteelblue]Trial:[/COLOR] Yes' , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in oOOo0O00o :
  o0O ( '[COLORsteelblue]Trial:[/COLOR] No' , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in iIiIi11 :
  o0O ( '[COLORsteelblue]Timezone:[/COLOR] %s' % ( IIIii1II1II ) . replace ( '\/' , '/' ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 for IIIii1II1II in OOOiiiiI :
  o0O ( '[COLORsteelblue]Time Now:[/COLOR] %s' % ( IIIii1II1II ) , '' , '' , oOOoo00O0O + '7.png' , '' , '' )
 o0O ( '[COLORsteelblue]Sign up[/COLOR]' , '' , 50006 , '' , '' , '' )
def OOoO ( ) :
 i1i1Ii1 = OOOO ( I11 + 'panel_api.php?username=' + o0oO0 + '&password=' + o00 )
 i11i1 = re . compile ( '"exp_date":"(.+?)"' ) . findall ( i1i1Ii1 )
 for IIIii1II1II in i11i1 :
  oooOo0OOOoo0 = datetime . fromtimestamp ( float ( i11i1 [ 0 ] ) )
  oooOo0OOOoo0 . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I11i <= oooOo0OOOoo0 <= I11i + timedelta ( hours = 24 ) :
   oOOoO0 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLORsteelblue]If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLORsteelblue]Please Visit [COLORred]' + Oo0o0000o0o0 + '[COLORsteelblue] To Purchase A licence[/COLOR]' )
   if 89 - 89: Iiii11I1i1Ii1 + iI11iiiI1II * ii1I11II1ii1i * I1i1iii
def iiIiI1i1 ( ) :
 o0O0OOO0Ooo = OOOO ( I1111IIi + '&action=get_simple_data_table&stream_id=1309' )
 i11i1 = re . compile ( '"id":"([^"]*)","epg_id":"([^"]*)","title":"([^"]*)","lang":"([^"]*)","start":"([^"]*)","end":"([^"]*)","description":"([^"]*)","channel_id":"([^"]*)"' , re . DOTALL ) . findall ( o0O0OOO0Ooo )
 for id , oO0O00oOOoooO , IiIi11iI , Oo0O00O000 , i11I1IiII1i1i , ooI1111i , IiI111111IIII , iIIii in i11i1 :
  o0O ( '[COLORsteelblue]' + iIIii + ' - ' + o0OoOoOO00 ( IiIi11iI ) + ' - ' + Oo0O00O000 + '[/COLOR]' , id , 31 , oOOoo00O0O + '0.png' , i1iiIIiiI111 , i11I1IiII1i1i + '[CR]' + ooI1111i + '[CR]' + o0OoOoOO00 ( IiI111111IIII ) )
def o00O0O ( url ) :
 url = Oo0oO + id + '.mp4'
 ii1iii1i ( url )
def Iii1I1111ii ( url ) :
 iI ( '*[COLORsteelblue]Search[/COLOR]*' , url , 4 , oOOoo00O0O + '2.png' , oOOoo00O0O + '2.png' , 'Search Movies' )
 o0O0OOO0Ooo = OOOO ( url )
 i11i1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( o0O0OOO0Ooo )
 for url , ooOoO00 , IiI111111IIII , Ii1IIiI1i , i1I1iI in i11i1 :
  if 'php' in url :
   iI ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , url , 21 , oOOoo00O0O + '2.png' , oOOoo00O0O + '2.png' , IiI111111IIII )
  else :
   o0O ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , url , 15 , ooOoO00 , Ii1IIiI1i , IiI111111IIII )
   xbmcplugin . addSortMethod ( ii11iIi1I , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0O00Oo0 ( url ) :
 o0O0OOO0Ooo = OOOO ( url )
 i11i1 = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o0O0OOO0Ooo )
 for ooOoO00 , i1I1iI , url in i11i1 :
  url = ( ( o0OoOoOO00 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + o0oO0 + '/' + o00 + url ) . strip ( )
  o0O ( ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(ULTIMATE ONLY)' , ' ' ) , url , 15 , ooOoO00 , OOO , '' )
def iI1i11iII111 ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 IiII111i1i11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 i111iIi1i1II1 = True
 oooO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 oooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 oooO . setProperty ( 'fanart_image' , fanart )
 oooO . setProperty ( "IsPlayable" , "true" )
 i1I1i111Ii = [ ]
 i1I1i111Ii . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 i1I1i111Ii . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 oooO . addContextMenuItems ( i1I1i111Ii , replaceItems = True )
 i111iIi1i1II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiII111i1i11 , listitem = oooO , isFolder = False )
 return i111iIi1i1II1
 if 67 - 67: II . i1IIi
 if 27 - 27: iiiIi1i1I % II
o0oooOO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.Xhoans/resources/catchup' , 'guide.xml' ) )
iiIiii1IIIII = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.Xhoans/resources/catchup' , 'g' ) )
o00o = 'http://piesustv.net:8000/panel_api.php?username=%s&password=%s' % ( o0oO0 , o00 )
def I1I1IiI1 ( data ) :
 III1iII1I1ii = len ( data ) % 4
 if 45 - 45: o0OOOOO00o0O0 . Iiii11I1i1Ii1 . o0OOOOO00o0O0 - II . Iiii11I1i1Ii1
 if 12 - 12: O0 - Iiii11I1i1Ii1
 if 81 - 81: O0oooo0Oo00 - O0oooo0Oo00 . IiiI11Iiiii
 if 73 - 73: ii1I11II1ii1i % i11iIiiIii - II
 if 7 - 7: O0 * i11iIiiIii * I1i1iii + iiiIi1i1I % iI11iiiI1II - iiiIi1i1I
 if 39 - 39: IIi * Ii1ii1 % Ii1ii1 - OoooooooOO + Iiii11I1i1Ii1 - ii1I11II1ii1i
 if III1iII1I1ii != 0 :
  data += b'=' * ( 4 - III1iII1I1ii )
 return base64 . decodestring ( data )
def oOooOOOoOo ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : ii = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : ii = ''
 else :
  try : ii = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : ii = ''
 return ii
 if 68 - 68: IiiI11Iiiii - II / IIIii1I1 / ii1I11II1ii1i
 if 12 - 12: I1i1iii + i11iIiiIii * iIii1I11I1II1 / o0OOOOO00o0O0 . ii1I11II1ii1i
def OOO00O0O ( text , start_with , end_with ) :
 ii = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return ii
def Iii1iI ( ) :
 IiI1iiiIii = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 IiI1iiiIii . connect ( ( '8.8.8.8' , 0 ) )
 IiI1iiiIii = IiI1iiiIii . getsockname ( ) [ 0 ]
 return IiI1iiiIii
 if 7 - 7: IIIii1I1 * iI11iiiI1II - iiiIi1i1I + Ii1ii1 * II % iI11iiiI1II
def iI1i111I1Ii ( ) :
 open = OOOO ( 'http://canyouseeme.org/' )
 i11i1ii1I = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( i11i1ii1I . group ( ) )
def o0OO0o0o00o ( ) :
 iiI111I1iIiI = "http://piesustv.net:8000/get.php?username=" + o0oO0 + "&password=" + o00 + "&type=m3u_plus&output=ts"
 try :
  IIIi1I1IIii1II = urllib2 . urlopen ( iiI111I1iIiI )
  print IIIi1I1IIii1II . getcode ( )
  IIIi1I1IIii1II . close ( )
  if 100 - 100: Ii1III1i11i1i / IIIii1I1 / o0OOOOO00o0O0
  pass
  if 78 - 78: IIi - Iiii11I1i1Ii1 / O0oooo0Oo00
 except urllib2 . HTTPError , oooooOoo0ooo :
  print oooooOoo0ooo . getcode ( )
  oOOoO0 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 10 - 10: IiiI11Iiiii + IIi * o0OOOOO00o0O0 + iIii1I11I1II1 / IIIii1I1 / o0OOOOO00o0O0
 IIIii1II1II = "http://piesustv.net:8000/xmltv.php?username=%s&password=%s" % ( o0oO0 , o00 )
 iI1II ( IIIii1II1II , iiIiii1IIIII + "uide.xml" )
 if 69 - 69: iiiIi1i1I % Ii1III1i11i1i
 IIiII = open ( o0oooOO00 , 'r+' )
 input = open ( o0oooOO00 ) . read ( ) . decode ( 'UTF-8' )
 ii1I1IIii11 = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 IIiII . write ( ii1I1IIii11 )
 IIiII . truncate ( )
 IIiII . close ( )
 O0o0oO ( )
 if 38 - 38: Ii1III1i11i1i % O0oooo0Oo00 + o0OOOOO00o0O0 . i11iIiiIii
def O0o0oO ( ) :
 open = OOOO ( o00o )
 all = OOO00O0O ( open , '{"num' , 'direct' )
 for iii in all :
  if '"tv_archive":1' in iii :
   i1I1iI = oOooOOOoOo ( iii , '"epg_channel_id":"' , '"' )
   i1Iii1i1I = oOooOOOoOo ( iii , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = oOooOOOoOo ( iii , 'stream_id":"' , '"' )
   i1I1iI = i1I1iI . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   iI ( i1I1iI , id , 90027 , i1Iii1i1I , OOO , i1I1iI )
   if 53 - 53: i11iIiiIii * IiiI11Iiiii
   if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . Iiii11I1i1Ii1 / oOOO0OOooOoO0Oo % IIi
def i1i11I11 ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 iiiiII1I = open ( o0oooOO00 )
 ooo00Ooo = ElementTree . parse ( iiiiII1I )
 Oo0o0O00 = "apples"
 import datetime as dt
 from datetime import time
 ii1I1i11 = datetime . now ( ) - timedelta ( days = 5 )
 OOo0O0oo0OO0O = str ( ii1I1i11 )
 I11i = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 OO0 = ooo00Ooo . findall ( "programme" )
 for o0Oooo in OO0 :
  if name in o0Oooo . attrib . get ( 'channel' ) :
   iiI = o0Oooo . attrib . get ( 'start' )
   oOIIiIi , OOoOooOoOOOoo , Iiii1iI1i = iiI . partition ( ' +' )
   OOo0O0oo0OO0O = str ( OOo0O0oo0OO0O ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   i1Oo0oO00o , I1ii1ii11i1I , o0OoOO = iiI . partition ( '2017' )
   O0O0Oo00 = o0Oooo . find ( 'title' ) . text + iiI
   o0OoOO = o0OoOO [ : - 6 ]
   if oOIIiIi > OOo0O0oo0OO0O :
    if oOIIiIi < I11i :
     oOoO00o = oOIIiIi
     oOoO00o = oOoO00o [ : 4 ] + '/' + oOoO00o [ 4 : ]
     oOIIiIi = oOIIiIi [ : 4 ] + '-' + oOIIiIi [ 4 : ]
     oOoO00o = oOoO00o [ : 7 ] + '/' + oOoO00o [ 7 : ]
     oOIIiIi = oOIIiIi [ : 7 ] + '-' + oOIIiIi [ 7 : ]
     oOoO00o = oOoO00o [ : 10 ] + ' - ' + oOoO00o [ 10 : ]
     oOIIiIi = oOIIiIi [ : 10 ] + ':' + oOIIiIi [ 10 : ]
     oOoO00o = oOoO00o [ : 15 ] + ':' + oOoO00o [ 15 : ]
     oOIIiIi = oOIIiIi [ : 13 ] + '-' + oOIIiIi [ 13 : ]
     oOoO00o = oOoO00o [ : - 2 ]
     oOIIiIi = oOIIiIi [ : - 2 ]
     oO00O0 = ( "http://piesustv.net:8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( oOIIiIi ) + "&duration=240" + "&stream=%s" ) % ( o0oO0 , o00 , id )
     Oo0o0O00 = oO00O0 + str ( oOIIiIi ) + "&duration=240"
     oOoO00o = '[COLOR blue]%s - [/COLOR]' % oOoO00o
     O0O0Oo00 = str ( oOoO00o ) + o0Oooo . find ( 'title' ) . text
     IiI111111IIII = o0Oooo . find ( 'desc' ) . text
     o0O ( O0O0Oo00 , oO00O0 , 15 , oOOoo00O0O + 'catchup.png' , i1iiIIiiI111 , IiI111111IIII )
def IIi1IIIi ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , o0oO0 ) . replace ( 'PASSWORD' , o00 )
 oooO = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = i1 )
 oooO . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 oooO . setProperty ( 'IsPlayable' , 'true' )
 oooO . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oooO )
def iI1II ( url , dest ) :
 iIiiiI = xbmcgui . DialogProgress ( )
 iIiiiI . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 iIiiiI . update ( 0 )
 O00Ooo = time . time ( )
 urllib . urlretrieve ( url , dest , lambda OOOO0OOO , i1i1ii , iII1ii1 : I1i1iiiI1 ( OOOO0OOO , i1i1ii , iII1ii1 , iIiiiI , O00Ooo ) )
def I1i1iiiI1 ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  iIIi = min ( numblocks * blocksize * 100 / filesize , 100 )
  oO0o00oo0 = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  ii1IIII = numblocks * blocksize / ( time . time ( ) - start_time )
  if ii1IIII > 0 :
   oO00oOooooo0 = ( filesize - numblocks * blocksize ) / ii1IIII
  else :
   oO00oOooooo0 = 0
  ii1IIII = ii1IIII / 1024
  oOo = ii1IIII / 1024
  O0OOooOoO = float ( filesize ) / ( 1024 * 1024 )
  i1II1I1Iii1 = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( oO0o00oo0 )
  oooooOoo0ooo = '[COLOR white]Speed:  %.02f Mb/s ' % oOo + '[/COLOR]'
  dp . update ( iIIi , i1II1I1Iii1 , oooooOoo0ooo )
 except :
  iIIi = 100
  dp . update ( iIIi )
 if dp . iscanceled ( ) :
  oOOoO0 = xbmcgui . Dialog ( )
  oOOoO0 . ok ( "GenieTv" , 'The download was cancelled.' )
  if 30 - 30: OoooooooOO - O0oooo0Oo00
  sys . exit ( )
  dp . close ( )
  if 75 - 75: iIii1I11I1II1 - I1i1iii . IIi % i11iIiiIii % ii1I11II1ii1i
def O00 ( ) :
 o0O ( '[COLORsteelblue]Delete Packages[/COLOR]' , '' , 6 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 o0O ( '[COLORsteelblue]Delete Cache[/COLOR]' , '' , 7 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 o0O ( '[COLORsteelblue]View Log File[/COLOR]' , '' , 50000 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 o0O ( '[COLORsteelblue]Force Refresh[/COLOR]' , '' , 50001 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 o0O ( '[COLORsteelblue]Force Close[/COLOR]' , '' , 8 , oOOoo00O0O + '4.png' , i1iiIIiiI111 , '' )
 if 30 - 30: II + iI11iiiI1II % I1i1iii * IiiI11Iiiii / IIi - ii1I11II1ii1i
 if 64 - 64: iIii1I11I1II1
 if 21 - 21: IIi . oOOO0OOooOoO0Oo
def ooo000o000 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def O0o ( url ) :
 if url == 'http://' : return False
 try :
  O0OOoOOO0oO = urllib2 . Request ( url )
  O0OOoOOO0oO . add_header ( 'User-Agent' , I1IiI )
  I1ii11 = urllib2 . urlopen ( O0OOoOOO0oO )
  I1ii11 . close ( )
 except Exception , oooooOoo0ooo :
  return oooooOoo0ooo
 return True
def oOoOoOoo0 ( ) :
 i1i1Ii1 = OOOO ( i11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i11i1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1i1Ii1 )
 for i1I1iI , IIIii1II1II , i1Ii11i1i , OOO , III1ii1I in i11i1 :
  o0O ( i1I1iI , IIIii1II1II , 60002 , i1Ii11i1i , oOOoo00O0O + 'a.png' , III1ii1I )
  if 13 - 13: i11iIiiIii + i1IIi * iIii1I11I1II1 % OoooooooOO - oOOO0OOooOoO0Oo * Ii1ii1
def iiIi1iI1iIii ( name , url ) :
 if ooo000o000 ( ) == 'android' :
  o00OooO0oo = oOOoO0 . yesno ( Iii1ii1II11i , "Would you like to download and install:" , "%s" % name )
  if not o00OooO0oo : iIIIIii1 ( Iii1ii1II11i , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  o0o0oOoOO0O = name
  if o00OooO0oo :
   if not os . path . exists ( iiIIIII1i1iI ) : os . makedirs ( iiIIIII1i1iI )
   if not O0o ( url ) == True : iIIIIii1 ( Iii1ii1II11i , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   iIiiiI . create ( Iii1ii1II11i , 'Downloading %s' % o0o0oOoOO0O , '' , 'Please Wait' )
   i1ii1II1ii = os . path . join ( iiIIIII1i1iI , "%s.apk" % name )
   try : os . remove ( i1ii1II1ii )
   except : pass
   downloader . download ( url , i1ii1II1ii , iIiiiI )
   xbmc . sleep ( 500 )
   iIiiiI . close ( )
   oOOoO0 . ok ( Iii1ii1II11i , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + i1ii1II1ii + '")' )
  else : iIIIIii1 ( Iii1ii1II11i , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iIIIIii1 ( Iii1ii1II11i , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 28 - 28: o0OOOOO00o0O0
 if 61 - 61: Ii1ii1 % Ii1ii1 * Iiii11I1i1Ii1 / Iiii11I1i1Ii1
 if 75 - 75: I1I1i . iiiIi1i1I
def iII111i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 O0000o = xbmcgui . Dialog ( )
 O0000o . ok ( "Xhoans IPTV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Xhoans IPTV[/COLOR]" )
 return
 if 7 - 7: O0 . I1i1iii
def OO0oOOoo ( url ) :
 print '###' + Iii1ii1II11i + ' - DELETING Addons20.db ###'
 oOOO00o000o = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , '' ) )
 iIi11i1 = os . path . join ( oOOO00o000o , 'Addons20.db' )
 try :
  os . remove ( iIi11i1 )
  O0000o = xbmcgui . Dialog ( )
  print '=== ' + Iii1ii1II11i + ' - DELETING    ' + str ( iIi11i1 ) + '    ==='
  O0000o . ok ( Iii1ii1II11i , "       Remove Addons20.db Sucessfull Please Reboot To Take Affect" )
 except :
  O0000o = xbmcgui . Dialog ( )
  O0000o . ok ( Iii1ii1II11i , "       No File To Remove" )
 return
 if 71 - 71: iiiIi1i1I
 if 53 - 53: OoooooooOO % I1i1iii . I1I1i / i11iIiiIii % IiiI11Iiiii
 if 28 - 28: ii1I11II1ii1i
 if 58 - 58: O0oooo0Oo00
def OoOo ( ) :
 if o00 == 'insert_password' :
  oOOoO0 . ok ( '[COLORsteelblue]Xhoans IPTV Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase ' , ' @ [COLORsteelblue]Xhoans IPTV Media[/COLOR]' )
  I1ii11iIi11i . openSettings ( sys . argv [ 0 ] )
 else :
  OOoO ( )
  if 37 - 37: IIi - iIii1I11I1II1 / o0OOOOO00o0O0
def OOOO ( url ) :
 O0OOoOOO0oO = urllib2 . Request ( url )
 O0OOoOOO0oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1ii11 = urllib2 . urlopen ( O0OOoOOO0oO )
 i1i1Ii1 = I1ii11 . read ( )
 I1ii11 . close ( )
 return i1i1Ii1
def oo0oOOo0 ( ) :
 IIIii1II1II = oOo0oooo00o
 O0OoO0ooOO0o = oOOoO0 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oOooOoOO = O0OoO0ooOO0o . lower ( )
 o0O0OOO0Ooo = OOOO ( IIIii1II1II )
 oo00ooOoO00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( o0O0OOO0Ooo )
 for IIIii1II1II , ooOoO00 , IiI111111IIII , Ii1IIiI1i , i1I1iI in oo00ooOoO00 :
  if OoOo0oOooOoOO in i1I1iI . lower ( ) :
   o0O ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , IIIii1II1II , 15 , ooOoO00 , Ii1IIiI1i , IiI111111IIII )
   iIiiiI . create ( '[COLORsteelblue]' + Iii1ii1II11i + '[/COLOR]' , "Checking Library" , '' , 'Please Wait' )
   iIiiiI . update ( 53 , "" , "Getting Movie Links" )
   if 96 - 96: Ii1ii1
  oOo00O0oo00o0 ( 'tvshows' , 'Media Info 3' )
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
 if 85 - 85: Iiii11I1i1Ii1 . O0oooo0Oo00 / iiiIi1i1I . O0 % IIIii1I1
def OO0ooo0oOO ( ) :
 i1i1Ii1 = OOOO ( i1111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i11i1 = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i1Ii1 )
 for i1I1iI , IIIii1II1II , oo000 , OOO , iiOoO in i11i1 :
  o0O ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , IIIii1II1II , 20 , oo000 , OOO , iiOoO )
 oOo00O0oo00o0 ( 'movies' , 'MAIN' )
def Iiiiii111i1ii ( url ) :
 oOOO00o000o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 iIiiiI = xbmcgui . DialogProgress ( )
 iIiiiI . create ( "Xhoans IPTV" , "Downloading Files" , '' , 'Please Wait' )
 i1ii1II1ii = os . path . join ( oOOO00o000o , 'plugin.video.Xhoans' + '.zip' )
 try :
  os . remove ( i1ii1II1ii )
 except :
  pass
 downloader . download ( url , i1ii1II1ii , iIiiiI )
 i1i1iII1 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 iIiiiI . update ( 0 , "" , "Xhoans IPTV Is Now Installing Files Please Wait" )
 print '======================================='
 print i1i1iII1
 print '======================================='
 extract . all ( i1ii1II1ii , i1i1iII1 , iIiiiI )
 iii11i1IIII ( url )
 O0000o = xbmcgui . Dialog ( )
 O0000o . ok ( "Xhoans IPTV" , "Press ok to force close Xhoans IPTV, If unsuccessful Please press home button got to settings/apps and force close Xhoans IPTV and clear cache. " , "[COLOR yellow]Brought To You By Xhoans IPTV[/COLOR]" )
 Ii ( )
def iii11i1IIII ( url ) :
 print '###' + Iii1ii1II11i + ' - DELETING PACKAGES###'
 o00iiI1Ii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ii1i , oOOoo , iII1111III1I in os . walk ( o00iiI1Ii1 ) :
   ii11i = 0
   ii11i += len ( iII1111III1I )
   if 100 - 100: iiiIi1i1I % iIii1I11I1II1 * oOOO0OOooOoO0Oo - IiiI11Iiiii
   if 92 - 92: iiiIi1i1I
   if ii11i > 0 :
    if 22 - 22: IIi % IiiI11Iiiii * o0OOOOO00o0O0 / Ii1ii1 % i11iIiiIii * ii1I11II1ii1i
    O0000o = xbmcgui . Dialog ( )
    if O0000o . yesno ( "Delete Package Cache Files" , str ( ii11i ) + " files found" , "Do you want to delete them?" ) :
     if 95 - 95: OoooooooOO - I1I1i * II + O0oooo0Oo00
     for IIiII in iII1111III1I :
      os . unlink ( os . path . join ( ii1i , IIiII ) )
     for iIi1 in oOOoo :
      shutil . rmtree ( os . path . join ( ii1i , iIi1 ) )
     O0000o = xbmcgui . Dialog ( )
     O0000o . ok ( Iii1ii1II11i , "       Deleting Packages all done" )
    else :
     pass
   else :
    O0000o = xbmcgui . Dialog ( )
    O0000o . ok ( Iii1ii1II11i , "       No Packages to DELETE" )
 except :
  O0000o = xbmcgui . Dialog ( )
  O0000o . ok ( Iii1ii1II11i , "Error Deleting Packages please visit The Support Group, Xhoans IPTV on facebook" )
 i11iiI1111 ( url )
 return
def i11iiI1111 ( url ) :
 oOoooo000Oo00 = os . path . join ( iI1Ii11111iIi , 'addon_data' )
 OOoo = [
 ( oOoooo000Oo00 ) ,
 ( I1i1iiI1 ) ,
 ( os . path . join ( IiII , 'cache' ) ) ,
 ( os . path . join ( IiII , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( I1i1iiI1 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I1i1iiI1 , 'plugin.video.Xhoans' , 'Images' ) ) ,
 ( os . path . join ( oOoooo000Oo00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOoooo000Oo00 , 'plugin.video.Xhoans' , 'Images' ) ) ]
 if 69 - 69: ii1I11II1ii1i
 O00oO0 = 0
 if 97 - 97: IIIii1I1 - iIii1I11I1II1
 for oo0o0O0Oooooo in OOoo :
  if os . path . exists ( oo0o0O0Oooooo ) and not oo0o0O0Oooooo in [ I1i1iiI1 , oOoooo000Oo00 ] :
   for ii1i , oOOoo , iII1111III1I in os . walk ( oo0o0O0Oooooo ) :
    ii11i = 0
    ii11i += len ( iII1111III1I )
    if ii11i > 0 :
     for IIiII in iII1111III1I :
      if not IIiII in i1i1II :
       try :
        os . unlink ( os . path . join ( ii1i , IIiII ) )
       except :
        pass
      else : O0OOO0OOoO0O ( 'Ignore Log File: %s' % IIiII )
     for iIi1 in oOOoo :
      try :
       shutil . rmtree ( os . path . join ( ii1i , iIi1 ) )
       O00oO0 += 1
       O0OOO0OOoO0O ( "[Success] cleared %s files from %s" % ( str ( ii11i ) , os . path . join ( oo0o0O0Oooooo , iIi1 ) ) )
      except :
       O0OOO0OOoO0O ( "[Failed] to wipe cache in: %s" % os . path . join ( oo0o0O0Oooooo , iIi1 ) )
  else :
   for ii1i , oOOoo , iII1111III1I in os . walk ( oo0o0O0Oooooo ) :
    for iIi1 in oOOoo :
     if 'cache' in iIi1 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( ii1i , iIi1 ) )
       O00oO0 += 1
       O0OOO0OOoO0O ( "[Success] wiped %s " % os . path . join ( oo0o0O0Oooooo , iIi1 ) )
      except :
       O0OOO0OOoO0O ( "[Failed] to wipe cache in: %s" % os . path . join ( oo0o0O0Oooooo , iIi1 ) )
       if 1 - 1: iiiIi1i1I % O0oooo0Oo00 * IIi
 iIIIIii1 ( Iii1ii1II11i , 'Clear Cache: Removed %s Files' % O00oO0 )
def o0O0oo0 ( url ) :
 print '###' + Iii1ii1II11i + ' - DELETING PACKAGES###'
 o00iiI1Ii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ii1i , oOOoo , iII1111III1I in os . walk ( o00iiI1Ii1 ) :
   ii11i = 0
   ii11i += len ( iII1111III1I )
   if 30 - 30: O0 * OoooooooOO
   if 38 - 38: I1I1i - o0OOOOO00o0O0 . O0oooo0Oo00 - IIIii1I1 . OoooooooOO
   if ii11i > 0 :
    if 89 - 89: iIii1I11I1II1
    O0000o = xbmcgui . Dialog ( )
    if O0000o . yesno ( "Delete Package Cache Files" , str ( ii11i ) + " files found" , "Do you want to delete them?" ) :
     if 21 - 21: ii1I11II1ii1i % ii1I11II1ii1i
     for IIiII in iII1111III1I :
      os . unlink ( os . path . join ( ii1i , IIiII ) )
     for iIi1 in oOOoo :
      shutil . rmtree ( os . path . join ( ii1i , iIi1 ) )
     O0000o = xbmcgui . Dialog ( )
     O0000o . ok ( Iii1ii1II11i , "       Deleting Packages all done" )
    else :
     pass
   else :
    O0000o = xbmcgui . Dialog ( )
    O0000o . ok ( Iii1ii1II11i , "       No Packages to DELETE" )
 except :
  O0000o = xbmcgui . Dialog ( )
  O0000o . ok ( Iii1ii1II11i , "Error Deleting Packages" )
 return
 if 27 - 27: i11iIiiIii / o0OOOOO00o0O0
def Ii ( ) :
 O0000o = xbmcgui . Dialog ( )
 oOoOOo = O0000o . yesno ( 'Force Close Xhoans IPTV' , 'You are about to close Xhoans IPTV' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if oOoOOo == 0 : return
 elif oOoOOo == 1 : pass
 ii1iI = ooo000o000 ( )
 O0OOO0OOoO0O ( "Platform: " + str ( ii1iI ) )
 os . _exit ( 1 )
 O0OOO0OOoO0O ( "Force close failed!  Trying alternate methods." )
 if ii1iI == 'osx' :
  O0OOO0OOoO0O ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  O0000o . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif ii1iI == 'linux' :
  O0OOO0OOoO0O ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  O0000o . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif ii1iI == 'android' :
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
  O0000o . ok ( Iii1ii1II11i , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif ii1iI == 'windows' :
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
  O0000o . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  O0OOO0OOoO0O ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  O0OOO0OOoO0O ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  O0000o . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 49 - 49: Iiii11I1i1Ii1 . I1I1i / iI11iiiI1II + oOOO0OOooOoO0Oo
def ii1iii1i ( url ) :
 import urlresolver
 try :
  ii11iIII11II1I1Ii1 = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( ii11iIII11II1I1Ii1 , xbmcgui . ListItem ( i1I1iI ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( i1I1iI ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def ooo000o000 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
 if 72 - 72: IiiI11Iiiii * Ii1III1i11i1i % I1i1iii . OoooooooOO
def O0OOO0OOoO0O ( log ) :
 xbmc . log ( "[%s]: %s" % ( Iii1ii1II11i , log ) )
 if not os . path . exists ( I1i1iiI1 ) : os . makedirs ( I1i1iiI1 )
 if not os . path . exists ( oo00 ) : IIiII = open ( oo00 , 'w' ) ; IIiII . close ( )
 with open ( oo00 , 'a' ) as IIiII :
  OoO0O0O0o00 = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  IIiII . write ( OoO0O0O0o00 . rstrip ( '\r\n' ) + '\n' )
  if 7 - 7: II + O0oooo0Oo00 / I1I1i
def OOOoO000 ( ) :
 try :
  oOOOO = getSet ( "core-player" )
  if ( oOOOO == 'DVDPLAYER' ) : IiIi1ii111i1 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oOOOO == 'MPLAYER' ) : IiIi1ii111i1 = xbmc . PLAYER_CORE_MPLAYER
  elif ( oOOOO == 'PAPLAYER' ) : IiIi1ii111i1 = xbmc . PLAYER_CORE_PAPLAYER
  else : IiIi1ii111i1 = xbmc . PLAYER_CORE_AUTO
 except : IiIi1ii111i1 = xbmc . PLAYER_CORE_AUTO
 return IiIi1ii111i1
 return True
 if 31 - 31: Ii1ii1 + O0
 if 87 - 87: iiiIi1i1I
def iI ( name , url , mode , iconimage , fanart , description ) :
 if 45 - 45: iI11iiiI1II / OoooooooOO - IiiI11Iiiii / I1i1iii % I1I1i
 IiII111i1i11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i111iIi1i1II1 = True
 oooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oooO . setProperty ( "Fanart_Image" , fanart )
 i111iIi1i1II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiII111i1i11 , listitem = oooO , isFolder = True )
 return i111iIi1i1II1
 if 83 - 83: II . iIii1I11I1II1 - I1I1i * i11iIiiIii
def o0O ( name , url , mode , iconimage , fanart , description ) :
 if 20 - 20: i1IIi * IIIii1I1 + oOOO0OOooOoO0Oo % Iiii11I1i1Ii1 % Ii1III1i11i1i
 IiII111i1i11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i111iIi1i1II1 = True
 oooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oooO . setProperty ( "Fanart_Image" , fanart )
 i111iIi1i1II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiII111i1i11 , listitem = oooO , isFolder = False )
 return i111iIi1i1II1
 if 13 - 13: IIi
def oOOo000oOoO0 ( ) :
 OoOo00o0OO = [ ]
 ii1IIIIiI11 = sys . argv [ 2 ]
 if len ( ii1IIIIiI11 ) >= 2 :
  iI1IIIii = sys . argv [ 2 ]
  I1i11ii11 = iI1IIIii . replace ( '?' , '' )
  if ( iI1IIIii [ len ( iI1IIIii ) - 1 ] == '/' ) :
   iI1IIIii = iI1IIIii [ 0 : len ( iI1IIIii ) - 2 ]
  OO00O0oOO = I1i11ii11 . split ( '&' )
  OoOo00o0OO = { }
  for Ii1iI111 in range ( len ( OO00O0oOO ) ) :
   O0oooo00o0Oo = { }
   O0oooo00o0Oo = OO00O0oOO [ Ii1iI111 ] . split ( '=' )
   if ( len ( O0oooo00o0Oo ) ) == 2 :
    OoOo00o0OO [ O0oooo00o0Oo [ 0 ] ] = O0oooo00o0Oo [ 1 ]
    if 36 - 36: I1i1iii / oOOO0OOooOoO0Oo / I1I1i / I1I1i + o0OOOOO00o0O0
 return OoOo00o0OO
 if 95 - 95: I1I1i
 if 51 - 51: oOOO0OOooOoO0Oo + I1I1i . i1IIi . o0OOOOO00o0O0 + O0oooo0Oo00 * II
iI1IIIii = oOOo000oOoO0 ( )
IIIii1II1II = None
i1I1iI = None
OOoOoo0 = None
oo000 = None
OOO = None
iiOoO = None
I1iIII1 = None
if 39 - 39: OoooooooOO
if 38 - 38: II
try :
 I1iIII1 = int ( iI1IIIii [ "fav_mode" ] )
except :
 pass
 if 84 - 84: Ii1III1i11i1i % i1IIi
try :
 IIIii1II1II = urllib . unquote_plus ( iI1IIIii [ "url" ] )
except :
 pass
try :
 i1I1iI = urllib . unquote_plus ( iI1IIIii [ "name" ] )
except :
 pass
try :
 oo000 = urllib . unquote_plus ( iI1IIIii [ "iconimage" ] )
except :
 pass
try :
 OOoOoo0 = int ( iI1IIIii [ "mode" ] )
except :
 pass
try :
 OOO = urllib . unquote_plus ( iI1IIIii [ "fanart" ] )
except :
 pass
try :
 iiOoO = urllib . unquote_plus ( iI1IIIii [ "description" ] )
except :
 pass
 if 70 - 70: IIi . OoooooooOO - IiiI11Iiiii
 if 30 - 30: o0OOOOO00o0O0 % II
print str ( oO ) + ': ' + str ( i1iII1IiiIiI1 )
print "Mode: " + str ( OOoOoo0 )
print "URL: " + str ( IIIii1II1II )
print "Name: " + str ( i1I1iI )
print "IconImage: " + str ( oo000 )
if 89 - 89: IIIii1I1 + OoooooooOO + IIIii1I1 * i1IIi + iIii1I11I1II1 % ii1I11II1ii1i
if 59 - 59: Ii1ii1 + i11iIiiIii
def oOo00O0oo00o0 ( content , viewType ) :
 if 88 - 88: i11iIiiIii - iiiIi1i1I
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if I1ii11iIi11i . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % I1ii11iIi11i . getSetting ( viewType ) )
  if 67 - 67: Ii1ii1 . IIi + O0oooo0Oo00 - OoooooooOO
  if 70 - 70: Ii1ii1 / oOOO0OOooOoO0Oo - iIii1I11I1II1 - IiiI11Iiiii
if OOoOoo0 == None : oOO00oOO ( )
elif OOoOoo0 == 1 : Genres ( )
elif OOoOoo0 == 2 : Lists ( IIIii1II1II , oo000 )
elif OOoOoo0 == 3 : all_mov ( )
elif OOoOoo0 == 4 : oo0oOOo0 ( )
elif OOoOoo0 == 5 : O00 ( )
elif OOoOoo0 == 6 : o0O0oo0 ( IIIii1II1II )
elif OOoOoo0 == 7 : i11iiI1111 ( IIIii1II1II )
elif OOoOoo0 == 8 : Ii ( )
elif OOoOoo0 == 9 : oo0 ( )
elif OOoOoo0 == 10 : OO0OOOOoo0OOO ( )
elif OOoOoo0 == 11 : TvGuide ( )
elif OOoOoo0 == 12 : OoOo ( )
elif OOoOoo0 == 13 : ReCreate_Addon_ini ( )
elif OOoOoo0 == 14 : iiIiI ( IIIii1II1II )
elif OOoOoo0 == 144 : I1I1I ( IIIii1II1II )
elif OOoOoo0 == 15 : ii1iii1i ( IIIii1II1II )
elif OOoOoo0 == 16 : o00oooO0Oo ( )
elif OOoOoo0 == 17 : Live_Events ( i1I1iI )
elif OOoOoo0 == 18 : I1ii11iIi11i . openSettings ( sys . argv [ 0 ] )
elif OOoOoo0 == 19 : OO0ooo0oOO ( )
elif OOoOoo0 == 20 : Iiiiii111i1ii ( IIIii1II1II )
elif OOoOoo0 == 30 : iiIiI1i1 ( )
elif OOoOoo0 == 31 : o00O0O ( IIIii1II1II )
elif OOoOoo0 == 40 : OO ( )
elif OOoOoo0 == 41 : iIiIIi1 ( IIIii1II1II )
elif OOoOoo0 == 21 : Iii1I1111ii ( IIIii1II1II )
elif OOoOoo0 == 22 : o0O00Oo0 ( IIIii1II1II )
elif OOoOoo0 == 50 : OooOooo ( )
elif OOoOoo0 == 51 : oo0OooOOo0 ( IIIii1II1II )
elif OOoOoo0 == 50000 : oo000OO00Oo ( )
elif OOoOoo0 == 50001 : iII111i ( )
elif OOoOoo0 == 50002 : OO0oOOoo ( IIIii1II1II )
elif OOoOoo0 == 60001 : oOoOoOoo0 ( )
elif OOoOoo0 == 60002 : iiIi1iI1iIii ( i1I1iI , IIIii1II1II )
elif OOoOoo0 == 90026 : o0OO0o0o00o ( )
elif OOoOoo0 == 90027 : i1i11I11 ( i1I1iI , IIIii1II1II , iiOoO )
elif OOoOoo0 == 90028 : IIi1IIIi ( IIIii1II1II )
if 11 - 11: iIii1I11I1II1 . OoooooooOO . oOOO0OOooOoO0Oo / i1IIi - ii1I11II1ii1i
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
