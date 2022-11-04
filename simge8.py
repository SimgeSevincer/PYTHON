# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:49:09 2022

@author: Lab435-Hoca
"""

F=open("ornek.txt",encoding="utf-8",mode="a")
F.write("\n")
F.write("yeni satır eklenmiştir\n")
F.write("bir satır daha eklendi\n")

F.flush()#yeni satırları yazar compilera.

F.close()

F=open("ogrenciler.txt",encoding="utf-8",mode="w")

ogrenciler=[["ali","öztürk","12214"],
            ["mehmet","yılmaz","585808"],
            ["ayşe","ertekin","12345"]]
for o in ogrenciler:
    for i in o:
        F.write(i+":")
    F.write('\n')
F.close()




print("----------------")



F=open("ogrenciler.txt",encoding="utf-8")


ogr_listesi=[]


for l in F:
    ls=l.strip()
    ll=ls.split(":")
    ogr_listesi.append([ll[0],ll[1],ll[2]])
    
print(ogr_listesi)



print("----------------")



#TUPLES AND DICTIONARY

#listelerden tek farkı normal parantezle yazılması ve üzerinde bir modifikasyon yapılmaması(tuples)

değerler=("12.30","20.00",4)

print("otobüsün kalkış saati %s varış saati %s. Mola kalkıştan %d saat sonra verilecektir." %değerler)

print(değerler[2])

#değerler[2]=3 hata verir çünkü tuple üzerinde işlem yapılmaz.

(kalkış,varış,mola)=("12.00","18.00",3)#böyle bir tuple tanımı yapılabilir 
kalkış,varış,mola="12.00","18.00",3 #böyle de tanımlanabilir.
#böyle yazdıktan sonra
mola=5#diyebiliriz sorun olmaz.sadece (kalkış,varış,mola) şeklinde yazarsak değiştirebiliriz.



print("----------------")



email="umitozturk@beykent.edu.tr"
(username,domain_name)=email.split("@")

print(username)

#tupleın en çok kullanıldığı bölüm

def topla(sy1,sy2,sy3):
    return sy1+sy2+sy3

t1=topla(3,4,5)
print(t1)

#t2=topla(3,4,5,6) hata verir gereğinden fazla argüman aldığımız için bunu düzeltmek için alttaki örnek kullanır.

def topla(*sayılar):#böylelikle *sayılar tuple gbi davranarak istediğimiz kadar argümanı toplayabiliriz.
    toplam=0
    for i in sayılar:
        toplam=toplam+i
    return toplam

t3=topla(2,3,4,5)
print(t3)



print("----------------")



#DİCTİONARY

d1={22565:"ali öztürk",334634:"ayşe ertekin",89798:"mehmet yılmaz"}#sayılar key anahtar isimler.

d2={}

print(d1[22565])

d1[675]="ahmet çetinsoy"
print(d1)

for key in d1:
    print("anahtar:",key,"değer",d1[key])


del d1[22565]

print(d1)


print(675 in d1)#675 keyi d1 de var mı diye kontrol edip true false döner

d2={"mike":41,"bob":3}
d3={"bob":3,"mike":41}

print(d2==d3)

print(len(d1))


#FONSKİYONLAR

print(d1.popitem())#sondakini siler
print("-------------------")
print(d1)
print("-------------------")
d1.clear()
print(d1)

d1={22565:"ali öztürk",334634:"ayşe ertekin",89798:"mehmet yılmaz"}

print(d1.keys())#keysleri yazar.

for k in d1.keys():#keysleri yazar.
    print(k)


print(d1.values())#valuesleri döndürür

for v in d1.values():#valuesleri döndürür.
    print(v)


print("-------------------")


print(d1.get(334634))#değeri,,get içine anahtarı yazınca alırız.
print(d1.get(3346,"sözlükte bulunamadı"))#anahtar bulunmazsa yanındaki argüman yazılacak.


print("-------------------")


d1.pop(334634)#anahtardaki değeri siler.
print(d1)


print("------------------")


d4={22565:"veli öztürk",5676576:"hakan sözen",121231:"özlem kaya"}
d1.update(d4)#anahtar değeri aynı olanı günceller.

print(d1)













