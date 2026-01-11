from ..abs_checkbox import AbsCheckbox

class LinuxCheckbox(AbsCheckbox): 

    def render(self): 
        print("[Linux Checkbox] rendered")

    def toggle(self): 
        print("[Windows Checkbox] toggled")