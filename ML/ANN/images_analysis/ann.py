import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import precision_score, accuracy_score, recall_score, f1_score, cohen_kappa_score, confusion_matrix


digits = load_digits()
data = digits.data
target = digits.target

# Runing trainning
x_train, x_test, y_train, y_test = train_test_split(
    data,
    target,
    test_size=0.3,
    random_state=30)


## data procesing
scaler = StandardScaler()
scaler.fit(x_train)
features_train_scale = scaler.transform(x_train)
features_test_scale = scaler.transform(x_test)

iterations = 1000   # define the iterations for training over the dataset
hidden_layers = [10,10,10]  # define the layers/depth of the NN

mlp = MLPClassifier(hidden_layer_sizes=(hidden_layers), max_iter=iterations)
mlp.fit(features_train_scale, y_train)
predicted = mlp.predict(features_test_scale)

# Metrics
print('---- Metrics ----')
accuracy = accuracy_score(y_true=y_test, y_pred=predicted)
precision = precision_score(y_true=y_test, y_pred=predicted, average='macro')
recall = recall_score(y_true=y_test, y_pred=predicted, average = 'micro')
f1 = f1_score(y_true=y_test, y_pred=predicted, average= 'micro')
kappa = cohen_kappa_score (y1= y_test, y2= predicted)

print('''
* Accuracy: {}
* Precision: {}
* Recall: {}
* F-score: {}
* Kappa: {}
'''.format(accuracy, precision, recall, f1, kappa))

print('Done!')

confunsion = confusion_matrix(y_test, predicted)
plot_confusion_matrix(mlp, features_test_scale, y_test)
plt.figure(figsize=(20, 20))
plt.show()