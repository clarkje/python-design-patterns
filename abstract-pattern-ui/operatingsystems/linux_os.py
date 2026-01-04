from .abs_os import AbsOS
from .linux.button import LinuxButton
from .linux.checkbox import LinuxCheckbox
from .linux.textinput import LinuxTextInput

class LinuxOS(AbsOS): 

    def __init__(self): 
        self.button = LinuxButton()
        self.checkbox = LinuxCheckbox()
        self.text_input = LinuxTextInput()

    def create_button(self): 
        return self.button
    
    def create_checkbox(self): 
        return self.checkbox
    
    def create_text_input(self): 
        return self.text_input