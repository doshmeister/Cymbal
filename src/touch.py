from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
#from subprocess import Popen, PIPE
import os, sys

Builder.load_string("""
<Screen>:
    btn:btn
    orientation: 'vertical'
    Label:
        id: msg
        text: "by jones its working"
        color: 1,0,0,1
        pos_hint: {"top":0.8}

    Button:
        id: btn
        size_hint: 0.2,0.2
        text: "Settings"
        on_release:  root.btn_touch_up()

""")


class Screen(BoxLayout):
    btn = ObjectProperty(None)

    def btn_touch_up(self):
        print("Touch Up ")
        #childprocess = Popen(['python3', 'settings.py',"r"], stdout=PIPE, stderr=PIPE)
        #return childprocess

        


class TouchApp(App):
    def build(self):
        return Screen()


if __name__ == "__main__":
    TouchApp().run()