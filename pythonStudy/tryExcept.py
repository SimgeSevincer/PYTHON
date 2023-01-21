# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:03:49 2022

@author: Lab435-Hoca
"""

#İSTİSNALAR 
#GÖREVİ:hatayı yönetmekle alakalıdır.hatayı yakalamak ön tanım istisanlar hatalar fırlatılan istisnaları yönetmek birden fazla istisna olursa da önceliğe göre yönetmek ve kendi istisnasını üretmek
#Hata varsa yazılım durmadanilerlemesi için kullanılır.


#print(x) burada hata olacağından abc çıktısı üretilmez
#print(abc)
#eğer şöyle yaparsak hata düzelir
try:
    print(x)
    print("dşsl")#print(x) yanlış olduğu için bu da çalışmaycak.
except:
    print("abc")
    print("sşaldfjaş")
#trydaki doğru çalışmazsa expectin çıktısı gözükücek ve kod akışı devam eder
print("xyz")

print("---------------------")

yas="20a"

try:
    if int(yas)>=18:
        print("yaş ehliyet için uygundur")
    else:
        print("yas ehliyet için uygun değildir")
except:
    print("HATA!!,Yaş düzgün girilmedi.")

print("-------------------")

#ÖN TANIMLI İSTİSNALAR

#print(int("yirmi"))
"""
a=[2,5,1,4,"ab"]
a.sort()
print(a)
#hata verir...
"""

#Genel mekanizma aşağıdaki gibidir.

try:
    print("işletilecek blok")
except:
    print("hata olduğunda işletilecek blok")

#ÇOKLU İSTİSNA MEKANAZİMASI
"""
tyr:
    işletilecek blok

except hatasınıfı1:
    sınıf1 tipinde hata ayıklanırsa işletilecek blok 
    
except hatasınıf2:
    sınıf2 tipinde hata ayıklanmoırsa işletilecek blok 

expect:
    diğer hatalar yakalnadığınmda işletilecek blok
#çalışma mantığı if elif ve else gibi
"""

print("----------------------------------")

#LOOPS sınavda çıkabilir
try:
    
    for i in ["5",(5,4),9,'m','6']:
        print(int(i))

except TypeError as hata1:
    print("tip hatası:",hata1)# (5,4) tuple tip hatsı verir. listede ilk tuple olduğu için 'm' yi görmezden gelip tupleın hatsaını çevirir.

except ValueError as hata2:
    print("değer hatası:",hata2)#listede 'm' (5,4)ten önce olsaydı bu expect dönecekti.'m' değer hatası verecekti.

except:
    print("diğer hata")
    
print("--------------------------------")
#aşağıdaki örnekte forun içinde try except kullanmamız bütün elemanları yazdırıp hataları görmemizi sağladı.
    
for i in ["5",(5,4),9,'m','6']:
    try:
        print(int(i))

    except TypeError as hata1:
        print("tip hatası:",hata1)

    except ValueError as hata2:
        print("değer hatası:",hata2)

    except:
        print("diğer hata")

print("------------------------------")

#HATA YÜKSELTME( HATA FIRLATMA)

x="24"

try:
    if not type(x) is int:#bu blok hatalı olup olmadığı için değil de hata tanımlamak için kullanıldı.
        raise TypeError ("x için yalnızca tamsayı girilebilir.")

except:
    print("hata alındı")

if not type(x) is int:
        raise TypeError ("x için yalnızca tamsayı girilebilir.")#hata olarak ekranda bu ifade çıktı verecek. ve program devam etmeyecek çünkü bu durumu handle etmedik.yani tyr içinde kullanmadık.









































