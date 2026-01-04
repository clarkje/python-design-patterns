from .abs_factory import AbsFactory
from operatingsystems.mac_os import MacOS

class MacFactory(AbsFactory): 

    def __init__(self): 
        print("==== Mac OS ====")
        self.os = MacOS()
 
    def create_button(self): 
        return self.os.create_button()

    def create_checkbox(self):
        return self.os.create_checkbox()

    def create_textInput(self):
        return self.os.create_text_input()
