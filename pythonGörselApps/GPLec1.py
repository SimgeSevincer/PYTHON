# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:46:59 2022

@author: umitozturk
"""

import keyword

# ANA BAŞLIK: DEĞİŞKENLER, İFADELER, DEYİMLER



# Python dilinde ekrana birşey yazdırmak yalnızca bir satırlık kod ile yapılabilir:  
# Aşağıda üç farklı tipte değer ekrana yazdırılmıştır.  
print (2022)
print (2500)
print (3.14)

print ("-------------------------------------")

# type fonksiyonu ilgili değerin tipini döner. print ile aşağıdaki gibi yazdırırız.

print (type("merhaba dünya"))
print (type(2500))
print(type(3.14))

print ("-------------------------------------")

# print ile farklı tipteki değerler tek seferde ekrana yazdırılabilir:
    
print ("pi sayısının değeri:", 3.14)    

print ("-------------------------------------")

# Değişken, değer taşıyan isimdir. Aşağıdaki gibi oluşturulurlar:

adres = "Fatih mahallesi, gül sokak, No: 21 "
fiyat = 150
cos60 = 0.5

print (adres)
print (fiyat)
print (cos60)
print (type(adres))
print (type(fiyat))
print (type(cos60))

print ("-------------------------------------")

# Bir değişkenin değerini ve tipini program akışında değiştirebilirsiniz:
    
cos60 = "cos 60 değeri 1/2'dir "
print ("cos60 değişkenin değeri ve tipi değişmiştir:", type(cos60))
    
# -------------------------------------

# Önce işlem sonra atama yapılır:
    
x = 9+3   
print (x) 

x = x + 2
print (x)  

print ("-------------------------------------")
  
#Değişken ismi belirlemede kural:
#A-Z, a-z ve alt çizgi ile başlayabilir. Ancak rakam ile başlayamaz
#A-Z, a-z ve rakam kombinasyonları kullanılabilir. Rakam ile başlaması yasaktır.
#Matematiksel işleçler gibi özel karakterler kullanılamaz.

# Yanlış kullanıma örnekler: 
#değer$ = 12
#abc?
#9x = 5

    
# Değişken isimleri büyük küçük harf duyarlılığına sahiptir.

telefon = "7987897"
Telefon = "5435435" 

print (telefon)
print (Telefon)

print ("-------------------------------------")


# Anahtar kelimeler değişken isimleri olarak rastgele atanamazlar.

# Yanlış kullanıma örnek: 

#lambda = 23   # lambda anahtar kelimedir. Herhangi bir değişken ataması
# için kullanılamazlar. 

print ("-------------------------------------")
  
# Anahtar kelimeler listesini bulmak için 
# önce keyword modülünün projeye eklenmesi ve ardından aşağıdaki kod satırının
#yazılması gereklidir:
    
print (keyword.kwlist)
     

print ("-------------------------------------")

# Python yorumlayıcının çalıştırabildiği en küçük 
# program koduna ifade denir. Bir program birçok ifadeden oluşur.
# hesaplama yapabilen özel karakterlere işleç denir
# işleç tarafından işlenen değerlere işlenen denir.
# Matematiksek işleçler:
# Matematiksel işlemlerin öncelik sırası python'da uygulanmaktadır.    
    
print (4 + 4) #toplama
print (16.7 - 4)  # çıkarma
print (13*14) # çarpma
print (19/4)  # bölme
print (19//4)  # tamsayı bölme
print (19%4)  # mod alma
print (2**5)  # kuvvet alma
print (2+5*2) # matematiksel öncelik uygulanır.

print ("-------------------------------------")

# Dairenin çevresi:
yarıçap = 2
pi = 3.14
print (2*pi*yarıçap)

print ("-------------------------------------")

# cümle işleçleri + ve * 'dır.
# Bazı önemli kullanım örnekleri:

print ("kırmızı","kalem")  #boşluğu kendi koyar
print ("kırmızı"+"kalem")  # boşluk gerekirse manuel ayarlanmalıdır.
print ("9"+"9")
print (type("9"+"9"))
print (3*"Python")  # üstüste 3 defa stringi yazar. boşluk koymaz.

print ("-------------------------------------")

# Tip dönüşümleri

x ='3'
print (type(x))
y = 4
print (type(y))

print (x*y)  # Tip3: Sonucu 12 bekliyorsak Anlamsal hataya (Tip3) düşeriz. 

# Bu durumda hata almamak için:

print (int(x)*y)

# int () içerisine gönderdiğimiz string mutlaka rakamlardan oluşmalıdır. Negatif olabilir.
# Aksi halde runtime hatası alınır. (çalışma zamanı hatası alınır):
    
#yanlış kullanım örneği:
#print (int("5ali")*3)    
    
print ("-------------------------------------")

# int fonksiyonunun çıktısını başka bir değişkene atayarak sonuç bulunabilir:

z = int(x)
print (z*y)

print ("-------------------------------------")


# Bir deyim, değer, değişken ve işleçlerden oluşur:
# Atanmamış bir değişkeni kullanamazsınız:
    
#yanlış kullanım örneği:   
#print (5*t)  # t değişkeni tanımlanmamıştır.  





# ANA BAŞLIK: FONKSİYONLAR (İŞLEVLER):
       
    
# fonksiyon tanımlama:

def abc ():
    print("abc fonksiyonu içerisindesiniz")
    
abc()    

print ("-------------------------------------")

# abc foknsiyonu belleğin neresinde konumlanmış bilgisi:
print (abc)
print ("-------------------------------------")


# işlev içerisinde işlem görecek işlev girdilerine argüman denir.
# Argümanlar da daha önce anlatılan değişken isimlendirme kurallarına 
# uygun olmalıdır. 


def abc (x):
    print ("x parametresinin aldığı değer:" , x)
    
    
    
print (abc(19)) # çıktı ekrana yazılır. 
#Fonksiyon birşey dönmediği için ayrıca None da ekrana yazılır

print ("-------------------------------------")


#Bir diğer kullanım:
    
    
def abc2 (x):
    t = x + 5
    print ("x parametresinin aldığı değer:" , t)    
    
print(abc2(19))

print ("-------------------------------------")

#Bir diğer kullanım:

def abc3 (x):
    t = x + 5
    return t

t = abc3 (19)

print(t)


print ("-------------------------------------")


# önce işlem sonra işleve girdi gerçekleşir:
    
# en güzel örneği print fonksiyonudur:
    
print (20 + 12)  
# diğer örnekler:
    
print (2*abc3(3*2))

# değişken ataması yaparak:
    
t = abc3(3*2)
print (t)

print ("-------------------------------------")


# fonksiyonun return kısmında da hesaplama yapılabilir:
    
    
def abc4(x):
    return x+5

#abc3 ve abc4 fonksiyonları aynı dönüşü yapar.

print ("-------------------------------------")

# Fonksiyon içinde tanımlanan değişkenler yereldir:


def abc5(k):
    l = 3
    return (l+k)


t = abc5(5)
print (t)


# l değişkeni yereldir. Tanımlandığı fonksiyon dışından ulaşılamaz.

#Yazım hatası alır:
#print (l) # hata !!!

print ("-------------------------------------")

# Python fonksiyonlarına dilediğiniz sayıda ve tipte argüman gönderebilirsiniz:
    
def carp (x, y):
    print (x*y)

print (carp(3,4))
    
print ("-------------------------------------")

# argüman tipleri forse edilemez:
    
print (carp("beykent",4))

print ("-------------------------------------")

# Çağrılma yapılırken, fonksiyon içerisinde argümanlar isimleriyle
# doğru şekilde atanması koşuluyla yer değişebilir:
    
def bölüm (bölünen, bölen):
    print (bölünen/bölen)
    

print(bölüm(bölen=3, bölünen=18))

print ("-------------------------------------")
# namespace: belli alandaki değişkenler o alanın dışındakilerden bağımsızdır
# 

m = 50

def degistir ():
    #global m  # bu kod satırı m değişkenini global yapmaktadır. Bu kod satırını
    # açarak tekrar çalıştırdığınızda daha üst seviyeden tanımlı m, 80 olacaktır. 
    m = 80
    return (m*2)

t = degistir()
print(t)
print(m)


# Bir işlevi başka bir işlevden çağırma:

def topla (a,b):
    return  a+b

def ortalama (a,b):
    t = topla(a,b)
    return t/2

print (ortalama(20,30))

print ("-------------------------------------")


# Bir python fonksiyonu birden fazla değer döndürebilir:
    
def cember (r):
    c = 2*3.14*r # dairenin çevresi 2 pi r
    a = 3.14*(r**2) # dairenin çevresi pi r kare
    return c, a

# sıralamaya dikkat !
cevre, alan  = cember(8)

print ("dairenin cevresi:", cevre, "dairenin alanı:", alan)