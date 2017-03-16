#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import re
mfile = open('new_sent_vybfin (1).txt','r', encoding='utf-8')
corpus = []
for t in mfile:
 corpus.append(t)
mfile.close()

spending = []
deficit = []
revenue = []

k = 0
for i in corpus:
 result = re.search(r'расходы', i)
 if result != None:
  k+=1
  spending.append(i)
  result = None
 else:
  result = re.search(r'затраты', i)
  if result != None:
   k+=1
   spending.append(i)
   result = None
  else:
   result = re.search(r'траты', i)
   if result != None:
    k+=1
    spending.append(i)
    result = None
   else:
    result = re.search(r'издержки',i)
    if result != None:
     k+=1
     spending.append(i)
     result = None

file = open('spndng.txt', 'w', encoding='utf-8')
file.writelines('%s/n' % i for i in spending)
file.close()

m = 0
for i in corpus:
 result = re.search(r'дефицит', i)
 if result != None:
  m+=1
  deficit.append(i)
  result = None
 else:
  result = re.search(r'недостаток', i)
  if result != None:
   m+=1
   deficit.append(i)
   result = None
  else:
   result = re.search(r'нехватка', i)
   if result != None:
    m+=1
    deficit.append(i)
    result = None
   else:
    result = re.search(r'недостача', i)
    if result != None:
     m+=1
     deficit.append(i)
     result = None

file = open('dfct.txt', 'w', encoding='utf-8')
file.writelines('%s/n' % i for i in deficit)
file.close()
 
n = 0
for i in corpus:
 result = re.search(r'доходы', i)
 if result != None:
  n+=1
  revenue.append(i)
  result = None
 else:
  result = re.search(r'профицит', i)
  if result != None:
   n+=1
   revenue.append(i)
   result = None
  else:
   result = re.search(r'профит', i)
   if result != None:
    n+=1
    revenue.append(i)
    result = None
   else:
    result = re.search(r'поступления', i)
    if result != None:
     n+=1
     revenue.append(i)
     result = None
    else:
     result = re.search(r'получения', i)
     if result != None:
      n+=1
      revenue.append(i)
      result = None

file = open('rvn.txt', 'w', encoding='utf-8')
file.writelines('%s/n' % i for i in revenue)
file.close()
   
print('spendings: ',k,' deficit: ',m,' revenue: ',n)
