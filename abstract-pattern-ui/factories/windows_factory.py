from .abs_factory import AbsFactory
from operatingsystems.windows import WindowsButton, WindowsCheckbox, WindowsTextInput

class WindowsFactory(AbsFactory): 

    def create_button(self): 
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

    def create_text_input(self):
        return WindowsTextInput()