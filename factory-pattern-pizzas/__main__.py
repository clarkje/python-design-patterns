from pizzas import loader

for pizza_type in 'margherita_pizza', 'pepperoni_pizza': 
    pizza = loader.create_pizza(pizza_type)
    pizza.name = pizza_type
    print(f"{pizza.name}")
    print(pizza.prepare())
    print(pizza.bake())
    print(pizza.cut())
    print(pizza.box())
