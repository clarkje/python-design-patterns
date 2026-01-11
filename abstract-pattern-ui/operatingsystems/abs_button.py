import abc

class AbsButton(abc.ABC): 

    @abc.abstractmethod
    def render(self):
        pass
    
    @abc.abstractmethod
    def click(self): 
        pass