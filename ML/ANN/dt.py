# Decision trees
import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn import tree
import graphviz 

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
df = df[:100]
## Cleaning genres
genres = col_uniqe(df, 'Genre')
genre_in = num_index(genres)
df = df.replace(to_replace=genres, value=genre_in)

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

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_train, y_train)
print(clf.score(x_test,y_test))
## to much data...I don't want to print
# print(clf.predict(x_test))
# print(y_test)

print('Done!')

print(target_names)
print(feature_names)

# Graph
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("games")

dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=feature_names,  
                         class_names=target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = graphviz.Source(dot_data)  
graph