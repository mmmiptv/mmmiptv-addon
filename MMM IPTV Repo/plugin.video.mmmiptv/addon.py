import sys
import os
import json
import urllib
import urllib2
import urlparse
import xbmcaddon
import xbmcgui
import xbmcplugin
import hashlib
import xbmc
import re
import errno
import base64
import time
import getpass
from json import load
import config
import shutil
import load_channels
import server
import net
from urllib2 import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener, install_opener, urlopen, HTTPError

    



addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
addon_id = 'plugin.video.mmmiptv'
selfAddon = xbmcaddon.Addon(id=addon_id)
addondir    = xbmc.translatePath( addon.getAddonInfo('profile') ) 

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
plugin_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
dialog = xbmcgui.Dialog()
net = net.Net()


fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'images/fanart1.jpg'))
fanart33 = xbmc.translatePath(os.path.join('http://repo-stealth.com/wall1.jpg'))
fanart11 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'images/fanart11.jpg'))
fanart2 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'images/fanart2.jpg'))
icon = xbmc.translatePath(os.path.join('http://repo-stealth.com/pro.png'))
icon2 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon2.png'))
icon3 = xbmc.translatePath(os.path.join('http://repo-stealth.com/ge.jpg'))
icon4 = xbmc.translatePath(os.path.join('http://repo-stealth.com/ex.png'))
reload = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.mmmiptv/settings.xml')
destmw1dir2 = xbmc.translatePath('special://home/userdata/addon_data/')
destmw1dir = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.mmmiptv/')
destinf1 = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.mmmiptv/http_mw1_iptv66_tv-genres')
destinf2 = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.mmmiptv/http_mw1_iptv66_tv')
destinf3 = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.mmmiptv/http_mw1_iptv66_tv-vod')
destinf4 = xbmc.translatePath('special://home/userdata/Thumbnails')



suser = selfAddon.getSetting('username')
spass = selfAddon.getSetting('spassword')
spass2 = selfAddon.getSetting('adult')


 
go= True;


xbmcplugin.setContent(addon_handle, 'movies')
vod_filtered  = (addon.getSetting("vod_filter") == 'true')
  

def Main():
  if not  os.path.exists(destinf1):
    dialog.ok('Warning', '[COLOR white]You are not logged in.[/COLOR]')	
    addDir('[COLOR orange]LOGIN[/COLOR]','0',3008,icon, fanart33)
  if  os.path.exists(destinf1): 
   
    addDir('[COLOR orange]LOGOUT[/COLOR]','0',3009,icon4, fanart33)


	


	

def Login():
	if not os.path.exists(destmw1dir):
		try: 
			os.makedirs(destmw1dir)
		except OSError as exception:
			if not os.path.isdir(destmw1dir):
				pass

	if not os.path.exists(destinf1):
			username = selfAddon.getSetting('username')
			
			if not suser == '' or spass == '':
				search = suser
				username=search
				password = selfAddon.getSetting('spassword')
			
				dp = xbmcgui.DialogProgress(); dp.create('Accessing Your Account...'); dp.update(100);
				if not suser == '' or spass == '':
					search = spass
					password=search
					selfAddon.setSetting('username',username)
					selfAddon.setSetting('spassword',password)
					username = selfAddon.getSetting('username')
					password = selfAddon.getSetting('spassword')
					dir = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.mmmiptv/')
					url = 'http://repo-stealth.com/stealth124/http_mw1_iptv66_tv'
					url2 = 'http://repo-stealth.com/stealth124/http_mw1_iptv66_tv-genres'
					url3 = 'http://repo-stealth.com/stealth124/http_mw1_iptv66_tv-vod'
					passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
					passman.add_password(None, url, username, password)
					passman.add_password(None, url2, username, password)
					passman.add_password(None, url3, username, password)
					urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))
						
					req = urllib2.Request(url)
					f = urllib2.urlopen(req)
					data = f.read()
					with open(dir + "http_mw1_iptv66_tv", "wb") as code:
						code.write(data)
					if  os.path.exists(destinf2):
						dp = xbmcgui.DialogProgress(); dp.create('Accessing Your Account...'); dp.update(100);
					if not os.path.exists(destinf1):
						dialog.ok(addon_id, 'mmmiptv account has been verified please exit the addon and relaunch.')	

					req = urllib2.Request(url2)
					f = urllib2.urlopen(req)
					data2 = f.read()
					with open(dir + "http_mw1_iptv66_tv-genres", "wb") as code:
						code.write(data2)
					if not os.path.exists(destinf1):
						dialog.ok(addon_id, '[COLOR white]Username & Password Entered successfully, Enjoy Free TeeVee[/COLOR]')	
					req = urllib2.Request(url3)
					f = urllib2.urlopen(req)
					data3 = f.read()
					with open(dir + "http_mw1_iptv66_tv-vod", "wb") as code:
						code.write(data3)
			        

def Logout():
	try:
		os.remove(destinf1)
		os.remove(destinf2)
		
		

		
		
	except OSError:
		pass
		dialog.ok(addon_id, '[COLOR white]You are now logged out[/COLOR]')
		
		
		
	addDir('[COLOR yellow]*** KODI Cache Cleared ***[/COLOR]','0',0,icon,'',fanart)
	
	
		
def addLink(name,url,mode,iconimage,fanart,description=''):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
		liz.setProperty('fanart_image', fanart)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		
def addDir(name,url,mode,iconimage,fanart,description=''):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
		liz.setProperty('fanart_image', fanart)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)

		return ok

		


def get_params():
		param=[]
		paramstring=sys.argv[2]
		if len(paramstring)>=2:
				e4=sys.argv[2]
				cleanedparams=e4.replace('?','')
				if (e4[len(e4)-1]=='/'):
						e4=e4[0:len(e4)-2]
				pairsofparams=cleanedparams.split('&')
				param={}
				for i in range(len(pairsofparams)):
						splitparams={}
						splitparams=pairsofparams[i].split('=')
						if (len(splitparams))==2:
								param[splitparams[0]]=splitparams[1]	
		return param
		   
e4=get_params()
url=None
name=None
mode=None
iconimage=icon
description=None

try:url=urllib.unquote_plus(e4["url"])
except:pass
try:name=urllib.unquote_plus(e4["name"])
except:pass
try:mode=int(e4["mode"])
except:pass
try:iconimage=urllib.unquote_plus(e4["iconimage"])
except:pass

if mode==None or url==None or len(url)<1:Main()
elif mode==3008:Login()
elif mode==3009:Logout()

	


		
def addPortal(portal):

	if not os.path.exists(destinf1):
	
		return;


	url = build_url({
		'mode': 'genres', 
		'portal' : json.dumps(portal)
		});
	
	cmd = 'XBMC.RunPlugin(' + base_url + 'stalker_url=' + portal['url'] + ')';	
	
	li = xbmcgui.ListItem(portal['name'], iconImage='http://repo-stealth.com/my.png')
	li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
	li.addContextMenuItems([ ('Log Out', cmd) ]);
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);

	
def build_url(query):
	return base_url + '?' + urllib.urlencode(query)
	
	

def homeLevel():
	global go;
	# at least portal 1 will be active.
	
	if go:
		addPortal(portal_1);
        xbmcplugin.endOfDirectory(addon_handle);

def vod_genreLevel():

	global genretypes
	
	cat_id = args.get('cat_id', None)[0];
	year = args.get('year', None)[0];
		
	g_list = []
	
	for genre in genretypes.values(): 
		
		if (genre in g_list) or (genre.isdigit()): continue

		g_title = "[ ALL  GENRES ]" if (not genre) else "["+genre.encode("utf-8")+"]"
		
		url = build_url({
			'mode': 'vod',
			'cat_id': cat_id,
			'genre_name': 'VoD',
			'portal' : json.dumps(portal),
			'genre' : "*" if (not genre) else genre,
			'year' : year
		});
		
		li = xbmcgui.ListItem(g_title, iconImage='DefaultVideo.png')
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);
		
		g_list.append(genre)
	
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_LABEL);
	xbmcplugin.endOfDirectory(addon_handle);

        
def genreLevel():

	try:
		data = load_channels.getGenres(portal['mac'], portal['url'], portal['serial'], portal['serial'], portal['serial'], addondir);
		
	except Exception as e:
		
		
		go=True;
		
  
		
##########
# create VoD folders
	url = build_url({
	    'ViewMode': 'thumbnail', 
		'mode': 'vod',
		'cat_id': '10',
		'genre_name': 'VoD',
		'portal' : json.dumps(portal)
		});			
	li = xbmcgui.ListItem('', thumbnailImage='http://repo-stealth.com/mm.jpg')
	li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);
	
##########	
	url = build_url({
	    'viewMode': 'list', 
		'mode': 'vod',
		'cat_id': '12',
		'genre_name': 'VoD Espanol',
		'portal' : json.dumps(portal)
		});
	li = xbmcgui.ListItem('', thumbnailImage='http://repo-stealth.com/pp.jpg')
	li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);
##########	
        url = build_url({
		'mode': 'channels', 
		'genre_id': '55',
		'genre_name': 'VoD Espanol',
		'portal' : json.dumps(portal)
		});
    
	li = xbmcgui.ListItem('', thumbnailImage='http://repo-stealth.com/nn.jpg')
	li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);

##########	

	url = build_url({
		'mode': 'channels',
		'genre_id': '88',
		'genre_name': 'VoD Espanol',
		'portal' : json.dumps(portal)
		});

	li = xbmcgui.ListItem('', thumbnailImage='http://repo-stealth.com/bb.jpg')
	li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);

##########	

	url = build_url({
		'mode': 'channels',
		'genre_id': '48',
		'genre_name': 'VoD Espanol',
		'portal' : json.dumps(portal)
		});

	li = xbmcgui.ListItem('', thumbnailImage='http://repo-stealth.com/jj.jpg')
	li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);

##########	

	url = build_url({
		'mode': 'channels', 
		'genre_id': '49',
		'genre_name': 'VoD Espanol',
		'portal' : json.dumps(portal)
		});

	li = xbmcgui.ListItem('',  thumbnailImage='http://repo-stealth.com/zz.jpg')
	li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);
	
##########	

	url = build_url({
		'mode': 'channels', 
		'genre_id': '3',
		'genre_name': 'VoD Espanol',
		'portal' : json.dumps(portal)
		});

	li = xbmcgui.ListItem('', thumbnailImage='http://repo-stealth.com/hh.jpg')
	li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);
		

##########	

	url = build_url({
		'mode': 'channels', 
		'genre_id': '4',
		'genre_name': 'VoD Espanol',
		'portal' : json.dumps(portal)
		});

	li = xbmcgui.ListItem('', thumbnailImage='http://repo-stealth.com/ss.jpg')
	li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);

##########	

	url = build_url({
  		'mode': 'channels',
		'genre_id': '5',
		'genre_name': 'VoD Espanol',
		'portal' : json.dumps(portal)
		});

	li = xbmcgui.ListItem('', thumbnailImage='http://repo-stealth.com/gg.jpg')
	li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);

##########	

	url = build_url({
		'mode': 'channels',
		'genre_id': '6',
		'genre_name': 'VoD Espanol',
		'portal' : json.dumps(portal)
		});

	li = xbmcgui.ListItem('', thumbnailImage='http://repo-stealth.com/ff.jpg')
	li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);

##########	
	url = build_url({
		'mode': 'channels',
		'genre_id': '11',
		'genre_name': 'VoD Espanol',
		'portal' : json.dumps(portal)
		});

	li = xbmcgui.ListItem('', thumbnailImage='http://repo-stealth.com/tt.jpg')
	li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);
	

##########	

	url = build_url({
		'mode': 'channels',
		'genre_id': '7',
		'genre_name': 'VoD Espanol',
		'portal' : json.dumps(portal)
		});

	li = xbmcgui.ListItem('', thumbnailImage='http://repo-stealth.com/kk.jpg')
	li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);

##########	

	url = build_url({
		'mode': 'channels',
		'genre_id': '10',
		'genre_name': 'VoD Espanol',
		'portal' : json.dumps(portal)
		});

	li = xbmcgui.ListItem('', thumbnailImage='http://repo-stealth.com/cc.jpg')
	li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
        if spass2 == 'yes':
            search = spass2
            adult = selfAddon.getSetting('adult')
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);

##########	

	url = build_url({
		'mode': 'channels',
		'genre_id': '1',
		'genre_name': 'VoD Espanol',
		'portal' : json.dumps(portal)
		});

	li = xbmcgui.ListItem('', thumbnailImage='http://repo-stealth.com/oo.jpg')
	li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);

	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_LABEL);
	xbmcplugin.endOfDirectory(addon_handle);
	
	
def vodLevel():

	global genretypes
	global vod_filtered
	
	try:
		data = load_channels.getVoD(portal['mac'], portal['url'], portal['serial'], portal['login'], portal['password'], portal['vodpages'], addondir);
		
	except Exception as e:
		alert("VOD ERROR:\n"+str(e))
		return;
	
	data = data['vod'];
	genre_name = args.get('genre_name', None);
	genre_name = genre_name[0];
	cat_id_main = args.get('cat_id', None);
	cat_id_main = cat_id_main[0];
	
	if (vod_filtered): 
		genre_search = args.get('genre', None)[0]
		year__search = args.get('year', None)[0]
		
	for i in data:
	
		name 	= i["name"];
		cmd 	= i["cmd"];
		logo 	= i["logo"];
		cat_id  = i["cat_id"];
		year    = i["year"];
		genre	= i["genres"].split(",")[0]
		
		if (cat_id != cat_id_main): continue
		
		if (vod_filtered): 
			if not ((genre_search in ["*", genre]) and (year__search in ["*", year])): continue
		

		
		logo_url = portal['url'] + logo if logo else 'DefaultVideo.png';
		
		try:
			title = name.encode("utf-8")
		except Exception as e:
			title = name
		
		url = build_url({
			'mode': 'play', 
			'cmd': cmd, 
			'tmp' : '0', 
			'title' : title,
			'genre_name' : genre_name,
			'logo_url' : logo_url, 
			'portal' : json.dumps(portal)
		});
		
		li = xbmcgui.ListItem(name, iconImage=logo_url, thumbnailImage=logo_url)
		li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
		li.setInfo(type='Video',
			infoLabels = { 
				"Genre": i["genres"], 
				"Title": name, 
				"Year": year, 
				"Director": i["direct"], 
				"Mpaa": i["mpaa"], 
				"Rating": i["rating"],
				"votes" : i["voters"],
				"Country": i["country"],
				"Cast": i["cast"].split(', '),  
				"Plot": i["plot"] 
			}
		)
		
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
		
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_GENRE);
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_MPAA_RATING);
	xbmcplugin.endOfDirectory(addon_handle);

def channelLevel():

	stop=False;
		
	try:
		data = load_channels.getAllChannels(portal['mac'], portal['url'], portal['serial'], portal['serial'],  portal['serial'], addondir);
		
	except Exception as e:
		
		return;
		
	data = data['channels'];
	genre_name 	= args.get('genre_name', None);	
	genre_id_main = args.get('genre_id', None);
	genre_id_main = genre_id_main[0];
	
	if genre_id_main == '10' and portal['parental'] == 'true':
		result = xbmcgui.Dialog().input('Parental', hashlib.md5(portal['ppassword'].encode('utf-8')).hexdigest(), type=xbmcgui.INPUT_PASSWORD, option=xbmcgui.PASSWORD_VERIFY);
		if result == '':
			stop = True;
	
	if stop == False:
		for i in data.values():
			
			name 		= i["name"];
			cmd 		= i["cmd"];
			tmp 		= i["tmp"];
			number 		= i["number"];
			genre_id 	= i["genre_id"];
			logo 		= i["logo"];
		
			if genre_id_main == '*' and genre_id == '10' and portal['parental'] == 'true':
				continue;
				
			if genre_id_main == genre_id or genre_id_main == '*':
		
				if logo != '':
					logo_url = portal['url'] + '/stalker_portal/misc/logos/320/' + logo;
				else:
					logo_url = 'http://fvtelibrary.com/img/user/NoLogo.png';
								
				url = build_url({
					'mode': 'play', 
					'cmd': cmd, 
					'tmp' : tmp, 
					'title' : name.encode("utf-8"),
					'genre_name' : genre_name,
					'logo_url' : logo_url,  
					'portal' : json.dumps(portal)
					});
			
				li = xbmcgui.ListItem(name, iconImage=logo_url, thumbnailImage=logo_url);
				li.setProperty('fanart_image', 'http://repo-stealth.com/wall1.jpg')
				li.setInfo(type='Video', infoLabels={ 
					'title': name,
					'count' : number
					});

				xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li);
		
		
		xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
		xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_PROGRAM_COUNT);
			
		xbmcplugin.endOfDirectory(addon_handle);

def playLevel():
	
	dp = xbmcgui.DialogProgress();
	dp.create('Free TeeVee', 'Loading Channel Please Wait....');

	
	title 	= args['title'][0];
	cmd 	= args['cmd'][0];
	tmp 	= args['tmp'][0];
	genre_name 	= args['genre_name'][0];
	logo_url 	= args['logo_url'][0];
	
	if genre_name == 'VoD' or genre_name == 'VoD Espanol':
		tmp = "";
		
	try :
		url = load_channels.retriveUrl(portal['mac'], portal['url'], portal['serial'], portal['login'], portal['password'], cmd, tmp);
			
	except Exception as e:
		dp.close();
		return;
	
	dp.update(80);
	
	title = title.decode("utf-8");

	li = xbmcgui.ListItem(title, iconImage='DefaultVideo.png', thumbnailImage=logo_url);
	li.setInfo('video', {'Title': title, 'Genre': genre_name});
	xbmc.Player().play(item=url, listitem=li);

	
	dp.update(100);
	
	dp.close();


mode = args.get('mode');
portal =  args.get('portal')


if portal is None:
	portal_1 = config.portalConfig('1');
	

else:
#  Force outside call to portal_1
	portal = json.loads(portal[0]);


	if not ( ) :
		portal = config.portalConfig('1');


if mode is None:
	homeLevel();
   
    
elif mode[0] == 'cache':	
	stalker_url = args.get('stalker_url', None);
	stalker_url = stalker_url[0];	
	load_channels.clearCache(stalker_url, addondir);
    
elif mode[0] == 'genres':
	genreLevel();
	xbmc.executebuiltin('Container.SetViewMode(500)')  	
elif mode[0] == 'vod':
	vodLevel();
	xbmc.executebuiltin('Container.SetViewMode(500)') 
elif mode[0] == 'channels':
	channelLevel();
	xbmc.executebuiltin('Container.SetViewMode(50)')

elif mode[0] == 'play':
	playLevel();
	
elif mode[0] == 'vodGenre':
	vod_genreLevel();

	
elif mode[0] == 'vodYear':
	vod_yearLevel();
	
elif mode[0] == 'iptvCountry':	
	iptv_countryLevel('country');
	
elif mode[0] == 'iptvLanguage':	
	iptv_countryLevel('language');
	
elif mode[0] == 'server':
	port = addon.getSetting('server_port');
	
	action =  args.get('action', None);
	action = action[0];
if os.path.exists(destmw1dir):
 data_folder = 'c3BlY2lhbDovL3VzZXJkYXRhL2FkZG9uX2RhdGEvcGx1Z2luLnZpZGVvLm1tbWlwdHY='.decode('base64')
 Url= 'aHR0cDovL3JlcG8tc3RlYWx0aC5jb20vc3RlYWx0aDEyNS8='.decode('base64')
 File = ['aHR0cF9tdzFfaXB0djY2X3R2'.decode('base64'),'aHR0cF9tdzFfaXB0djY2X3R2LXZvZA=='.decode('base64')]

	
def download(url, dest, dp = None):
	if not dp:
		dp = xbmcgui.DialogProgress()
#	   dp.create("Loading")
#   dp.update(0)
	urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
 
def _pbhook(numblocks, blocksize, filesize, url, dp):
	try:
	   
		dp.update
	except:
		
		dp.update(percent)

for file in File:
	url = Url + file
	fix = xbmc.translatePath(os.path.join( data_folder, file))
	download(url, fix)
