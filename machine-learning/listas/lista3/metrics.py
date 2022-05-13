import numpy as np

def accuracy(y, y_p):
    total = y.shape[0]
    error = 0
    if total != y_p.shape[0]:
        print(f'Warning: Predição possui shape diferente dos dados de comparação: y_p: {y_p.shape}, y:{y.shape}')
        return -1
    for i in range(total):
        if y[i] != y_p[i]:
            error += 1
            #print(f'diferença no indice {i}: y = {y[i][0]} y_p = {y_p[i][0]}')
    return 1.0 - (error/total)