from .abs_pizza import AbsPizza

class NullPizza(AbsPizza): 

    def __init__(self, name):
        self._pizza_type = name
        self._name = None
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
        print(f"Pizza Type {self._pizza_type} not Found")

    def bake(self): 
        print(f"Pizza Type {self._pizza_type} not found")

    def cut(self): 
        print(f"Pizza Type {self._pizza_type} not found")

    def box(self): 
        print(f"Pizza Type {self._pizza_type} not found")