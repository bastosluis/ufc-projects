import numpy as np
from abc import ABC
from typing import List

VALID_OP = ['r', 'w', 'c']
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


test = 'r1(x) w1(x) r2(x) w2(x) c1 c2'
tokens = test.split()
op_list, transaction_num_order = parse(tokens)
transaction_num = np.unique(transaction_num_order)
transaction_total = transaction_num[-1]
for op in op_list:
    print(f'Operador: {op}')
