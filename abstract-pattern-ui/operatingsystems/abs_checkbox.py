import abc

class AbsCheckbox(abc.ABC): 

    @abc.abstractmethod
    def render(self): 
        pass

    @abc.abstractmethod
    def toggle(self): 
        pass