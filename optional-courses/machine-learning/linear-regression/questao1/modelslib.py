import numpy as np

# implementação de mínimos quadrados ordinários (OLS) 
def OLS(x, y):
    w = np.linalg.inv(x.T @ x) @ x.T @ y
    y_p = x @ w
    errors = y - y_p
    MSE = np.mean(errors ** 2)
    return w, MSE

def GD(x, y):
    pace = 0.001
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

def SGD_simple(x, y):
    pace = 0.000001
    t = 0       #iteração
    w0 = 0
    w1 = 0
    error_list = []
    iter_num = []
    y_p = np.empty_like(x)
    errors = np.zeros_like(x)
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