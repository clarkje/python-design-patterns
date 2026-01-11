from ..abs_checkbox import AbsCheckbox
class WindowsCheckbox(AbsCheckbox): 

    def render(self): 
        print("[Windows Checkbox] rendered")

    def toggle(self): 
        print("[Windows Checkbox] toggled")