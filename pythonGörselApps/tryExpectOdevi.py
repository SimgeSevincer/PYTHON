# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 10:38:35 2023

@author: Simge SEVİNCER
"""

class listeHatası(Exception):
    def __init__(self,hata):
        self.hata=hata
    def __str__(self):
        return self.hata

def hataCiktisi(x):
    if not ((type(x) is tuple or list) or len(x)==2):
        raise listeHatası("ikişer öğeli liste yada tüp olmalıdır")
    return x



l2 = [[1,5],(23,4),(8,8),3,(2,6),(5,3),[11,9],[8,10,2]] 

try:
    for x in l2:
        print(hataCiktisi(x))
except listeHatası as hata1:  
    print(hata1)
except: 
    print("diger hata")
    
        