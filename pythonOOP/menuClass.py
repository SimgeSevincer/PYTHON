class Value:
    def __init__(self):
        self.value=[]
    def append(self,element):
        self.value.append(element)
    def __str__(self):
        return self.value
v1=Value()
menu=1 

while(menu==1):
    print("0:exit//1:append//2:display")
    item=int(input("enter a choose=>"))
    if(item==0):
        print("exit")
        menu=0
    if(item==1):
        element=input("enter a value=>")
        v1.append(element)
    if(item==2):
        print(v1.__str__())