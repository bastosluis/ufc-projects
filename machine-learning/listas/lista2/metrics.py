import numpy as np

def accuracy(y, y_p):
    total = y.shape[0]
    error = 0
    for i in range(total):
        if y[i] != y_p[i]:
            error += 1
    return 1.0 - (error/total)