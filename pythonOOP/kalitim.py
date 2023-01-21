class Person:
    def __init__(self,fname,lname,number):
        self.firstname=fname
        self.lastname=lname
        self.studentNumber=number
        print('Person Created')
        
    def who_am_i(self):
        print('I am a person')
        
    def sayHello(self):
        print("Hello I am a student")
    def eat(self):
        print('I am eating')

class Student(Person):
    def _init_(self,fname,lname,number):
        Person._init_(self,fname,lname)
        print('Student Created')
        
class Teacher(Person):
    def _init_(self,fname,lname):
        Person()._init_(fname,lname)
        self.branch=branch
    
    def who_am_i(self):
        print('I am a {self.branch} Teacher')

p1= Person("Ali","Yılmaz",13)
s1=Student("Çınar","Turan",1256)
t1=Teacher("Serkan","Yılmaz","Math")
t1.who_am_i()
print(p1.firstname+' '+p1.lastname)
print(s1.firstname+' '+s1.lastname+' '+str(p1.studentNumber))
p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()