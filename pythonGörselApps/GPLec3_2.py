# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:15:04 2022

@author: umitozturk
"""


# TÜPLER (Tuples) ve SÖZLÜKLER (Dictionary)


# Tüpler:
# Tüpler tıpkı listeler gibidir.
# Ancak bir defa tanımlandıktan sonra tekrar değiştirilemezler.


değerler = ("12.30", "20.00", 4)
print ("otobüsün kalkış saati %s, varış saati %s dir. Mola kalkıştan %d saat sonradır." %değerler)

# Tüp elemanlarını tıpkı listeler gibi çağırabiliriz:
    
print (değerler[0])
print ("-----------------------------------")


# Aşağıdaki kod parçası hata verecektir:
    
#değerler[0] ="13.00"

# Ancak bir satırda birden fazla tanımlama yapmaya olanak tanır:
    
(kalkış, varış, mola) = ("13.00", "19.30", 3)

# değişkenlere yeni değerler atanabilir:

mola = 5    


# eğer parantez kullanılmazsa da tüp olarak değerlendirilir:
    
kalkış, varış, mola = "12.00", "18.00", 4

print (mola)

print ("-----------------------------------")

# cümle parçalanmasında kullanışlıdırlar:

email = "umitozturk@beykent.edu.tr"    

(user_name, domain_name)=email.split('@')


print (user_name)
print (domain_name)
print ("-----------------------------------")
# işlevsel kullanımı:

def topla(sy1,sy2,sy3):
    return sy1+sy2+sy3


# 4 argüman verilirse hata olur. Örnek aşağıdadır:
    
t1 = topla (3,4,5)    #hatasız
print (t1)


 # t1 = topla (3,4,5,6)   # hatalı

# eğer tasarımda argüman sayısının dinamik olması gerekecekse: 
def sayıYazdır (*sayılar):
    print (sayılar)

sayıYazdır (3,4,5,6,7,8) # * işareti önüne gelen değişken tipini tuple yapar 

# o halde topla fonksiyonunu yeniden tasarlayalım:
    

    
def topla2 (*sayılar):
    toplam = 0
    for i in sayılar:
        toplam = toplam + i
    return toplam

# şimdi toplamayı dilediğiniz kadar argüman vererek gerçekleştirebilirsiniz:
    
t2= topla2 (4,5,6,3,4,5,6,7,8,2,3)

print (t2)

print ("---------------dictionary:--------------------")


# Sözlükler (Dictionary)

# Üzerinde key-value (anahtar-değer) şeklinde kayıt tutulabilen python veri yapısıdır.

d1 = { 22565: "ali öztürk", 
      3454634: "ayşe ertekin", 
      9876869: "mehmet yılmaz"
      
         }

d2 = {} # boş sözlük oluşturur değişkene atar.


# anahtar değeri kullanılarak eleman elde edilebilir:
    
print (d1[22565])

print ("-----------------------------------")

# Bir sözlüğe anahtar-değer ikilisi eklenebilir:
    
d1 [675] ="ahmet çetinsoy"

print (d1)

print ("-----------------------------------")


# Sözlük üzerinde gezinme:

for key in d1:
    print ("anahtar:", key, "değer:",d1[key])

print ("-----------------------------------")
# sözlükten eleman silme:
    
del d1[22565]

print (d1)

print ("-----------------------------------")

print (len(d1)) # sözlük uzunluğu

print ("-----------------------------------")

# boolean sorgulama örneği:
    
print (675 in d1)


print ("-----------------------------------")

d2 = {"mike":41, "bob":3}
d3 = {"bob":3, "mike":41}

# true dönebilmesi için anahtar-değer ikilisi aynı olmalı. Yerleri değişebilir.

print (d2==d3)


# Sözlük özelliklerine dair önemli fonksiyonlar:
    
    

print (d1.popitem()) # tuple tipinde rastgele bir item döner ve o itemi siler.
print ("-----------------abc---------------------")
print (d1)
d1.clear () # sözlük üzerindeki tüm anahtar-değer verileri silinir. 
print (d1)
d1 = { 22565: "ali öztürk", 
      3454634: "ayşe ertekin", 
      9876869: "mehmet yılmaz"
      
         }
print (d1.keys()) # tüm anahtar değerlerini döner.

print (type(d1.keys()))
print ("----------------------------------")


# for ile keys üzerinde gezinilebilir:

for k in d1.keys():
    print (k)
    
print ("----------------------------------")

print (d1.values()) # tüm values değerlerini döner.
print (type(d1.values()))


# for ile values üzerinde gezinilebilir:

for v in d1.values():
    print (v)

# for ile keys üzerinde gezinilebilir:

print ("-------------------------------------")

print (d1.get(3454634)) # o anahtara ait değeri döner
print (d1.get(34546355, "sözlükte bulunamadı"))

print ("-------------------------------------")


d1.pop(9876869)  # o anahtara ait key-value ikilisini siler.

print (d1)

print ("-------------------------------------")

# sözlük güncelleme:
    
    
d4 = {22565: "veli öztürk", 67676767: "hakan sözen", 121212: "özlem kaya"}
# yukarıdaki satır kullanılarak d1 güncellenmek istenirse şu alacaktır:
# eğer d4teki bir anahtar d1de varsa o anahtarın değeri güncellenir,
# yoksa yeni key-value ikilisi olarak d1 üzerine eklenir:

d1.update(d4)

print (d1)     
print ("-------------------------------------")


# enumerate fonksiyonu:
    
    
# liste yada tuple üzerinde kullanılabilirler:


for i in enumerate (["ali","ahmet","osman","kaya"]):
    print (i)

print ("-------------------------------------")

for i, k in enumerate (("ali", "ahmet", "can")):
    print (i,k)

