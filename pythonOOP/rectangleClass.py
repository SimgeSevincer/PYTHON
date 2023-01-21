class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def calculate_area(self):
        return self.height*self.width
h=int(input("height=>"))
w=int(input("width=> "))
r1=Rectangle(h,w)
h=int(input("height=>"))
w=int(input("width=> "))
r2=Rectangle(h,w)
f=open("rectangle.txt","w")
f.write(str(r1.calculate_area())+"\n")
f.write(str(r2.calculate_area()))
f.close()