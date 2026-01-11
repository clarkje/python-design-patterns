from .abs_pizza import AbsPizza

class NullPizza(AbsPizza): 

    def __init__(self, name: str = None):
        self._pizza_type = name
        self._name = "NullPizza"
        self._prep_instructions = None
        self._bake_instructions = None
        self._cut_instructions = None
        self._box_instructions = None

    @property
    def name(self): 
        return None
    
    @name.setter
    def name(self, name): 
        pass
    
    def prepare(self): 
        raise ValueError(f"Pizza Type {self._pizza_type} not Found")

    def bake(self): 
        raise ValueError(f"Pizza Type {self._pizza_type} not found")

    def cut(self): 
        raise ValueError(f"Pizza Type {self._pizza_type} not found")

    def box(self): 
        raise ValueError(f"Pizza Type {self._pizza_type} not found")