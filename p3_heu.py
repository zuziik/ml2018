## Loads preprocessed train and test data
# and applies a heuristic to the data

import json
import numpy as np
from movie_lengths_lib import *

# Computes predicted values for each training sample - chooses the average value for the respective movie type
# Computes and returns the score computed as in sklearn.linear_model.LinearRegression (so that we can compare it):
    #The coefficient R^2 is defined as (1 - u/v), where u is the residual sum of squares ((y_true - y_pred) ** 2).sum() and v is the total sum of squares ((y_true - y_true.mean()) ** 2).sum(). The best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). A constant model that always predicts the expected value of y, disregarding the input features, would get a R^2 score of 0.0.
def get_score (X, y_true, coeffs):
    y_pred = np.sum(X*coeffs, axis=1)
    y_pred, = np.array(y_pred.T)
    y_true, = np.array(y_true.T)
    a = y_true - y_pred
    b = a**2
    u = a.sum(axis=0)
    u = ((y_true - y_pred) ** 2).sum()
    v = ((y_true - y_true.mean()) ** 2).sum()
    return 1 - u/v

#------------------------------------------------------------------------------

print ("Loading data from files:")

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

#------------------------------------------------------------------------------

print ("Computing heuristic estimates based on movie types:")
print ()

coeffs = np.zeros(41)

# Counts and prints average movie length for each movie type
# Types are columns 31-40
# Each movie has only one type so we can create a mask of avg length per type

print ( "MOVIE TYPE | NUMBER OF SAMPLES | AVERAGE LENGTH" )
print ( "-----------------------------------------------" )
for col in range (31,41):
    condition = (X_train[:,col] == 1)
    avg = np.mean (np.extract (condition, y_train))
    coeffs[col] = avg
    print ( "{:12s}{:20d}{:15.2f}".format(header[0,col], np.sum(condition), avg) )
print ( "-----------------------------------------------" )
print ()

coeffs = coeffs.reshape((coeffs.shape[0], 1))

#------------------------------------------------------------------------------

train_score = get_score(X_train, y_train, coeffs)
print("Train score: {}".format(train_score))
test_score = get_score(X_test, y_test, coeffs)
print("Test score: {}".format(test_score))