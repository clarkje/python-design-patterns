from .abs_factory import AbsFactory
from operatingsystems.windows_os import WindowsOS

class WindowsFactory(AbsFactory): 

    def __init__(self): 
        print("==== Windows OS ====")
        self.os = WindowsOS()
 
    def create_button(self): 
        return self.os.create_button()

    def create_checkbox(self):
        return self.os.create_checkbox()

    def create_textInput(self):
        return self.os.create_text_input()
