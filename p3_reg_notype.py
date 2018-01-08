## Loads preprocessed train and test data, omits the 'type'
# attributes, applies linear regression
# and generalized linear regression to the data

import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import cross_val_score
from movie_lengths_lib import *

#------------------------------------------------------------------------------

print ("Loading data from files")

X_train = load_data_from_file ( file_X_train )
y_train = load_data_from_file ( file_y_train )
X_test = load_data_from_file ( file_X_test )
y_test = load_data_from_file ( file_y_test )
header = load_data_from_file ( file_header )

X_train = X_train[:,:31]
y_train = y_train[:,:31]
X_test = X_test[:,:31]
y_test = y_test[:,:31]
header = header[:,:31]

print ("'Type' attribute ommited")

print ("X_train shape: {}".format(X_train.shape))
print ("y_train shape: {}".format(y_train.shape))
print ("X_test shape: {}".format(X_test.shape))
print ("y_test shape: {}".format(y_test.shape))
print ()

print ("Linear regression:")
linear_regression = LinearRegression(fit_intercept=True, normalize=True, copy_X=True)
theta = linear_regression.fit(X_train, y_train)


print ("ATTRIBUTE    | COEFFICIENT")
print ("-----------------------------------------")
for col in range(header.shape[1]):
    print ( "{:15s}{}".format(header[0,col], linear_regression.coef_[0,col]) )
print ("-----------------------------------------")

kf = KFold(n_splits=10)
train_score = (cross_val_score(linear_regression, X_train, y_train, cv=kf)).mean()
test_score = linear_regression.score(X_test, y_test)
print("Train score: {}".format(score))
print("Test score: {}".format(test_score))


print ()
print ("Generalized linear regression on first 500 samples")

def polynomial(X_train, y_train, X_test, y_test, k):
    print ("-----------------------------------------")
    print ("k = {}".format(k))
    poly = PolynomialFeatures(degree=k)
    X_train_t = poly.fit_transform(X_train)
    X_test_t = poly.fit_transform(X_test)
    linear_regression = LinearRegression(fit_intercept=True, normalize=True, copy_X=True)
    theta = linear_regression.fit(X_train_t, y_train)
    kf = KFold(n_splits=10)
    train_score = (cross_val_score(linear_regression, X_train_t, y_train, cv=kf)).mean()
    test_score = linear_regression.score(X_test_t, y_test)
    print("Train score: {}".format(train_score))
    print("Test score: {}".format(test_score))

for i in range(1,5):
    polynomial(X_train[:500,:], y_train[:500,:], X_test[:500,:], y_test[:500,:], i)