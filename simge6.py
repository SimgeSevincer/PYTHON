# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 16:47:15 2022

@author: Lab435-Hoca
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#katar (string) işlemleri

yer="Beykent Üniversitesi"

print(yer[3])
print(yer[-2])
print(yer[:-2])
print(yer[-2:])




print("--------------------")




#yer[2]="w"

print(len(yer))




print("--------------------")




for i in yer:
    print(i)
    
    
print("--------------------")


def harfBul(cümle,harf):
    i=0
    while(i<len(cümle)):
        if(cümle[i]==harf):
            return i
        i+=1
    return -1

a=harfBul("ayazağa yerleşkesi","ğ")
print(a)



print("--------------------")



yer2="Ayazağa Yerleşkesi"
yer2='Ayazağa Yerleşkesi'

yer2='Sınav için Taksim\'e gittim'#özel karakterlerin string içinde kullanımı \ bu işaret sayesinde gerçeklerşir.
print(yer2)



print("--------------------")



print("simge\nsevincer")#alt satıra atlamak için\n kullanır.



print("--------------------")



#sekme karakteri (\t)

ogrenciler=[["ali","öztürk",12214],
            ["mehmet","yılmaz",585808],
            ["ayşe","ertekin",12345]]

for obje in ogrenciler:
    print(obje[0],obje[1],obje[2])
    
    
    
print("--------------------")



for obje in ogrenciler:
    print(obje[0],'\t',obje[1],'\t',obje[2])#\t ile listeler arası yazdırma yaparken yapısal olarak aynı tipteki adları alt alta getirir. raporlamaya yardımcı olur.



print("--------------------")



#cümle biçimleme

ders_saati="16.00"
print("Dersim saat %s'da başlıyor" %ders_saati)#virgül konmayacak çünkü birleştiriyo gibi düşünür virgül konduğunda.

mevcut=80

print("sınıf mevcudu toplam %d kişidir." %mevcut)

print("Sınıf mevcudu %d kişi olan GP dersi saat %s itibariyle başlıyor." %(mevcut, ders_saati))



print("--------------------")



#Fonksiyonlar

print("Sınıf mevcudu {0} kişi olan GP dersi saat {1} itibariyle başlıyor.".format(mevcut,ders_saati))

liste=[60,"13.30"]

print("Sınıf mevcudu {0} kişi olan GP dersi saat {1} itibariyle başlıyor.".format(*liste))



print("--------------------")



print(yer)
print(yer.lower())#tamamını küçük harfe çevirir.
print(yer.upper())#tamamını büyük harfe çevirir.
print(yer.title())#kelimelerin ilk harfini büyük yapar.



print("--------------------")



def kelimeBul(cümle, kelime):
    for i in range(len(cümle)-len(kelime)+1):
        if(cümle[i: i+len(kelime)]==kelime):
            return i
    
    return -1

b=kelimeBul("Beykent Üniversitesi Ayazağa Yerleşkesi","Yerleşkesi")
print(b)
        

