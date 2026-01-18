import copy
from abs_document import AbsDocument

class Contract(AbsDocument): 

    def __init__(self): 
        super().__init__()
        self._party_a = None
        self._party_b = None
        self._terms = None

    def __eq__(self, other):
        if not isinstance(other, Contract):
            return False
        return (
            self._title == other._title and
            self._party_a == other._party_a and
            self._party_b == other._party_b and
            self._terms == other._terms and
            self._content == other._content and
            self._metadata == other._metadata
        )

    def clone(self): 
        return copy.deepcopy(self)
    
    def display(self): 
        print("=== Contract ===")
        print(f"Title: {self._title}")
        print(f"Party A: {self._party_a}")
        print(f"Party B: {self._party_b}")
        print(f"Terms: {self._terms}")
        print(f"Content: {self._content}")
        print(f"Metadata: {self._metadata}")
        print(f"Sections: {self._sections}")
    
    @property
    def party_a(self) -> str: 
        return self._party_a
    
    @party_a.setter
    def party_a(self, party_a: str): 
        self._party_a = party_a
    
    @property
    def party_b(self) -> str: 
        return self._party_b
    
    @party_b.setter
    def party_b(self, party_b: str): 
        self._party_b = party_b
    
    @property
    def terms(self) -> str: 
        return self._terms
    
    @terms.setter
    def terms(self, terms: str):
        self._terms = terms 


