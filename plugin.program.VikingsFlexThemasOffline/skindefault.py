import xbmc,xbmcaddon,xbmcgui,os,time,sys
import skinSwitch

AddonID = 'plugin.program.VikingsFlexThemasOffline'
ADDON = xbmcaddon.Addon(id='plugin.program.VikingsFlexThemasOffline')
ADDONPATH = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID))
AddonTitle = "[COLOR aqua]Vikings Flex Themas Offline[/COLOR]"
HOME =  xbmc.translatePath('special://home/')
KODIVERSION = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
dialog = xbmcgui.Dialog()    
PATH = xbmcaddon.Addon().getAddonInfo('name')
VERSION = xbmcaddon.Addon().getAddonInfo('version')


def SetDefaultSkin():
	skin = xbmc.getSkinDir()
	skinswapped = 0

	##SWITCH SKIN IF THE CURRENT SKIN IS NOT DEFAULT SKIN
	if skin not in ['skin.confluence','skin.estuary']:
            choice = dialog.yesno(AddonTitle, '[COLOR red]Para mudar seu novo Tema, sera preciso que seu Kodi volte a Skin Padrao! Nao se procupe, apos a instalacao ela sera Ativada.[/COLOR]','Por favor, para continuar clique SIM. Enquanto isso, nao mexa em seu mouse, teclado ou controle, ou nao toque na tela de se SmartPhone ou Tablet', yeslabel='[B][COLOR green]SIM[/COLOR][/B]',nolabel='[B][COLOR red]NAO[/COLOR][/B]')
            if choice == 0:
                sys.exit(1)
            skin = 'skin.estuary' if KODIVERSION >= 17 else 'skin.confluence'
            skinSwitch.swapSkins(skin)
            skinswapped = 1
            time.sleep(1)

	##IF A SKIN SWAP HAS HAPPENED, CHECK IF OK DIALOG (CONFLUENCE INFO SCREEN) IS PRESENT, PRESS OK IF IT'S PRESENT
	if skinswapped == 1:
            if not xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
		xbmc.executebuiltin( "Action(Select)" )
	
	##IF THERE'S NO YES/NO DIALOG (SWITCH TO DEFAULT SKIN), THEN SLEEP UNTIL IT APPEARS
	if skinswapped == 1:
            while not xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
		time.sleep(1)
	
	##WHILE YES/NO DIALOG IS PRESENT, AUTOSELECT SKIN CHANGE (PRESS LEFT AND THEN SELECT)
	if skinswapped == 1:
            while xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
		xbmc.executebuiltin( "Action(Left)" )
		xbmc.executebuiltin( "Action(Select)" )
		time.sleep(1)

	skin = xbmc.getSkinDir()

	#CHECK IF THE SKIN IS NOT DEFAULT SKIN
	if skin not in ['skin.confluence','skin.estuary']:
            if skinswapped == 1:
		choice = dialog.yesno(AddonTitle,'ERRO: A desativacao da Skin em uso, nao foi bem sucedida!','Por favor, clique em SIM para instalar manualmente (nao recomendado), ou clique em NAO, para tentar novamente.', yeslabel='[B][COLOR green]SIM[/COLOR][/B]',nolabel='[B][COLOR lightskyblue]NAO (recomendado)[/COLOR][/B]')
		if choice == 1:
                    xbmc.executebuiltin("ActivateWindow(appearancesettings)")
                    return
		else:
                    sys.exit(1)