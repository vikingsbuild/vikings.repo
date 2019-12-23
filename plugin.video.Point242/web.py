import webbrowser
import xbmc

def os():
    if (xbmc . getCondVisibility ( 'system.platform.android' )) :
        return android
    else:
        return notandroid

def web(url):
    if os == 'android' :
      xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( url ) )

    else :
      webbrowser.open ( url )
