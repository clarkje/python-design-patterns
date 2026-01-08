from .abs_factory import AbsFactory
from operatingsystems.windows import *

class WindowsFactory(AbsFactory): 

    @staticmethod
    def create_button(): 
        return WindowsButton()

    @staticmethod
    def create_checkbox():
        return WindowsCheckbox()

    @staticmethod
    def create_text_input():
        return WindowsTextInput()