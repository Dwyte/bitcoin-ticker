import os
import requests
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator, GLib

CURRPATH = os.path.dirname(os.path.realpath(__file__))
REFRESH_TIME = 3
EXCHANGE_API = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

class Indicator():
    def __init__(self):
        self.indicator = appindicator.Indicator.new("customtray", "semi-starred-symbolic", appindicator.IndicatorCategory.APPLICATION_STATUS)
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.indicator.set_icon(CURRPATH + "/btc.png")
        self.indicator.set_menu(self.build_menu())
        GLib.timeout_add_seconds(0, self.checkPrice)
    
    def build_menu(self):
        menu = gtk.Menu()

        exittray = gtk.MenuItem('Quit')
        exittray.connect('activate', self.quit)
        menu.append(exittray)
        
        menu.show_all()
        return menu

    def checkPrice(self):
        response = requests.get(EXCHANGE_API)
        if(response.ok):
            resJson = response.json()
            btcPrice = round(float(resJson['price']), 2)
            self.indicator.set_label(str(btcPrice), "")
        GLib.timeout_add_seconds(REFRESH_TIME, self.checkPrice)

    def quit(self, window):
        gtk.main_quit()

    
Indicator()
gtk.main()