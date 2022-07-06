import numpy as np
from abc import ABC
from typing import List
import operations as op
import db_objects as db
VALID_OP = ['r', 'w', 'c']
READ_LOCK = 0
WRITE_LOCK = 1
CERTIFY_LOCK = 2

def parse(raw_tokens: List[str]):
    op_list: List[op.Operation] = []
    transaction_num_order: List[int] = []
    for token in raw_tokens:
        parsed_token = transform(token)
        op_list.append(parsed_token)
        transaction_num_order.append(parsed_token.transaction_id)
    return op_list, transaction_num_order

def transform(token: str):
    operation = token[0]
    if operation not in VALID_OP:
        raise Exception(f'Operação inválida encontrada: {token}') 
    l_paren = token.find('(')
    r_paren = token.find(')')
    if operation == 'r':
        transformed_op = op.Read(transaction_id=int(token[1:l_paren]), operand=token[l_paren+1:r_paren] )
    elif operation == 'w':
        transformed_op = op.Write(transaction_id=int(token[1:l_paren]), operand=token[l_paren+1:r_paren] )
    elif operation == 'c':
        transformed_op = op.Commit(transaction_id=int(token[1]))
    return transformed_op



page_list = []
for i in range(4):
    new_page = db.Page(id = i, name=f'page{i}', tuple_list=[1])
    page_list.append(new_page)
table1 = db.Table(id=0, name='table1', page_list=page_list)
print(table1)

test = 'r1(x) w1(x) r2(x) w2(x) c1 c2'
tokens = test.split()
op_list, transaction_num_order = parse(tokens)
transaction_num = np.unique(transaction_num_order)
transaction_total = transaction_num[-1]
for op in op_list:
    print(f'{op}')