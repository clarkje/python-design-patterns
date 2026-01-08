from abc import ABC

class AbsDocument(ABC): 

    def __init__(self): 
        self._title: str = None
        self._content: str = None
        self._metadata: dict = {}
        self._sections: list = []

    @staticmethod
    def clone(self): 
        pass

    def display(self): 
        pass

    @property
    def title(self) -> str: 
        return self._title
    
    @title.setter
    def title(self, title: str): 
        self._title = title

    @property
    def content(self) -> str: 
        return self._content
    
    @content.setter
    def content(self, content: str): 
        self._content = content

    @property
    def metadata(self) -> str: 
        return self._metadata
    
    @metadata.setter
    def metadata(self, metadata: dict): 
        self._metadata = metadata