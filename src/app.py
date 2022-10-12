from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
import time
from sys import console

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
    except:
        console.log("MainScreen Class failed to run.")