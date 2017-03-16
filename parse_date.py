#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import re
mfile = open('new_sent_vybfin (1).txt','r', encoding='utf-8')
corpus = []
for t in mfile:
 corpus.append(t)
mfile.close()

years16 = []
years15 = []
years14 = []
years13 = []
years12 = []
years11 = []
years10 = []
years09 = []
years08 = []
years07 = []

t = 0
for i in corpus:
 result = re.search(r'2016', i)
 if result != None:
  t+=1
  years16.append(i)
  result = None
 else:
  result = re.search(r'2015', i)
  if result != None:
   t+=1
   years15.append(i)
   result = None
  else:
   result = re.search(r'2014', i)
   if result != None:
    t+=1
    years14.append(i)
    result = None
   else:
    result = re.search(r'2013', i)
    if result != None:
     t+=1
     years13.append(i)
     result = None
    else:
     result = re.search(r'2012', i)
     if result != None:
      t+=1
      years12.append(i)
      result = None
     else:
      result = re.search(r'2011', i)
      if result != None:
       t+=1
       years11.append(i)
       result = None
      else:
       result = re.search(r'2010', i)
       if result != None:
        t+=1
        years10.append(i)
        result = None
       else:
        result = re.search(r'2009', i)
        if result != None:
         t+=1
         years09.append(i)
         result = None
        else:
         result = re.search(r'2008', i)
         if result != None:
          t+=1
          years08.append(i)
          result = None
         else:
          result = re.search(r'2007', i)
          if result != None:
           t+=1
           years07.append(i)
           result = None
  
print(str(len(years16))+' '+str(len(years15))+' '+str(len(years14))+' '+str(len(years13))+' '+str(len(years12))+' '+str(len(years11))+' '+str(len(years10))+' '+str(len(years09))+' '+str(len(years08))+' '+str(len(years07)))
