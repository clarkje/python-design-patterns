from .abs_os import AbsOS
from .windows import *
class WindowsOS(AbsOS): 

    def __init__(self): 
        self.button = WindowsButton()
        self.checkbox = WindowsCheckbox()
        self.text_input = WindowsTextInput()

        for item in self.button, self.checkbox, self.text_input: 
            if not isinstance(item, WinUI): 
                raise TypeError("Only WinUI elements are allowed")


    def create_button(self): 
        return self.button
    
    def create_checkbox(self): 
        return self.checkbox
    
    def create_text_input(self): 
        return self.text_input