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





































