# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 16:19:58 2022

@author: umitozturk
"""

# Daha önce görülen parçacıklar: etiket (QLabel) ve bastırılabilir düğme (QPushButton): 

# Döner kutu ve Açılır Liste (yüklenen DonerKutuAcilirListe jpgsine bakarak kodu anlayınız):
#Döner Kutu: QSpinBox ve Açılır Liste: QComboBox. 
#Aşağıdaki örneği inceleyiniz.   
    
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class guiUygulama3 (QDialog):
    def __init__(self, parent=None):
        super(guiUygulama3,self).__init__(parent)
        self.boy = 2
        self.yt = {0:'Arial', 1:'Times New Roman', 2:'Verdana', 3:'Comic Sans MS'}
        self.yaziTipi = self.yt[0]
        self.metin = '<center><font color ="blue" size ="+%d" face="%s"> görsel programlama dersi</font></center>'
        self.etiket = QLabel(self.metin % (self.boy, self.yaziTipi))
        izgara = QGridLayout()
        izgara.addWidget(self.etiket, 0, 0, 1, 2)
        izgara.addWidget(QLabel('Yazı Boyu: '), 1,0,1,1)
        donerKutu = QSpinBox()
        donerKutu.setRange(1, 4)
        donerKutu.setValue(self.boy)
        donerKutu.valueChanged.connect(self.metinBoyuDegistir)
        izgara.addWidget(donerKutu,1,1,1,1)
        izgara.addWidget(QLabel('Yazı Tipi: '), 2,0,1,1)
        acilirListe = QComboBox()
        acilirListe.addItem('Arial')
        acilirListe.addItem('Times New Roman')
        acilirListe.addItem('Verdana')
        acilirListe.addItem('Comic Sans MS')
        listeMetinIndisi = acilirListe.findText(self.yaziTipi)
        acilirListe.setCurrentIndex(listeMetinIndisi)
        acilirListe.activated.connect(self.yaziTipiDegistir)  #.connect(self.yazıTipiDegistir) #.connect   #.connect(self.yazıTipiDegistir)
        izgara.addWidget(acilirListe, 2,1,1,1)
        self.setLayout(izgara)
        self.setWindowTitle("Metin Formatı")
        self.resize(500,150)
        
        
    
    def metinBoyuDegistir (self, boy):
        self.boy = boy 
        self.etiket.setText(self.metin % (self.boy, self.yaziTipi))
                           
    def yaziTipiDegistir (self, tip):
        self.yaziTipi = self.yt[tip]
        self.etiket.setText(self.metin % (self.boy,self.yaziTipi))
        
                
                      
uyg = QApplication([])
pencere = guiUygulama3()  
pencere.show()
uyg.exec_()     
        



"""
    
# Uygulama örneği: Uygulamadan yakıt hesaplama görevi istenmektedir.
# Yüklenilen yakıt hesaplayıcısı gui jpg dosyasına bakarak yazılması gereken
# PyQt GUI kodu aşağıda verilmiştir:


class yakitHesaplayicisi (QDialog):
    def __init__(self, parent=None):
        super(yakitHesaplayicisi,self).__init__(parent)
        # ızgarayı oluştur:
        izgara = QGridLayout()
        # widgetları tek tek ekle (gui jpgsindeki tasarıma göre)
        izgara.addWidget(QLabel ('Gideceğiniz Yol (km):'),0,0,1,1)
        self.gidilenYol = QLineEdit() # QlineEdit metin kutusu oluşturur
        self.gidilenYol.setInputMask('0000000000') # text giriş formatını netleştirir.
        izgara.addWidget(self.gidilenYol,0,1,1,1)
        
        izgara.addWidget(QLabel ('Yakıtın Litre Fiyatı:'),1,0,1,1)
        self.yakitFiyati = QLineEdit() # QlineEdit edit edilebilir metin kutusu oluşturur
        self.yakitFiyati.setInputMask('00.00') # text giriş formatını netleştirir.
        izgara.addWidget(self.yakitFiyati,1,1,1,1)
        
        izgara.addWidget(QLabel ("100km'de Tüketilen Yakıt:" ),2,0,1,1)
        self.yakitTuketimi = QLineEdit() # QlineEdit edit edilebilir metin kutusu oluşturur
        self.yakitTuketimi.setInputMask('0.0') # text giriş formatını netleştirir.
        izgara.addWidget(self.yakitTuketimi,2,1,1,1)
        
        
        izgara.addWidget(QLabel ("Toplam Tutar:" ),3,0,1,1)
        self.tutar = (QLabel('<i> KM Giriniz</i>')) 
        izgara.addWidget(self.tutar,3,1,1,1)
        
        
        self.hesaplaDugmesi = QPushButton("Hesapla")
        self.hesaplaDugmesi.clicked.connect(self.yakitHesapla)
        izgara.addWidget(self.hesaplaDugmesi,4,0,1,2)
        
        
        self.setLayout(izgara)
        self.setWindowTitle('Yakıt Hesaplayıcısı')
        
        
    def yakitHesapla (self):
        yol = 0
        try: yol = int(self.gidilenYol.text())
        except: pass
    
        fiyat = 0
        try: fiyat = float(self.yakitFiyati.text())
        except: pass
    
        tuketim = 0
        try: tuketim = float(self.yakitTuketimi.text())
        except: pass
    
    
        if not yol :
            self.tutar.setText('<font color ="red"><i> KM giriniz</i></font>')
            self.gidilenYol.setFocus()    
        elif not fiyat:
            self.tutar.setText('<font color ="red"><i> Fiyat Giriniz</i></font>')
            self.yakitFiyati.setFocus()
        elif not tuketim:
            self.tutar.setText('<font color ="red"><i> Tuketim Giriniz</i></font>')
            self.yakitTuketimi.setFocus()
            
        else: 
            tutar = fiyat*((yol*tuketim)/100)
            self.tutar.setText('<font color ="black"><b>%0.2f</b></font>' % tutar)
            
            
    
uyg = QApplication([]) 
pencere = yakitHesaplayicisi()   
pencere.show()
uyg.exec_()

 
    
"""




    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     
    
    
    