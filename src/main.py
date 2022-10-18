from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.config import Config
import time
import logging

Config.window_icon = "data/icon.png"
Config.set("input", "mouse", "mouse,disable_multitouch")

logger = logging.getLogger("logger")
logging.basicConfig(format = "%(asctime)s - %(message)s",level=logging.INFO)
logging.basicConfig(format = "%(asctime)s - %(message)s",level=logging.DEBUG)
logging.basicConfig(format = "%(asctime)s - %(message)s",level=logging.WARNING)
logging.basicConfig(format = "%(asctime)s - %(message)s",level=logging.ERROR)
logging.basicConfig(format = "%(asctime)s - %(message)s",level=logging.CRITICAL)

class MainScreen(Widget):
    pass

class ship(Widget):
    pass
    #def move(self):
        #self.pos = "ais viewer api"

class CymbalApp(App):
    def build(self):
        return MainScreen()

    def on_touch_down(self,touch):
        if super().on_touch_down(touch):
            return True
        if not self.collide_point(touch.x,touch.y):
            return False
    
    


if __name__ == "__main__":
    try:
        CymbalApp().run()
        start = time.perf_counter()
    except Exception as e:
        logger.critical("Cymbal class failed to start")
        pass