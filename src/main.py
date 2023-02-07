import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MyWidget(Widget):
    def redraw(self,args):
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos

class CymbalApp(App):
    def build(self):
        return MyWidget()

widget = Widget()
with widget.canvas:
    widget.bg_rect = Rectangle(source="thefleshcapturesyourmind.jpg", pos=self.pos,size=self.size)
widget.bind(pos=redraw,size=redraw)

if __name__=="__main__":
    CymbalApp().run()