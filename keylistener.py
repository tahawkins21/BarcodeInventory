#for the keyboardlistener class
from kivy.core.window import Window
from kivy.uix.widget import Widget
from scattertext import ScatterTextWidget
#move to sep class 
#Only way i could access root object widgets was to pass ScatterTextWidget to the listener
#This is what is returned after app.build()
class MyKeyboardListener(ScatterTextWidget):
    
    def __init__(self, **kwargs):
        super(MyKeyboardListener, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            # If it exists, this widget is a VKeyboard object which you can use
            # to change the keyboard layout.
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        pass#TODO: find out why keyboard is closing when focus moves to input, then remove pass and add back logic

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keycode)
        if keycode == (13,'enter'):
            self.bcEnter()###this is where 'enter' keypress is handled to submit form
        

        # Keycode is composed of an integer + a string
        # If we hit escape, release the keyboard
        if keycode[1] == 'escape':
            keyboard.release()

        # Return True to accept the key. Otherwise, it will be used by
        # the system.
        return True