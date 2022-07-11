from os import abort
from typing import List
from tableRow import TableRow
from graph import Graph, detect_cycle
import constants

# coisas a fazer:
# adicionar implementações faltantes

class CheckTable():
        def __init__(self, transact_order) -> None:
                self.__rows : List[TableRow]= []
                self.graph: Graph = Graph()
                self.transact_order: List[int] = transact_order
                self.order_counter = 0
        def get_row_by_index(self,index):
            return self.__rows[index]

        def get_all_rows(self) -> TableRow:
            return self.__rows
        
        def get_table_len(self) -> int:
            return len(self.__rows)

        # retorna uma flag true: sem abort, false: ocourreu abort
        def add_row(self,row : TableRow) -> bool:
            curr_lock = row.get_lock_type()
            curr_transaction = row.get_transaction_id()
            if curr_lock == constants.READ_LOCK:
                # implementação do pseudocódigo:
                # ...
                # ...
                # ...
                # checagem de abort
                # ...
                # ...
                self.__rows.append(row)
                # adicionar possiveis bloqueios intencionais
                pass
            elif curr_lock == constants.WRITE_LOCK:
                conflict = False
                conflict_list = []
                # checa se existe um wl(x) ou um cl(x) de outra transação
                # ...
                # ...
                # ...
                if conflict == True:
                    row.set_status(constants.STATUS_WAITING)
                    # checa se a nova transação gera cíclo no grafo de espera 
                    for id in conflict_list:
                        self.graph.addNeigh(curr_transaction, id)
                    # se gerar, transação é abortada: 
                    if detect_cycle(self.graph):
                         # remove a aresta mais recente
                        self.graph.removeNeigh()
                        last_added = self.graph.last_added 
                        newest = max( self.transact_order[last_added[0]], self.transact_order[last_added[1]] )
                        self.remove_where(newest)
                        return False
                else: 
                    row.set_status(constants.STATUS_GRANTED)
                self.__rows.append(row)
                # adicionar possiveis bloqueios intencionais
            elif curr_lock == constants.CERTIFY_LOCK:
                # implementação do pseudocódigo:
                # ...
                # ...
                # ...
                # checagem de abort
                # ...
                # ...
                self.__rows.append(row)
                # adicionar possiveis bloqueios intencionais
                pass
            elif curr_lock == constants.UPDATE_LOCK:
                # implementação do pseudocódigo:
                # ...
                # ...
                # ...
                # checagem de abort
                # ...
                # ...
                self.__rows.append(row)
                # adicionar possiveis bloqueios intencionais
                pass
            elif curr_lock == constants.READ_INTENTIONAL:
                # implementação do pseudocódigo:
                # ...
                # ...
                # ...
                # checagem de abort
                # ...
                # ...
                self.__rows.append(row)
                # adicionar possiveis bloqueios intencionais
                pass
            elif curr_lock == constants.WRITE_INTENTIONAL:
                # implementação do pseudocódigo:
                # ...
                # ...
                # ...
                # checagem de abort
                # ...
                # ...
                self.__rows.append(row)
                # adicionar possiveis bloqueios intencionais
                pass
            elif curr_lock == constants.UPDATE_INTENTIONAL:
                # implementação do pseudocódigo:
                # ...
                # ...
                # ...
                # checagem de abort
                # ...
                # ...
                self.__rows.append(row)
                # adicionar possiveis bloqueios intencionais
                pass
            # caso seja a primeira visita à transação, sua ordem de chegada é anotada:
            if self.transact_order[curr_transaction] == -1:
                self.transact_order[curr_transaction] = self.order_counter
                self.order_counter += 1
            return True

        def remove_where(self, transaction_id : int) -> List[TableRow]:
            removed : List[TableRow]
            row_count = len(self.__rows)
            for index in range(row_count):
                if self.__rows[index].transaction_id == transaction_id:
                    removed.append(self.__rows[index])
                    self.__rows.pop(index)
                    row_count-=1
            return removed














            