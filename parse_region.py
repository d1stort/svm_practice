#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import re
mfile = open('new_sent_vybfin (1).txt','r', encoding='utf-8')
corpus = []
for t in mfile:
 corpus.append(t)
mfile.close()

rf=[]
kavkz=[]
stavr=[]
ing = []
dag=[]
kabbal=[]
oset=[]
karcher=[]
chech=[]
uzh=[]
krasnod=[]
asrth=[]
volgogr=[]
rostov=[]
adyg=[]
kalm=[]
privolg=[]
nizh=[]
kir=[]
samar=[]
orenb=[]
penz=[]
perm=[]
sarat=[]
ylyan=[]
bashkortstn=[]
maryel=[]
mord=[]
tatarst=[]
ydmyrt=[]
chuv=[]
sevzap=[]
arh=[]
nenets=[]
volog=[]
kaliningr=[]
saintp=[]
leningr=[]
murm=[]
novg=[]
pskv=[]
karel=[]
komi=[]
sib=[]
alt=[]
krasnoyarsk=[]
kemer=[]
irk=[]
novosib=[]
omsk=[]
tomsk=[]
zabaykl=[]
burya=[]
altaysk=[]
tyva=[]
hakas=[]
yral=[]
kurg=[]
sverdl=[]
tumen=[]
hantymans=[]
yamalonen=[]
chelyab=[]
tsentr=[]
belgorod=[]
bryansk=[]
vlad=[]
voronezh=[]
ivan=[]
tversk=[]
kaluzh=[]
kostrom=[]
kursk=[]
lipets=[]
moscow=[]
moscovs=[]
orlovs=[]
ryazans=[]
smol=[]
tamb=[]
tylsk=[]
yarosl=[]
dalnevost=[]
primorsk=[]
habar=[]
amyrska=[]
kamch=[]
magad=[]
sahalin=[]
chukot=[]
saha=[]
evr=[]
krymsk=[]
krym=[]
sevast=[]
baykonyr=[]
kemerovsk=[]
sevkav=[]
astrah=[]

t=0

for i in corpus:
 result = re.search(r'адыг', i)
 if result !=None:
  t+=1
  adyg.append(i)
  result = None
 else:
  result = re.search(r'алтай ', i)
  if result !=None:
   t+=1
   alt.append(i)
   result = None
  else:
   result = re.search(r'алтайск', i)
   if result !=None:
    t+=1
    altaysk.append(i)
    result = None
   else:
    result = re.search(r'амурс', i)
    if result != None:
     t+=1
     amyrska.append(i)
     result = None
    else:
     result = re.search(r'арханг', i)
     if result !=None:
      t+=1
      arh.append(i)
      result = None
     else:
      result = re.search(r'астрах', i)
      if result !=None:
       t+=1
       astrah.append(i)
       result = None
      else:
       result = re.search(r'байконур', i)
       if result !=None:
        t+=1
        baykonyr.append(i)
        result = None
       else:
        result = re.search(r'башкор', i)
        if result !=None:
         t+=1
         bashkortstn.append(i)
         result = None
        else:
         result = re.search(r'белгород', i)
         if result !=None:
          t+=1
          belgorod.append(i)
          result = None
         else:
          result = re.search(r'брянск', i)
          if result !=None:
           t+=1
           bryansk.append(i)
           result = None
          else:
           result = re.search(r'бурят', i)
           if result !=None:
            t+=1
            burya.append(i)
            result = None
           else:
            result = re.search(r'владим', i)
            if result !=None:
             t+=1
             vlad.append(i)
             result = None
            else:
             result = re.search(r'волгогр', i)
             if result !=None:
              t+=1
              volgogr.append(i)
              result = None
             else:
              result = re.search(r'волог', i)
              if result !=None:
               t+=1
               volog.append(i)
               result = None
              else:
               result = re.search(r'воронеж', i)
               if result !=None:
                t+=1
                voronezh.append(i)
                result = None
               else:
                result = re.search(r'дагест', i)
                if result !=None:
                 t+=1
                 dag.append(i)
                 result = None
                else:
                 result = re.search(r'дальневост', i)
                 if result !=None:
                  t+=1
                  dalnevost.append(i)
                  result = None

for i in corpus:
 result = re.search(r'евр', i)
 if result !=None:
  t+=1
  ing.append(i)
  result = None
 else:
  result = re.search(r'забайк', i)
  if result != None:
   t+=1
   irk.append(i)
   result = None
  else:
   result = re.search(r'иван', i)
   if result != None:
    t+=1
    kabbal.append(i)
    result = None
   else:
    result = re.search(r'ингуш', i)
    if result != None:
     t+=1
     kaliningr.append(i)
     result = None
    else:
     result = re.search(r'иркут', i)
     if result != None:
      t+=1
      kalm.append(i)
      result = None
     else:
      result = re.search(r'кабард', i)
      if result != None:
       t+=1
       kaluzh.append(i)
       result = None
      else:
       result = re.search(r'калинингр', i)
       if result != None:
        t+=1
        kamch.append(i)
        result = None
       else:
        result = re.search(r'калмык', i)
        if result != None:
         t+=1
         karcher.append(i)
         result = None
        else:
         result = re.search(r'калужск', i)
         if result != None:
          t+=1
          karel.append(i)
          result = None
         else:
          result = re.search(r'камч', i)
          if result != None:
           t+=1
           kemer.append(i)
           result = None
          else:
           result = re.search(r'карач', i)
           if result != None:
            t+=1
            kir.append(i)
            result = None
           else:
            result = re.search(r'карел', i)
            if result != None:
             t+=1
             komi.append(i)
             result = None
            else:
             result = re.search(r'кемер', i)
             if result != None:
              t+=1
              kostrom.append(i)
              result = None
             else:
              result = re.search(r'кировск', i)
              if result != None:
               t+=1
               krasnod.append(i)
               result = None
              else:
               result = re.search(r'коми', i)
               if result != None:
                t+=1
                krasnoyarsk.append(i)
                result = None
               else:
                result = re.search(r'костр', i)
                if result != None:
                 t+=1
                 krym.append(i)
                 result = None
                else:
                 result = re.search(r'краснод', i)
                 if result != None:
                  t+=1
                  kurg.append(i)
                  result = None
                 else:
                  result = re.search(r'курск', i)
                  if result != None:
                   t+=1
                   kursk.append(i)
                   result = None

for i in corpus:				   
 result = re.search(r'ленингр', i)
 if result != None:
  t+=1
  leningr.append(i)
  result = None
 else:
  result = re.search(r'липецк', i)
  if result != None:
   t+=1
   lipets.append(i)
   result = None
  else:
   result = re.search(r'магадан', i)
   if result != None:
    t+=1
    magad.append(i)
    result = None
   else:
    result = re.search(r'марий', i)
    if result != None:
     t+=1
     maryel.append(i)
     result = None
    else:
     result = re.search(r'морд', i)
     if result != None:
      t+=1
      mord.append(i)
      result = None
     else:
      result = re.search(r'моск', i)
      if result != None:
       t+=1
       moscow.append(i)
       result = None
      else:
       result = re.search(r'московск', i)
       if result != None:
        t+=1
        moscovs.append(i)
        result = None
       else:
        result = re.search(r'мурм', i)
        if result != None:
         t+=1
         murm.append(i)
         result = None
        else:
         result = re.search(r'ненецк', i)
         if result != None:
          t+=1
          nenets.append(i)
          result = None
         else:
          result = re.search(r'нижегор', i)
          if result != None:
           t+=1
           nizh.append(i)
           result = None
          else:
           result = re.search(r'новгор', i)
           if result != None:
            t+=1
            novg.append(i)
            result = None
           else:
            result = re.search(r'новосиб', i)
            if result != None:
             t+=1
             novosib.append(i)
             result = None
            else:
             result = re.search(r'омск', i)
             if result != None:
              t+=1
              omsk.append(i)
              result = None
             else:
              result = re.search(r'оренб', i)
              if result != None:
               t+=1
               orenb.append(i)
               result = None
              else:
               result = re.search(r'орл', i)
               if result != None:
                t+=1
                orlovs.append(i)
                result = None
               else:
                result = re.search(r'осет', i)
                if result != None:
                 t+=1
                 oset.append(i)
                 result = None

for i in corpus:				 
 result = re.search(r'пенз', i)
 if result != None:
  t+=1
  penz.append(i)
  result = None
 else:
  result = re.search(r'перм', i)
  if result != None:
   t+=1
   perm.append(i)
   result = None
  else:
   result = re.search(r'приволжс', i)
   if result != None:
    t+=1
    privolg.append(i)
    result = None
   else:
    result = re.search(r'приморск', i)
    if result != None:
     t+=1
     primorsk.append(i)
     result = None
    else:
     result = re.search(r'псков', i)
     if result != None:
      t+=1
      pskv.append(i)
      result = None
     else:
      result = re.search(r'росс', i)
      if result != None:
       t+=1
       rf.append(i)
       result = None
      else:
       result = re.search(r'рф', i)
       if result != None:
        t+=1
        rf.append(i)
        result = None
       else:
        result = re.search(r'рост', i)
        if result != None:
         t+=1
         rostov.append(i)
         result = None
        else:
         result = re.search(r'ряз', i)
         if result != None:
          t+=1
          ryazans.append(i)
          result = None
         else:
          result = re.search(r'самар', i)
          if result != None:
           t+=1
           samar.append(i)
           result = None
          else:
           result = re.search(r'санкт', i)
           if result != None:
            t+=1
            saintp.append(i)
            result = None
           else:
            result = re.search(r'петер', i)
            if result != None:
             t+=1
             saintp.append(i)
             result = None
            else:
             result = re.search(r'сарат', i)
             if result != None:
              t+=1
              sarat.append(i)
              result = None
             else:
              result = re.search(r'саха ', i)
              if result != None:
               t+=1
               saha.append(i)
               result = None
              else:
               result = re.search(r'якут', i)
               if result != None:
                t+=1
                saha.append(i)
                result = None
               else:
                result = re.search(r'сахал', i)
                if result != None:
                 t+=1
                 sahalin.append(i)
                 result = None
                else:
                 result = re.search(r'свердл', i)
                 if result != None:
                  t+=1
                  sverdl.append(i)
                  result = None
                 else:
                  result = re.search(r'севаст', i)
                  if result != None:
                   t+=1
                   sevast.append(i)
                   result = None
                  else:
                   result = re.search(r'северо-зап', i)
                   if result != None:
                    t+=1
                    sevzap.append(i)
                    result = None
                   else:
                    result = re.search(r'северо-кавк', i)
                    if result != None:
                     t+=1
                     sevkav.append(i)
                     result = None
                    else:
                     result = re.search(r'сибир', i)
                     if result != None:
                      t+=1
                      sib.append(i)
                      result = None
                     else:
                      result = re.search(r'смоленс', i)
                      if result != None:
                       t+=1
                       smol.append(i)
                       result = None
                      else:
                       result = re.search(r'ставропол', i)
                       if result != None:
                        t+=1
                        stavr.append(i)
                        result = None

for i in corpus:		  
 result = re.search(r'тамб', i)
 if result != None:
  t+=1
  tamb.append(i)
  result = None
 else:
  result = re.search(r'татарст', i)
  if result != None:
   t+=1
   tatarst.append(i)
   result = None
  else:
   result = re.search(r'тверск', i)
   if result != None:
    t+=1
    tversk.append(i)
    result = None
   else:
    result = re.search(r'томск', i)
    if result != None:
     t+=1
     tomsk.append(i)
     result = None
    else:
     result = re.search(r'тульск', i)
     if result != None:
      t+=1
      tylsk.append(i)
      result = None
     else:
      result = re.search(r'тыв', i)
      if result != None:
       t+=1
       tyva.append(i)
       result = None
      else:
       result = re.search(r'тюменск', i)
       if result != None:
        t+=1
        tumen.append(i)
        result = None
       else:
        result = re.search(r'удмурт', i)
        if result != None:
         t+=1
         ydmyrt.append(i)
         result = None
        else:
         result = re.search(r'ульян', i)
         if result != None:
          t+=1
          ylyan.append(i)
          result = None
         else:
          result = re.search(r'уральс', i)
          if result != None:
           t+=1
           yral.append(i)
           result = None
          else:
           result = re.search(r'хабар', i)
           if result != None:
            t+=1
            habar.append(i)
            result = None
           else:
            result = re.search(r'хакас', i)
            if result != None:
             t+=1
             hakas.append(i)
             result = None
            else:
             result = re.search(r'ханты', i)
             if result != None:
              t+=1
              hantymans.append(i)
              result = None
             else:
              result = re.search(r'централь', i)
              if result != None:
               t+=1
               tsentr.append(i)
               result = None
              else:
               result = re.search(r'челяб', i)
               if result != None:
                t+=1
                chelyab.append(i)
                result = None
               else:
                result = re.search(r'чечен', i)
                if result != None:
                 t+=1
                 chech.append(i)
                 result = None
                else:
                 result = re.search(r'чуваш', i)
                 if result != None:
                  t+=1
                  chuv.append(i)
                  result = None
                 else:
                  result = re.search(r'чукот', i)
                  if result != None:
                   t+=1
                   chukot.append(i)
                   result = None
                  else:
                   result = re.search(r'южн', i)
                   if result != None:
                    t+=1
                    uzh.append(i)
                    result = None
                   else:
                    result = re.search(r'ямал', i)
                    if result != None:
                     t+=1
                     yamalonen.append(i)
                     result = None
                    else:
                     result = re.search(r'яросл', i)
                     if result != None:
                      t+=1
                      yarosl.append(i)
                      result = None
                      
l=0
for i in rf:
 file = open('regions/rf/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in adyg:
 file = open('regions/adygeya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in alt:
 file = open('regions/altai/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in altaysk:
 file = open('regions/altaiski/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in amyrska:
 file = open('regions/amyrskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in astrah:
 file = open('regions/astrahanskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in baykonyr:
 file = open('regions/baikonyr/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in bashkortstn:
 file = open('regions/bashkortostan/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in belgorod:
 file = open('regions/belgorodskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in bryansk:
 file = open('regions/bryanskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in burya:
 file = open('regions/byryatiya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in chech:
 file = open('regions/chechenskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in chelyab:
 file = open('regions/chelyabinskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in chukot:
 file = open('regions/chukotskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in chuv:
 file = open('regions/chuvashskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in dag:
 file = open('regions/dagestan/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in dalnevost:
 file = open('regions/dalnevostochnyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in evr:
 file = open('regions/evreiskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in habar:
 file = open('regions/habarovskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in hakas:
 file = open('regions/hakasiya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in hantymans:
 file = open('regions/hanty-mansyiskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in ing:
 file = open('regions/ingushetiya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in irk:
 file = open('regions/irkytskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in ivan:
 file = open('regions/ivanovskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in kabbal:
 file = open('regions/kabardino-balkarskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in kaliningr:
 file = open('regions/kaliningradskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in kalm:
 file = open('regions/kalmikiya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in kaluzh:
 file = open('regions/kalyzhskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close() 
 
l=0
for i in kamch:
 file = open('regions/kamchatskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in karcher:
 file = open('regions/karachaevo-cherkessiya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in karel:
 file = open('regions/kareliya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in kemer:
 file = open('regions/kemerovskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in kir:
 file = open('regions/kirovskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in komi:
 file = open('regions/komi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in kostrom:
 file = open('regions/kostromskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in krasnod:
 file = open('regions/krasnodarskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in krasnoyarsk:
 file = open('regions/krasnoyarskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in krym:
 file = open('regions/krym/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in krymsk:
 file = open('regions/krymskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in kurg:
 file = open('regions/kyrganskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in kursk:
 file = open('regions/kyrskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in leningr:
 file = open('regions/leningradskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in lipets:
 file = open('regions/lipetskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in magad:
 file = open('regions/magadanskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in maryel:
 file = open('regions/maryi-el/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in mord:
 file = open('regions/mordoviya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in moscovs:
 file = open('regions/moskovskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in moscow:
 file = open('regions/moskva/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in murm:
 file = open('regions/myrmanskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in nenets:
 file = open('regions/nenetskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in nizh:
 file = open('regions/nizhegorodskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in novg:
 file = open('regions/novgorodskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in novosib:
 file = open('regions/novosibirskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in omsk:
 file = open('regions/omskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in orenb:
 file = open('regions/orenburgskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in orlovs:
 file = open('regions/orlovskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in oset:
 file = open('regions/osetiya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in penz:
 file = open('regions/penzenskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in perm:
 file = open('regions/permskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in primorsk:
 file = open('regions/primorskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in privolg:
 file = open('regions/privolzhskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in pskv:
 file = open('regions/pskovskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in rostov:
 file = open('regions/rostovskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in ryazans:
 file = open('regions/ryazanskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in saha:
 file = open('regions/saha/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in sahalin:
 file = open('regions/sahalinskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in samar:
 file = open('regions/samarskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in saintp:
 file = open('regions/sankt-peterburg/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in sarat:
 file = open('regions/saratovskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()

l=0
for i in sevast:
 file = open('regions/sevastopol/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in sevkav:
 file = open('regions/severo-kavkazskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in sevzap:
 file = open('regions/severo-zapadnyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in sib:
 file = open('regions/sibirskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in smol:
 file = open('regions/smolenskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in stavr:
 file = open('regions/stavropolskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in sverdl:
 file = open('regions/sverdlovskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in tamb:
 file = open('regions/tambovskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in tatarst:
 file = open('regions/tatarstan/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in tomsk:
 file = open('regions/tomskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in tsentr:
 file = open('regions/tsentralnyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in tumen:
 file = open('regions/tumenskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in tversk:
 file = open('regions/tverskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in tylsk:
 file = open('regions/tylskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in tyva:
 file = open('regions/tyva/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in uzh:
 file = open('regions/uzhnyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in vlad:
 file = open('regions/vladimirskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in volgogr:
 file = open('regions/volgogradskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in volog:
 file = open('regions/vologodskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in voronezh:
 file = open('regions/voronezhskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in yamalonen:
 file = open('regions/yamalo-nenetskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in yarosl:
 file = open('regions/yaroslavskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in ydmyrt:
 file = open('regions/ydmyrtiya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in ylyan:
 file = open('regions/ylyanovskaya/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in yral:
 file = open('regions/yralskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close()
 
l=0
for i in zabaykl:
 file = open('regions/zabaikalskyi/0'+str(l)+'.txt', 'w', encoding='utf-8')
 file.write(i)
 l+=1
 file.close() 
