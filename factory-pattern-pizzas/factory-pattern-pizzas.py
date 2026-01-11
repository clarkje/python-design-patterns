import argparse
from pizza_factory import PizzaFactory
from pizzas import NullPizza, MargheritaPizza, PepperoniPizza, VeggiePizza

parser = argparse.ArgumentParser(prog="factory-pattern-pizzas.py", description="Demonstrative implementation of the factory pattern in Python 3")
parser.add_argument("-pizza",type=str,help="Choose from the available pizza types: <margherita|pepperoni|veggie>)")
parser.add_argument("-all",action="store_true",help="Exercise all available pizza types")
args = parser.parse_args()

def print_pizza(pizza_type):
    factory = PizzaFactory()
    pizza = factory.create_pizza(pizza_type)
    print(f"{pizza.__class__.__name__}")
    
    for operation in [pizza.prepare, pizza.bake, pizza.cut, pizza.box]:      
        try:
            print(operation())
        except ValueError: 
            if isinstance(pizza, NullPizza): 
                print("Invoking this operation on NullPizza threw a ValueError as expected.")

## Main ##

if args.pizza is not None: 
    print_pizza(args.pizza.lower())
elif args.all is True: 
    for pizza_type in ["margherita", "pepperoni", "veggie", "undefined"]: 
        print_pizza(pizza_type)
else: 
    parser.print_usage()
