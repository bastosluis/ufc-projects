from abc import ABC
from typing import List
import constants
from db_objects import DB_Object

class Operation(ABC):
    def __init__(self, transaction_id: int, operand: str, granulosity : DB_Object=None):
        self.transaction_id = transaction_id
        self.operand = operand
        self.granulosity = granulosity
    def __str__(self):
        return f'T{self.transaction_id}: {self.__class__.__name__}({self.operand})'

class Read(Operation):
    def __init__(self, transaction_id: int, operand: str, granulosity : DB_Object):
        super().__init__(transaction_id, operand, granulosity)
        self.lock_type=constants.READ_LOCK

class Write(Operation):
    def __init__(self, transaction_id: int, operand: str, granulosity : DB_Object):
        super().__init__(transaction_id, operand, granulosity)
        self.lock_type=constants.WRITE_LOCK

class Update(Operation):
    def __init__(self, transaction_id: int, operand: str, granulosity : DB_Object):
        super().__init__(transaction_id, operand, granulosity)
        self.lock_type=constants.UPDATE_LOCK

class Commit(Operation):
    def __init__(self, transaction_id: int, operand: str=None):
        super().__init__(transaction_id, operand)
        self.lock_type=constants.CERTIFY_LOCK