# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:32:14 2022

@author: Lab435-Hoca
"""

liste6=[11,33,44,66,788,1]

print(liste6[0:5])#0 dan 6 ya kadar
print(liste6[:3])#0 dan 4 e kadar
print(liste6[2:])#2 den sonuna kadar
print(liste6[-1])#en sondaki eleman
print(liste6[-2])#sondan 2. eleman
print(liste6[-2:])#-2 ve -1 yazılır

#listelerde + ve * operatör kullanımları

liste7=[11,33]
liste8=[1,9]
liste9=liste7+liste8#listeleri birleştirme
print(liste9)

liste10=3*liste9
print(liste10)



print("-------------------")



#liste için fonksiyonlar

#append

liste11=[2,3,4,1,32]
liste11.append(19)#değişkene atanılmaz atanılırsa ğer null none döner çünkü bu bir operasyon yapar..
print(liste11)

#count

ab=liste11.count(4)
print(ab)

#extend

liste12=[99,54]
liste11.extend(liste12)#liste12 nin elelmanlarını liste11 ekler.. değişkene atanılamaz atanırsa null none döner.. çünkü operasyon yapar
print(liste11)

#index

print(liste11.index(4))#listede 4 ün olduğu indexi söyler..

#insert

liste11.insert(1,25)#1. indexe 25 i ekle araya sıkıştırma yöntemi..
print(liste11)

liste11.pop(2)#2. indexteki elemanı siler
print(liste11) 
eleman=liste11.pop()#son elemanı siler
print(liste11)

#remove

liste11.remove(32)#32 değerini çıkarır
print(liste11)

#reverse ters çevirmek

liste11.reverse()
print(liste11)

#sort

liste11.sort()#küçükten büyüğe doğru sıralar...
print(liste11)
sorted(liste11)#böyle yapıldığında liste11 değişmez sadece bu satır için büyükten küçüğe sıralar yani liste11 in durumu değişmez...
print(sorted(liste11))#böyle yapıldığında liste11 değişmez sadece bu satır için büyükten küçüğe sıralar yani liste11 in durumu değişmez..


