from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class TSPILayout(BoxLayout):
    pass


class TSPIApp(App):
    def build(self):
        return TSPILayout()


if __name__ == '__main__':
    TSPIApp().run()
