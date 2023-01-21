def add():
    list=[]
    for number in range(2):
        x=int(input("x=> "))
        list.append(x)
    return(list)
list=add()
f=open("list.txt","w")
for item in list:
    f.write(str(item))
    f.write("\n")
f=open("list.txt","r")
for x in f:
  print(x)
f.close()