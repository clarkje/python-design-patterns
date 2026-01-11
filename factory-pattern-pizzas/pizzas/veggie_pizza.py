from .abs_pizza import AbsPizza

class VeggiePizza(AbsPizza): 

    def __init__(self):
        super().__init__()
        self._name = "Veggie Pizza"
        self._prep_instructions = """ 
            Add 1 Scoop Marinara Sauce
            Add 2 handfuls of mozarella
            Add 12 tomato slices
            Add 2 scoops broccoli
            Add 12 onion slices
            Add 1 scoop olives
            """
        self._bake_instructions = """ 
            Preheat oven to 450
            Bake 9 minutes
        """
        self._cut_instructions = """ 
            Cut into 12 even pieces
        """
        self._box_instructions = """ 
            Put in box
            Open vent holes
            Add veggie label
        """

    @property
    def name(self) -> str: 
        return self._name
    
    def prepare(self) -> str: 
        return f"Preparation Instructions\n {self._prep_instructions}"

    def bake(self) -> str: 
        return f"Baking Instructions\n {self._bake_instructions}"

    def cut(self) -> str: 
        return f"Cutting Instructions: {self._cut_instructions}"

    def box(self) -> str: 
        return f"Boxing Instructions: {self._box_instructions}"