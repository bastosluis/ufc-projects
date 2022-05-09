import numpy as np

# função para separar os dados em treinamento e teste:
def separate_data(data, test_size):
    line_num = data.shape[0]
    return data[:int(line_num*test_size)], data[int(line_num*test_size):]