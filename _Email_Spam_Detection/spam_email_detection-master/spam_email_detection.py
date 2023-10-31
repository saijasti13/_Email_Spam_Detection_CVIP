# -*- coding: utf-8 -*-

import os
import email
from utility import read_email

DATA_DIR = r'data\'
LABEL_FILE = r'full\index'

labels = {}

with open(LABEL_FILE,'r') as f:
    for line in f:
        label, key = line.split()
        if label == 'ham':
            labels[key.split('/')[-1]] = 0
        else:
            labels[key.split('/')[-1]] = 1

    
X, y = read_email(labels, DATA_DIR)

print(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, random_state = 2)

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
X_train_vector = vectorizer.fit_transform(X_train)
X_test_vector = vectorizer.transform(X_test)

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Initialize the classifier and make label predictions
mnb = MultinomialNB()
mnb.fit(X_train_vector, y_train)
y_pred = mnb.predict(X_test_vector)

# Print results
print(classification_report(y_test, y_pred, target_names=['Spam', 'Ham']))
print('Classification accuracy {:.1%}'.format(accuracy_score(y_test, y_pred)))   
    
    
    
    
    
    
    
    
    
    
