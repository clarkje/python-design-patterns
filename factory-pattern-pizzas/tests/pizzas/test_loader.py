from pizzas import loader
from pizzas.null_pizza import NullPizza
from pizzas.veggie_pizza import VeggiePizza
from pizzas.margherita_pizza import MargheritaPizza

class TestLoader: 

    def test_load_veggie_pizza(self): 
        pizza = loader.create_pizza("veggie_pizza")
        assert(isinstance(pizza, VeggiePizza)) == True

    def test_load_margherita_pizza(self): 
        pizza = loader.create_pizza("margherita_pizza")
        assert(isinstance(pizza, MargheritaPizza)) == True

    def test_return_null_for_unknown_pizza(self): 
        pizza = loader.create_pizza("this_pizza_should_never_exist_123493297923tye98wyf")
        assert(isinstance(pizza, NullPizza)) == True

    