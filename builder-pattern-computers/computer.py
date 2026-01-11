from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class Computer(): 

    cpu: str = None
    ram: int = None
    storage: int = None
    gpu: str = None
    motherboard: str = None
    power_supply: int = None
    case: str = None
    cooling: str = None
    wifi_card: bool = None
    bluetooth: bool = None
    
    @classmethod
    def _from_builder(cls, cpu: str, ram: int, storage: int, gpu: str = None, motherboard: str = None, power_supply: int = None, case: str = None, cooling_system: str = None, wifi_card: bool = False, bluetooth: bool = False): 
        cls.cpu: str = cpu
        cls.ram: int = ram
        cls.storage: int = storage
        cls.gpu: str = gpu
        cls.motherboard: str = motherboard
        cls.power_supply: int = power_supply
        cls.case: str = case
        cls.cooling: str = cooling_system
        cls.wifi_card: bool = wifi_card
        cls.bluetooth: bool = bluetooth
   
    @classmethod
    def __str__(cls): 
        output = f"""   CPU: {cls.cpu}
        RAM: {cls.ram} GB
        Storage: {cls.storage} GB   
        GPU: {cls.gpu}
        Motherboard: {cls.motherboard}   
        PSU: {cls.power_supply} W
        Case: {cls.case}
        Cooling System: {cls.cooling}
        WiFi Card: {'Yes' if cls.wifi_card else 'No'}
        Bluetooth: {'Yes' if cls.bluetooth else 'No'}
        """
        return output
        
    def __repr__(cls): 
        output = f"""   CPU: {cls.cpu}
        RAM: {cls.ram} GB
        Storage: {cls.storage} GB   
        GPU: {cls.gpu}
        Motherboard: {cls.motherboard}   
        PSU: {cls.power_supply} W
        Case: {cls.case}
        Cooling System: {cls.cooling}
        WiFi Card: {'Yes' if cls.wifi_card else 'No'}
        Bluetooth: {'Yes' if cls.bluetooth else 'No'}
        """
        return output
    