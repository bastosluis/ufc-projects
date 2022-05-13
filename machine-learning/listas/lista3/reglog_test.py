import numpy as np
import modelslib as model
import matplotlib.pyplot as plt
import norm
import metrics
import training

dataset = np.genfromtxt('./kc2.csv', delimiter=',')
#np.random.seed(1234)
#np.random.shuffle(dataset)

x_dataset = dataset[:,:-1]
y_dataset = dataset[:,[-1]]
x = x_dataset
y = y_dataset

# treino com divisão treinamento/teste:
data_training, data_test = training.separate_data(dataset, 0.8)
x = data_training[:,:-1]
y = data_training[:,[-1]]

x_test = data_test[:,:-1]
y_test = data_test[:,[-1]]

'''
# Normalizando x:
x = norm.normalize(x)
# Aplicando a coluna de 1s
x = np.c_[np.ones((x.shape[0],1)), x]

# regressao logistica:
x_test = norm.normalize(x_test)
x_test = np.c_[np.ones((x_test.shape[0],1)), x_test]
w, iter_num, error_list = model.GD_logi(x, y)
y_p = np.around(model.sigmoid(x_test @ w)) 
'''
'''
# naive bayes:
y_test = y
tupla = model.naive_bayes_gaussian(x,y)
y_p = model.predict_nbg(x, tupla[0], tupla[1], tupla[2])
print(f'estamos usando naive bayes')
'''
'''
# adg:
y_test = y
tupla = model.gaussian_discriminant_analysis(x,y)
y_p = model.predict_gda(x, tupla[0], tupla[1], tupla[2])
'''
# knn:
# Normalizando x:
x = norm.normalize(x)
x_test = norm.normalize(x_test)
y_p = model.k_nearest_neighbour(5, x, y, x_test)



print(f'==============teste===============\nshape y_p: {y_p.shape}')
print(f'shape y treinamento: {y.shape}')
print(f'shape dataset: {dataset.shape}')
print(f'acurácia: {metrics.accuracy(y_test, y_p)*100:.2f}%')
print(f'presença de zeros: {metrics.accuracy(np.zeros_like(y_p), y_p)*100:.2f}%')
print(f'presença de ums: {metrics.accuracy(np.ones_like(y_p), y_p)*100:.2f}%')
print(f'a acurácia da função comparadora: {metrics.accuracy(np.zeros_like(y_p), np.zeros_like(y_p))*100:.2f}%')
#print(y_p[:30])

