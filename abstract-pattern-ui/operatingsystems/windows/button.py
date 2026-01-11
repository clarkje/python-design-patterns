from ..abs_button import AbsButton
class WindowsButton(AbsButton): 

    def render(self): 
        print("[Windows Button] rendered")

    def click(self): 
        print("[Windows Button] clicked")