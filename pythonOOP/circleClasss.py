class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return self.pi*self.radius*self.radius
    def circumference(self):
        return 2*self.pi*self.radius
    def __str__(self):
        return ("area=",self.area(),"circumference=",self.circumference())
rds1=int(input("radius1=> "))
rds2=int(input("radius2=> "))
r1=Circle(rds1)
r2=Circle(rds2)
f=open("circle.txt","w")
f.write("3.5")
f=open("circle.txt","r")
rds3=f.read()
rds3=float(rds3)
r3=Circle(rds3)
print("First Circle=>",r1.__str__())
print("Second Circle=>",r2.__str__())
print("Third Circle=>",r3.__str__())
circle=[]
circle.append(rds1)
circle.append(rds2)
circle.append(rds3)
for i in range(3):
    print(circle[i])

