# Factory Pattern Practice Assignment

## Scenario: Pizza Restaurant Order System

You're building an order system for a pizza restaurant that needs to create different types of pizzas based on customer orders.

## Your Task

Implement the Factory Pattern to create a pizza ordering system with the following requirements:

### 1. Create a Pizza base class (or protocol)

All pizzas should have:
- A name attribute
- A prepare() method that prints preparation steps
- A bake() method that prints baking information
- A cut() method that prints cutting style
- A box() method that prints boxing information

### 2. Create concrete Pizza classes
Implement at least three pizza types:
- MargheritaPizza: Simple cheese and tomato
- PepperoniPizza: With pepperoni toppings
- VeggiePizza: With various vegetables

Each should implement the methods with unique messages appropriate to that pizza type.

### 3. Create a PizzaFactory
Implement a factory class with a create_pizza(pizza_type: str) method that:
- Takes a string indicating the pizza type
- Returns the appropriate pizza object
- Raises an exception for unknown pizza types

### 4. Test your implementation
Write code that:
- Creates several different pizzas using the factory
- Calls all methods on each pizza to simulate the full preparation process
- Handles invalid pizza type requests gracefully

### Bonus Challenges
- Add a get_available_pizzas() method to your factory that returns a list of all pizza types
- Add pricing to each pizza and a get_price() method
- Extend with a second factory for different restaurant locations with regional pizza varieties