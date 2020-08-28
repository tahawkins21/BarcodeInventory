#main widget stuff
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter#tracks touches
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown

import random
import dbconnect
from barcodehandle import BarcodeHandler
#for the keyboardlistener class
from kivy.core.window import Window
from kivy.uix.widget import Widget
#move to sep class 
#Only way i could access root object widgets was to pass ScatterTextWidget to the listener
#This is what is returned after app.build()

class ScatterTextWidget(BoxLayout):
    #need to work in SESSIONS to the creation of database handler...
    test = BarcodeHandler(1)
    #what actually looks up the barcode when called
    def lookupColor(self,*args):
        labelText = self.ids['myLabel']#reference to the label to change
        input = self.ids['textInput']#reference to the input
        barcode = ''
        try:
            ##>mysql -u admin -pJess#0521 -- root same pass -- database BarcodeInv
            barcode = input.text.replace('\n','')#get the barcode text from the input we linked to through main.kv
            self.test.checkProd(barcode)
        except Exception as e:
            print(e)
    
    #bound to the "reporting" button in .kv currently
    #also called from MyKeyBoardListener._on_key_down if key pressed is 'enter' or '\n' entered
    def bcEnter(self,*args):
        self.lookupColor()#looks up color
        testText = self.ids['textInput']#reference to the labelto change
        testText.text = ''#clears input text
        #TODO: more logic here after the lookup. Maybe callback with success/fail handling here?

#testing with dropdown for session loading
class SessionDropDown(DropDown):
    pass

class SessionButton(Widget):
    pass

