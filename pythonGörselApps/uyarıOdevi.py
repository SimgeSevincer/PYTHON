# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 14:33:40 2023

@author: Simge SEVİNCER
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# Akıllı Diyalog Uyarı Ekranı Örneği




class yaziTipiDiyalog2 (QDialog):
    def __init__(self, parent = None):
        super (yaziTipiDiyalog2,self).__init__(parent)
        self.parent = parent
        self.setAttribute(Qt.WA_DeleteOnClose)
        
        izgara = QGridLayout()
        
        
        izgara.addWidget(QLabel("Yazı Tipi:"), 0,0,1,1) 
        self.yaziTipiListe = QFontComboBox()
        self.yaziTipiListe.setCurrentFont(QFont(self.parent.yaziTipi))
        izgara.addWidget(self.yaziTipiListe,0,1,1,1)   
        
        
        izgara.addWidget(QLabel("Yazı Rengi:"), 1,0,1,1)   
        self.renkKutu = QLineEdit(self.parent.yaziRengi)
        izgara.addWidget(self.renkKutu,1,1,1,1)
        
        
        
        dugmeKutusu = QDialogButtonBox(QDialogButtonBox.Ok|
                                       QDialogButtonBox.Cancel)
        
        dugmeKutusu.button(QDialogButtonBox.Ok).setText("Tamam")
        dugmeKutusu.button(QDialogButtonBox.Cancel).setText("Vazgeç")
    
        
        dugmeKutusu.button(QDialogButtonBox.Ok).clicked.connect(self.kabul)
        dugmeKutusu.button(QDialogButtonBox.Cancel).clicked.connect(self.reject)
        
        izgara.addWidget(dugmeKutusu,2,0,1,2)
        
        self.setLayout(izgara)
        self.setWindowTitle("Yazı Tipi Ayarı")
        self.setWindowIcon (QIcon("icons8-spyder-ide-5-48"))
        
        
        
    def kabul (self): 
        renk = self.renkKutu.text()
        try:
           if not self.renkKontrol(renk):
               raise Exception()
              
        except:
            print("renk hatası alındı")
            QMessageBox.warning(self, "Hatalı Renk", "Renk Kodu Yanlış. Düzeltiniz.")
            self.renkKutu.selectAll()
            self.renkKutu.setFocus()
            return
        self.parent.yaziTipi = self.yaziTipiListe.currentFont().family()
        self.parent.yaziRengi = renk
        self.parent.etiket.setText(self.parent.metin % (self.parent.yaziTipi, self.parent.yaziRengi))
        QDialog.accept(self)

        
        
    def renkKontrol (self, renk):
       if not len(renk)==7 : return False
       if not renk[0] =='#': return False
       for  i in renk[1:]:
           if not i.upper() in 'ABCDEF0123456789': 
               return False            
       return True
            
        
        

class AnaUygulamaAkilliDiyalog(QDialog):
    def __init__(self, parent = None):
        super (AnaUygulamaAkilliDiyalog,self).__init__(parent)
        self.yaziTipi = 'Verdana'
        self.yaziRengi = '#FF0000'
        self.metin = '<font size="+3" face="%s" color="%s"> görsel programlama dersi </font>'
        self.etiket = QLabel(self.metin % (self.yaziTipi, self.yaziRengi))
        
        kutu = QVBoxLayout()
        kutu.addWidget(self.etiket)
        
        yaziTipiDugme = QPushButton("Yazı Tipini ve Rengini Değiştir")
        yaziTipiDugme.clicked.connect(self.yaziTipiDegistir)
        kutu.addWidget(yaziTipiDugme)
        self.setLayout(kutu)
        
        self.setWindowTitle("Ana Uygulama")
        self.setWindowIcon (QIcon("icons8-python-50"))
        
        
    def yaziTipiDegistir(self):
        diyalog = yaziTipiDiyalog2(self)
        diyalog.exec_()




uyg = QApplication([])
pencere = AnaUygulamaAkilliDiyalog()
pencere.show()
uyg.exec_() 