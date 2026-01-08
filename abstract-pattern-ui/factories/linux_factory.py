from .abs_factory import AbsFactory
from operatingsystems.linux import *

class LinuxFactory(AbsFactory): 

    @staticmethod
    def create_button(): 
        return LinuxButton()

    @staticmethod
    def create_checkbox():
        return LinuxCheckbox()

    @staticmethod
    def create_text_input():
        return LinuxTextInput()