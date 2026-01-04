from .abs_factory import AbsFactory

class NullFactory(): 
     
    @abc.staticmethod
    @abc.abstractmethod
    def create_button(self): 
        return None

    @abc.staticmethod
    @abc.abstractmethod
    def create_checkbox(self):
        return None

    @abc.staticmethod
    @abc.abstractmethod
    def create_textInput(self):
        return None