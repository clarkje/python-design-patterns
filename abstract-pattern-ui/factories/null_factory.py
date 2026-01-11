from .abs_factory import AbsFactory
class NullFactory(AbsFactory): 

    def create_button(self): 
        raise NotImplementedError

    def create_checkbox(self):
        raise NotImplementedError

    def create_text_input(self):
        raise NotImplementedError