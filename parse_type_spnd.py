#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import re
mfile = open('new_sent_vybfin (1).txt','r', encoding='utf-8')
corpus = []
for t in mfile:
 corpus.append(t)
mfile.close()

tek = []
plan = []
fact = []

m = 0
for i in corpus:
 result = re.search(r'текущ', i)
 if result !=None:
  m+=1
  tek.append(i)
  result = None
 else:
  result = re.search(r'планов', i)
  if result !=None:
   m+=1
   plan.append(i)
   result = None
  else:
   result = re.search(r'фактическ', i)
   if result !=None:
    m+=1
    fact.append(i)
    result = None

l=0
for i in plan:
 file = open('type_spendings/plan/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in fact:
 file = open('type_spendings/fact/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in tek:
 file = open('type_spendings/tek/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
