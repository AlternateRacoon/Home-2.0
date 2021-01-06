import os
import re
import sys
import urllib
import urllib2
import urlparse
import xbmc
import xbmcgui
import xbmcplugin
from resources.libs.common_addon import Addon

addon_id = 'plugin.video.home.2.0'

opener = urllib2.build_opener()

opener.addheaders = [('User-agent', 'Mozilla/5.0')]

addon = Addon(addon_id, sys.argv)

fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'background_2.jpg'))

icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))

args = urlparse.parse_qs(sys.argv[2][1:])


def addLink(name, url, mode, iconimage, description, fanart):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(
        name) + "&description=" + str(description)

    ok = True

    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)

    liz.setInfo(type="Video", infoLabels={"Title": name, 'plot': description})

    liz.setProperty('fanart_image', fanart)

    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=False)

    return ok


def addDir(name, url, mode, iconimage, description, fanart):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(
        name) + "&description=" + str(description)

    ok = True

    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)

    liz.setInfo(type="Video", infoLabels={"Title": name, 'plot': description})

    liz.setProperty('fanart_image', fanart)

    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)

    return ok


def get_latest_movie(url):
    html_data = urllib.urlopen("http://www.dmasti.pk/movies/index/0").read().decode("utf-8")
    movies_links = re.findall('<a class="poster" href="(.*?)">', html_data)
    movie_posters = re.findall('<img src="(.*?)" alt="', html_data)
    movie_names = re.findall('<h1>(.*?)</h1><span>', html_data)
    for row in range(len(movie_posters)):
        addDir(movie_names[row].encode('utf8'), movies_links[row].encode('utf8'), 8, movie_posters[row].encode('utf8'), '', fanart)
    addDir('Next Page', 'http://www.dmasti.pk/movies/index/48', 7, icon, '', fanart)


def get_latest_tv(url):
    html_data = urllib.urlopen("http://www.dmasti.pk/tvshows/index/0").read().decode("utf-8")
    movies_links = re.findall('<a class="poster" href="(.*?)">', html_data)
    movie_posters = re.findall('<img src="(.*?)" alt="', html_data)
    movie_names = re.findall('<h1>(.*?)</h1><span>', html_data)
    for row in range(len(movie_posters)):
        addDir(movie_names[row].encode('utf8'), movies_links[row].encode('utf8'), 8, movie_posters[row].encode('utf8'), '', fanart)
    addDir('Next Page', 'http://www.dmasti.pk/tvshows/index/24', 7, icon, '', fanart)


def get_latest_kids(url):
    html_data = urllib.urlopen("http://www.dmasti.pk/kids/index/0").read().decode("utf8")
    movies_links = re.findall('<a class="poster" href="(.*?)">', html_data)
    movie_posters = re.findall('<img src="(.*?)" alt="', html_data)
    movie_names = re.findall('<h1>(.*?)</h1><span>', html_data)
    for row in range(len(movie_posters)):
        addDir(movie_names[row].encode('utf8'), movies_links[row].encode('utf8'), 8, movie_posters[row].encode('utf8'),
               '', fanart)
    addDir('Next Page', 'http://www.dmasti.pk/kids/index/24', 7, icon, '', fanart)


def emastisearch(movie_data):
    search_string = movie_data
    movie_data_split = search_string.split()
    movie_data_split_length = len(movie_data_split)
    if movie_data_split_length == 1:
        html_page = "http://www.emasti.pk/search?keyword=" + movie_data_split[0]
    elif movie_data_split_length == 2:
        html_page = "http://www.emasti.pk/search?keyword=" + movie_data_split[0] + "+" + movie_data_split[1]
    elif movie_data_split_length == 3:
        html_page = "http://www.emasti.pk/search?keyword=" + movie_data_split[0] + "+" + movie_data_split[1] + "+" + \
                    movie_data_split[2]
    elif movie_data_split_length == 4:
        html_page = "http://www.emasti.pk/search?keyword=" + movie_data_split[0] + "+" + movie_data_split[1] + "+" + \
                    movie_data_split[2] + "+" + movie_data_split[3]
    elif movie_data_split_length == 5:
        html_page = "http://www.emasti.pk/search?keyword=" + movie_data_split[0] + "+" + movie_data_split[1] + "+" + \
                    movie_data_split[2] + "+" + movie_data_split[3] + "+" + movie_data_split[4]
    html_data = urllib.urlopen(html_page).read().decode("utf-8")
    if '<h1>Error 404</h1>' in html_data:
        search_string_split = search_string.split()
        search_string_split_len = len(search_string_split)
        if search_string_split_len == 1:
            html_data = opener.open("https://www.google.com/search?q=" + search_string_split[0]).read()
        if search_string_split_len == 2:
            html_data = opener.open(
                "https://www.google.com/search?q=" + search_string_split[0] + "+" + search_string_split[1]).read()
        if search_string_split_len == 3:
            html_data = opener.open(
                "https://www.google.com/search?q=" + search_string_split[0] + "+" + search_string_split[1] + "+" +
                search_string_split[2]).read()
        if search_string_split_len == 4:
            html_data = opener.open(
                "https://www.google.com/search?q=" + search_string_split[0] + "+" + search_string_split[1] + "+" +
                search_string_split[2] + "+" + search_string_split[3]).read()
        if search_string_split_len == 5:
            html_data = opener.open(
                "https://www.google.com/search?q=" + search_string_split[0] + "+" + search_string_split[1] + "+" +
                search_string_split[2] + "+" + search_string_split[3] + "+" + search_string_split[4]).read()
        movie_name = re.findall('<span>(.*?)</span>', html_data)
        movie_name = re.findall('AP7Wnd">(.*?)</div>', movie_name[0])
        if movie_name:
            search_string = movie_name[0]
            movie_data_split = search_string.split()
            movie_data_split_length = len(movie_data_split)
            if movie_data_split_length == 1:
                html_page = "http://www.emasti.pk/search?keyword=" + movie_data_split[0]
            elif movie_data_split_length == 2:
                html_page = "http://www.emasti.pk/search?keyword=" + movie_data_split[0] + "+" + movie_data_split[1]
            elif movie_data_split_length == 3:
                html_page = "http://www.emasti.pk/search?keyword=" + movie_data_split[0] + "+" + movie_data_split[
                    1] + "+" + movie_data_split[2]
            elif movie_data_split_length == 4:
                html_page = "http://www.emasti.pk/search?keyword=" + movie_data_split[0] + "+" + movie_data_split[
                    1] + "+" + movie_data_split[2] + "+" + movie_data_split[3]
            elif movie_data_split_length == 5:
                html_page = "http://www.emasti.pk/search?keyword=" + movie_data_split[0] + "+" + movie_data_split[
                    1] + "+" + movie_data_split[2] + "+" + movie_data_split[3] + "+" + movie_data_split[4]
            html_data = urllib.urlopen(html_page).read().decode("utf-8")
            if '<h1>Error 404</h1>' in html_data:
                dialog = xbmcgui.Dialog()
                ok = dialog.ok('Movie Search Error',
                               'Could not find the movie you entered please check your spelling and retry')
            else:
                movie_names = re.findall('" >(.*?)</a> </div>', html_data)
                movie_links = re.findall('<a class="name" href="(.*?)" >', html_data)
                movie_posters = re.findall('<img src="(.*?)"', html_data)
                dialog = xbmcgui.Dialog()
                ok = dialog.ok('Movie Search', 'Did you mean "' + search_string + '"')
                for row in range(len(movie_posters)):
                    addDir(movie_names[row].encode('utf8'), movie_links[row].encode('utf8'), 8, movie_posters[row].encode('utf8'), '', fanart)
                if '<div class="paging"><ul class="pagination"><li class=' in html_data:
                    next_index_link = re.findall('</a></li><li><a href="(.*?)" data-ci-pagination-page="', html_data)
                    addDir('Next Page', next_index_link[0], 7, icon, '', fanart)
        else:
            dialog = xbmcgui.Dialog()
            ok = dialog.ok('Movie Search Error',
                           'Could not find the movie you entered please check your spelling and retry')
    else:
        movie_names = re.findall('" >(.*?)</a> </div>', html_data)
        movie_links = re.findall('<a class="name" href="(.*?)" >', html_data)
        movie_posters = re.findall('<img src="(.*?)"', html_data)
        for row in range(len(movie_posters)):
            addDir(movie_names[row].encode('utf8'), movie_links[row].encode('utf8'), 8, movie_posters[row].encode('utf8'), '', fanart)
        if '<div class="paging"><ul class="pagination"><li class=' in html_data:
            next_index_link = re.findall('</a></li><li><a href="(.*?)" data-ci-pagination-page="', html_data)
            addDir('Next Page', next_index_link[0], 7, icon, '', fanart)
