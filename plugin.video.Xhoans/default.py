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
o0OO00 = ''
def oo ( i , t1 , t2 = [ ] ) :
 i1iII1IiiIiI1 = o0OO00
 for iIiiiI1IiI1I1 in t1 :
  i1iII1IiiIiI1 += chr ( iIiiiI1IiI1I1 )
  i += 1
  if i > 1 :
   i1iII1IiiIiI1 = i1iII1IiiIiI1 [ : - 1 ]
   i = 0
 for iIiiiI1IiI1I1 in t2 :
  i1iII1IiiIiI1 += chr ( iIiiiI1IiI1I1 )
  i += 1
  if i > 1 :
   i1iII1IiiIiI1 = i1iII1IiiIiI1 [ : - 1 ]
   i = 0
 return i1iII1IiiIiI1
 if 87 - 87: OoOoOO00
 if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
 if 73 - 73: OOooOOo / ii11ii1ii
O00ooOO = 'plugin.video.Xhoans'
I1iII1iiII = 'plugin.video.Xhoans'
iI1Ii11111iIi = xbmc . translatePath ( 'special://home/addons/' )
i1i1II = xbmc . translatePath ( 'special://home/addonsbroke/' )
O0oo0OO0 = xbmcaddon . Addon ( id = O00ooOO )
I1i1iiI1 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
O00ooOO = 'plugin.video.Xhoans'
iiIIIII1i1iI = 'plugin.video.Xhoans'
o0oO0 = xbmcgui . DialogProgress ( )
oo00 = "Xhoans IPTV"
o00 = Net ( )
Oo0oO0ooo = base64 . decodestring
o0oOoO00o = O0oo0OO0 . getSetting ( 'User' )
i1 = O0oo0OO0 . getSetting ( 'Pass' )
oOOoo00O0O = O0oo0OO0 . getSetting ( 'AdultPass' )
i1111 = xbmc . translatePath ( 'special://home/' )
i11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + O00ooOO , 'icon.png' ) )
I11 = ( Oo0oO0ooo ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQv' ) )
Oo0o0000o0o0 = "0.0.3"
oOo0oooo00o = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.Xhoans' )
oO0o0o0ooO0oO = xbmc . translatePath ( 'special://thumbnails' ) ;
oo0o0O00 = "Xhoans"
oO = ( Oo0oO0ooo ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vUGllVHYv' ) )
i1iiIIiiI111 = oO + 'fanart.jpg'
oooOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.Xhoans/imports/tvGuide/ResetDatabase.py' ) )
i1iiIII111ii = base64 . decodestring ( 'LnBocA==' )
i1iIIi1 = O0oo0OO0 . getLocalizedString
ii11iIi1I = CookieJar ( )
iI111I11I1I1 = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( ii11iIi1I ) )
iI111I11I1I1 . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
OOooO0OOoo = int ( sys . argv [ 1 ] )
iIii1 = xbmc . translatePath ( O0oo0OO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
oOOoO0 = xbmc . translatePath ( 'special://home/userdata/' )
O0OoO000O0OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
iiI1IiI = oOo0oooo00o + '/addons.ini'
II = xbmcgui . Dialog ( )
if 57 - 57: ooOoo0O
def OooO0 ( ) :
 II11iiii1Ii ( )
 OO0o ( 'Tv Guide' , '' , 11 , oO + 'TVGUIDE.png' , i1iiIIiiI111 , '' )
 OO0o ( 'Link Streams to Guide' , '' , 13 , oO + 'LINKSTREAMS.png' , i1iiIIiiI111 , '' )
 Ooo ( 'Stream Lists' , '' , 16 , oO + 'STREAMLISTS.png' , i1iiIIiiI111 , '' )
 if 68 - 68: oOo00Oo00O + I11i1I + o0o0OOO0o0 % IIII % o0O0 . o0
 if 9 - 9: OO0oo0oOO + Ooo00oOo00o - OOOo0 % OoOoOO00 % OoOoOO00
def II11iiii1Ii ( ) :
 if i1 == 'insert_password' :
  II . ok ( 'Please Login' , 'You need to set username and password to access this' , 'These are unique and provided only to subscribers of' , 'Xhoans IPTV' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
 else :
  iI1 = open ( iiI1IiI , "r" )
  i11Iiii = re . compile ( 'plugin.video.Xhoans.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( iI1 ) )
  for iI , I1i1I1II in i11Iiii :
   if iI == 'replace_user' or I1i1I1II == 'replace_pass' :
    II . ok ( '[COLOR=yellow]Need to set login details' , 'You need to input your login details to activate streams' , '' )
    O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
    if 45 - 45: o0 . I1IiI
    if 83 - 83: ooOoo0O . iIii1I11I1II1 . ii11ii1ii
def I1I ( ) :
 Ooo ( 'Full List' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 Ooo ( 'PPV' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 Ooo ( 'Entertainment' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 Ooo ( 'Factual' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 Ooo ( 'Movie Channels' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 Ooo ( 'US Movie Channels TEST' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 Ooo ( 'Kids' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 Ooo ( 'Music' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 Ooo ( 'UK Sports' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 Ooo ( 'International Sports' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 Ooo ( 'News UK & International' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 Ooo ( 'German' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 Ooo ( 'Arabic' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 Ooo ( 'TV Series Latest' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 Ooo ( 'VOD Latest' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 Ooo ( 'VOD Bollywood' , '' , 14 , I11 + 'UltimateList.png' , i1iiIIiiI111 , '' )
 if 80 - 80: I1IiI - Ooo00oOo00o
 if 87 - 87: ooOoo0O / I11i1I - i1IIi * oOo00Oo00O / OoooooooOO . O0
def iii11I111 ( name ) :
 OOOO00ooo0Ooo = name
 OOOooOooo00O0 = Oo0OO ( 'http://piesustv.net:8000/get.php?username=' + o0oOoO00o + '&password=' + i1 + '&type=m3u_plus&output=mpegts' )
 i11Iiii = re . compile ( '#EXTINF:.+?tvg-name="(.+?)" tvg-logo="(.+?)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( OOOooOooo00O0 )
 for name , oOOoOo00o , o0OOoo0OO0OOO in i11Iiii :
  o0OOoo0OO0OOO = ( o0OOoo0OO0OOO ) . replace ( 'replace_user' , o0oOoO00o ) . replace ( 'replace_pass' , i1 )
  OO0o ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( o0OOoo0OO0OOO ) . strip ( ) , 15 , oOOoOo00o , oOOoOo00o , '' )
 else :
  OO0o ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 15 , '' , '' , '' )
  if 19 - 19: ooOoo0O % i1IIi % OOooOOo
def oo0OooOOo0 ( ) :
 II . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + oooOOOOO + ")" )
 o0O ( )
 II . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 72 - 72: IIII / i1IIi * Oo - o0
 if 51 - 51: OoOoOO00 * Ooo00oOo00o % OOooOOo * OoOoOO00 % ii11ii1ii / OO0oo0oOO
def iIIIIii1 ( name ) :
 OOOO00ooo0Ooo = name
 OOOooOooo00O0 = Oo0OO ( 'http://piesustv.net:8000/get.php?username=' + o0oOoO00o + '&password=' + i1 + '&type=m3u_plus&output=mpegts' )
 i11Iiii = re . compile ( '#EXTINF:.+?tvg-name="(.+?)" tvg-logo="(.+?)" group-title="(.+?)"",.+?\n(.+?)\n' ) . findall ( OOOooOooo00O0 )
 for name , oOOoOo00o , oo000OO00Oo , o0OOoo0OO0OOO in i11Iiii :
  if OOOO00ooo0Ooo == 'Full List' :
   o0OOoo0OO0OOO = ( o0OOoo0OO0OOO ) . replace ( 'replace_user' , o0oOoO00o ) . replace ( 'replace_pass' , i1 ) . replace ( '.ts' , '.m3u8' )
   OO0o ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( o0OOoo0OO0OOO ) . strip ( ) , 15 , oOOoOo00o , oOOoOo00o , '' )
  else :
   OOOO00ooo0Ooo = ( OOOO00ooo0Ooo ) . replace ( 'World' , 'القنوات العربية' )
   if OOOO00ooo0Ooo in oo000OO00Oo :
    o0OOoo0OO0OOO = ( o0OOoo0OO0OOO ) . replace ( 'replace_user' , o0oOoO00o ) . replace ( 'replace_pass' , i1 )
    print o0OOoo0OO0OOO + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    OO0o ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( o0OOoo0OO0OOO ) . strip ( ) , 15 , oOOoOo00o , oOOoOo00o , '' )
   else :
    pass
def O0OOO0OOoO0O ( ) :
 o0O ( )
 try :
  O00Oo000ooO0 = gui . TVGuide ( )
  O00Oo000ooO0 . doModal ( )
  del O00Oo000ooO0
  if 100 - 100: O0 + o0O0 - oOo00Oo00O + i11iIiiIii * o0o0OOO0o0
 except :
  import sys
  import traceback as tb
  ( iII , o0ooOooo000oOO , traceback ) = sys . exc_info ( )
  tb . print_exception ( iII , o0ooOooo000oOO , traceback )
  if 59 - 59: OoOoOO00 + OoooooooOO * I1IiI + i1IIi
def Oo0OO ( url ) :
 Oo0OoO00oOO0o = urllib2 . Request ( url )
 Oo0OoO00oOO0o . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOO00O = urllib2 . urlopen ( Oo0OoO00oOO0o )
 OOoOO0oo0ooO = OOO00O . read ( )
 OOO00O . close ( )
 return OOoOO0oo0ooO
 if 98 - 98: IIII * IIII / IIII + I11i1I
 if 34 - 34: OO0oo0oOO
 if 15 - 15: I11i1I * OO0oo0oOO * Oo % i11iIiiIii % I1IiI - oOo00Oo00O
def o0O ( ) :
 O0ooo0O0oo0 = os . path . join ( oOo0oooo00o , 'addons.ini' )
 oo0oOo = open ( O0ooo0O0oo0 , "w+" )
 OOOooOooo00O0 = Oo0OO ( 'http://piesustv.net:8000/get.php?username=' + o0oOoO00o + '&password=' + i1 + '&type=m3u_plus&output=mpegts' )
 i11Iiii = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( OOOooOooo00O0 )
 oo0oOo . write ( r'[' + I1iII1iiII + ']' + '\n' )
 for o000O0o , oOOoOo00o , oo000OO00Oo , o0OOoo0OO0OOO in i11Iiii :
  o0OOoo0OO0OOO = ( o0OOoo0OO0OOO + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  iI1iII1 = ( o000O0o + '=plugin://' + I1iII1iiII + '/?url=' + o0OOoo0OO0OOO + '&mode=15&name=' + ( o000O0o ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( oOOoOo00o ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( oOOoOo00o ) . replace ( ' ' , '' ) + '+&amp;description=' )
  oo0oOo . write ( iI1iII1 + '\n' )
  if 86 - 86: oOo00Oo00O
def OOoo0O ( url ) :
 Oo0ooOo0o = xbmc . Player ( Ii1i1 ( ) )
 import urlresolver
 try : Oo0ooOo0o . play ( url ) . strip ( )
 except : pass
 if 15 - 15: OoOoOO00
 if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
def Ii1i1 ( ) :
 try :
  OO0OoO0o00 = getSet ( "core-player" )
  if ( OO0OoO0o00 == 'DVDPLAYER' ) : ooOO0O0ooOooO = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( OO0OoO0o00 == 'MPLAYER' ) : ooOO0O0ooOooO = xbmc . PLAYER_CORE_MPLAYER
  elif ( OO0OoO0o00 == 'PAPLAYER' ) : ooOO0O0ooOooO = xbmc . PLAYER_CORE_PAPLAYER
  else : ooOO0O0ooOooO = xbmc . PLAYER_CORE_AUTO
 except : ooOO0O0ooOooO = xbmc . PLAYER_CORE_AUTO
 return ooOO0O0ooOooO
 return True
 if 55 - 55: OOooOOo * I1IiI
 if 61 - 61: I11i1I
def Ooo ( name , url , mode , iconimage , fanart , description ) :
 if 86 - 86: I11i1I % I1IiI / OOOo0 / I1IiI
 iIIi1i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1IIIiiII1 = True
 OOOOoOoo0O0O0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOOOoOoo0O0O0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOOOoOoo0O0O0 . setProperty ( "Fanart_Image" , fanart )
 i1IIIiiII1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIi1i1 , listitem = OOOOoOoo0O0O0 , isFolder = True )
 return i1IIIiiII1
 if 85 - 85: ooOoo0O % i11iIiiIii - IIII * OoooooooOO / OOOo0 % OOOo0
def OO0o ( name , url , mode , iconimage , fanart , description ) :
 if 1 - 1: Ooo00oOo00o - ooOoo0O . I11i1I . Ooo00oOo00o / Oo + I11i1I
 iIIi1i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1IIIiiII1 = True
 OOOOoOoo0O0O0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOOOoOoo0O0O0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOOOoOoo0O0O0 . setProperty ( "Fanart_Image" , fanart )
 i1IIIiiII1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIi1i1 , listitem = OOOOoOoo0O0O0 , isFolder = False )
 return i1IIIiiII1
 if 78 - 78: O0 . ooOoo0O . OoOoOO00 % oOo00Oo00O
def i1iIi ( ) :
 ooOOoooooo = [ ]
 II1I = sys . argv [ 2 ]
 if len ( II1I ) >= 2 :
  O0i1II1Iiii1I11 = sys . argv [ 2 ]
  IIIIiiIiI = O0i1II1Iiii1I11 . replace ( '?' , '' )
  if ( O0i1II1Iiii1I11 [ len ( O0i1II1Iiii1I11 ) - 1 ] == '/' ) :
   O0i1II1Iiii1I11 = O0i1II1Iiii1I11 [ 0 : len ( O0i1II1Iiii1I11 ) - 2 ]
  o00oooO0Oo = IIIIiiIiI . split ( '&' )
  ooOOoooooo = { }
  for o0O0OOO0Ooo in range ( len ( o00oooO0Oo ) ) :
   iiIiI = { }
   iiIiI = o00oooO0Oo [ o0O0OOO0Ooo ] . split ( '=' )
   if ( len ( iiIiI ) ) == 2 :
    ooOOoooooo [ iiIiI [ 0 ] ] = iiIiI [ 1 ]
    if 6 - 6: o0O0 . ooOoo0O * I1IiI - o0o0OOO0o0 - o0O0
 return ooOOoooooo
 if 45 - 45: OOOo0 - OoooooooOO + iIii1I11I1II1 . OOOo0 * I11i1I
 if 51 - 51: Ooo00oOo00o / Ooo00oOo00o
O0i1II1Iiii1I11 = i1iIi ( )
o0OOoo0OO0OOO = None
o000O0o = None
ooOOO0 = None
o0o = None
O0OOoO00OO0o = None
I1111IIIIIi = None
Iiii1i1 = None
if 84 - 84: OOOo0 . iIii1I11I1II1 % OoooooooOO + o0o0OOO0o0 % OoooooooOO % Ooo00oOo00o
if 42 - 42: Ooo00oOo00o / I11i1I / OOooOOo + IIII / I1IiI
try :
 Iiii1i1 = int ( O0i1II1Iiii1I11 [ "fav_mode" ] )
except :
 pass
 if 84 - 84: OO0oo0oOO * OoOoOO00 + Oo
try :
 o0OOoo0OO0OOO = urllib . unquote_plus ( O0i1II1Iiii1I11 [ "url" ] )
except :
 pass
try :
 o000O0o = urllib . unquote_plus ( O0i1II1Iiii1I11 [ "name" ] )
except :
 pass
try :
 o0o = urllib . unquote_plus ( O0i1II1Iiii1I11 [ "iconimage" ] )
except :
 pass
try :
 ooOOO0 = int ( O0i1II1Iiii1I11 [ "mode" ] )
except :
 pass
try :
 O0OOoO00OO0o = urllib . unquote_plus ( O0i1II1Iiii1I11 [ "fanart" ] )
except :
 pass
try :
 I1111IIIIIi = urllib . unquote_plus ( O0i1II1Iiii1I11 [ "description" ] )
except :
 pass
 if 53 - 53: IIII % OoOoOO00 . o0O0 - iIii1I11I1II1 - o0O0 * OoOoOO00
 if 77 - 77: iIii1I11I1II1 * Ooo00oOo00o
print str ( oo0o0O00 ) + ': ' + str ( Oo0o0000o0o0 )
print "Mode: " + str ( ooOOO0 )
print "URL: " + str ( o0OOoo0OO0OOO )
print "Name: " + str ( o000O0o )
print "IconImage: " + str ( o0o )
if 95 - 95: OOOo0 + i11iIiiIii
if 6 - 6: OO0oo0oOO / i11iIiiIii + IIII * ooOoo0O
def o00o0 ( content , viewType ) :
 if 45 - 45: O0
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if O0oo0OO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % O0oo0OO0 . getSetting ( viewType ) )
  if 26 - 26: I11i1I - iIii1I11I1II1 - OOOo0 / Ooo00oOo00o . I1IiI % iIii1I11I1II1
  if 91 - 91: OOooOOo . iIii1I11I1II1 / ooOoo0O + i1IIi
if ooOOO0 == None : OooO0 ( )
elif ooOOO0 == 11 : O0OOO0OOoO0O ( )
elif ooOOO0 == 12 : II11iiii1Ii ( )
elif ooOOO0 == 13 : oo0OooOOo0 ( )
elif ooOOO0 == 14 : iIIIIii1 ( o000O0o )
elif ooOOO0 == 15 : OOoo0O ( o0OOoo0OO0OOO )
elif ooOOO0 == 16 : I1I ( )
elif ooOOO0 == 17 : iii11I111 ( o000O0o )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
