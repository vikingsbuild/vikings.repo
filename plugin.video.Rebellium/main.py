# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import urllib
import urllib2
import datetime
from datetime import datetime
import xml.etree.ElementTree as ET
import re
import os
import base64
import codecs
import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import time
from BeautifulSoup import BeautifulStoneSoup, BeautifulSOAP
from bs4 import BeautifulSoup
try:
    import json
except:
    import simplejson as json


##CONFIGURAÇÕES
####  TITULO DO MENU  #################################################################
title_menu = "[B][COLOR white]BEM-VINDOS AO [COLOR skyblue][B]REBELLIUM[/COLOR][/B]"
###  DESCRIÇÃO DO ADDON ###############################################################
title_descricao = "REBELLIUM Trazendo o melhor conteudo de filmes e séries para você e toda sua família"
####  LINK DO TITULO DE MENU  #########################################################
url_title = 'AGRADECEMOS POR USAREM O ADDON REBELLIUM'

#### MENSAGEM BEM VINDOS  #############################################################
titulo_boas_vindas = "BEM-VINDOS"
mensagem_bem_vindo = "[B][COLOR white]Obrigado por terem escolhido o REBELLIUM[/COLOR]\n[COLOR white]Entre no nosso grupo do:[/COLOR] [COLOR green]Whatsaap[/COLOR] (71) 9619-1556[/B]"
####  MENSAGEM SECUNDARIA ######################################################
mensagem_secundaria = "[COLOR skyblue][B]REBELLIUM[/B][/COLOR] - [COLOR white][B]O MELHOR PRA VOCÊ[/B][/COLOR]"
####  TEMPO DA MENSAGEM EM MILISEGUNDOS ###############################################
time_msg = 15000


## MENU CONFIGURAÇÕES
menu_configuracoes = "[B][COLOR white]CONFIGURAÇÕES[/COLOR][/B]"
thumb_icon_config = ''
desc_configuracoes = "Configurações do REBELLIUM"

## FAVORITOS
menu_favoritos = "[B][COLOR white]FAVORITOS[/COLOR][/B]"
thumb_favoritos = ''
desc_favoritos = "Adicione Itens aos Favoritos, pressionando OK do controle "

#### MENU VIP ################################################################
titulo_vip = "[B][COLOR white]REBELLIUM[/COLOR]  [COLOR gold](VIP)[/COLOR][/B]"
thumbnail_vip = 'https://ia601504.us.archive.org/0/items/vip_20200719/vip.jpg'
fanart_vip = 'https://ia601504.us.archive.org/0/items/vip_20200719/vip.jpg'
#### DESCRIÇÃO VIP ###########################################################
vip_descricao = 'SOLICITE SEU TESTE VIP, O MENOR PREÇO DE TODOS'
#### DIALOGO VIP - SERVIDOR DESATIVADO - CLICK ###################################
vip_dialogo = "[B][COLOR white]CONFIGURE SEU ACESSO A NOSSA ÁREA VIP ANTES DE ENTRAR AQUI, MAIS INFORMAÇÕES ENTRE EM CONTATO COM NOSSO SUPORTE\nENTRE EM COMTATO PELO WHATSAPP: 55+ (71) 9619-1556 E SOLICITE SEU TESTE[/COLOR][/B]"
##SERIVODR VIP
url_server_vip1 = ''
url_server_vip2 = ''

##CONTADOR DE ACESSO
url_contador = 'https://whos.amung.us/pingjs/?k=0hxv4huvw3'
nome_contador = 'SeuAddon-3.1.7'


## MULTLINK
## nome para $nome, padrão: lsname para $lsname
playlist_command = 'nome'
dialog_playlist = 'Selecione um item'


# user - Padrão: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0
#useragent_b64 = 'digite-o-user-agent-em-base64'
#useragent = base64.b32decode(useragent_b64).decode('utf-8')
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"

#Base
url_b64_principal = 'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L1JrcHZHdDkw'
url_principal = base64.b64decode(url_b64_principal).decode('utf-8')


    
if sys.argv[1] == 'limparFavoritos':
    Path = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile')).decode("utf-8")
    arquivo = os.path.join(Path, "favorites.dat")
    exists = os.path.isfile(arquivo)
    if exists:
        try:
            os.remove(arquivo)
        except:
            pass
    xbmcgui.Dialog().ok('Sucesso', '[B][COLOR red]Favoritos limpo com sucesso![/COLOR][/B]')
    xbmc.sleep(2000)
    exit()


if sys.argv[1] == 'SetPassword':
    addonID = xbmcaddon.Addon().getAddonInfo('id')
    addon_data_path = xbmc.translatePath(os.path.join('special://home/userdata/addon_data', addonID))
    if os.path.exists(addon_data_path)==False:
        os.mkdir(addon_data_path)
    xbmc.sleep(4)
    #Path = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile')).decode("utf-8")
    #arquivo = os.path.join(Path, "password.txt")
    arquivo = os.path.join(addon_data_path, "password.txt")
    exists = os.path.isfile(arquivo)
    keyboard = xbmcaddon.Addon().getSetting("keyboard")
    if exists == False:
        password = '0069'
        p_encoded = base64.b64encode(password.encode()).decode('utf-8')
        p_file1 = open(arquivo,'w')
        p_file1.write(p_encoded)
        p_file1.close()
        xbmc.sleep(4)
        p_file = open(arquivo,'r+')
        p_file_read = p_file.read()
        p_file_b64_decode = base64.b64decode(p_file_read).decode('utf-8')
        dialog = xbmcgui.Dialog()
        if int(keyboard) == 0:
            ps = dialog.numeric(0, 'Insira a senha atual:')
        else:
            ps = dialog.input('Insira a senha atual:', option=xbmcgui.ALPHANUM_HIDE_INPUT)
        if ps == p_file_b64_decode:
            if int(keyboard) == 0:
                ps2 = dialog.numeric(0, 'Insira a nova senha:')
            else:
                ps2 = dialog.input('Insira a senha atual:', option=xbmcgui.ALPHANUM_HIDE_INPUT)
            if ps2 != '':
                ps2_b64 = base64.b64encode(ps2.encode()).decode('utf-8')
                p_file = open(arquivo,'w')
                p_file.write(ps2_b64)
                p_file.close()
                xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','A Senha foi alterada com sucesso!')
            else:
                xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','Não foi possivel alterar a senha!')
        else:
            xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','Senha invalida!, se não alterou utilize a senha padrão')
    else:
        p_file = open(arquivo,'r+')
        p_file_read = p_file.read()
        p_file_b64_decode = base64.b64decode(p_file_read).decode('utf-8')
        dialog = xbmcgui.Dialog()
        if int(keyboard) == 0:
            ps = dialog.numeric(0, 'Insira a senha atual:')
        else:
            ps = dialog.input('Insira a senha atual:', option=xbmcgui.ALPHANUM_HIDE_INPUT)
        if ps == p_file_b64_decode:
            if int(keyboard) == 0:
                ps2 = dialog.numeric(0, 'Insira a nova senha:')
            else:
                ps2 = dialog.input('Insira a senha atual:', option=xbmcgui.ALPHANUM_HIDE_INPUT)
            if ps2 != '':
                ps2_b64 = base64.b64encode(ps2.encode()).decode('utf-8')
                p_file = open(arquivo,'w')
                p_file.write(ps2_b64)
                p_file.close()
                xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','A Senha foi alterada com sucesso!')
            else:
                xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','Não foi possivel alterar a senha!')
        else:
            xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','Senha invalida!, se não alterou utilize a senha padrão')
    exit()



addon_handle = int(sys.argv[1])
__addon__ = xbmcaddon.Addon()
addon = __addon__
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
addon_version = __addon__.getAddonInfo('version')
profile = xbmc.translatePath(__addon__.getAddonInfo('profile').decode('utf-8'))
home = xbmc.translatePath(__addon__.getAddonInfo('path').decode('utf-8'))
favorites = os.path.join(profile, 'favorites.dat')
favoritos = xbmcaddon.Addon().getSetting("favoritos")

if os.path.exists(favorites)==True:
    FAV = open(favorites).read()
else: 
    FAV = []


def notify(message, timeShown=5000):
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % (__addonname__, message, timeShown, __icon__))



def getRequest(url, count):
    proxy_mode = addon.getSetting('proxy')
    if proxy_mode == 'true':
        try:
            import requests
            import random
            headers={'User-agent': useragent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Content-Type': 'text/html'}
            if int(count) > 0:
                attempt = int(count)-1
            else:
                attempt = 0
            #print('tentativa: '+str(attempt)+'')
            ### https://proxyscrape.com/free-proxy-list
            ##http
            data_proxy1 = getRequest2('', '')
            list1 = data_proxy1.splitlines()
            total1 = len(list1)
            number_http = random.randint(0,total1-1)
            proxy_http = 'http://'+list1[number_http]
            ##https
            data_proxy2 = getRequest2('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=BR&ssl=yes&anonymity=all', '')
            list2 = data_proxy2.splitlines()
            total2 = len(list2)
            number_https = random.randint(0,total2-1)
            proxy_https = 'https://'+list2[number_https]
            #print(proxy_https)
            proxyDict = {"http" : proxy_http, "https" : proxy_https}
            req = requests.get(url, headers=headers, proxies=proxyDict)
            req.encoding = 'utf-8'
            #status = req.status_code
            response = req.text
            return response
        except:
            proxy_number = addon.getSetting('proxy_try')
            if int(attempt) > 0:
                limit = int(attempt)
            elif int(count) == 1 and int(attempt) == 0:
                limit = int(proxy_number)+1+1
            if int(limit) > 1:
                #print('ativar outro proxy')
                data = getRequest(url, int(limit))
                return data
            else:
                notify('[COLOR red]Erro ao utilizar o proxy ou servidor![/COLOR]')
                response = ''
                return response
    else:
        try:
            try:
                import urllib.request as urllib2
            except ImportError:
                import urllib2
            request_headers = {
            "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,ru;q=0.7,de-DE;q=0.6,de;q=0.5,de-AT;q=0.4,de-CH;q=0.3,ja;q=0.2,zh-CN;q=0.1,zh;q=0.1,zh-TW;q=0.1,es;q=0.1,ar;q=0.1,en-GB;q=0.1,hi;q=0.1,cs;q=0.1,el;q=0.1,he;q=0.1,en-US;q=0.1",
            "User-Agent": useragent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
            }
            request = urllib2.Request(url, headers=request_headers)
            response = urllib2.urlopen(request).read().decode('utf-8')
            return response
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                xbmc.executebuiltin("XBMC.Notification(Falha, código de erro - "+str(e.code)+",10000,"+__icon__+")")    
            elif hasattr(e, 'reason'):
                xbmc.executebuiltin("XBMC.Notification(Falha, motivo - "+str(e.reason)+",10000,"+__icon__+")")
            response = ''
            return response



def getRequest2(url, ref):
    try:
        try:
            import urllib.request as urllib2
        except ImportError:
            import urllib2
        if ref > '':
            ref2 = ref
        else:
            ref2 = url
        request_headers = {
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,ru;q=0.7,de-DE;q=0.6,de;q=0.5,de-AT;q=0.4,de-CH;q=0.3,ja;q=0.2,zh-CN;q=0.1,zh;q=0.1,zh-TW;q=0.1,es;q=0.1,ar;q=0.1,en-GB;q=0.1,hi;q=0.1,cs;q=0.1,el;q=0.1,he;q=0.1,en-US;q=0.1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer": ref2
        }
        request = urllib2.Request(url, headers=request_headers)
        response = urllib2.urlopen(request).read().decode('utf-8')
        return response
    except:
        #pass
        response = ''
        return response




def regex_get_all(text, start_with, end_with):
    r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
    return r



def re_me(data, re_patten):
    match = ''
    m = re.search(re_patten, data)
    if m != None:
        match = m.group(1)
    else:
        match = ''
    return match


def vip_serverlist():
	dnsvip = xbmcaddon.Addon().getSetting("dnsvip")
	if int(dnsvip) == 0:
		url_server_vip = url_server_vip1
	elif int(dnsvip) == 1:
		url_server_vip = url_server_vip2
	return url_server_vip


def resolve_data(url):
    server_vip = vip_serverlist()
    if url.startswith(server_vip) == True:
        data = getRequest2(url, '')
    else:
        data = getRequest(url, 1)
    return data



def getData(url, fanart):
    adult = xbmcaddon.Addon().getSetting("adult")
    adult2 = xbmcaddon.Addon().getSetting("adult2")
    uhdtv = addon.getSetting('uhdtv')
    fhdtv = addon.getSetting('fhdtv')
    hdtv = addon.getSetting('hdtv')
    sdtv = addon.getSetting('sdtv')
    #futebol = addon.getSetting('futebol')
    filtrar = addon.getSetting('filtrar')
    data = resolve_data(url)
    #soup = BeautifulSoup(data, 'html.parser')
    soup = BeautifulSOAP(data, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
    #if isinstance(soup,BeautifulSoup):
    if isinstance(soup,BeautifulSOAP):
        #if len(soup('layoutype')) > 0:
        #    SetViewLayout = "thumbnail"

        if len(soup('channels')) > 0:
            channels = soup('channel')
            for channel in channels:
#                print channel

                linkedUrl=''
                lcount=0
                try:
                    linkedUrl =  channel('externallink')[0].string
                    lcount=len(channel('externallink'))
                except: pass
                #print 'linkedUrl',linkedUrl,lcount
                if lcount>1: linkedUrl=''
                try:
                    name = channel('name')[0].string
                except:
                    name = 'Desconhecido'
                try:
                    thumbnail = channel('thumbnail')[0].string
                    if thumbnail == None:
                        thumbnail = ''
                except:
                    thumbnail = ''

                try:
                    if not channel('fanart'):
                        if __addon__.getSetting('use_thumb') == "true":
                            fanArt = thumbnail
                        else:
                            fanArt = fanart
                    else:
                        fanArt = channel('fanart')[0].string
                    if fanArt == None:
                        raise
                except:
                    fanArt = fanart

                try:
                    desc = channel('info')[0].string
                    if desc == None:
                        raise
                except:
                    desc = ''
                    
                try:
                    if channel('tmdb') and len(channel('tmdb')) >0 and channel('imdb') and len(channel('imdb')) >0:
                        #name2 = item('title')[0].string.replace(";", "")
                        tmdb_id = channel('tmdb')[0].string
                        imdb_id = channel('imdb')[0].string
                        title, desc, thumbnail = tmdb_info(tmdb_id)
                        name = '[B][COLOR white]'+title+'[/COLOR] [COLOR yellow](imdb '+imdb_info(imdb_id)+')[/COLOR][/B]'
                except:   
                    try:
                        name = channel('name')[0].string
                    except:
                        name = 'Desconhecido'
                    try:
                        thumbnail = channel('thumbnail')[0].string
                        if thumbnail == None:
                            thumbnail = ''
                    except:
                        thumbnail = ''
                    try:
                        desc = channel('info')[0].string
                        if desc == None:
                            raise
                    except:
                        desc = ''
                    

                try:
                    if linkedUrl=='':
                        #addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),2,thumbnail,fanArt,desc,genre,date,credits,True)
                        addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),2,thumbnail,fanArt,desc)
                    else:
                        #print linkedUrl
                        #addDir(name.encode('utf-8'),linkedUrl.encode('utf-8'),1,thumbnail,fanArt,desc,genre,date,None,'source')
                        if adult == 'false' and re.search("ADULTOS",name,re.IGNORECASE) and name.find('(+18)') >=0:
                            pass
                        else:
                            addDir(name.encode('utf-8', 'ignore'),linkedUrl.encode('utf-8'),1,thumbnail,fanArt,desc)
                except:
                    notify('[COLOR red]Erro ao Carregar os dados![/COLOR]')
        elif re.search("#EXTM3U",data) or re.search("#EXTINF",data):
            content = data.rstrip()
            match = re.compile(r'#EXTINF:(.+?),(.*?)[\n\r]+([^\r\n]+)').findall(content)
            for other,channel_name,stream_url in match:
                if 'tvg-logo' in other:
                    thumbnail = re_me(other,'tvg-logo=[\'"](.*?)[\'"]')
                    if thumbnail:
                        if thumbnail.startswith('http'):
                            thumbnail = thumbnail
                        #elif not addon.getSetting('logo-folderPath') == "":
                        #    logo_url = addon.getSetting('logo-folderPath')
                        #    thumbnail = logo_url + thumbnail

                        else:
                            thumbnail = ''
                    else:
                        thumbnail = ''
                else:
                    thumbnail = ''
                    
                if 'group-title' in other:
                    cat = re_me(other,'group-title=[\'"](.*?)[\'"]')
                else:
                    cat = ''                       

                try:
                    server_vip = vip_serverlist()
                    if url.startswith(server_vip) == True:
                        resolver_final = resolver_vip(stream_url, channel_name, thumbnail)
                    else:
                        resolver_final = resolver(stream_url, channel_name, thumbnail)                    
                    if uhdtv == 'false' and re.search("4K",channel_name):
                        pass
                    elif fhdtv == 'false' and re.search("FHD",channel_name):
                        pass
                    elif hdtv == 'false' and re.search("HD",channel_name) and not re.search("FHD",channel_name):
                        pass
                    elif sdtv == 'false' and re.search("SD",channel_name):
                        pass
                    elif sdtv == 'false' and not re.search("SD",channel_name) and not re.search("HD",channel_name) and not re.search("4K",channel_name):
                        pass
                    #Futebol
                    elif int(filtrar) == 1 and not re.search("SPORTV",channel_name,re.IGNORECASE) and not re.search("DAZN",channel_name,re.IGNORECASE) and not re.search("ESPN Brasil",channel_name,re.IGNORECASE) and not re.search("PREMIERE",channel_name,re.IGNORECASE):
                        pass
                    #Esportes
                    elif int(filtrar) == 2 and not re.search("Band Sports",channel_name,re.IGNORECASE) and not re.search("Combate",channel_name,re.IGNORECASE) and not re.search("Fox Sports",channel_name,re.IGNORECASE) and not re.search("SPORTV",channel_name,re.IGNORECASE) and not re.search("DAZN",channel_name,re.IGNORECASE) and not re.search("ESPN",channel_name,re.IGNORECASE) and not re.search("PREMIERE",channel_name,re.IGNORECASE):
                        pass
                    #Filmes e Series
                    elif int(filtrar) == 3 and re.search("Sports",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 3 and re.search("XY Max",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 3 and not re.search("AMC",channel_name,re.IGNORECASE) and not re.search("Canal Brasil",channel_name,re.IGNORECASE) and not re.search("Cinemax",channel_name,re.IGNORECASE) and not re.search("HBO",channel_name,re.IGNORECASE) and not re.search("Max",channel_name,re.IGNORECASE) and not re.search("Megapix",channel_name,re.IGNORECASE) and not re.search("Paramount",channel_name,re.IGNORECASE) and not re.search("SPACE",channel_name,re.IGNORECASE) and not re.search("TCM",channel_name,re.IGNORECASE) and not re.search("Telecine Action",channel_name,re.IGNORECASE) and not re.search("TC Action",channel_name,re.IGNORECASE) and not re.search("Telecine Cult",channel_name,re.IGNORECASE) and not re.search("TC Cult",channel_name,re.IGNORECASE) and not re.search("TC Cult",channel_name,re.IGNORECASE) and not re.search("Telecine Fun",channel_name,re.IGNORECASE) and not re.search("TC Fun",channel_name,re.IGNORECASE) and not re.search("Telecine Pipoca",channel_name,re.IGNORECASE) and not re.search("TC Pipoca",channel_name,re.IGNORECASE) and not re.search("Telecine Premium",channel_name,re.IGNORECASE) and not re.search("TC Premium",channel_name,re.IGNORECASE) and not re.search("Telecine Touch",channel_name,re.IGNORECASE) and not re.search("TC Touch",channel_name,re.IGNORECASE) and not re.search("TNT",channel_name,re.IGNORECASE) and not re.search("A&E",channel_name,re.IGNORECASE) and not re.search("AXN",channel_name,re.IGNORECASE) and not re.search("AXN",channel_name,re.IGNORECASE) and not re.search("FOX",channel_name,re.IGNORECASE) and not re.search("FX",channel_name,re.IGNORECASE) and not re.search("SONY",channel_name,re.IGNORECASE) and not re.search("Studio Universal",channel_name,re.IGNORECASE) and not re.search("SyFy",channel_name,re.IGNORECASE) and not re.search("Universal Channel",channel_name,re.IGNORECASE) and not re.search("Universal TV",channel_name,re.IGNORECASE) and not re.search("Warner",channel_name,re.IGNORECASE):
                        pass
                    #Infantil
                    elif int(filtrar) == 4 and re.search("FM",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 4 and not re.search("Baby TV",channel_name,re.IGNORECASE) and not re.search("BOOMERANG",channel_name,re.IGNORECASE) and not re.search("CARTOON NETWORK",channel_name,re.IGNORECASE) and not re.search("DISCOVERY KIDS",channel_name,re.IGNORECASE) and not re.search("DISNEY",channel_name,re.IGNORECASE) and not re.search("GLOOB",channel_name,re.IGNORECASE) and not re.search("NAT GEO KIDS",channel_name,re.IGNORECASE) and not re.search("NICKELODEON",channel_name,re.IGNORECASE) and not re.search("NICK JR",channel_name,re.IGNORECASE) and not re.search("PLAYKIDS",channel_name,re.IGNORECASE) and not re.search("TOONCAST",channel_name,re.IGNORECASE) and not re.search("ZOOMOO",channel_name,re.IGNORECASE):
                        pass
                    #Documentario
                    elif int(filtrar) == 5  and re.search("Kids",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 5 and not re.search("Discovery",channel_name,re.IGNORECASE) and not re.search("H2 HD",channel_name,re.IGNORECASE) and not re.search("H2 SD",channel_name,re.IGNORECASE) and not re.search("H2 FHD",channel_name,re.IGNORECASE) and not re.search("History",channel_name,re.IGNORECASE) and not re.search("Nat Geo Wild",channel_name,re.IGNORECASE) and not re.search("National Geographic",channel_name,re.IGNORECASE):
                        pass
                    #Abertos
                    elif int(filtrar) == 6 and re.search("Brasileirinhas",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 6 and re.search("News",channel_name,re.IGNORECASE) or int(filtrar) == 6 and re.search("Sat",channel_name,re.IGNORECASE) or int(filtrar) == 6 and re.search("FM",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 6 and not re.search("Globo",channel_name,re.IGNORECASE) and not re.search("RECORD",channel_name,re.IGNORECASE) and not re.search("RedeTV",channel_name,re.IGNORECASE) and not re.search("Rede Vida",channel_name,re.IGNORECASE) and not re.search("SBT",channel_name,re.IGNORECASE) and not re.search("TV Brasil",channel_name,re.IGNORECASE) and not re.search("TV Cultura",channel_name,re.IGNORECASE) and not re.search("TV Diario",channel_name,re.IGNORECASE) and not re.search("BAND",channel_name,re.IGNORECASE):
                        pass
                    #Reality show
                    elif int(filtrar) == 7 and not re.search("BBB",channel_name,re.IGNORECASE) and not re.search("Big Brother Brasil",channel_name,re.IGNORECASE) and not re.search("A Fazenda",channel_name,re.IGNORECASE):
                        pass
                    elif adult2 == 'false' and re.search("Adult",cat,re.IGNORECASE) or adult2 == 'false' and re.search("ADULT",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Blue Hustler",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("PlayBoy",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Redlight",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Sextreme",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("SexyHot",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Venus",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("AST TV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("ASTTV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("AST.TV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("BRAZZERS",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("CANDY",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("CENTOXCENTO",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("DORCEL",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("EROXX",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("PASSION",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("PENTHOUSE",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("PINK-O",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("PINK O",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("PRIVATE",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("RUSNOCH",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("SCT",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("SEXT6SENSO",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("SHALUN TV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("VIVID RED",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Porn",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("XY Plus",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("XY Mix",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("XY Mad",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("XXL",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Desire",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Bizarre",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Sexy HOT",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Reality Kings",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Prive TV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Hustler TV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Extasy",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Evil Angel",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Erox",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("DUSK",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Brazzers",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Brasileirinhas",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Pink Erotic",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Passion",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Passie",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Meiden Van Holland Hard",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Sext & Senso",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Super One",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Vivid TV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Hustler HD",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("SCT",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Sex Ation",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Hot TV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Hot HD",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("MILF",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("ANAL",channel_name,re.IGNORECASE) and not re.search("CANAL",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("PUSSY",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("ROCCO",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("BABES",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("BABIE",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("XY Max",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("TUSHY",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("BLACKED",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("FAKE TAXI",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("XXX",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("18",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Porno",channel_name,re.IGNORECASE):
                        pass
                    #Noticias
                    elif int(filtrar) == 8 and re.search("FM",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 8 and not re.search("CNN",channel_name,re.IGNORECASE) and not re.search("NEWS",channel_name,re.IGNORECASE):
                        pass
                    elif re.search("Adult",cat,re.IGNORECASE) or re.search("ADULT",channel_name,re.IGNORECASE) or re.search("Blue Hustler",channel_name,re.IGNORECASE) or re.search("PlayBoy",channel_name,re.IGNORECASE) or re.search("Redlight",channel_name,re.IGNORECASE) or re.search("Sextreme",channel_name,re.IGNORECASE) or re.search("SexyHot",channel_name,re.IGNORECASE) or re.search("Venus",channel_name,re.IGNORECASE) or re.search("AST TV",channel_name,re.IGNORECASE) or re.search("ASTTV",channel_name,re.IGNORECASE) or re.search("AST.TV",channel_name,re.IGNORECASE) or re.search("BRAZZERS",channel_name,re.IGNORECASE) or re.search("CANDY",channel_name,re.IGNORECASE) or re.search("CENTOXCENTO",channel_name,re.IGNORECASE) or re.search("DORCEL",channel_name,re.IGNORECASE) or re.search("EROXX",channel_name,re.IGNORECASE) or re.search("PASSION",channel_name,re.IGNORECASE) or re.search("PENTHOUSE",channel_name,re.IGNORECASE) or re.search("PINK-O",channel_name,re.IGNORECASE) or re.search("PINK O",channel_name,re.IGNORECASE) or re.search("PRIVATE",channel_name,re.IGNORECASE) or re.search("RUSNOCH",channel_name,re.IGNORECASE) or re.search("SCT",channel_name,re.IGNORECASE) or re.search("SEXT6SENSO",channel_name,re.IGNORECASE) or re.search("SHALUN TV",channel_name,re.IGNORECASE) or re.search("VIVID RED",channel_name,re.IGNORECASE) or re.search("Porn",channel_name,re.IGNORECASE) or re.search("XY Plus",channel_name,re.IGNORECASE) or re.search("XY Mix",channel_name,re.IGNORECASE) or re.search("XY Mad",channel_name,re.IGNORECASE) or re.search("XXL",channel_name,re.IGNORECASE) or re.search("Desire",channel_name,re.IGNORECASE) or re.search("Bizarre",channel_name,re.IGNORECASE) or re.search("Sexy HOT",channel_name,re.IGNORECASE) or re.search("Reality Kings",channel_name,re.IGNORECASE) or re.search("Prive TV",channel_name,re.IGNORECASE) or re.search("Hustler TV",channel_name,re.IGNORECASE) or re.search("Extasy",channel_name,re.IGNORECASE) or re.search("Evil Angel",channel_name,re.IGNORECASE) or re.search("Erox",channel_name,re.IGNORECASE) or re.search("DUSK",channel_name,re.IGNORECASE) or re.search("Brazzers",channel_name,re.IGNORECASE) or re.search("Brasileirinhas",channel_name,re.IGNORECASE) or re.search("Pink Erotic",channel_name,re.IGNORECASE) or re.search("Passion",channel_name,re.IGNORECASE) or re.search("Passie",channel_name,re.IGNORECASE) or re.search("Meiden Van Holland Hard",channel_name,re.IGNORECASE) or re.search("Sext & Senso",channel_name,re.IGNORECASE) or re.search("Super One",channel_name,re.IGNORECASE) or re.search("Vivid TV",channel_name,re.IGNORECASE) or re.search("Hustler HD",channel_name,re.IGNORECASE) or re.search("SCT",channel_name,re.IGNORECASE) or re.search("Sex Ation",channel_name,re.IGNORECASE) or re.search("Hot TV",channel_name,re.IGNORECASE) or re.search("Hot HD",channel_name,re.IGNORECASE) or re.search("MILF",channel_name,re.IGNORECASE) or re.search("ANAL",channel_name,re.IGNORECASE) and not re.search("CANAL",channel_name,re.IGNORECASE) or re.search("PUSSY",channel_name,re.IGNORECASE) or re.search("ROCCO",channel_name,re.IGNORECASE) or re.search("BABES",channel_name,re.IGNORECASE) or re.search("BABIE",channel_name,re.IGNORECASE) or re.search("XY Max",channel_name,re.IGNORECASE) or re.search("TUSHY",channel_name,re.IGNORECASE) or re.search("FAKE TAXI",channel_name,re.IGNORECASE) or re.search("BLACKED",channel_name,re.IGNORECASE) or re.search("XXX",channel_name,re.IGNORECASE) or re.search("18",channel_name,re.IGNORECASE) or re.search("Porno",channel_name,re.IGNORECASE):
                        addDir2(channel_name.encode('utf-8', 'ignore'),resolver_final.encode('utf-8'),10,'','',thumbnail,'','',False)
                    else:
                        #addLink(channel_name.encode('utf-8', 'ignore'),resolver_final.encode('utf-8'),'','',thumbnail,'','')
                        addDir2(channel_name.encode('utf-8', 'ignore'),resolver_final.encode('utf-8'),17,'','',thumbnail,'','',False)
                except:
                    #notify('[COLOR red]Erro ao Carregar os dados![/COLOR]')
                    pass
        else:
            getItems(soup('item'),fanart)
            #getItems(soup('item'))
    else:
        #parse_m3u(soup)
        notify('[COLOR red]Erro ao Carregar os dados![/COLOR]')



def getChannelItems(name,url,fanart):
        data = resolve_data(url)
        soup = BeautifulSOAP(data, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        channel_list = soup.find('channel', attrs={'name' : name.decode('utf-8')})
        items = channel_list('item')
        try:
            fanArt = channel_list('fanart')[0].string
            if fanArt == None:
                raise
        except:
            fanArt = fanart
        for channel in channel_list('subchannel'):
            name = channel('name')[0].string
            try:
                thumbnail = channel('thumbnail')[0].string
                if thumbnail == None:
                    raise
            except:
                thumbnail = ''
            try:
                if not channel('fanart'):
                    if __addon__.getSetting('use_thumb') == "true":
                        fanArt = thumbnail
                else:
                    fanArt = channel('fanart')[0].string
                if fanArt == None:
                    raise
            except:
                pass
            try:
                desc = channel('info')[0].string
                if desc == None:
                    raise
            except:
                desc = ''

            try:
                #addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),3,thumbnail,fanArt,desc,genre,credits,date)
                addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),3,thumbnail,fanArt,desc)
            except:
                notify('[COLOR red]Erro ao Carregar os dados![/COLOR]')
        getItems(items,fanArt)
        #getItems(items)



def getItems(items, fanart):
    use_thumb = addon.getSetting('use_thumb')
    for item in items:
        try:
            name = item('title')[0].string.replace(";", "")
            if name is None:
                name = 'unknown?'
        except:
            name = ''

        try:
            thumbnail = item('thumbnail')[0].string
            if thumbnail == None:
                raise
        except:
            thumbnail = ''
        try:
            if not item('fanart'):
                if __addon__.getSetting('use_thumb') == "true":
                    fanArt = thumbnail
                else:
                    fanArt = fanart
            else:
                fanArt = item('fanart')[0].string
            if fanArt == None:
                raise
        except:
            fanArt = fanart

        try:
            desc = item('info')[0].string
            if desc == None:
                raise
        except:
            desc = ''


        try:
            if item('category'):
                category = item('category')[0].string
            else:
                category = ''
        except:
            category = ''


        try:
            if item('subtitle') and len(item('subtitle')) >0:
                subtitle = item('subtitle')[0].string
                subtitle2  = item('subtitle')
            else:
                subtitle = ''
                subtitle2 = ''
        except:
            subtitle = ''
            subtitle2 = ''

        try:
            if item('utube') and len(item('utube')) >0:
                utube = item('utube')[0].string
            else:
                utube = ''
        except:
            utube = ''
            
        try:
            if item('tmdb') and len(item('tmdb')) >0 and item('imdb') and len(item('imdb')) >0:
                #name2 = item('title')[0].string.replace(";", "")
                tmdb_id = item('tmdb')[0].string
                imdb_id = item('imdb')[0].string
                title, desc, thumbnail = tmdb_info(tmdb_id)
                name = '[B][COLOR white]'+title+'[/COLOR] [COLOR yellow](imdb '+imdb_info(imdb_id)+')[/COLOR][/B]'
        except:
            try:
                name = item('title')[0].string.replace(";", "")
                if name is None:
                    name = 'unknown?'
            except:
                name = ''
            try:
                desc = item('info')[0].string
                if desc == None:
                    raise
            except:
                desc = ''
            try:
                thumbnail = item('thumbnail')[0].string
                if thumbnail == None:
                    raise
            except:
                thumbnail = ''


        try:
            if len(item('jsonrpc')) >0:
                url = item('jsonrpc')[0].string
            elif len(item('externallink')) >0:
                url = item('externallink')[0].string
            elif len(item('link')) >0:
                try:
                    url = item('link')[0].string
                    url2 = item('link')
                except:
                    url = item('link')[0].string
                    url2 = ''
            else:
                url = ''
                url2 = ''
        except:
            url = ''
            url2 = ''

        try:
            if category == 'Adult' and url.find('redecanais') >= 0 and url.find('m3u8') >= 0:
                addDir2(name.encode('utf-8', 'ignore'),url.encode('utf-8'),10,subtitle,'',thumbnail,fanArt,desc.encode('utf-8'),False)
            elif url.find('redecanais') >= 0 and url.find('m3u8') >= 0:
                addDir2(name.encode('utf-8', 'ignore'),url.encode('utf-8'),16,subtitle,'',thumbnail,fanArt,desc.encode('utf-8'),False)        
            elif resolver(url, name, thumbnail).startswith('plugin://plugin.video.youtube/playlist') == True or resolver(url, name, thumbnail).startswith('plugin://plugin.video.youtube/channel') == True or resolver(url, name, thumbnail).startswith('plugin://plugin.video.youtube/user') == True or resolver(url, name, thumbnail).startswith('Plugin://plugin.video.youtube/playlist') == True:
                addDir(name.encode('utf-8', 'ignore'),resolver(url, name, thumbnail).encode('utf-8'),6,thumbnail,fanArt,desc)
            elif utube > '' and len(utube) == 11:
                link_youtube = 'plugin://plugin.video.youtube/play/?video_id='+utube
                #addLink(name.encode('utf-8', 'ignore'), link_youtube.encode('utf-8'), subtitle, cleaname, thumbnail, fanArt, desc)
                addLink(name.encode('utf-8', 'ignore'), link_youtube.encode('utf-8'), subtitle, '', thumbnail, fanArt, desc)
            elif len(item('externallink')) >0:
                addDir(name.encode('utf-8', 'ignore'),resolver(url, name, thumbnail).encode('utf-8'),1,thumbnail,fanArt,desc)
            #elif len(url2) >1 and cleaname == '' and len(subtitle2) >1 and re.search(playlist_command,url,re.IGNORECASE):
            elif len(url2) >1 and len(subtitle2) >1 and re.search(playlist_command,url,re.IGNORECASE):
                #addDir2(name.encode('utf-8', 'ignore')+'[COLOR aquamarine] ('+str(len(url2))+' itens)[/COLOR]'.encode('utf-8', 'ignore'),str(url2).replace(',','||').replace('$'+playlist_command+'','#'+playlist_command+''),11,str(subtitle2).replace(',','||'),cleaname,thumbnail,fanArt,desc.encode('utf-8'),False)
                addDir2(name.encode('utf-8', 'ignore')+'[COLOR red] ('+str(len(url2))+' itens)[/COLOR]'.encode('utf-8', 'ignore'),str(url2).replace(',','||').replace('$'+playlist_command+'','#'+playlist_command+''),11,str(subtitle2).replace(',','||'),'',thumbnail,fanArt,desc.encode('utf-8'),False)
            #elif len(url2) >1 and cleaname == '' and re.search(playlist_command,url,re.IGNORECASE):
            elif len(url2) >1 and re.search(playlist_command,url,re.IGNORECASE):
                #addDir2(name.encode('utf-8', 'ignore')+'[COLOR aquamarine] ('+str(len(url2))+' itens)[/COLOR]'.encode('utf-8', 'ignore'),str(url2).replace(',','||').replace('$'+playlist_command+'','#'+playlist_command+''),11,subtitle,cleaname,thumbnail,fanArt,desc.encode('utf-8'),False)
                addDir2(name.encode('utf-8', 'ignore')+'[COLOR red] ('+str(len(url2))+' itens)[/COLOR]'.encode('utf-8', 'ignore'),str(url2).replace(',','||').replace('$'+playlist_command+'','#'+playlist_command+''),11,subtitle,'',thumbnail,fanArt,desc.encode('utf-8'),False)
            #elif cleaname > '' and category == 'Adult':
            elif category == 'Adult':
                #addDir2(name.encode('utf-8', 'ignore'),resolver(url, cleaname, thumbnail).encode('utf-8'),10,subtitle,cleaname,thumbnail,fanArt,desc.encode('utf-8'),False)
                addDir2(name.encode('utf-8', 'ignore'),resolver(url, cleaname, thumbnail).encode('utf-8'),10,subtitle,'',thumbnail,fanArt,desc.encode('utf-8'),False)
            else:
                addLink(name.encode('utf-8', 'ignore'), resolver(url, name, thumbnail).encode('utf-8'), subtitle, '', thumbnail, fanArt, desc)
            #elif cleaname > '':
            #    addLink(name.encode('utf-8', 'ignore'), resolver(url, cleaname, thumbnail).encode('utf-8'), subtitle, cleaname, thumbnail, fanArt, desc)

        except:
            notify('[COLOR red]Erro ao Carregar os items![/COLOR]')



def getSubChannelItems(name,url,fanart):
    data = resolve_data(url)
    soup = BeautifulSOAP(data, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
    channel_list = soup.find('subchannel', attrs={'name' : name.decode('utf-8')})
    items = channel_list('subitem')
    getItems(items,fanart)



def adult(name, url, cleaname, iconimage, description, subtitle):
    Path = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile')).decode("utf-8")
    arquivo = os.path.join(Path, "password.txt")
    exists = os.path.isfile(arquivo)
    keyboard = xbmcaddon.Addon().getSetting("keyboard")
    if exists == False:
        parental_password()
        xbmc.sleep(10)
        p_file = open(arquivo,'r+')
        p_file_read = p_file.read()
        p_file_b64_decode = base64.b64decode(p_file_read).decode('utf-8')
        dialog = xbmcgui.Dialog()
        if int(keyboard) == 0:
            ps = dialog.numeric(0, 'Insira a senha atual:')
        else:
            ps = dialog.input('Insira a senha atual:', option=xbmcgui.ALPHANUM_HIDE_INPUT)
        if ps == p_file_b64_decode:
            if url.startswith("plugin://plugin.video.f4mTester"):
                xbmc.executebuiltin('RunPlugin(' + url + ')')
            elif url.startswith('plugin://plugin.video.youtube/playlist') == True or url.startswith('plugin://plugin.video.youtube/channel') == True or url.startswith('plugin://plugin.video.youtube/user') == True or url.startswith('Plugin://plugin.video.youtube/playlist') == True:
                xbmc.executebuiltin("ActivateWindow(10025," + url + ",return)")
            else:
                li = xbmcgui.ListItem(name, path=url, iconImage=iconimage, thumbnailImage=iconimage)
                if cleaname > '':
                    li.setInfo(type='video', infoLabels={'Title': cleaname, 'plot': description })
                else:
                    li.setInfo(type='video', infoLabels={'Title': name, 'plot': description })
                if subtitle > '':
                    li.setSubtitles([subtitle])
                xbmc.Player().play(item=url, listitem=li)
        else:
            xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','Senha invalida!, se não alterou utilize a senha padrão')
    else:
        p_file = open(arquivo,'r+')
        p_file_read = p_file.read()
        p_file_b64_decode = base64.b64decode(p_file_read).decode('utf-8')
        dialog = xbmcgui.Dialog()
        if int(keyboard) == 0:
            ps = dialog.numeric(0, 'Insira a senha atual:')
        else:
            ps = dialog.input('Insira a senha atual:', option=xbmcgui.ALPHANUM_HIDE_INPUT)
        if ps == p_file_b64_decode:
            if url.startswith("plugin://plugin.video.f4mTester"):
                xbmc.executebuiltin('RunPlugin(' + url + ')')
            elif url.startswith('plugin://plugin.video.youtube/playlist') == True or url.startswith('plugin://plugin.video.youtube/channel') == True or url.startswith('plugin://plugin.video.youtube/user') == True or url.startswith('Plugin://plugin.video.youtube/playlist') == True:
                xbmc.executebuiltin("ActivateWindow(10025," + url + ",return)")
            else:
                li = xbmcgui.ListItem(name, path=url, iconImage=iconimage, thumbnailImage=iconimage)
                if cleaname > '':
                    li.setInfo(type='video', infoLabels={'Title': cleaname, 'plot': description })
                else:
                    li.setInfo(type='video', infoLabels={'Title': name, 'plot': description })
                if subtitle > '':
                    li.setSubtitles([subtitle])
                xbmc.Player().play(item=url, listitem=li)
        else:
            xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','Senha invalida!, se não alterou utilize a senha padrão')



def playlist(name, url, cleaname, iconimage, description, subtitle):
    playlist_command1 = playlist_command
    dialog = xbmcgui.Dialog()
    links = re.compile('<link>([\s\S]*?)#'+playlist_command1+'', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(url)
    names = re.compile('#'+playlist_command1+'=([\s\S]*?)</link>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(url)
    subtitles = re.compile('<subtitle>([\s\S]*?)</subtitle>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(subtitle)
    if links !=[] and names !=[]:
        index = dialog.select(dialog_playlist, names)
        if index >= 0:
            playname=names[index]
            if playname > '':
                playname1 = playname
            else:
                playname1 = 'Desconhecido'
            playlink=links[index]
            if subtitles !=[]:
                playsub=subtitles[index]
            else:
                playsub = ''
            urlresolver = resolver(playlink, playname1, iconimage)
            if urlresolver.startswith("plugin://plugin.video.f4mTester"):
                xbmc.executebuiltin('RunPlugin(' + urlresolver + ')')
            elif urlresolver.startswith('plugin://plugin.video.youtube/playlist') == True or urlresolver.startswith('plugin://plugin.video.youtube/channel') == True or urlresolver.startswith('plugin://plugin.video.youtube/user') == True or urlresolver.startswith('Plugin://plugin.video.youtube/playlist') == True:
                xbmc.executebuiltin("ActivateWindow(10025," + urlresolver + ",return)")
            else:
                li = xbmcgui.ListItem(playname1, path=urlresolver, iconImage=iconimage, thumbnailImage=iconimage)
                if cleaname > '':
                    li.setInfo(type='video', infoLabels={'Title': cleaname, 'plot': description })
                else:
                    li.setInfo(type='video', infoLabels={'Title': playname1, 'plot': description })
                if subtitle > '':
                    li.setSubtitles([playsub])
                xbmc.Player().play(item=urlresolver, listitem=li)


def individual_player(name, url, cleaname, iconimage, description, subtitle):
    if cleaname > '':
        urlresolver = resolver(url, cleaname, iconimage)
    else:
        urlresolver = resolver(url, name, iconimage)
    if urlresolver.startswith("plugin://plugin.video.f4mTester"):
        xbmc.executebuiltin('RunPlugin(' + urlresolver + ')')
    else:
        li = xbmcgui.ListItem(name, path=urlresolver, iconImage=iconimage, thumbnailImage=iconimage)
        if cleaname > '':
            li.setInfo(type='video', infoLabels={'Title': cleaname, 'plot': description })
        else:
            li.setInfo(type='video', infoLabels={'Title': name, 'plot': description })
        if subtitle > '':
            li.setSubtitles([subtitle])
        xbmc.Player().play(item=urlresolver, listitem=li)


def m3u8_player(name, url, cleaname, iconimage, description, subtitle):
    if url.startswith("plugin://plugin.video.f4mTester"):
        xbmc.executebuiltin('RunPlugin(' + url + ')')
    else:
        li = xbmcgui.ListItem(name, path=url, iconImage=iconimage, thumbnailImage=iconimage)
        if cleaname > '':
            li.setInfo(type='video', infoLabels={'Title': cleaname, 'plot': description })
        else:
            li.setInfo(type='video', infoLabels={'Title': name, 'plot': description })
        if subtitle > '':
            li.setSubtitles([subtitle])
        xbmc.Player().play(item=url, listitem=li)



#NETCINE
def netcine_resolver(url):
    link_decoded = url
    if not link_decoded.startswith("plugin://plugin") and link_decoded.startswith('https://netcine.info/') == True:
        try:
            try:
                import urllib.request as urllib2
            except ImportError:
                import urllib2
            request_headers = {
            "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,ru;q=0.7,de-DE;q=0.6,de;q=0.5,de-AT;q=0.4,de-CH;q=0.3,ja;q=0.2,zh-CN;q=0.1,zh;q=0.1,zh-TW;q=0.1,es;q=0.1,ar;q=0.1,en-GB;q=0.1,hi;q=0.1,cs;q=0.1,el;q=0.1,he;q=0.1,en-US;q=0.1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
            }
            url2 = 'https://netcine.info/'
            request = urllib2.Request(url2, headers=request_headers)
            response = urllib2.urlopen(request)
            result_host = response.geturl()
            #return response
        except:
            result_host = 'https://netcine.info/'
        host_final = result_host.replace('tvshows/', '').replace('?filmes/', '').replace('?filmes', '')
        referer = host_final.replace('https://', 'https://p.')
        link_atualizado = link_decoded.replace('https://netcine.info/', host_final)
        #print(link_atualizado)
        procurar_idioma = re.compile('.+?idioma=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_atualizado)
        #print(find_idioma[0])
        if procurar_idioma[0] == 'legendado':
            #print(procurar_idioma[0])
            link_normal = link_atualizado.replace('$idioma=legendado','')
            #print(link_normal)
            data = getRequest2(link_normal, host_final)
            #print(data)
            #result1 = re.compile('<p><iframe src="(.+?)".+?</p>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
            result1 = re.compile('<iframe src="(.+?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
            #print(result1)
            for link in result1:
                if link.find('leg') >= 0:
                    #print(link)
                    data2 = getRequest2(link, referer)
                    #print(data2)
                    result2 = re.compile('<iframe src="(.+?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data2)
                    #print(result2)
                    link2 = result2[0]
                    data3 = getRequest2(link2, referer)
                    #print(data3)
                    #print('Teste\n'+data3+'\n#########')
                    result3 = re.compile('<a href ="(.+?)".+?target="_blank"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data3)
                    #print(result3[1])
                    link3 = result3[1]
                    #print(link3)
                    #link4 = link3.replace('https://p.netcine.info/redirecionar.php?data=','')
                    result_redirect = re.compile('.+?data=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link3)
                    link4 = result_redirect[0]
                    #print(link4)
                    data4 = getRequest2(link4, referer)
                    #print(data4)
                    result4 = re.compile("location.href='(.+?)'", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data4)
                    #print(result4[2])
                    #print(result4)
                    if result4 !=[]:
                        for player in result4:
                            if player.find('desktop') >= 0:
                                #print(result4[2])
                                link5 = player
                                data5 = getRequest2(link5, referer)
                                #print(data5)
                                link6 = re.compile("file':'(.+?)'", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data5)
                                for video_url in link6:
                                    if video_url.find('-ALTO') >= 0:
                                        #print(video_url)
                                        #resolved = video_url+'|Referer='+getlink2
                                        resolved = video_url
                                        #print(resolved)
                                        return resolved
                                    else:
                                        resolved = ''
                            else:
                                resolved = ''
                    else:
                        link6 = re.compile("file':'(.+?)'", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data4)
                        for video_url in link6:
                            if video_url.find('-ALTO') >= 0:
                                #print(video_url)
                                #resolved = video_url+'|Referer='+getlink2
                                resolved = video_url
                                #print(resolved)
                                return resolved
                            else:
                                resolved = ''

                #elif link.find('LEG') >= 0 or link.find('nv32.php') >= 0 and link.find('filmes') >= 0:
                elif link.find('filmes') >= 0 and link.find('LEG') >=0:
                    #print(link)
                    data2 = getRequest2(link, referer)
                    #print(data2)
                    result2 = re.compile('<iframe src="(.+?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data2)
                    #print(result2)
                    link2 = result2[0]
                    data3 = getRequest2(link2, referer)
                    #print(data3)
                    #print('Teste\n'+data3+'\n#########')
                    result3 = re.compile('<a href ="(.+?)".+?target="_blank"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data3)
                    #print(result3[1])
                    link3 = result3[1]
                    #print(link3)
                    #link4 = link3.replace('https://p.netcine.info/redirecionar.php?data=','')
                    result_redirect = re.compile('.+?data=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link3)
                    link4 = result_redirect[0]
                    #print(link4)
                    data4 = getRequest2(link4, referer)
                    #print(data4)
                    result4 = re.compile("location.href='(.+?)'", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data4)
                    #print(result4[2])
                    if result4 !=[]:
                        for player in result4:
                            if player.find('desktop') >= 0:
                                #print(result4[2])
                                link5 = player
                                data5 = getRequest2(link5, referer)
                                #print(data5)
                                link6 = re.compile("file':'(.+?)'", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data5)
                                for video_url in link6:
                                    if video_url.find('-ALTO') >= 0:
                                        #print(video_url)
                                        #resolved = video_url+'|Referer='+getlink2
                                        resolved = video_url
                                        #print(resolved)
                                        return resolved
                                    else:
                                        resolved = ''
                            else:
                                resolved = ''
                    else:
                        link6 = re.compile("file':'(.+?)'", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data4)
                        for video_url in link6:
                            if video_url.find('-ALTO') >= 0:
                                #print(video_url)
                                #resolved = video_url+'|Referer='+getlink2
                                resolved = video_url
                                #print(resolved)
                                return resolved
                            else:
                                resolved = ''
                else:
                    resolved = ''
        elif procurar_idioma[0] == 'dublado':
            #print(procurar_idioma[0])
            link_normal = link_atualizado.replace('$idioma=dublado','')
            #print(link_normal)
            data = getRequest2(link_normal, host_final)
            #print(data)
            #result1 = re.compile('<p><iframe src="(.+?)".+?</p>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
            result1 = re.compile('<iframe src="(.+?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
            #print(result1)
            for link in result1:
                if link.find('dub') >= 0:
                    #print(link)
                    data2 = getRequest2(link, referer)
                    #print(data2)
                    result2 = re.compile('<iframe src="(.+?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data2)
                    #print(result2)
                    link2 = result2[0]
                    data3 = getRequest2(link2, referer)
                    #print(data3)
                    #print('Teste\n'+data3+'\n#########')
                    result3 = re.compile('<a href ="(.+?)".+?target="_blank"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data3)
                    #print(result3[1])
                    link3 = result3[1]
                    #print(link3)
                    #link4 = link3.replace('https://p.netcine.info/redirecionar.php?data=','')
                    result_redirect = re.compile('.+?data=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link3)
                    link4 = result_redirect[0]
                    #print(link4)
                    data4 = getRequest2(link4, referer)
                    #print(data4)
                    result4 = re.compile("location.href='(.+?)'", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data4)
                    #print(result4[2])
                    if result4 !=[]:
                        for player in result4:
                            if player.find('desktop') >= 0:
                                #print(result4[2])
                                link5 = player
                                data5 = getRequest2(link5, referer)
                                #print(data5)
                                link6 = re.compile("file':'(.+?)'", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data5)
                                for video_url in link6:
                                    if video_url.find('-ALTO') >= 0:
                                        #print(video_url)
                                        #resolved = video_url+'|Referer='+getlink2
                                        resolved = video_url
                                        #print(resolved)
                                        return resolved
                                    else:
                                        resolved = ''
                            else:
                                resolved = ''
                    else:
                        link6 = re.compile("file':'(.+?)'", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data4)
                        for video_url in link6:
                            if video_url.find('-ALTO') >= 0:
                                #print(video_url)
                                #resolved = video_url+'|Referer='+getlink2
                                resolved = video_url
                                #print(resolved)
                                return resolved
                            else:
                                resolved = ''
                #elif link.find('nv26.php') >= 0 or link.find('DUB') >=0 and link.find('filmes') >= 0:
                elif link.find('filmes') >= 0 and link.find('DUB') >=0:
                    #print(link)
                    data2 = getRequest2(link, referer)
                    #print(data2)
                    result2 = re.compile('<iframe src="(.+?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data2)
                    #print(result2)
                    link2 = result2[0]
                    data3 = getRequest2(link2, referer)
                    #print(data3)
                    #print('Teste\n'+data3+'\n#########')
                    result3 = re.compile('<a href ="(.+?)".+?target="_blank"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data3)
                    #print(result3[1])
                    link3 = result3[1]
                    #print(link3)
                    #link4 = link3.replace('https://p.netcine.info/redirecionar.php?data=','')
                    result_redirect = re.compile('.+?data=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link3)
                    link4 = result_redirect[0]
                    #print(link4)
                    data4 = getRequest2(link4, referer)
                    #print(data4)
                    result4 = re.compile("location.href='(.+?)'", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data4)
                    #print(result4[2])
                    if result4 !=[]:
                        for player in result4:
                            if player.find('desktop') >= 0:
                                #print(result4[2])
                                link5 = player
                                data5 = getRequest2(link5, referer)
                                #print(data5)
                                link6 = re.compile("file':'(.+?)'", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data5)
                                for video_url in link6:
                                    if video_url.find('-ALTO') >= 0:
                                        #print(video_url)
                                        #resolved = video_url+'|Referer='+getlink2
                                        resolved = video_url
                                        #print(resolved)
                                        return resolved
                                    else:
                                        resolved = ''
                            else:
                                resolved = ''
                    else:
                        link6 = re.compile("file':'(.+?)'", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data4)
                        for video_url in link6:
                            if video_url.find('-ALTO') >= 0:
                                #print(video_url)
                                #resolved = video_url+'|Referer='+getlink2
                                resolved = video_url
                                #print(resolved)
                                return resolved
                            else:
                                resolved = ''
                else:
                    resolved = ''

        else:
            resolved = ''



def ascii(string):
    if isinstance(string, basestring):
        if isinstance(string, unicode):
           string = string.encode('ascii', 'ignore')
    return string
def uni(string, encoding = 'utf-8'):
    if isinstance(string, basestring):
        if not isinstance(string, unicode):
            string = unicode(string, encoding, 'ignore')
    return string
def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))

def sendJSON(command):
    data = ''
    try:
        data = xbmc.executeJSONRPC(uni(command))
    except UnicodeEncodeError:
        data = xbmc.executeJSONRPC(ascii(command))

    return uni(data)


def tmdb_info(id):
    data = getRequest('https://www.themoviedb.org/movie/'+id+'?language=pt-BR', '')
    info_RE = re.compile('<section.+?class="header.+?poster">.+?div.+?class="title.+?a.+?href.+?>(.+?)</a>.+?<span.+?class="tag.+?release_date">(.+?)</span>.+?<span.+?class="release">(.+?)</span>.+?<span.+?<span.+?class="runtime">(.+?)</span>.+?<div.+?class="header_info">.+?<p>(.+?)</p>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
    thumb_RE = re.compile('<div.+?class="image_content.+?backdrop">.+?srcset.+?1x,(.+?)2x', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
    if thumb_RE !=[]:
        thumb  = str(thumb_RE[0]).replace(' ', '')
    if info_RE !=[] and thumb_RE !=[]:
        for name, year, release, runtime, sinopse in info_RE:
            title = name+' '+year
            desc = sinopse+'\n[Lançamento]'+release.replace('\n\n', '').replace('  ', '')+'\n[Duração]\n'+runtime.replace('\n', '').replace('  ', '')
            return title, desc, thumb
        
        
def imdb_info(id):
    data = getRequest(''+id, '')
    info_RE = re.compile('<span.+?itemprop="ratingValue">(.+?)</span>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
    title = info_RE[0]
    return title


def pluginquerybyJSON(url):
    json_query = uni('{"jsonrpc":"2.0","method":"Files.GetDirectory","params":{"directory":"%s","media":"video","properties":["thumbnail","title","year","dateadded","fanart","rating","season","episode","studio"]},"id":1}') %url

    json_folder_detail = json.loads(sendJSON(json_query))
    for i in json_folder_detail['result']['files'] :
        url = i['file']
        name = removeNonAscii(i['label'])
        thumbnail = removeNonAscii(i['thumbnail'])
        try:
            fanart = removeNonAscii(i['fanart'])
        except Exception:
            fanart = ''
        try:
            date = i['year']
        except Exception:
            date = ''
        try:
            episode = i['episode']
            season = i['season']
            if episode == -1 or season == -1:
                description = ''
            else:
                description = '[COLOR yellow] S' + str(season)+'[/COLOR][COLOR hotpink] E' + str(episode) +'[/COLOR]'
        except Exception:
            description = ''
        try:
            studio = i['studio']
            if studio:
                description += '\n Studio:[COLOR steelblue] ' + studio[0] + '[/COLOR]'
        except Exception:
            studio = ''
        
        desc = description+'\n\nDate: '+str(date)

        if i['filetype'] == 'file':
            #addLink(url,name,thumbnail,fanart,description,'',date,'',None,'',total=len(json_folder_detail['result']['files']))
            addLink(name.encode('utf-8', 'ignore'),url.encode('utf-8'),'','',thumbnail,fanart,desc)
            #xbmc.executebuiltin("Container.SetViewMode(500)")

        else:
            #addDir(name,url,53,thumbnail,fanart,description,'',date,'')
            addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),6,iconimage,fanart,desc)
            #xbmc.executebuiltin("Container.SetViewMode(500)")



def youtube(url):
    plugin_url = url
    xbmc.executebuiltin("ActivateWindow(10025," + plugin_url + ",return)")



def youtube_resolver(url):
    link_youtube = url
    if link_youtube.startswith('https://www.youtube.com/watch?v') == True or link_youtube.startswith('https://youtube.com/watch?v') == True:
        get_id1 = re.compile('v=(.+?)&', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        get_id2 = re.compile('v=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        if get_id1 !=[]:
            #print('tem')
            id_video = get_id1[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/play/?video_id='+id_video
        elif get_id2 !=[]:
            #print('tem2')
            id_video = get_id2[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/play/?video_id='+id_video
        else:
            resolve = ''
    elif link_youtube.startswith('https://www.youtube.com/playlist?') == True or link_youtube.startswith('https://youtube.com/playlist?') == True:
        get_id1 = re.compile('list=(.+?)&', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        get_id2 = re.compile('list=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        if get_id1 !=[]:
            #print('tem')
            id_video = get_id1[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/playlist/'+id_video+'/?page=0'
        elif get_id2 !=[]:
            #print('tem2')
            id_video = get_id2[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/playlist/'+id_video+'/?page=0'
        else:
            resolve = ''
    elif link_youtube.startswith('https://www.youtube.com/channel') == True or link_youtube.startswith('https://youtube.com/channel') == True:
        get_id1 = re.compile('channel/(.+?)&', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        get_id2 = re.compile('channel/(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        if get_id1 !=[]:
            #print('tem')
            id_video = get_id1[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/channel/'+id_video+'/'
        elif get_id2 !=[]:
            #print('tem2')
            id_video = get_id2[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/channel/'+id_video+'/'
        else:
            resolve = ''
    elif link_youtube.startswith('https://www.youtube.com/user') == True or link_youtube.startswith('https://youtube.com/user') == True:
        get_id1 = re.compile('user/(.+?)&', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        get_id2 = re.compile('user/(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        if get_id1 !=[]:
            #print('tem')
            id_video = get_id1[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/user/'+id_video+'/'
        elif get_id2 !=[]:
            #print('tem2')
            id_video = get_id2[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/user/'+id_video+'/'
        else:
            resolve = ''

    else:
        resolve = ''
    return resolve


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def getInfoPlaylistYoutube(url):
    try:
        import requests
        sourceCode = requests.get(url).text
    except:
        sourceCode = ''
    soup = BeautifulSoup(sourceCode, 'html.parser')
    #print(soup)
    info_web = str(soup.find(id="eow-description")).replace("<br/>", "\n")
    info = cleanhtml(info_web)
    return info  


def youtube_restore(url):
    if url.find('/?video_id=') >= 0:
        find_id = re.compile('/?video_id=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(url)
        normal_url = 'https://www.youtube.com/watch?v='+str(find_id[0])
    elif url.find('youtube/playlist/') >= 0:
        find_id = re.compile('/playlist/(.+?)/', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(url)
        normal_url = 'https://www.youtube.com/playlist?list='+str(find_id[0])
    else:
        normal_url = ''
    return normal_url


def getPlaylistLinksYoutube(url):
    try:
        import requests
        sourceCode = requests.get(youtube_restore(url)).text
    except:
        sourceCode = ''
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com'
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')
        if href.startswith('/watch?'):
            name = str(link.string.strip())
            #video_url = re.compile('(.+?)&', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(str(href))
            video_id = re.compile('v=(.+?)&', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(str(href))
            #url = str(domain + video_url[0])
            thumbnail = "https://img.youtube.com/vi/%s/0.jpg" % video_id[0]
            fanart = "https://i.ytimg.com/vi/%s/hqdefault.jpg" % video_id[0]
            plugin_url = 'plugin://plugin.video.youtube/play/?video_id='+video_id[0]
            urlfinal = str(plugin_url)
            #description = getInfoPlaylistYoutube(url)
            description = ''
            addLink(name.encode('utf-8', 'ignore'),urlfinal.encode('utf-8'),'','',str(thumbnail),str(fanart),description)



def rc_pro3(channel):
    try:
        canal = str(re.compile('redecanais_m3u8=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(channel)[0]).replace('.m3u8','')
        regex = getRequest2('https://dl.dropboxusercontent.com/s/kr2iv34q826s5es/rc_pro.txt','').replace('\n','').replace('\r','')
        match_data = re.compile('player="(.+?)".+?eferer="(.+?)".+?eferer_canal="(.+?)".+?pt_player="(.+?)".+?pt_referer_canal="(.+?)".+?odo_opt="(.+?)"').findall(regex)
        player = match_data[0][0].replace('\n','').replace('\r','')
        referer = match_data[0][1].replace('\n','').replace('\r','')
        referer_canal = match_data[0][2].replace('\n','').replace('\r','')
        opt_player = match_data[0][3].replace('\n','').replace('\r','')
        opt_referer_canal = match_data[0][4].replace('\n','').replace('\r','')
        modo_opt = match_data[0][5].replace('\n','').replace('\r','')
        if str(modo_opt) == 'false':
            data = getRequest2(str(player)+canal, str(referer)+canal)
            referer_m3u8 = str(referer_canal)+canal
        else:
            data = getRequest2(str(player)+canal+str(opt_player), str(referer)+canal)
            referer_m3u8 = str(referer_canal)+canal+str(opt_referer_canal)
        source = re.compile('source.+?"(.+?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)[0].replace('\n','').replace('\r','')
        servidor_rc = source
        referer_rc = urllib.quote_plus(referer_m3u8)
        return servidor_rc, referer_rc 
    except:
        servidor_rc = ''
        referer_rc = ''
        return servidor_rc, referer_rc



def resolver(link, name, thumbnail):
    link_decoded = link
    try:
        f4m = __addon__.getSetting('f4m')
        if not link_decoded.startswith("plugin://plugin") and link_decoded.startswith('https://drive.google.com') == True:
            #print('verdadeiro')
            resolved = link_decoded.replace('http','plugin://plugin.video.gdrive?mode=streamURL&amp;url=http')
            #print(resolved)
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.startswith('http://drive.google.com') == True:
            #print('verdadeiro')
            resolved = link_decoded.replace('http','plugin://plugin.video.gdrive?mode=streamURL&amp;url=http')
            #print(resolved)
        #Rede Canais
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('redecanais') >= 0 and link_decoded.find('m3u8') >= 0:
            try:
                servidor_rc, referer_rc = rc_pro3(link_decoded)
                if servidor_rc > '' and referer_rc > '':
                    link_final2 = servidor_rc+'|Referer='+referer_rc+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
                    #print(link_final2)
                else:
                    link_final2 = ''
                    #print(link_final2)
            except:
                link_final2 = ''
            if int(f4m) == 0:
                #print('f4m ativado')
                try:
                    clear3 = re.compile("Referer(.*)", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_final2)
                    clear4 = re.compile("User-Agent(.*)", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_final2)
                    if clear3 !=[] and clear4 !=[]:
                        link_clear2 = link_final2.replace(clear3[0],'').replace(clear4[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                    elif clear3 !=[]:
                        link_clear2 = link_final2.replace(clear3[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                    elif clear4 !=[]:
                        link_clear2 = link_final2.replace(clear4[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                    else:
                        link_clear2 = link_final2
                        #print(link_clear)
                    get_referer = re.compile("Referer=(.*).+?User-Agent", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_final2)
                    get_referer2 = re.compile('Referer=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_final2)
                    get_user = re.compile('User-Agent=(.*).+?Referer', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_final2)
                    get_user2 = re.compile('User-Agent=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_final2)
                    if get_referer !=[]:
                        ref = get_referer[0]
                        referer = 'Referer='+ref+''
                    elif get_referer2 !=[]:
                        ref = get_referer2[0]
                        referer = 'Referer='+ref+''
                    else:
                        referer = ''
                    if get_user !=[]:
                        user = get_user[0]
                        user_agent = 'User-Agent='+user+''
                    elif get_user2 !=[]:
                        user = get_user2[0]
                        user_agent = 'User-Agent='+user+''
                    else:
                        user_agent = ''
                    if referer > '' and user_agent > '':
                        result = '|'+referer+'|'+user_agent
                    elif referer > '':
                        result = '|'+referer
                    elif user_agent > '':
                        result = '|'+user_agent
                    else:
                        result = ''
                    name2 = name.replace('&','e').replace('BR | ','').replace('BR : ','').replace('BR: ','').replace('BR| ','').replace('|','')
                    url_quote = urllib.quote_plus(link_clear2)
                    resolved1 = url_quote.replace('http','plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name='+urllib.quote_plus(str(name2))+'&amp;iconImage='+urllib.quote_plus(thumbnail)+'&amp;thumbnailImage='+urllib.quote_plus(thumbnail)+'&amp;url=http')
                    resolved = resolved1+urllib.quote_plus(result)
                    #print(resolved)
                except:
                    resolved = link_final2
            else:
                resolved = link_final2
                #print(resolved)
        #netcine.info
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.startswith('https://netcine.info/') == True:
            try:
                resultado = netcine_resolver(link_decoded)
                if resultado==None:
                    #print('vazio')
                    resolved = ''
                else:
                    resolved = resultado
            except:
                resolved = ''
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.startswith('https://youtube.com/') == True or link_decoded.startswith('https://www.youtube.com/') == True:
            try:
                resultado = youtube_resolver(link_decoded)
                if resultado==None:
                    #print('vazio')
                    resolved = ''
                else:
                    resolved = resultado
            except:
                resolved = ''
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.startswith('https://photos.app') == True:
            try:
                data = getRequest2(link_decoded, 'https://photos.google.com/')
                result = re.compile('<meta property="og:video" content="(.+?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
                if result !=[]:
                    resolved = result[0].replace('-m18','-m22')
                else:
                    resolved = ''
            except:
                resolved = ''
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.startswith('magnet:?xt=') == True:
            resolved = 'plugin://plugin.video.elementum/play?uri='+link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.torrent') >= 0:
            resolved = 'plugin://plugin.video.elementum/play?uri='+link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.mp4') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.mkv') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.wmv') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.wma') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.avi') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.mp3') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.ac3') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.rmvb') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and not link_decoded.find('live.cinexplay.com') >= 0 and link_decoded.find('.m3u8') >= 0:
            if int(f4m) == 0:
                clear1 = re.compile("Referer(.*)", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                clear2 = re.compile("User-Agent(.*)", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                if clear1 !=[] and clear2 !=[]:
                    link_clear = link_decoded.replace(clear1[0],'').replace(clear2[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                elif clear1 !=[]:
                    link_clear = link_decoded.replace(clear1[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                elif clear2 !=[]:
                    link_clear = link_decoded.replace(clear2[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                else:
                    link_clear = link_decoded
                #print(link_clear)
                get_referer = re.compile("Referer=(.*).+?User-Agent", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_referer2 = re.compile('Referer=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_user = re.compile('User-Agent=(.*).+?Referer', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_user2 = re.compile('User-Agent=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                if get_referer !=[]:
                    ref = get_referer[0]
                    referer = 'Referer='+ref+''
                elif get_referer2 !=[]:
                    ref = get_referer2[0]
                    referer = 'Referer='+ref+''
                else:
                    referer = ''
                if get_user !=[]:
                    user = get_user[0]
                    user_agent = 'User-Agent='+user+''
                elif get_user2 !=[]:
                    user = get_user2[0]
                    user_agent = 'User-Agent='+user+''
                else:
                    user_agent = ''
                if referer > '' and user_agent > '':
                    result = '|'+referer+'|'+user_agent
                elif referer > '':
                    result = '|'+referer
                elif user_agent > '':
                    result = '|'+user_agent
                else:
                    result = ''
                name2 = name.replace('&','e').replace('BR | ','').replace('BR : ','').replace('BR: ','').replace('BR| ','').replace('|','')
                url_quote = urllib.quote_plus(link_clear)
                resolved1 = url_quote.replace('http','plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name='+urllib.quote_plus(str(name2))+'&amp;iconImage='+urllib.quote_plus(thumbnail)+'&amp;thumbnailImage='+urllib.quote_plus(thumbnail)+'&amp;url=http')
                resolved = resolved1+urllib.quote_plus(result)
            else:
                resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.ts') >= 0:
            if int(f4m) == 0:
                clear1 = re.compile("Referer(.*)", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                clear2 = re.compile("User-Agent(.*)", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                if clear1 !=[] and clear2 !=[]:
                    link_clear = link_decoded.replace(clear1[0],'').replace(clear2[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                elif clear1 !=[]:
                    link_clear = link_decoded.replace(clear1[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                elif clear2 !=[]:
                    link_clear = link_decoded.replace(clear2[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                else:
                    link_clear = link_decoded
                #print(link_clear)
                get_referer = re.compile("Referer=(.*).+?User-Agent", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_referer2 = re.compile('Referer=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_user = re.compile('User-Agent=(.*).+?Referer', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_user2 = re.compile('User-Agent=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                if get_referer !=[]:
                    ref = get_referer[0]
                    referer = 'Referer='+ref+''
                elif get_referer2 !=[]:
                    ref = get_referer2[0]
                    referer = 'Referer='+ref+''
                else:
                    referer = ''
                if get_user !=[]:
                    user = get_user[0]
                    user_agent = 'User-Agent='+user+''
                elif get_user2 !=[]:
                    user = get_user2[0]
                    user_agent = 'User-Agent='+user+''
                else:
                    user_agent = ''
                if referer > '' and user_agent > '':
                    result = '|'+referer+'|'+user_agent
                elif referer > '':
                    result = '|'+referer
                elif user_agent > '':
                    result = '|'+user_agent
                else:
                    result = ''
                name2 = name.replace('&','e').replace('BR | ','').replace('BR : ','').replace('BR: ','').replace('BR| ','').replace('|','')
                url_quote = urllib.quote_plus(link_clear)
                resolved1 = url_quote.replace('http','plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+urllib.quote_plus(str(name2))+'&amp;iconImage='+urllib.quote_plus(thumbnail)+'&amp;thumbnailImage='+urllib.quote_plus(thumbnail)+'&amp;url=http')
                resolved = resolved1+urllib.quote_plus(result)
            else:
                resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and not link_decoded.find('googlevideo.com') >= 0 and not link_decoded.find('blogspot.com') >= 0 and not link_decoded.find('googleusercontent.com') >= 0 and not link_decoded.find('p.netcine.info') >= 0 and not link_decoded.find('live.cinexplay.com') >= 0 and not link_decoded.find('youtube.com') >= 0 and int(link_decoded.count(":")) == 2 and int(link_decoded.count("/")) > 3:
            if int(f4m) == 0:
                clear1 = re.compile("Referer(.*)", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                clear2 = re.compile("User-Agent(.*)", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                if clear1 !=[] and clear2 !=[]:
                    link_clear = link_decoded.replace(clear1[0],'').replace(clear2[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                elif clear1 !=[]:
                    link_clear = link_decoded.replace(clear1[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                elif clear2 !=[]:
                    link_clear = link_decoded.replace(clear2[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                else:
                    link_clear = link_decoded
                #print(link_clear)
                get_referer = re.compile("Referer=(.*).+?User-Agent", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_referer2 = re.compile('Referer=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_user = re.compile('User-Agent=(.*).+?Referer', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_user2 = re.compile('User-Agent=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                if get_referer !=[]:
                    ref = get_referer[0]
                    referer = 'Referer='+ref+''
                elif get_referer2 !=[]:
                    ref = get_referer2[0]
                    referer = 'Referer='+ref+''
                else:
                    referer = ''
                if get_user !=[]:
                    user = get_user[0]
                    user_agent = 'User-Agent='+user+''
                elif get_user2 !=[]:
                    user = get_user2[0]
                    user_agent = 'User-Agent='+user+''
                else:
                    user_agent = ''
                if referer > '' and user_agent > '':
                    result = '|'+referer+'|'+user_agent
                elif referer > '':
                    result = '|'+referer
                elif user_agent > '':
                    result = '|'+user_agent
                else:
                    result = ''
                name2 = name.replace('&','e').replace('BR | ','').replace('BR : ','').replace('BR: ','').replace('BR| ','').replace('|','')
                url_quote = urllib.quote_plus(link_clear)
                resolved1 = url_quote.replace('http','plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+urllib.quote_plus(str(name2))+'&amp;iconImage='+urllib.quote_plus(thumbnail)+'&amp;thumbnailImage='+urllib.quote_plus(thumbnail)+'&amp;url=http')
                resolved = resolved1+urllib.quote_plus(result)
            else:
               resolved = link_decoded
        else:
            #print('falso')
            resolved = link_decoded
        return resolved
    except:
        resolved = ''
        return resolved
        #pass
        #notify('[COLOR red]Não foi possivel resolver um link![/COLOR]')


def resolver_vip(link, name, thumbnail):
    link_decoded = link
    try:
        f4mvip = __addon__.getSetting('f4mvip')
        if not link_decoded.startswith("plugin://plugin") and not link_decoded.find('live.cinexplay.com') >= 0 and link_decoded.find('.m3u8') >= 0:
            if int(f4mvip) == 0:
                clear1 = re.compile("Referer(.*)", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                clear2 = re.compile("User-Agent(.*)", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                if clear1 !=[] and clear2 !=[]:
                    link_clear = link_decoded.replace(clear1[0],'').replace(clear2[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                elif clear1 !=[]:
                    link_clear = link_decoded.replace(clear1[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                elif clear2 !=[]:
                    link_clear = link_decoded.replace(clear2[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                else:
                    link_clear = link_decoded
                #print(link_clear)
                get_referer = re.compile("Referer=(.*).+?User-Agent", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_referer2 = re.compile('Referer=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_user = re.compile('User-Agent=(.*).+?Referer', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_user2 = re.compile('User-Agent=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                if get_referer !=[]:
                    ref = get_referer[0]
                    referer = 'Referer='+ref+''
                elif get_referer2 !=[]:
                    ref = get_referer2[0]
                    referer = 'Referer='+ref+''
                else:
                    referer = ''
                if get_user !=[]:
                    user = get_user[0]
                    user_agent = 'User-Agent='+user+''
                elif get_user2 !=[]:
                    user = get_user2[0]
                    user_agent = 'User-Agent='+user+''
                else:
                    user_agent = ''
                if referer > '' and user_agent > '':
                    result = '|'+referer+'|'+user_agent
                elif referer > '':
                    result = '|'+referer
                elif user_agent > '':
                    result = '|'+user_agent
                else:
                    result = ''
                name2 = name.replace('&','e').replace('BR | ','').replace('BR : ','').replace('BR: ','').replace('BR| ','').replace('|','')
                url_quote = urllib.quote_plus(link_clear)
                resolved1 = url_quote.replace('http','plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name='+urllib.quote_plus(str(name2))+'&amp;iconImage='+urllib.quote_plus(thumbnail)+'&amp;thumbnailImage='+urllib.quote_plus(thumbnail)+'&amp;url=http')
                resolved = resolved1+urllib.quote_plus(result)
            else:
                resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.ts') >= 0:
            if int(f4mvip) == 0:
                clear1 = re.compile("Referer(.*)", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                clear2 = re.compile("User-Agent(.*)", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                if clear1 !=[] and clear2 !=[]:
                    link_clear = link_decoded.replace(clear1[0],'').replace(clear2[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                elif clear1 !=[]:
                    link_clear = link_decoded.replace(clear1[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                elif clear2 !=[]:
                    link_clear = link_decoded.replace(clear2[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                else:
                    link_clear = link_decoded
                #print(link_clear)
                get_referer = re.compile("Referer=(.*).+?User-Agent", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_referer2 = re.compile('Referer=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_user = re.compile('User-Agent=(.*).+?Referer', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_user2 = re.compile('User-Agent=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                if get_referer !=[]:
                    ref = get_referer[0]
                    referer = 'Referer='+ref+''
                elif get_referer2 !=[]:
                    ref = get_referer2[0]
                    referer = 'Referer='+ref+''
                else:
                    referer = ''
                if get_user !=[]:
                    user = get_user[0]
                    user_agent = 'User-Agent='+user+''
                elif get_user2 !=[]:
                    user = get_user2[0]
                    user_agent = 'User-Agent='+user+''
                else:
                    user_agent = ''
                if referer > '' and user_agent > '':
                    result = '|'+referer+'|'+user_agent
                elif referer > '':
                    result = '|'+referer
                elif user_agent > '':
                    result = '|'+user_agent
                else:
                    result = ''
                name2 = name.replace('&','e').replace('BR | ','').replace('BR : ','').replace('BR: ','').replace('BR| ','').replace('|','')
                url_quote = urllib.quote_plus(link_clear)
                resolved1 = url_quote.replace('http','plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+urllib.quote_plus(str(name2))+'&amp;iconImage='+urllib.quote_plus(thumbnail)+'&amp;thumbnailImage='+urllib.quote_plus(thumbnail)+'&amp;url=http')
                resolved = resolved1+urllib.quote_plus(result)
            else:
                resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and not link_decoded.find('googlevideo.com') >= 0 and not link_decoded.find('blogspot.com') >= 0 and not link_decoded.find('googleusercontent.com') >= 0 and not link_decoded.find('p.netcine.info') >= 0 and not link_decoded.find('live.cinexplay.com') >= 0 and not link_decoded.find('youtube.com') >= 0 and int(link_decoded.count(":")) == 2 and int(link_decoded.count("/")) > 3:
            if int(f4mvip) == 0:
                clear1 = re.compile("Referer(.*)", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                clear2 = re.compile("User-Agent(.*)", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                if clear1 !=[] and clear2 !=[]:
                    link_clear = link_decoded.replace(clear1[0],'').replace(clear2[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                elif clear1 !=[]:
                    link_clear = link_decoded.replace(clear1[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                elif clear2 !=[]:
                    link_clear = link_decoded.replace(clear2[0],'').replace('|Referer','').replace('|referer','').replace('|User-Agent','').replace('|user-agent','').replace('|User-agent','').replace('|user-Agent','')
                else:
                    link_clear = link_decoded
                #print(link_clear)
                get_referer = re.compile("Referer=(.*).+?User-Agent", re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_referer2 = re.compile('Referer=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_user = re.compile('User-Agent=(.*).+?Referer', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                get_user2 = re.compile('User-Agent=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_decoded)
                if get_referer !=[]:
                    ref = get_referer[0]
                    referer = 'Referer='+ref+''
                elif get_referer2 !=[]:
                    ref = get_referer2[0]
                    referer = 'Referer='+ref+''
                else:
                    referer = ''
                if get_user !=[]:
                    user = get_user[0]
                    user_agent = 'User-Agent='+user+''
                elif get_user2 !=[]:
                    user = get_user2[0]
                    user_agent = 'User-Agent='+user+''
                else:
                    user_agent = ''
                if referer > '' and user_agent > '':
                    result = '|'+referer+'|'+user_agent
                elif referer > '':
                    result = '|'+referer
                elif user_agent > '':
                    result = '|'+user_agent
                else:
                    result = ''
                name2 = name.replace('&','e').replace('BR | ','').replace('BR : ','').replace('BR: ','').replace('BR| ','').replace('|','')
                url_quote = urllib.quote_plus(link_clear)
                resolved1 = url_quote.replace('http','plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+urllib.quote_plus(str(name2))+'&amp;iconImage='+urllib.quote_plus(thumbnail)+'&amp;thumbnailImage='+urllib.quote_plus(thumbnail)+'&amp;url=http')
                resolved = resolved1+urllib.quote_plus(result)
            else:
               resolved = link_decoded
        else:
            #print('falso')
            resolved = link_decoded
        return resolved
    except:
        resolved = ''
        return resolved
        #pass
        #notify('[COLOR red]Não foi possivel resolver um link![/COLOR]')



###FAVORITOS
def getFavorites():
    try:
        items = json.loads(open(favorites).read())
        total = len(items)
        for i in items:
            name = i[0]
            url = i[1]
            try:
                urldecode = base64.b64decode(base64.b16decode(url))
            except:
                urldecode = url
            mode = i[2]
            subtitle = i[3]
            try:
                subtitledecode = base64.b64decode(base64.b16decode(subtitle))
            except:
                subtitledecode = subtitle
            cleaname = i[4]
            iconimage = i[5]
            try:
                fanArt = i[6]
                if fanArt == None:
                    raise
            except:
                if addon.getSetting('use_thumb') == "true":
                    fanArt = iconimage
                else:
                    fanArt = fanart
            description = i[7]

            if mode == 0:
                try:
                    addLink(name,urldecode,subtitledecode,cleaname,iconimage,fanArt,description)
                except:
                    pass
            elif mode == 11 or mode == 16 or mode == 17:
                try:
                    addDir2(str(name).encode('utf-8', 'ignore'),str(urldecode),mode,str(subtitledecode),cleaname.encode('utf-8', 'ignore'),iconimage,fanArt,description.encode('utf-8'),False)
                except:
                    pass
            elif mode > 0 and mode < 7:
                try:
                    addDir(name,urldecode,mode,iconimage,fanArt,description)
                except:
                    pass
            else:
                try:
                    addDir2(str(name).encode('utf-8', 'ignore'),str(urldecode),mode,str(subtitledecode),cleaname.encode('utf-8', 'ignore'),iconimage,fanArt,description.encode('utf-8'))
                except:
                    pass
    except:
        pass


def addFavorite(name,url,fav_mode,subtitle,cleaname,iconimage,fanart,description):
    favList = []
    try:
        # seems that after
        name = name.encode('utf-8', 'ignore')
    except:
        pass
    if os.path.exists(favorites)==False:
        addonID = xbmcaddon.Addon().getAddonInfo('id')
        addon_data_path = xbmc.translatePath(os.path.join('special://home/userdata/addon_data', addonID))
        if os.path.exists(addon_data_path)==False:
            os.mkdir(addon_data_path)
        xbmc.sleep(7)
        favList.append((name,url,fav_mode,subtitle,cleaname,iconimage,fanart,description))
        a = open(favorites, "w")
        a.write(json.dumps(favList))
        a.close()
        notify('Adicionado aos Favoritos do AKATSUKI')
        xbmc.executebuiltin("XBMC.Container.Refresh")
    else:
        a = open(favorites).read()
        data = json.loads(a)           
        data.append((name,url,fav_mode,subtitle,cleaname,iconimage,fanart,description))
        b = open(favorites, "w")
        b.write(json.dumps(data))
        b.close()
        notify('Adicionado aos Favoritos do AKATSUKI!')
        xbmc.executebuiltin("XBMC.Container.Refresh")

            
def rmFavorite(name):
    data = json.loads(open(favorites).read())
    for index in range(len(data)):
        if data[index][0]==name:
            del data[index]
            b = open(favorites, "w")
            b.write(json.dumps(data))
            b.close()
            break
    notify('Removido dos Favoritos do AKATSUKI')
    xbmc.executebuiltin("XBMC.Container.Refresh")            




def addDir(name,url,mode,iconimage,fanart,description,folder=True):
    if mode == 1:
        if url > '':
            #u=sys.argv[0]+"?url="+urllib.quote_plus(base64.b64encode(url))+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
            u=sys.argv[0]+"?url="+urllib.quote_plus(codecs.encode(base64.b32encode(base64.b16encode(url)), '\x72\x6f\x74\x31\x33'))+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        else:
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(5)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
    else:
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
    if folder==True:
        li=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    else:
        li=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    li.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
    if fanart > '':
        li.setProperty('fanart_image', fanart)
    else:
        li.setProperty('fanart_image', ''+home+'/fanart.jpg')
    ##FAV
    if favoritos == 'true' and  mode !=4 and mode !=7 and mode !=8 and mode !=9 and mode !=10 and mode !=15 and not url.find('username') >= 0:
        try:
            name_fav = json.dumps(name)
        except:
            name_fav =  name
        try:
            contextMenu = []
            if name_fav in FAV:
                try:
                    contextMenu.append(('Remover dos Favoritos do AKASTSUKI','XBMC.RunPlugin(%s?mode=14&name=%s)'%(sys.argv[0], urllib.quote_plus(name))))
                except:
                    contextMenu.append(('Remover dos Favoritos do AKASTSUKI','XBMC.RunPlugin(%s?mode=14&name=%s)'%(sys.argv[0], urllib.quote_plus(name.encode('utf-8', 'ignore')))))
            else:
                try:            
                    fav_params = ('%s?mode=13&name=%s&url=%s&subtitle=%s&cleaname=%s&iconimage=%s&fanart=%s&description=%s&fav_mode=%s'%(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(base64.b16encode(base64.b64encode(url.encode('utf-8')))), '', '', urllib.quote_plus(iconimage), urllib.quote_plus(fanart), urllib.quote_plus(description), str(mode)))
                except:            
                    fav_params = ('%s?mode=13&name=%s&url=%s&subtitle=%s&cleaname=%s&iconimage=%s&fanart=%s&description=%s&fav_mode=%s'%(sys.argv[0], urllib.quote_plus(name.encode('utf-8', 'ignore')), urllib.quote_plus(base64.b16encode(base64.b64encode(url.encode('utf-8')))), '', '', urllib.quote_plus(iconimage.encode("utf-8")), urllib.quote_plus(fanart.encode("utf-8")), urllib.quote_plus(description.encode("utf-8")), str(mode)))
                contextMenu.append(('Adicionar aos Favoritos do AKASTSUKI','XBMC.RunPlugin(%s)' %fav_params))
            li.addContextMenuItems(contextMenu)
        except:
            pass
    xbmcplugin.addDirectoryItem(handle=addon_handle,url=u,listitem=li, isFolder=folder)



def addDir2(name,url,mode,subtitle,cleaname,iconimage,fanart,description,folder=True):
    if mode == 1:
        if url > '':
            #u=sys.argv[0]+"?url="+urllib.quote_plus(base64.b64encode(url))+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
            u=sys.argv[0]+"?url="+urllib.quote_plus(codecs.encode(base64.b32encode(base64.b16encode(url)), '\x72\x6f\x74\x31\x33'))+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        else:
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(5)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
    else:
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)+"&iconimage="+urllib.quote_plus(iconimage)+"&subtitle="+urllib.quote_plus(subtitle)+"&cleaname="+urllib.quote_plus(cleaname)+"&description="+urllib.quote_plus(description)
    if folder==True:
        li=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    else:
        li=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    li.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
    if fanart > '':
        li.setProperty('fanart_image', fanart)
    else:
        li.setProperty('fanart_image', ''+home+'/fanart.jpg')
    ##FAV
    if favoritos == 'true' and  mode !=4 and mode !=7 and mode !=8 and mode !=9 and mode !=10 and mode !=15 and not url.find('username') >= 0:
        try:
            name_fav = json.dumps(name)
        except:
            name_fav =  name
        try:
            contextMenu = []
            if name_fav in FAV:
                try:
                    contextMenu.append(('Remover dos Favoritos do AKASTSUKI','XBMC.RunPlugin(%s?mode=14&name=%s)'%(sys.argv[0], urllib.quote_plus(name))))
                except:
                    contextMenu.append(('Remover dos Favoritos do AKASTSUKI','XBMC.RunPlugin(%s?mode=14&name=%s)'%(sys.argv[0], urllib.quote_plus(name.encode('utf-8', 'ignore')))))
            else:
                try:
                    fav_params = ('%s?mode=13&name=%s&url=%s&subtitle=%s&cleaname=%s&iconimage=%s&fanart=%s&description=%s&fav_mode=%s'%(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(base64.b16encode(base64.b64encode(url.encode('utf-8')))), urllib.quote_plus(base64.b16encode(base64.b64encode(subtitle.encode('utf-8')))), urllib.quote_plus(cleaname), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), urllib.quote_plus(description), str(mode)))
                except:            
                    fav_params = ('%s?mode=13&name=%s&url=%s&subtitle=%s&cleaname=%s&iconimage=%s&fanart=%s&description=%s&fav_mode=%s'%(sys.argv[0], urllib.quote_plus(name.encode('utf-8', 'ignore')), urllib.quote_plus(base64.b16encode(base64.b64encode(url.encode('utf-8')))), urllib.quote_plus(base64.b16encode(base64.b64encode(subtitle.encode('utf-8')))), urllib.quote_plus(cleaname.encode("utf-8")), urllib.quote_plus(iconimage.encode("utf-8")), urllib.quote_plus(fanart.encode("utf-8")), urllib.quote_plus(description.encode("utf-8")), str(mode)))
                contextMenu.append(('Adicionar aos Favoritos do AKASTSUKI','XBMC.RunPlugin(%s)' %fav_params))
            li.addContextMenuItems(contextMenu)
        except:
            pass
    xbmcplugin.addDirectoryItem(handle=addon_handle,url=u,listitem=li, isFolder=folder)



def addLink(name,url,subtitle,cleaname,iconimage,fanart,description,folder=False):
    if iconimage > '':
        thumbnail = iconimage
    else:
        thumbnail = 'DefaultVideo.png'
    li = xbmcgui.ListItem(name, iconImage=thumbnail, thumbnailImage=thumbnail)
    if url.startswith("plugin://plugin.video.f4mTester"):
        li.setProperty('IsPlayable', 'false')
    else:
        li.setProperty('IsPlayable', 'true')
    if fanart > '':
        li.setProperty('fanart_image', fanart)
    else:
        li.setProperty('fanart_image', ''+home+'/fanart.jpg')
    if cleaname > '':
        try:
            name_fav = json.dumps(cleaname)
        except:
            name_fav =  cleaname
        name2_fav = cleaname
        desc_fav = ''
        li.setInfo(type='video', infoLabels={'Title': cleaname, 'plot': description })
    else:
        try:
            name_fav = json.dumps(name)
        except:
            name_fav = name
        name2_fav = name
        desc_fav = description
        li.setInfo(type='video', infoLabels={'plot': description })
    if subtitle > '':
        li.setSubtitles([subtitle])
    ##FAV
    if favoritos == 'true':
        try:
            contextMenu = []
            if name_fav in FAV:
                try:
                    contextMenu.append(('Remover dos Favoritos do AKASTSUKI','XBMC.RunPlugin(%s?mode=14&name=%s)'%(sys.argv[0], urllib.quote_plus(name2_fav))))
                except:
                    contextMenu.append(('Remover dos Favoritos do AKASTSUKI','XBMC.RunPlugin(%s?mode=14&name=%s)'%(sys.argv[0], urllib.quote_plus(name2_fav.encode('utf-8', 'ignore')))))
            else:
                try:           
                    fav_params = ('%s?mode=13&name=%s&url=%s&subtitle=%s&cleaname=%s&iconimage=%s&fanart=%s&description=%s&fav_mode=0'%(sys.argv[0], urllib.quote_plus(name2_fav), urllib.quote_plus(base64.b16encode(base64.b64encode(url.encode('utf-8')))), urllib.quote_plus(base64.b16encode(base64.b64encode(subtitle.encode('utf-8')))), urllib.quote_plus(cleaname), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), urllib.quote_plus(desc_fav)))
                except:
                    fav_params = ('%s?mode=13&name=%s&url=%s&subtitle=%s&cleaname=%s&iconimage=%s&fanart=%s&description=%s&fav_mode=0'%(sys.argv[0], urllib.quote_plus(name2_fav.encode('utf-8', 'ignore')), urllib.quote_plus(base64.b16encode(base64.b64encode(url.encode('utf-8')))), urllib.quote_plus(base64.b16encode(base64.b64encode(subtitle.encode('utf-8')))), urllib.quote_plus(cleaname.encode("utf-8")), urllib.quote_plus(iconimage.encode("utf-8")), urllib.quote_plus(fanart.encode("utf-8")), urllib.quote_plus(desc_fav.encode("utf-8"))))
                contextMenu.append(('Adicionar aos Favoritos do AKASTSUKI','XBMC.RunPlugin(%s)' %fav_params))
            li.addContextMenuItems(contextMenu)
        except:
            pass
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=folder)



def parental_password():
    try:
        addonID = xbmcaddon.Addon().getAddonInfo('id')
        addon_data_path = xbmc.translatePath(os.path.join('special://home/userdata/addon_data', addonID))
        if os.path.exists(addon_data_path)==False:
            os.mkdir(addon_data_path)
        xbmc.sleep(7)
        #Path = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile')).decode("utf-8")
        #arquivo = os.path.join(Path, "password.txt")
        arquivo = os.path.join(addon_data_path, "password.txt")
        exists = os.path.isfile(arquivo)
        if exists == False:
            password = '0069'
            p_encoded = base64.b64encode(password.encode()).decode('utf-8')
            p_file = open(arquivo,'w')
            p_file.write(p_encoded)
            p_file.close()
    except:
        pass



def check_addon():
    try:
        check_file = xbmc.translatePath(home+'/check.txt')
        exists = os.path.isfile(check_file)
        check_addon = addon.getSetting('check_addon')
        #check_file = 'check.txt'
        if exists == True:
            #print('existe')
            fcheck = open(check_file,'r+')
            elementum = addon.getSetting('elementum')
            if fcheck and fcheck.read() == '1' and check_addon == 'true':
                #print('valor 1')
                fcheck.close()
                link = getRequest2('https://raw.githubusercontent.com/zoreu/zoreu.github.io/master/verificar_addons.txt','').replace('\n','').replace('\r','')
                match = re.compile('addon_name="(.+?)".+?ddon_id="(.+?)".+?ir="(.+?)".+?rl_zip="(.+?)".+?escription="(.+?)"').findall(link)
                for addon_name,addon_id,directory,url_zip,description in match:
                    #if addon_id == id_elementum:
                    if addon_id == 'plugin.video.elementum' and elementum == 'false':
                        pass
                    else:
                        existe = xbmc.translatePath(directory)
                        #print('Path dir:'+existe)
                        if os.path.exists(existe)==False:
                            install_wizard(addon_name,addon_id,url_zip,directory,description)
                            anti_bug(addon_id)
                            if addon_id == 'plugin.video.elementum':
                                xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','FECHE O KODI E ABRA NOVAMENTE PARA ATIVAR O ELEMENTUM')
                        else:
                            pass
        elif check_addon == 'true':
            #print('nao existe')
            fcheck = open(check_file,'w')
            fcheck.write('1')
            fcheck.close()
            xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','FECHE O KODI E ABRA NOVAMENTE PARA VERIFICAR COMPLEMENTOS')
    except:
        pass



def install_wizard(name,addon_id,url,directory,description):
    try:
        import downloader
        import extract
        import ntpath
        #import zipfile
        path = xbmc.translatePath(os.path.join('special://','home/','addons', 'packages'))
        print('Path download:'+path)
        filename = ntpath.basename(url)
        dp = xbmcgui.DialogProgress()
        dp.create("Install addons","Baixando "+name+"....",'', '')
        lib=os.path.join(path, filename)
        try:
         os.remove(lib)
        except:
            pass
        #downloader.download(url, lib, dp)
        downloader.download(url, name, lib, dp)
        addonfolder = xbmc.translatePath(os.path.join('special://','home/','addons'))
        #time.sleep(2)
        xbmc.sleep(100)
        dp.update(0,"", "Instalando "+name+", Por Favor Espere")
        #extract.all(lib,addonfolder,dp)
        #### zip
        #zf = zipfile.ZipFile(lib)
        #zf.extractall(addonfolder)
        try:
            xbmc.executebuiltin("Extract("+lib+","+addonfolder+")")
        except:
            extract.all(lib,addonfolder,dp)
        #############
        #time.sleep(2)
        xbmc.sleep(100)
        xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
        notify(name+' Instalado com Sucesso!')
        import database
        database.enable_addon(0, addon_id)
        database.check_database(addon_id)
        #xbmc.executebuiltin("XBMC.Container.Refresh()")
        xbmc.executebuiltin("XBMC.Container.Update()")
        #xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]',''+name+' instalado, feche e abra o Kodi novamente')
    except:
        notify('Erro ao baixar o complemento')



def anti_bug(addon_id):
    import database
    database.enable_addon(0, addon_id)



def contador():
    try:
        request_headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8",
        "Referer": nome_contador,
        "Connection": "close",
        }
        request = urllib2.Request(url_contador, headers=request_headers)
        response = urllib2.urlopen(request).read()
        #tempo_delay = 0
        #xbmc.sleep(tempo_delay*0)
    except:
        pass
contador()



def time_convert(timestamp):
    try:
        if timestamp > '':
            dt_object = datetime.fromtimestamp(int(timestamp))
            time_br = dt_object.strftime('%d/%m/%Y às %H:%M:%S')
            return str(time_br)
        else:
            valor = ''
            return valor
    except:
        valor = ''
        return valor


def info_vip():
    username_vip = addon.getSetting('username')
    password_vip = addon.getSetting('password')
    server_vip = vip_serverlist()
    if server_vip == url_server_vip1:
        numero_servidor = 'Servidor 1'
    elif server_vip == url_server_vip2:
        numero_servidor = 'Servidor 2'
    if username_vip > '' and password_vip > '':
        try:
            url_info = server_vip.replace('/get.php', '')+'/player_api.php?username=%s&password=%s'%(username_vip,password_vip)
            dados_vip = getRequest2(url_info, '')
            filtrar_info = re.compile('"status":"(.+?)".+?"exp_date":"(.+?)".+?"is_trial":"(.+?)".+?"created_at":"(.+?)".+?max_connections":"(.+?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(dados_vip)
            if filtrar_info !=[]:
                status = str(filtrar_info[0][0])
                exp_date = str(filtrar_info[0][1])
                trial = str(filtrar_info[0][2])
                created = str(filtrar_info[0][3])
                max_connection = str(filtrar_info[0][4])
                #status do usuario
                if status > '' and status == 'Active':                    
                    status_result = 'Ativo'
                else:
                    status_result = 'Expirado'
                #Validade do vip
                if exp_date > '':
                    expires = time_convert(str(exp_date))
                else:
                    expires = ''
                #usuario de teste
                if trial > '' and trial == '0':
                    vip_trial = 'Não'
                else:
                    vip_trial = 'Sim'
                #criado
                if created > '':
                    created_time = time_convert(str(created))
                else:
                    created_time = ''
                #limite de conexoes
                if max_connection > '':
                    limite_conexao = max_connection
                else:
                    limite_conexao = ''                    
                    
                try:
                    xbmcaddon.Addon().setSetting("server_number", numero_servidor)
                    xbmcaddon.Addon().setSetting("status_vip", status_result)
                    xbmcaddon.Addon().setSetting("created_at", created_time)
                    xbmcaddon.Addon().setSetting("exp_date", expires)
                    xbmcaddon.Addon().setSetting("is_trial", vip_trial)
                    xbmcaddon.Addon().setSetting("max_connection", limite_conexao)
                except:
                    pass
        except:
            try:
                xbmcaddon.Addon().setSetting("server_number", '')
                xbmcaddon.Addon().setSetting("status_vip", '')
                xbmcaddon.Addon().setSetting("created_at", '')
                xbmcaddon.Addon().setSetting("exp_date", '')
                xbmcaddon.Addon().setSetting("is_trial", '')
                xbmcaddon.Addon().setSetting("max_connection", '')
            except:
                pass



def vip():
    username_vip = addon.getSetting('username')
    password_vip = addon.getSetting('password')
    #tipo_servidor = addon.getSetting('servidor')
    vip_menu = addon.getSetting('exibirvip')
    saida_transmissao = addon.getSetting('saida')
    server_vip = vip_serverlist()
    if username_vip > '' and password_vip > '':
        info_vip()
    if int(saida_transmissao) == 1:
        saida_canal = 'm3u8'
    else:
        saida_canal = 'ts'
    if vip_menu == 'true':
        if username_vip > '' and password_vip > '':
            url = ''+server_vip+'?username=%s&password=%s&type=m3u_plus&output=%s'%(username_vip,password_vip,saida_canal)
            #addDir(name,url,mode,iconimage,fanart,description)
            addDir(titulo_vip,url,1,thumbnail_vip,fanart_vip,vip_descricao)
        else:
            #if tipo_servidor=='Desativado':
            #addDir(name,url,mode,iconimage,fanart,description)
            addDir(titulo_vip,'',9,thumbnail_vip,fanart_vip,vip_descricao)



def SetView(name):
    if name == 'Wall':
        try:
            xbmc.executebuiltin('Container.SetViewMode(500)')
        except:
            pass
    if name == 'List':
        try:
            xbmc.executebuiltin('Container.SetViewMode(50)')
        except:
            pass
    if name == 'Poster':
        try:
            xbmc.executebuiltin('Container.SetViewMode(51)')
        except:
            pass
    if name == 'Shift':
        try:
            xbmc.executebuiltin('Container.SetViewMode(53)')
        except:
            pass
    if name == 'InfoWall':
        try:
            xbmc.executebuiltin('Container.SetViewMode(54)')
        except:
            pass
    if name == 'WideList':
        try:
            xbmc.executebuiltin('Container.SetViewMode(55)')
        except:
            pass
    if name == 'Fanart':
        try:
            xbmc.executebuiltin('Container.SetViewMode(502)')
        except:
            pass

def SKindex():
    #addDir(name,url,mode,iconimage,fanart,description)
    if addon.getSetting('mensagem1') == 'true':
        xbmcgui.Dialog().ok(titulo_boas_vindas,mensagem_bem_vindo)
    addDir(title_menu,url_title,1,__icon__,'',title_descricao)
    ### VIP ##############
    vip()
    if favoritos == 'true':
        addDir(menu_favoritos,'',15,thumb_favoritos,'',desc_favoritos)
    getData(url_principal, '')   
    addDir(menu_configuracoes,'',4,thumb_icon_config,'',desc_configuracoes)
    if addon.getSetting('mensagem2') == 'true':
        #xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,mensagem_secundaria, time_msg, __icon__))
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,getRequest2('https://pastebin.com/raw/pN8Peiui', 'https://pastebin.com/raw/xGgK3Ca1'), time_msg, __icon__))
    xbmcplugin.endOfDirectory(addon_handle)


def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]

        return param


params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None
subtitle=None
cleaname=None

xbmcplugin.setContent(addon_handle, 'movies')


try:
    #url=urllib.unquote(params["url"])
    url=urllib.unquote_plus(params["url"]).decode('utf-8')
except:
    pass

try:
    #name=urllib.unquote(params["name"])
    name=urllib.unquote_plus(params["name"])
except:
    pass

try:
    #iconimage=urllib.unquote(params["iconimage"])
    iconimage=urllib.unquote_plus(params["iconimage"])
except:
    pass

try:
    mode=int(params["mode"])
except:
    pass

try:
    #fanart=urllib.unquote(params["fanart"])
    fanart=urllib.unquote_plus(params["fanart"])
except:
    pass

try:
    #description=urllib.unquote(params["description"])
    description=urllib.unquote_plus(params["description"])
except:
    pass

try:
    subtitle=urllib.unquote_plus(params["subtitle"])
except:
    pass

try:
    cleaname=urllib.unquote_plus(params["cleaname"])
except:
    pass
    
try:
    fav_mode=int(params["fav_mode"])
except:
    pass



if mode==None:
    check_addon()
    parental_password()
    SKindex()
    SetView('List')

elif mode==1:
    url = base64.b16decode(base64.b32decode(codecs.decode(url, '\x72\x6f\x74\x31\x33')))
    #url = base64.b64decode(url)
    getData(url, fanart)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode==2:
    getChannelItems(name,url,fanart)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode==3:
    getSubChannelItems(name,url,fanart)
    xbmcplugin.endOfDirectory(addon_handle)


#Configurações
elif mode==4:
    xbmcaddon.Addon().openSettings()
    xbmc.executebuiltin("XBMC.Container.Refresh")
    xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','FECHE O KODI E ABRA NOVAMENTE PARA ATUALIZAR AS CONFIGURAÇÕES')
    #xbmc.executebuiltin("XBMC.Container.Refresh")

#Link Vazio
elif mode==5:
    xbmc.executebuiltin("XBMC.Container.Refresh")

elif mode==6:
    ytbmode = addon.getSetting('ytbmode')
    if int(ytbmode) == 0:
        pluginquerybyJSON(url)
    elif int(ytbmode) == 1:
        getPlaylistLinksYoutube(url)
    else:
        youtube(url)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode==9:      
    xbmcgui.Dialog().ok(titulo_vip, vip_dialogo)
    xbmcaddon.Addon().openSettings()
    xbmcgui.Dialog().ok('[B][COLOR white]AVISO[/COLOR][/B]','FECHE O KODI E ABRA NOVAMENTE PARA ATUALIZAR AS CONFIGURAÇÕES')
    xbmc.executebuiltin("XBMC.Container.Refresh")

elif mode==10:
    adult(name, url, cleaname, iconimage, description, subtitle)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode==11:
    playlist(name, url, cleaname, iconimage, description, subtitle)
    xbmcplugin.endOfDirectory(addon_handle)
    
elif mode==13:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass    
    addFavorite(name,url,fav_mode,subtitle,cleaname,iconimage,fanart,description)
    
elif mode==14:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    rmFavorite(name)
    
elif mode==15:
    getFavorites()
    xbmcplugin.endOfDirectory(addon_handle)
    
elif mode==16:
    individual_player(name, url, cleaname, iconimage, description, subtitle)
    xbmcplugin.endOfDirectory(addon_handle)
    
elif mode==17:
    m3u8_player(name, url, cleaname, iconimage, description, subtitle)
    xbmcplugin.endOfDirectory(addon_handle)