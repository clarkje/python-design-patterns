from typing import Self
from computer import Computer

class ComputerBuilder(): 
    
    def __init__(self): 
        self._cpu: str = None
        self._ram: int = None
        self._storage: int = None
        self._gpu: str = None
        self._motherboard: str = None
        self._psu: int = None
        self._case: str = None
        self._cooling: str = None
        self._wifi_card: bool = False
        self._bluetooth: bool = False

    def build(self) -> Computer:
        if None in (self._cpu, self._ram, self._storage):
            raise TypeError("CPU, RAM and Storage are required properties") 
        
        return Computer._from_builder(
            self._cpu,
            self._ram, 
            self._storage, 
            self._gpu, 
            self._motherboard, 
            self._psu, 
            self._case, 
            self._cooling, 
            self._wifi_card, 
            self._bluetooth
        )

    def reset(self) -> None: 
        self.__init__()

    def get_cpu(self): 
        return self._cpu

    def set_cpu(self, cpu: str) -> Self: 
        self._cpu = cpu
        return self

    def get_ram(self): 
        return self._ram
    
    def set_ram(self, ram_gb: int) -> Self: 
        self._ram = ram_gb
        return self
        
    def get_storage(self):
        return self._storage

    def set_storage(self, storage_gb: int) -> Self: 
        self._storage = storage_gb
        return self

    def get_gpu(self): 
        return self._gpu

    def set_gpu(self, gpu: str) -> Self: 
        self._gpu = gpu
        return self

    def get_motherboard(self): 
        return self._motherboard
    
    def set_motherboard(self, motherboard: str) -> Self: 
        self._motherboard = motherboard
        return self

    def get_psu(self): 
        return self._psu
    
    def set_psu(self, psu_watts: int) -> Self: 
        self._psu = psu_watts
        return self

    def get_case(self): 
        return self._case

    def set_case(self, case: str) -> Self: 
        self._case = case
        return self

    def get_cooling(self): 
        return self._cooling

    def set_cooling(self, cooling: str) -> Self: 
        self._cooling = cooling
        return self

    def get_wifi_card(self): 
        return self._wifi_card
    
    def set_wifi_card(self, wifi_card: bool = True) -> Self:
        self._wifi_card = wifi_card
        return self
    
    def get_bluetooth(self): 
        return self._bluetooth
    
    def set_bluetooth(self, bluetooth: bool = True) -> Self: 
        self._bluetooth = bluetooth
        return self