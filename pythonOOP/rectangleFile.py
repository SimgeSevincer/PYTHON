f=open("rectangle.txt","a")
list=[]
f=open("rectangle.txt","r")
for line in f:
    list.append(line)
a=int(list[0])
b=int(list[1])
for i in range(2):
    if(a>b):
        high=a
        width=b
    else:
        high=b
        width=a
area=high*width
print("Area=",area)