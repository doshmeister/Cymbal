import kivy
from kivy.app import App
from kivy.uix.label import Label
import os

kivy.config.Config.set('graphics', 'width', '400')
kivy.config.Config.set('graphics', 'height', '200')

class MyApp(App):
    def build(self):
        return Label(text="Hello, world!")

if __name__ == '__main__':
    MyApp().run()