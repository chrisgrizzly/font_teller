# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 07:43:46 2019

@author: venkatesh avula
"""
from PIL import ImageFont, ImageDraw, Image, ImageFilter
import Lib
from Lib import add_noise_img, ImgData, ImgSize, Fonts, MakeDataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import shuffle
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.decomposition import PCA
#inputs---------------------------------------------------
N=500

#build dataset
x,y=MakeDataset(N)        
x, y = shuffle(x, y, random_state=10)



#Split The Data Into Train And Test Sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)



# Build A Random Forest Classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train.ravel())


#Predict
preds = clf.predict(X_test)


## Create confusion matrix
#pd.crosstab(y_test.ravel(), preds, rownames=['Actual Fonts'], colnames=['Predicted Fonts']);
#mat = confusion_matrix(y_test, preds)
#sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
#plt.xlabel('true label')
#plt.ylabel('predicted label');



#classification report for this classifier
#print(metrics.classification_report(preds, y_test))


#Check The Accuracy Of The Model
print("Accuracy:", accuracy_score(y_test,preds))

#dataset = sns.load_dataset('titanic')
#dataset.head()

##statistical distribution of data
#sns.distplot(x[:,1])  
#sns.distplot(x[:,400])  
##The Rug Plot
#sns.rugplot(x[:,400])  


#Check Feature Importance
#list(zip(X_train, clf.feature_importances_))




#PCA---------------------------------------------------
pca = PCA()  
X_train2 = pca.fit_transform(X_train)  
X_test2 = pca.transform(X_test) 
explained_variance = pca.explained_variance_ratio_  


pca = PCA(n_components=36)  
X_train = pca.fit_transform(X_train)  
X_test = pca.transform(X_test)  


# Build A Random Forest Classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train.ravel())

#Predict
preds = clf.predict(X_test)

#Check The Accuracy Of The Model
print("Accuracy:", accuracy_score(y_test,preds))




