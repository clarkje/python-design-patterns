import abc

class AbsFactory(abc.ABC):
    
    @staticmethod
    @abc.abstractmethod
    def create_button(self): 
        pass; 

    @staticmethod
    @abc.abstractmethod
    def create_checkbox(self):
        pass;

    @staticmethod
    @abc.abstractmethod
    def create_textInput(self):
        pass;