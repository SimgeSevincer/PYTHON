# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 16:48:16 2022

@author: Lab435-Hoca
"""
"""
#PyQt Sinyalleri
#exec halinde kullanıcıdan gelen sinyaller yani fareden tıklama yapmak vb.
#bu sinyaller üzerine uygun fonksiyonlara yönlendirme yapılır.
#sinyallerin bağlandığı fonksiyonlar yuva veya slot olrak adlandırılır.

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def metınGuncelle():
    print("Düğmeye basıldı.")

def metınGuncelle2():
    etiket.setText('<font color = "red",size = "+3">Dugmeye Basın</font>')
    

uyg=QApplication([])
pencere=QWidget()#önce pencere oluştururlur.
etiket=QLabel('<font color = "blue",size = "+3">görsel programlama dersi</font>')#etiket oluşturulur
dugme=QPushButton("TIKLA")#dugme oluştururldu.
dugme.clicked.connect(metınGuncelle2)#düğmeye bir kez tıklandığında bu fonksiyon çalışacak. 
#clicked bir defa basılınca anlamına gelir.
kutu=QVBoxLayout()#taslak oluşturuldu
kutu.addWidget(etiket)
kutu.addWidget(dugme)
#taslak doldururludu.
pencere.setLayout(kutu)
pencere.setWindowTitle("DERS HAKKINDA")#PENCERENİN SOL ÜT KÖŞESİNDEKİ BİLGİLENDİRME YAZISI
pencere.show()
uyg.exec_()
"""
"""
#PyQt SINIFLARI
#sınıf şeklinde yapılırsa daha sistematik daha kontrol edilebilir oluyo

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class guiUygulama(QDialog):
    # QDiolog pencereye ait bütün ögeleri kullanabilir bir sınıftır. pencereyi inheration eder.
     def __init__(self,parent=None):
         super(guiUygulama,self).__init__(parent)
         #gui uygulamasına ait super parent ile başlanır yani parent yok parentı direkt gui yaptık
         self.etiket('<font color = "blue",size = "+3">görsel programlama dersi</font>')
         dugme=QPushButton("Tıklayınız")
         dugme.clicked.connect(self.metınGuncelle2)
         kutu=QVBoxLayout()
         kutu.addWidget(self.etiket)
         kutu.addWidget(dugme)
         self.setLayout(kutu)#pencere yazmamıza gerek yok çünkü QDialog pencerenin tüm ögelerini kullanır inheration eder
         self.setWindowTitle("GP Dersi")
         self.resize(300,400)#300 yatay 400 dikey genişlik. pencerenin boyutu bu şekilde belirlenir
         self.move(200,50)# ilk arguman x e ait köşe 2. arguman ise y ye ait köşedir.
         #ekranın sol üst köşesi 00dır normalde.bunu değiştimek için move kullanılır. ilk arguman x e ait köşe 2. arguman ise y ye ait köşedir.

    def metınGuncelle2(self):
        self.etiket.setText('<font color = "red",size = "+3">Dugmeye Basın</font>')

uyg=QApplication([])
pencere=guiUygulama()
pencere.show()
uyg.exec_()

"""















































































