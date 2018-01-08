## Outputs various statistics about the dataset

import json
import numpy as np
from movie_lengths_lib import *
from matplotlib import pyplot as plt

print ("Loading data from files:")

data = load_data_from_file ( file_data )
header = load_data_from_file ( file_header )

print ("data shape: {}".format(data.shape))
print ()

#------------------------------------------------------------------------------

# Counts and prints average movie length for each movie type
# Types are columns 31-40
# Each movie has only one type so we can create a mask of avg length per type

print ( " ATTRIBUTE | NUMBER OF SAMPLES" )
print ( "------------------------------" )

for col in range (41):
    if col in (1,2):
        continue
    condition = (data[:,col] == 1)
    print ( "{:12s}{:20d}".format(header[0,col], np.sum(condition)) )
print ( "------------------------------" )
print ()

print ( "Average movie length: {}".format(int(np.mean(data[:,-1], axis=0))) )
print ( "Minimal movie length: {}".format(np.min(data[:,-1], axis=0)) )
print ( "Maximal movie length: {}".format(np.max(data[:,-1], axis=0)) )
print ( "Std of movie length: {}".format(int(np.std(data[:,-1], axis=0))) )
print ()
print ( "Average movie year: {}".format(int(np.mean(data[:,1], axis=0))) )
print ( "Minimal movie year: {}".format(np.min(data[:,1], axis=0)) )
print ( "Maximal movie year: {}".format(np.max(data[:,1], axis=0)) )
print ( "Std of movie year: {}".format(int(np.std(data[:,1], axis=0))) )
print ()
print ( "Average director year: {}".format(int(np.mean(data[:,2], axis=0))) )
print ( "Minimal director year: {}".format(np.min(data[:,2], axis=0)) )
print ( "Maximal director year: {}".format(np.max(data[:,2], axis=0)) )
print ( "Std of director year: {}".format(int(np.std(data[:,2], axis=0))) )
print ()
age = data[:,1] - data[:,2]
print ( "Average director age: {}".format(int(np.mean(age, axis=0))) )
print ( "Std of director age: {}".format(int(np.std(age, axis=0))) )

#------------------------------------------------------------------------------
# Visualization

#plt.xlabel ("Rok vydania snímky")
#plt.ylabel ("Dĺžka snímky")
#plt.scatter (data[:,1].tolist(), data[:,-1].tolist(), marker='x')
#plt.show()

#plt.xlabel ("Rok vydania snímky")
#plt.ylabel ("Dĺžka snímky")
#plt.ylim (ymax=1000)
#plt.scatter (data[:,1].tolist(), data[:,-1].tolist(), marker='x')
#plt.show()

#plt.xlabel ("Vek režiséra snímky")
#plt.ylabel ("Dĺžka snímky")
#plt.scatter (age.tolist(), data[:,-1].tolist(), marker='x')
#plt.show()

#plt.xlabel ("Vek režiséra snímky")
#plt.ylabel ("Dĺžka snímky")
#plt.ylim (ymax=1000)
#plt.scatter (age.tolist(), data[:,-1].tolist(), marker='x')
#plt.show()

# types

data_type = []

for d in data:
    data_type.append (header[0,31+np.argmax(d[0,31:41])])
    
plt.xlabel ("Typ snímky")
plt.ylabel ("Dĺžka snímky")
plt.scatter (data_type, data[:,-1].tolist(), marker='x')
plt.show()

plt.xlabel ("Typ snímky")
plt.ylabel ("Dĺžka snímky")
plt.ylim (ymax=1000)
plt.scatter (data_type, data[:,-1].tolist(), marker='x')
plt.show()
