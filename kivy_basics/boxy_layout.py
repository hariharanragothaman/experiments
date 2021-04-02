"""
Some key notes:

1. A widget is an onscreen control that the user will interact with.
2.All interface tool kits come with a set of widgets.
    Eg: buttons, combo-boxes and tabs
    Like this there are many widgets in the framework
"""
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        #padding - this can be specified in pixels
        """
        A four-argument list: [padding_left, padding_top, padding_right, padding_bottom]
        A two-argument list: [padding_horizontal, padding_vertical]
        A singular argument: padding=10
        """
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text="Button #%s" % (i+1),
                         background_color=random.choice(colors)
                         )

            layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()