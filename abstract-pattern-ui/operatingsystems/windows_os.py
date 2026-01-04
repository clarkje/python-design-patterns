from .abs_os import AbsOS
from .windows.button import WindowsButton
from .windows.checkbox import WindowsCheckbox
from .windows.textinput import WindowsTextInput

class WindowsOS(AbsOS): 

    def __init__(self): 
        self.button = WindowsButton()
        self.checkbox = WindowsCheckbox()
        self.text_input = WindowsTextInput()

    def create_button(self): 
        return self.button
    
    def create_checkbox(self): 
        return self.checkbox
    
    def create_text_input(self): 
        return self.text_input