# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:57:20 2022

@author: Lab435-Hoca
"""

class Taşit:
    def __init__(self,isim,renk):
        self.__isim=isim
        self.__renk=renk
        
    def getRenk(self):
        return self.__renk
    
    def setRenk(self,renk):
        self.__renk=renk
        
    def getIsim(self):
        return self.__isim
    
class Araba(Taşit): #extends yerine(parent) yazılır
    def __init__(self,isim,renk,model):#childın kendine has özelliği model olsun.
        super().__init__(isim,renk)#taşittaki initten isim ve renk özelliklerini atamış olduk. set ederken kullanılmış oluyor.
        self.__model=model
        
    def getTanım(self):
        return "Araç " + self.getIsim() + ' '+ self.__model + " Renk "+ self.getRenk()
    
    
c=Araba("Toyota","Kırmızı","Coralla")
print(c.getTanım())

#çoklu miras

class SuperClass1:
    def method_super1(self):
        print("metotsuper1 çağrıldı")
        

class SuperClass2:
    def method_super2(self):
        print("metotsuper2 çağrıldı")
        
class ChildClass(SuperClass1, SuperClass2):#her iki classı da içeriyor (çoklu miras)
    def child_method(self):
        print("child metot")

c=ChildClass()

c.method_super1()
c.method_super2()


#overriding ve poliformanizm örneği

class A:
    def __init__(self):
        self.__x=1
        
    def m1(self):
        print("A sınıfına ait m1 fonksiyonu")
        
class B(A):
    def __init__(self):
        self.__y=1
        
    def m1(self):
        print("B sınıfına ait m1 fonksiyonu")
#poliformanizm olayı aşağıdaki satırlara ait bu kodun tamamına overriding deniyo overriding ezme demek.
c=B()#B sınıfına ait nesne
c.m1()

c2=A()#A sınıfına ait nesne
c2.m1()


#ISINSTANCE

print(isinstance(1,int)) #inte 1 örnek mi
print(isinstance(1.2,int))
print(isinstance([1,1,2,3,4],list)) #listeye önceki argüman örnek mi
print(isinstance(A,B))#b a ya örnek mi
print(isinstance(B,A))# a bye örnek mi / a byi kapsar mı




















































