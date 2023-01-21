# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 12:09:50 2022

@author: Simge SEVİNCER
"""

class Kisi:
    def __init__(self,isim):        
        self.__isim=isim
    
    def getİsim(self):
        return self.__isim
k1=Kisi("simge")
print(k1.getİsim())

class Banka:
    
    def __init__(self,bakiye,para):
        self.__bakiye=bakiye
        self.__para=para
        
    def paraYatır(self):
        self.__bakiye+=self.__para
        return self.__bakiye
    def paraÇek(self):
        if(self.__bakiye>self.__para):
            self.__bakiye-=self.__para
            return self.__bakiye
        else:
            return "Yetersiz Bakiye..."
        
    def bakiyeKontrol(self):
        return self.__bakiye

b1=Banka(1000,200)
print(b1.paraYatır())
print(b1.paraÇek())
print(b1.bakiyeKontrol())


class Daire:
    pi=3.14
    def __init__(self,yarıcap):
        self.__yarıcap=yarıcap
    
    def setYarıcap(self,yarıcap):
        self.__yarıcap=yarıcap
        
    def getYarıcap(self):
        return self.__yarıcap
    
    def getAlan(self):
        return self.pi*self.__yarıcap**self.__yarıcap
    
    def __add__(self,DigerYarıcap):#overload
        return Daire(self.__yarıcap+DigerYarıcap.__yarıcap)
    
d1=Daire(4)
d1.setYarıcap(4)
print(d1.getYarıcap())
print(Daire)#<class '__main__.Daire'>
print(Daire(4))#<__main__.Daire object at ADRES>
d2=Daire(5)
d3=d1+d2
print(d3.getYarıcap())



class Taşıt:
    
    def __init__(self,isim,renk):
        self.__isim=isim
        self.__renk=renk
        
    def setRenk(self,renk):
        self.__renk=renk
    
    def getRenk(self):
        return self.__renk
    
    def setİsim(self,isim):
        self.__isim=isim
        
    def getİsim(self):
        return self.__isim
    
class Araba(Taşıt):#kalıtım(inheritance)
    def __init__(self,isim,renk,model):
        super().__init__(isim,renk)#poliformanizm
        self.__model=model
        
    def setModel(self,model):
        self.__model=model
    
    def getBilgi(self):
        return "İsim=",self.getİsim(),"Renk=",self.getRenk(),"Model",self.__model

a1=Araba("Opel","White","Corsa")
print(a1.getBilgi())

#ÇOKLU MİRAS
class SuperClass1:
    def method_super1(self):
        print("super1 methodu çağrıldı")

class SuperClass2:
    def method_super2(self):
        print("super2 methodu çağrıldı")

class ChildClass(SuperClass1,SuperClass2):
    
    def childMethod(self):
        print("child method")
        
nesne=ChildClass()
nesne.method_super2()
nesne.childMethod()




print("------------------------------------------")


class LogAnalysis:
    
    def __init__(self,fileName):
        self.__f=open(fileName,encoding="utf-8")
        self.__d1={}
        self.__d2={}
        self.__d3={}
        self.__d4={}
        
        
    def setIp(self):
        self.__f.seek(0)
        for line in self.__f:
            line=line.strip()
            line=line.split(",")[0]
            if line.count(".") == 3:
                if line in self.__d1.keys():
                    self.__d1[line]+=1
                else:
                    self.__d1[line]=1
    
    
    def setDay(self):
        self.__f.seek(0)
        for line in self.__f:
            line=line.strip()
            line=line.split(",")[1]
            line=line.split(":")[0]
            if line in self.__d2.keys():
                self.__d2[line]+=1
            else:
                self.__d2[line]=1     
            
            
    def setClock(self):
        self.__f.seek(0)
        for line in self.__f:
            line=line.strip()
            line=line.split(":")[1]
            line=int(line)
            if(line<8):
                self.__d3[line]+=1
            elif(line<12):
                 self.__d3[line]+=1
            elif(line<17):
                self.__d3[line]+=1
            elif(line<21):
                 self.__d3[line]+=1
            elif(line<24):
                 self.__d3[line]+=1
                 
                 
    def setURL(self):
        self.__f.seek(0)
        for line in self.__f:
            line=line.strip()
            line=line.split("/")[3]
            if line in self.__d4.keys():
                self.__d4[line]+=1
            else:
                self.__d4[line]=1
                
      
    def getIp(self):
        print(self.__d1)
        
        
    def getDay(self):
        print(self.__d2)
    
    
    def getClock(self):
        print(self.__d3)
        
        
    def getURL(self):
        print(self.__d4)
    
    def closeFile(self):
        self.__f.close()


log=LogAnalysis("web_log.txt")
log.setIp()
log.getIp()
log.setDay()
log.getDay()
"""
log.setClock()
log.getClock()

log.setURL()
log.getURL()
"""

print("------------------------------------------")


class Liste:
    
    def __init__(self,fileName):
        self.__f=open(fileName,encoding="utf-8",mode="w")
        self.__liste=[]
        
    def setListe(self,liste):
        self.__liste=liste
    def setFile(self):
        i=0
        for i in self.__liste:
            self.__f.write(str(self.__liste[i])+"\n")
            i+=1
    def getFile(self,fileName):
        self.__f=open(fileName,encoding="utf-8",mode="r")
        for line in self.__f:
            print(line)

file=Liste("file.txt")
file.setListe(list([0,1,2,3,4,5]))
file.setFile()
file.getFile("file.txt")
























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    