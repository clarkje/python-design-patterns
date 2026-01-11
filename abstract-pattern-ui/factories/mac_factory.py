from .abs_factory import AbsFactory
from operatingsystems.mac import MacButton, MacCheckbox, MacTextInput

class MacFactory(AbsFactory): 

    def create_button(self): 
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

    def create_text_input(self):
        return MacTextInput()