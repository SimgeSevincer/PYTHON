class Numbers:
    def __init__(self):
        self.value=[]
    def append(self,element):
        self.value.append(element)
    def total(self):
        totall=0
        for item in self.value:
            totall=totall+item
        print("total=",totall)
    def __str__(self):
        return self.value
value=Numbers()
menu=1
while(menu!=0):
    print("0:exit//1:append//2:display//3:total")
    choose=int(input("enter your choice=> "))
    if(choose==0):
        print("exit")
        menu=0
    if(choose==1):
        element=int(input("enter a value=> "))
        value.append(element)
    if(choose==2):
        print(value.__str__())
    if(choose==3):
        value.total()

