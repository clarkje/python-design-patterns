import copy
from datetime import datetime, date
from .abs_document import AbsDocument

class Report(AbsDocument): 

    def __init__(self): 
        super().__init__()
        self._date: datetime = None
        self._data_points: list = []
        self._author: str = None

    def clone(self): 
        return copy.deepcopy(self)
    
    def display(self): 
        print("=== Report ===")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Content: {self.content}")
        print(f"Metadata: {self.metadata}")
        print(f"Sections: {self.sections}")
        if isinstance(self.date, date): 
            print(f"Date: {self.date.strftime('%Y-%m-%d')}")
        print(f"Data Points: {self.data_points}")

    @property
    def author(self) -> str: 
        return self._author
    
    @author.setter
    def author(self, author: str) -> None: 
        self._author = author   

    @property
    def date(self) -> datetime: 
        return self._date
    
    @date.setter
    def date(self, timestamp: datetime.datetime = None) -> None: 
        self._date = timestamp or datetime.datetime.now()

    @property
    def data_points(self) -> list: 
        return self._data_points
    
    @data_points.setter
    def data_points(self, data_points: list) -> None: 
        self._data_points = data_points