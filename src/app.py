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
#Kivy  Markup
Builder.load_string("""
<MainScreen>:
    canvas.before:
        Color:
            rgba: .5,.5,.5,.5
        Rectangle:
            size: self.size
            pos: self.pos
    id: MainScreen
    BoxLayout:
        focus: True
        orientation: "horizontal"
        MainHeader:
            InfoLabel:
                text: "Cymbal AIS Viewer"
                
        
   """)

class MainScreen(App):
    def build(self):
        self.on_touch_down = False
        

    def on_touch_down(self,touch):
        if super().on_touch_down(touch):
            return True
        if not self.collide_point(touch.x,touch.y):
            return False
    
    


if __name__ == "__main__":
    try:
        MainScreen().run()
        start = time.perf_counter()
    except Exception as e:
        logger.exception("Exception occurred")
        pass