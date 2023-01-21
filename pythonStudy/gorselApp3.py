# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 17:44:33 2022

@author: Lab435-Hoca
"""

#IZGARA 
#addWidget(parçacık,satır,sutün,satır genişliği,sutün genişliği)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class guiUygulama2(QDialog):
    # QDiolog pencereye ait bütün ögeleri kullanabilir bir sınıftır. pencereyi inheration eder.
    def __init__(self,parent=None):
        super(guiUygulama2,self).__init__(parent)
        self.boy=3
        self.metin='<center><font color = "blue",size = "+%d">görsel programlama dersi</font></center>'
        #center ortalamak için %d ise bastıkça metinin büyümesi için kullanıldı.
        self.etiket=QLabel(self.metin % self.boy)
         #%d deki dnin yerine self.boy kullanıldı.
        dugmeKucult=QPushButton("Metni Kucult")
        dugmeKucult.clicked.connect(self.metinKucult)
        dugmeBuyut=QPushButton("Metni Buyut")
        dugmeKucult.clicked.connect(self.metinBuyut)
        izgara=QGridLayout()
        izgara.addWidget(self.etiket,0,0,1,2)
         #0. satır 0. sutündan başla (yani sol en üst noktadan başla) ve 1 satır yer kapla 2 sutün yer kapla demek
        izgara.addWidget(dugmeKucult,1,0,1,1)
         #1,0 karteyeninden başla 1 sattır ve 1 sutütnlük yer kapla.
        izgara.addWidget(dugmeBuyut,1,1,1,1)
        self.setLayout(izgara)
        self.setWindowTitle("Pyqt Izgarası")
        self.resize(500,100)
         
    def metinBuyut(self):
        if self.boy<=4:
            self.boy=self.boy+1
            self.etiket.setText(self.metin % self.boy)
    
    def metinKucult(self):
        if self.boy<=4:
            self.boy=self.boy-1
            self.etiket.setText(self.metin % self.boy)
            

uyg=QApplication([])
pencere=guiUygulama2()
pencere.show()
uyg.exec_()         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        