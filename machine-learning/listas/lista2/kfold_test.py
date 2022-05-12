import numpy as np
import modelslib as model
import matplotlib.pyplot as plt
import norm
from sklearn import metrics
import training

dataset = np.genfromtxt('./breastcancer.csv', delimiter=',')

fold_list = training.kfold(10, dataset)
logreg_param = []
nbg_param = []
gda_param = []

logreg_pred = []
nbg_pred = []
gda_pred = []

model_names = [ 'LR', 'GDA', 'NBG' ]
models_param = [ logreg_param, gda_param, nbg_param ]
model_preds = [ logreg_pred, gda_pred, nbg_pred ]

# Inicializando métricas:
# Listas de Listas de métricas para cada modelo (são 3, divididos em 10-fold totalizando 30)
acurracy_matrix = [[],[],[]]
precision_matrix = [[],[],[]]
f1score_matrix = [[],[],[]]
recall_matrix = [[],[],[]]

for i in range(len(fold_list)):

    # Filtragem dos dados por cada fold: 
    train_dataset = dataset[fold_list[i].reshape(-1) == True] 
    test_dataset = dataset[fold_list[i].reshape(-1) == False]
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
    w, iter_num, error_list = model.GD_logi(x_scaled, y_train)
    logreg_param.append(w)
    y_p = np.around(model.sigmoid(x_test_scaled @ w))
    logreg_pred.append(y_p)
    acurracy_matrix[0].append(metrics.accuracy_score(y_test, y_p))
    precision_matrix[0].append(metrics.precision_score(y_test, y_p, average='macro'))
    recall_matrix[0].append(metrics.recall_score(y_test, y_p, average='macro'))
    f1score_matrix[0].append(metrics.f1_score(y_test, y_p, average='macro'))

    
    # Análise de Discriminante Gaussiano:
    gda_p = model.gaussian_discriminant_analysis(x_train,y_train)
    gda_param.append(gda_p)
    y_p = model.predict_gda(x_test, gda_p[0], gda_p[1], gda_p[2])
    gda_pred.append(y_p)
    acurracy_matrix[1].append(metrics.accuracy_score(y_test, y_p))
    precision_matrix[1].append(metrics.precision_score(y_test, y_p, average='macro'))
    recall_matrix[1].append(metrics.recall_score(y_test, y_p, average='macro'))
    f1score_matrix[1].append(metrics.f1_score(y_test, y_p, average='macro'))


    # Naive Bayes Gaussiano:
    nbg_p = model.naive_bayes_gaussian(x_train,y_train)
    nbg_param.append(nbg_p)
    y_p = model.predict_nbg(x_test, nbg_p[0], nbg_p[1], nbg_p[2])
    nbg_pred.append(y_p)
    acurracy_matrix[2].append(metrics.accuracy_score(y_test, y_p))
    precision_matrix[2].append(metrics.precision_score(y_test, y_p, average='macro'))
    recall_matrix[2].append(metrics.recall_score(y_test, y_p, average='macro'))
    f1score_matrix[2].append(metrics.f1_score(y_test, y_p, average='macro'))
# Medições:
for i in range(len(model_names)):
    
    print(f'\nAverage score in 10-fold training for {model_names[i]}:\n')
    print(f'Accuracy:   {np.mean(acurracy_matrix[i]):.2f}, with standard deviation: {np.std(acurracy_matrix[i]):.2f};')
    print(f'Precision:  {np.mean(precision_matrix[i]):.2f}, with standard deviation: {np.std(precision_matrix[i]):.2f};')
    print(f'Recall:     {np.mean(recall_matrix[i]):.2f}, with standard deviation: {np.std(recall_matrix[i]):.2f};')
    print(f'F1:         {np.mean(f1score_matrix[i]):.2f}, with standard deviation: {np.std(f1score_matrix[i]):.2f};\n')

