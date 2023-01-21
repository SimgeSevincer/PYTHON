class Course:
    def __init__(self):
        self.course=[]
    def append(self,coursee):
        self.course.append(coursee)
class Student:
    def __init__(self):
        self.student=[]
    def append(self,studentt):
        self.student.append(studentt)
class Enroll:
    def __init__(self):
        self.listt=[]
    def addCourse(self,add):
        self.listt.append(add)
    def frecord(self):
        f=open("enroll.txt","w")
        for item in self.listt:
            f.write(item+"\n")
    def __str__(self):
        return self.listt
f1=open("student.txt","w")
f1.write("01 Simge\n02 Ufuk\n03 Gülüzar\n04 Muharrem")
studentt=[]
f1=open("student.txt","r")
for i in f1:
    i=i.rstrip("\n")
    studentt.append(i)
f2=open("courses.txt","w")
f2.write("CE0 JAVA\nCE1 PYTHON\nCE3 SWİFT")
coursse=[]
f2=open("courses.txt","r")
for x in f2:
    x=x.rstrip("\n")
    coursse.append(x)
c1=Course()
s1=Student()
e1=Enroll()
for line in f2:
    line=line.rstrip("\n")
    c1.append(line)
for linee in f1:
    linee=linee.rstrip("\n")
    s1.append(linee)
for item in range(4):
    print("for java:0//for python:1//for swift:2")
    print("for",item+1,".student")
    lesson=int(input("lesson=>"))
    a=studentt[item]+" "+coursse[lesson]
    print(a)
    e1.addCourse(a)
e1.frecord()
print(e1.__str__())
            
            
        

    

