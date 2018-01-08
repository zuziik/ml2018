## Loads preprocessed train and test data, splits the test data to 10 parts,
# and applies heuristic to each of the data parts

import json
import numpy as np
from movie_lengths_lib import *

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

t = X_train.shape[0]

print ("Training each 1/10 of the data:")

for i in range(10):
    print("----------------------------------------------------------")
    start = int(i*t/10)
    stop = int((i+1)*t/10)
    data_X = X_train[start:stop, :]
    data_y = y_train[start:stop]
    
    coeffs = np.zeros(41)
    for col in range (31,41):
        condition = (data_X[:,col] == 1)
        avg = np.mean (np.extract (condition, data_y))
        coeffs[col] = avg
    coeffs = coeffs.reshape((coeffs.shape[0], 1))
        
    train_score = get_score(data_X, data_y, coeffs)
    print("Train score: {}".format(train_score))
    test_score = get_score(X_test, y_test, coeffs)
    print("Test score: {}".format(test_score))