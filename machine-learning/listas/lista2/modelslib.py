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
        w = w + pace * np.reshape(np.mean(errors * x,axis=0), (-1,1))
        error_list.append(np.mean(errors**2))
    return w, iter_num, error_list
'''
def SGD_noperm(x, y):
    pace = 0.01
    t = 0       #iteração
    w = np.zeros((x.shape[1],1))
    error_list = []
    iter_num = []
    temp_list = []
    y_p = np.zeros_like(y)
    errors = np.zeros_like(y)
    number_of_loops = 0
    while t < 1500:
        #line_perm = np.random.permutation(np.arange(x.shape[0]))
        #print(f'{line_perm}\nvalor total: {line_perm.shape}')
        i = 0
        for i in range(x.shape[0]):  #for k in line_perm:
            iter_num.append(t)
            t += 1
            y_p[i] = x[i] @ w
            errors[i] = y[i][0] - y_p[i][0]
            w = w + (pace * np.reshape(errors[i][0] * x[i], (-1,1)))
            temp_list.append(errors[i][0])
            error_list.append(np.mean(np.array(temp_list)**2 ))
            #error_list.append(np.mean((errors[:i+1])**2))
            #i += 1
    return w, iter_num, error_list
'''
def SGD(x, y):
    pace = 0.01
    t = 0       #iteração
    w = np.zeros((x.shape[1],1))
    error_list = []
    iter_num = []
    temp_list = []
    y_p = np.zeros_like(y)
    errors = np.zeros_like(y)
    number_of_loops = 0
    while t < 1500:
        line_perm = np.random.permutation(np.arange(x.shape[0]))
        i = 0
        for k in line_perm:
            iter_num.append(t)
            t += 1
            y_p[k] = x[k] @ w
            errors[k] = y[k][0] - y_p[k][0]
            w = w + (pace * np.reshape(errors[k][0] * x[k], (-1,1)))
            temp_list.append(errors[k][0])
            error_list.append(np.mean(np.array(temp_list)**2 ))
            i += 1
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


def GD_logi(x, y):
    pace = 0.01
    t = 0       #iteração
    w = np.zeros((x.shape[1],1))
    error_list = []
    iter_num = []
    while t < 1500:
        iter_num.append(t)
        t += 1
        y_p = sigmoid(x @ w) # exclusivo da regressão logística
        errors = y - y_p 
        w = w + pace * np.reshape(np.mean(errors * x,axis=0), (-1,1))
        error_list.append(np.mean(errors**2))
    return w, iter_num, error_list

def SGD_logi(x, y):
    pace = 0.01
    t = 0       #iteração
    w = np.zeros((x.shape[1],1))
    error_list = []
    iter_num = []
    temp_list = []
    y_p = np.zeros_like(y)
    errors = np.zeros_like(y)
    number_of_loops = 0
    while t < 1500:
        line_perm = np.random.permutation(np.arange(x.shape[0]))
        i = 0
        for k in line_perm:
            iter_num.append(t)
            t += 1
            y_p[k] = sigmoid(x[k] @ w) # exclusivo da regressão logística
            errors[k] = y[k][0] - y_p[k][0]
            w = w + (pace * np.reshape(errors[k][0] * x[k], (-1,1)))
            temp_list.append(errors[k][0])
            error_list.append(np.mean(np.array(temp_list)**2 ))
            i += 1
    return w, iter_num, error_list

# auxiliares:
def sigmoid(value):
    return 1 / (1 + np.exp(-value))

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