import abc

class AbsPizza(abc.ABC): 

    '''
    Pizza Name Property
    '''
    @property
    @abc.abstractmethod
    def name(self): 
        pass;

    @name.setter
    @abc.abstractmethod
    def name(self, name): 
        pass;

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