from typing import List
from db_objects import DB_Object

class TableRow():
    def __init__(self, transaction_id : int, lock_type :  int, object :  DB_Object, status : int) -> None:
        self.__transaction_id = transaction_id
        self.__lock_type = lock_type
        self.__object = object
        self.__status = status

    def set_transaction_id(self, transaction_id : int) -> None:
        self.__transaction_id = transaction_id

    def get_transaction_id(self) -> int:
        return self.__transaction_id

    def set_lock_type(self, lock_type : int) -> None:
        self.__lock_type = lock_type

    def get_lock_type(self) -> int:
        return self.__lock_type

    def set_object(self, object : DB_Object) -> None:
        self.__object = object

    def get_object(self) -> DB_Object:
        return self.__object

    def set_status(self, status : int) -> None:
        self.__status = status

    def get_status(self) -> int:
        return self.__status


    

    