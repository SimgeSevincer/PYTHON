# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

#akılsız app yapalım
#ana pencreyi dizayn edelim
class yaziTipiDiyalog(QDialog):
    def __init__(self,parent=None):
        super(yaziTipiDiyalog,self).__init__(parent)
        izgara=QGridLayout()
        #diyalog pencersini oluşturalım
        izgara.addWidget(QLabel("Yazı Tipi:"),0,0,1,1)
        self.yaziTipiListe=QComboBox()#pencereyi seçeneklendiriyor.
        self.yaziTipiListe.addItems(('Arial','Times New Roman','Verdana','Comic Sans MS'))
        self.yaziTipiListe.setCurrentIndex(2)#ilkte verdana çıkacak anlamına gelir.
        izgara.addWidget(self.yaziTipiListe,0,1,1,1)
        
        kabulDugme=QPushButton("Tamam")
        iptalDugme=QPushButton("İptal")
        
        dugmeKutusu=QHBoxLayout()
        dugmeKutusu.addWidget(kabulDugme)
        dugmeKutusu.addWidget(iptalDugme)
        
        izgara.addLayout(dugmeKutusu,1,0,1,2)#1 satır 2 sutün
        
        kabulDugme.clicked.connect(self.accept)#exec 1
        kabulDugme.clicked.connect(self.reject)#exec 0
        
        self.setLayout(izgara)
        self.resize(300,100)
        self.setWindowTitle("Yazı Tipi Ayarı")
        #self.setWindowIcon(QIcon("resim linki")) yazı tipi ayarının yanındaki icon
        
#ana uygulamayı dizayn edelim
class AnaUygulamaAkilsizDiyalog(QDialog):
    def __init__(self,parent=None):
        super(AnaUygulamaAkilsizDiyalog,self).__init__(parent)
        self.yaziTipi='Verdana'
        self.metin='<font color ="black" size ="+3" face="%s"> görsel programlama dersi</font>'
        self.etiket=QLabel(self.metin % self.yaziTipi)
        
        kutu=QVBoxLayout()
        kutu.addWidget(self.etiket)
        yaziTipiDugme=QPushButton("Yazi Tipini Degistir")
        yaziTipiDugme.clicked.connect(self.yaziTipiDegistir)
        kutu.addWidget(yaziTipiDugme)
        self.setLayout(kutu)
        
        self.setWindowTitle("Ana Uygulama")
    
    def yaziTipiDegistir(self):
        diyalog=yaziTipiDiyalog()
        if diyalog.exec_():#exec değeri 1 olursa 
            self.yaziTipi=diyalog.yaziTipiListe.currentText()
            self.etiket.setText(self.metin % self.yaziTipi)#etiketi yazı tipiyle güncelleyip metini set ediyoruz.
            
            
uyg = QApplication([]) 
pencere = AnaUygulamaAkilsizDiyalog()   
pencere.show()
uyg.exec_()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      
        