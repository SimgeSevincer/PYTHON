# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:56:08 2022

@author: Lab435-Hoca
"""

class Kisi:
    
    def __init__(self,isim):
        self.isim=isim
         
    def isimVer(self):
        return "adınız soyadınız "+self.isim
    
k1=Kisi("Hakan Sözer")

print(k1.isim)


print("--------")

k1.isim="Serkan Sözer"

print(k1.isimVer())


print("------------------")


class BankaHesabı:
    def __init__(self,isim,para):
        self.__isim=isim #private oldu ( __ ile)
        self.__bakiye=para
        
    def paraYatır(self,para):
        self.__bakiye+=para
        
    def paraCek(self,para):
        if self.__bakiye>=para:
            self.__bakiye-=para
            return para
        else:
            return "yetersiz bakiye"
        
    def bakiyeKontrol(self): #__bakiyeKontrol yazsaydık bu methodu private haline getirmiş oluruz ve dışardan ulaşamazlar.
        return self.__bakiye


b1=BankaHesabı("Simge Sevincer",400)
print(b1.paraCek(500))
b1.paraYatır(500)
print(b1.bakiyeKontrol())
print(b1.paraCek(800))
print(b1.bakiyeKontrol())




print("---------------")

print(b1.bakiyeKontrol())

print("-------------")


import math

class Daire:
    def __init__(self,cap):
        self.__cap=cap
        
    def setCap(self,cap):
        self.__cap=cap
        
    def getCap(self):
        return self.__cap
    
    def alanBul(self):
        return math.pi*(self.__cap/2)**2
    
    def __add__(self,digerDaire):
        return Daire(self.__cap + digerDaire.__cap)
    
c1=Daire(4)
print(c1.getCap())

c2=Daire(5)
print(c2.getCap())


c3=c1+c2#overloading yaptık...
print(c3.getCap())

print(c1.alanBul())

print("-----------------")


#kalıtımda parent child ilişkisi vardır. child parentin tüm özelliklerini kullanabilir. parent bir child değildir fakat child bir parenttır.
#poliformanizim bir sınıf başka sınıftan üretildiği zaman kullanılmış olur.
#overriding= child ve parentta aynı fonksiyon varsa oluşturduğumuz nesne hangi sınıfa aitse o sınıfta kullanılır.