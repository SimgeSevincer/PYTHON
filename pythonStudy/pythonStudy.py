# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:03:49 2022

@author: Lab435-Hoca
"""
import keyword
print("hello world")
print(200)
print(type("merhaba"))
print(type(200))

print("-----------------------")

adres="sarıyer"
fiyat=150
cos60=1/2
print(adres)
print(cos60)
print(fiyat)

print("-----------------------")

cos60="cos60 1/2dir"
print("cos60ın degeri",cos60)

telefon="123456"
Telefon="987654"
print(telefon)
print(Telefon)

print("-----------------------")

x=9+3 #önce işlem yapılır daha sonra atama işlemi yapılır.
print(keyword.kwlist)
print("-----------------------")

print(4+4)
print(16.7-4)
print(13*14)
print(19/4)
print(19//4)
print(19%4)
print(2**5)
print(2+5*2)

print("-----------------------")

yarıcap=2
pi=3.14
print(2*pi*yarıcap)

print("-----------------------")

print("kırımızı","kalem")
print("kırmızı"+"kalem")
print("9"+"9")
print(type("9"+"9"))
print(3*"python")

print("-----------------------")

x="3"
y=4
print(x*y)

print("-----------------------")





import keyword
print("hello world")
print(200)
print(type("merhaba"))
print(type(200))



print("-----------------------")



adres="sarıyer"
fiyat=150
cos60=1/2
print(adres)
print(cos60)
print(fiyat)



print("-----------------------")



cos60="cos60 1/2dir"
print("cos60ın degeri",cos60)



print("-----------------------")



telefon="123456"
Telefon="987654"
print(telefon)
print(Telefon)



print("-----------------------")



x=9+3 #önce işlem yapılır daha sonra atama işlemi yapılır.
print(keyword.kwlist)



print("-----------------------")



print(4+4)
print(16.7-4)
print(13*14)
print(19/4)
print(19//4)
print(19%4)
print(2**5)
print(2+5*2)



print("-----------------------")



yarıcap=2
pi=3.14
print(2*pi*yarıcap)



print("-----------------------")



print("kırımızı","kalem")
print("kırmızı"+"kalem")
print("9"+"9")
print(type("9"+"9"))
print(3*"python")



print("-----------------------")



x="3"
y=4
print(x*y)



print("-----------------------")



print(int(x)*y)

#print((int("55a"))) #yanlıs kullanıma ornek

z=int(x)
print(z*y)



print("-----------------------")



def abc():
    print("suanda fonksiyon icerisindesiniz.")
abc()
print(abc())
print(abc)



print("-----------------------")



x=3
def abc(x):
    print("x parametresinin değeri",x)
    
abc(19)
print(abc(19))



print("-----------------------")



def abc2(x):
    t=x+5 #local degisken
    print("t parametresinin degeri",t)

abc2(19)
print(abc2(19))



print("-----------------------")



def abc3(x):
    t=x+5
    return t
t=abc3(19)
print(t)
print(abc3(19))    



print("-----------------------")

print(2*abc3(3*2))#işlem önceliğii..



print("-----------------------")



def abc4(x):
    return x+5
print(abc4(7))



print("-----------------------")



def abc5(k):
    l=3 #lokal yerel degisken
    return(l+k)
print(abc5(5))
#print(l)#l lokal oldugu icin ulaşılamaz


print("-----------------------")



def carp(x,y):
    print(x*y)
carp(3,6)
carp("beykent",3)



print("-----------------------")



def bolum(bolunen,bolen):
    print(bolunen/bolen)
print(bolum(bolen=3,bolunen=12))#degerler atanarak yazıldığı için yerlerin önemi yok.



print("-----------------------")



m=50

def degistir():
    m=80
    return m*2
print(degistir())
print(m)   

def degistir2():
    global m #myi lokalden globele geçirdik ve fonksiyon dışında da m 80 oldu
    m=80
    return m*2
print(degistir2())
print(m)



print("-----------------------")



def topla(a,b):
    return a+b

def ortalama(a,b):
    t=topla(a,b)
    return t/2
print(ortalama(20,30))
print(type(ortalama(20,30)))



print("-----------------------")



def cember(r):
    c=2*3.14*r
    a=3.14*(r**2)
    return c,a
cevre,alan=cember(8)
print("dairenin cevresi",cevre,"dairenin alanı",alan)




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




liste6=[11,33,44,66,788,1]

print(liste6[0:5])#0 dan 6 ya kadar
print(liste6[:3])#0 dan 4 e kadar
print(liste6[2:])#2 den sonuna kadar
print(liste6[-1])#en sondaki eleman
print(liste6[-2])#sondan 2. eleman
print(liste6[-2:])#-2 ve -1 yazılır

#listelerde + ve * operatör kullanımları

liste7=[11,33]
liste8=[1,9]
liste9=liste7+liste8#listeleri birleştirme
print(liste9)

liste10=3*liste9
print(liste10)



print("-------------------")



#liste için fonksiyonlar

#append

liste11=[2,3,4,1,32]
liste11.append(19)#değişkene atanılmaz atanılırsa ğer null none döner çünkü bu bir operasyon yapar..
print(liste11)

#count

ab=liste11.count(4)
print(ab)

#extend

liste12=[99,54]
liste11.extend(liste12)#liste12 nin elelmanlarını liste11 ekler.. değişkene atanılamaz atanırsa null none döner.. çünkü operasyon yapar
print(liste11)

#index

print(liste11.index(4))#listede 4 ün olduğu indexi söyler..

#insert

liste11.insert(1,25)#1. indexe 25 i ekle araya sıkıştırma yöntemi..
print(liste11)

liste11.pop(2)#2. indexteki elemanı siler
print(liste11) 
eleman=liste11.pop()#son elemanı siler
print(liste11)

#remove

liste11.remove(32)#32 değerini çıkarır
print(liste11)

#reverse ters çevirmek

liste11.reverse()
print(liste11)

#sort

liste11.sort()#küçükten büyüğe doğru sıralar...
print(liste11)
sorted(liste11)#böyle yapıldığında liste11 değişmez sadece bu satır için büyükten küçüğe sıralar yani liste11 in durumu değişmez...
print(sorted(liste11))#böyle yapıldığında liste11 değişmez sadece bu satır için büyükten küçüğe sıralar yani liste11 in durumu değişmez..



#iterasyonlar


liste12=[10,23,54,7,0,-21]

for i in liste12:
    print(i)



print("----------------------")



for i in range(1,10):#1 den 10 a kadar yazdırır.
    print(i)



print("----------------------")



for i in range(10):#0 dan 10 a kadar yazar. 9 dahile değil
    print(i)



print("----------------------")



for i in range(1,19,2):#1den başlar 19 akadar 2şer 2şer atlayarak yazar.
    print(i)



print("----------------------")




for i in range(len(liste12)):#range içindeki 6 dır yani 0 dan 6 ya kadar indis elemanlarını verir.
    print(liste12[i])




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



































































































































































































































































































































































