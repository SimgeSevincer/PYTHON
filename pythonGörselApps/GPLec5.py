# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:40:08 2022

@author: umitozturk
"""

# İSTİSNALAR

# Program hata ile karşılaşırsa nasıl yönetilmelidir ?
# Hata oluştuğunda programın sonlanmasına mani olarak
# kullanıcı bilgilendirmesi yapılmalıdır ve kodun işleyişi devam etmelidir.
# İstisna yönetimi şunları kapsar:    
# Hatayı yakala
# Ön tanımlı istisnalar kullan
# Hatalardan fırlatılan istisnaları yönet
# Birden fazla istisnanın olduğu durumları dikkate al
# Hata yükselt
# Kendi istisnanı oluştur ve yükselt

# x adında bir değişkeni yazmaya çalışırsak:
# x adında bir değişken bulamayacağı için hata verir.
# Dolayısıyla aşağıdaki satır hata verir:    
# print(x)

try:
    print (x)
except:
    print ("hata: x değişkeni tanımlı değildir")    
    
print ("----------------------------------")

yas = "20a"

# try-except yapısında program try içerisinde hata aldığında derhal excepte geçer
# ve oradan devam ederek programı düzgün şekilde sonlanır.

try:
    if int(yas)>=18:
        print ("Yaşınız ehliyet almak için uygundur")
    else:
        print ("yaşınız ehliyet almak için uygun değildir")
except:
        print ("hata: yaş düzgün girilemedi" )
        
        
print ("----------------------------------")        

# yukarıdaki aynı kodu try-except kullanmadan yapsaydık
# hata alınan yerde program hatayı gösterirdi ve daha fazla devam etmeden 
# tam o noktada istenmeyen şekilde kapanırdı.  
       
"""
if int(yas)>=18:
    print ("Yaşınız ehliyet almak için uygundur")
else:
    print ("yaşınız ehliyet almak için uygun değildir")
"""
               
# Ön tanımlı istisnalar:
# Aşağıdaki kod bloklarının hangi hataları verdiğini inceleyiniz:
    
#print (int('yirmi')) 

"""
a =  [2,5,1,"ab"]
a.sort()   
print(a)        
        
"""      
        
# genel mekanizma:

try:
    print ("işletilecek blok")
    
except:
    
    print ("hata olduğunda işletilecek blok") 


# Çoklu istisnalar:

# Program çalışması esnansında birden fazla istisna gerçekleşebilir:


        
# çoklu istisna mekanizması:

"""    
try:
   işletilecek blok        
        
except hatasınıfı1:
    
    sınıf1 tipinde hata yakalanırsa işletilecek blok

except hatasınıfı2:
    
    sınıf2 tipinde hata yakalanırsa işletilecek blok

except:
    
    diğer hatalar yakalandığında işletilecek blok 

"""

# Önemli!!! Loop iki farklı şekilde kurulmuştur. Aradaki farkı algılayıp açıklayabilmelisiniz.
print ("-------loops---------")
try:
    for i in ["5", (5,4), 9, 'm', '6']:
        print (int(i))
        
except TypeError as hata1:
    print ("tip hatası !!!:", hata1.args[0])
    
except ValueError as hata2:
    print ("değer hatası !!!", hata2.args[0])
    
except:
    print ("diğer hata")    
    

print ("-------------------loop2----------------------------")    

for i in ["5", (5,4), 9, 'm', '6']:
    
    try:
        print (int(i))
        
    except TypeError as hata1:
        print ("tip hatası !!!:", hata1.args[0])
    
    except ValueError as hata2:
        print ("değer hatası !!!", hata2.args[0])
    
    except:
        print ("diğer hata") 
    
print ("-------------------hata yükseltme----------------------------")      
    
# Hata Yükseltme (Hata fırlatma):

x = "24"


try:
    if not type(x) is int:
        raise TypeError ("x için yalnızca tamsayı girilebilir")    # bu hatayı kullanıcı olarak biz tanımladık ve fırlattık.

except:
    print ("hata alındı")
print ("-----------------------------------------------")  



# Aşağıdaki kod bloğunu açarsak ve koşul ifi sağlarsa program parantez içerisindeki yazıyı
# fırlattığımız hata sınıfı ile birlikte ekrana yazar.   

"""
if not type(x) is int:
    raise TypeError ("x için yalnızca tamsayı girilebilir") 

"""

# Örneğe özel açıklama: Tipi net tanımlayamadığımız durumda TypeError yerine Exception yazılabilir.
# Fakat bu yazım debugging esnasında daha az bilgilendiricidir. 
print ("abc")

# isnumeric floatı tanımıyor hem tamsayı hem de floatı if içerisinde tanıt
# yapısal olmayan durumlarda kullanıcıya bilgi ver, arasınav sorusu alternatif yanıt:


def Isfloat(m):
    try:
            float(m)
            return True
    except:
            return False

m = "55"

if (m.isnumeric() or Isfloat(m)):
    print (m)
else:
    print ("geçerli fiyat girilememiştir")

   

# Kullanıcı İstisnaları

"""

Python'da ön tanımlı yeterli istisnalar olsa da geliştirici kendi istisnasını 
oluşturmak zorunda kalabilir. Yöntem aşağıdaki gibidir:

""" 


class GecersizDeger (Exception):
    def __init__(self, hata_iletisi):
        self.hata = hata_iletisi
        
    def __str__(self):
        return self.hata
    
def yasVer (x):
    if x < 0 or type(x)==str or type(x)==float:
        raise GecersizDeger("Yaş için geçersiz değer")
    return x

# aşağıdaki kod satırı ile Kullanıcı tanımlı GecersizDeger tipinde hata fırlatılır
# mekanizmada except olmadığı için program istenmeyen şekilde durur.
#raise GecersizDeger("geçersiz yaş değeri")


print ("-----------gecersizdeger---------------")
try:
    print (yasVer("5"))
except GecersizDeger as hata:
    print ("yaş bilgisi girilemedi:", hata)
    
except: 
    print ("diğer hata")

# Önemli!!! yukarıdaki kod bloğunda "5" yazıldığında neden "diğer hata"ya girilmiştir?

# Try ifadesi herhangi bir istisna ile karşılaşmaz ise else çalışır. 

# mekanizma:
    
"""    
try:
   işletilecek blok        
        
except:
    
    Hata yakalandığında işletilecek blok

else:
    
    hata ile karşılaşılmadığında işletilecek blok



"""
print ("------------------xxxx-------------------------")
try:
    print (yasVer(-5))
except: 
    print ("HATA: yaş için geçersiz değer")
else:
    print ("yaş bilgisi başarıyla alındı")

print ("abc")

# önemli!!! yukarıdaki örneği 23, 23a, "23","23.a", 22.4 ve "22.4" için deneyiniz.
# sonuçları gözlemleyiniz.


# finally anahtar kelimesi 
# try ifadesi hata yakalasa da yakalamasa da son bir bloku işletecektir. 
# Bu blok finally ifadesi altındaki bloktur. 


# mekanizma:
    
"""    
try:
   işletilecek blok        
        
except:
    
    Hata yakalandığında işletilecek blok

else:
    
    hata ile karşılaşılmadığında işletilecek blok

finally:
    
    Son blok her zaman işletilir. 

"""
print ("-------------------------------------------")

try:
    print (yasVer(-5))
except: 
    print ("HATA: yaş için geçersiz değer")
else:
    print ("yaş bilgisi başarıyla alındı")
finally:
    print ("finally son kez çalışır")


print ("-------------------------------------------")

try:
    print (yasVer(18))
except: 
    print ("HATA: yaş için geçersiz değer")
else:
    print ("yaş bilgisi başarıyla alındı")
finally:
    print ("finally son kez çalışır")
    
    
    
# !!!ödev!!!: içerisindeki elemanları ikili tuple veya liste olan bir liste veri yapısı 
# düşünün. Bu durum için bir kontrol sağlayın. Program kontrolü şunu yapacak:
# Ana liste elemanları ikili tuple yada liste değilse "ikişer öğeli liste yada
# tüp olmalıdır'şeklinde bir istisna fırlatsın.(raise) Hata oluşmaz ise 
# listeyi direk ekrana yazsın. Kontrol edilecek liste kullanıcı tarafından verilen herhangi bir listedir.     
# örnek listeler: l1 = [[1,5],(23,4),(8,8),(2,6),(5,3),[11,9],[8,10]]  
# l2 = [[1,5],(23,4),(8,8),3,(2,6),(5,3),[11,9],[8,10,2]] 
# l3 = [[1,5],(23,4),(8,8),"asd",(2,6),(5,3),[11,9],[8,10]] gibi...
    
    
    
    
    
    







