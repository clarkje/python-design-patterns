from ..abs_checkbox import AbsCheckbox

class MacCheckbox(AbsCheckbox): 
    
    def render(self): 
        print("[Mac Checkbox] rendered")

    def toggle(self): 
        print("[Windows Checkbox] toggled")