from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree
iris = load_iris()

print(iris.data)
print(iris.target)

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=30)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_train, y_train)
print(clf.score(x_test,y_test ))
print(clf.predict(x_test))
print(y_test)

import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("iris")

print(iris.feature_names)
print(iris.target_names)
print(iris)

dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = graphviz.Source(dot_data)  
graph
