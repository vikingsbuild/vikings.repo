# -*- coding: utf-8 -*-
import xbmc,xbmcaddon,xbmcgui,os,time,sys
import skinSwitch

AddonID = xbmcaddon.Addon().getAddonInfo('id')
ADDON = xbmcaddon.Addon(id=AddonID) 
AddonTitle = ADDON.getAddonInfo('name')
ADDONPATH = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID))
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
            choice = dialog.yesno(AddonTitle, '[COLOR red]Para mudar seu novo Tema, sera preciso que seu Kodi volte a Skin Padrão! Não se procupe, após a instalação ela será Ativada.[/COLOR]','Por favor, para continuar clique SIM. Enquanto isso, não mexa em seu mouse, teclado ou controle, ou não toque na tela de se SmartPhone ou Tablet', yeslabel='[B][COLOR green]SIM[/COLOR][/B]',nolabel='[B][COLOR red]Não[/COLOR][/B]')
            if choice == 0:
                sys.exit(1)
            skin = 'skin.estuary' if KODIVERSION >= 17 else 'skin.confluence'
            skinSwitch.swapSkins(skin)
            skinswapped = 1
            time.sleep(1)

	##IF A SKIN SWAP HAS HAPPENED, CHECK IF VI OK DIALOG (CONFLUENCE INFO SCREEN) IS PRESENT, PRESS OK IF IT'S PRESENT
	if skinswapped == 1:
            if not xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
		xbmc.executebuiltin( "Action(Select)" )
	
	##IF THERE'S NO YES/NO DIALOG (SWITCH TO DEFAULT SKIN), THEN SLEEP UNTIL IT APPEARS
	if skinswapped == 1:
            while not xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
		time.sleep(1)
	
	##WHILE YES/NO DIALOG IS PRESENT, AUTOSELECT SKIN KIN CHANGE (PRESS LEFT AND THEN SELECT)
	if skinswapped == 1:
            while xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
		xbmc.executebuiltin( "Action(Left)" )
		xbmc.executebuiltin( "Action(Select)" )
		time.sleep(1)

	skin = xbmc.getSkinDir()

	#CHECK IF THE SKIN IS NOT DEFAULT SKIN GS
	if skin not in ['skin.confluence','skin.estuary']:
            if skinswapped == 1:
		choice = dialog.yesno(AddonTitle,'ERRO: A desativacão da Skin em uso, não foi bem sucedida!','Por favor, clique em SIM para instalar manualmente (não recomendado), ou clique em Não, para tentar novamente.', yeslabel='[B][COLOR green]SIM[/COLOR][/B]',nolabel='[B][COLOR lightskyblue]Não (recomendado)[/COLOR][/B]')
		if choice == 1:
                    xbmc.executebuiltin("ActivateWindow(appearancesettings)")
                    return
		else:
                    sys.exit(1)