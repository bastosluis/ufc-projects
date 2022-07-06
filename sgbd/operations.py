from abc import ABC
from typing import List

class Operation(ABC):
    def __init__(self, transaction_id: int, operand: str):
        self.transaction_id = transaction_id
        self.operand = operand
    def __str__(self):
        return f'T{self.transaction_id}: {self.__class__.__name__}({self.operand})'

class Read(Operation):
    def __init__(self, transaction_id: int, operand: str):
        super().__init__(transaction_id, operand)

class Write(Operation):
    def __init__(self, transaction_id: int, operand: str):
        super().__init__(transaction_id, operand)

class Commit(Operation):
    def __init__(self, transaction_id: int, operand: str=None):
        super().__init__(transaction_id, operand)