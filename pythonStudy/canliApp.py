# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class yaziTipiDiyalog3 (QDialog):
    #burası ikinci açılan işlemlerin yapılduğı pencere
    def __init__(self, parent=None):
        super(yaziTipiDiyalog3,self).__init__(parent)
        self.parent=parent
        
        izgara=QGridLayout()
        izgara.addWidget(QLabel('Yazı Tipi:'),0,0,1,1)
        
        self.yaziTipiListe=QFontComboBox()
        simdikiYaziTipi=self.parent.metin.currentFont()
        self.yaziTipiListe.setCurrentFont(simdikiYaziTipi)
        self.yaziTipiListe.activated.connect(self.yaziTipiDegistir)#tamam demeden doğrudan değişikliği uygulamak için yazıldı.
        izgara.addWidget(self.yaziTipiListe,0,1,1,1)
        
        kapatDugmesi=QPushButton("Kapat")
        kapatDugmesi.clicked.connect(self.accept)#hem kapatmayı hem de kabul etmeyi aynı anda sağlayacak
        izgara.addWidget(kapatDugmesi,1,0,1,2)#tek satır iki sutün kaplasın dedik
        
        self.setLayout(izgara)
        self.setWindowTitle('Yazı Tipini Ayarla')
        
    
    def yaziTipiDegistir(self):
        yaziTipi=self.yaziTipiListe.currentFont()
        self.parent.metin.setCurrentFont(yaziTipi)
        
        
class AnaUygulamaCanliDiyalog(QDialog):
    # burası ilk açılan ana pencere
    def __init__(self, parent=None):
        super(AnaUygulamaCanliDiyalog,self).__init__(parent)
        self.yaziTipiDiyalogNesnesi=None
        
        self.metin=QTextEdit()#metni kendimiz yazıcaz bu fonskiyon ona yarıyor
        
        kutu=QVBoxLayout()
        kutu.addWidget(self.metin)
        
        yaziTipiDugme=QPushButton("Yazı Tipi Değiştir:")
        yaziTipiDugme.clicked.connect(self.yaziTipiDegistir)
        kutu.addWidget(yaziTipiDugme)
        
        self.setLayout(kutu)
        self.setWindowTitle('Ana Uygulama')
        
    def yaziTipiDegistir(self):
        if self.yaziTipiDiyalogNesnesi is None:
            self.yaziTipiDiyalogNesnesi=yaziTipiDiyalog3(self)
            
            self.yaziTipiDiyalogNesnesi.show()
            self.yaziTipiDiyalogNesnesi.raise_()
            self.yaziTipiDiyalogNesnesi.activateWindow()
            #yukarıdaki 3 kod exec yerine geçiyor
            
            
    def closeEvent(self,olay):
        if self.yaziTipiDiyalogNesnesi:
            self.yaziTipiDiyalogNesnesi.close()
        
        
        
uyg = QApplication([]) 
pencere = AnaUygulamaCanliDiyalog() 
pencere.show()
uyg.exec_()           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    