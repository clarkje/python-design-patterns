class Computer(): 

    def __init__(): 
        self.cpu: str = None
        self.ram: int = None
        self.storage: int = None
        self.gpu: str = None
        self.motherboard: str = None
        self.psu: int = None
        self.case: str = None
        self.cooling: str = None
        self.wifi_card: bool = None
        self.bluetooth: bool = None

    def __init__(self, cpu: str, ram: int, storage: int, gpu: str = None, motherboard: str = None, psu: int = None, case: str = None, cooling_system: str = None, wifi_card: bool = False, bluetooth: bool = False): 
        self.cpu: str = cpu
        self.ram: int = int
        self.storage: int = storage
        self.gpu: str = gpu
        self.motherboard: str = motherboard
        self.psu: int = psu
        self.case: str = case
        self.cooling: str = cooling_system
        self.wifi_card: bool = wifi_card
        self.bluetooth: bool = bluetooth
   
    def __str__(self): 
        output = f"CPU: {self.cpu}"
        output += f"RAM: {self.ram} GB"
        output += f"Storage: {self.storage} GB"    
        output += f"GPU: {self.gpu}"
        output += f"Motherboard: {self.motherboard}"   
        output += f"PSU: {self.psu} W"
        output += f"Case: {self.case}"
        output += f"Cooling System: {self.cooling}"
        output += f"WiFi Card: {'Yes' if self.wifi_card else 'No'}"
        output += f"Bluetooth: {'Yes' if self.bluetooth else 'No'}"
        return output
        
    def __repr__(self): 
        print(f"CPU: {self.cpu}")
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB")    
        print(f"GPU: {self.gpu}")
        print(f"Motherboard: {self.motherboard}")   
        print(f"PSU: {self.psu} W")
        print(f"Case: {self.case}")
        print(f"Cooling System: {self.cooling}")
        print(f"WiFi Card: {'Yes' if self.wifi_card else 'No'}")
        print(f"Bluetooth: {'Yes' if self.bluetooth else 'No'}")
    