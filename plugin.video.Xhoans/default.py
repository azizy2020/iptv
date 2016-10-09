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
from urllib2 import urlopen
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup , BeautifulSOAP
from cookielib import CookieJar
from addon . common . addon import Addon
from addon . common . net import Net
from imports . tvGuide import gui
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
i1I1ii1II1iII = 'plugin.video.Xhoans'
oooO0oo0oOOOO = 'plugin.video.Xhoans'
O0oO = xbmc . translatePath ( 'special://home/addons/' )
o0oO0 = xbmc . translatePath ( 'special://home/addonsbroke/' )
oo00 = xbmcaddon . Addon ( id = oooO0oo0oOOOO )
o00 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
oooO0oo0oOOOO = 'plugin.video.Xhoans'
Oo0oO0ooo = 'plugin.video.Xhoans'
o0oOoO00o = xbmcgui . DialogProgress ( )
i1 = "Xhoans IPTV"
oOOoo00O0O = Net ( )
i1111 = base64 . decodestring
i11 = oo00 . getSetting ( 'User' )
I11 = oo00 . getSetting ( 'Pass' )
Oo0o0000o0o0 = oo00 . getSetting ( 'AdultPass' )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
oO0o0o0ooO0oO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oooO0oo0oOOOO , 'icon.png' ) )
oo0o0O00 = ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQv' ) )
oO = "0.0.5"
i1iiIIiiI111 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.Xhoans' )
oooOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.Xhoans/imports/tvGuide/ResetDatabase.py' ) )
i1iiIII111ii = xbmc . translatePath ( 'special://thumbnails' ) ;
i1iIIi1 = "Xhoans"
ii11iIi1I = ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vUGllVHYv' ) )
iI111I11I1I1 = ii11iIi1I + 'fanart.jpg'
OOooO0OOoo = base64 . decodestring ( 'LnBocA==' )
iIii1 = oo00 . getLocalizedString
oOOoO0 = CookieJar ( )
O0OoO000O0OO = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( oOOoO0 ) )
O0OoO000O0OO . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
iiI1IiI = int ( sys . argv [ 1 ] )
II = xbmc . translatePath ( oo00 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
ooOoOoo0O = xbmc . translatePath ( 'special://home/userdata/' )
OooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
II11iiii1Ii = i1iiIIiiI111 + '/addons.ini'
OO0o = xbmcgui . Dialog ( )
Ooo = ''
def O0o0Oo ( i , t1 , t2 = [ ] ) :
 Oo00OOOOO = Ooo
 for O0O in t1 :
  Oo00OOOOO += chr ( O0O )
  i += 1
  if i > 1 :
   Oo00OOOOO = Oo00OOOOO [ : - 1 ]
   i = 0
 for O0O in t2 :
  Oo00OOOOO += chr ( O0O )
  i += 1
  if i > 1 :
   Oo00OOOOO = Oo00OOOOO [ : - 1 ]
   i = 0
 return Oo00OOOOO
def O00o0OO ( ) :
 I11i1 ( )
 iIi1ii1I1 ( 'Tv Guide' , '' , 11 , ii11iIi1I + 'TVGUIDE.png' , iI111I11I1I1 , '' )
 iIi1ii1I1 ( 'Link Streams to Guide' , '' , 13 , ii11iIi1I + 'LINKSTREAMS.png' , iI111I11I1I1 , '' )
 o0 ( 'Stream Lists' , '' , 16 , ii11iIi1I + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'Live Sport On Xhoans IPTV' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 17 , ii11iIi1I + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 if 9 - 9: Ii1I + oO0o % Ii1I + i1IIi . OOooOOo
 if 31 - 31: o0oOOo0O0Ooo + I11i + I11i / II111iiii
def I11i1 ( ) :
 if I11 == 'insert_password' :
  OO0o . ok ( 'Please Login' , 'You need to set username and password to access this' , 'These are unique and provided only to subscribers of' , 'Xhoans IPTV' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  iiI1 = open ( II11iiii1Ii )
  i11Iiii = re . compile ( 'plugin.video.Xhoans.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( iiI1 ) )
  for iI , I1i1I1II in i11Iiii :
   if iI == 'needs replacing' or I1i1I1II == 'needs replacing' :
    i1IiIiiI ( )
    OO0o . ok ( '[COLOR=yellow]Need to set login details' , 'You need to input your login details to activate streams' , '' )
    oo00 . openSettings ( sys . argv [ 0 ] )
    if 31 - 31: Ii1I . Ii1I - o0oOOo0O0Ooo / OoO0O00 + ooOoO0o * I1IiiI
    if 63 - 63: I1Ii111 % i1IIi / OoooooooOO - OoooooooOO
def iIii11I ( ) :
 o0 ( 'Full List' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'PPV' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'Entertainment' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'Factual' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'Movie Channels' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'US Movie Channels TEST' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'Kids' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'Music' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'UK Sports' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'International Sports' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'US Sports Live Event/Ticket/Pass' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'News UK & International' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'German' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'Arabic' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'TV Series Latest' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'VOD Latest' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 o0 ( 'VOD Bollywood' , '' , 14 , oo0o0O00 + 'STREAMLISTS.png' , iI111I11I1I1 , '' )
 if 69 - 69: oO0o % I1Ii111 - o0oOOo0O0Ooo + I1Ii111 - O0 % OoooooooOO
 if 31 - 31: II111iiii - OOooOOo . I1Ii111 % OoOoOO00 - O0
def iii11 ( ) :
 OO0o . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + oooOOOOO + ")" )
 i1IiIiiI ( )
 OO0o . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your streams' )
 if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
def ii11i1 ( url ) :
 IIIii1II1II = i1I1iI ( url )
 i11Iiii = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIii1II1II )
 for oo0OooOOo0 , o0O , url in i11Iiii :
  url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + i11 + '/' + I11 + url ) . strip ( )
  iIi1ii1I1 ( ( o0O ) . replace ( '_' , ' ' ) . replace ( 'G-Tv' , 'Xhoans IPTV' ) . replace ( '(ULTIMATE ONLY)' , '' ) , url , 15 , oo0OooOOo0 , O00oO , '' )
def I11i1I1I ( name ) :
 oO0Oo = name
 IIIii1II1II = i1I1iI ( 'http://piesustv.net:8000/get.php?username=' + i11 + '&password=' + I11 + '&type=m3u_plus&output=mpegts' )
 i11Iiii = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( IIIii1II1II )
 for name , oo0OooOOo0 , oOOoo0Oo , o00OO00OoO in i11Iiii :
  if oO0Oo == 'Full List' :
   o00OO00OoO = ( o00OO00OoO ) . replace ( '.ts' , '.m3u8' )
   iIi1ii1I1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( o00OO00OoO ) . strip ( ) , 15 , oo0OooOOo0 , oo0OooOOo0 , '' )
  else :
   oO0Oo = ( oO0Oo ) . replace ( 'World' , 'القنوات العربية' )
   if oO0Oo in oOOoo0Oo :
    o00OO00OoO = ( o00OO00OoO ) . replace ( '.ts' , '.m3u8' )
    print o00OO00OoO + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    iIi1ii1I1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( o00OO00OoO ) . strip ( ) , 15 , oo0OooOOo0 , oo0OooOOo0 , '' )
   else :
    pass
def OOOO0OOoO0O0 ( ) :
 i1IiIiiI ( )
 try :
  O0Oo000ooO00 = gui . TVGuide ( )
  O0Oo000ooO00 . doModal ( )
  del O0Oo000ooO00
  if 75 - 75: oO0o . OoO0O00 * OOooOOo
 except :
  import sys
  import traceback as tb
  ( ooOoOO0oo0O , IIi , traceback ) = sys . exc_info ( )
  tb . print_exception ( ooOoOO0oo0O , IIi , traceback )
  if 26 - 26: iII111i
def i1I1iI ( url ) :
 OOO = urllib2 . Request ( url )
 OOO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Oo0oOOo = urllib2 . urlopen ( OOO )
 Oo0OoO00oOO0o = Oo0oOOo . read ( )
 Oo0oOOo . close ( )
 return Oo0OoO00oOO0o
 if 80 - 80: oO0o + OOooOOo - OOooOOo % iII111i
 if 63 - 63: I1IiiI - I1ii11iIi11i + O0 % I11i / iIii1I11I1II1 / o0oOOo0O0Ooo
 if 98 - 98: iII111i * iII111i / iII111i + I11i
def i1IiIiiI ( ) :
 ii111111I1iII = os . path . join ( i1iiIIiiI111 , 'addons.ini' )
 O00ooo0O0 = open ( ii111111I1iII , "w+" )
 IIIii1II1II = i1I1iI ( 'http://piesustv.net:8000/get.php?username=' + i11 + '&password=' + I11 + '&type=m3u_plus&output=mpegts' )
 i11Iiii = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( IIIii1II1II )
 O00ooo0O0 . write ( r'[' + i1I1ii1II1iII + ']' + '\n' )
 for o0O , oo0OooOOo0 , oOOoo0Oo , o00OO00OoO in i11Iiii :
  o00OO00OoO = ( o00OO00OoO + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  i1iIi1iIi1i = ( o0O + '=plugin://' + i1I1ii1II1iII + '/?url=' + o00OO00OoO + '&mode=15&name=' + ( o0O ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( oo0OooOOo0 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( oo0OooOOo0 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  O00ooo0O0 . write ( i1iIi1iIi1i + '\n' )
  if 46 - 46: I1Ii111 % I11i + OoO0O00 . OoOoOO00 . OoO0O00
  if 96 - 96: Oo0Ooo
def Ii1I1IIii1II ( url ) :
 O0ii1ii1ii = xbmc . Player ( oooooOoo0ooo ( ) )
 import urlresolver
 try : O0ii1ii1ii . play ( url ) . strip ( )
 except : pass
 if 6 - 6: I11i - Ii1I + iIii1I11I1II1 - I1Ii111 - i11iIiiIii
 if 79 - 79: OoOoOO00 - O0 * OoO0O00 + OoOoOO00 % O0 * O0
def oooooOoo0ooo ( ) :
 try :
  oOOo0 = getSet ( "core-player" )
  if ( oOOo0 == 'DVDPLAYER' ) : oo00O00oO = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oOOo0 == 'MPLAYER' ) : oo00O00oO = xbmc . PLAYER_CORE_MPLAYER
  elif ( oOOo0 == 'PAPLAYER' ) : oo00O00oO = xbmc . PLAYER_CORE_PAPLAYER
  else : oo00O00oO = xbmc . PLAYER_CORE_AUTO
 except : oo00O00oO = xbmc . PLAYER_CORE_AUTO
 return oo00O00oO
 return True
 if 23 - 23: OoO0O00 + OoO0O00 . OOooOOo
 if 38 - 38: I1Ii111
def o0 ( name , url , mode , iconimage , fanart , description ) :
 if 7 - 7: O0 . iII111i % I1ii11iIi11i - I1IiiI - iIii1I11I1II1
 I111IIIiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0000OOo00 = True
 iiIi1IIiIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIi1IIiIi . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIi1IIiIi . setProperty ( "Fanart_Image" , fanart )
 oO0000OOo00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIIiIii , listitem = iiIi1IIiIi , isFolder = True )
 return oO0000OOo00
 if 75 - 75: I1IiiI + Oo0Ooo
def iIi1ii1I1 ( name , url , mode , iconimage , fanart , description ) :
 if 73 - 73: O0 - OoooooooOO . OOooOOo - OOooOOo / OoOoOO00
 I111IIIiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0000OOo00 = True
 iiIi1IIiIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIi1IIiIi . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIi1IIiIi . setProperty ( "Fanart_Image" , fanart )
 oO0000OOo00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIIiIii , listitem = iiIi1IIiIi , isFolder = False )
 return oO0000OOo00
 if 45 - 45: iIii1I11I1II1 % OoO0O00
def I1iIIii ( ) :
 iii1i = [ ]
 I11i1ii1 = sys . argv [ 2 ]
 if len ( I11i1ii1 ) >= 2 :
  O0Oooo0O = sys . argv [ 2 ]
  O0o = O0Oooo0O . replace ( '?' , '' )
  if ( O0Oooo0O [ len ( O0Oooo0O ) - 1 ] == '/' ) :
   O0Oooo0O = O0Oooo0O [ 0 : len ( O0Oooo0O ) - 2 ]
  OoOooO = O0o . split ( '&' )
  iii1i = { }
  for II111iiiI1Ii in range ( len ( OoOooO ) ) :
   o0O0OOO0Ooo = { }
   o0O0OOO0Ooo = OoOooO [ II111iiiI1Ii ] . split ( '=' )
   if ( len ( o0O0OOO0Ooo ) ) == 2 :
    iii1i [ o0O0OOO0Ooo [ 0 ] ] = o0O0OOO0Ooo [ 1 ]
    if 45 - 45: O0 / o0oOOo0O0Ooo
 return iii1i
 if 32 - 32: iII111i . IiII . IiII
 if 62 - 62: I1ii11iIi11i + IiII % iII111i + OOooOOo
O0Oooo0O = I1iIIii ( )
o00OO00OoO = None
o0O = None
iii = None
oOooOOOoOo = None
O00oO = None
i1Iii1i1I = None
OOoO00 = None
if 40 - 40: I1IiiI * Ii1I + OOooOOo % iII111i
if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + I1Ii111 / OoOoOO00
try :
 OOoO00 = int ( O0Oooo0O [ "fav_mode" ] )
except :
 pass
 if 23 - 23: O0
try :
 o00OO00OoO = urllib . unquote_plus ( O0Oooo0O [ "url" ] )
except :
 pass
try :
 o0O = urllib . unquote_plus ( O0Oooo0O [ "name" ] )
except :
 pass
try :
 oOooOOOoOo = urllib . unquote_plus ( O0Oooo0O [ "iconimage" ] )
except :
 pass
try :
 iii = int ( O0Oooo0O [ "mode" ] )
except :
 pass
try :
 O00oO = urllib . unquote_plus ( O0Oooo0O [ "fanart" ] )
except :
 pass
try :
 i1Iii1i1I = urllib . unquote_plus ( O0Oooo0O [ "description" ] )
except :
 pass
 if 85 - 85: Ii1I
 if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii1I % OoooooooOO % OoO0O00
print str ( i1iIIi1 ) + ': ' + str ( oO )
print "Mode: " + str ( iii )
print "URL: " + str ( o00OO00OoO )
print "Name: " + str ( o0O )
print "IconImage: " + str ( oOooOOOoOo )
if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + iII111i / OoOoOO00
if 84 - 84: ooOoO0o * II111iiii + Oo0Ooo
def O0ooO0Oo00o ( content , viewType ) :
 if 77 - 77: iIii1I11I1II1 * OoO0O00
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 95 - 95: I1IiiI + i11iIiiIii
  if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
if iii == None : O00o0OO ( )
elif iii == 11 : OOOO0OOoO0O0 ( )
elif iii == 12 : I11i1 ( )
elif iii == 13 : iii11 ( )
elif iii == 14 : I11i1I1I ( o0O )
elif iii == 15 : Ii1I1IIii1II ( o00OO00OoO )
elif iii == 16 : iIii11I ( )
elif iii == 17 : ii11i1 ( o00OO00OoO )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
