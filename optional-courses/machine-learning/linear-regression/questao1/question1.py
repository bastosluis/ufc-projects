import numpy as np
import matplotlib.pyplot as plt  # Biblioteca para gerar gráficos
import modelslib as model
import zscore
#carregar os dados
dataset = np.genfromtxt('./artificial1d.csv', delimiter=',')
x_dataset = dataset[:,0:-1]
y_dataset = dataset[:,[-1]]
# calculo de média e desvio padrão
x = x_dataset
y = y_dataset
x_mean = np.mean(x)
y_mean = np.mean(y)
x_std = np.std(x)
y_std = np.std(y)
# normalização
x = zscore.normalize(x, x_mean, x_std)
y = zscore.normalize(y, y_mean, y_std)

space = np.linspace(np.min(x), np.max(x))
figure, axis = plt.subplots(2, 2)


# Gradient Descent
w0, w1, iter_num, error_list = model.GD_simple(x, y)
axis[0,0].plot(iter_num, error_list)
axis[0,0].set_title("MSE ao longo das iterações do GD:")
funct = w0 + w1*space
axis[0,1].plot(x,y, 'bo')
axis[0,1].plot(space, funct, '-r', label='y=w0+w1*x')
axis[0,1].set_title("Reta resultante para o GD:")



# Stocastic Gradient Descent
w0, w1, iter_num, error_list = model.SGD_simple(x, y)
axis[1,0].plot(iter_num, error_list)
axis[1,0].set_title("MSE ao longo das iterações do SGD:")
funct = w0 + w1*space
axis[1,1].plot(x,y, 'bo')
axis[1,1].plot(space, funct, '-r', label='y=w0+w1*x')
axis[1,1].set_title("Reta resultante para o SGD:")

plt.show()

# Ordinary Least Squares
x1 = np.c_[np.ones((x.shape[0],1)), x]
w, MSE = model.OLS(x1, y)
print(f'Valor do MSE no OLS: {MSE}')
plt.plot(x,y, 'bo')
funct = w[0] + w[1]*space
plt.plot(space, funct, '-r', label='y=w0+w1*x')
plt.title("Reta resultante para o OLS:")
plt.show()
