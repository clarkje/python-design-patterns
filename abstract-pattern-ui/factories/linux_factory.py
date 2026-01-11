from .abs_factory import AbsFactory
from operatingsystems.linux import LinuxButton, LinuxCheckbox, LinuxTextInput

class LinuxFactory(AbsFactory): 

    def create_button(self): 
        return LinuxButton()

    def create_checkbox(self):
        return LinuxCheckbox()

    def create_text_input(self):
        return LinuxTextInput()