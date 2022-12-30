# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 17:05:05 2022

@author: Lab435-Hoca
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class yaziTipiDiyalog2(QDialog):
     def __init__(self,parent=None):
        super(yaziTipiDiyalog2,self).__init__(parent)
        self.parent=parent#bunu yazmamızın nedeni aprent dediğimiz yer ana uygulama kısmı olucak ve uygulamaya parent üzerinden ulaşıcaz.
        self.setAttribute(Qt.WA_DeleteOnClose)#kapattıktan sonra hafızadan sil
        izgara=QGridLayout()#izgara oluşturduk
        izgara.addWidget(QLabel("Yazı Tipi"),0,0,1,1)
        
        self.yaziTipiListe=QFontComboBox()#yazı fontları otomatik olarak çıkarılır.
        self.yaziTipiListe.setCurrentFont(QFont(self.parent.yaziTipi))
        izgara.addWidget(self.yaziTipiListe,0,0,1,1)#yazı tipi yazısının yanına listeyi ekledik
        
        dugmeKutusu=QDialogButtonBox(QDialogButtonBox.Ok| 
                                     QDialogButtonBox.Apply|
                                     QDialogButtonBox.Reset|
                                     QDialogButtonBox.Cansel)
        
        dugmeKutusu.button(QDialogButtonBox.Ok).setText("Tamam")
        dugmeKutusu.button(QDialogButtonBox.Cansel).setText("Vazgeç")
        dugmeKutusu.button(QDialogButtonBox.Apply).setText("Uygula")
        dugmeKutusu.button(QDialogButtonBox.Reset).setText("Sıfırla")
        
        dugmeKutusu.button(QDialogButtonBox.Ok).clicked.connect(self.kabul)
        dugmeKutusu.button(QDialogButtonBox.Cansel).clicked.connect(self.iptal)
        dugmeKutusu.button(QDialogButtonBox.Apply).clicked.connect(self.uygula)
        dugmeKutusu.button(QDialogButtonBox.Reset).clicked.connect(self.sifirla)
        
        izgara.addWidget(dugmeKutusu,1,0,1,2)
        
        self.setLayout(izgara)#pencereyi ızgaraya ekledik yani görünür oldu
        self.setWindowTitle("Yazı Tipi Ayarı")
        
        #akılsız uygulamada yaptığımız ana uygulamada yapılan işlemler bu class içinde yapılacak
        
     def kabul(self):
        self.parent.yaziTipi=self.yaziTipiListe.currentFont().family()#yazi tipi listeyi değiştirir
        self.parent.etiket.setText(self.parent.metin % self.parent.yaziTipi)#etikete uygulanır
        QDialog.accept(self)#onayladık
     
     def uygula(self):
        self.parent.etiket.setText(self.parent.metin % self.yaziTipiListe.currentFont().family())
        
     def sifirla(self):
         self.parent.etiket.setText(self.parent.metin % self.parent.yaziTipi)
         self.yaziTipiListe.setCurrentFont(QFont(self.parent.yaziTipi))
         
     def iptal(self):
        self.parent.etiket.setText(self.parent.metin % self.parent.yaziTipi)
        QDialog.reject(self)
        

class AnaUygulamaAkilliDiyalog(QDialog):
     def __init__(self,parent=None):
        super(AnaUygulamaAkilliDiyalog,self).__init__(parent)
        self.yaziTipi='Verdana'
        self.metin='<font color ="black" size ="+3" face="%s"> görsel programlama dersi</font>'
        self.etiket=QLabel(self.metin % self.yaziTipi)
        
        kutu=QVBoxLayout()#kutu açtık
        kutu.addWidget(self.etiket)#etiket eklemesi yaptık
        
        yaziTipiDugme=QPushButton("Yazı Tipini Degistir")
        yaziTipiDugme.clicked.connect(self.yaziTipiDegistir())
        kutu.addWidget(yaziTipiDugme)#kutuya dugmeyi ekledik
        self.setLayout(kutu)#kutuyu pencereye ekledik.
        
        self.setWindowTitle("Ana Uygulama")
        
     def yaziTipiDegistir(self):
        diyalog=yaziTipiDiyalog2(self)#parent tanındı
        diyalog.exec_()
                
        
uyg = QApplication([]) 
pencere = AnaUygulamaAkilliDiyalog()   
pencere.show()
uyg.exec_()
               
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        