
from sklearn.datasets import load_iris # sklearn is the abbr. of scikit-learn, which is a free machine learning base including various methods (SVM,RF,Boosting,k-means,DBSCAN)
import numpy as np
from sklearn import tree
import graphviz
from sklearn.metrics import accuracy_score as acc_rate

iris = load_iris()
print(iris.data) # the data of the dataset iris
print(iris.feature_names) # the names of the features
print(iris.target_names) # the names of the targets
print(iris.target) # the targets if the dataset iris

np.random.seed(123) # for reproducibility
test_idx = np.random.randint(0, len(iris.target), len(iris.target)//3) # randomly choose approx. 1/3 of samples as testing data (e.g. 10//3 returns to 3)
train_data = np.delete(iris.data, test_idx, axis=0) # for iris.data, delete the testing data (approx. 1/3) from the dataset iris to get the training data (approx. 2/3) (delete by row)
train_target = np.delete(iris.target, test_idx) # for iris.target, delete the testing data (approx. 1/3) from the dataset iris to get the training data (approx. 2/3)

test_data = iris.data[test_idx] # the testing data for iris.data
test_target = iris.target[test_idx] # the testing data for iris.target

# Initialize a decision tree classifier object with given arguments 'criterion' and 'splitter'; Note that it is possible that many other arguments can be placed into the object
clf = tree.DecisionTreeClassifier(criterion = 'entropy', splitter='best',) # see more details of this tree.DecisionTreeClassifier() e.g. via online materials if necessary

# train the model using train_data and train_target as two parameteris
clf.fit(X=train_data, y=train_target)

# compare the test set for target and the predicted result based on clf obtained via the test set for data
print('\nThe test set for target is:\n', test_target)
print('\nThe predicted result based on clf obtained via the test set for data is:\n', clf.predict(test_data))
print('\nAccuracy rate is:\n', acc_rate(test_target,clf.predict(test_data))) # Accuracy

# visualize the tree and save it as a pdf file using graphviz module
dot_data = tree.export_graphviz(clf,
                                out_file=None,
                                feature_names=iris.feature_names,
                                filled=True,
                                rounded=True,
                                impurity=False,
                                special_characters=True)
graph = graphviz.Source(dot_data)
direct = r'C:/Users/admin/PycharmProjects/pythonProject4/' + '/DEDA_MachineLearning/'
graph.render(direct + 'iris')