import kivy
from kivy.app import App
from kivy_garden.mapview import MapView, MapLayer, Coordinate 
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


kv = Builder.load_string("""
<MapScreen>:
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

class MapScreen(Screen):
    pass

class MapApp(App):

    def build(self):
        return MapScreen()

while __name__ == "__main__":
    MapApp.run()