# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:01:42 2022

@author: Lab435-Hoca
"""


#ara sınav sorusu

m="5..5"

def Isfloat(m):
    try:
        float(m)
        return True
    except:
        return False
if(m.isnumeric() or Isfloat(m)):
    print(m)

else:
    print("geçerli fiyat bilgisi girilememiştir.")
    
print("--------------------------------")
    
#KULLANICI İSTİSNALARI 

class GecersizDeger(Exception):
    def __init__ (self,hata_iletisi):
        self.hata=hata_iletisi
        
    def __str__(self):
        return self.hata
    
def yasVer(x):
    if x<0 or type(x)==str or type(x)==float:
        raise GecersizDeger("yaş için geçersiz değer girilmiştir.")
    return x

#raise GecersizDeger("Geçersiz yaş değeri")#bu hata döner ve program patlar o yüzden yorum satırına alınmalı
    
try:
    print(yasVer("5"))
    
except GecersizDeger as hata:
    print("yas bilgisi girilemedi:",hata)
    
except:
    print("diğer hatalar")
#diğer hatalar çıktısı vermesinin sebebi fonksiyon içindeki ifin ilkönce x<0 ı incelemesi ve burdan patlak verince excepte düşmesi.
    
"""
#Mekanizma

try:
    işletilecek blok
except:
    hata yakalandığında işletilecek blok
else:
    hata ile karşılaşılmadığında işletilecek blok
"""

print("----------------------------")

try:
    print(yasVer(-5))
    
except:
    print("hata için geçersiz değer")
    
else:
    print("yas bilgisi başarıyla alındı.")
    
print("---------------------------------")

try:
    print(yasVer(10))
    
except:
    print("hata için geçersiz değer")
    
else:
    print("yas bilgisi başarıyla alındı.")


print("--------------------------")
"""
#Mekanizma

try:
    işletilecek blok
except:
    hata yakalandığında işletilecek blok
else:
    hata ile karşılaşılmadığında işletilecek blok
finally:
    son blok her zaman çalışır.koşulsuz şartsız çalışır.
    
"""

for i in ["5",(5,4),9,'m','6']:
    try:
        print(int(i))

    except TypeError as hata1:
        print("tip hatası:",hata1)

    except ValueError as hata2:
        print("değer hatası:",hata2)

    except:
        print("diğer hata")
    
    else:
        print("else")#hata olmadığında çalışır hata durumunda çalışmaz.
    
    finally:
        print("finally çalıştı")#döngü her döndüğünde çalışacak. hata olsun olmasın çalışır
    















