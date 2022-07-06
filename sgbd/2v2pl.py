import numpy as np
from abc import ABC
from typing import List

VALID_OP = ['r', 'w', 'c']
READ_LOCK = 0
WRITE_LOCK = 1
CERTIFY_LOCK = 2

def parse(raw_tokens: List[str]):
    op_list: List[Operation] = []
    transaction_num_order: List[int] = []
    for token in raw_tokens:
        parsed_token = transform(token)
        op_list.append(parsed_token)
        transaction_num_order.append(parsed_token.transaction_id)
    return op_list, transaction_num_order

def transform(token: str):
    op = token[0]
    if op not in VALID_OP:
        raise Exception(f'Operação inválida encontrada: {token}') 
    l_paren = token.find('(')
    r_paren = token.find(')')
    if op == 'r':
        transformed_op = Read(transaction_id=int(token[1:l_paren]), operand=token[l_paren+1:r_paren] )
    elif op == 'w':
        transformed_op = Write(transaction_id=int(token[1:l_paren]), operand=token[l_paren+1:r_paren] )
    elif op == 'c':
        transformed_op = Commit(transaction_id=int(token[1]))
    return transformed_op

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

class Tuple():
    def __init__(self, id: int, name: str, value):
        self.id = id
        self.name = name
        self.value = value

class Page():
    def __init__(self, id: int, name: str, tuple_list: List[Tuple]):
        self.id = id
        self.name = name
        self.tuple_list = tuple_list

class Table():
    def __init__(self, id: int, name: str, page_list: List[Page]):
        self.id = id
        self.name = name
        self.page_list = page_list
    def __str__(self):
        string = f'Table {self.name} (id: {self.id}):'
        for i in range(len(self.page_list)):
            curr_page = self.page_list[i]
            string += f'\n{curr_page.name}: has {len(curr_page.tuple_list)} tuples'
        return string


page_list = []
for i in range(4):
    new_page = Page(id = i, name=f'page{i}', tuple_list=[1])
    page_list.append(new_page)
table1 = Table(id=0, name='table1', page_list=page_list)
print(table1)

test = 'r1(x) w1(x) r2(x) w2(x) c1 c2'
tokens = test.split()
op_list, transaction_num_order = parse(tokens)
transaction_num = np.unique(transaction_num_order)
transaction_total = transaction_num[-1]
for op in op_list:
    print(f'{op}')