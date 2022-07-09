from abc import ABC
from typing import List
import operations as op

class DB_Object(ABC):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Tuple(DB_Object):
    def __init__(self, id: int, name: str, value_list: List[int]=None):
        super().__init__(id, name)
        self.value_list = value_list

class Page(DB_Object):
    def __init__(self, id: int, name: str, tuple_list: List[Tuple]=None):
        super().__init__(id, name)
        self.tuple_list = tuple_list

class Table(DB_Object):
    def __init__(self, id: int, name: str, page_list: List[Page]=None):
        super().__init__(id, name)
        self.page_list = page_list
    def __str__(self):
        string = f'Table {self.name} (id: {self.id}):'
        for i in range(len(self.page_list)):
            curr_page = self.page_list[i]
            string += f'\n{curr_page.name}: has {len(curr_page.tuple_list)} tuples'
        return string