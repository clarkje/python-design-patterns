from .abs_os import AbsOS
from .windows import *
class WindowsOS(AbsOS): 

    def __init__(self): 
        pass

    @staticmethod
    def create_button(): 
        return WindowsButton()
    
    @staticmethod
    def create_checkbox(): 
        return WindowsCheckbox()
    
    @staticmethod
    def create_text_input(): 
        return WindowsTextInput()