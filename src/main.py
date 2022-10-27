from kivy.app import App
from kivy.uix.widget import Widget
#from kivy.lang.builder import Builder
from kivy.config import Config
from kivy.clock import Clock
import logging

#Fetches ais data with api key
#ais.coordinates = doc.ais.something(something)


#Sets icon in top left
#Config.window_icon = "data/icon.png"
#Sets input sources as mouse and disables touchscreen functionality (this helps prevent accidental inputs on trackpad)
#Config.set("input", "mouse", "mouse,disable_multitouch")
logger = logging.getLogger("logger")
logging.basicConfig(format = "%(asctime)s - %(message)s",level=logging.INFO)
logging.basicConfig(format = "%(asctime)s - %(message)s",level=logging.DEBUG)
logging.basicConfig(format = "%(asctime)s - %(message)s",level=logging.WARNING)
logging.basicConfig(format = "%(asctime)s - %(message)s",level=logging.ERROR)
logging.basicConfig(format = "%(asctime)s - %(message)s",level=logging.CRITICAL)

class MainScreen(Widget):
    pass

class Shipobj(Widget):
    pass
    #def move(self):
        #self.pos = "ais api coordinates"
        #self.direction = "ais api bearing"

class CymbalApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    try:
        CymbalApp().run()
    except Exception as e:
        logger.critical("Cymbal class failed to start\n", exc_info = True)            