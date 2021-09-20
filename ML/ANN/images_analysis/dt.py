import graphviz
from sklearn import tree
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, accuracy_score, recall_score, f1_score, cohen_kappa_score, confusion_matrix

digits = load_digits()

x_train, x_test, y_train, y_test = train_test_split(
    digits.data,
    digits.target,
    test_size=0.3,
    random_state=40)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_train, y_train)
predicted = clf.predict(x_test)

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

# Confusion matrix
print('---- Confusion Matrix ----')
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
scaler = StandardScaler()
scaler.fit(x_train)
features_test_scale = scaler.transform(x_test)
confunsion = confusion_matrix(y_test, predicted)
plot_confusion_matrix(clf, features_test_scale, y_test)
plt.figure(figsize=(20, 20))
plt.show()