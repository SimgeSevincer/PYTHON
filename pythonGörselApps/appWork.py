# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:16:29 2023

@author: Simge SEVİNCER
"""
"""

from PyQt5.QtWidgets import *  

uyg=QApplication([])
etiket=QLabel('<font color="purple",size="+18">MERTCAN SEVİNCER</font>')
etiket.show()
uyg.exec_()

"""
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def metinguncelle():
    etiket.setText('<font color="blue",size="+3">DERS BİTTİ</font>')



uyg=QApplication([])
pencere=QWidget()
etiket=QLabel('<font color="red",size=+3>GÖRSEL APP</font>')
dugme=QPushButton("Tıklayınız")
dugme.clicked.connect(metinguncelle)
kutu=QVBoxLayout()
kutu.addWidget(etiket)
kutu.addWidget(dugme)
pencere.setLayout(kutu)
pencere.setWindowTitle("DERS HAKKINDA")
pencere.show()
uyg.exec_()

"""
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class guiUygulama(QDialog):
    def __init__(self,parent=None):
        super(guiUygulama,self).__init__(parent)
        self.etiket=QLabel('<font color="red",size="+5">ben bir appim</font>')
        dugme=QPushButton("tıkla bana ulan")
        dugme.clicked.connect(self.etiketGuncelle)
        kutu=QVBoxLayout()
        kutu.addWidget(self.etiket)
        kutu.addWidget(dugme)
        self.setLayout(kutu)
        self.setWindowTitle("HARİKA APP")
        self.resize(300,400)
        self.move(200,50)
        
    def etiketGuncelle(self):
        self.etiket.setText('<font color="blue",size="+5">dugmeye bastın gız</font>')

uyg=QApplication([])
pencere=guiUygulama()
pencere.show()
uyg.exec_()
"""

"""
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*

class guiUygulama(QDialog):
    def __init__(self,parent=None):
        super(guiUygulama,self).__init__(parent)
        self.boy=2
        self.yaziTipleri={0:'Arial', 1:'Times New Roman', 2:'Verdana', 3:'Comic Sans MS'}
        self.yaziTipi=self.yaziTipleri[0]
        self.metin='<center><font color="blue" size=+%d face=%s>"Görsel Programlama Dersi</font></center>'
        self.etiket=QLabel(self.metin % (self.boy,self.yaziTipi))
        izgara=QGridLayout()
        izgara.addWidget(self.etiket,0,0,1,2)
        izgara.addWidget(QLabel("Yazı Boyutu:"),1,0,1,1)
        izgara.addWidget(QLabel("Yazı Tipi:"),2,0,1,1)
        donerKutu=QSpinBox()
        donerKutu.setRange(1,4)
        donerKutu.setValue(self.boy)
        donerKutu.valueChanged.connect(self.boyDegistir)
        izgara.addWidget(donerKutu,1,1,1,1)
        acilirListe=QComboBox()
        acilirListe.addItems(('Arial','Times New Roman', 'Verdana', 'Comic Sans MS'))
        acilirListe.setCurrentIndex(acilirListe.findText(self.yaziTipi))
        acilirListe.activated.connect(self.yaziTipiDegistir)
        izgara.addWidget(acilirListe,2,1,1,1)
        self.setLayout(izgara)
        self.setWindowTitle("Metin Düzenleme")
        self.resize(500,150)
        
        
    def boyDegistir(self,boy):
        self.boy=boy
        self.etiket.setText(self.metin %(self.boy,self.yaziTipi))
        
    def yaziTipiDegistir(self,index):
        self.yaziTipi=self.yaziTipleri[index]
        self.etiket.setText(self.metin % (self.boy,self.yaziTipi))

uyg=QApplication([])
pencere=guiUygulama()
pencere.show()
uyg.exec_()

"""
        
"""
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*

class yakitHesaplamaApp(QDialog):
    def __init__(self,parent=None):
        super(yakitHesaplamaApp,self).__init__(parent)
        izgara=QGridLayout()
        izgara.addWidget()
     
"""     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        















































