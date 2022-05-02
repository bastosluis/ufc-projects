import numpy as np
import math
import modelslib as models 
import zscore
import training

dataset = np.genfromtxt('./california.csv', delimiter=',')
x_original = dataset[:,:-1]
y_original = dataset[:,[-1]]
for i in range(11): # mudar pra 11
    x_current = training.nonlinear_transform(x_original, i)
    w, training_RMSE = training.train(models.OLS, 0.8, x_current, y_original)
    training.ols_test(w, 0.8, x_current, y_original, training_RMSE, f'P = {i+1}', i)