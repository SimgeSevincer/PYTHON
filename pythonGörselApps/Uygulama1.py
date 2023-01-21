# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 12:51:17 2022

@author: umitozturk
"""



class LogAnalysis():
    
    def __init__ (self, filename):
        self.__ipaccess = {}
        self.__dayaccess = {}
        self.__clockgroupaccess = {}
        self.__file = open (filename, encoding="utf-8" )
# ip: spesifik ip numarası
# ip_access: ip erişim sayısı 

       
        
    def closeFile (self):
        self.__file = self.__file.close()
        
        
    def setDataforIpaccess (self): # sunucuya hangi IP kaç defa erişim sağladı?
        self.__file.seek(0)
        for l in self.__file:
           ls = l.strip()
           ll = ls.split(",")[0]
           if ll.count(".") == 3:
               if ll in self.__ipaccess.keys():
                   self.__ipaccess[ll] += 1
               else:
                   self.__ipaccess[ll] = 1
        
                


    def setDataforDayaccess (self): # sunucuya hangi gün ne kadar erişildi ?
        self.__file.seek(0)
        for l in self.__file:
           ls = l.strip()
           ll = ls.split(",")[1]
           if ll.startswith('['):
               lm = ll[1:].split(":")[0]
               if lm in self.__dayaccess.keys():
                   self.__dayaccess[lm] += 1
               else:
                   self.__dayaccess[lm] = 1          

                
                
    def setDataforClockgroupAccess (self): # sunucuya '08:00-11:59','12:00-16:59','17:00-20:59', '21:00-23:59', '00.00-07:59' saat aralıklarında erişim sayısı nedir?
        self.__file.seek(0)
        clock_groups = ['08:00-11:59','12:00-16:59','17:00-20:59', '21:00-23:59', '00.00-07:59']
        for l in self.__file:
           ls = l.strip()
           ll = ls.split(",")[1]
           if ll.startswith('['):
               if ((int (ll[1:].split(":")[1]) < 8)):
                   
                   if clock_groups[4] in self.__clockgroupaccess.keys():
                       self.__clockgroupaccess[clock_groups[4]] += 1
                   else:
                       self.__clockgroupaccess[clock_groups[4]] = 1
                   
               elif ((int (ll[1:].split(":")[1]) < 12)):
                  
                   if clock_groups[0] in self.__clockgroupaccess.keys():
                       self.__clockgroupaccess[clock_groups[0]] += 1
                   else:
                       self.__clockgroupaccess[clock_groups[0]] = 1     
                   
               elif ((int (ll[1:].split(":")[1]) < 17)):
                 
                   if clock_groups[1] in self.__clockgroupaccess.keys():
                       self.__clockgroupaccess[clock_groups[1]] += 1
                   else:
                       self.__clockgroupaccess[clock_groups[1]] = 1     
                   
               elif ((int(ll[1:].split(":")[1]) < 21)):
                  
                   if clock_groups[2] in self.__clockgroupaccess.keys():
                       self.__clockgroupaccess[clock_groups[2]] += 1
                   else:
                       self.__clockgroupaccess[clock_groups[2]] = 1     
                   
               elif ((int(ll[1:].split(":")[1]) < 24)):
                  
                   if clock_groups[3] in self.__clockgroupaccess.keys():
                       self.__clockgroupaccess[clock_groups[3]] += 1
                   else:
                       self.__clockgroupaccess[clock_groups[3]] = 1     
                   


    def getIpaccess (self):
        return self.__ipaccess
    
    def getDayaccess (self):
        return self.__dayaccess
    
    
    def getClockgroupAccess (self):
        return self.__clockgroupaccess
    
    
    
# Ödev !!! web_log file içerisinde Hangi url' e kaç erişim olduğunu 
# yukarıdaki yaklaşıma benzer şekilde dictionary veri yapısında hazırlayınız.           
     

log = LogAnalysis("web_log.txt") 
          
log.setDataforIpaccess()  
log.setDataforDayaccess()
log.setDataforClockgroupAccess()     

print (log.getIpaccess()) 
print ("-----------------------------------------")  
print (log.getDayaccess())   
print ("-----------------------------------------")      
print (log.getClockgroupAccess())
print ("-----------------------------------------") 
log.closeFile()





