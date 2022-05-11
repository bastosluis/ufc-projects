import numpy as np

# função para separar os dados em treinamento e teste:
def separate_data(data, test_size):
    line_num = data.shape[0]
    return data[:int(line_num*test_size)], data[int(line_num*test_size):]

def kfold(k, data):
    n = data.shape[0]
    fold_size = int(n/k)
    fold_vector = []
    residue = n%k
    current = 0
    # construindo cada fold:
    for i in range(k):
        # a iteração é um array de boleanos, onde o fold de teste é a parte que possui somente False
        fold = np.full((1,data.shape[0]), True)
        for j in range(current, current+fold_size):
            fold[:,[j]] = False
            current+=1
        if residue > 0:
            fold[:,[current]] = False
            current+=1
            residue -= 1
        fold_vector.append(fold)
    return fold_vector
