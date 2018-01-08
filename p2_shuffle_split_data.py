## Shuffles all the data and splits them into a train and test set

import numpy as np
from movie_lengths_lib import *

print ( "Starting data loading..." )
data = load_data_from_file ( file_data )
print ( "--- {}".format(file_data) )
print ( "Loaded data from files, {} lines".format(len(data)) )
print ()

#shuffle data
np.random.shuffle (data)
print ( "Data shuffled" )

# split data 80:20
t = data.shape[0]
last = data.shape[1]-1
train_stop = int (4*t/5)

X_train = np.delete(data[:train_stop], last, axis = 1)
y_train = data[:train_stop, last]

X_test = np.delete(data[train_stop:], last, axis = 1)
y_test = data[train_stop:, last]

print ( "Data split 80:20" )
print ( "Shape of training set: {}, shape of test set: {}".format(X_train.shape, X_test.shape) )
print ()

print ( "Saving data to files" )
for (d, fn) in [(X_train, file_X_train), (y_train, file_y_train), (X_test, file_X_test), (y_test, file_y_test)]:
    dump_data_to_file ( d, fn )
    print ( "--- {}".format(fn) )