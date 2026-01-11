from .abs_pizza import AbsPizza

class NullPizza(AbsPizza): 

    def __init__(self, name: str = None):
        super().__init__()
        self._pizza_type = name
        self._name = "NullPizza"
        self._prep_instructions = None
        self._bake_instructions = None
        self._cut_instructions = None
        self._box_instructions = None

    @property
    def name(self) -> str: 
        return self._name
    
    def prepare(self) -> str: 
        raise ValueError(f"Pizza Type {self._pizza_type} not Found")

    def bake(self) -> str: 
        raise ValueError(f"Pizza Type {self._pizza_type} not found")

    def cut(self) -> str: 
        raise ValueError(f"Pizza Type {self._pizza_type} not found")

    def box(self) -> str: 
        raise ValueError(f"Pizza Type {self._pizza_type} not found")