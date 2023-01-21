# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 08:02:54 2022

@author: umitozturk
"""


# KATARLAR İŞLEMLERİ (String işlemleri), DOSYA İŞLEMLERİ,


# KATARLAR
# Katarlarda her karakter ayrı eleman olmak üzere
# bir liste şeklinde ele alınır.

yer = "Beykent Üniversitesi"

print(yer[3])
print(yer[-2])
print(yer[-2:])  # output:  si
print(yer[:-2])  # output: Beykent Üniversite

print("-------------------------------------")

# Fakat liste değişim operasyonları katarlara uygulanamaz.
# Aşağıdaki işlem hata verecektir:

# yer[2] = "a"

# Bir cümlenin kaç karakterden oluştuğu bilgisi:
print(len(yer))
print("-------------------------------------")
# katarlar üzerinde iterasyon işlemi önceden gösterildiği şekilde
# yapılabilir:

for i in yer:
    print(i)

print("-------------------------------------")


# Bir harfin cümle içerisinde bulunup bulunmadığını araştıran işlev:

def harfBul(cümle, harf):
    i = 0
    while (i < len(cümle)):
        if cümle[i] == harf:
            return i
        i = i+1
    return -1


a = harfBul("ayazağa yerleşkesi", "ğ")

print(a)


print("-------------------------------------")


# Cümle atamaları çift yada tek tırnakla yapılabilir:

yer2 = "Ayazağa Yerleşkesi"  # yada
yer2 = 'Hadımköy Yerleşkesi'

# aşağıdaki gibi yazılırsa hata verecektir.
#yer2 = 'Sınav için Taksim'e gittim'
# Bu gibi durumlarda kaçış karakteri (escape sequence) kullanmalısınız.
# karışıklık yaratan karakterin soluna "\" işareti konulur.

yer2 = 'Sınav için Taksim\'e gittim'
cevap = "\"Yarın burada olacağım\" demişti."

print(yer2)
print(cevap)

print("-------------------------------------")

# satır sonu karakteri (\n)
print("Bir saat anlattım bir tek buseni,\nDoktorlar efsane sandılar seni.")
print("-------------------------------------")


# sekme karakteri (tab) (\t)

# içiçe liste örneği:

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

print("-------------------------------------")


# cümle biçimleme:

ders_saati = "16.00"
print("Dersim saat %s'da başlıyor" % ders_saati)

mevcut = 80

print("sınıf mevcudu toplam %d kişiden oluşmaktadır." % mevcut)

print("-------------------------------------")

# aynı örnek float veri tipi için %f kullanılarak yapılabilmektedir.


#birleşik örnek:

print("sınıf mevcudu %d kişi olan GP dersi saat %s itibari ile başlamaktadır." %
      (mevcut, ders_saati))

print("-------------------------------------")


# Cümle Özellikleri ile ilgili fonksiyonlar:

print("sınıf mevcudu {0} olan GP dersi saat {1} itibari ile başlamaktadır".format(
    mevcut, ders_saati))

liste = [60, "13.00"]

print(
    "sınıf mevcudu {0} olan GP dersi saat {1} itibari ile başlamaktadır".format(*liste))


# Cümle harflerinde küçüklük/Büyüklük Durumu:

print("-------------------------------------")

print(yer)

print(yer.upper())  # tamamı büyük harf
print(yer.lower())  # tamamı küçük harf
print(yer.title())  # Kelimelerin ilk harfleri büyük


# Cümle içerisinde arama:

# bir kelimenin cümle içerisinde olup olmadığını var ise hangi konumdan başladığını
# dönen bir fonksiyon:

def kelimeBul(cümle, kelime):
    for i in range(len(cümle)-len(kelime)+1):
        if cümle[i:i+len(kelime)] == kelime:
            return i
    return -1


#Flashback:
print(liste[0:5])  # hata vermez
# print (liste [5]) # hata verir

print("--------------------------------------------")

b = kelimeBul("Beykent Üniversitesi Ayazağa Yerleşkesi", "Yerleşkesi")

print(b)


print("-------------------------------------")

# Bir stringin başka bir string içinde olup olmadığı bilgisi
# in anahtar kelimesi ile aşağıdaki gibi alınabilir.
# Fakat bu şekilde cümlede başlangıç yeri dönmez.

print("Ayazağa" in "Beykent Üniversitesi Ayazağa Yerleşkesi")
print("Hadımköy" in "Beykent Üniversitesi Ayazağa Yerleşkesi")

# find tarafından aranılan string bulunamaz ise -1 döner:
print("Beykent Üniversitesi Ayazağa Yerleşkesi".find("Hadımköy"))

print("-------------------------------------")


bölgeler = ["Bolu", "Manavgat", "Edirne", "Van",
            "Alanya", "İnebolu", "Samsun", "Nevşehir"]

# bölgeler listesinde bolu geçen yerleşim yerlerini bulan fonksiyon:

for b in bölgeler:
    b = b.lower()
    if b.find("bolu") > -1:
        print(b)
print("-------------------------------------")
# başlangıç ve bitiş sorgulama:

print("inebolu".endswith("bolu"))
print("Çanakkale".startswith("çan"))


print("-------------------------------------")

# cümle parçalama

splitted = "Beykent Üniversitesi Ayazağa Yerleşkesi".split()

print(splitted)


print("-------------------------------------")

info = "Beykent:Mühendislik ve Mimarlık Fak.:Bilgisayar Müh.:Görsel Programlama"
print(info.split(":"))
print("-------------------------------------")


# e posta örneği:
# kullanıcı adını görüntülemek istiyoruz:

email = "mehmet.yilmaz@hotmail.com"

[user_name, domain] = email.split("@")

print(user_name)

#yada:

user_name2 = email.split("@")[0]

print(user_name2)


# liste birleştirme :
# split fonksiyonunun tersi gibi olacaktır:

mail_addr = '@'.join(["m.yilmaz", "gmail.com"])

print(mail_addr)

print("-------------------------------------")

# Bir katarın herhangi bir alt katarını başka bir katar ile değiştirme

yer3 = "tıp fakültesi beylikdüzü yerleşkesi"

print(yer3.replace(' ', '_'))

print("-------------------------------------")

# stringte başta ve sondaki boşlukların (white space) kaldırılması:

print("    beykent üniversitesi ".strip())


print("-------------------------------------")
# stringin yalnızca sayılardan oluşup oluşmadığının kontrolü:

fiyat1 = "120"
fiyat2 = "120.50"
print(fiyat1.isnumeric())  # True
print(fiyat2.isnumeric())  # False: string nokta içerdiği için bozmuştur
print("-------------------------------------")
# ÖDEV !!! Bu noktada sayı Float ise nasıl düşünmeliyiz ???

# Dosya İşlemleri:

F = open("ornek.txt", encoding="utf-8")

# dosyadan bir satır oku:

bilgi = F.readline()

print(bilgi)

# daha sonraki her readline dosya sona erene kadar bir sonraki satırı okur.

bilgi = F.readline()

print(bilgi)

print("-------------------------------------")
# Herhangi bir anda dosyayı baştan yada istenilen başka bir konumdan itibaren okumak için
# seek kullanılır:
print("-------------------------------------")
print(F.seek(0))  # başa ayarlanır
print("-------------------------------------")
print(F.readline())  # yazılır
print("-------------------------------------")
# dosya ile işiniz bittiği anda
# olası hataların önüne geçmek için bu dosyayı kapatmalısınız:

F.close()

# dosya tamamen okunarak tek cümle gibi başka bir değişkene atanabilir:

s = open("ornek.txt", encoding="utf-8").read()

print(s)

print(type(s))

print("-------------------------------------")
# iterasyon ile satır satır okumak:

F = open("ornek.txt", encoding="utf-8")

for l in F:
    print(l.strip())

print("-------------------------------------")
# Dosyanın tüm içeriğini bir listeye koymak için:

F = open("ornek.txt", encoding="utf-8")

l = F.readlines()


print(l[2])
print("------------------------------------")

# Dosyalara yazmak:

# dosyanın ne şekilde açılacağı open fonksiyonuna
# argüman olarak geçebilmektedir.
# argüman verilmezse salt metin salt okunur olarak açılır.
# argümanlar şu şekildedir:

# r : salt okuma
# w : yazma kipi
# a : sonuna ekleme kipi
# b : ikili (binary kipi)
# t : salt metin kipi
# + : hem okuma hem yazma kipi

F = open("ornek.txt", encoding="utf-8", mode="a")

F.write("\n")
F.write("yeni satır eklenmiştir\n")
F.write("yeni satır tekrar eklenmiştir\n")

F.flush()  # flush fonksiyonu çalıştırılmadan değişiklikler dosyaya yansımaz.
# yazma modunda açılan dosya için flush otomatik gerçekleşir.

F.close()

# Eğer dosya w ile açılırsa her açılışta dosya tamamen sıfırlanacaktır.
# Yani tamamı silinmiş olacaktır.

F = open("ogrenciler.txt", encoding="utf-8", mode="w")


for o in ogrenciler:
    for i in o:
        F.write(i+':')
    F.write('\n')

F.close()
# dosyaya yazılacak veri mutlaka string tipinde olmalıdır.
# aksi durumda str() içerisinde kullanılarak tip dönüşümüne gidilmelidir.

# yukarıdaki kod ile belli formatta ogrenciler dosyasına belli formatta
# veri atılmıştır.

# formatlı dosyadan tekrar listeye dönmek için:
F = open("ogrenciler.txt", encoding="utf-8")
ogr_listesi = []

for l in F:
    ls = l.strip()
    ll = ls.split(":")
    ogr_listesi.append([ll[0], ll[1], ll[2]])

print(ogr_listesi)
