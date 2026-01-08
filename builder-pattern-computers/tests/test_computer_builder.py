import pytest
from computer import Computer
from computer_builder import ComputerBuilder

class TestComputerBuilder(): 

    def test_gpu_setter(self): 
        cb = ComputerBuilder()
        cb.set_gpu("Test")
        assert(cb._gpu == "Test")

    def test_cpu_setter(self): 
        cb = ComputerBuilder()
        cb.set_cpu("i386")
        assert(cb._cpu=="i386")

    def test_ram_setter(self): 
        cb = ComputerBuilder()
        cb.set_ram(12345)
        assert(cb._ram==12345)

    def test_storage_setter(self): 
        cb = ComputerBuilder()
        cb.set_storage(1234)
        assert(cb._storage==1234)

    def test_gpu(self): 
        cb = ComputerBuilder()
        cb.set_gpu("Nvidia 849230x")
        assert(cb._gpu=="Nvidia 849230x")

    def test_motherboard(self): 
        cb = ComputerBuilder()
        cb.set_motherboard("Testing")
        assert(cb._motherboard=="Testing")

    def test_psu(self): 
        cb = ComputerBuilder()
        cb.set_psu(999)
        assert(cb._psu==999)

    def test_case(self):
        cb = ComputerBuilder()
        cb.set_case("All The Lights")
        assert(cb._case=="All The Lights")

    def test_cooling(self):
        cb = ComputerBuilder()
        cb.set_cooling("CoolerMaster")
        assert(cb._cooling=="CoolerMaster")

    def test_wifi(self): 
        cb = ComputerBuilder()
        cb.set_wifi_card()
        assert(cb._wifi_card==True)

    def test_bluetooth(self): 
        cb = ComputerBuilder()
        cb.set_bluetooth()
        assert(cb._bluetooth==True)

    def test_chained_complete_creation(self): 
        cb = ComputerBuilder()
        cb.set_gpu("gpu").set_cpu("cpu").set_ram(123).set_storage(321).set_motherboard("mb").set_case("test_case").set_psu(800).set_bluetooth().set_wifi_card()
        assert cb._gpu=="gpu"
        assert cb._cpu=="cpu"
        assert cb._ram==123
        assert cb._storage==321
        assert cb._motherboard=="mb"
        assert cb._case=="test_case"
        assert cb._psu==800
        assert cb._bluetooth==True
        assert cb._wifi_card==True

    def test_only_mandatory_properties(self): 
        cb = ComputerBuilder()
        cb.set_gpu("gpu").set_cpu("cpu").set_ram(123)
        assert cb._gpu=="gpu"
        assert cb._cpu=="cpu"
        assert cb._ram==123

    def test_missing_mandatory_properties(self): 
        cb = ComputerBuilder()
        with pytest.raises(TypeError): 
            cb.build()

        cb.set_cpu("test-cpu")
        with pytest.raises(TypeError): 
            cb.build()

        cb.set_ram(123)
        with pytest.raises(TypeError):
            cb.build()

        # All required params present
        cb.set_storage(987)
        assert isinstance(cb.build(), Computer)

        # Remove one of the required params
        cb.set_cpu(None)
        with pytest.raises(TypeError): 
            cb.build()

        # An an optional param, for funsies
        cb.set_gpu("test-gpu")
        with pytest.raises(TypeError): 
            cb.build()
