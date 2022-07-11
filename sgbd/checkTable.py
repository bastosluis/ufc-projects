from typing import List
from tableRow import TableRow
from graph import Graph, detect_cycle
import constants

# coisas a fazer:
# adicionar implementações faltantes
# adicionar o Xn ao final das implementações

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

        def check_abort(self, id, conflict_list) -> bool:
            # checa se a nova transação gera cíclo no grafo de espera 
            for k in conflict_list:
                self.graph.addNeigh(id, k)
            # se gerar, transação deve ser abortada: 
            return detect_cycle(self.graph)
                 
        def abort_newest(self):
            # remove a aresta mais recente com a transação:
            self.graph.removeNeigh()
            last_added = self.graph.last_added 
            newest = max( self.transact_order[(last_added[0].label)-1], self.transact_order[(last_added[1].label)-1] )
            self.remove_where(newest)

        # retorna uma flag true: sem abort, false: ocourreu abort
        def add_row(self,row : TableRow) -> bool:
            curr_lock = row.get_lock_type()
            curr_transaction = row.get_transaction_id()


            if curr_lock == constants.READ_LOCK:
                conflict = False
                conflict_list = []
                for i in self.get_all_rows():
                    # checa se existe cl(x) de outra transação
                    if i.get_transaction_id() != curr_transaction and (i.get_lock_type() == constants.CERTIFY_LOCK) and i.get_object() == row.get_object():
                        conflict = True
                        conflict_list.append(i.get_transaction_id())
                if conflict == True:
                    row.set_status(constants.STATUS_WAITING)
                    # checa se a nova transação gera cíclo no grafo de espera 
                    if self.check_abort(curr_transaction, conflict_list):
                        print(f'ciclo encontrado com a adição de T{curr_transaction}')
                         # remove a aresta mais recente
                        self.abort_newest()
                        return False
                else: 
                    row.set_status(constants.STATUS_GRANTED)
                self.__rows.append(row)
                # adicionar possiveis bloqueios intencionais

                
            elif curr_lock == constants.WRITE_LOCK:
                conflict = False
                conflict_list = []
                # checa se existe um wl(x) ou um cl(x) de outra transação
                for i in self.get_all_rows():
                    if i.get_transaction_id() != curr_transaction and (i.get_lock_type() == constants.WRITE_LOCK or i.get_lock_type() == constants.CERTIFY_LOCK) and i.get_object() == row.get_object():
                        conflict = True
                        conflict_list.append(i.get_transaction_id())
                if conflict == True:
                    row.set_status(constants.STATUS_WAITING)
                    # checa se a nova transação gera cíclo no grafo de espera 
                    if self.check_abort(curr_transaction, conflict_list):
                        print(f'ciclo encontrado com a adição de T{curr_transaction}')
                         # remove a aresta mais recente
                        self.abort_newest()
                        return False
                else: 
                    row.set_status(constants.STATUS_GRANTED)
                self.__rows.append(row)
                # adicionar possiveis bloqueios intencionais


            elif curr_lock == constants.CERTIFY_LOCK:
                conflict = False
                conflict_list = []
                # recebe c_i: para todo wl_i(x) checa se existe um rl_k(x)
                for i in self.get_all_rows():
                    if i.get_transaction_id() == curr_transaction and i.get_lock_type() == constants.WRITE_LOCK:
                        for k in self.get_all_rows():
                            if k.get_transaction_id() != curr_transaction and k.get_lock_type() == constants.READ_LOCK and i.get_object() == k.get_object():
                                conflict = True
                                conflict_list.append(k.get_transaction_id())
                if conflict == True:
                    row.set_status(constants.STATUS_WAITING)
                    # checa se a nova transação gera cíclo no grafo de espera 
                    if self.check_abort(curr_transaction, conflict_list):
                        print(f'ciclo encontrado com a adição de T{curr_transaction}')
                         # remove a aresta mais recente
                        self.abort_newest()
                        return False
                else: 
                    row.set_status(constants.STATUS_GRANTED)
                self.__rows.append(row)
                # adicionar possiveis bloqueios intencionais


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
            if self.transact_order[curr_transaction-1] == -1:
                self.transact_order[curr_transaction-1] = self.order_counter
                self.order_counter += 1
            return True

        def remove_where(self, transaction_id : int) -> List[TableRow]:
            removed : List[TableRow] = []
            for index in range(len(self.__rows)):
                if self.__rows[index].get_transaction_id() == transaction_id:
                    removed.append(self.__rows[index])
                    self.__rows.pop(index)
            return removed














            