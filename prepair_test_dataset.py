#!/usr/bin/env python
#-*- coding: CP1251 -*-

from re import sub

co = open('text.txt')
corpus=[]
categories=[]
for i in co:
    corpus.append(sub('#.+\n?','',i))
    categories.append(sub('\n|[^#]+#','',i))
categories=list(set(categories))

file = open('tiny_test_dataset.txt', 'w', encoding='utf-8')
for i in corpus:
 file.write(i+'\n')
file.close()

print(corpus,categories)
