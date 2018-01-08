## Definitions of some constants and utility functions

import json
import numpy as np

dir_raw = "data_raw/"
dir_clean = "data_clean/"
file_title = dir_raw + "title.basics.tsv"
file_crew = dir_raw + "title.crew.tsv"
file_name = dir_raw + "name.basics.tsv"
file_X_test = dir_clean + "X_test.json"
file_y_test = dir_clean + "y_test.json"
file_X_train = dir_clean + "X_train.json"
file_y_train = dir_clean + "y_train.json"
file_data = dir_clean + "data_all.json"
file_header = dir_clean + "header.json"

def load_data_from_file ( filename ):
    with open ( filename, 'r' ) as f:
        s = f.read ()
    a = json.loads (s)
    return np.matrix (a)

def dump_data_to_file ( data, filename ):
    s = json.dumps ( data.tolist() )
    with open ( filename, 'w' ) as f:
        f.write (s)
        
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