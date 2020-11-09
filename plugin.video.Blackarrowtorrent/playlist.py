import xbmc
import xbmcgui


def play_playlist2(name, mu_playlist):
        import urlparse
        if addon.getSetting('ask_playlist_items') == 'true':
            names = []
            for i in mu_playlist:
                d_name=urlparse.urlparse(i).netloc
                if d_name == '':
                    names.append(name)
                else:
                    names.append(d_name)
            dialog = xbmcgui.Dialog()
            index = dialog.select('Choose a video source', names)
            if index >= 0:
                if "&mode=19" in mu_playlist[index]:
                    xbmc.Player().play(urlsolver(mu_playlist[index].replace('&mode=19','')))
                elif "$doregex" in mu_playlist[index] :

                    sepate = mu_playlist[index].split('&regexs=')

                    url,setresolved = getRegexParsed(sepate[1], sepate[0])
                    xbmc.Player().play(url)
                else:
                    url = mu_playlist[index]
                    xbmc.Player().play(url)
        else:
            playlist = xbmc.PlayList(1) # 1 means video
            playlist.clear()
            item = 0
            for i in mu_playlist:
                item += 1
                info = xbmcgui.ListItem('%s) %s' %(str(item),name))
                playlist.add(i, info)
                xbmc.executebuiltin('playlist.playoffset(video,0)')
