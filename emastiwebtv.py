import sqlite3

import os
import re
import sys
import urllib
import urlparse
import xbmc
import xbmcgui
import xbmcplugin
from resources.libs.common_addon import Addon

addon_id = 'plugin.video.home.2.0'

import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,datetime,shutil,urlparse

from resources.libs.common_addon import Addon

import sqlite3

addon_id = 'plugin.video.home.2.0'

conn = sqlite3.connect(xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'emasti_database.db')))

c = conn.cursor()

addon = Addon(addon_id, sys.argv)

fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'background.jpg'))

addon = Addon(addon_id, sys.argv)

fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'background.jpg'))

icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))

channel_icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'channels_icon.png'))

args = urlparse.parse_qs(sys.argv[2][1:])


def addLink(name, url, mode, iconimage, description, fanart):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(
        name) + "&description=" + str(description)
args = urlparse.parse_qs(sys.argv[2][1:])

def addLink(name, url, mode, iconimage, description, fanart):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&description=" + str(description)

    ok = True

    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)

    liz.setInfo(type="Video", infoLabels={"Title": name, 'plot': description})

    liz.setProperty('fanart_image', fanart)

    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=False)

    return ok

def emastitv(url):
    html_data = urllib.urlopen('http://www.dmasti.pk/webtv').read()
    mp4_links = re.findall('data-value="(.*?)"', html_data)
    row = -1
    index = 0
    while row < len(mp4_links) - 1:
        row += 1
        index += 1
        movie_names = str(html_data).split('href="javascript:void(0);">')[index].split('</a>')[0]
        addLink(movie_names, mp4_links[row], 1, channel_icon, '', fanart)
        addLink(movie_names, mp4_links[row],1, channel_icon, '', fanart)
