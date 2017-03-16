#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import re
mfile = open('tiny_test_dataset.txt','r', encoding='utf-8')
corpus = []
for t in mfile:
 corpus.append(t)
mfile.close()

gos = []
sec = []
defence = []
econ = []
zhkh=[]
eco = []
edu = []
cul=[]
med=[]
soc=[]
sport=[]

t=0
for i in corpus:
 result = re.search(r'жкх', i)
 if result !=None:
  t+=1
  zhkh.append(i)
  result = None
 else:
  result = re.search(r'жилищно', i)
  if result !=None:
   t+=1
   zhkh.append(i)
   result = None
  else:
   result = re.search(r'хозяйств', i)
   if result !=None:
    t+=1
    zhkh.append(i)
    result = None
   else:
    result = re.search(r'благоутр', i)
    if result != None:
     t+=1
     zhkh.append(i)
     result = None
    else:
     result = re.search(r'теплоснабж', i)
     if result !=None:
      t+=1
      zhkh.append(i)
      result = None
     else:
      result = re.search(r'отоплен', i)
      if result !=None:
       t+=1
       zhkh.append(i)
       result = None
      else:
       result = re.search(r'электроснабж', i)
       if result !=None:
        t+=1
        zhkh.append(i)
        result = None
       else:
        result = re.search(r'обслуж', i)
        if result !=None:
         t+=1
         zhkh.append(i)
         result = None
        else:
         result = re.search(r'подъезд', i)
         if result !=None:
          t+=1
          zhkh.append(i)
          result = None
         else:
          result = re.search(r'инженер', i)
          if result !=None:
           t+=1
           zhkh.append(i)
           result = None
          else:
           result = re.search(r'утилиз', i)
           if result !=None:
            t+=1
            zhkh.append(i)
            result = None
           else:
            result = re.search(r'мусор', i)
            if result !=None:
             t+=1
             zhkh.append(i)
             result = None
            else:
             result = re.search(r'уборк', i)
             if result !=None:
              t+=1
              zhkh.append(i)
              result = None
             else:
              result = re.search(r'ремонт', i)
              if result !=None:
               t+=1
               zhkh.append(i)
               result = None
              else:
               result = re.search(r'водоснабж', i)
               if result !=None:
                t+=1
                zhkh.append(i)
                result = None
               else:
                result = re.search(r'комунал', i)
                if result !=None:
                 t+=1
                 zhkh.append(i)
                 result = None

for i in corpus:
 result = re.search(r'образован', i)
 if result !=None:
  t+=1
  edu.append(i)
  result = None
 else:
  result = re.search(r'обуч', i)
  if result !=None:
   t+=1
   edu.append(i)
   result = None
  else:
   result = re.search(r'просвещен', i)
   if result !=None:
    t+=1
    edu.append(i)
    result = None

for i in corpus:
 result = re.search(r'окружающ', i)
 if result !=None:
  t+=1
  eco.append(i)
  result = None
 else:
  result = re.search(r'эколог', i)
  if result !=None:
   t+=1
   eco.append(i)
   result = None

for i in corpus:
 result = re.search(r'культура ', i)
 if result !=None:
  t+=1
  edu.append(i)
  result = None
 else:
  result = re.search(r'культуру', i)
  if result !=None:
   t+=1
   edu.append(i)
   result = None
  else:
   result = re.search(r'культуре', i)
   if result !=None:
    t+=1
    edu.append(i)
    result = None
	
for i in corpus:
 result = re.search(r'кинематогр', i)
 if result !=None:
  t+=1
  cul.append(i)
  result = None
 else:
  result = re.search(r'кино', i)
  if result !=None:
   t+=1
   cul.append(i)
   result = None
  else:
   result = re.search(r'театр', i)
   if result !=None:
    t+=1
    cul.append(i)
    result = None
   else:
    result = re.search(r'музык', i)
    if result != None:
     t+=1
     cul.append(i)
     result = None
    else:
     result = re.search(r'концерт', i)
     if result !=None:
      t+=1
      cul.append(i)
      result = None
     else:
      result = re.search(r'нашест', i)
      if result !=None:
       t+=1
       cul.append(i)
       result = None
      else:
       result = re.search(r'фестив', i)
       if result !=None:
        t+=1
        cul.append(i)
        result = None
       else:
        result = re.search(r'искусст', i)
        if result !=None:
         t+=1
         cul.append(i)
         result = None

for i in corpus:
 result = re.search(r'здрав', i)
 if result !=None:
  t+=1
  med.append(i)
  result = None
 else:
  result = re.search(r'здоров', i)
  if result !=None:
   t+=1
   med.append(i)
   result = None
  else:
   result = re.search(r'медиц', i)
   if result !=None:
    t+=1
    med.append(i)
    result = None
	
for i in corpus:
 result = re.search(r'социал', i)
 if result !=None:
  t+=1
  soc.append(i)
  result = None
 else:
  result = re.search(r'обществ', i)
  if result !=None:
   t+=1
   soc.append(i)
   result = None
   
for i in corpus:
 result = re.search(r'безопасн', i)
 if result !=None:
  t+=1
  sec.append(i)
  result = None
 else:
  result = re.search(r'защит', i)
  if result !=None:
   t+=1
   sec.append(i)
   result = None
   
for i in corpus:
 result = re.search(r'госуд', i)
 if result !=None:
  t+=1
  gos.append(i)
  result = None
 else:
  result = re.search(r'эконом', i)
  if result !=None:
   t+=1
   econ.append(i)
   result = None
   
for i in corpus:
 result = re.search(r'оборон', i)
 if result !=None:
  t+=1
  defence.append(i)
  result = None
		 
for i in corpus:
 result = re.search(r'спорт', i)
 if result !=None:
  t+=1
  sport.append(i)
  result = None
 else:
  result = re.search(r'спидвей', i)
  if result !=None:
   t+=1
   sport.append(i)
   result = None
  else:
   result = re.search(r'четырехб', i)
   if result !=None:
    t+=1
    sport.append(i)
    result = None
   else:
    result = re.search(r'шестибор', i)
    if result != None:
     t+=1
     sport.append(i)
     result = None
    else:
     result = re.search(r'ринк', i)
     if result !=None:
      t+=1
      sport.append(i)
      result = None
     else:
      result = re.search(r'скалолаз', i)
      if result !=None:
       t+=1
       sport.append(i)
       result = None
      else:
       result = re.search(r'сноуборд', i)
       if result !=None:
        t+=1
        sport.append(i)
        result = None
       else:
        result = re.search(r'тобоган', i)
        if result !=None:
         t+=1
         sport.append(i)
         result = None
        else:
         result = re.search(r'ушу', i)
         if result !=None:
          t+=1
          sport.append(i)
          result = None
         else:
          result = re.search(r'шорт', i)
          if result !=None:
           t+=1
           sport.append(i)
           result = None
          else:
           result = re.search(r'коньк', i)
           if result !=None:
            t+=1
            sport.append(i)
            result = None
           else:
            result = re.search(r'лыж', i)
            if result !=None:
             t+=1
             sport.append(i)
             result = None
            else:
             result = re.search(r'парашют', i)
             if result !=None:
              t+=1
              sport.append(i)
              result = None
             else:
              result = re.search(r'мини', i)
              if result !=None:
               t+=1
               sport.append(i)
               result = None
              else:
               result = re.search(r'могул', i)
               if result !=None:
                t+=1
                sport.append(i)
                result = None
               else:
                result = re.search(r'яхтинг', i)
                if result !=None:
                 t+=1
                 sport.append(i)
                 result = None
                else:
                 result = re.search(r'физ', i)
                 if result !=None:
                  t+=1
                  sport.append(i)
                  result = None

for i in corpus:
 result = re.search(r'самбо', i)
 if result !=None:
  t+=1
  sport.append(i)
  result = None
 else:
  result = re.search(r'шашк', i)
  if result !=None:
   t+=1
   sport.append(i)
   result = None
  else:
   result = re.search(r'карат', i)
   if result !=None:
    t+=1
    sport.append(i)
    result = None
   else:
    result = re.search(r'ходьб', i)
    if result != None:
     t+=1
     sport.append(i)
     result = None
    else:
     result = re.search(r'марафон', i)
     if result !=None:
      t+=1
      sport.append(i)
      result = None
     else:
      result = re.search(r'атлет', i)
      if result !=None:
       t+=1
       sport.append(i)
       result = None
      else:
       result = re.search(r'триатл', i)
       if result !=None:
        t+=1
        sport.append(i)
        result = None
       else:
        result = re.search(r'фристайл', i)
        if result !=None:
         t+=1
         sport.append(i)
         result = None
        else:
         result = re.search(r'скийор', i)
         if result !=None:
          t+=1
          sport.append(i)
          result = None
         else:
          result = re.search(r'культуризм', i)
          if result !=None:
           t+=1
           sport.append(i)
           result = None
          else:
           result = re.search(r'армрестлинг', i)
           if result !=None:
            t+=1
            sport.append(i)
            result = None
           else:
            result = re.search(r'кетч', i)
            if result !=None:
             t+=1
             sport.append(i)
             result = None
            else:
             result = re.search(r'борье', i)
             if result !=None:
              t+=1
              sport.append(i)
              result = None
             else:
              result = re.search(r'кэндо', i)
              if result !=None:
               t+=1
               sport.append(i)
               result = None
              else:
               result = re.search(r'диаулос', i)
               if result !=None:
                t+=1
                sport.append(i)
                result = None
               else:
                result = re.search(r'скелетон', i)
                if result !=None:
                 t+=1
                 sport.append(i)
                 result = None
                else:
                 result = re.search(r'дром', i)
                 if result !=None:
                  t+=1
                  sport.append(i)
                  result = None
				  
for i in corpus:
 result = re.search(r'скач', i)
 if result !=None:
  t+=1
  sport.append(i)
  result = None
 else:
  result = re.search(r'слалом', i)
  if result !=None:
   t+=1
   sport.append(i)
   result = None
  else:
   result = re.search(r'регата', i)
   if result !=None:
    t+=1
    sport.append(i)
    result = None
   else:
    result = re.search(r'айкидо', i)
    if result != None:
     t+=1
     sport.append(i)
     result = None
    else:
     result = re.search(r'бег', i)
     if result !=None:
      t+=1
      sport.append(i)
      result = None
     else:
      result = re.search(r'бобслей', i)
      if result !=None:
       t+=1
       sport.append(i)
       result = None
      else:
       result = re.search(r'бейсбол', i)
       if result !=None:
        t+=1
        sport.append(i)
        result = None
       else:
        result = re.search(r'поло ', i)
        if result !=None:
         t+=1
         sport.append(i)
         result = None
        else:
         result = re.search(r'дельтаплан', i)
         if result !=None:
          t+=1
          sport.append(i)
          result = None
         else:
          result = re.search(r'дзюдо', i)
          if result !=None:
           t+=1
           sport.append(i)
           result = None
          else:
           result = re.search(r'мотобол', i)
           if result !=None:
            t+=1
            sport.append(i)
            result = None
           else:
            result = re.search(r'мотобол', i)
            if result !=None:
             t+=1
             sport.append(i)
             result = None
            else:
             result = re.search(r'пушбол', i)
             if result !=None:
              t+=1
              sport.append(i)
              result = None
             else:
              result = re.search(r'биатл', i)
              if result !=None:
               t+=1
               sport.append(i)
               result = None
              else:
               result = re.search(r'конкур', i)
               if result !=None:
                t+=1
                sport.append(i)
                result = None
               else:
                result = re.search(r'бенди', i)
                if result !=None:
                 t+=1
                 sport.append(i)
                 result = None
                else:
                 result = re.search(r'дартс', i)
                 if result !=None:
                  t+=1
                  sport.append(i)
                  result = None

for i in corpus:
 result = re.search(r'фехтов', i)
 if result !=None:
  t+=1
  sport.append(i)
  result = None
 else:
  result = re.search(r'аэроб', i)
  if result !=None:
   t+=1
   sport.append(i)
   result = None
  else:
   result = re.search(r'акробат', i)
   if result !=None:
    t+=1
    sport.append(i)
    result = None
   else:
    result = re.search(r'гимнаст', i)
    if result != None:
     t+=1
     sport.append(i)
     result = None
    else:
     result = re.search(r'хокк', i)
     if result !=None:
      t+=1
      sport.append(i)
      result = None
     else:
      result = re.search(r'кросс', i)
      if result !=None:
       t+=1
       sport.append(i)
       result = None
      else:
       result = re.search(r'выездк', i)
       if result !=None:
        t+=1
        sport.append(i)
        result = None
       else:
        result = re.search(r'гандбол', i)
        if result !=None:
         t+=1
         sport.append(i)
         result = None
        else:
         result = re.search(r'сервинг', i)
         if result !=None:
          t+=1
          sport.append(i)
          result = None
         else:
          result = re.search(r'гребл', i)
          if result !=None:
           t+=1
           sport.append(i)
           result = None
          else:
           result = re.search(r'картинг', i)
           if result !=None:
            t+=1
            sport.append(i)
            result = None
           else:
            result = re.search(r'ориентиров', i)
            if result !=None:
             t+=1
             sport.append(i)
             result = None
            else:
             result = re.search(r'гольф', i)
             if result !=None:
              t+=1
              sport.append(i)
              result = None
             else:
              result = re.search(r'крокет', i)
              if result !=None:
               t+=1
               sport.append(i)
               result = None
              else:
               result = re.search(r'крикет', i)
               if result !=None:
                t+=1
                sport.append(i)
                result = None
               else:
                result = re.search(r'серф', i)
                if result !=None:
                 t+=1
                 sport.append(i)
                 result = None
                else:
                 result = re.search(r'регби', i)
                 if result !=None:
                  t+=1
                  sport.append(i)
                  result = None
				  
for i in corpus:
 result = re.search(r'альпин', i)
 if result !=None:
  t+=1
  sport.append(i)
  result = None
 else:
  result = re.search(r'бадмин', i)
  if result !=None:
   t+=1
   sport.append(i)
   result = None
  else:
   result = re.search(r'теннис', i)
   if result !=None:
    t+=1
    sport.append(i)
    result = None
   else:
    result = re.search(r'футбол', i)
    if result != None:
     t+=1
     sport.append(i)
     result = None
    else:
     result = re.search(r'волейбол', i)
     if result !=None:
      t+=1
      sport.append(i)
      result = None
     else:
      result = re.search(r'баскетб', i)
      if result !=None:
       t+=1
       sport.append(i)
       result = None
      else:
       result = re.search(r'бокс', i)
       if result !=None:
        t+=1
        sport.append(i)
        result = None
       else:
        result = re.search(r'борьб', i)
        if result !=None:
         t+=1
         sport.append(i)
         result = None
        else:
         result = re.search(r'стрельб', i)
         if result !=None:
          t+=1
          sport.append(i)
          result = None
         else:
          result = re.search(r'плав', i)
          if result !=None:
           t+=1
           sport.append(i)
           result = None
		   
print(t)
		   
l=0
for i in gos:
 file = open('sphere_spending_test/government/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in cul:
 file = open('sphere_spending_test/culture/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in eco:
 file = open('sphere_spending_test/ecology/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in econ:
 file = open('sphere_spending_test/economics/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in edu:
 file = open('sphere_spending_test/education/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in sec:
 file = open('sphere_spending_test/security/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in defence:
 file = open('sphere_spending_test/defence/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in soc:
 file = open('sphere_spending_test/social/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in sport:
 file = open('sphere_spending_test/sports/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in med:
 file = open('sphere_spending_test/medicine/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in zhkh:
 file = open('sphere_spending_test/establishment/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
