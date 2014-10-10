#!/usr/bin/env python
# author: Jason Dolatshahi

import StringIO

import pydot
import sklearn.cross_validation as cv
from sklearn import tree
from sklearn.datasets import load_digits

TRAIN_PCT = 0.9
def main(n=3):

    print 'n_class = {0}'.format(n)
    digits = load_digits(n_class=n)

    # perform train/test split
    tts = cv.train_test_split(digits.data, digits.target, train_size=TRAIN_PCT)
    train_features, test_features, train_labels, test_labels = tts

    # train model
    clf = tree.DecisionTreeClassifier()
    clf.fit(train_features, train_labels)

    # get genlzn accuracy
    acc = round(100 * clf.score(test_features, test_labels), 0)
    print 'accuracy = {0} %'.format(acc)

    # save dec tree graph as pdf
    # dot_data = StringIO.StringIO() 
    # tree.export_graphviz(clf, out_file=dot_data)
    # graph = pydot.graph_from_dot_data(dot_data.getvalue())
    # graph.write_pdf('tree.pdf')

if __name__ == '__main__':
    main()
