# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 16:16:48 2022

@author: Lab435-Hoca
"""
"""
#GÖRSEL PROGRAMLAMA
#katman katman düşünülebilir.
#pencere açıcaz ve tasarım yapıcaz. aynı similatörde olduğu gibi
#pencereye bir dizayn açıyoruz ve dizaynı dolduruyoruz.


from PyQt5.QtWidgets import *#KÜTÜPHANE BUNU YAZARAK ALINIR

uyg=QApplication([])#uygulama qapp ile açıldı.

#etiket widgettir ve bunlar birleşir ve tarasarımı oluştururlar.

etiket=QLabel("görsel programlama")
etiket.show()#göstermek için kullanılır.
uyg.exec_()
#EXEC AÇIKLAMASI
#olay döngüsüdür.kullanıcıdan gelen etkilere anında tepki vermek reaksiyon vermek olay döngüsüdür.
#uygulamaya alır.çalıştırır. exece aldığımızda uygulama biz pencereyi kapatmadığımız sürece açık kalır ve çalışır.
#bu döngü sayesinde kullanıcı ile sürekli etkileşim halinde kalınır ve her bir reaksiyonu anında alabilriz.
#event klavye ve fare hareketi bu hareketle birlikte fonskiyonlar yazılır 
 
"""
"""
#Etiketler HTMLden anlar.
#yani etiket=Qlabel(-HTML kodu-)

from PyQt5.QtWidgets import *
etiket=QLabel('<font color = "blue",size = "+3">görsel programlama dersi</font>')
etiket.show()
uyg.exec_()
"""

#PENCERE DÜZENLERİ
#widgetleri pencereye ekleyeceğiz sonra dizaynı pencereye ekle.
#pencere düzenleri boxlarla veya ızgaralarla yapışır. bunlar nasıl tasarım yapacağımıza göre değişir

from PyQt5.QtWidgets import *
uyg=QApplication([])#uyg açıldı
pencere=QWidget()#pencere koyuldu eklendi. 
#taslak yaratılcak ve eklemeler yapılcak onun içerisinde widgetler ekelenecek ve en son pencereye eklenecek.

etiket=QLabel('<font color = "blue",size = "+3">görsel programlama dersi</font>')
dugme=QPushButton('Tıkla')
#pencere oluşturuldu widgetler oluşturuldu sıra taslaklarda
kutu=QVBoxLayout()#taslak oluşturuldu. layout taslak demek.taslaklara ekleme yapmada sıra
kutu.addWidget(etiket)
kutu.addWidget(dugme)
#eklemeler yapıldı. şimdi kutuyu pencereye eklemede sıra
pencere.setLayout(kutu)#kutu penecereye eklenedi
pencere.setWindowTitle("Ders Hakkında")
pencere.show()
uyg.exec_()

#3 bileşen widget etiket(layout) pencere

































