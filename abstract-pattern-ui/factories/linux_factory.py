from .abs_factory import AbsFactory
from operatingsystems.linux_os import LinuxOS

class LinuxFactory(AbsFactory): 

    def __init__(self): 
        print("==== Linux OS ====")
        self.os = LinuxOS()
 
    def create_button(self): 
        return self.os.create_button()

    def create_checkbox(self):
        return self.os.create_checkbox()

    def create_textInput(self):
        return self.os.create_text_input()
