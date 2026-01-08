from .abs_os import AbsOS
from .mac import *
class MacOS(AbsOS): 

    @staticmethod
    def create_button(): 
        return MacButton()
    
    @staticmethod
    def create_checkbox(): 
        return MacCheckbox()
    
    @staticmethod
    def create_text_input(): 
        return MacTextInput()
    