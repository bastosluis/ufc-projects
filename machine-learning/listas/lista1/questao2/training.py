import numpy as np
import modelslib as models 
import matplotlib.pyplot as plt
import zscore
#   erros:
#   checar como usar o COLON (:)
#   pensar em como fazer o novo x com as transformações, pois eu pensei que era só 1 coluna (são 8)
def train(model, training_percent, x_total, y_total):
    line_num = x_total.shape[0]
    x = x_total[:int(line_num*training_percent)]         
    y = y_total[:int(line_num*training_percent)]
    # calculo de média e desvio padrão
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_std = np.std(x)
    y_std = np.std(y)
    # normalização
    x = zscore.normalize(x, x_mean, x_std)
    y = zscore.normalize(y, y_mean, y_std)
    # uso do algoritmo do modelo
    x = np.c_[np.ones((x.shape[0],1)), x]
    w = model(x,y)
    w = w[0]
    y_p = x @ w
    errors = zscore.denormalize(y - y_p, y_mean, y_std)
    return w, RMSE(errors)

def ols_test(w, training_percent, x_total, y_total, training_RMSE, graph_title, current_iter):
    line_num = x_total.shape[0]
    x_test = x_total[int(line_num*training_percent):]
    y_test = y_total[int(line_num*training_percent):]

    normalized_x = zscore.normalize(x_test, np.mean(x_test), np.std(x_test))
    normalized_x = np.c_[np.ones((x_test.shape[0],1)), normalized_x]
    y_p = normalized_x @ w
    errors = y_test - zscore.denormalize(y_p, np.mean(y_p), np.std(y_p))
    test_RMSE = RMSE(errors)
    print('====================================')
    print(f'P = {current_iter+1}')
    print(f'RMSE de treino: {training_RMSE}')
    print(f'RMSE de teste: {test_RMSE}')
    print('====================================')
    print(f'valor de min e max: {np.min(x_total)}, {np.max(x_total)}')
'''    interval = np.linspace(np.min(x_total), np.max(x_total))
    plt.plot(x_total[:,1], y_total, 'bo')
    plt.plot(interval, polynomial(interval, current_iter+1), '-r')
    plt.set_title(graph_title)
    plt.show()'''
    

def RMSE(errors):
    return np.sqrt( np.mean(errors ** 2) )

def nonlinear_transform(x_original, new_rows):
    x = x_original
    res = np.ones((x.shape[0],1))
    for j in range(x_original.shape[1]):
        temp_columns = x[:,[j]]
        for i in range(1,new_rows):
            new_row = x[:,[j]]**(i+1) 
            temp_columns = np.c_[temp_columns, new_row]
        res = np.c_[res, temp_columns]
    return res[:,1:]

def polynomial(interval, order):
    result = 0
    for i in range(order):
        result += interval**i+1
    return i