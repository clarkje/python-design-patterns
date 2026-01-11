import abc

class AbsFactory(abc.ABC):
    
    @abc.abstractmethod
    def create_button(self): 
        pass

    @abc.abstractmethod
    def create_checkbox(self):
        pass

    @abc.abstractmethod
    def create_text_input(self):
        pass