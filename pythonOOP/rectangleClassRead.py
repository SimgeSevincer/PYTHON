class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def calculate_area(self):
        return self.height*self.width
f=open("rectangle.txt","r")
list=[]
for line in f:
    list.append(line)
h=int(list[0])
w=int(list[1])
r1=Rectangle(h,w)
print(r1.calculate_area())
f.close()