###################### SIMPLE KNN VS NAIVE BAIS##################################
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

#Loading Iris Data Set from sklearn
irisdataset = datasets.load_iris()
#X containing the main Array
x = irisdataset.data
#Y containing the target data
y = irisdataset.target

print(x)
#Creatinga a NB Gausian model
model1=GaussianNB()
#Training the NB Gausian model
model1.fit(x,y)

print("Gausian NB:          ",model1.predict([[1, 2, 3, 4], [2, 3, 4, 5]])," Score: ", model1.score(x,y))

#Creating a KNN model
model = KNeighborsClassifier(n_neighbors=10)
#Training the KNN model
model.fit(x, y)
print("K Nearest Neighbour: ",model.predict([[1, 2, 3, 4], [2, 3, 4, 5]])," Score: ",model.score(x, y))

###################### CROSS VALIDATION KNN VS CROSS VALIDATION NAIVE BAIS##################################

from sklearn.neighbors import KNeighborsClassifier
from sklearn import naive_bayes
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

# Loading the dataset
irisdataset = datasets.load_iris()

# getting the data and response of the dataset
x = irisdataset.data
y = irisdataset.target

# split the data for training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

##NNB MODEL HOMEWORK
model1=GaussianNB()
model1.fit(x_train,y_train)

#Predicting the Values using the newly training model
y_nb_pred= model1.predict(x_test)

print("Accuracy for NaiveBayes: ",metrics.accuracy_score(y_test,y_nb_pred))

#Creating and training a KNN model with 5 nearest neighbours
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)

#Predicting the Values using the newly training model
y_pred = model.predict(x_test)

print("Accuracy for KNN         ",metrics.accuracy_score(y_test, y_pred))


###################### CROSS VALIDATION SVM VS SVM WITH RBF KERNEL##################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import warnings
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import datasets

irisdataset = datasets.load_iris()
import seaborn as sns

X = irisdataset.data
y = irisdataset.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0,test_size=0.2)
#Creating and Training SVM with RBF Kernel
svmrbf = SVC(kernel='rbf', random_state=0, gamma=.01, C=1)
svmrbf.fit(X_train,y_train)

print('Accuracy of SVM RBF classifier on training set: {:.2f}'.format(svmrbf.score(X_train, y_train)))
print('Accuracy of SVM RBF classifier on test set: {:.2f}'.format(svmrbf.score(X_test, y_test)))

#Creating and Training SVM without RBF
svm = SVC()
svm.fit(X_train, y_train)

print('Accuracy of SVM classifier on training set: {:.2f}'.format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'.format(svm.score(X_test, y_test)))