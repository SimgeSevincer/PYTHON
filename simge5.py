# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:38:05 2022

@author: Lab435-Hoca
"""



#iterasyonlar


liste12=[10,23,54,7,0,-21]

for i in liste12:
    print(i)



print("----------------------")



for i in range(1,10):#1 den 10 a kadar yazdırır.
    print(i)



print("----------------------")



for i in range(10):#0 dan 10 a kadar yazar. 9 dahile değil
    print(i)



print("----------------------")



for i in range(1,19,2):#1den başlar 19 akadar 2şer 2şer atlayarak yazar.
    print(i)



print("----------------------")




for i in range(len(liste12)):#range içindeki 6 dır yani 0 dan 6 ya kadar indis elemanlarını verir.
    print(liste12[i])