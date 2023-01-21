# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 22:41:28 2022

@author: Simge SEVİNCER
"""

f=open("simgos.txt",encoding="utf-8")
print(f.readlines())

f=open("simgos.txt",encoding="utf-8",mode="a")#a da silinme olmaz
f.write("\nseni seviyorum")
f.flush()
f.close()

ogrencilerr=["simge sevincer","ufuk sevincer","mertcan alkan"]
f=open("ogrencilerr.txt",encoding="utf-8",mode="w")# wde silinme olur.
for o in ogrencilerr:
        f.write(o+'\n')
        
f.close()

f=open("liste.txt",encoding="utf-8",mode="r")

liste=[]
for line in f:
    liste.append(line)
    
print(liste)