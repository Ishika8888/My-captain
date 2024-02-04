# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kSUaV5ydINHWr1jLwVPXtWfXvDaU-LtB
"""

# Commented out IPython magic to ensure Python compatibility.
#importing dependencies
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
# %matplotlib inline

#using pandas to read database stored in the folder
data=pd.read_csv("mnist.csv")

#viewing column heads
data.head()

#extracting data from dataset and viewing them up close
a= data.iloc[3,1:].values

#reshaping the extracted data into resonable size
a= a.reshape(28,28).astype('uint8')
plt.imshow(a)

#prepairing the data
#saperating labels and data values
df_x= data.iloc[:,1:]
df_y= data.iloc[:,0]

#creating test and train series
x_train, x_test, y_train, y_test= train_test_split(df_x, df_y,test_size = 0.2, random_state=4)

#check data
x_train.head()
y_train.head()

#call rf classifier
rf= RandomForestClassifier(n_estimators=100)

# fit the model
rf.fit(x_train, y_train)

# prediction on test data
pred= rf.predict(x_train)
pred()

# check prediction accuracy
s = y_test.values

# calculate number of correctly predicted values
count = 0
for i in range(len(pred)):
  if pred[i] == s[i]:
    count= count+1
count()

#total values that the prediction code was run on
len(pred)

# accuracy value
8090/8400