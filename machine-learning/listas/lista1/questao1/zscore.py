import numpy as np

def normalize_row(row):
    #print(f'=========rows:==============\nrow: {row}')
    return (row - np.mean(row))/np.std(row)

def denormalize_row(row, mean, std):
    return mean+(row*x)

def normalize(m):
    #print(f'==========normalize:=============')
    line_num = m.shape[0]
    column_num = m.shape[1]
    m_res = np.reshape(normalize_row(m[:,0]), (line_num,1))
    #print(f'aqui: {m_res} \nshape: {m_res.shape}')
    for i in range(1,column_num):
        #print(f'=========iteração {i}:==============\n')
        norm_row = np.reshape(normalize_row(m[:,i]), (line_num,1))
        #print(f'=========matrizes do loop:==============\nnorm_row: {norm_row} \nshape: {norm_row.shape}')
        m_res = np.c_[ m_res, norm_row ] 
        #print(f'm_res: {m_res} \nshape: {m_res.shape}')
    return m_res

def denormalize(m, mean, std):
    #print(f'==========denormalize:=============')
    line_num = m.shape[0]
    column_num = m.shape[1]
    m_res = np.reshape(denormalize_row(m[:,0], mean, std), (line_num,1))
    #print(f'aqui: {m_res} \nshape: {m_res.shape}')
    for i in range(1,column_num):
        #print(f'=========iteração {i}:==============\n')
        denorm_row = np.reshape(denormalize_row(m[:,i], mean, std), (line_num,1))
        #print(f'=========matrizes do loop:==============\nnorm_row: {norm_row} \nshape: {norm_row.shape}')
        m_res = np.c_[ m_res, denorm_row ] 
        #print(f'm_res: {m_res} \nshape: {m_res.shape}')
    return m_res

def sigmoid(value):
    return 1 / (1 + np.exp(-value))
