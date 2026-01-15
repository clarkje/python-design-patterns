import copy
from .abs_document import AbsDocument

class Invoice(AbsDocument): 

    def __init__(self): 
        super().__init__()
        self._invoice_number: int = None
        self._items: list[dict] = []
        self._total: float = None

    def clone(self): 
        return copy.deepcopy(self)

    def display(self): 
        #TODO: Print out all object properties
        print("Displaying Invoice")

    @property
    def invoice_number(self) -> int: 
        return self._invoice_number
    
    @invoice_number.setter
    def invoice_number(self, invoice_number: int) -> None: 
        self._invoice_number: int = invoice_number

    @property
    def items(self) -> list[dict]: 
        return self._items
    
    @items.setter
    def items(self, items: list[dict]) -> None: 
        self._items = items

    @property
    def total(self) -> float: 
        return self._total
    
    @total.setter
    def total(self, total: float) -> None: 
        self._total = total