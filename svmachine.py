#!/usr/bin/env python
#-*- coding: UTF-8 -*-
from re import sub

#Choose one of the 'categories' array depending on what classes you want to get in the end

#categories = ['deficit', 'revenue', 'spending']
#categories = ['dalnevostochnyi', 'habarovskyi', 'rf', 'rostovskaya']
#categories = ['fact','tek','plan']
categories = ['culture','defence','ecology','economics','education','establishment','government','medicine','security','social','sports']

from sklearn.datasets import load_files
twenty_train = load_files("sphere_spending_train",categories=categories)

from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print(X_train_counts.shape)

#Printing the number of a word in u'...' from the dictionary
#print(count_vect.vocabulary_.get(u'расходы'))

from sklearn.feature_extraction.text import TfidfTransformer

tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
X_train_tf.shape

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape

#Adding the Naive Bayes classificator in order to compare 2 algorithms

from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

docs_new = ['дефицит о экономику 1866 год в севастополя','поступления без экономики 1944 год в вологодскую','дефицит от образование 2000 год в центральным']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
 print('%r => %s' % (doc, twenty_train.target_names[category]))

from sklearn.pipeline import Pipeline

text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])
text_clf = text_clf.fit(twenty_train.data, twenty_train.target)

#Testing the Naive Bayes classificator on a test dataset
import numpy as np

twenty_test = load_files("sphere_spending_test", categories=categories)
docs_test = twenty_test.data
predicted = text_clf.predict(docs_test)
print('bayes: '+str(np.mean(predicted == twenty_test.target)))

#Using SVM instead of NB (note that the 'clf' parameter has changed)
from sklearn.linear_model import SGDClassifier

text_clf = Pipeline([('vect', CountVectorizer()),
 ('tfidf', TfidfTransformer()),
 ('clf', SGDClassifier(loss='hinge', penalty='l2',
       alpha=1e-3, n_iter=5, random_state=42))])
	  
text_clf = text_clf.fit(twenty_train.data, twenty_train.target)
predicted = text_clf.predict(docs_test)
print('svm: '+str(np.mean(predicted == twenty_test.target)))

#Printing some more detailed analysis
from sklearn import metrics

print(metrics.classification_report(twenty_test.target, predicted, target_names=twenty_test.target_names))

print(metrics.confusion_matrix(twenty_test.target, predicted))

#I personaly didn't use parameter tuning here, but you can use code below to perform it:
"""
from sklearn.model_selection import GridSearchCV
parameters = {'vect_ngram_range':[(1,1),(1,2)], 'tfidf_use_idf':(True,False), 'clf_alpha':(1e-2,1e-3)}
gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)
gs_clf = gs_clf.fit(twenty_train.data,twenty_train.target)
print(twenty_train.target_names[gs_clf.predict(['траты о жкх 1996 год в магаданской'])[0]])
"""

