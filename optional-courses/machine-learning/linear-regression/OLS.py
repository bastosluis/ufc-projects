# exemplo de implementação de mínimos quadrados ordinários (OLS) 
# 
import numpy as np
import matplotlib.pyplot as plt  # Biblioteca para gerar gráficos

peixe_dataset = np.genfromtxt('./peixe.txt', delimiter=',')
peixe_dataset

# X = [1]T + [2 ultimas col. de peixe_dataset] (concatenação de colunas)
x = np.c_[np.ones((peixe_dataset.shape[0],1)), peixe_dataset[:,[0,-2]]]
y = peixe_dataset[:,[-1]]
w = np.linalg.inv(x.T @ x) @ x.T @ y
y_p = x @ w

# Raíz do erro quadrático médio (RMSE):
RMSE = np.sqrt( np.mean(((y - y_p) ** 2)) )
#print(RMSE)
