from pizzas import MargheritaPizza, PepperoniPizza, VeggiePizza, NullPizza, AbsPizza

class PizzaFactory:

    _available_pizza_types = {"margherita": MargheritaPizza, "pepperoni": PepperoniPizza, "veggie": VeggiePizza}

    def create_pizza(cls, pizza_type: str) -> AbsPizza: 
        if pizza_type not in cls._available_pizza_types:
            pizza_class = NullPizza(pizza_type)
        else: 
            pizza_class = cls._available_pizza_types[pizza_type]()
        return pizza_class
    
    @classmethod
    def get_available_pizza_types(cls) -> dict[str, type[AbsPizza]]: 
        return cls._available_pizza_types