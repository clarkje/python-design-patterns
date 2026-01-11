# Factory Pattern Implementation - Code Review

## Overall Assessment

The implementation demonstrates a creative approach using dynamic module loading, but there are several areas that need improvement to better align with the Factory Pattern requirements and Python best practices.

---

## 🎯 Design Pattern Issues

### 1. **Factory Pattern Implementation**

**Issue**: The current implementation uses dynamic module loading (`importlib`) rather than a traditional Factory Pattern. While functional, this doesn't match the assignment requirements which ask for a `PizzaFactory` class with a `create_pizza()` method.

**Current Approach**:
- Uses `loader.create_pizza()` with dynamic imports
- Discovers classes at runtime using introspection

**Recommended Approach**:
```python
class PizzaFactory:
    _pizza_types = {
        'margherita_pizza': MargheritaPizza,
        'pepperoni_pizza': PepperoniPizza,
        'veggie_pizza': VeggiePizza,
    }
    
    @classmethod
    def create_pizza(cls, pizza_type: str) -> AbsPizza:
        pizza_class = cls._pizza_types.get(pizza_type)
        if pizza_class is None:
            raise ValueError(f"Unknown pizza type: {pizza_type}")
        return pizza_class()
    
    @classmethod
    def get_available_pizzas(cls) -> list[str]:
        return list(cls._pizza_types.keys())
```

**Why**: 
- More explicit and maintainable
- Better error handling (raises exception as required)
- Easier to understand and debug
- Supports the bonus challenge (`get_available_pizzas()`)

---

## 🐛 Code Quality Issues

### 2. **Abstract Base Class Issues**

**File**: `pizzas/abs_pizza.py`

**Issues**:
- Semicolons after `pass` statements (lines 11, 16, 23, 30, 37, 44) - unnecessary in Python
- Property setter decorator issue: The `@name.setter` decorator should not be abstract. Abstract setters don't work the same way as abstract methods.

**Fix**:
```python
@property
@abc.abstractmethod
def name(self) -> str:
    """Get the pizza name."""
    pass

@name.setter
def name(self, value: str) -> None:
    """Set the pizza name."""
    pass  # Concrete classes can override if needed
```

**Better Approach**: Consider making `name` a concrete property in the base class:
```python
class AbsPizza(metaclass=abc.ABCMeta):
    def __init__(self):
        self._name = None
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        self._name = value
```

---

### 3. **Inconsistent Name Initialization**

**Issue**: 
- `MargheritaPizza` and `PepperoniPizza` initialize `_name = None`
- `VeggiePizza` initializes `_name = "Veggie Pizza"`
- `__main__.py` sets the name after creation: `pizza.name = pizza_type`

**Problem**: This inconsistency makes the code harder to maintain and understand.

**Recommendation**: 
- Either initialize all pizzas with their proper names in `__init__`
- Or remove name initialization and always set it via the property
- Consider making name a required constructor parameter

---

### 4. **NullPizza Implementation Issues**

**File**: `pizzas/null_pizza.py`

**Issues**:
- Methods use `print()` instead of returning strings (inconsistent with other pizzas)
- The assignment requires methods to "print" but the other pizzas return strings
- `prepare()`, `bake()`, `cut()`, `box()` should return strings for consistency

**Fix**:
```python
def prepare(self) -> str:
    return f"Pizza Type {self._pizza_type} not Found"

def bake(self) -> str:
    return f"Pizza Type {self._pizza_type} not found"

def cut(self) -> str:
    return f"Pizza Type {self._pizza_type} not found"

def box(self) -> str:
    return f"Pizza Type {self._pizza_type} not found"
```

**Note**: The assignment says methods should "print", but returning strings is more flexible and testable. Consider clarifying the requirement or documenting the design choice.

---

### 5. **String Formatting Issues**

**Files**: All pizza classes

**Issue**: Inconsistent use of f-strings and string concatenation.

**Examples**:
- Line 33 in `margherita_pizza.py`: `return(f"Preparation Instructions\n {self._prep_instructions}")`
- Line 39: `return(f"Cutting Instructions: {self._cut_instructions}")`

**Fix**: Remove unnecessary parentheses around f-strings:
```python
return f"Preparation Instructions\n {self._prep_instructions}"
```

---

### 6. **Typo in Instructions**

**Files**: `margherita_pizza.py`, `pepperoni_pizza.py`

**Issue**: "handfulls" should be "handfuls" (line 9 in both files)

---

### 7. **Missing Type Hints**

**Issue**: The code lacks type hints, which are considered best practice in modern Python.

**Recommendation**: Add type hints throughout:
```python
def create_pizza(pizza_type: str) -> AbsPizza:
    ...
```

---

## 🧪 Testing Issues

### 8. **Test Structure**

**Files**: `tests/pizzas/test_loader.py`, `tests/pizzas/test_veggie_pizza.py`

**Issues**:
- Tests are written as classes but don't use pytest's class-based test structure properly
- Should use `pytest` fixtures or `pytest` test functions
- Assertions are written incorrectly: `assert(isinstance(pizza, VeggiePizza)) == True` should be `assert isinstance(pizza, VeggiePizza)`

**Current**:
```python
class TestLoader:
    def test_load_veggie_pizza(self):
        pizza = loader.create_pizza("veggie_pizza")
        assert(isinstance(pizza, VeggiePizza)) == True
```

**Recommended**:
```python
import pytest
from pizzas import loader
from pizzas.veggie_pizza import VeggiePizza

def test_load_veggie_pizza():
    pizza = loader.create_pizza("veggie_pizza")
    assert isinstance(pizza, VeggiePizza)

def test_load_margherita_pizza():
    pizza = loader.create_pizza("margherita_pizza")
    assert isinstance(pizza, MargheritaPizza)

def test_return_null_for_unknown_pizza():
    pizza = loader.create_pizza("unknown_pizza_type")
    assert isinstance(pizza, NullPizza)
```

**Or using pytest classes**:
```python
class TestLoader:
    def test_load_veggie_pizza(self):
        pizza = loader.create_pizza("veggie_pizza")
        assert isinstance(pizza, VeggiePizza)
```

---

### 9. **Test Coverage**

**Missing Tests**:
- Test for `pepperoni_pizza`
- Test for error handling (if using exceptions instead of NullPizza)
- Test for all pizza methods (prepare, bake, cut, box) for each pizza type
- Integration test in `__main__.py`

---

## 📋 Assignment Requirements Compliance

### ✅ Met Requirements:
- ✅ Base class with abstract methods
- ✅ Three concrete pizza classes
- ✅ Factory function to create pizzas
- ✅ Handles unknown pizza types (via NullPizza)
- ✅ Tests included

### ❌ Missing/Incomplete:
- ❌ Factory should be a class (requirement says "PizzaFactory")
- ❌ Should raise exception for unknown types (currently returns NullPizza)
- ❌ Methods should "print" according to requirements (currently return strings)

---

## 🎁 Bonus Challenges

### Not Implemented:
- ❌ `get_available_pizzas()` method
- ❌ Pricing and `get_price()` method
- ❌ Regional factory variants

---

## 🔧 Specific Recommendations

### Priority 1 (Critical):
1. **Refactor to use a proper Factory class** instead of dynamic loading
2. **Fix NullPizza methods** to return strings consistently
3. **Fix test assertions** to use proper pytest syntax
4. **Add exception handling** for unknown pizza types (as per requirements)

### Priority 2 (Important):
5. **Remove semicolons** from abstract base class
6. **Fix property setter** in abstract class
7. **Standardize name initialization** across all pizza classes
8. **Add type hints** throughout the codebase

### Priority 3 (Nice to have):
9. **Fix typos** ("handfulls" → "handfuls")
10. **Remove unnecessary parentheses** around f-strings
11. **Add docstrings** to classes and methods
12. **Implement bonus challenges**

---

## 📝 Example Refactored Factory

Here's how a proper Factory Pattern implementation might look:

```python
# pizzas/pizza_factory.py
from typing import Dict, Type
from .abs_pizza import AbsPizza
from .margherita_pizza import MargheritaPizza
from .pepperoni_pizza import PepperoniPizza
from .veggie_pizza import VeggiePizza


class PizzaFactory:
    """Factory for creating pizza instances."""
    
    _pizza_types: Dict[str, Type[AbsPizza]] = {
        'margherita_pizza': MargheritaPizza,
        'pepperoni_pizza': PepperoniPizza,
        'veggie_pizza': VeggiePizza,
    }
    
    @classmethod
    def create_pizza(cls, pizza_type: str) -> AbsPizza:
        """
        Create a pizza instance based on the pizza type.
        
        Args:
            pizza_type: String identifier for the pizza type
            
        Returns:
            An instance of the requested pizza type
            
        Raises:
            ValueError: If the pizza type is not recognized
        """
        pizza_class = cls._pizza_types.get(pizza_type.lower())
        if pizza_class is None:
            raise ValueError(f"Unknown pizza type: {pizza_type}")
        return pizza_class()
    
    @classmethod
    def get_available_pizzas(cls) -> list[str]:
        """Return a list of all available pizza types."""
        return list(cls._pizza_types.keys())
```

---

## 🎓 Learning Points

1. **Factory Pattern**: Should use a centralized factory class that maps types to classes, not dynamic discovery
2. **Error Handling**: Requirements specify raising exceptions, not returning null objects
3. **Testing**: Use pytest's assertion syntax properly
4. **Consistency**: Keep method signatures and return types consistent across implementations
5. **Python Style**: Remove semicolons, use proper type hints, follow PEP 8

---

## Summary

The implementation shows good understanding of Python's dynamic capabilities and abstract base classes. However, to better align with the Factory Pattern and assignment requirements, consider:

1. Implementing a traditional Factory class
2. Raising exceptions for unknown types
3. Fixing test structure and assertions
4. Improving code consistency and quality

The dynamic loading approach is interesting but adds unnecessary complexity for this use case.

