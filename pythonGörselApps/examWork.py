# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 17:07:44 2022

@author: Simge SEVİNCER
"""

print("simge")
print(3.14)
print(2)
print(type("simge"))
print(type('s'))
print(type(2))
print(type(2.14))
#print("simgenin yaşı"+21) hata verir çünkü farklı tipteki değişkenler toplanamaz.
yas=21
print("simgenin yaşı",yas)
yas="21"
print("simgenin yaşı"+yas)#+ operatörü boşluk bırakmadan yazdırır.
import keyword#keyword modulunu kullanmak için import kullanılır. modul kullanak için import kullanılır.
print(keyword.kwlist)

def abc():
    print("abc fonskiyonu içindesiniz..")
#print(abc()) fonksiyon çıktısı ile beraber None çıktısı da alınır.
abc()

def abc(x):
    print("x değeri",x)
abc(10)
print(abc)#abc fonksiyonu belleğin neresinde konumlandı bilgisini çıktı olarak yazar.

def abc(x):
    t=x+5
    return t
print(abc(10))
print(2*2+abc(2*3))

#yerel değişkenler yani sadece fon içinde tanımlanmış ve döndürülmemiş şeyler fonk dışında tanımlı değildir.

def bölme(bölünen,bölen):
    return(bölünen/bölen)

print(bölme(bölen=3,bölünen=16))
print(bölme(16,4))

m = 50

def degistir ():
    #global m  # bu kod satırı m değişkenini global yapmaktadır. Bu kod satırını
    # açarak tekrar çalıştırdığınızda daha üst seviyeden tanımlı m, 80 olacaktır. 
    m = 80
    return (m*2)

t = degistir()
print(t)
print(m)

def topla(x,y):
    return x+y
def ort (x,y):
    ort=topla(x,y)/2
    return ort
print(ort(5,9))

def çember(r):
    alan=3*r**2
    çevre=2*3*r
    return alan,çevre
alan,çevre=çember(4)
print(alan,çevre)

print(0 and 9)

x=22
if(x%2==0):
    print("x={} ifadesi çifttir".format(x))
else:
    print("x={} ifadesi tektir".format(x))
    

gün="cumartesi"

if(gün=="pazartesi"):
    print("bugün pazartesi")
elif(gün=="salı"):
    print("bugün salı")
elif(gün=="çarşamba"):
    print("bugün çarşamba")
elif(gün=="perşembe"):
    print("bugün perşembe")
elif(gün=="cuma"):
    print("bugün cuma")
else:
    print("bugün haftasonu")


#if elif else te koşul sağlandığı an çıktı verip komuttan çıkar.



sayac=0

while sayac<10:
    sayac+=1
    if(sayac==5):
        break
    print(sayac)

print("------")
sayac=0

while(sayac <10):
    sayac+=2
    if(sayac==6):
        continue
    print(sayac)

print("------------------")
liste=[]#farklı tipteki değişkenleri tutabilir.
print(type(liste))

print(abc)

liste=["simge",21,1.8]
print(liste)
liste2=list(["abc","abcd"])
print(liste2)
liste3=list("abc")#listenin elelmanları stringin harfleri olur çünkü abc yi [] içine koymadık...
print(liste3)
liste4=[1,2,3]
print(liste[0])
print(len(liste3))

print(2 in liste3)
print(max(liste3))
print(sum(liste4))


liste5=[12,13,14,15,16]
print(liste5[-3])

liste6=liste5+liste4
print(liste6)
liste7=liste4*3
print(liste7)
print(liste5[-2:])


def harfBul(cümle,harf):
    i=0
    while(i<len(cümle)):
        if(cümle[i]==harf):
            return i
        i+=1
    return -1
print(harfBul("simge sevincer","r"))
    
yer="simge sevincer"
#yer[2]="a"#hata verir.


ogrenciler=[["simge sevincer","2015"],
            ["ufuk sevincer","1936"],
            ["mertcan alkan","1828"]]


for i in ogrenciler:
    print(i[0],"\t",i[1]) #yapısal yazdırma olarak geçer..


ders_saati="18.00"

print("Ders saatimiz saat %sdadır."%ders_saati)
mevcut=40
print("sınıf %d kişi kadardır ve %s de dersimiz vardır."%(mevcut,ders_saati))

print("sınıf {} kişi kadardır ve {} de dersimiz vardır.".format(mevcut,ders_saati))


liste=[40,"18.00"]

print("sınıf {} kişi kadardır ve {} de dersimiz vardır.".format(*liste))

isim="simge sevincer"

print(isim.upper())
print(isim.title())


cümle="bugün python dersimiz var."

"""def kelimeBul(cümle,kelime):
    for i in """


print("inebolu".endswith("bolu"))
print("Çanakkale".startswith("çan"))

isim="simgesevincer@gmail.com"
(ad,domain)=isim.split("@")
print(ad,domain)

isim2="@".join(["simgesevincer","gmail.com"])
print(isim2)



def abc5(k):
    l = 3
    return l+k


t = abc5(5)
print (t)

liste=list("python")
print(liste[0])




ogrenciler = [["ali", "öztürk", "12345678"],
              ["mehmet", "yılmaz", "87654321"],
              ["ayşe", "ertekin", "12345677"]]

# yazdırma işlemi:
# yapısal değil:
for o in ogrenciler:
    print(o[0], o[1], o[2])

print("-------------------------------------")

#yapısal çıktı:
for o in ogrenciler:
    print(o[0], '\t', o[1], '\t', o[2])



    







