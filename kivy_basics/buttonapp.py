from kivy.app import App
from kivy.uix.button import Button

"""
This code might look a bit odd at first glance, 
as it creates a Button without setting any of its attributes or binding it 
to any events. What’s happening here is that 
Kivy will automatically look for a file that has the same name as the class 
in lowercase, without the App part of the class name.

In this case, the class name is ButtonApp, 
so Kivy will look for a file named button.kv. 
If that file exists and is properly formatted, 
then Kivy will use it to load up the UI. 
Go ahead and create this file 
"""

class ButtonApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print('You pressed the button!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()
