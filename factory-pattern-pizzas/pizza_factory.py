from pizzas import MargheritaPizza, PepperoniPizza, VeggiePizza, NullPizza, AbsPizza

class PizzaFactory:

    _available_pizza_types = {"margherita": MargheritaPizza, "pepperoni": PepperoniPizza, "veggie": VeggiePizza}

    @classmethod
    def create_pizza(self, pizza_type: str) -> AbsPizza: 
        print(f"Pizza Type: {pizza_type}")
        if pizza_type not in self._available_pizza_types:
            pizza_class = NullPizza(pizza_type)
        else: 
            pizza_class = self._available_pizza_types[pizza_type]()
        return pizza_class
    
    @property
    def available_pizza_types(self): 
        return self._available_pizza_types