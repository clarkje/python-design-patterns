from .abs_os import AbsOS
from .linux import *
class LinuxOS(AbsOS): 

    def __init__(self): 
        pass

    @staticmethod
    def create_button(): 
        return LinuxButton()
    
    @staticmethod
    def create_checkbox(): 
        return LinuxCheckbox()
    
    @staticmethod
    def create_text_input(): 
        return LinuxTextInput()