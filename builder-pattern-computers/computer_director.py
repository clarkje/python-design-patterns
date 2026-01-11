from computer import Computer
from computer_builder import ComputerBuilder

class ComputerDirector(): 

    @staticmethod
    def build_gaming_pc() -> Computer:
        computer = (ComputerBuilder()
                    .set_cpu("Intel 9000+")
                    .set_ram(32)
                    .set_storage(1000)
                    .set_gpu("NVIDIA RDX 8040")
                    .set_wifi_card(True)
                    .build())
        return computer        

    @staticmethod
    def build_office_pc() -> Computer: 
        computer = (ComputerBuilder()
                    .set_cpu("Intel Celeron")
                    .set_ram(32)
                    .set_storage(1000)
                    .set_wifi_card(True)
                    .set_bluetooth(True)
                    .build())
        return computer        
    
    @staticmethod
    def build_workstation() -> Computer:
        computer = (ComputerBuilder()
                    .set_cpu("ESP32")
                    .set_ram(1293240187)
                    .set_storage(100142359789870)
                    .set_gpu("NVIDIA RDX 100000000")
                    .set_wifi_card(True)
                    .set_bluetooth(False)
                    .build())
        return computer        
