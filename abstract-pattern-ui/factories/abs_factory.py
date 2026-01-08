import abc

class AbsFactory(abc.ABC):
    
    @staticmethod
    @abc.abstractmethod
    def create_button(): 
        pass; 

    @staticmethod
    @abc.abstractmethod
    def create_checkbox():
        pass;

    @staticmethod
    @abc.abstractmethod
    def create_textInput():
        pass;