## Loads preprocessed train and test data, splits the test data to 10 parts,
# omits all the "type" attributes and applies linear regression to each of
# the data parts

import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score
from movie_lengths_lib import *

print ("Loading data from files")

X_train = load_data_from_file ( file_X_train )
y_train = load_data_from_file ( file_y_train )
X_test = load_data_from_file ( file_X_test )
y_test = load_data_from_file ( file_y_test )
header = load_data_from_file ( file_header )

print ("X_train shape: {}".format(X_train.shape))
print ("y_train shape: {}".format(y_train.shape))
print ("X_test shape: {}".format(X_test.shape))
print ("y_test shape: {}".format(y_test.shape))
print ()

X_train = X_train[:,:31]
y_train = y_train[:,:31]
X_test = X_test[:,:31]
y_test = y_test[:,:31]
header = header[:31]

print ("'Type' attributes omitted")
print ()

#------------------------------------------------------------------------------

t = X_train.shape[0]

print ("Training each 1/10 of the data:")

for i in range(10):
    print("----------------------------------------------------------")
    start = int(i*t/10)
    stop = int((i+1)*t/10)
    data_X = X_train[start:stop,:]
    data_y = y_train[start:stop]
    linear_regression = LinearRegression(fit_intercept=True, normalize=True, copy_X=True)
    theta = linear_regression.fit(data_X, data_y)
    kf = KFold(n_splits=10)
    train_score = (cross_val_score(linear_regression, data_X, data_y, cv=kf)).mean()
    print("Train score: {}".format(train_score))
    test_score = linear_regression.score(X_test, y_test)
    print("Test score: {}".format(test_score))