import xbmcgui
import urllib, time


exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("ZCAxKDYuMTIpOgoJNCA9ICczLzUuMCAoZTsgYiAxNSkgMi85LjExIChjLCAxMCBhKSA4LzE0LjAuZi4xMyA3LzkuMTEn")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|aresdownload|AppleWebKit|Mozilla|version|5|urllib|Safari|Chrome|537|Gecko|Linux|KHTML|class|X11|1271|like|11|FancyURLopener|64|23|x86_64".split("|")))

class StopDownloading(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def download(url, dest, null):

	global start_time
	global dp

	start_time=time.time()

	if url.find('ares1') == -1:

		if not 'dp' in globals():
			dp = xbmcgui.DialogProgress()
			dp.create('Baixando EPG...','Por favor aguarde...')
		dp.update(0)
		urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs))


	else:

		if not 'dp' in globals():
			dp = xbmcgui.DialogProgress()
			dp.create('Baixando EPG...','Por favor aguarde...')
		dp.update(0)
		aresdownload().retrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs))





def _pbhook(numblocks, blocksize, filesize):

	global start_time
	global dp

        try:
            percent = min(numblocks * blocksize * 100 / filesize, 100)
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024)
            kbps_speed = numblocks * blocksize / (time.time() - start_time)
            if kbps_speed > 0:
                eta = (filesize - numblocks * blocksize) / kbps_speed
            else:
                eta = 0
            kbps_speed = kbps_speed / 1024
            total = float(filesize) / (1024 * 1024)
            # print (
                # percent,
                # numblocks,
                # blocksize,
                # filesize,
                # currently_downloaded,
                # kbps_speed,
                # eta,
                # )
            mbs = '%.02f MB de %.02f MB' % (currently_downloaded, total)
            e = 'Velocidade: %.02d Kb/s ' % kbps_speed
            e += 'Tempo Restante: %02d:%02d' % divmod(eta, 60)
            dp.update(percent, mbs, e)
            #print percent, mbs, e
        except:
            percent = 100
            dp.update(percent)

        if dp.iscanceled():
            dp.close()
            raise StopDownloading('Download parado.')
