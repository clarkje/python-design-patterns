import abc

class AbsTextInput(abc.ABC): 

    @abc.abstractmethod
    def render(self): 
        pass