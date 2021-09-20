# ANN
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import precision_score, accuracy_score, recall_score, f1_score, cohen_kappa_score, confusion_matrix

df = pd.read_csv('https://query.data.world/s/bpnkvanty2ewdnhap5lm3z4cqbr67o')

# Cleaning data
col_uniqe = lambda df, col: [e for e in df[col].explode().unique()]
'''
col_uniqe
----------------
obtains all the unique values of a column dataset

params:
    - dataframe [DataFrame]: dataframe
    - column [str]: column's name

returns:
    - a list of unique values corresponding to the column
'''


num_index = lambda data: [ind for ind in range(1, len(data)+1)]
'''
num_index
----------------
create a numeric index from a list

params:
    - data[list]: list to create the indexes

returns:
    - a list of indexes for data
'''

## Cleaning Publishers
publishers = col_uniqe(df, 'Publisher')
publishers_in = num_index(publishers)
df = df.replace(to_replace=publishers, value=publishers_in)
## Cleaning genres
genres = col_uniqe(df, 'Genre')
genre_in = num_index(genres)
df = df.replace(to_replace=genres, value=genre_in)

df = df[:100]

## target
indexes = {}
ind = 0
for plat in df['Platform']:
    if plat not in indexes:
        indexes[plat] = ind
        ind += 1

target = []
for plat in df['Platform']:
    target.append(indexes[plat])

target_names = col_uniqe(df, 'Platform')

## Removing unnecesary columns
for col in ['Platform', 'Name']:
    del df[col]

feature_names = df.columns
data = df.values

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
