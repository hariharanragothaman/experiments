from kivy.app import App
from kivy.uix.button import Button

"""
Kivy is an event-based framework.
responds to keypresses, mouse events, touch events etc.
Kivy also has the concept of a Clock, that can used to schedule function calls

What are 'Properties' ?
Properties + EventDispatcher --> help in validation checking
Also helps in firing events.

"""

class MainApp(App):
    def build(self):
        button = Button(text='Hello from Kivy',
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})


        # This is acting like a function-calllback? Alright.
        button.bind(on_press=self.on_press_button)

        return button

    def on_press_button(self, instance):
        print('You pressed the button!')

if __name__ == '__main__':
    app = MainApp()
    app.run()
