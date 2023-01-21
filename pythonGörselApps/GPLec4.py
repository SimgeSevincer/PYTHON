# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 11:43:15 2022

@author: umitozturk
"""
# MODUL KULLANIMI
# SINIFLAR 

# MODUL

# Bir modül fonksiyonlar, sınıflar ve değişkenleri tutabilen
# .py uzantılı normal bir Python dosyasıdır.  
# İlgili konuma modul1 oluşturulmuştur. 
# Bu modül aşağıdaki gibi çağırılabilir.
# Değişken ve fonksiyonlara erişilebilir ve amaca uygun kullanılabilir: 
# Aşağıdaki kod bloğunu açarak deneyiniz.


"""
import modul1

print (modul1.ceza)
print ("-----------------------------------")

yeni_borc = modul1.borcVer(8)
print (yeni_borc)

"""

# from ile de erişim sağlanabilir:
    
# Bu durumda yalnızca ihtiyaç duyulan fonksiyon(lar) ve değişken(ler)in
# çekilmesi istenebilir Bu durumda 'from...import...' yapısı kullanılır 
# Aşağıda sıralı iki farklı kod bloğunu deneyiniz.


 
"""
from modul1 import ceza 

print (ceza)

"""


"""
from modul1 import borcVer

borc = borcVer(4)

"""

# dir fonksiyonu ile modülün sahip olduğu tüm özellikler 
# (sahip olunan tüm sınıf, fonksiyon ve değişkenler) görülür.
# Bizleri ilgilendiren kısım: borcVer fonksiyonu ve ceza değişkenidir. Diğerleri yazılımdan gelen 
# standard ihtiyaçlara ait bilgilerdir. (memory, dosya adı, spesifikasyonlar, paket bilgisi vs.).
# Aşağıdaki kod bloğunu açarak inceleyiniz:

"""    
import modul1 
    
print (dir (modul1))

"""


# SINIFLAR

# Sınıfın Tanımlanması:

class Kisi:
    
       # konstraktör yada başlatıcı (constructor or initializer)
      def __init__(self, isim):  
            self.isim = isim
                  
    
      # string dönen bir metot:
      def isimVer(self):
         return "Adınız soyadınız " + self.isim

# _init_ fonksiyonu yapılandırıcıdır. Sınıfa ait değişkenlerin başlangıç atamalarını
# yapmak üzere kullanılırlar. Sınıfa ait nesne oluşturulduğunda en başta çalışıp 
# atamaları yaparlar.
# self ise Java'daki 'this' anahtar kelimesi ile birebir aynı olmasa da benzer bir görevdedir.
# Soluna ilişiklendiği değişkenin tanımlandığı sınıfa ait olduğunu belirtirler.
# Bir sınıftan nesne oluşturulduğunda o nesne self ile belirtilen özellikleri kullanabilir:
    
k1 = Kisi("Hakan Sözen")
#Yukarıdaki satırda name için başlangıç değeri verilmiştir.


print (k1.isim) # k1 nesnesine ait name yazdırılıyor

print (k1.isimVer()) 

# nesneye ait değişken değerleri güncellenebilir:

k1.isim = "Serkan Sözen"    
print (k1.isimVer()) 
     

print ("----------------------------------------------------")

# Örnek: Basit bir uygulama 

class BankaHesabı:

     # constructor or initializer
    def __init__(self, isim, para):
         self.__isim = isim
         self.__bakiye = para   # __bakiye yanına çift alt çizgi ile private yapılıyor. Sınıf dışından erişilemez.
         

    def paraYatır(self, para):
         self.__bakiye += para

    def paraÇek(self, para):
         if self.__bakiye > para :
             self.__bakiye -= para
             return para
         else:
             return "Yetersiz bakiye"

    def bakiyeKontrol(self):
         return self.__bakiye

# Aşağıdaki kod çıktılarını inceleyiniz:

b1 = BankaHesabı('Hakan Sözen', 400)

print(b1.paraÇek(500))

b1.paraYatır(500)

print(b1.bakiyeKontrol())

print(b1.paraÇek(800))

print(b1.bakiyeKontrol())

# Dikkat bakiye ve isim private olduğu için direk erişilmez. 
# Aşağıdaki 2 kod satırı hata verecektir:
#print (b1.__isim) 
#print (b1.__bakiye) 


# Nesnelere ait özellikleri de dir fonksiyonu kullanarak gözlemleyebilirsiniz:

print(dir (b1)) 

# Metot aşırı yüklenmesi (overloading)

# overloading aynı isimdeki birden fazla fonksiyonun farklı parametreler üzerinden 
# çağrılması ile uygulanır. Ancak Python'da fonksiyonlarda parametre tipleri 
# belli olmadığı için farklı uygulanır:
    

import math     

class Daire:

    def __init__(self, cap):
        self.__cap = cap

    def setCap(self, cap):
        self.__cap = cap

    def getCap(self):
        return self.__cap

    def alanBul(self):
        return math.pi * (self.__cap/2) ** 2

    def __add__(self, digerDaire):  #overload yapılıyor
        return Daire( self.__cap + digerDaire.__cap )


# Yukarıdaki Daire sınıfında toplama işlemi __add__ fonksiyonu üzerinden
# aşırı yüklenmiştir. Bu durumda Daire sınıfına ait nesneler üzerinden kullanımı
# halinde + operatörü farklı davranacaktır. Yapılan işleme göre c1 + c2 uygulandığında
# eğer c1 ve c2 birer daire nesnesi ise bu nesnelerin çapları toplanır ve
# çapı c1 + c2 olan yeni bir daire nesnesi olarak sonuç oluşur:
    
c1 = Daire(4)
print(c1.getCap())

c2 = Daire(5)
print(c2.getCap())

c3 = c1 + c2 
print(c3.getCap())

print ("----------------------------------------------------")



# KALITIM (inheritance) ve ÇOK BİÇİMLİLİK (polymorphism)


# kalıtım programcıya genelden özele daha özelleşmiş sınıflar üretebilmesine olanak verir.
# kalıtımda parent-child ilişkisi vardır. Child, parentten türer. Parentin tüm özelliklerini
# kullanabilir. Kalıtım ifadesi buradan gelmektedir. Child bir parenttir. Fakat Parent bir child 
# değildir. Child parentte varolan tüm özellikleri kullanabildiği gibi
# fazladan eklemek istediği özellikleri kendinde tanımlar.

# Polymorphism (çok biçimlilik) NYP'de programlama dilinin farklı tip verileri ve sınıfları
# farklı şekilde işleme yeteneğini belirten özelliğidir. 
# Daha belirgin olmak gerekirse, metotları ve türetilmiş sınıfları yeniden tanımlama yeteneğidir.
# Farklı sınıflara ait nesneler aynı metot ismiyle tanımlansa dahi fonksiyonel olarak
# ilgili olduğu sınıf dahilindeki işi yapacaktır. 
# Child ve parent sınıflarında aynı isimli iki fonksiyon varsa: 
# oluşturulan nesne hangi sınıfa ait olursa aynı isimlilerden o sınıftaki fonksiyon çalışır.
# Bu durum overriding (üstünü ezme) olarak geçer. Çok biçimlilik ile ilintilidir:

class Taşıt:

    def __init__(self, isim, renk):
        self.__isim = isim      # __isim is Taşıt sınıfı için private
        self.__renk = renk

    def getRenk(self):         
        return self.__renk

    def setRenk(self, renk):  
        self.__renk = renk

    def getIsim(self):         
        return self.__isim

class Araba(Taşıt): # Taşıttan Araba isimli yeni bir sınıf türetiliyor (Java'da extends)

    def __init__(self, isim, renk, model):
        # super() ile parent yapılandırıcısını çağır, isim ve rengi set et:  
        super().__init__(isim, renk)    
        self.__model = model

    def getTanım(self):
        return "Araç: "+ self.getIsim() +' '+ self.__model + ", Renk: " + self.getRenk()
    

# in method getDescrition we are able to call getName(), getColor() because they are 
# accessible to child class through inheritance 


c = Araba("Toyota", "kırmızı", "Corolla")
# c.setRenk("Beyaz") # rengi değiştirebilirsiniz.
print(c.getTanım())

print(c.getIsim()) # Araba sınıfında getIsım() adlı fonksiyon yoktur. 
#Ancak Taşıt sınıfının özellikleri kullanılabildiği için erişim mümkündür.

print ("----------------------------------------------------")

# Çoklu Miras: Python'da mümkündür.(Bilgi: Java desteklemez.)
    


class SuperClass1():

    def method_super1(self):
        print("method_super1 çağırıldı")

class SuperClass2():

    def method_super2(self):
        print("method_super2 çağırıldı")
        
# Child sınıfı hem SuperClass1 hem de SuperClass2'nin özelliklerini kullanabilir.
class ChildClass(SuperClass1, SuperClass2): 

    def child_method(self):
        print("child method")

c = ChildClass()

c.method_super1()

c.method_super2()

print ("----------------------------------------------------")

# Overriding (üstünü ezme) konusuna daha önce değinilmişti. Uygulaması aşağıdaki gibidir:
    
class A():

    def __init__(self):
        self.__x = 1

    def m1(self):
        print("A sınıfına ait m1 fonksiyonu")


class B(A):

    def __init__(self):
        self.__y = 1

    def m1(self):
        print("B sınıfına ait m1 fonksiyonu")

c = B()
# Hemen yukarıdaki kod satırını kapatıp aşağıdaki kod satırını açarak sonucu gözlemleyiniz.
# c = A()
c.m1()

print ("----------------------------------------------------")


#isinstance() function #

# isinstance boolean yapıdaır ve şu soruya yanıt verir:
# x nesnesi A sınıfının bir örneği midir ? isinstance(x, A)


print (isinstance(1, int))
print (isinstance(1.2, int))
print (isinstance([1,2,3,4], list))

print ("----------------------------------------------------")
# Tasarladığımız sınıflardan örnek verecek olursak:
    
print (isinstance (Araba, Taşıt))  # Araba sınıfı Taşıt sınıfının bir örneği midir? Yanıt: False

print (isinstance (Taşıt, Araba))   # Taşıt sınıfı Araba sınıfının bir örneği midir? Yanıt: False












