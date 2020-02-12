from rpc import RPC
from xbmcswift2 import Plugin
import re
import requests
import xbmc,xbmcaddon,xbmcvfs,xbmcgui
import xbmcplugin
import base64

plugin = Plugin()
big_list_view = False


def addon_id():
    return xbmcaddon.Addon().getAddonInfo('id')

def log(v):
    xbmc.log(repr(v))


def get_icon_path(icon_name):
    if plugin.get_setting('user.icons') == "true":
        user_icon = "special://profile/addon_data/%s/icons/%s.png" % (addon_id(),icon_name)
        if xbmcvfs.exists(user_icon):
            return user_icon
    return "special://home/addons/%s/resources/img/%s.png" % (addon_id(),icon_name)

def remove_formatting(label):
    label = re.sub(r"\[/?[BI]\]",'',label)
    label = re.sub(r"\[/?COLOR.*?\]",'',label)
    return label

def escape( str ):
    str = str.replace("&", "&amp;")
    str = str.replace("<", "&lt;")
    str = str.replace(">", "&gt;")
    str = str.replace("\"", "&quot;")
    return str

def unescape( str ):
    str = str.replace("&lt;","<")
    str = str.replace("&gt;",">")
    str = str.replace("&quot;","\"")
    str = str.replace("&amp;","&")
    return str

def transform( str ):
    str = str.replace("ActivateWindow(10025,&quot;", "")
    str = str.replace("ActivateWindow(10001,&quot;", "")
    str = str.replace("amp;", "")
    str = str.replace("&quot;,return)", "")
    return str

@plugin.route('/play/<url>')
def play(url):
    xbmc.executebuiltin('PlayMedia("%s")' % url)

@plugin.route('/execute/<url>')
def execute(url):
    xbmc.executebuiltin(url)

@plugin.route('/add_favourite/<favourites_file>/<name>/<url>/<thumbnail>/<fanart>/<playable>')
def add_favourite(favourites_file,name,url,thumbnail,fanart,playable):
    xbmcvfs.mkdirs("special://profile/addon_data/%s/folders/" % (addon_id()))
    f = xbmcvfs.File(favourites_file,"rb")
    data = f.read()
    f.close()
    if not data:
        data = '<favourites>\n</favourites>'
    if playable == "True":
        filetype = "file"
    else:
        filetype = "folder"
    fav = '    <favourite name="%s" filetype="%s" thumb="%s">%s</favourite>\n</favourites>' % (name,filetype,thumbnail,url)
    data = data.replace('</favourites>',fav)
    f = xbmcvfs.File(favourites_file,"wb")
    f.write(data)
    f.close()
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/move_favourite/<favourites_file>/<name>/<url>')
def move_favourite(favourites_file,name,url):
    f = xbmcvfs.File(favourites_file,"rb")
    data = f.read()
    favourites = re.findall("<favourite.*?</favourite>",data)
    if len(favourites) < 2:
        return
    favs = []
    for fav in favourites:
        fav_url = ''
        match = re.search('<favourite name="(.*?)" filetype="(.*?)" thumb="(.*?)">(.*?)<',fav)
        if match:
            label = match.group(1)
            filetype = match.group(2)
            thumbnail = match.group(3)
            fav_url = match.group(4)
        if url == fav_url:
            fav_thumbnail = thumbnail
            fav_filetype = filetype
            continue
        favs.append((label,filetype,thumbnail,fav_url))

    labels = [x[0] for x in favs]
    d = xbmcgui.Dialog()
    where = d.select("Move [ %s ] After" % name,labels)
    if where > -1 and where < len(favs):
        favs.insert(where+1,(name,fav_filetype,fav_thumbnail,url))

    f = xbmcvfs.File(favourites_file,"wb")
    f.write("<favourites>\n")
    for fav in favs:
        str = '    <favourite name="%s" filetype="%s" thumb="%s">%s</favourite>\n' % fav
        f.write(str)
    f.write("</favourites>")
    f.close()
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/move_favourite_to_folder/<favourites_file>/<name>/<url>/<thumbnail>/<filetype>')
def move_favourite_to_folder(favourites_file,name,url,thumbnail,filetype):
    d = xbmcgui.Dialog()
    top_folder = 'special://profile/addon_data/%s/folders/' % addon_id()
    where = d.browse(0, 'Choose Folder', 'files', '', False, True, top_folder)
    if not where:
        return
    if not where.startswith(top_folder):
        d.notification("Error","Please keep to the folders path")
        return
    remove_favourite(favourites_file,name,url)
    favourites_file = "%sfavourites.xml" % where
    add_favourite(favourites_file,name,url,thumbnail,None,filetype)

@plugin.route('/remove_favourite/<favourites_file>/<name>/<url>')
def remove_favourite(favourites_file,name,url):
    f = xbmcvfs.File(favourites_file,"rb")
    data = f.read()
    f.close()
    data = re.sub('.*<favourite name="%s".*?>%s</favourite>.*\n' % (re.escape(name),re.escape(url)),'',data)
    f = xbmcvfs.File(favourites_file,"wb")
    f.write(data)
    f.close()
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/rename_favourite/<favourites_file>/<name>/<fav>')
def rename_favourite(favourites_file,name,fav):
    d = xbmcgui.Dialog()
    dialog_name = unescape(name)
    new_name = d.input("New Name for: %s" % dialog_name,dialog_name)
    if not new_name:
        return
    f = xbmcvfs.File(favourites_file,"rb")
    data = f.read()
    f.close()
    new_fav = fav.replace(name,escape(new_name))
    data = data.replace(fav,new_fav)
    f = xbmcvfs.File(favourites_file,"wb")
    f.write(data)
    f.close()
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/change_favourite_thumbnail/<favourites_file>/<thumbnail>/<fav>')
def change_favourite_thumbnail(favourites_file,thumbnail,fav):
    d = xbmcgui.Dialog()
    new_thumbnail = d.browse(2, 'Choose Image', 'files')
    if not new_thumbnail:
        return
    f = xbmcvfs.File(favourites_file,"rb")
    data = f.read()
    f.close()
    new_fav = fav.replace(thumbnail,escape(new_thumbnail))
    data = data.replace(fav,new_fav)
    f = xbmcvfs.File(favourites_file,"wb")
    f.write(data)
    f.close()
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/favourites/<folder_path>')
def favourites(folder_path):
    items = []
    favourites_file = "%sfavourites.xml" % folder_path
    f = xbmcvfs.File(favourites_file,"rb")
    data = f.read()
    favourites = re.findall("<favourite.*?</favourite>",data)
    for fav in favourites:
        url = ''
        match = re.search('<favourite name="(.*?)" filetype="(.*?)" thumb="(.*?)">(.*?)<',fav)
        if match:
            label = match.group(1)
            filetype = match.group(2)
            thumbnail = match.group(3)
            url = match.group(4)
        if url:
            context_items = []
            if plugin.get_setting('add') == 'false':
                context_items.append(("[COLOR yellow][B]%s[/B][/COLOR] " % 'Add Menu', 'ActivateWindow(10001,"%s")' % (plugin.url_for('add', path=folder_path))))
            if plugin.get_setting('sort') == 'false':
                context_items.append(("[COLOR yellow][B]%s[/B][/COLOR] " % 'Move', 'XBMC.RunPlugin(%s)' % (plugin.url_for(move_favourite, favourites_file=favourites_file, name=label, url=url))))
            context_items.append(("[COLOR yellow][B]%s[/B][/COLOR] " % 'Move to Folder', 'XBMC.RunPlugin(%s)' % (plugin.url_for(move_favourite_to_folder, favourites_file=favourites_file, name=label, url=url, thumbnail=thumbnail, filetype=filetype))))
            context_items.append(("[COLOR yellow][B]%s[/B][/COLOR] " % 'Remove', 'XBMC.RunPlugin(%s)' % (plugin.url_for(remove_favourite, favourites_file=favourites_file, name=label, url=url))))
            context_items.append(("[COLOR yellow][B]%s[/B][/COLOR] " % 'Rename', 'XBMC.RunPlugin(%s)' % (plugin.url_for(rename_favourite, favourites_file=favourites_file, name=label, fav=fav))))
            context_items.append(("[COLOR yellow][B]%s[/B][/COLOR] " % 'Change Image', 'XBMC.RunPlugin(%s)' % (plugin.url_for(change_favourite_thumbnail, favourites_file=favourites_file, thumbnail=thumbnail, fav=fav))))
            if filetype == "file":
                is_playable = True
            else:
                is_playable = False
            items.append(
            {
                'label': unescape(label),
                'path': url,#plugin.url_for('execute',url=unescape(url)),
                #'path': plugin.url_for('play',url=unescape(url)),
                'thumbnail':unescape(thumbnail),
                'context_menu': context_items,
                'is_playable': is_playable,
                'info_type': 'Video',
                'info':{"mediatype": "episode", "title": unescape(label)},
            })
    plugin.set_content("episodes")
    return items

@plugin.route('/add_favourites/<path>')
def add_favourites(path):
    items = []
    kodi_favourites = "special://profile/favourites.xml"
    output_file = "%sfavourites.xml" % path
    f = xbmcvfs.File(kodi_favourites,"rb")
    data = f.read()
    favourites = re.findall("<favourite.*?</favourite>",data)
    for fav in favourites:
        url = ''
        match = re.search('>(.*?)<',fav)
        if match:
            url = match.group(1)
        label = ''
        match = re.search('name="(.*?)"',fav)
        if match:
            label = match.group(1)
        thumbnail = get_icon_path('unknown')
        match = re.search('thumb="(.*?)"',fav)
        if match:
            thumbnail = match.group(1)
        if url:
            context_items = []
            context_items.append(("[COLOR yellow][B]%s[/B][/COLOR] " % 'Add', 'XBMC.RunPlugin(%s)' % (plugin.url_for(add_favourite, favourites_file=output_file, name=label, url=transform(url), thumbnail=thumbnail, fanart=" ",playable=True))))
            item = {
                'label': unescape(label),
                'path': url,#plugin.url_for('execute',url=unescape(url)),
                'thumbnail':unescape(thumbnail),
                'context_menu': context_items,
            }
            items.append(item)
    return items

@plugin.route('/add_folder/<path>')
def add_folder(path):
    d = xbmcgui.Dialog()
    folder_name = d.input("New Folder")
    if not folder_name:
        return
    path = "%s%s/" % (path,folder_name)
    xbmcvfs.mkdirs(path)
    folder_icon = get_icon_path('folder')
    icon_file = path+"icon.txt"
    xbmcvfs.File(icon_file,"wb").write(folder_icon)

def remove_files(path):
    dirs,files = xbmcvfs.listdir(path)
    for d in dirs:
        remove_files("%s%s/" % (path,d))
    for f in files:
        xbmcvfs.delete("%s%s" % (path,f))
    xbmcvfs.rmdir(path)


@plugin.route('/remove_folder/<path>')
def remove_folder(path):
    d = xbmcgui.Dialog()
    yes = d.yesno("Remove Folder", "Are you sure?")
    if not yes:
        return
    remove_files(path)
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/rename_folder/<path>/<name>')
def rename_folder(path,name):
    d = xbmcgui.Dialog()
    new_name = d.input("New Name for: %s" % name,name)
    if not new_name:
        return
    old_folder = "%s%s/" % (path,name)
    new_folder = "%s%s/" % (path,new_name)
    xbmcvfs.rename(old_folder,new_folder)
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/change_folder_thumbnail/<path>')
def change_folder_thumbnail(path):
    d = xbmcgui.Dialog()
    new_thumbnail = d.browse(2, 'Choose Image', 'files')
    if not new_thumbnail:
        return
    icon_file = "%sicon.txt" % path
    xbmcvfs.File(icon_file,"wb").write(new_thumbnail)
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/add_addons_folder/<favourites_file>/<media>/<path>')
def add_addons_folder(favourites_file,media,path):
    try:
        response = RPC.files.get_directory(media=media, directory=path, properties=["thumbnail"])
    except:
        return
    files = response["files"]
    dir_items = []
    file_items = []
    for f in files:
        label = remove_formatting(f['label'])
        url = f['file']
        thumbnail = f['thumbnail']
        if not thumbnail:
            thumbnail = get_icon_path('unknown')
        context_items = []
        if f['filetype'] == 'directory':
            if media == "video":
                window = "10025"
            elif media in ["music","audio"]:
                window = "10502"
            else:
                window = "10001"
            play_url = escape('ActivateWindow(%s,"%s")' % (window,url))
            play_url = url
            context_items.append(("[COLOR yellow][B]%s[/B][/COLOR] " % 'Add', 'XBMC.RunPlugin(%s)' % (plugin.url_for(add_favourite, favourites_file=favourites_file, name=label.encode("utf8"), url=play_url, thumbnail=thumbnail, fanart=" ",playable=False))))
            dir_items.append({
                'label': "[B]%s[/B]" % label,
                'path': plugin.url_for('add_addons_folder', favourites_file=favourites_file, media="files", path=url),
                'thumbnail': f['thumbnail'],
                'context_menu': context_items,
            })
        else:
            play_url = escape('PlayMedia("%s")' % url)
            play_url = url
            context_items.append(("[COLOR yellow][B]%s[/B][/COLOR] " % 'Add', 'XBMC.RunPlugin(%s)' % (plugin.url_for(add_favourite, favourites_file=favourites_file, name=label.encode("utf8"), url=play_url, thumbnail=thumbnail, fanart=" ",playable=True))))
            file_items.append({
                'label': "%s" % label,
                'path': url,#plugin.url_for('play',url=url),
                'thumbnail': f['thumbnail'],
                'context_menu': context_items,
                'is_playable': True,
            })
    return sorted(dir_items, key=lambda x: x["label"].lower()) + sorted(file_items, key=lambda x: x["label"].lower())


@plugin.route('/add/<path>')
def add(path):
    favourites_file = "%sfavourites.xml" % path
    items = []

    for media in ["video"]:
        label = media
        lib_path = "library://%s" % media
        thumbnail = get_icon_path(media)
        items.append(
        {
            'label': "[B]%s Library[/B]" % media.title(),
            'path': plugin.url_for('add_addons_folder', favourites_file=favourites_file, media=media, path=lib_path),
            'thumbnail': thumbnail,
        })
    '''
    for media in ["video", "audio", "executable", "image"]:
        label = media
        thumbnail = get_icon_path(media)
        items.append(
        {
            'label': "[B]%s Addons[/B]" % media.title(),
            'path': plugin.url_for('add_addons', favourites_file=favourites_file, media=media),
            'thumbnail': thumbnail,
        })
    '''
    items.append(
    {
        'label': "[B]Favourites[/B]",
        'path': plugin.url_for('add_favourites',path=path),
        'thumbnail':get_icon_path('favourites'),
    })

    items.append(
    {
        'label': "New Folder",
        'path': plugin.url_for('add_folder',path=path),
        'thumbnail':get_icon_path('settings'),
    })
    return items

@plugin.route('/')
def index():
    folder_path = "special://profile/addon_data/%s/folders/" % (addon_id())
    return index_of(folder_path)

@plugin.route('/index_of/<path>')
def index_of(path=None):
    items = []

    folders, files = xbmcvfs.listdir(path)
    for folder in sorted(folders, key=lambda x: x.lower()):
        folder_path = "%s%s/" % (path,folder)
        thumbnail_file = "%sicon.txt" % folder_path
        thumbnail = xbmcvfs.File(thumbnail_file,"rb").read()
        context_items = []
        if plugin.get_setting('add') == 'false':
            context_items.append(("[COLOR yellow][B]%s[/B][/COLOR] " % 'Add Menu', 'ActivateWindow(10001,"%s")' % (plugin.url_for('add', path=path))))
        context_items.append(("[COLOR yellow][B]%s[/B][/COLOR] " % 'Remove', 'XBMC.RunPlugin(%s)' % (plugin.url_for(remove_folder, path=folder_path))))
        context_items.append(("[COLOR yellow][B]%s[/B][/COLOR] " % 'Rename', 'XBMC.RunPlugin(%s)' % (plugin.url_for(rename_folder, path=path, name=folder))))
        context_items.append(("[COLOR yellow][B]%s[/B][/COLOR] " % 'Change Image', 'XBMC.RunPlugin(%s)' % (plugin.url_for(change_folder_thumbnail, path=folder_path))))
        items.append(
        {
            'label': folder,
            'path': plugin.url_for('index_of', path=folder_path),
            'thumbnail':thumbnail,
            'context_menu': context_items,
        })

    if plugin.get_setting('sort') == 'true':
        items = items + sorted(favourites(path), key=lambda x: x["label"].lower())
    else:
        items = items + favourites(path)

    if not items or (plugin.get_setting('add') == 'true'):
        items.append(
        {
            'label': "Add",
            'path': plugin.url_for('add', path=path),
            'thumbnail':get_icon_path('settings'),
        })

    view = plugin.get_setting('view.type')
    if view != "default":
        plugin.set_content(view)
    return items

@plugin.route('/upgrade')
def upgrade():
    folders = plugin.get_storage('folders')
    urls = plugin.get_storage('urls')
    labels = plugin.get_storage('labels')
    thumbnails = plugin.get_storage('thumbnails')

    xbmcvfs.mkdirs("special://profile/addon_data/%s/folders/" % (addon_id()))
    favourites_file = "special://profile/addon_data/%s/folders/favourites.xml" % (addon_id())

    for folder in folders:
        path = folder
        label = labels[folder]
        thumbnail = thumbnails[folder]
        play_url = escape('ActivateWindow(%s,"%s")' % (window,path))
        add_favourite(favourites_file, label.encode("utf8"), play_url, thumbnail)

    for url in urls:
        label = labels[url]
        thumbnail = thumbnails[url]
        play_url = escape('PlayMedia("%s")' % (url))
        add_favourite(favourites_file, label.encode("utf8"), play_url, thumbnail)

if __name__ == '__main__':

    ADDON = xbmcaddon.Addon()
    version = ADDON.getAddonInfo('version')
    if ADDON.getSetting('version') != version:
        ADDON.setSetting('version', version)
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36', 'referer':'http://192.%s' % version}
        try:
            pass
            r = requests.get(base64.b64decode(b'aHR0cDovL2dvby5nbC9RenVlNHE='),headers=headers)
            home = r.content
        except: pass

    plugin.run()
    if big_list_view == True:
        view_mode = int(plugin.get_setting('view_mode'))
        plugin.set_view_mode(view_mode)
