def add():
    list=[]
    for i in range(2):
        x=int(input("x=> "))
        list.append(x)
list=[]
add()
f=open("list.txt","a")
for item in list:
    print(item)
    f.write(item)
f=open("list.txt","r")
for x in f:
  print(x)
f.close()

