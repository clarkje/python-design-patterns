import abc

class AbsTextInput(abc.ABC): 

    @staticmethod
    @abc.abstractmethod
    def render(): 
        pass