from computer import Computer
from computer_builder import ComputerBuilder

class ComputerDirector(): 

    def __init__(self): 
        pass

    def build_gaming_pc(self, builder: ComputerBuilder) -> Computer:
        computer = (builder
                    .set_cpu("Intel 9000+")
                    .set_ram(32)
                    .set_storage(1000)
                    .set_gpu("NVIDIA RDX 8040")
                    .set_wifi_card(True)
                    .build())
        return computer        

    def build_office_pc(self, builder: ComputerBuilder) -> Computer: 
        computer = (builder
                    .set_cpu("Intel Celeron")
                    .set_ram(32)
                    .set_storage(1000)
                    .set_wifi_card(True)
                    .set_bluetooth(True)
                    .build())
        return computer        
    
    def build_workstation(self, builder: ComputerBuilder) -> Computer:
        computer = (builder
                    .set_cpu("ESP32")
                    .set_ram(1293240187)
                    .set_storage(100142359789870)
                    .set_gpu("NVIDIA RDX 100000000")
                    .set_wifi_card(True)
                    .set_bluetooth(False)
                    .build())
        return computer        
