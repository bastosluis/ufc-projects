import numpy as np
import modelslib as model
import matplotlib.pyplot as plt
import norm
import metrics

dataset = np.genfromtxt('./breastcancer.csv', delimiter=',')
x_dataset = dataset[:,:-1]
y_dataset = dataset[:,[-1]]
x = x_dataset
y = y_dataset

# Normalizando x:
x = norm.normalize(x)
# Aplicando a coluna de 1s
x = np.c_[np.ones((x.shape[0],1)), x]
'''
figure, axis = plt.subplots(1, 2)

w, iter_num, error_list = model.GD_logi(x, y)
plt.plot(iter_num, error_list)
plt.title("MSE ao longo das iterações do GD logístico:")
y_p = x @ w 

plt.show()
'''
w, iter_num, error_list = model.GD_logi(x, y)
y_p = x @ w 
'''
rows = 400
y_p = y[:rows]
y_p = np.r_[y_p, np.ones( (y.shape[0]-rows, 1) )]
'''
print(f'acurácia: {metrics.accuracy(y, y_p)*100}%, shape do y: {y.shape}')
print(y_p[:30])
