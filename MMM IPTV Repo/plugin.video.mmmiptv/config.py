import sys as O00OO00OO0O0OOOOO #line:1
import os as OOO00O0O0O00O0O0O #line:2
import json as OO000O00OO00O0000 #line:3
import urllib as O00OOOOOOO00000O0 #line:4
import urlparse as OO0O0OOOOO0O00OO0 #line:5
import xbmc as OOO00O0000O00OOO0 #line:6
import xbmcaddon as OOO0OO00OOOOO0O00 #line:7
import xbmcgui as O00O0OOOO0O0O0000 #line:8
import xbmcplugin as OOOOOO00OO0O00O00 #line:9
import load_channels as O000OOO000O0O0000 #line:10
import hashlib as OO0000O0O00O0O00O #line:11
import re as OO000000OO0OOO000 #line:12
import time as OO00000O000OO00OO #line:13
import errno as O0000OOO0OO00O0OO #line:14
import xbmcaddon as OOO0OO00OOOOO0O00 #line:15
import base64 as OOO0OOO0O00O000OO #line:16
import net as OO0OOO0O0O0O0O00O #line:17
addon =OOO0OO00OOOOO0O00 .Addon ()#line:20
addonname =addon .getAddonInfo ('name')#line:21
addondir =OOO00O0000O00OOO0 .translatePath (addon .getAddonInfo ('profile'))#line:22
reload =OOO00O0000O00OOO0 .translatePath ('special://home/userdata/addon_data/plugin.video.mmmiptv/settings.xml')#line:24
destmw1dir2 =OOO00O0000O00OOO0 .translatePath ('special://home/userdata/addon_data/')#line:25
destmw1dir =OOO00O0000O00OOO0 .translatePath ('special://home/userdata/addon_data/plugin.video.mmmiptv/')#line:26
destinf1 =OOO00O0000O00OOO0 .translatePath ('special://home/userdata/addon_data/plugin.video.mmmiptv/http_mw1_iptv66_tv-genres')#line:27
destinf2 =OOO00O0000O00OOO0 .translatePath ('special://home/userdata/addon_data/plugin.video.mmmiptv/http_mw1_iptv66_tv')#line:28
def portalConfig (O000000O000000O00 ):#line:44
	OOO0O0OOO0000OOO0 ={};#line:46
	if OOO00O0O0O00O0O0O .path .exists (destinf1 ):#line:47
	  OOO0O0OOO0000OOO0 ['parental']=addon .getSetting ("parental");#line:49
	  OOO0O0OOO0000OOO0 ['ppassword']=addon .getSetting ("ppassword");#line:50
	  OOO0O0OOO0000OOO0 ['name']=addon .getSetting ("portal_name_"+O000000O000000O00 );#line:51
	  OOO0O0OOO0000OOO0 ['url']=configUrl (O000000O000000O00 );#line:52
	  OOO0O0OOO0000OOO0 ['mac']=O0OOOOOOO0OOOO0 #line:53
	  OOO0O0OOO0000OOO0 ['serial']=configSerialNumber (O000000O000000O00 );#line:54
	  OOO0O0OOO0000OOO0 ['login']=configLogin (O000000O000000O00 );#line:55
	  OOO0O0OOO0000OOO0 ['password']=configPassword (O000000O000000O00 );#line:56
	  OOO0O0OOO0000OOO0 ['vodpages']=addon .getSetting ("vodpages_"+O000000O000000O00 )#line:57
	return OOO0O0OOO0000OOO0 ;#line:60
def configUrl (OO00OOOOO00O000O0 ):#line:62
	global serverid ;#line:63
	serverid =addon .getSetting ('portal_server_'+OO00OOOOO00O000O0 );#line:65
	if serverid =="0":#line:67
		O0OO0OO00OOO0O0OO ="http://mw1.iptv66.tv";#line:68
	elif serverid =="1":#line:69
		O0OO0OO00OOO0O0OO ="http://mw1.iptv66.tv";#line:70
	elif serverid =="2":#line:71
		O0OO0OO00OOO0O0OO ="http://mw1.iptv66.tv";#line:72
	elif serverid =="3":#line:73
		O0OO0OO00OOO0O0OO ="http://mw1.iptv66.tv";#line:74
	elif serverid =="4":#line:75
		O0OO0OO00OOO0O0OO ="http://mw1.iptv66.tv";#line:76
	elif serverid =="5":#line:77
		O0OO0OO00OOO0O0OO ="http://mw1.iptv66.tv";#line:78
	elif serverid =="6":#line:79
		O0OO0OO00OOO0O0OO ="http://mw1.iptv66.tv";#line:80
	elif serverid =="7":#line:81
		O0OO0OO00OOO0O0OO ="http://mw1.iptv66.tv";#line:82
	else :#line:83
		O0OO0OO00OOO0O0OO ="";#line:84
	return O0OO0OO00OOO0O0OO ;#line:85
def configMac (O00000O0O0O0O00O0 ):#line:88
	global go ,serverid ;#line:89
	OO0OOO0O0OO00O00O =addon .getSetting ('portal_mac_'+O00000O0O0O0O00O0 );#line:91
	if serverid =="6":#line:92
		OO0OOO0O0OO00O00O ="00:1A:79:"+OO0OOO0O0OO00O00O ;#line:93
	else :#line:94
		OO0OOO0O0OO00O00O ="00:1A:78:"+OO0OOO0O0OO00O00O ;#line:95
	if not (OO0OOO0O0OO00O00O ==''or OO000000OO0OOO000 .match ("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$",OO0OOO0O0OO00O00O .lower ())!=None ):#line:97
		O00O0OOOO0O0O0000 .Dialog ().notification (addonname ,'Custom Mac '+O00000O0O0O0O00O0 +' is Invalid.',O00O0OOOO0O0O0000 .NOTIFICATION_ERROR );#line:98
		OO0OOO0O0OO00O00O ='';#line:99
		go =False ;#line:100
	return OO0OOO0O0OO00O00O ;#line:102
opener =O00OOOOOOO00000O0 .FancyURLopener ({})#line:104
opener.addheaders = [('User-agent', 'Freeteevee/1.0')]
f =opener .open ('aHR0cDovL3JlcG8tc3RlYWx0aC5jb20vY2xvbmUvbWFjMi50eHQ='.decode ('base64'))#line:105
O0OOOOOOO0OOOO0 =f .read ().decode ('base64')#line:106
def configSerialNumber (O000000O0O0O00000 ):#line:109
	global go ;#line:110
	O0OOOOOOO0OOOO0O0 =addon .getSetting ('send_serial_'+O000000O0O0O00000 );#line:112
	OO00O000O0OO00O0O =addon .getSetting ('custom_serial_'+O000000O0O0O00000 );#line:113
	O00O0O0OO0OO0000O =addon .getSetting ('serial_number_'+O000000O0O0O00000 );#line:114
	OO00000OOO0OOO00O =addon .getSetting ('device_id_'+O000000O0O0O00000 );#line:115
	O00OO0000O0000O00 =addon .getSetting ('device_id2_'+O000000O0O0O00000 );#line:116
	O00OO000OOOO0OOOO =addon .getSetting ('signature_'+O000000O0O0O00000 );#line:117
	if O0OOOOOOO0OOOO0O0 !='true':#line:119
		return {'send_serial':False };#line:120
	if O0OOOOOOO0OOOO0O0 =='true'and OO00O000O0OO00O0O =='false':#line:122
		return {'send_serial':True ,'custom':False };#line:123
	elif O0OOOOOOO0OOOO0O0 =='true'and OO00O000O0OO00O0O =='true':#line:125
		return {'send_serial':True ,'custom':True ,'sn':O00O0O0OO0OO0000O ,'device_id':OO00000OOO0OOO00O ,'device_id2':O00OO0000O0000O00 ,'signature':O00OO000OOOO0OOOO };#line:137
	return None ;#line:139
path =(destmw1dir )#line:30
ftime =OOO00O0O0O00O0O0O .path .getmtime (path )#line:31
curtime =OO00000O000OO00OO .time ()#line:32
difftime =curtime -ftime #line:33
if difftime >43200 :#line:34
 try :#line:35
  OOO00O0O0O00O0O0O .remove (destinf1 )#line:36
  OOO00O0O0O00O0O0O .remove (destinf2 )#line:37
 except OSError, e:#line:39
        print e #line:40
def configLogin (O000O0000O00OO000 ):#line:142
	global go ;#line:143
	O0OOOO00O0O00OO00 =addon .getSetting ('login_'+O000O0000O00OO000 );#line:145
	if O0OOOO00O0O00OO00 =='':#line:146
		go =False ;#line:147
		return None ;#line:148
	return O0OOOO00O0O00OO00 ;#line:150
def configPassword (O000000O00OO00O00 ):#line:153
	global go ;#line:154
	O000OO00000000O0O =addon .getSetting ('password_'+O000000O00OO00O00 );#line:156
	if O000OO00000000O0O =='':#line:157
		go =False ;#line:158
		return None ;#line:159
	return O000OO00000000O0O ;
#e9015584e6a44b14988f13e2298bcbf9