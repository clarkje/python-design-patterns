from .abs_os import AbsOS
from .linux import *
class LinuxOS(AbsOS): 

    def __init__(self): 
        self.button = LinuxButton()
        self.checkbox = LinuxCheckbox()
        self.text_input = LinuxTextInput()

        for item in self.button, self.checkbox, self.text_input: 
            if not isinstance(item, LinuxUI): 
                raise TypeError("Only LinuxUI elements are allowed")

    def create_button(self): 
        return self.button
    
    def create_checkbox(self): 
        return self.checkbox
    
    def create_text_input(self): 
        return self.text_input