from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder


Builder.load_string("""
<MainScreen>:
    canvas.before:
        Color:
            rgba: .5,.5,.5,.5
        Rectangle:
            size: self.size
            pos: self.pos
    id: MapScreen
    BoxLayout:
        focus: True
        orientation: "horizontal"
        MainHeader:
            InfoLabel:
                text: "Cymbal AIS Viewer"
        
   """)


class CymbalWidget(Widget):
    pass

class MainScreen(App):
    def build(self):
        return CymbalWidget()

    def on_touch_down(self,touch):
        if super().on_touch_down(touch):
            return True
        if not self.collide_point(touch.x,touch.y):
            return False



if __name__ == "__main__":
    MainScreen().run()
        
