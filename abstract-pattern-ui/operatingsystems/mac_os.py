from .abs_os import AbsOS
from .mac.button import MacButton
from .mac.checkbox import MacCheckbox
from .mac.textinput import MacTextInput

class MacOS(AbsOS): 

    def __init__(self): 
        self.button = MacButton()
        self.checkbox = MacCheckbox()
        self.text_input = MacTextInput()

    def create_button(self): 
        return self.button
    
    def create_checkbox(self): 
        return self.checkbox
    
    def create_text_input(self): 
        return self.text_input