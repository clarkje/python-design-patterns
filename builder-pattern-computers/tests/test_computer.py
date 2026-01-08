import pytest
from computer import Computer

class TestComputer(): 

    def test_gpu_setter(self): 
        c = Computer()
        c.add_gpu("Test")
        assert(c.gpu == "Test")

