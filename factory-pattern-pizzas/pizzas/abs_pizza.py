import abc

class AbsPizza(abc.ABC): 

    def __init__(self): 
        self._name = None

    '''
    Pizza Name Property
    '''
    @property
    def name(self) -> str: 
        return self._name

    '''
    Prints preparation steps
    '''
    @abc.abstractmethod
    def prepare(self) -> str: 
        pass 

    '''
    Prints baking information
    '''
    @abc.abstractmethod
    def bake(self) -> str: 
        pass

    '''
    Prints cutting style
    '''
    @abc.abstractmethod
    def cut(self) -> str: 
        pass
    
    '''
    Prints boxing information
    '''
    @abc.abstractmethod
    def box(self) -> str: 
        pass