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
    add_one = 1
    # construindo cada fold:
    for i in range(k):
        # a iteração é um array de boleanos, onde o fold de teste é a parte que possui somente False
        fold = np.full((1,data.shape[0]), True)
        if residue == 0:
            add_one = 0
        for j in range(i*fold_size, (i+1)*fold_size + add_one):
            fold[:,[j]] = False
        if residue > 0:
            residue -= 1
        fold_vector.append(fold)
    return fold_vector
