import numpy as np
from abc import ABC
from typing import List
import operations as op
import db_objects as db
from checkTable import CheckTable
from tableRow import TableRow
import constants

# coisas a fazer:
# ver a linha 85
# implementar o escalonamento 

def parse(raw_tokens: List[str]):
    op_list: List[op.Operation] = []
    transaction_num_order: List[int] = []
    for token in raw_tokens:
        parsed_token = transform(token)
        op_list.append(parsed_token)
        transaction_num_order.append(parsed_token.transaction_id)
    return op_list, transaction_num_order

def parse_granulosity(transaction_id : int, operand : str, granulosity : str) -> db.DB_Object:
    if granulosity.lower()=="table":
        return db.Table(id=transaction_id,name=operand)
    elif granulosity.lower()=="page":
        return db.Page(id=transaction_id,name=operand)
    elif granulosity.lower()=="tuple":
        return db.Tuple(id=transaction_id,name=operand)

def transform(token: str):
    operation = token[0]
    if operation not in constants.VALID_OP:
        raise Exception(f'Operação inválida encontrada: {token}') 
    l_paren = token.find('(')
    r_paren = token.find(')')
    colon = token.find(':')

    
    operand=token[l_paren+1:colon]
    if operation!='c':
        transaction_id=int(token[1])
        granulosity=token[colon+1:r_paren]
        granulosity_object=parse_granulosity(transaction_id,operand,granulosity)
    else:
        transaction_id=int(token[1])


    if operation == 'r':
        transformed_op = op.Read(transaction_id=transaction_id, operand=operand, granulosity=granulosity_object )
    elif operation == 'w':
        transformed_op = op.Write(transaction_id=int(token[1:l_paren]), operand=token[l_paren+1:colon], granulosity=granulosity_object )
    elif operation == 'u':
        transformed_op = op.Update(transaction_id=int(token[1:l_paren]), operand=token[l_paren+1:colon], granulosity=granulosity_object)
    elif operation == 'c':
        
        transformed_op = op.Commit(transaction_id=int(token[1]))

    return transformed_op

def main():
    user_input = input("Digite:")
    tokens = user_input.replace(","," ").split(" ")
    print(tokens)
    op_list, transaction_num_order = parse(tokens)
    transaction_list = np.unique(transaction_num_order)
    aborted_status = [False for status in transaction_list]
    order_list = [-1 for i in transaction_list]
    wait_rows = []
    table = CheckTable(order_list)
    # preenchimento inicial do grafo 
    for t in transaction_list:
        table.graph.addVertex(t)
    # escalonamento das transações
    for op in op_list:
        if aborted_status[op.transaction_id] == True:
            pass
        else:
            newRow = TableRow(op.transaction_id,op.lock_type,op.granulosity,constants.STATUS_UNDEFINED)
            # se não ocorreu abort:
            if table.add_row(newRow): 
                if newRow.get_status() == constants.STATUS_WAITING:
                    wait_rows.append()  
            # se ocorreu abort:
            else:
                aborted_status[op.transaction_id] = True
                # mudar: remover da lista de espera todas as linhas da transação
                wait_rows.remove()
    for row in table.get_all_rows():
        print(row.get_lock_type())

if __name__=="__main__":
    main()

"""
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
    print(f'{op}')"""