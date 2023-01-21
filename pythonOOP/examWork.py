'''
x=int(input("enter a number"))
y=int(input("enter a number"))
if(x>y):
    print(x,"is greater than",y)
elif(y>x):
    print(y,"is greater than",x)
else:
    print(x,"is equal with",y)
'''
'''
y=0
x=5
loopnumber=1
while(x>y):
    print("[",loopnumber,"]")
    print("x=",x)
    print("y=",y)
    y+=1
    loopnumber+=1
'''
'''
def greater(x,y):
    if(x>y):
        return(x,"is greater",y)
    elif(y>x):
        return(y,"is greater",x)
    else:
        return(x,"and",y,"is equal")
print(greater(5,13))
'''
'''
def greater(x,y):
    if(x>y):
        return(chr(x))
    else:
        return(chr(y))
def display(bigger):
    if(x>y):
        return(chr(x),"is greater",chr(y))
    else:
        return(chr(y),"is greater",chr(x))
x=ord(input("enter a char->"))
y=ord(input("enter a char=>"))
bigger=greater(x,y)
print(display(bigger))
'''
'''
def appendList():
    listt=[]
    for item in range(2):
        listt.append(int(input("enter a number")))
    return listt
def sumList(result):
    total=0
    for item in result:
        total+=item
    return total
def display(result):
    print(result)
result=appendList()
summ=sumList(result)
print(summ)
display(result)
'''
'''
def appendList():
    listt=[]
    for item in range(3):
        listt.append(input("enter a number->"))
    return listt
result=appendList()
f=open("listt.txt","w")
for item in result:
    f.write(item)
    f.write("\n")
f=open("listt.txt","r")
for line in f:
    print(line)
'''
'''
def enterTxt():
    f=open("read.txt","w")
    for item in range(3):
        f.write(input("enter a thing->"))
        f.write("\n")
def readTxt():
    listt=[]
    f=open("read.txt","r")
    for line in f:
        line=line.rstrip("\n")
        listt.append(line)
    return listt
enterTxt()
print(readTxt())
'''
'''
f=open("rectangle.txt","w")
f.write("3.5\n4.5")
listt=[]
f=open("rectangle.txt","r")
for line in f:
    line=line.rstrip("\n")
    line=float(line)
    listt.append(line)
rectangleArea=listt[0]*listt[1]
print("area=",rectangleArea)
'''
'''
class Rectangle:
    def __init__(self,heigth,width):
        self.heigth=heigth
        self.width=width
    def area(self):
        return self.heigth*self.width
x=float(input("enter a heigth->"))
y=float(input("enter a width->"))
a1=Rectangle(x,y)
print(a1.area())
'''
'''
class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def area(self):
        return self.height*self.width
f=open("rec.txt","w")
f.write("3.5\n4.5")
f=open("rec.txt","r")
listt=[]
for line in f:
    line=line.rstrip("\n")
    line=float(line)
    listt.append(line)
a1=Rectangle(listt[0],listt[1])
print(a1.area())
'''
'''
class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return self.pi*self.radius**2
    def circumference(self):
        return 2*self.pi*self.radius
    def __str__(self):
        return("area:",self.area(),"circumference:",self.circumference())

f=open("value.txt","w")
f.write("3.5")
f=open("value.txt","r")
for line in f:
    x=line
x=float(x)
c1=Circle(x)
print(c1.__str__())
'''
'''
class Number:
    def __init__(self):
        self.value=[]
    def append(self,element):
        self.value.append(element)
    def total(self):
        total=0
        for item in self.value:
            item=int(item)
            total+=item
        return total
    def __str__(self):
        return self.value
v1=Number()
menu=1
while(menu!=0):
    print("0:exit//1:append//2:display//3:totalsum")
    choose=int(input("enter a choice->"))
    if(choose==0):
        print("exit")
        menu=0
    if(choose==1):
        element=input("enter a element")
        v1.append(element)
    if(choose==2):
        print(v1.__str__())
    if(choose==3):
        print(v1.total())
'''
'''
class Value:
    def __init__(self):
        self.value=[]
    def append(self,element):
        self.value.append(element)
    def __str__(self):
        return self.value
f=open("value.txt","w")
f.write("10\n20\n30\n40")
v1=Value()
f=open("value.txt","r")
for line in f:
    line=line.rstrip("\n")
    v1.append(line)
print(v1.__str__())
'''
















































































