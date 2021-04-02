"""
Some key notes:

1. A widget is an onscreen control that the user will interact with.
2.All interface tool kits come with a set of widgets.
    Eg: buttons, combo-boxes and tabs
    Like this there are many widgets in the framework
"""

from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    """
    Every application needs to subclass App, and override build
    This is where UI code to make calls or other functions that define your UI code
    """
    def build(self):
        """
        size_hint tells the proportions to create the widget (width, height)

        :return:
        """
        # The label class can also take an image by passing the source param
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, "center_y": .5})
        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()