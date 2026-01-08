from .abs_factory import AbsFactory
from operatingsystems.mac import *

class MacFactory(AbsFactory): 

    @staticmethod
    def create_button(): 
        return MacButton()

    @staticmethod
    def create_checkbox():
        return MacCheckbox()

    @staticmethod
    def create_text_input():
        return MacTextInput()