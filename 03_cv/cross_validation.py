#!/usr/bin/env python


import numpy as np
import pandas as pd
from ggplot import *

from sklearn.linear_model import LogisticRegression as LR
from sklearn.metrics import confusion_matrix
from sklearn import cross_validation


TRAIN_FILE = 'logit-train.csv'
TEST_FILE = 'logit-test.csv'
TEST_PCT = 0.3
PENALTY = 'l2'
K = 10


def preprocess_data(train_file=TRAIN_FILE,test_file=TEST_FILE):
    """Load data from csv file, perform preprocessing and return df."""

    # load dataset, drop na's
    train = pd.read_csv(train_file).dropna()
    test = pd.read_csv(test_file).dropna()
    #Training Set
    trainX = train.drop('heartdisease::category|0|1',1)
    trainY = train['heartdisease::category|0|1']
    print 'training set loaded'
    #Test Set
    testX = test.drop('heartdisease::category|0|1',1)
    testY = test['heartdisease::category|0|1']
    print 'test set loaded'
    return trainX,trainY,testX,testY

def run_model(X,Y,test_pct=TEST_PCT,penalty = PENALTY,k=K):
    """Perform train/test split, fit model and output results."""
    #Divide into test/training via cross_validation
    #A random split into training and test sets can be quickly computed with the train_test_split helper function
    #http://scikit-learn.org/stable/modules/cross_validation.html
    X_train, X_val, y_train, y_val = cross_validation.train_test_split(X, Y, test_size=test_pct)
    #Inverse of regularization strength. Smaller values specify stronger regularization
    C= np.arange(50,0,-1)
    accuracy_train = np.zeros(len(C))
    accuracy_test = np.zeros(len(C))
    for i,c in enumerate(C):
        # initialize the instance & specify regulartization parameter & perform fit
        # L1 : Lasso, L2: Ridge
        clf = LR(penalty=penalty,C=c)
        #k-fold cross validation. For Leave-One-Out set k to length of the training set. 
        #When the cv argument is an integer, cross_val_score uses the KFold strategies by default.
        #Explicity setting the scoring parameter. Accuracy measures the fraction (default) or the number of correct predictions.
        #With mean() we calculate the average error rate across folds. 
        accuracy_train[i] = cross_validation.cross_val_score(clf, X_train, y_train, cv=k,scoring='accuracy').mean()
        #Test
        clf.fit(X_train,y_train)
        accuracy_test[i] = clf.score(X_val, y_val)
        print 'Accuracy training set: {0} and test set :  {1} for C: {2}'.\
            format(accuracy_train[i], accuracy_test[i], c)
    #Plot 
    df = pd.DataFrame({'Test':accuracy_test, 'Train':accuracy_train,'Regularization_parameter':C})
    df = pd.melt(df,id_vars= ['Regularization_parameter'])
    g  = (ggplot(df, aes(x='Regularization_parameter', y='value', colour='variable')) 
        + geom_line() + scale_x_reverse() + ylab('Accuracy'))
    print 'saving the plot ... '
    ggsave(g,'plot.jpg')



    # # get model outputs
    # inputs = map(str, train_x.columns.format())
    # coeffs = model.coef_[0]
    # accuracy = model.score(test_x, test_y)

    # predicted_y = model.predict(test_x)
    # cm = confusion_matrix(test_y, predicted_y)

    # print 'inputs = {0}'.format(inputs)
    # print 'coeffs = {0}'.format(coeffs)
    # print 'accuracy = {0}'.format(accuracy)     # mean 0/1 loss
    # print 'confusion matrix:\n', cm, '\n'

if __name__ == '__main__':

    trainX,trainY,testX,testY = preprocess_data()
    run_model(trainX,trainY)



