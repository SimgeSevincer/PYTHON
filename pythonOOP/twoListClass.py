class Numbers:
    def __init__(self):
        self.number0=[]
        self.number1=[]
    def append0(self,element0):
        self.number0.append(element0)
    def append1(self,element1):
        self.number1.append(element1)
    def total0(self):
        total=0
        for item in self.number0:
            total+=item
        return total
    def total1(self):
        total=0 
        for item in self.number1:
            total+=item
        return total
    def compare(self):
        if(self.number0==self.number1):
            print("(",self.number0,") & (",self.number1,") are equal ")
        else:
            print("(",self.number0,") & (",self.number1,") are not equal")
    def display0(self):
        return self.number0
    def display1(self):
        return self.number1
number=Numbers()
menu=1 
while(menu!=0):
    print("0:exit//1:append//2:print sums//3:compare")
    choose=int(input("enter a choice=> "))
    if(choose==0):
        print("exit")
        menu=0 
    if(choose==1):
        index=int(input("index(0 or 1)=>"))
        if(index==0):
            element=int(input("enter a value=>"))
            number.append0(element)
        if(index==1):
            element=int(input("enter a value=>"))
            number.append1(element)
    if(choose==2):
        print("Total(",number.display0(),") = ",number.total0())
        print("Total(",number.display1(),") = ",number.total1())
    if(choose==3):
        number.compare()

            