from .abs_factory import AbsFactory
from operatingsystems.linux_os import LinuxOS

class LinuxFactory(AbsFactory): 

    def __init__(self): 
        print("==== Linux OS ====")

    @staticmethod
    def create_button(): 
        return LinuxOS.create_button()

    @staticmethod
    def create_checkbox():
        return LinuxOS.create_checkbox()

    @staticmethod
    def create_textInput():
        return LinuxOS.create_text_input()
