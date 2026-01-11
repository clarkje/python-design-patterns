from pizzas import MargheritaPizza, PepperoniPizza, VeggiePizza, NullPizza, AbsPizza

class PizzaFactory:

    _available_pizza_types = {"margherita": MargheritaPizza, "pepperoni": PepperoniPizza, "veggie": VeggiePizza}

    @classmethod
    def create_pizza(cls, pizza_type: str) -> AbsPizza: 
        print(f"Pizza Type: {pizza_type}")
        if pizza_type not in cls._available_pizza_types:
            pizza_class = NullPizza(pizza_type)
        else: 
            pizza_class = cls._available_pizza_types[pizza_type]()
        return pizza_class
    
    @property
    def available_pizza_types(cls) -> dict: 
        return cls._available_pizza_types