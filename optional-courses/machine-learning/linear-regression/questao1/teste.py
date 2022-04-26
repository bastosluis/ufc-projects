import numpy as np
import matplotlib.pyplot as plt
import modelslib as model
import zscore

dataset = np.genfromtxt('./artificial1d.csv', delimiter=',')
x_dataset = dataset[:,0:-1]
y_dataset = dataset[:,[-1]]
x = x_dataset
y = y_dataset
space = np.linspace(np.min(x), np.max(x))
x = np.c_[np.ones((x.shape[0],1)), x]

# Gradient Descent
w, iter_num, error_list = model.GD(x, y)
plt.subplot(1,2,1)
plt.plot(iter_num, error_list)
plt.title("MSE ao longo das iterações do GD:")
#funct = w0 + w1*space
print(f'w.shape: {w.shape} \nx.shape: {x.shape} \ny.shape: {y.shape}')
y_p = x @ w 
plt.subplot(1,2,2)
plt.plot(x_dataset,y_dataset, 'bo')
plt.plot(x_dataset, y_p, '-r', label='y=w0+w1*x')
plt.title("Reta resultante para o GD:")
plt.show()
'''
# Ordinary Least Squares
w, MSE = model.OLS(x1, y)
print(f'Valor do MSE no OLS: {MSE}')
plt.plot(x,y, 'bo')
funct = w[0] + w[1]*space
plt.plot(space, funct, '-r', label='y=w0+w1*x')
plt.title("Reta resultante para o OLS:")
plt.show()
'''