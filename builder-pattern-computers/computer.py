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
    cooling_system: str = None
    wifi_card: bool = None
    bluetooth: bool = None

    @classmethod
    def _from_builder(cls, cpu: str, ram: int, storage: int, gpu: str = None, motherboard: str = None, power_supply: int = None, case: str = None, cooling_system: str = None, wifi_card: bool = False, bluetooth: bool = False) -> Computer: 
        return cls(
            cpu=cpu, 
            ram=ram, 
            storage=storage,
            gpu=gpu, 
            motherboard=motherboard, 
            power_supply=power_supply, 
            case=case, 
            cooling_system=cooling_system,
            wifi_card=wifi_card,
            bluetooth=bluetooth
        ) 
       
    def __str__(self) -> str:
        return (
            f"CPU: {self.cpu}\n"
            f"RAM: {self.ram} GB\n"
            f"Storage: {self.storage} GB\n"
            f"GPU: {self.gpu or 'None'}\n"
            f"Motherboard: {self.motherboard or 'None'}\n"
            f"Power Supply: {self.power_supply or 'None'} W\n"
            f"Case: {self.case or 'None'}\n"
            f"Cooling System: {self.cooling_system or 'None'}\n"
            f"WiFi Card: {'Yes' if self.wifi_card else 'No'}\n"
            f"Bluetooth: {'Yes' if self.bluetooth else 'No'}"
        )

    def __repr__(self) -> str:
        return (
            f"Computer(cpu={self.cpu!r}, ram={self.ram}, storage={self.storage}, "
            f"gpu={self.gpu!r}, motherboard={self.motherboard!r}, "
            f"power_supply={self.power_supply!r}, case={self.case!r}, "
            f"cooling_system={self.cooling_system!r}, "
            f"wifi_card={self.wifi_card}, bluetooth={self.bluetooth})"
        )
    