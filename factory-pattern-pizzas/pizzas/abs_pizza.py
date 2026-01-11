import abc

class AbsPizza(abc.ABC): 

    def __init__(self): 
        self._name = None

    '''
    Pizza Name Property
    '''
    @property
    @abc.abstractmethod
    def name(self): 
        pass

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    '''
    Prints preparation steps
    '''
    @abc.abstractmethod
    def prepare(self): 
        pass 

    '''
    Prints baking information
    '''
    @abc.abstractmethod
    def bake(self): 
        pass

    '''
    Prints cutting style
    '''
    @abc.abstractmethod
    def cut(self): 
        pass
    
    '''
    Prints boxing information
    '''
    @abc.abstractmethod
    def box(self): 
        pass