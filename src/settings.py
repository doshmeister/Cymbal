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
            text: 'Setting Screen'
        Button:
            id: btn
            text: 'Exit'
            on_release: app.stop()
""")


class SettingScreen(BoxLayout):
    btn = ObjectProperty(None)
        
class SettingsApp(App):
    def build(self):
        return SettingScreen()

if __name__ == "__main__":
    SettingsApp().run()