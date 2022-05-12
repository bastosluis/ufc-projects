import numpy as np
import modelslib as model
import matplotlib.pyplot as plt
import norm
from sklearn import metrics
import training

dataset = np.genfromtxt('./breastcancer.csv', delimiter=',')

fold_list = training.kfold(10, dataset)

for i in range(len(fold_list)):

    # Filtragem dos dados por cada fold: 
    train_dataset = dataset[fold_list[i] == True] 
    test_dataset = dataset[fold_list[i] == False]
    x_train = train_dataset[:,:-1]
    y_train = train_dataset[:,[-1]]
    x_test = test_dataset[:,:-1]
    y_test = test_dataset[:,[-1]]
    # Normalizando x:
    x_scaled = norm.normalize(x_train)
    x_test_scaled = norm.normalize(x_test)
    # Aplicando a coluna de 1s
    x_scaled = np.c_[np.ones((x_scaled.shape[0],1)), x_scaled]
    x_test_scaled = np.c_[np.ones((x_test_scaled.shape[0],1)), x_test_scaled]


    # Regressão Logística:
    logreg_param, iter_num, error_list = model.GD_logi(x_scaled, y_train)
    w = logreg_param
    logreg_pred = np.around(model.sigmoid(x_test_scaled @ w)) 