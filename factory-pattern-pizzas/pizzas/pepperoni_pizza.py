from .abs_pizza import AbsPizza

class PepperoniPizza(AbsPizza): 

    def __init__(self):
        super().__init__()
        self._name = "Pepperoni Pizza"
        self._prep_instructions = """ 
            Add 1 Scoop Marinara Sauce
            Add 2 handfulls of mozarella
            Add 36 pepperoni slices
            """
        self._bake_instructions = """ 
            Preheat oven to 450
            Bake 14 minutes
        """
        self._cut_instructions = """ 
            Cut into 12 even pieces
        """
        self._box_instructions = """ 
            Put in box
            Open vent holes
        """

    @property
    def name(self): 
        return self._name
    
    @name.setter
    def name(self, name): 
        self._name = name
    
    def prepare(self): 
        return(f"Preparation Instructions\n {self._prep_instructions}")

    def bake(self): 
        return(f"Baking Instructions\n {self._bake_instructions}")

    def cut(self): 
        return(f"Cutting Instructions: {self._cut_instructions}")

    def box(self): 
        return(f"Boxing Instructions: {self._box_instructions}")