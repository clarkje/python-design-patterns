from pizza_factory import PizzaFactory
from pizzas.abs_pizza import AbsPizza

class TestVeggiePizza: 

    def setup_method(self): 
        self.vp = PizzaFactory.create_pizza("veggie")

    def test_name_property(self): 
        assert self.vp.name == "Veggie Pizza"

    def test_is_instance_of_abs_pizza(self): 
        assert issubclass(self.vp.__class__, AbsPizza)

    # These asserts are pointless in practice, here for the exercise of including unit tests with the implementation

    def test_prepare(self): 
        vp = self.vp
        assert vp.prepare() == f"Preparation Instructions\n {vp._prep_instructions}"

    def test_cut(self):
        vp = self.vp 
        assert vp.cut() == f"Cutting Instructions: {vp._cut_instructions}"

    def test_bake(self):
        vp = self.vp 
        assert vp.bake() == f"Baking Instructions\n {vp._bake_instructions}"

    def test_box(self): 
        vp = self.vp
        assert vp.box() == f"Boxing Instructions: {vp._box_instructions}"