from kivy.lang import Builder
from kivymd.app import MDApp

import kivymd_extensions.akivymd
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch
class Container(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True

class App(MDApp):
    def build(self):
        self.title = 'Setting Screen UI'
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.theme_style = "Dark"  # "Light"
        return Builder.load_file('main.kv')


App().run()
