import pytest
from pizza_factory import PizzaFactory
from pizzas import NullPizza, PepperoniPizza, MargheritaPizza, VeggiePizza

class TestPizzaFactory: 

    def test_load_veggie_pizza(self): 
        factory = PizzaFactory()
        pizza = factory.create_pizza("veggie")
        assert isinstance(pizza, VeggiePizza)

    def test_load_margherita_pizza(self): 
        factory = PizzaFactory()
        pizza = factory.create_pizza("margherita")
        assert isinstance(pizza, MargheritaPizza)

    def test_load_veggie_pizza(self): 
        factory = PizzaFactory()
        pizza = factory.create_pizza("pepperoni")
        assert isinstance(pizza, PepperoniPizza)

    def test_return_null_for_unknown_pizza(self): 
        factory = PizzaFactory()
        pizza = factory.create_pizza("this_pizza_should_never_exist_123493297923tye98wyf")
        assert isinstance(pizza, NullPizza) 

    