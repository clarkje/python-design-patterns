from collections import namedtuple
from documents.abs_document import AbsDocument

'''
Stores prototype instances by name 
Provides methods to register and retrieve (clone) prototypes 
Handles both shallow and deep copy scenarios appropriately
'''

class DocumentRegistry():

    def __init__(self): 
        self._registry: dict[str, AbsDocument] = {} 

    def add(self, key: str, prototype: AbsDocument) -> None: 
        if isinstance(prototype, AbsDocument): 
            if not key in self._registry:
                self._registry[key] = prototype

    def get(self, key: str) -> AbsDocument: 
        return self._registry[key].clone()
    
