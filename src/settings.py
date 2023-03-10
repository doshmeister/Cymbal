from kivy.uix.screenmanager import Screen as SettingScreen
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import os


kv = Builder.load_string("""
<SettingScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Settings'
        Button:
            id: btn
            text: 'Exit'
            size_hint: 0.2,0.2
            on_release: app.stop()
""")


class SettingScreen(BoxLayout):
    btn = ObjectProperty(None)
        
class SettingsApp(App):
    def build(self):
        return SettingScreen()

if __name__ == "__main__":
    SettingsApp().run()