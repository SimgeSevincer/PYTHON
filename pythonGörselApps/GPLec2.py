# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 11:57:09 2022

@author: umitozturk
"""

# KARŞILAŞTIRMALAR, KOŞULLAR VE DÖNGÜLER

# Karşılaştırma işleçleri
# Karşılaştırma işleci birşeyin doğru yada yanlış olduğu sonucunu verir
# '==' iki nesnenin eşit olup olmadığını kontrol etmek için kullanılır:

print (3==3)  
print (3==4) 
# iki nesnenin eşit olup olmadığı sonucu 'boolean' tipinde döner.
# True veya false olabilir  
print (type(3==3))  


print ("-----------------------------------------------")



print ("-----------------------------------------------")


# karşılaştırma işleçleri string için kullanıldığında: 
# karşılaştırma her iki stringin ilk harflerinden başlanarak yapılır
# ve alfabetik öncelik dikkate alınır. Aşağıdaki satırların sonuçlarını 
# inceleyiniz:
    
print('a' > 'b')
print('ab' > 'aa')
print('aa' <= 'ab')
print('ab' <= 'aa')
print('ab' != 'aa')
print('aa' != 'aa')
print ("beykent" =="beykent")

print ("-----------------------------------------------")

# Karşılaştırma işleçleri için diğer örnekler:

print (4==5)
print (4==4)
print (4!=5)
print (4!=4)
print (4>=5)
print (4>=4)
print (4<=5)
print (4<=4)
print (4>5)
print (4>4)
print (4<5)
print (4<4)


print ("-----------------------------------------------")

# Mantıksal işleçler: 've' , 'veya'

# ve: işlenenlerin tamamının doğru olması durumunda 'doğru' sonucu verir.
# veya: işlenenlerin birinin doğru olması sonucun 'doğru' vermesini sağlar.
# 'veya'da doğru sonucu almamak için işlenenlerin tamamının yanlış olması gerekir.
# mantıksal işleçlerde işlenenlerin sayısal değer olması durumunda sıfırdan farklı
# her sayı True olarak; ancak 0 false olarak değerlendirilir.
# Strinlerde ise boş olmayan her değer True kabul edilir.
# Örnekler:
print (0 and 9) 
print (4 or 6)    
print (1 and False)
print (0 and True)
print (1>2 and "b")
print (9 and True)
print (1 and False)
print (7>9 or "abc")
print (7>9 and "abc")
print (9>7 or "abc")
print (9>7 and "abc")

# değil işleci:
# mantıksal ve karşılaştırma işleçlerinin sonunda elde edilen durumların 
# tersini alır.
print ("-----------------------------------------------")

print (not True)
print (not False) 
print (not 3>4)
print (not ('m' != 'm'))
print (not ('m' != 'u'))

print ("-----------------------------------------------")

# Kodun koşullu işletilmesi:

# if deyimi:

x=10    

# eğer x, 20'den büyük olsaydı if koşuluna girilmeyeceği için
# ekrana birşey yazılmayacaktı.    
if (x<20): print ("x'in değeri 20'den küçüktür")

print ("-----------------------------------------------")

# if else deyimi
# if koşullu işletmesinde, if koşulunun doğru olmadığı durumda
# else bloğu çalışır:

y = 15

if (y%2 == 0):
   print("sayı çifttir")
else:
   print("sayı tektir")

print ("-----------------------------------------------")

# zincirleme karşılaştırmalar:
# birden fazla koşulu zincirleme olarak tanımlayabilmek ve işletebilmek
# mümkündür:
    
today = "cuma"
# yukarıdaki satırı kapatıp aşağıdaki satırı açınız ve sonucu gözlemleyiniz.
#today = "cumartesi"   

if today == "pazartesi":
   print("bugün pazartesi")
elif today == "salı":
   print("bugün salı")
elif today == "çarşamba":
   print("bugün çarşamba")
elif today == "perşembe":
   print("bugün perşembe")
elif today == "cuma":
   print("bugün cuma")
else:
   print("cumartesi yada pazar")
   
print ("-----------------------------------------------")  
    
# önemli not: birden fazla koşul doğru olabilir.
# bu durumda sıralamada ilk olarak doğru olan şarta girilerek 
# yalnızca bu ilgili şart içindeki kod koşturulur.
# Örnek:

z = 3    

if z > 1:
   print("z sayısı 1'den büyüktür")
elif z > 2:
   print("z sayısı 2'den büyüktür")
elif z > 3:
   print("z sayısı 3'ten büyüktür")
else:
   print("bilgi yok")

print ("-----------------------------------------------")

# 

# oda-sıcaklık değerini değiştirerek farklı değerlerle deneyiniz.
oda_sıcaklık = 23.5

if oda_sıcaklık < 22:
   print("oda serin yada soğuk")
elif ((oda_sıcaklık >= 23.5) and (oda_sıcaklık <= 25)):
   print("oda ideal ısıda")
else:
   print("oda ısısı normalden fazla")     


print ("-----------------------------------------------")




# içiçe karşılaştırmalar:
# t sayısını farklı değerlerle deneyerek sonuçları gözlemleyiniz.
t = 34

if (t > 0):
   if (t%3 == 0):
      print("t sayısı üçe bölünebilir")
   else:
      print("t sayısı üçe bölünemez")
else:
   print("girdiğiniz sayı negatiftir.")


print ("-----------------------------------------------")

# While döngüsü:
# while içerisindeki komutlar, ilgili koşulu yanlış olana kadar
# tekrarlı bir biçimde çalışır:


# aşağıdaki while döngüsünün çıktılarını inceleyiniz:    
sayac = 1

while (sayac < 10):
    print(sayac)
    sayac += 1    # sayac değişkenini her defasında 1 arttırır

print ("-----------------------------------------------")

# break anahtar kelimesi:
# Genelde if ile beraber kullanılır. Break görüldüğü yerde döngüden çıkılır.    
    
    
sayac2 = 0

while sayac2 < 10:
    sayac2 += 1
    if sayac2 == 5:
        break
    print("while döngüsü içerisinde", sayac2)


print("while döngüsünün dışına çıkılmıştır.")


# continue anahtar kelimesi:
# Genelde if ile beraber kullanılır. O andaki iterasyonu keser. Döngü devam eder:    
# aşağıdaki döngü 1'den 10'a kadar (10 dahil) tek sayıları ekrana yazar:

    
sayac3 = 0
while sayac3 < 10:
    sayac3 += 1
    if sayac3 % 2 == 0:
           continue
    print(sayac3)

print ("Listeler")



# LİSTELER VE İTERASYONLAR

# listeler birden fazla değişkeni tutmaya yarayan nesnelerdir.

# aşağıda bir liste oluşturuluyor:

liste = [] 
# listenin nin hangi sınıfa ait olduğu:
print (type(liste))
# liste, list sınıfına ait bir nesnedir.

# Python listeleri farklı tiplerdeki değişkenleri tutabilir.
l2 = ["bu bir string", 12]

#diğer liste yaratma yöntemleri aşağıda verilmiştir:

liste1 = list() # bir boş liste
liste2 = list([22, 34, 61]) # 22, 34, 61 sayılarını içeren bir liste
liste3 = list(["ali", "ahmet", "osman"]) # stringler listesi
liste4 = list("python") #  p, y, t, h, o, n karakterlerinden oluşan bir liste

print ("-----------------------------------------------")

# liste elemanlarına erişim:

liste = [1,2,3,4,5]

print (liste[0])
print (liste[1])
print (liste4)


print ("-----------------------------------------------")

# len listenin uzunluğunu verir:
    
print (len(liste))    


print ("-----------------------------------------------")


# in kullanımı:
# in işleci bir değerin ilgili liste içerisinde olup olmadığını 
# kontrol eder. Var ise True yok ise False döner.
# not in şeklinde de kullanımı vardır:
    
print (2 in liste2)
print (34 in liste2)
print (34 not in liste2)
print ("-----------------------------------------------")

# max, min ve sum fonksiyonları:

print(max(liste2))  # listedeki maks. değerdeki elamanı döner
print(min(liste2))  # listedeki min. değerdeki elemanı döner
print(sum(liste2))  # listedeki tüm elemanları toplar ve sonucu döner

print ("-----------------------------------------------")

# Liste dilimleme:
    
liste5 = [11,33,44,66,788,1]

print(liste5[0:5]) # indeks olarak 0'dan 4'e kadar olan tüm değerleri döner.
# 5'i dahil etmez

print(liste5[:3]) # indeks olarak 0'dan (en baştan) 3'e kadar olan değerleri döner.
# 3 dahil değildir.

print (liste5[2:]) # indeks olarak 2'den başlar sonuna kadar tüm elamanları alır.
# 2 dahildir.


print (liste2[-1])  # listenin son elemanını döner. 
print (liste2[-2])  # listenin sondan ikinci elemanını döner.

print ("-----------------------------------------------")



# listelerde + ve  * operator kullanımları:
    
    
liste6 = [11, 33]
liste7 = [1, 9]
liste8 = liste7 + liste6  # iki listeyi sırayı bozmadan birleştirir.
print(liste8)


liste9 = 3*liste7  # liste elemanlarını kopyalar. Burada 3 defa kopyalıyor.

print (liste9)

print ("-----------------------------------------------")

# Sık kullanılan liste fonksiyonları:
print ("Liste Fonksiyonları:")    
liste10 = [2, 3, 4, 1, 32, 4]
liste10.append(19) #listenin sonuna 19 sayısını ekler. None döner.
print(liste10)
print ("-----------------------------------------------")

print(liste10.count(4)) # 4 sayısının liste içerisinde kaç defa tekrar edildiğini döner
print ("-----------------------------------------------")
liste11 = [99, 54]
liste10.extend(liste11) # liste 10'a liste 11'i ekler. None döner.
print (liste10)
print ("-----------------------------------------------")
print (liste10.index(4)) # 4 sayısının listedeki indeksinin ilk görüldüğü yeri döner
print ("-----------------------------------------------")
liste10.insert(1, 25) # indeks 1 konumuna 25 sayısını yerleştir. Eleman silmez. Araya yerleştirir. None döner.
print (liste10)
print ("-----------------------------------------------")
eleman = liste10.pop(2) # 2. indeksteki sayıyı listeden çıkarır. Çıkardığı elemanı döner.
print (eleman)
print (liste10)
print ("-----------------------------------------------")
eleman2 = liste10.pop() # eğer pop() şeklinde parametresiz kullanılırsa son elemanı çıkarır.
print (eleman2)
print (liste10) 
print ("-----------------------------------------------")
liste10.remove(32) # ilk görülen konumdaki 32 değerini listeden kaldırır. None döner.
print (liste10)
print ("-----------------------------------------------")
liste10.reverse() # listeyi tersine çevirir. None döner.
print (liste10)
print ("-----------------------------------------------")
liste10.sort()
print (liste10) # listeyi artan biçimde yeniden yazar. None döner.

print ("-----------------------------------------------")







# İTERASYONLAR: 
# Yineleme anlamındadır.Nesneler üzerinde adım adım ilerlemeye olanak sağlar.
# İteratif yaklaşım 'for' deyimi ile kurgulanır:
print ("İterasyonlar")

# For kullanımı:
    
liste12 = [10,23,54,7,0,-21]

# liste elemanları aşağıdaki gibi yazdırılabilir:
# Listenin tüm elamanlarında bu şekilde gezilebilir:
    
for i in liste12:
    print(i)


print ("-----------------------------------------------")

# For kullanımı1 : range (a,b)


for i in range(1, 10): # 1'den başlar 10 dahil değildir:
    print(i)

print ("-----------------------------------------------")



# For kullanımı2 : range (a)


for i in range(10): # 0'den başlar 10 dahil değildir:
    print(i)

print ("-----------------------------------------------")



# For kullanımı3 : range (a,b,c)

for i in range(1, 19, 2): # 1'den başlayıp 19'a kadar, 19 dahil değil, 2'şerli arttırarak yazar.  
    print(i)

print ("-----------------------------------------------")

# liste uzunluğu üzerinden gidilerek:
    
for i in range (len(liste12)):
    print (liste12[i])



 