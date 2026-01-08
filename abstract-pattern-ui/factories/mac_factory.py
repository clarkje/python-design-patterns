from .abs_factory import AbsFactory
from operatingsystems.mac_os import MacOS

class MacFactory(AbsFactory): 

    def __init__(self): 
        print("==== Mac OS ====")
    
    @staticmethod
    def create_button(): 
        return MacOS.create_button()

    @staticmethod
    def create_checkbox():
        return MacOS.create_checkbox()

    @staticmethod
    def create_textInput():
        return MacOS.create_text_input()
