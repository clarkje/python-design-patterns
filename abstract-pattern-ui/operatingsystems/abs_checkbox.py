import abc

class AbsCheckbox(abc.ABC): 

    @staticmethod
    @abc.abstractmethod
    def render(): 
        pass