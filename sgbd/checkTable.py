from typing import List
from tableRow import TableRow

class CheckTable():
        def __init__(self) -> None:
                self.__rows : List[TableRow]= []
        def get_row_by_index(self,index):
            return self.__rows[index]

        def get_all_rows(self) -> TableRow:
            return self.__rows
        
        def get_table_len(self) -> int:
            return len(self.__rows)

        def add_row(self,row : TableRow) -> None:
            self.__rows.append(row)

        def remove_where(self, transaction_id : int) -> List[TableRow]:
            removed : List[TableRow]
            for index in range(len(self.__rows)):
                if self.__rows[index].transaction_id == transaction_id:
                    removed.append(self.__rows[index])
                    self.__rows.pop(index)
            return removed














            