# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:47:48 2022

@author: Lab435-Hoca
"""

bölgeler=["Bolu","Manavgat","Edirne","Van","Alanya","İnegöl"]

for b in bölgeler:
    b=b.lower()
    if b.find("bolu")>-1:
        print(b)



print("--------------------")



print("inebolu".endswith("bolu"))#stringin bolu ile bitip bitmediğine bakıp true veya false sonucu verir.
print("inebolu".startswith("ine"))


splitted="Beykent Ünivesitesi Ayazağa Yerleşkesi".split()#boşık gördüğünde bu boşlukjlara göre liste elemanları oluşturur.
print(splitted)

info="Beykent: Mühendislik Mimarlık Fak.:Bilgisayar Müh.:Görsel Programlama"
print(info.split(":"))#splitin içine yazadığımız karakterin olduğu yere göre liste elemanlarını ayırır ve oluşturur.



print("--------------------")



email="mehmet.yilmaz@gmail.com"

[user_name,domain]=email.split("@")
print(user_name)
print(domain)

user_name2=email.split("@")[0]
print(user_name2)



print("--------------------")



mail_addr='@'.join(["m.yilmaz","gmail.com"])#splitin tam tersi işlevini görür.
print(mail_addr)



print("--------------------")



yer3="tıp fakültesi beylikdüzü yerleşkesi"
print(yer3.replace(" ","_"))#replace içine yazdığımız birinici karakterle ikinici karakteri yer değiştirip yer3 ü revize eder...

print(" beykent   ".strip())#sonda ve başta olan boşlukları kaldırır.
 


print("--------------------")



fiyat1="120"
fiyat2="120.50"#bunda uygulanınca olmuyor araştır.

print(fiyat1.isnumeric())#string olmasına rağmen bu sayısal türe çevrilebiliyorsa ifade true döner



print("--------------------")

#DOSYA İŞLEMLERİ

"""F=open("ornek.txt",encoding="utf-8")#utf-8 yazmazsak türkçe karakterlerde sorun yaşarız.
bilgi=F.readline()
print(bilgi)#1.satır okundu..

bilgi=F.readline()
print(bilgi)#2.satır okundu..

"""

"""print("--------------------")

s=open("ornek.txt",encoding="utf-8").read()
print(s)

F.close()

F=open("ornek.txt",encoding="utf-8")

for l in F:
    print(l.strip())

#print(type(F))
    
F=open("ornek.txt",encoding="utf-8")
l=F.readlines

print(type(l[2]))"""