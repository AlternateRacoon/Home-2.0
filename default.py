import emastiwebtv
import os
import re
import sys
import urllib
import urlparse
import urlrequest
import xbmc
import xbmcgui
import xbmcplugin
from resources.libs.common_addon import Addon

addon_id = 'plugin.video.home.2.0'

addon = Addon(addon_id, sys.argv)

fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'background_1.png'))

icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))

args = urlparse.parse_qs(sys.argv[2][1:])


def getusersearch():
    kb = xbmc.Keyboard('default', 'heading')
    kb.setDefault('')
    kb.setHeading('Enter The Name For A Movie')
    kb.setHiddenInput(False)
    kb.doModal()
    if (kb.isConfirmed()):
        search_term = kb.getText()
        return (search_term)
    else:
        return
        mode = args.get('mode', None)


def getusersearch_channel():
    kb = xbmc.Keyboard('default', 'heading')
    kb.setDefault('')
    kb.setHeading('Enter The Name For A channel')
    kb.setHiddenInput(False)
    kb.doModal()
    if (kb.isConfirmed()):
        search_term = kb.getText()
        return (search_term)
    else:
        return
        mode = args.get('mode', None)


def INDEX():
    addDir('All Channels', 'url', 3, '', '', fanart)

    addDir('Movies Search', 'url', 2, '', '', fanart)

    addDir('Latest Movies', 'url', 6, '', '', fanart)

    addDir('Channels Search', 'url', 4, '', '', fanart)


def emasti_movie_search(url):
    get_user_input = getusersearch()
    xbmcplugin.setContent(int(sys.argv[1]), 'movies')
    urlrequest.emastisearch(get_user_input)


def channel_search(url):
    get_user_input = getusersearch_channel()
    xbmcplugin.setContent(int(sys.argv[1]), 'movies')
    html_page = urllib.urlopen("http://www.emasti.pk/webtv").read()
    paragraphs1 = re.findall(r'data-value="(.*?)"', str(html_page))
    x = -1
    y = 0
    while x < 125:
        x += 1
        y += 1
        titletv = str(html_page).split('href="javascript:void(0);">')[y].split('</a>')[0]
        if get_user_input.lower() in titletv.lower():
            addLink(titletv, paragraphs1[x], 1,
                    xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'channels_icon.png')), '',
                    fanart)
        else:
            pass

def load_another_page(url):
    html_data = urllib.urlopen(url).read().decode("utf-8")
    movies_links = re.findall('<a class="poster" href="(.*?)">', html_data)
    movie_posters = re.findall('<img src="(.*?)" alt="', html_data)
    movie_names = re.findall('<h1>(.*?)</h1><span>', html_data)
    url1 = url

    for row in range(len(movie_posters)):
        addDir(movie_names[row], movies_links[row], 8, movie_posters[row], '', fanart)
    url1 += "code1245"
    index_number = re.findall('/index/(.*?)code1245', url1)
    index_number = int(index_number[0])
    index_number += index_number
    addDir('Next Page', 'http://www.dmasti.pk/movies/index/' + str(index_number), 7, icon, '', fanart)

def load_mp4_link(url):
    html_data_movies = urllib.urlopen(url).read().decode("utf8")
    mp4_link = re.findall('<a href="(.*?)" class="vh_button red icon-down', html_data_movies)[0]
    addLink('Movie', mp4_link, 1, '', '', fanart)
def PLAYLINK(name, url):
    ok = True
    liz = xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=icon);
    liz.setInfo(type="Video", infoLabels={"Title": name})
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=liz)
    xbmc.Player().play(url, liz, False)

def get_params():
    param = []

    paramstring = sys.argv[2]

    if len(paramstring) >= 2:

        params = sys.argv[2]

        cleanedparams = params.replace('?', '')

        if (params[len(params) - 1] == '/'):
            params = params[0:len(params) - 2]

        pairsofparams = cleanedparams.split('&')

        param = {}

        for i in range(len(pairsofparams)):

            splitparams = {}

            splitparams = pairsofparams[i].split('=')

            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]

    return param


def addDir(name, url, mode, iconimage, description, fanart):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(
        name) + "&description=" + str(description)

    ok = True

    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)

    liz.setInfo(type="Video", infoLabels={"Title": name, 'plot': description})

    liz.setProperty('fanart_image', fanart)

    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)

    return ok


def addLink(name, url, mode, iconimage, description, fanart):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&description=" + str(description)

    ok = True

    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)

    liz.setInfo(type="Video", infoLabels={"Title": name, 'plot': description})

    liz.setProperty('fanart_image', fanart)

    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=False)

    return ok


params = get_params();
url = None;
name = None;
mode = None;
site = None

try:
    site = urllib.unquote_plus(params["site"])

except:
    pass

try:
    url = urllib.unquote_plus(params["url"])

except:
    pass

try:
    name = urllib.unquote_plus(params["name"])

except:
    pass

try:
    mode = int(params["mode"])

except:
    pass


def url_data(args):
    pass


if mode == None or url == None or len(url) < 1:
    INDEX()


elif mode == 1:
    PLAYLINK(name, url)

elif mode == 2:
    emasti_movie_search(url)

elif mode == 3:
    emastiwebtv.emastitv(url)

elif mode == 4:
    channel_search(url)


elif mode == 6:
    urlrequest.get_latest_movie(url)

elif mode == 7:
    load_another_page(url)

elif mode == 8:
    load_mp4_link(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
