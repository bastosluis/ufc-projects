import numpy as np
import matplotlib.pyplot as plt
import modelslib as model
import zscore

dataset = np.genfromtxt('./artificial1d.csv', delimiter=',')
x_dataset = dataset[:,:-1]
y_dataset = dataset[:,[-1]]

x = model.nonlinear_transform(x_dataset, 25) #polinomio de grau 25
y = y_dataset
#print(x_dataset)
# Salvando a média e desvio padrão:
x_mean = np.mean(x)
x_std = np.std(x)
y_mean = np.mean(y)
y_std = np.std(y)

# Normalizando x e y:
x = zscore.normalize(x)
y = zscore.normalize(y)

# Aplicando a coluna de 1s
x = np.c_[np.ones((x.shape[0],1)), x]
figure, axis = plt.subplots(2, 2)

# Gradient Descent
w, iter_num, error_list = model.GD(x, y)
axis[0,0].plot(iter_num, error_list)
axis[0,0].set_title("MSE ao longo das iterações do GD:")
y_p = x @ w 
axis[0,1].plot(x_dataset,y_dataset, 'bo')
axis[0,1].plot(x_dataset, y_p, '-r', label='y=w0+w1*x')
axis[0,1].set_title("Reta resultante para o GD:")



# Stocastic Gradient Descent
w, iter_num, error_list = model.SGD(x, y)
axis[1,0].plot(iter_num, error_list)
axis[1,0].set_title("MSE ao longo das iterações do SGD:")
y_p = x @ w 
axis[1,1].plot(x_dataset,y_dataset, 'bo')
axis[1,1].plot(x_dataset, y_p, '-r', label='y=w0+w1*x')
axis[1,1].set_title("Reta resultante para o SGD:")
plt.show()