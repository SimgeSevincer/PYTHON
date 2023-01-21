class Circle:
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
    def area(self):
        return self.pi*self.radius*self.radius
    def circumference(self):
        return 2*self.pi*self.radius
    def __str__(self):
        return ("area=",self.area(),"circumference=",self.circumference())
c1=Circle()
print(c1.__str__())