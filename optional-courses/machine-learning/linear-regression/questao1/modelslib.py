import numpy as np

# implementação de mínimos quadrados ordinários (OLS) 
# erros: verificar que w + (erro*x) é pra ser uma soma de matrizes (d+1 x 1) ou apenas da média que é um valor escalar (erro*x) somado com w
# verificar porque que w passa a ter dimensão 2x2
def OLS(x, y):
    w = np.linalg.inv(x.T @ x) @ x.T @ y
    y_p = x @ w
    errors = y - y_p
    MSE = np.mean(errors ** 2)
    return w, MSE

def GD(x, y):
    pace = 0.01
    t = 0       #iteração
    w = np.zeros((x.shape[1],1))
    error_list = []
    iter_num = []
    while t < 1500:
        iter_num.append(t)
        t += 1
        y_p = x @ w
        errors = y - y_p
        w = w + pace * np.mean(errors * x)
        error_list.append(np.mean(errors**2))
    return w, iter_num, error_list

def SGD(x, y):
    pace = 0.01
    t = 0       #iteração
    w = np.zeros((x.shape[1],1))
    error_list = []
    iter_num = []
    y_p = np.zeros_like(y)
    errors = np.zeros_like(y)
    number_of_loops = 0
    while t < 1500:
        x_perm = np.random.permutation(x)
        number_of_loops += 1
        for i in range(x.shape[0]):
            iter_num.append(t)
            t += 1
            print(f'dentro do sgd:\nw.shape: {w.shape} \nx[1].shape: {np.reshape(x[i], (1,x.shape[1])).shape} ')
            y_p[i] = x[i] @ w
            print(f'shape y_p[i]: {y_p[i].shape} e valor no i: {y_p[i][0]}')
            errors[i] = y[i][0] - y_p[i][0]
            print(f'shape (errors[i][0] * x[i]): {(errors[i][0] * x[i]).T.shape} e a sua matriz: {(errors[i][0] * x[i]).T}')
            w = w + (pace * (errors[i][0] * x[i])).T
            error_list.append(np.mean(errors[:1+(i*number_of_loops)]**2))
    return w, iter_num, error_list

def SGD_simple(x, y):
    pace = 0.001
    t = 0       #iteração
    w0 = 0
    w1 = 0
    error_list = []
    iter_num = []
    y_p = np.empty_like(y)
    errors = np.zeros_like(y)
    while t < 1500:
        x_perm = np.random.permutation(x)
        for i in range(x.shape[0]):
            t += 1
            y_p[i] = w0 + (w1*x_perm[i]) 
            errors[i] = y[i] - y_p[i]
            w0 = w0 + pace * errors[i]
            w1 = w1 + pace * errors[i] * x_perm[i]
        iter_num.append(t)
        error_list.append(np.mean(errors**2))
    return w0, w1, iter_num, error_list

def GD_simple(x, y):
    pace = 0.000001
    t = 0       #iteração
    w0 = 0
    w1 = 0
    error_list = []
    iter_num = []
    while t < 1500:
        t += 1
        y_p = w0 + (w1*x) 
        errors = y - y_p
        error_list.append(np.mean(errors**2))
        iter_num.append(t)
        w0 = w0 + pace * np.mean(errors)
        w1 = w1 + pace * np.mean(errors * x)
    return w0, w1, iter_num, error_list


def RMSE(errors):
    return np.sqrt( np.mean(errors ** 2) )
