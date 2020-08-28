from kivy.app import App
from kivy.core.window import Window

from keylistener import MyKeyboardListener
from dbconnect import DatabaseHandler
#main app
class MainApp(App):
    def build(self):
        Window.size = (400, 600) #resize window
        return MyKeyboardListener()#return this so we can listen to keys, it extends ScatterTextWidget so access to widgets
        

if __name__ == '__main__':
    mainApp = MainApp()
    mainApp.run()

