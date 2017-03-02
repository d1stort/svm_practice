#!/usr/bin/env python
#-*- coding: UTF-8 -*-
from re import sub

categories = ['deficit', 'revenue', 'spending']

from sklearn.datasets import load_files
twenty_train = load_files("datatron_requests_pt2")

from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
X_train_counts.shape

count_vect.vocabulary_.get(u'algorithm')

from sklearn.feature_extraction.text import TfidfTransformer

tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
X_train_tf.shape

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape

from sklearn.naive_bayes import MultinomialNB

# clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

# docs_new = ['God is love', 'OpenGL on the GPU is fast']
# X_new_counts = count_vect.transform(docs_new)
# X_new_tfidf = tfidf_transformer.transform(X_new_counts)

# predicted = clf.predict(X_new_tfidf)

# for doc, category in zip(docs_new, predicted):
  # print('%r => %s' % (doc, twenty_train.target_names[category]))

from sklearn.pipeline import Pipeline

text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])
text_clf = text_clf.fit(twenty_train.data, twenty_train.target)

import numpy as np

twenty_test = load_files("datatron_requests")
docs_test = twenty_test.data
predicted = text_clf.predict(docs_test)
np.mean(predicted == twenty_test.target)

from sklearn.linear_model import SGDClassifier

text_clf = Pipeline([('vect', CountVectorizer()),
 ('tfidf', TfidfTransformer()),
 ('clf', SGDClassifier(loss='hinge', penalty='l2',
       alpha=1e-3, n_iter=5, random_state=42))])
	  
text_clf = text_clf.fit(twenty_train.data, twenty_train.target)
predicted = text_clf.predict(docs_test)
print(np.mean(predicted == twenty_test.target))

from sklearn import metrics

print(metrics.classification_report(twenty_test.target, predicted, target_names=twenty_test.target_names))

print(metrics.confusion_matrix(twenty_test.target, predicted))



