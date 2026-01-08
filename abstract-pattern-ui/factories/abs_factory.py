import abc

class AbsFactory(abc.ABC):
    
    @abc.abstractmethod
    def create_button(): 
        pass; 

    @abc.abstractmethod
    def create_checkbox():
        pass;

    @abc.abstractmethod
    def create_text_input():
        pass;