from .abs_factory import AbsFactory
from operatingsystems.windows_os import WindowsOS

class WindowsFactory(AbsFactory): 

    def __init__(self): 
        print("==== Windows OS ====")

    @staticmethod
    def create_button(): 
        return WindowsOS.create_button()

    @staticmethod
    def create_checkbox():
        return WindowsOS.create_checkbox()

    @staticmethod
    def create_textInput():
        return WindowsOS.create_text_input()
