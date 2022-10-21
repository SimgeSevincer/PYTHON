# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:58:44 2022

@author: Lab435-Hoca
"""

print(3==3)
print(3==4)
print(type(3==3))



print("-------------------")



print('a'>'b')
print('ab'>'aa')
print('aa'<='ab')
print('ab'<='aa')
print('ab'!='aa')
print('aa'!='aa')
print("beykent"=="beykent")



print("-------------------")



print(4==5)
print(4==4)
print(4!=5)
print(4!=4)
print(4>=5)
print(4>=4)
print(4<=5)
print(4<=4)
print(4>5)
print(4<4)



print("-------------------")



print(4 or 6)#4 veya 6 diyince 6 ya gitmeden 4ü yazar.
print(1 and False)#False
print(0 and True)#0
print(1>2 and "b")
#boş olmayan stringler truedur
print(9 and True)
print(1 and False)
print(7>9 or "abc")
print(7>9 and "abc")
print(9>7 or "abc")
print(9>7 and "abc")



print("-------------------")



print(not True)
print(not False)
print(not 3>4)
print(not ('m'!='m'))
print(not ('m'!='u'))



print("-------------------")



x=10

if(x<20): print("x 20den kucuktur.")#tek satırda da yazılabilir...



print("-------------------")



y=15

if(y%2==0):
    print("bu sayı çifttir.")
else:
    print("bu sayı tektir.")



print("-------------------")



today="salı"

if today=="pazartesi":
    print("Bugün pazartesi")
elif today=="salı":
    print("Bugün salı")
elif today=="çarşamba":
    print("Bugün çarşamba")
elif today=="perşembe":
    print("Bugün perşembe")
elif today=="cuma":
    print("Bugün cuma")
else:
    print("bugün cumartesi veya pazar")



print("-------------------")



z=3

if z>1:
    print("z 1 den buyuktur.")
elif z>2:
    print("z 2den buyuktur")
elif z>3:
    print("z 3ten buyuktur.")
elif today=="perşembe":
    print("Bugün perşembe")
else:
    print("z negatif veya 0 dır")



print("-------------------")



oda_sıcaklıgı=22

if oda_sıcaklıgı<22:
    print("oda serin ya da soguk")
elif(oda_sıcaklıgı>=22.0 and oda_sıcaklıgı<=25.0):
    print("oda ideal ısıda")
else:
    print("sıcaklık normalden fazla")
    


print("-------------------")



t=34

if(t>0):
    if(t%3==0):
        print("girilen pozitif sayı 3 e bolunebiliyor")
    else:
        print("girilen pozitif sayı 3 e bolunmez")
else:
    print("girdiğiniz sayı negatiftir.")



print("-------------------")



#while döngüsü:

sayac=1

while(sayac<10):
    print(sayac)
    sayac+=1



print("-------------------")



sayac2=0

while(sayac2<10):
    sayac2+=1
    if(sayac2==5):
        break
    print("dongudesiniz",sayac2)



print("-------------------")


sayac3=0

while(sayac3<10):
    sayac3+=1
    if(sayac3%2==0):#tek sayıları yazdırmak amacaıyla içerisine continue kullanırız...
        continue
    print("dongudesiniz",sayac3)



print("-------------------")



#LİSTELER:

liste=[]#bunu oluşturduğumuz an nesne oluşturmuş oluyoruz...

print(type(liste))

l2=["bu bir stringtir",12]#farklı değişken tipinde olanları yazabiliriz.

liste1=list()#liste tipinde liste1 nesnesi oluşturduk.
liste2=list([22,34,61])#liste tipinde liste2 oluşturuldu ve içine değerler atandı...
liste3=list(["simge","mert","ufuk"])
liste4=list("python")#karakterler ayrılır ve her birini listenin içine eleman olarak atar...
print(liste4)

liste5=[1,2,3,4,5]
print(liste5[0])
print(liste5[1])



print("-------------------")



print(len(liste5))#uzunluğunu verir



print("-------------------")



print(2 in liste5)#listede olup olmadığını kontrol etmek amacıyla yazıldı ya true ya false döner....
print(34 in liste5)
print(2 not in liste5)

#max min ve sum fonksiyonları

print(max(liste5))#listede max olan sayıyı bulur. sayılar için kullanılır. stringlerde hata verir.
print(min(liste5))
print(sum(liste5))#liste5 teki tüm elemanları toplar ve çıktı olarak geri döner.



























































































































































































































































































































