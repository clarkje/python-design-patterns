from abc import ABC, abstractmethod

class AbsDocument(ABC): 

    def __init__(self): 
        self._title: str = None
        self._content: str = None
        self._metadata: dict = None
        self._sections: list = None

    @abstractmethod
    def clone(self): 
        pass

    @abstractmethod
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
    def metadata(self) -> dict: 
        return self._metadata
    
    @metadata.setter
    def metadata(self, metadata: dict): 
        self._metadata = metadata

    @property
    def sections(self) -> list: 
        return self._sections
    
    @sections.setter
    def sections(self, sections: list) -> None: 
        self._sections = sections