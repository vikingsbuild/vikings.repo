import xbmc
import xbmcgui
import extract
import downloader


def sublegenda(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("Addon Selecionado","Baixando ",'', 'Por Favor Espere')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home/','media'))
    time.sleep(2)
    dp.update(0,"", "Instalando Por Favor Espere")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    #dialog = xbmcgui.Dialog()
    #dialog.ok("Baixado com Sucesso:)", 'Para continuar a Instalacao irar ser solicitado que desligue o Kodi', 'Se for uma Box precione [COLOR yellow]NAO[/COLOR] depois sai do kodi para terminar a instalacao.','[COLOR yellow][B][Kodi 17][/B][/COLOR]Ao Voltar vai Addons em Meus Addons ativa o addons instalado')
    time.sleep(2)
    xbmc.executebuiltin("XBMC.UpdateLocalAddons()");
    addon_able.set_enabled("")
    addon_able.setall_enable()
