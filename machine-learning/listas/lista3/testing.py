import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
# implementações feitas por mim
import modelslib as model
import norm
import training

dataset = np.genfromtxt('./kc2.csv', delimiter=',')
np.random.shuffle(dataset)

fold_list = training.kfold(10, dataset)
nn_param = []
knn_param = []
tree_param = []

nn_pred = []
tree_pred = []
knn_pred = []

model_names = [ '1NN', '5NN', 'TREE']
models_param = [ nn_param, knn_param, tree_param ]
model_preds = [ nn_pred, knn_pred, tree_pred ]

print(f"Número de amostras: {dataset.shape[0]}")
print(f"Número de dimensões: {dataset.shape[1]}")
print(f"Número de classes: {np.unique(dataset[:,[-1]]).shape[0]}")
print(f"Número de folds: {len(fold_list)}")

# Inicializando métricas:
# Listas de Listas de métricas para cada modelo (são 3, divididos em 10-fold totalizando 30)
acurracy_matrix = [[],[],[]]
precision_matrix = [[],[],[]]
f1score_matrix = [[],[],[]]
recall_matrix = [[],[],[]]
# Lista para guardar os testes de cada fold, em formato de tupla (x,y):
fold_test_list = []

for i in range(len(fold_list)):

    # Filtragem dos dados por cada fold: 
    train_dataset = dataset[fold_list[i].reshape(-1) == True] 
    test_dataset = dataset[fold_list[i].reshape(-1) == False]
    x_train = train_dataset[:,:-1]
    y_train = train_dataset[:,[-1]]
    x_test = test_dataset[:,:-1]
    y_test = test_dataset[:,[-1]]
    # Guarda-se o grupo de teste:
    fold_test_list.append((x_test,y_test))
    # Normalizando x:
    x_scaled = norm.normalize(x_train)
    x_test_scaled = norm.normalize(x_test)


    # Nearest Neighbour:
    y_p = model.k_nearest_neighbour(1, x_scaled, y_train, x_test_scaled)
    nn_param.append((x_scaled,y_train)) # knn não é paramétrico, logo guardaremos o conjunto de dados utilizados
    nn_pred.append(y_p)
    acurracy_matrix[0].append(metrics.accuracy_score(y_test, y_p))
    precision_matrix[0].append(metrics.precision_score(y_test, y_p, average='macro'))
    recall_matrix[0].append(metrics.recall_score(y_test, y_p, average='macro'))
    f1score_matrix[0].append(metrics.f1_score(y_test, y_p, average='macro'))

    
    # 5-Nearest Neighbour:
    y_p = model.k_nearest_neighbour(5, x_scaled, y_train, x_test_scaled)
    knn_param.append((x_scaled,y_train)) # knn não é paramétrico, logo guardaremos o conjunto de dados utilizados
    knn_pred.append(y_p)
    acurracy_matrix[1].append(metrics.accuracy_score(y_test, y_p))
    precision_matrix[1].append(metrics.precision_score(y_test, y_p, average='macro'))
    recall_matrix[1].append(metrics.recall_score(y_test, y_p, average='macro'))
    f1score_matrix[1].append(metrics.f1_score(y_test, y_p, average='macro'))


    # Árvore de Decisão:
    tree_model = DecisionTreeClassifier().fit(x_train, y_train)
    y_p = tree_model.predict(x_test)
    tree_param.append(tree_model)
    tree_pred.append(y_p)
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

model = 0
fold = 0
print(f"Summary for the classifier {model_names[model]} (Fold {fold+1}) with accuracy {metrics.accuracy_score(fold_test_list[fold][1], model_preds[model][fold]):.2f}")
print(metrics.classification_report(fold_test_list[fold][1], model_preds[model][fold]))